#!/usr/bin/env python3
"""Complete exterior first-correction old-circle sources from exact accepted stages.

Only new same-order matrix conversions, source-amplitude products and radial
source integrals are computed. All original coefficients, Fourier fields,
folds, first-correction derivatives, local numerators and true seams are reused.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_inner_first_Airy_complete_sources as inner

PUBLIC="Rogerhu12/math-research-public"
EXT_RUN="43657793725"
EXT_SOURCE="e196557e61aa9b83249654a1a81ca3a003ca38e1e07f4ff4fdb19a877f86f4df"
INNER_NATIVE="6b5e6c646f02b48d82f25e12a41b329e7ab71d649b39d29c1608ef03a1fd847e"
INNER_SOURCE="0b0dc7b3b5c747dd8935f77c75554c60f2b08fd40a6cf5dd27c7c81f5c945fbf"
ROOT="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
DIRECTED=inner.DIRECTED
DPROC=inner.DPROC
NORM=inner.NORM
SEAM="871aa54de8c4ee1caa47cdab39c8033bb9cd02e9d4d1f404b711ab8c28825642"
DELTA=Q(1,10**8)
H=Q(9,10**6)
SIGMA=Q(1,512)
CUTOFF=97
RADII=(Q(1,1000),Q(1,500),Q(1,200),Q(1,100),Q(3,200),Q(1,50))
WORD_NAMES=inner.WORD_NAMES
TERM_NAMES=inner.TERM_NAMES
sha=inner.sha
payload_sha=inner.payload_sha
read=inner.read
ex=inner.ex
box=inner.box
up=inner.up
record=inner.record
encode=inner.encode
decode=inner.decode
powr=inner.powr
ipow=inner.ipow
ensure_nonnegative=inner.ensure_nonnegative

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,compresslevel=6 if value.get("complete") else 1,mtime=0)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)

def receipt(path,base):
    return dict(file=str(path.relative_to(base)),bytes=path.stat().st_size,sha256=sha(path))

def checked_stage(base,entry):
    path=base/entry["file"]
    if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
        raise ValueError("an original complete natural stage changed: "+entry["file"])
    return read(path)

def complete_profile(extcase,rootcase,seamcase,roots,inner_profile_payload):
    """New p=1/6 same-order costs on the already complete real fold."""
    radius=Q(extcase["exact_radius"]);R=ex(radius+roots[1]-roots[0])
    if radius!=Q(rootcase["exact_radius"]) or radius!=Q(seamcase["exact_radius"]):
        raise ValueError("different completed real fold radii were paired")
    vals=decode(rootcase["bounds"]);af=seamcase["actual_forcing"]
    if not (rootcase["passed"] and af["leading_strip"]=="3/64"
        and af["output_strip"]=="1/64" and SIGMA<Q(1,64)):
        raise ValueError("the original complete amplitude strips are unavailable")
    Am=vals["A_lower"].lower();Ap=up(vals["A_upper"]);ap=up(vals["a_upper"])
    E=up(box(af["flow_variational_C"]["1"]));m=(2-E).lower()
    if not (R>0 and Am>0 and m>0):
        raise ValueError("the original real fold or inverse circle map lost its gap")
    A=[Ap]+[(R*up(box(af["A_angular_constants"][str(q)]))).upper() for q in range(1,4)]
    F2=(R*up(box(af["flow_variational_C"]["2"]))).upper()
    F3=(R*up(box(af["flow_variational_C"]["3"]))).upper()
    original=decode(extcase["original_complete_analytic_amplitude_numeric"])
    profiles=decode(extcase["original_radial_reference_profiles_numeric"])
    plus=inner.power_angular_jets(Q(1,3),Am,Ap,A)
    minus=inner.power_angular_jets(Q(-1,3),Am,Ap,A)
    PQ=[[[arb(0),(ap*R*plus[q]).upper()],
         [(ap*minus[q]).upper(),arb(0)]] for q in range(4)]
    L1=(ex(Q(2,3))*A[1]/Am).upper()
    L2=(ex(Q(2,3))*(A[2]/Am+A[1]*A[1]/(Am*Am))).upper()
    H0=powr(Am,Q(-1,6))
    N0=powr(R,Q(1,4))*powr(ex(4*CUTOFF),Q(-1,6))
    B0=powr(R,Q(1,2))*powr(Ap,Q(1,6))
    def sc(a,v):return [(a*x).upper() for x in v]
    negative=[
        [sc(H0,[16,94*L1,1208*L1*L1+94*L2]),sc(N0,[8,51*L1,650*L1*L1+51*L2])],
        [sc(H0,[3,16*L1,209*L1*L1+16*L2]),sc(B0,[4,22*L1,290*L1*L1+22*L2])],
        [sc(H0,[3,16*L1,209*L1*L1+16*L2]),sc(B0,[4,22*L1,290*L1*L1+22*L2])]]
    positive=[[sc(H0,[3,3*L1,5*L1*L1+3*L2]),sc(N0,[3,3*L1,6*L1*L1+3*L2])]]
    fixed=decode(inner_profile_payload["numeric"])
    fourier,fe=inner.complete_fourier((m*ex(SIGMA)).lower())
    numeric=dict(R=R,PQ=PQ,m=m,M=E,F2=F2,F3=F3,
        composition=original["composition"],fourier=fourier,
        near=fixed["near"],far=fixed["far"],analytic_profiles=profiles,
        real_negative=negative,real_positive=positive)
    if not ensure_nonnegative(numeric):
        raise ValueError("a new exterior same-order profile is nonfinite or negative")
    return dict(numeric=encode(numeric),complete_fourier_evidence=fe,
        exact_old_phi_width=str(SIGMA),exact_input_cutoff=CUTOFF,
        original_complete_analytic_payload_sha256=payload_sha(extcase["original_complete_analytic_amplitude_numeric"]),
        original_radial_reference_profiles_payload_sha256=payload_sha(extcase["original_radial_reference_profiles_numeric"]),
        original_phase_composition_recomputed=False,
        original_analytic_Airy_profiles_recomputed=False,
        original_universal_real_near_far_constants_recomputed=False,
        real_two_derivative_and_complex_strip_estimates_separate=True,
        original_complete_root_case_payload_sha256=payload_sha(rootcase),
        original_complete_refined_forcing_case_payload_sha256=payload_sha(seamcase),
        exact_PQ_top_right_identity="-a*rho*A^(1/3)",
        positive_estimate_only_for_the_original_decaying_Airy_columns=True)

def coefficient_views(accepted,real):
    """Never promote a real-circle derivative bound to a complex-strip norm."""
    analytic=dict(U=accepted["U"],V=accepted["V"],D=accepted["D"],em=accepted["eta_lower"])
    realview=dict(U=[real["U"]],V=[real["V"]],D=real["D"],em=real["eta_lower"])
    if min(len(analytic["U"][0]),len(analytic["V"][0]),len(analytic["D"]))<4:
        raise ValueError("an original complete complex coefficient jet is missing")
    if min(len(real["U"]),len(real["V"]),len(real["D"]))<4:
        raise ValueError("an original complete real coefficient jet is missing")
    if not (analytic["em"]>0 and realview["em"]>0):
        raise ValueError("the actual radial-scalar eta lower gap was lost")
    return realview,analytic

def source_amplitudes(row,accepted,real,p):
    if row["exact_amplitude_output_phi_width"]!=str(SIGMA):
        raise ValueError("an accepted first-correction derivative strip changed")
    vals=decode(row["first_amplitude_budgets"])
    for name in ("a1","b1"):
        if not (all("0,"+str(q) in vals[name]["strip_sup"] for q in range(4))
            and all("1,"+str(q) in vals[name]["strip_sup"] for q in range(3))):
            raise ValueError("the original complete first-correction derivative table is incomplete")
    rv,cv=coefficient_views(accepted,real)
    # The original positive-strip bounds also bound real amplitude derivatives.
    # Only real coefficients may then be sharpened by the independent saved real table.
    rj=inner.amplitude_jets(row,rv,p["PQ"])
    cj=inner.amplitude_jets(row,cv,p["PQ"])
    side=row["side"]
    operators={k:inner.Airy_bound(rj[k],cj[k][0],p,side) for k in rj}
    return dict(complete_operators=operators,
        complete_real_amplitude_jets=encode(rj),complete_complex_amplitude_jets=encode(cj),
        exact_complex_amplitude_width=str(SIGMA),
        exact_original_complex_coefficient_width="1/16",
        original_first_correction_derivative_payload_sha256=payload_sha(row["first_amplitude_budgets"]),
        all_carrier_signs_and_full_mean_retained=True,
        no_input_cutoff_factor_applied_to_density_one_sixth=True)

def nonlocal_constants(c,z,operators,oldlocal):
    """The complete Y.10--Y.12 words, including every independent old mean."""
    a={k:up(box(v["bound"])) for k,v in operators.items()}
    terms=dict(
        complete_SV=z["SV"]*a["w"],
        complete_SQ=z["SQ"]*a["h"],
        complete_RQ_J_gd=z["RQJ"]*a["gd"],
        complete_RQ_JL_h=z["RQJL"]*a["h"],
        complete_primitive_error=z["primitive"]*a["qv"],
        old_mean_rQ=c["m0_rQ"]*a["h"],
        old_mean_vphi=c["cB"]*c["V"][1]*a["y"],
        old_mean_raw_D=(c["cB"]*c["V"][1]*min(c["V"][0],c["V"][1]/4)/4+c["m0_T0"])*a["gd"],
        old_mean_V0=c["m0_V0"]*a["w"])
    terms={k:up(v) for k,v in terms.items()}
    means=dict(direct_u_h=a["uh"],complete_uJ_gd=z["uJ"]*a["gd"],
        complete_uJL_h=z["uJL"]*a["h"],complete_uJB_w=z["uJB"]*a["w"],
        complete_curvature_v_nonmean_w=c["K"]*a["vmw"])
    means={k:up(v) for k,v in means.items()}
    first=(c["C_J_scalar"]*sum(terms.values(),arb(0))).upper()
    mean=(c["exact_nonlocal_even_mean_row_factor"]*sum(means.values(),arb(0))).upper()
    local=up(box(oldlocal))
    squared=((first+local)*(first+local)+mean*mean).upper()
    if not ensure_nonnegative([first,mean,local,squared]):
        raise ValueError("a complete exterior source component is invalid")
    return dict(first_nonlocal_singular_envelope=record(first),
        independent_even_mean_singular_envelope=record(mean),
        original_first_local_singular_envelope=copy.deepcopy(oldlocal),
        complete_squared_vector_envelope=record(squared),
        complete_nine_nonlocal_terms=encode(terms),
        complete_five_independent_even_mean_terms=encode(means),
        final_old_J_Hminus5over3_to_Hminus2over3=record(c["C_J_scalar"]),
        independent_even_mean_factor=record(c["exact_nonlocal_even_mean_row_factor"]),
        original_local_unnormalized_numerator_recomputed=False,
        original_old_circle_mean_is_not_canonical_X_mean=True)

def copy_resume_stages(index_path,previous,out):
    import shutil
    entries=[]
    if previous.get("coefficient_stage"):entries.append(previous["coefficient_stage"])
    entries.extend(previous.get("case_stages",[]))
    for entry in entries:
        source=index_path.parent/entry["file"];target=out.parent/entry["file"]
        if not source.is_file() or sha(source)!=entry["sha256"] or source.stat().st_size!=entry["bytes"]:
            raise ValueError("an accepted complete exterior source prefix changed")
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():raise FileExistsError("a preserved prefix would overwrite another state")
        shutil.copyfile(source,target)

def summarize_case(case,source):
    totals={}
    for side in ("negative","positive"):
        rows=[v for v in case["rows"] if v["side"]==side]
        if not rows:raise ValueError("an actual exterior side is empty")
        sq=sum((up(box(v["complete_squared_source_integral"])) for v in rows),arb(0)).upper()
        components={}
        for key in ("first_nonlocal","independent_even_mean","original_first_local"):
            q=sum((up(box(v["separate_squared_source_integrals"][key])) for v in rows),arb(0)).upper()
            components[key]=record(q.sqrt().upper())
        terms={}
        for name in TERM_NAMES:
            q=sum((up(box(v["radial_weight_integral"]))*
                ipow(up(box(v["source_bounds"]["final_old_J_Hminus5over3_to_Hminus2over3"]))*
                     up(box(v["source_bounds"]["complete_nine_nonlocal_terms"][name])),2)
                for v in rows),arb(0)).upper()
            terms[name]=record(q.sqrt().upper())
        totals[side]=dict(complete_exterior_rows=len(rows),
            complete_first_correction_ordinary_L2_source=record(sq.sqrt().upper()),
            separate_component_L2_bounds=components,individual_first_row_nonlocal_L2_bounds=terms,
            complete_squared_source_integral=record(sq))
    gain=up(box(source["actual_negative_source_to_primitive_L2_gain"]))
    negative=up(box(totals["negative"]["complete_first_correction_ordinary_L2_source"]))
    return dict(exact_radius=case["exact_radius"],complete=True,
        exact_cover=source["exact_cover"],exact_inner_interval=source["exact_inner_interval"],
        complete_exterior_rows=len(case["rows"]),source_summary=totals,
        original_actual_negative_source_to_primitive_L2_gain=source["actual_negative_source_to_primitive_L2_gain"],
        negative_first_correction_source_component_Hminus4over3_to_primitive_L2=record((gain*negative).upper()),
        positive_collar_first_correction_source_L2=record(arb(0)),
        positive_body_first_correction_source_L2=totals["positive"]["complete_first_correction_ordinary_L2_source"],
        positive_weighted_port_conversion_claimed=False,
        independent_mean_included=True,original_physical_seam_sources_separate=True,
        whole_first_corrected_strong_return_or_cutoff97_inverse_claimed=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","prepared","out"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new complete source mathematics runs only in public Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),
        flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):
        raise RuntimeError("the exact original scalar interval runtime changed")
    if args.out.exists():raise FileExistsError("preserve every accepted or failed source prefix")
    ctx.prec=320;start=time.monotonic()
    doc=dict(kind="complete_strict_exterior_first_Airy_old_circle_and_independent_mean_sources",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        complete=False,proved=False,failure=None,gates=[],runtime=runtime,
        source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),
        original_exterior_run_id=EXT_RUN,original_exterior_source_sha256=EXT_SOURCE,
        original_inner_native_sha256=INNER_NATIVE,original_inner_source_sha256=INNER_SOURCE,
        original_complete_root_native_sha256=ROOT,original_complete_directed_native_sha256=DIRECTED,
        original_complete_moment_native_sha256=NORM,original_complete_seam_native_sha256=SEAM,
        fixed_intrinsic_parameter="eta_0",exact_real_delta_radius=str(DELTA),
        exact_complete_inner_radius=str(H),input_cutoff=CUTOFF,physical_frequency="4 abs(j)",
        actual_first_correction_density="n^(1/6)",
        source_window="H^-4/3 input -> ordinary radial L2 (H^-2/3 pair); second row is independent even mean",
        original_target_FFT_intrinsic_coefficient_fold_ray_Taylor_and_derivative_stages_recomputed=0,
        original_complete_matrix_words_recomputed=0,original_exterior_local_sources_recomputed=0,
        original_complete_six_analytic_profiles_recomputed=0,original_physical_seams_recomputed=0,
        new_same_order_matrix_conversions=0,reused_new_same_order_matrix_conversions=0,
        reused_inner_same_order_matrix_conversions=0,
        new_complete_profiles=0,reused_complete_profiles=0,
        new_complete_source_rows=0,reused_complete_source_rows=0,
        coefficient_stage=None,case_stages=[],cases=[],
        all_fourier_outputs_old_projections_and_independent_mean_retained=True,
        artificial_interface_source_introduced=False,
        complete_first_corrected_trial_seam_sources_paid=False,
        positive_weighted_port_conversion_claimed=False,
        full_high_feedback_strong_return_cutoff97_inverse_or_PDE_branch_claimed=False)
    def gate(name,test):
        passed=bool(test);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("complete exterior source gate failed: "+name)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(args.out,doc)
    def saved(path,value):
        save(path,value);return receipt(path,args.out.parent)
    try:
        manifest=read(args.manifest)
        gate("this immutable manifest describes the complete exterior source consumer",
            manifest["public_repository"]==PUBLIC and
            manifest["mathematical_parameters"]["exact_inner_radius"]==str(H)
            and manifest["mathematical_parameters"]["input_cutoff"]==CUTOFF
            and manifest["mathematical_parameters"]["new_phi_width"]==str(SIGMA))
        for entry in manifest["files"]:
            path=args.repo_root/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a complete pinned scientific input changed: "+entry["path"])
        paths={k:args.repo_root/v for k,v in manifest["input_paths"].items()}
        external={x["name"]:args.prepared/x["prepared_path"] for x in manifest["external_completed_natives"]}
        for entry in manifest["external_completed_natives"]:
            path=external[entry["name"]]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("an exact original complete artifact file changed")
        ext=read(paths["exterior_index"]);ep=read(paths["exterior_process"])
        root=read(external["root"]);directed=read(external["directed"])
        norm,seam,inn,ip,dp=[read(paths[k]) for k in
            ("moment_native","seam_native","inner_native","inner_process","directed_process")]
        gate("the exact successful exterior source and actual zero-return receipt remain complete",
            str(ext["run_id"])==str(ep["run_id"])==EXT_RUN
            and ext["source_sha256"]==ep["mathematical_source_sha256"]==EXT_SOURCE
            and ep["actual_returncode"]==0 and ep["mathematical_complete"] and ep["mathematical_proved"]
            and ep["mathematical_failure"] is None and ep["native_sha256"]==sha(paths["exterior_index"])
            and ep["native_bytes"]==paths["exterior_index"].stat().st_size
            and ext["complete"] and ext["proved"] and ext["failure"] is None
            and len(ext["case_stages"])==len(ext["cases"])==6
            and ext["gates"]==ep["mathematical_gates"] and all(g["passed"] for g in ext["gates"]))
        doc["original_exterior_native_sha256"]=sha(paths["exterior_index"])
        doc["original_exterior_process_sha256"]=sha(paths["exterior_process"])
        doc["original_exterior_manifest_sha256"]=ext["input_manifest_sha256"]
        gate("the complete original root directed moment and seam objects retain their exact bytes",
            sha(external["root"])==ROOT and sha(external["directed"])==DIRECTED
            and sha(paths["moment_native"])==NORM and sha(paths["seam_native"])==SEAM
            and sha(paths["directed_process"])==DPROC
            and all(v["complete"] and v["proved"] and v["failure"] is None
                and v["gates"] and all(g["passed"] for g in v["gates"])
                for v in (root,directed,norm,seam))
            and directed["source_sha256"]==inner.DSOURCE
            and directed["input_manifest_sha256"]==inner.DMANIFEST
            and dp["actual_returncode"]==0 and dp["native_sha256"]==DIRECTED
            and dp["mathematical_gates"]==directed["gates"])
        gate("the original successful inner source retains all17 gates and four complete matrix conversions",
            sha(paths["inner_native"])==INNER_NATIVE
            and inn["source_sha256"]==ip["mathematical_source_sha256"]==INNER_SOURCE
            and inn["complete"] and inn["proved"] and inn["failure"] is None
            and ip["actual_returncode"]==0 and ip["native_sha256"]==INNER_NATIVE
            and len(inn["gates"])==17 and all(g["passed"] for g in inn["gates"])
            and ip["mathematical_gates"]==inn["gates"]
            and len(inn["matrix_conversions"])==4 and inn["new_stages"]==0
            and inn["reused_stages"]==2)
        roots=list(map(Q,ext["exact_root_interval"]));rl,ru=roots
        gate("the fixed eta0 full real delta family and exact inner physical interval remain identical",
            ext["actual_intrinsic_parameter"]==inn["fixed_intrinsic_parameter"]=="eta_0"
            and Q(ext["exact_real_delta_radius"])==Q(inn["exact_real_delta_radius"])==DELTA
            and root["exact_root_interval"]==ext["exact_root_interval"]==inn["exact_root_interval"]
                ==directed["exact_root_interval"]
            and ext["exact_physical_inner_interval"]==inn["exact_physical_inner_interval"]
                ==[str(rl-H),str(ru+H)]
            and ext["background_definition_sha256"]==root["background_definition_sha256"]==inner.BASE
            and ext["explicit_direction_definition_sha256"]==root["explicit_direction_definition_sha256"]==inner.ZDEF)
        coefficient=checked_stage(paths["exterior_index"].parent,ext["coefficient_stage"])
        nr=norm["coefficient_rows"];dr=directed["coefficient_rows"];cr=coefficient["rows"]
        gate("all1328 derivative moment and full directed rows share the same original intervals",
            coefficient["complete"] and coefficient["source_sha256"]==EXT_SOURCE
            and coefficient["input_manifest_sha256"]==ext["input_manifest_sha256"]
            and len(cr)==len(nr)==len(dr)==1328
            and all(c["common_row"]==n["common_row"]==d["common_row"]==i
                and c["interval"]==n["interval"]==d["interval"]
                and c["original_root_row"]==n["original_root_row"]==d["original_root_row"]
                and d["original_completed_moment_row"]==i
                and len(d["complete_width_evidence"])==3 for i,(c,n,d) in enumerate(zip(cr,nr,dr)))
            and all(a["interval"][1]==b["interval"][0] for a,b in zip(cr,cr[1:])))
        gate("every inherited inner matrix conversion is the original complete same-order word",
            all(value["original_coefficient_row_payload_sha256"]==payload_sha(dr[int(k)])
                and value["conversion"]=="kappa_5over3 times z, not right_gain"
                and set(value["costs"])==set(WORD_NAMES) for k,value in inn["matrix_conversions"].items()))
        stage=inn["stages"]["new-inner-Airy-profile-and-exact-PQ-jets"]
        gate("only the unchanged universal near and far constants are reused from the complete inner stage",
            stage["complete"] and stage["payload_sha256"]==payload_sha(stage["payload"])
            and inn["input_cutoff"]==CUTOFF and inn["physical_frequency"]=="4|j|")
        innerprofile=stage["payload"]
        doc.update(exact_root_interval=ext["exact_root_interval"],
            exact_physical_inner_interval=ext["exact_physical_inner_interval"],
            exact_cover=ext["exact_cover"],fixed_positive_body_cut=ext["fixed_positive_body_cut"],
            original_all1328_coefficient_identities_verified=True,
            original_complete_directed_table_payload_sha256=payload_sha(dr),
            original_complete_derivative_table_payload_sha256=payload_sha(cr),
            original_exterior_natural_stage_receipts=copy.deepcopy([ext["coefficient_stage"],*ext["case_stages"]]))
        if args.resume:
            previous=read(args.resume)
            keys=("public_repository","source_sha256","input_manifest_sha256","runtime",
                "original_exterior_native_sha256","original_exterior_process_sha256",
                "original_exterior_source_sha256","original_exterior_manifest_sha256",
                "original_inner_native_sha256","original_complete_root_native_sha256",
                "original_complete_directed_native_sha256","original_complete_moment_native_sha256",
                "original_complete_seam_native_sha256","exact_root_interval","exact_physical_inner_interval")
            gate("every accepted new prefix has the exact same source runtime manifest and completed inputs",
                all(previous.get(k)==doc.get(k) for k in keys))
            copy_resume_stages(args.resume,previous,args.out)
            doc["coefficient_stage"]=copy.deepcopy(previous.get("coefficient_stage"))
            doc["case_stages"]=copy.deepcopy(previous.get("case_stages",[]))
            doc["cases"]=copy.deepcopy(previous.get("cases",[]))
            doc["preserved_actual_prefix"]=dict(native_sha256=sha(args.resume),
                native_bytes=args.resume.stat().st_size,complete=previous["complete"],
                proved=previous["proved"],failure=previous["failure"],
                original_gates=previous["gates"])
        checkpoint()
        cp=args.out.parent/"coefficients"/"complete-same-order-matrix-conversions.json.gz"
        if doc["coefficient_stage"]:
            converted=checked_stage(args.out.parent,doc["coefficient_stage"])
            if converted["source_sha256"]!=sha(__file__) or converted["input_manifest_sha256"]!=sha(args.manifest):
                raise ValueError("a resumed new matrix conversion table changed identity")
        else:
            converted=dict(kind="complete_same_order_exterior_matrix_conversions",
                source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),
                complete=False,rows=[])
        prefix=len(converted["rows"])
        if prefix>1328:raise ValueError("a completed conversion prefix exceeds the complete coefficient cover")
        doc["reused_new_same_order_matrix_conversions"]=prefix
        for idx,row in enumerate(dr):
            identity=dict(common_row=idx,interval=row["interval"],
                original_root_row=row["original_root_row"],
                original_moment_row_payload_sha256=payload_sha(nr[idx]),
                original_complete_directed_row_payload_sha256=payload_sha(row))
            if idx<prefix:
                old=converted["rows"][idx]
                if any(old[k]!=v for k,v in identity.items()):
                    raise ValueError("an accepted conversion row changed its original identity")
                continue
            doc["last_attempted_matrix_row"]=idx
            key=str(idx)
            if key in inn["matrix_conversions"]:
                value=copy.deepcopy(inn["matrix_conversions"][key])
                inherited=True;doc["reused_inner_same_order_matrix_conversions"]+=1
            else:
                value=inner.matrix_conversion(row)
                inherited=False;doc["new_same_order_matrix_conversions"]+=1
            converted["rows"].append(dict(**identity,matrix_conversion=value,
                complete_original_inner_conversion_reused=inherited))
            doc["coefficient_stage"]=saved(cp,converted)
            doc.pop("last_attempted_matrix_row",None);checkpoint()
        converted["complete"]=True;doc["coefficient_stage"]=saved(cp,converted);checkpoint()
        gate("all1328 same-order conversions retain every original admissible width and full z word",
            len(converted["rows"])==1328 and converted["complete"]
            and all(v["matrix_conversion"]["original_coefficient_row_payload_sha256"]==payload_sha(dr[i])
                and set(v["matrix_conversion"]["costs"])==set(WORD_NAMES)
                for i,v in enumerate(converted["rows"])))
        for ci,(entry,rootcase,seamcase) in enumerate(zip(ext["case_stages"],root["cases"],seam["refined_forcing_radius_cases"])):
            source=checked_stage(paths["exterior_index"].parent,entry)
            radius=Q(source["exact_radius"])
            if not (radius==RADII[ci] and source["complete"] and seamcase["passed"]
                and all(g["passed"] for g in seamcase["gates"])
                and source["source_sha256"]==EXT_SOURCE
                and source["input_manifest_sha256"]==ext["input_manifest_sha256"]
                and source["exact_inner_interval"]==doc["exact_physical_inner_interval"]
                and source["exact_cover"]==rootcase["exact_radial_cover"]==seamcase["exact_cover"]):
                raise ValueError("a completed original exterior radius or family identity changed")
            path=args.out.parent/"cases"/("radius-"+str(radius.numerator)+"-"+str(radius.denominator)+".json.gz")
            if ci<len(doc["case_stages"]):
                case=checked_stage(args.out.parent,doc["case_stages"][ci])
                if not (case["source_sha256"]==sha(__file__) and case["input_manifest_sha256"]==sha(args.manifest)
                    and case["original_exterior_case_sha256"]==entry["sha256"]
                    and case["exact_radius"]==str(radius)):
                    raise ValueError("a resumed complete exterior source case changed its exact original")
            else:
                case=dict(kind="complete_strict_exterior_first_Airy_full_source_radius",
                    source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),
                    original_exterior_case_sha256=entry["sha256"],complete=False,
                    exact_radius=str(radius),exact_cover=source["exact_cover"],
                    exact_inner_interval=source["exact_inner_interval"],
                    original_complete_analytic_amplitude_numeric=copy.deepcopy(source["original_complete_analytic_amplitude_numeric"]),
                    original_radial_reference_profiles_numeric=copy.deepcopy(source["original_radial_reference_profiles_numeric"]),
                    complete_new_profile=None,rows=[])
                doc["case_stages"].append(saved(path,case));checkpoint()
            if case["complete"]:
                if "complete_case_summary" not in case:
                    raise ValueError("a completed case lost its accepted source summary")
                if ci>len(doc["cases"]):raise ValueError("an accepted case summary has a gap")
                if ci==len(doc["cases"]):doc["cases"].append(copy.deepcopy(case["complete_case_summary"]))
                elif doc["cases"][ci]!=case["complete_case_summary"]:
                    raise ValueError("an accepted complete case summary changed")
                doc["reused_complete_source_rows"]+=len(case["rows"])
                doc["reused_complete_profiles"]+=1
                checkpoint();continue
            if case["complete_new_profile"] is None:
                doc["last_attempted_profile"]=str(radius)
                profile=complete_profile(source,rootcase,seamcase,roots,innerprofile)
                case["complete_new_profile"]=dict(complete=True,payload=profile,payload_sha256=payload_sha(profile))
                doc["new_complete_profiles"]+=1
                doc["case_stages"][ci]=saved(path,case)
                doc.pop("last_attempted_profile",None);checkpoint()
            else:
                profile=case["complete_new_profile"]
                if not profile["complete"] or profile["payload_sha256"]!=payload_sha(profile["payload"]):
                    raise ValueError("an accepted complete exterior source profile changed")
                doc["reused_complete_profiles"]+=1
            p=decode(case["complete_new_profile"]["payload"]["numeric"])
            prefix=len(case["rows"]);doc["reused_complete_source_rows"]+=prefix
            if prefix>len(source["rows"]):raise ValueError("a resumed integral prefix exceeds its exact exterior cover")
            for serial,row in enumerate(source["rows"]):
                idx=row["common_row"];L,R=map(Q,row["interval"]);side=row["side"]
                c0,c1=map(Q,cr[idx]["interval"])
                if not (c0<=L<R<=c1 and row["original_root_row"]==cr[idx]["original_root_row"]
                    and row["original_piece"]==cr[idx]["original_piece"]
                    and ((side=="negative" and R<=rl-H) or (side=="positive" and L>=ru+H))):
                    raise ValueError("a complete accepted exterior row changed its actual physical piece")
                identity=dict(serial=serial,common_row=idx,interval=row["interval"],side=side,
                    original_root_row=row["original_root_row"],original_piece=row["original_piece"],
                    original_complete_exterior_row_payload_sha256=payload_sha(row))
                if serial<prefix:
                    if any(case["rows"][serial][k]!=v for k,v in identity.items()):
                        raise ValueError("an accepted new source row changed its original cell or amplitude")
                    continue
                doc["last_attempted_source_row"]=dict(radius=str(radius),**identity);checkpoint()
                real=decode(nr[idx]["bounds"]);accepted=decode(cr[idx]["bounds"])
                z=decode(converted["rows"][idx]["matrix_conversion"]["costs"])
                amps=source_amplitudes(row,accepted,real,p)
                bounds=nonlocal_constants(real,z,amps["complete_operators"],
                    row["actual_first_row_local_source_singular_envelope"])
                weight=up(box(row["radial_weight_integral"]))
                if not weight>0:raise ValueError("an actual one-sided source integral lost its positive weight")
                sep={
                    "first_nonlocal":record((weight*ipow(up(box(bounds["first_nonlocal_singular_envelope"])),2)).upper()),
                    "independent_even_mean":record((weight*ipow(up(box(bounds["independent_even_mean_singular_envelope"])),2)).upper()),
                    "original_first_local":copy.deepcopy(row["complete_first_row_local_squared_source_integral"])}
                item=dict(**identity,complete_amplitude_operator_evidence=amps,source_bounds=bounds,
                    radial_weight_integral=copy.deepcopy(row["radial_weight_integral"]),
                    original_radial_weight_reused_without_recomputation=True,
                    original_local_source_integral_reused_without_recomputation=True,
                    separate_squared_source_integrals=sep,
                    complete_squared_source_integral=record((weight*up(box(bounds["complete_squared_vector_envelope"]))).upper()))
                case["rows"].append(item);doc["new_complete_source_rows"]+=1
                doc["case_stages"][ci]=saved(path,case)
                doc.pop("last_attempted_source_row",None);checkpoint()
                if serial%128==0:
                    print(json.dumps(dict(radius=str(radius),accepted_rows=len(case["rows"]),
                        expected_rows=len(source["rows"]),seconds=time.monotonic()-start)),flush=True)
            if len(case["rows"])!=len(source["rows"]):
                raise ValueError("an actual exterior source cover is incomplete")
            summary=summarize_case(case,source)
            case.update(complete=True,complete_case_summary=summary,
                original_accepted_source_rows_reused=len(source["rows"]),
                original_physical_seam_sources_unchanged=True,
                no_artificial_inner_interface_source=True)
            doc["case_stages"][ci]=saved(path,case);checkpoint()
            if ci==len(doc["cases"]):doc["cases"].append(summary)
            elif ci<len(doc["cases"]):doc["cases"][ci]=summary
            else:raise ValueError("the actual six-case summary has a gap")
            checkpoint()
        gate("all six actual exterior radii have complete local nine-term nonlocal and independent-mean sources",
            len(doc["cases"])==len(doc["case_stages"])==6
            and all(c["complete"] and Q(c["exact_radius"])==RADII[i] for i,c in enumerate(doc["cases"]))
        gate("all original successful science remains unchanged and no full inverse or positive port was inferred",
            doc["original_target_FFT_intrinsic_coefficient_fold_ray_Taylor_and_derivative_stages_recomputed"]==0
            and doc["original_complete_matrix_words_recomputed"]==0
            and doc["original_exterior_local_sources_recomputed"]==0
            and doc["original_complete_six_analytic_profiles_recomputed"]==0
            and doc["original_physical_seams_recomputed"]==0
            and not doc["positive_weighted_port_conversion_claimed"]
            and not doc["full_high_feedback_strong_return_cutoff97_inverse_or_PDE_branch_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_same_order_matrix_conversions=doc["new_same_order_matrix_conversions"],
            reused_inner_same_order_matrix_conversions=doc["reused_inner_same_order_matrix_conversions"],
            new_complete_profiles=doc["new_complete_profiles"],new_complete_source_rows=doc["new_complete_source_rows"],
            complete_cases=len(doc["cases"]),native_sha256=sha(args.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
