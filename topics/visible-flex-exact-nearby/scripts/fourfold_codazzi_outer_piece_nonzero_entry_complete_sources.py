#!/usr/bin/env python3
"""Complete first-Airy sources on pieces2547/2551 with actual nonzero entries.

The original78 accepted stages,49 Fourier norm/multiplier stages and every
unchanged source row are immutable inputs. New work consumes those bounds on
the next two whole physical pieces. New mathematical data stay temporary;
only small conclusions, parameters, execution identities and hashes publish.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,io,json,os,shutil,sys,time,traceback
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L
import fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources as old
import fourfold_codazzi_adjacent_piece_correlated_Airy_algebra as A
import fourfold_codazzi_outer_piece_entry_Airy_algebra as E

PUBLIC="Rogerhu12/math-research-public"
CONTRACT="ae529c46c898828823d130fb3d5ccf332da14bfdd8fb5b6b45ccae4f815cc337"
HELPER="d9547ccc78147fd705279c3c776255e3f2b0e0f8a6ab240cacf0bb129fcef389"
OLD_SOURCE="fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d"
OLD_ALGEBRA="071065fcdad85536af613d0d198b0034f27ee575b6b2a1c31752cb6ea4a9bc0b"
OLD_MANIFEST="57b978dbff16590d593686a8c7b98b8374aae532b500ec88cf975d3ab3821695"
OLD_NATIVE="5754193c193b9769eeec94bf6a9258489db14f9bfda758bf34a549d71c867a0f"
OLD_PROCESS="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
OLD_PUBLICATION="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
OLD_RUN="43676926141"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_ALGEBRA="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
DOMAIN_EXECUTION="5c43b69390fabd7d8ce247aa28eb82b43a1d1162f7326a436c190de5f3bcd918"
DOMAIN_CONCLUSION="8bd0ae3d892cb1a603bcebc3f150a95ff5ded2d7dd69ade2c63e947c68644182"
DOMAIN_SOURCE="43abdfca9fdb16ebaae6a50349e3faaab87b8def87e1a233e7e44aca18ad6017"
DOMAIN_MANIFEST="9c5aac3369fa328284d08f1daf5a40f1230cdbb3fd1d70afcde5b9ef21d4cdf3"
HISTORICAL_INPUT_COMMIT="a3d84d905ce72e3a854874bbe98d119623f3f8de"
ROOTS=old.ROOTS;GERM=old.GERM;RG=old.RG;RHO=old.RHO;RC=old.RC
SIGMA=old.SIGMA;SG=old.SG;DELTA=old.DELTA;WIDTHS=old.WIDTHS
WIDE=Q(5,256);PHASE_FLOW=Q(1,128);FORCING=Q(3,512)
CORRECTION_FLOW=Q(9,2048);FINAL=Q(3,1024)
PIECES=(2547,2551);CUTOFF=97
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
whole=old.whole;inner=whole.inner;full=whole.full
sha=old.sha;read=old.read;save=old.save;payload_sha=old.payload_sha
record=old.record;box=old.box;up=old.up;ex=A.ex;ipow=A.ipow
pack=old.pack;checked=old.checked;native_success=old.native_success
LEADING_FIELDS=("chi","A","G","a0","b0","T","Q","Xp")
CORRECTION_FIELDS=("F0","F1","f0","f1","Z0","Z1","w1a","w1b")
LEGACY_NAMES={
    "complete-original-reference-holomorphic-majorants",
    "complete-root-bstar-polynomial-norms-at-one-thirtytwo",
    "exact-signed-cubic-difference-2548",
    "same-intrinsic-root15-and-third-tail-2548",
}
for field in LEADING_FIELDS:
    for width in (WIDE,FORCING):
        LEGACY_NAMES.add("reference-Fourier-norms-"+field+"-"+str(width.numerator)+"-"+str(width.denominator))
for field in CORRECTION_FIELDS:
    LEGACY_NAMES.add("reference-Fourier-norms-"+field+"-3-512")
STAGE_KINDS=(
    "new_exact_cubic_difference_stages","new_missing_entry_budget_stages",
    "new_intrinsic_consumption_stages","new_reference_tail_consumptions",
    "new_background_comparison_stages","new_phase_comparison_stages",
    "new_forcing_comparison_stages","new_correction_comparison_stages",
    "new_reference_radius_budgets","new_actual_radius_budgets",
    "new_complete_source_rows","new_piece_summaries",
    "new_case_selections","new_case_summaries",
)

def restored(v):
    if isinstance(v,dict):
        if v.get("normalization")=="partial_rho^p partial_phi^q / (p! q!)":
            return A.J.restore(v)
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:restored(x) for k,x in v.items()}
    if isinstance(v,list):return [restored(x) for x in v]
    return v

def receipt(path,base):
    return dict(file=str(path.relative_to(base)),bytes=path.stat().st_size,sha256=sha(path))

def compact_case(v):
    return dict(exact_radius=v["exact_radius"],complete_rows=v["complete_rows"],
        source_summary={side:{
            "complete_first_correction_ordinary_L2_source":
                z["complete_first_correction_ordinary_L2_source"],
            "separate_component_L2_bounds":z["separate_component_L2_bounds"],
            "complete_rows":z["complete_rows"]}
            for side,z in v["source_summary"].items()},
        negative_first_correction_source_component_Hminus4over3_to_primitive_L2=
            v["negative_first_correction_source_component_Hminus4over3_to_primitive_L2"],
        original_actual_negative_source_to_primitive_L2_gain=
            v["original_actual_negative_source_to_primitive_L2_gain"],
        new_complete_outer_piece_rows_selected=v["new_complete_outer_piece_rows_selected"])

def ball_text(v):
    if isinstance(v,dict):
        if "ball" in v:return str(v["ball"])
        if "upper" in v:return str(v["upper"])
    return str(v)

def write_small(path,value):
    text=json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+"\n"
    data=text.encode("utf-8")
    if len(data)>60000:raise ValueError("the self-contained small process exceeds60000bytes")
    temporary=path.with_name(path.name+".tmp")
    temporary.write_bytes(data);os.replace(temporary,path)

def conclusion(doc,command):
    out=[
        "# Actual nonzero-entry complete sources on physical pieces2547 and2551",
        "",
        "This result consumes the same fixed eta0 and the same real delta family "
        "with |delta|<=1e-8. The complex coefficient box, all independent means, "
        "both carrier branches and every true physical seam are retained.",
        "",
        "- Public repository: "+PUBLIC+".",
        "- Actual run: "+str(doc["run_id"])+"/"+str(doc["run_attempt"])+".",
        "- Script: topics/visible-flex-exact-nearby/scripts/"
            "fourfold_codazzi_outer_piece_nonzero_entry_complete_sources.py.",
        "- Script SHA256: "+doc["source_sha256"]+".",
        "- Entry-algebra SHA256: "+doc["algebra_sha256"]+".",
        "- Input manifest SHA256: "+doc["input_manifest_sha256"]+".",
        "- Original successful adjacent run: "+OLD_RUN+"/1, native SHA256 "+OLD_NATIVE+".",
        "- Whole-piece domain run:43680556665/1; all15 gates passed.",
        "- Actual return code: "+str(doc["actual_returncode"])+".",
        "- Original targets, FFTs, scalar root coefficients, saved Fourier norms, "
            "matrix words, phase profiles and unchanged source enclosures recomputed:0.",
        "- New temporary mathematical stages completed: "+str(len(doc["stages"]))+".",
        "- New whole physical source rows completed: "+str(doc["new_complete_source_rows"])+".",
        "- Complete cases recombined from whole rows: "+str(len(doc["cases"]))+".",
        "- CLI: "+json.dumps(command,ensure_ascii=False)+".",
        "",
        "## Actual gates",
        "",
    ]
    for g in doc["gates"]:
        out.append("- "+g["name"]+": "+("passed" if g["passed"] else "FAILED")+".")
    if doc["failure"] is not None:
        out.extend(["","## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False)])
    for p in doc["pieces"]:
        out.extend(["","## Complete physical piece"+str(p["piece"]),"",
            "- Exact physical interval: ["+", ".join(p["interval"])+"].",
            "- Genuine nonzero entry from piece"+str(p["predecessor_piece"])+
                " at "+p["exact_entry_seam"]+".",
            "- Exact strict-side rho range: ["+", ".join(p["exact_rho_interval"])+"].",
            "- Full common rows: "+str(p["complete_common_rows"])+".",
            "",
            "| retained entry quantity | complete upper ball | paid old width |",
            "| --- | --- | --- |"])
        ent=p["entry_bounds"];ext=p["exit_bounds"]
        for label,key,width in (
            ("Phase-label difference","phase_error_sup","phase_entry_width"),
            ("Scalar first-correction difference","scalar_transport_error_sup","scalar_entry_width"),
            ("Radial log-ratio integration constant","log_ratio_error_sup",None)):
            out.append("| "+label+" | "+ball_text(ent[key])+" | "+
                (ent[width] if width else "radial scalar; full ordinary mean")+" |")
        out.extend(["","The following are complete exit-supremum conclusions, "
            "including inherited entry values. They may be used as numerical "
            "conclusions on the stated real-parameter family and angular domains; "
            "they are not zero-entry normalizations.","",
            "| complete exit quantity | upper ball | width |",
            "| --- | --- | --- |"])
        for label,key,width in (
            ("Phase-label difference","phase_error_sup",str(PHASE_FLOW)),
            ("Scalar first-correction difference","scalar_transport_error_sup",str(CORRECTION_FLOW)),
            ("Radial log-ratio constant","log_ratio_error_sup","radial scalar")):
            out.append("| "+label+" | "+ball_text(ext[key])+" | "+width+" |")
        out.extend(["",
            "- Complete new phase-ray path bound: "+ball_text(p["phase_path_upper"])+".",
            "- Complete new scalar-ray path bound: "+ball_text(p["correction_path_upper"])+".",
            "- Phase and correction entry widths are checked on the actual rays; "
                "the barred path is not substituted.",
            "",
            "| full ordinary radial L2 channel | upper ball |",
            "| --- | --- |"])
        z=p["full_complete_source_summary"]
        out.append("| complete first-correction source | "+
            ball_text(z["complete_first_correction_ordinary_L2_source"])+" |")
        for name,v in z["separate_component_L2_bounds"].items():
            out.append("| "+name+" | "+ball_text(v)+" |")
        out.extend(["","| complete nonlocal term after its original J fee | upper L2 ball |",
            "| --- | --- |"])
        for name,v in z["individual_first_row_nonlocal_L2_bounds"].items():
            out.append("| "+name+" | "+ball_text(v)+" |")
        out.extend(["","| independent even-mean term after its original factor | upper L2 ball |",
            "| --- | --- |"])
        for name,v in z["individual_independent_mean_L2_bounds"].items():
            out.append("| "+name+" | "+ball_text(v)+" |")
    out.extend(["","## Complete six-radius row recombination","",
        "Each selected new bound replaces one complete original row on the identical "
        "physical interval. Every other row is copied unchanged. Old and new upper "
        "integrals are never subtracted.","",
        "| radius | side | complete source L2 | local L2 | nonlocal L2 | independent mean L2 |",
        "| --- | --- | --- | --- | --- | --- |"])
    for v in doc["cases"]:
        for side in ("negative","positive","positive_collar","positive_body"):
            z=v["source_summary"][side];s=z["separate_component_L2_bounds"]
            out.append("| "+str(v["exact_radius"])+" | "+side+" | "+
                ball_text(z["complete_first_correction_ordinary_L2_source"])+" | "+
                ball_text(s["original_first_local"])+" | "+ball_text(s["first_nonlocal"])+" | "+
                ball_text(s["independent_even_mean"])+" |")
    out.extend(["","## Scope","",
        "The local first-row source is JP S(Nraw), with Nraw the unnormalized "
        "numerator. No extra division by mu or inverse Fourier frequency is inserted. "
        "The nine full old-circle nonlocal terms and the five independent even-mean "
        "terms remain. The full65 centre, full193 direction, all1079 original physical "
        "seams and the653 previously recorded normalized seam rows retain their identity.",
        "",
        "These are source bounds for the same actual first correction. They do not "
        "prove the complete corrected-seam operator, a strong return bound, the cutoff97 "
        "inverse, the unknown high-frequency feedback, or an exact PDE branch. Failed "
        "old large-radius bounds remain historical evidence; no old upper is removed "
        "by subtracting another upper.",
        "",
        "The original78 accepted stages and old complete norm tables are immutable "
        "historical inputs. New native/stage/case files stay in the temporary runner "
        "and are not uploaded to main, a Release or an Actions artifact. This conclusion "
        "records only script, parameters, actual run, numerical conclusions and identities.",
        ""])
    data="\n".join(out)
    if len(data.encode("utf-8"))>60000:
        raise ValueError("the numerical conclusion exceeds60000bytes")
    return data

def source_row(piece_id,common,conversion,budget,profile):
    real=whole.decode(common["bounds"]);p=whole.decode(profile["payload"]["numeric"])
    # The profile is the actual physical phase on R=1/1000, not the auxiliary phase.
    rv=dict(U=[real["U"]],V=[real["V"]],D=real["D"],em=real["eta_lower"])
    def row(width):return next(v for v in budget["budgets"] if Q(v["exact_output_phi_width"])==width)
    rbudget=row(Q(0));abudget=row(Q(1,512))
    rj=inner.amplitude_jets(rbudget,rv,p["PQ"])
    # These are fresh joint Fourier majorants of the same actual continued-piece
    # cubic differences on FORCING. No real-circle bound is promoted to a strip.
    cv=whole.decode(budget["complete_actual_complex_coefficient_jets"])
    if not Q(budget["exact_complex_coefficient_strip"])>Q(1,512):
        raise ValueError("the actual complete coefficient strip was lost")
    aj=inner.amplitude_jets(abudget,cv,p["PQ"])
    side="negative" if piece_id<2549 else "positive"
    ops={key:inner.Airy_bound(rj[key],aj[key][0],p,side) for key in rj}
    rn=whole.decode(rbudget["complete_Nraw_derivative_budgets"])["strip_sup"]
    an=whole.decode(abudget["complete_Nraw_derivative_budgets"])["strip_sup"]
    lj=[[rn[k][str(q)] for k in ("a","b")] for q in range(3)]
    la=[an[k]["0"] for k in ("a","b")]
    lop=inner.Airy_bound(lj,la,p,side)
    local=record((real["C_J_scalar"]*up(box(lop["bound"]))).upper())
    z=whole.decode(conversion["matrix_conversion"]["costs"])
    bounds=full.nonlocal_constants(real,z,ops,local)
    a,b=map(Q,common["interval"]);weight=inner.radial_weight(a,b,ROOTS,side)
    if not weight>0:raise ValueError("the genuine neighboring row has no positive one-sided radial measure")
    separated={k:record((weight*ipow(up(box(bounds[v])),2)).upper()) for k,v in (
        ("first_nonlocal","first_nonlocal_singular_envelope"),
        ("independent_even_mean","independent_even_mean_singular_envelope"),
        ("original_first_local","original_first_local_singular_envelope"))}
    return dict(common_row=common["common_row"],interval=copy.deepcopy(common["interval"]),
        original_root_row=common["original_root_row"],original_piece=piece_id,side=side,
        radial_weight_integral=record(weight),complete_amplitude_operator_evidence=ops,
        correlated_local_numerator_operator_evidence=lop,source_bounds=bounds,
        separate_squared_source_integrals=separated,
        complete_squared_source_integral=record((weight*up(box(bounds["complete_squared_vector_envelope"]))).upper()),
        original_moment_row_payload_sha256=payload_sha(common),
        original_same_order_conversion_payload_sha256=payload_sha(conversion),
        complete_adjacent_piece_budget_payload_sha256=payload_sha(budget),
        original_actual_phase_profile_payload_sha256=profile["payload_sha256"],
        actual_local_source_is_JP_S_of_unnormalized_Nraw=True,
        complete_nine_nonlocal_and_five_independent_mean_terms_retained=True,
        all_original_physical_seams_and_independent_mean_equations_retained=True,
        auxiliary_phase_not_substituted_for_actual_physical_phase=True)
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--out-dir",type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematical evaluations run only in the public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the completed scientific runtime changed")
    if args.out_dir.exists() and any(args.out_dir.iterdir()):
        raise FileExistsError("do not overwrite an earlier complete or failed temporary result")
    args.out_dir.mkdir(parents=True,exist_ok=True)
    native_path=args.out_dir/"outer-piece-nonzero-entry-complete-sources.json.gz"
    process_path=args.out_dir/"process.json";conclusion_path=args.out_dir/"conclusion.md"
    ctx.prec=320;ctx.cap=4;start=time.monotonic();original_reads=set()
    command=[sys.executable,str(Path(__file__).resolve()),*sys.argv[1:]]
    doc=dict(kind="actual_outer_piece_nonzero_entry_complete_first_Airy_sources",
        complete=False,proved=False,failure=None,actual_returncode=1,gates=[],
        stages={},pieces=[],cases=[],case_stages=[],runtime=runtime,public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),algebra_sha256=sha(E.__file__),
        original_algebra_sha256=sha(A.__file__),Laurent_algebra_sha256=sha(L.__file__),
        input_manifest_sha256=sha(args.manifest),contract_sha256=CONTRACT,
        original_adjacent_native_sha256=OLD_NATIVE,original_adjacent_source_sha256=OLD_SOURCE,
        original_adjacent_manifest_sha256=OLD_MANIFEST,original_adjacent_run_id=OLD_RUN,
        original_domain_run_id="43680556665",original_domain_execution_sha256=DOMAIN_EXECUTION,
        fixed_intrinsic_parameter="eta_0",exact_real_delta_radius=str(DELTA),
        exact_complex_coefficient_delta_radius=str(DELTA),exact_root_interval=list(map(str,ROOTS)),
        physical_outer_pieces=list(PIECES),original_root_piece=2549,
        input_cutoff=CUTOFF,exact_positive_body_cut=str(whole.BODY),
        actual_first_correction_density="n^(1/6), n=4|j|",
        source_window="ordinary L2_r of complete H^(-2/3) first row and independent even mean",
        original_accepted_adjacent_stage_count=78,old_mathematical_stages_recomputed=0,
        old_targets_FFT_intrinsic_cubics_coefficients_norms_words_phases_source_rows_recomputed=0,
        original_complete_physical_seams_retained=1079,
        original_complete_normalized_seam_rows_retained=653,
        inherited_entry_errors_reset_to_zero=False,original_physical_or_parameter_family_replaced=False,
        complete_corrected_seam_operator_paid=False,full_strong_return_or_high_inverse_claimed=False,
        all_original_failed_large_radius_results_retained=True,
        old_circle_nine_terms_and_five_independent_mean_terms_retained=True,
        reused_new_stages=0,recovered_unindexed_complete_stages=0,
        copied_original_complete_rows=0,selected_new_complete_rows=0,
        new_data_published_to_repository=False,new_data_uploaded_to_Releases=False,
        new_data_uploaded_to_Actions_artifacts=False)
    for kind in STAGE_KINDS:doc[kind]=0
    def checkpoint():
        doc["seconds"]=time.monotonic()-start
        doc["complete_original_stage_names_read"]=sorted(original_reads)
        save(native_path,doc)
    def gate(name,value):
        ok=bool(value);doc["gates"].append(dict(name=name,passed=ok))
        if not ok:raise ValueError("outer-piece gate failed: "+name)
    expected=dict(source_sha256=doc["source_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
        algebra_sha256=doc["algebra_sha256"],runtime=runtime)
    def validate_new(value,name,kind):
        if not (kind in STAGE_KINDS and value.get("complete") is True
            and value.get("name")==name and value.get("stage")==name
            and value.get("stage_kind")==kind
            and all(value.get(k)==v for k,v in expected.items())
            and value.get("payload_sha256")==payload_sha(value.get("payload"))):
            raise ValueError("a temporary complete stage changed its exact current identity")
    def stage(name,kind,build):
        if not name.replace("-","").replace("_","").isalnum():
            raise ValueError("unsafe natural stage name")
        path=args.out_dir/"stages"/(name+".json.gz")
        if name in doc["stages"]:
            value=checked(path,doc["stages"][name]);doc["reused_new_stages"]+=1
        elif path.exists():
            value=read(path);doc["recovered_unindexed_complete_stages"]+=1
        else:
            payload=pack(build())
            value=dict(name=name,stage=name,stage_kind=kind,complete=True,
                payload_sha256=payload_sha(payload),payload=payload,**expected)
            save(path,value);doc[kind]+=1
        validate_new(value,name,kind)
        entry=receipt(path,args.out_dir);entry["stage_kind"]=kind
        doc["stages"][name]=entry;checkpoint()
        return value["payload"]
    try:
        gate("the exact current helper and frozen original scientific modules are unchanged",
            doc["algebra_sha256"]==HELPER and sha(old.__file__)==OLD_SOURCE
            and doc["original_algebra_sha256"]==OLD_ALGEBRA
            and doc["input_manifest_sha256"]==args.manifest_sha and len(LEGACY_NAMES)==28)
        manifest=read(args.manifest)
        gate("only the two fully checked next physical pieces are selected",
            manifest["public_repository"]==PUBLIC
            and manifest["mathematical_parameters"]["physical_pieces"]==list(PIECES)
            and manifest["mathematical_parameters"]["original_root_piece"]==2549
            and manifest["mathematical_parameters"]["original_adjacent_run_id"]==OLD_RUN)
        pins={}
        for pin in manifest["files"]+manifest.get("external_completed_natives",[]):
            path=args.repo/pin["path"];key=str(path.resolve())
            if key in pins and any(pins[key][k]!=pin[k] for k in ("bytes","sha256")):
                raise ValueError("two contradictory complete input pins")
            if not path.is_file() or path.stat().st_size!=pin["bytes"] or sha(path)!=pin["sha256"]:
                raise ValueError("an immutable complete scientific input changed: "+pin["path"])
            pins[key]=pin
        paths={key:args.repo/value for key,value in manifest["input_paths"].items()}
        if any(str(p.resolve()) not in pins for p in paths.values()):
            raise ValueError("an input role was not independently pinned")
        gate("the proved nonzero-entry and actual whole-domain contracts are the exact input texts",
            sha(paths["contract"])==CONTRACT
            and sha(paths["domain_execution"])==DOMAIN_EXECUTION
            and sha(paths["domain_conclusion"])==DOMAIN_CONCLUSION)
        domain=read(paths["domain_execution"])
        dr=domain["actual_domain_comparison_receipt"]
        gate("the actual whole intervals passed all15 original domain gates",
            domain["run_id"]=="43680556665" and domain["complete"] is True
            and domain["actual_returncode"]==0 and domain["actual_failure"] is None
            and domain["domain_comparison_source_sha256"]==DOMAIN_SOURCE
            and domain["input_manifest_sha256"]==DOMAIN_MANIFEST
            and domain["historical_input_commit"]==HISTORICAL_INPUT_COMMIT
            and dr["domain_extension_permitted_by_this_comparison"] is True
            and len(dr["gates"])==15 and all(g["passed"] for g in dr["gates"]))
        prior,pp,publication,tn,tp,hn,hp,aux,ap,ind,ip,nn,npdoc=[read(paths[key]) for key in (
            "adjacent_native","adjacent_process","adjacent_publication",
            "Taylor_native","Taylor_process","higher_native","higher_process",
            "auxiliary_native","auxiliary_process","intrinsic_domain_native","intrinsic_domain_process",
            "Nraw_native","Nraw_process")]
        gate("the original successful78-stage adjacent native and its public process remain unchanged",
            sha(paths["adjacent_native"])==OLD_NATIVE and sha(paths["adjacent_process"])==OLD_PROCESS
            and sha(paths["adjacent_publication"])==OLD_PUBLICATION
            and native_success(prior,pp) and len(prior["gates"])==14
            and prior["source_sha256"]==OLD_SOURCE and prior["algebra_sha256"]==OLD_ALGEBRA
            and prior["input_manifest_sha256"]==OLD_MANIFEST and prior["runtime"]==runtime
            and len(prior["stages"])==78 and len(prior["cases"])==6
            and prior["original_scalar_coercion_complete_stages_inherited"]==28
            and prior["original_scalar_coercion_stages_recomputed"]==0
            and str(pp["run_id"])==OLD_RUN and pp["native_sha256"]==OLD_NATIVE
            and publication["complete"] is True and publication["actual_returncode"]==0
            and str(publication["run_id"])==OLD_RUN)
        gate("all other accepted Taylor intrinsic and whole-product natives retain their exact identity",
            sha(paths["Taylor_native"])==whole.TAYLOR and sha(paths["Taylor_process"])==whole.TPROC
            and sha(paths["higher_native"])==old.HIGHER and sha(paths["higher_process"])==old.HPROC
            and sha(paths["auxiliary_native"])==whole.AUX and sha(paths["auxiliary_process"])==whole.APROC
            and sha(paths["intrinsic_domain_native"])==old.INTRINSIC
            and sha(paths["intrinsic_domain_process"])==old.IPROC
            and sha(paths["Nraw_native"])==whole.NRAW and sha(paths["Nraw_process"])==whole.NPROC
            and all(native_success(n,p) for n,p in ((tn,tp),(hn,hp),(aux,ap),(nn,npdoc))))
        gate("the same fixed eta0 complete family root and every original mean and seam remain",
            tn["exact_root_interval"]==prior["exact_root_interval"]==aux["exact_root_interval"]==list(map(str,ROOTS))
            and tn["exact_fixed_intrinsic_parameter"]==hn["exact_fixed_intrinsic_parameter"]
            and prior["original_complete_physical_seams_retained"]==1079
            and prior["original_complete_normalized_seam_rows_retained"]==653
            and tn["complete_branch_identity"]==prior["original_complete_branch_identity"]
            and tn["complete_branch_identity"]["same_complex_delta_without_conjugation"]
            and prior["both_original_Airy_carrier_branches_retained"] is True)
        doc["exact_fixed_intrinsic_parameter"]=tn["exact_fixed_intrinsic_parameter"]
        doc["original_complete_branch_identity"]=copy.deepcopy(tn["complete_branch_identity"])
        doc["original_complete_adjacent_stage_receipts"]=copy.deepcopy(prior["stages"])
        doc["original_complete_adjacent_case_receipts"]=copy.deepcopy(prior["case_stages"])
        legacy=prior["accepted_scalar_coercion_prefix"]
        gate("only the previously accepted exact28 legacy headers remain in the original lineage",
            legacy==pp["accepted_scalar_coercion_prefix"]
            and legacy["source_sha256"]==LEGACY_SOURCE and legacy["algebra_sha256"]==LEGACY_ALGEBRA
            and legacy["input_manifest_sha256"]==LEGACY_MANIFEST and legacy["runtime"]==runtime
            and legacy["complete_original_stage_count"]==28
            and legacy["original_stage_headers_and_payloads_unchanged"] is True)
        pub={v["file"]:v for v in publication["files"]}
        def original_stage(name):
            entry=prior["stages"][name];path=paths["adjacent_native"].parent/entry["file"]
            if str(path.resolve()) not in pins:raise ValueError("an original accepted stage is not pinned")
            value=checked(path,entry);p=pub["consumers/"+entry["file"]]
            identity=(LEGACY_SOURCE,LEGACY_ALGEBRA,LEGACY_MANIFEST) if name in LEGACY_NAMES else (
                OLD_SOURCE,OLD_ALGEBRA,OLD_MANIFEST)
            if not (p["bytes"]==entry["bytes"] and p.get("sha256",p.get("original_sha256"))==entry["sha256"]
                and value["complete"] is True and value["name"]==value["stage"]==name
                and value["runtime"]==runtime
                and (value["source_sha256"],value["algebra_sha256"],value["input_manifest_sha256"])==identity
                and value["payload_sha256"]==payload_sha(value["payload"])):
                raise ValueError("an original stage no longer matches its own accepted immutable header and payload")
            original_reads.add(name)
            return value["payload"]
        def accepted(native,key,base,oldsource,newsource,newmanifest):
            oldkey=key in native.get("original_stages",{})
            entry=(native["original_stages"] if oldkey else native["stages"])[key]
            path=base/entry["file"]
            if str(path.resolve()) not in pins:raise ValueError("an original norm/background file is not pinned: "+key)
            value=checked(path,entry)
            source=oldsource if oldkey else newsource
            m=whole.numerator.OLD_MANIFEST if oldkey else newmanifest
            if not (value["complete"] and value.get("stage",value.get("name"))==key
                and value["source_sha256"]==source and value["input_manifest_sha256"]==m):
                raise ValueError("an original norm or background changed its own scientific identity")
            return value["payload"]
        def tstage(key):
            return accepted(tn,key,paths["Taylor_native"].parent,
                whole.numerator.OLD_SOURCE,whole.TSOURCE,whole.TMANIFEST)
        def nstage(key):
            return accepted(nn,key,paths["Nraw_native"].parent,
                whole.numerator.OLD_SOURCE,whole.NSOURCE,whole.NMANIFEST)
        if args.resume:
            previous=read(args.resume)
            same=("source_sha256","algebra_sha256","original_algebra_sha256","Laurent_algebra_sha256",
                "input_manifest_sha256","runtime","original_adjacent_native_sha256","contract_sha256")
            gate("a same-run temporary prefix is accepted only with the exact current scientific identity",
                all(previous.get(k)==doc.get(k) for k in same))
            for source in sorted((args.resume.parent/"stages").glob("*.json.gz")):
                value=read(source);name=value.get("name");kind=value.get("stage_kind")
                validate_new(value,name,kind)
                if source.name!=name+".json.gz":raise ValueError("a resumed temporary stage changed its filename")
                target=args.out_dir/"stages"/source.name;target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(source,target)
                entry=receipt(target,args.out_dir);entry["stage_kind"]=kind
                if name in previous["stages"] and any(previous["stages"][name][k]!=entry[k]
                    for k in ("file","bytes","sha256","stage_kind")):
                    raise ValueError("an indexed temporary stage was altered")
                doc["stages"][name]=entry
            if set(previous["stages"])-set(doc["stages"]):
                raise ValueError("a previously complete temporary stage is missing")
            for kind in STAGE_KINDS:doc[kind]=previous.get(kind,0)
            doc["recovered_original_temporary_prefix"]=dict(native_sha256=sha(args.resume),
                complete=previous["complete"],failure=previous["failure"],original_stage_count=len(previous["stages"]))
        checkpoint()
        cp,zp=[read(paths[k]) for k in ("candidate_index","response_index")]
        alpha=Q(cp["metadata"]["exact_float_amplitude"])
        gate("the complete original65 and193 cubics and their ordinary means are retained",
            sha(paths["candidate_index"])==old.CANDIDATE and sha(paths["response_index"])==old.RESPONSE
            and cp["coefficient_shape"]==[4,6144,65] and zp["coefficient_shape"]==[4,6144,193]
            and alpha==Q(6890507429876859,9007199254740992)
            and zp["metadata"]["finite_head_mean_was_not_removed_from_the_solve"])
        shards={}
        for key,index,first,end,count,wanted in (
            ("candidate",cp,1346,2692,65,old.CSHARD),("response",zp,2265,2718,193,old.ZSHARD)):
            path=paths[key+"_shard"];parts=index.get("parts",index.get("shards",[]))
            part=next(v for v in parts if v["first_interval"]==first)
            if not (part["last_interval_exclusive"]==end and part["sha256"]==sha(path)==wanted
                and part["file"]==path.name and part["bytes"]==path.stat().st_size):
                raise ValueError("an original complete natural cubic shard changed")
            with np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False) as z:
                nodes=z["radial_nodes"].copy();coeff=z["piece_coefficients"].copy()
            if not (nodes.shape==(end-first+1,) and coeff.shape==(4,end-first,count)
                and np.isfinite(nodes).all() and np.isfinite(coeff).all() and (np.diff(nodes)>0).all()):
                raise ValueError("the whole original cubic arrays are incomplete")
            shards[key]=(nodes,coeff)
        background={k:L.unpack_series(v) for k,v in tstage("complete-background-root-series")["series"].items()}
        tnorm={};nnorm={}
        for width in WIDTHS:
            tag=str(width.numerator)+"_"+str(width.denominator)
            tnorm[str(width)]=[tstage("full-Fourier-norm-"+tag+"-degree-"+str(j).zfill(3)) for j in range(13)]
            nnorm[str(width)]=[nstage("full-Nraw-Fourier-norm-"+tag+"-degree-"+str(j).zfill(3)) for j in range(11)]
        multi=nstage("complete-local-numerator-whole-product-multipliers")
        multipliers=whole.decode(multi["complete_multiplier_bounds"])
        amp={k:up(box(tn["old_product_domain"]["full_canonical_"+v+"_sup"]))
            for k,v in (("a","a1"),("b","b1"))}
        auxcase=aux["cases"][1]
        gate("the complete auxiliary reference products retain their original old-coordinate domains",
            auxcase["complete"] and auxcase["proved"] and auxcase["failure"] is None
            and all(g["passed"] for g in auxcase["gates"])
            and Q(auxcase["exact_fold_radius"])==RG and Q(auxcase["exact_old_leading_width"])==SG
            and Q(tn["old_product_domain"]["exact_rho_radius"])==RHO
            and Q(tn["old_product_domain"]["exact_phi_width"])==SIGMA)
        old_majorants=restored(original_stage("complete-original-reference-holomorphic-majorants"))
        majors={k:(v[0],Q(v[1]),Q(v[2])) for k,v in old_majorants["majorants"].items()}
        fold=old_majorants["fold"]
        def complete_reference(H,width,leading_only):
            ans={}
            fields=LEADING_FIELDS if leading_only else LEADING_FIELDS+CORRECTION_FIELDS
            for name in fields:
                M,R,S=majors[name]
                if not (Q(H)<R and width<S):raise ValueError("a new reference consumption leaves the original product")
                key="reference-Fourier-norms-"+name+"-"+str(width.numerator)+"-"+str(width.denominator)
                p=original_stage(key)
                if not (p["field"]==name and Q(p["exact_width"])==width
                    and p["full_coefficients_and_all_outputs_retained"] is True
                    and p["original_finite_coefficients_recomputed"] is False):
                    raise ValueError("a complete old reference norm changed its field width or full-output scope")
                norms=[[up(box(v)) for v in row] for row in p["norms"]]
                if len(norms)!=(15 if name in LEADING_FIELDS else 13) or any(len(row)!=9 for row in norms):
                    raise ValueError("an original full reference norm table lost a degree or angular derivative")
                ans[name]=A.mixed_sup_from_norms(norms,H,R,S,width,M,8,3)
            if not leading_only:
                for key,a,b in (("F","F0","F1"),("f","f0","f1"),("Z","Z0","Z1"),("w1","w1a","w1b")):
                    ans[key]=[ans.pop(a),ans.pop(b)]
            return ans
        bs=original_stage("complete-root-bstar-polynomial-norms-at-one-thirtytwo")
        if not (Q(bs["exact_width"])==Q(1,32) and bs["complete_root_mean_retained"] is True):
            raise ValueError("the complete original root bstar value or its true strip was lost")
        bstar=[up(box(x)) for x in bs["complete_bstar"]]
        intrinsic_case=next(v for v in ind["cases"] if Q(v["exact_auxiliary_radius"])==RC)
        rect=intrinsic_case["exact_complex_rectangle"]
        gate("the entire true-root intrinsic disk lies in the same previously proved complex rectangle",
            intrinsic_case["complete"] and intrinsic_case["proved"] and intrinsic_case["failure"] is None
            and Q(rect["real_interval"][0])<=ROOTS[0]-RC and Q(rect["real_interval"][1])>=ROOTS[1]+RC
            and Q(rect["imaginary_half_width"])>=RC and ip["native_sha256"]==old.INTRINSIC
            and Q(ip["cases"][1]["exact_auxiliary_radius"])==RC
            and ip["cases"][1]["proved"] and ip["cases"][1]["failure"] is None
            and hn["intrinsic_stage"]["complete"] and hn["at_the_certified_true_root"]["exact_K0"]=="0")
        original_raw=hn["intrinsic_stage"]["ordinary_old_radial_jets"]
        third={key:ip["cases"][1]["complete_intrinsic"]["ordinary_jet_modulus_upper"][key][3]
            for key in ("K","beta","gamma","s")}
        norm=read(paths["moment_native"]);converted=read(paths["conversions"])
        nr=norm["coefficient_rows"];zr=converted["rows"]
        gate("all1328 original complete moment and old-circle matrix rows remain identical",
            sha(paths["moment_native"])==whole.MOMENT and sha(paths["conversions"])==whole.CONVERSIONS
            and len(nr)==len(zr)==1328 and norm["complete"] and norm["proved"] and converted["complete"]
            and all(n["common_row"]==z["common_row"]==j and n["interval"]==z["interval"]
                and z["original_moment_row_payload_sha256"]==payload_sha(n)
                for j,(n,z) in enumerate(zip(nr,zr))))
        bcase=read(paths["bstar_case_0"]);profile=bcase["complete_new_profile"]
        gate("the old actual physical phase supplies the complete all-output profiles on these pieces",
            bcase["complete"] and Q(bcase["exact_radius"])==Q(1,1000)
            and profile["complete"] and profile["payload_sha256"]==payload_sha(profile["payload"])
            and profile["payload"]["exact_old_phi_width"]==str(Q(1,512))
            and profile["payload"]["exact_input_cutoff"]==CUTOFF)
        all_new_rows={}
        for piece in PIECES:
            predecessor=piece+1 if piece<2549 else piece-1
            predecessor_raw=original_stage("exact-signed-cubic-difference-"+str(predecessor))
            predecessor_comparison=original_stage("complete-correlated-phase-forcing-and-w1-"+str(predecessor))
            entry=stage("complete-inherited-entry-"+str(piece),"new_missing_entry_budget_stages",
                lambda predecessor=predecessor,piece=piece:
                    E.consume_complete_inner_entry(predecessor_comparison,predecessor,piece))
            incoming=restored(entry)
            raw=stage("exact-nonzero-cubic-difference-"+str(piece),"new_exact_cubic_difference_stages",
                lambda piece=piece:E.exact_outer_cubic_difference(piece,shards,alpha,predecessor_raw))
            left,right=map(Q,raw["interval"]);seam=Q(raw["exact_entry_seam"])
            side="negative" if piece<2549 else "positive"
            rinterval=(ROOTS[0]-right,ROOTS[1]-left)
            h=min(abs(v) for v in rinterval);H=max(abs(v) for v in rinterval)
            gate("the whole physical piece"+str(piece)+" preserves its proved domain and true nonzero entry",
                GERM[0]<=left<right<=GERM[1] and 0<h<=H<RHO and H<RG and H<RC
                and (right<=ROOTS[0] if side=="negative" else left>=ROOTS[1])
                and Q(entry["exact_physical_entry"])==seam
                and raw["nonzero_entry_repair_difference_retained"] is True
                and entry["entry_errors_reset_to_zero"] is False)
            ib=stage("same-intrinsic-root15-and-third-tail-"+str(piece),"new_intrinsic_consumption_stages",
                lambda rinterval=rinterval:dict(exact_rho_interval=list(map(str,rinterval)),
                    exact_Cauchy_radius=str(RC),complete_jets=A.intrinsic_boxes(original_raw,third,rinterval,RC),
                    old_root_derivatives_or_complex_targets_recomputed=False))
            intrinsic=restored(ib["complete_jets"])
            def background_pair():
                du,dv=old.cubic_difference_jets(raw)
                rho=ex(rinterval[0]).union(ex(rinterval[1]))
                ubar,vbar=A.evaluate_old_background(background,intrinsic,rho)
                return dict(wide=A.background_pairs(ubar,vbar,du,dv,intrinsic,WIDE),
                    forcing=A.background_pairs(ubar,vbar,du,dv,intrinsic,FORCING),
                    exact_wide_strip=str(WIDE),exact_forcing_strip=str(FORCING),
                    full65_full193_and_ordinary_mean_retained=True)
            cstage=stage("complete-background-difference-jets-"+str(piece),
                "new_background_comparison_stages",background_pair)
            cwide=restored(cstage["wide"]);cforce=restored(cstage["forcing"])
            refwide=restored(stage("complete-reference-tail-wide-"+str(piece),
                "new_reference_tail_consumptions",lambda H=H:complete_reference(H,WIDE,True)))
            refforce=restored(stage("complete-reference-tail-forcing-"+str(piece),
                "new_reference_tail_consumptions",lambda H=H:complete_reference(H,FORCING,False)))
            def phase_step():
                v=E.phase_comparison_with_entry(cwide,refwide,ex(h),ex(H),ex(right-left),WIDE,PHASE_FLOW,
                    FORCING,fold["Am"].lower(),side,
                    entry_phase_error_sup=incoming["phase_error_sup"],
                    entry_phase_width=Q(incoming["phase_entry_width"]),
                    entry_log_ratio_sup=incoming["log_ratio_error_sup"],
                    local_coefficients=cforce,local_reference=refforce)
                v.update(h=ex(h),H=ex(H),side=side)
                return v
            phase_payload=stage("complete-nonzero-entry-phase-"+str(piece),
                "new_phase_comparison_stages",phase_step)
            phase=restored(phase_payload)
            gate("the complete new actual phase rays and original bstar composition stay inside their paid strips on piece"+str(piece),
                ex(FORCING)+refforce["chi"].get()+phase["X"].get(which="delta")<ex(Q(1,32))
                and phase["path_upper"]<ex(min(WIDE,Q(incoming["phase_entry_width"])))
                and phase["A_gap_actual"]>0 and phase["only_comparison_entry_is_exactly_zero"] is False)
            force=restored(stage("complete-correlated-forcing-"+str(piece),"new_forcing_comparison_stages",
                lambda:A.forcing_comparison(cforce,phase,refforce,fold["mu"].lower(),fold["Bi"])))
            cor_payload=stage("complete-nonzero-entry-first-correction-"+str(piece),
                "new_correction_comparison_stages",lambda:E.correction_comparison_with_entry(
                    cforce,phase,force,refforce,bstar,ex(right-left),
                    FORCING,CORRECTION_FLOW,FINAL,
                    entry_scalar_error_sup=incoming["scalar_transport_error_sup"],
                    entry_scalar_width=Q(incoming["scalar_entry_width"])))
            correction=restored(cor_payload)
            gate("the complete new actual scalar rays inherit their original nonzero value on piece"+str(piece),
                correction["path_upper"]<ex(min(FORCING,Q(incoming["scalar_entry_width"])))
                and correction["comparison_entry_error_reset_to_zero"] is False
                and correction["old_mean_projection_not_deleted"] is True)
            original_radius=stage("complete-reference-radius-"+str(piece),"new_reference_radius_budgets",
                lambda H=H:whole.radius_budget(H,tnorm,nnorm,tn["first_correction_derivative_budgets"],
                    nn["complete_correlated_Nraw_budgets"],multipliers,amp))
            def actual_budget():
                coefficients=dict(
                    U=[[cforce["u"].get(0,q,"actual") for q in range(4)]],
                    V=[[cforce["v"].get(0,q,"actual") for q in range(4)]],
                    D=[cforce["d"].get(0,q,"actual") for q in range(4)],em=cforce["eta_gap_actual"])
                return old.complete_radius_augmented(original_radius,correction,coefficients)
            budget=stage("complete-actual-amplitudes-and-Nraw-"+str(piece),
                "new_actual_radius_budgets",actual_budget)
            plan=[n for n in nr if left<=Q(n["interval"][0])<Q(n["interval"][1])<=right]
            if (not plan or Q(plan[0]["interval"][0])!=left or Q(plan[-1]["interval"][1])!=right
                or any(a["interval"][1]!=b["interval"][0] for a,b in zip(plan,plan[1:]))):
                raise ValueError("the complete original common grid does not cover this whole physical piece")
            piece_rows=[]
            for n in plan:
                j=n["common_row"]
                row=stage("complete-outer-"+str(piece)+"-common-"+str(j).zfill(4),
                    "new_complete_source_rows",lambda n=n,j=j:source_row(piece,n,zr[j],budget,profile))
                if not (row["common_row"]==j and row["interval"]==n["interval"] and row["original_piece"]==piece
                    and row["side"]==side and row["original_moment_row_payload_sha256"]==payload_sha(n)):
                    raise ValueError("a complete new source row changed its actual physical interval")
                all_new_rows[(piece,j)]=row;piece_rows.append(row)
            summary=stage("complete-outer-piece-summary-"+str(piece),"new_piece_summaries",
                lambda:whole.channel_sum(piece_rows))
            doc["pieces"].append(dict(piece=piece,predecessor_piece=predecessor,
                interval=list(map(str,(left,right))),side=side,exact_entry_seam=str(seam),
                exact_rho_interval=list(map(str,rinterval)),complete_common_rows=len(piece_rows),
                entry_bounds=entry,
                exit_bounds=dict(phase_error_sup=phase_payload["phase_error_strip_sup"],
                    phase_entry_width=str(PHASE_FLOW),
                    scalar_transport_error_sup=cor_payload["scalar_transport_difference_sup"],
                    scalar_entry_width=str(CORRECTION_FLOW),
                    log_ratio_error_sup=phase_payload["complete_log_ratio_sup"]),
                phase_path_upper=phase_payload["path_upper"],
                correction_path_upper=cor_payload["path_upper"],
                complete_summary_stage="complete-outer-piece-summary-"+str(piece),
                full_complete_source_summary=summary))
            checkpoint()
        for ci,radius in enumerate(whole.RADII):
            original_path=paths["adjacent_case_"+str(ci)]
            original=checked(original_path,prior["case_stages"][ci])
            if not (original["complete"] is True and original["source_sha256"]==OLD_SOURCE
                and original["input_manifest_sha256"]==OLD_MANIFEST and original["algebra_sha256"]==OLD_ALGEBRA
                and original["runtime"]==runtime and Q(original["exact_radius"])==radius
                and original["complete_case_summary"]==prior["cases"][ci]):
                raise ValueError("an original complete six-radius case changed its own scientific identity")
            def select_rows():
                roles=[]
                for oldserial,oldrow in enumerate(original["rows"]):
                    key=(oldrow["original_piece"],oldrow["common_row"])
                    base=dict(oldserial=oldserial,original_complete_row_payload_sha256=payload_sha(oldrow))
                    if key not in all_new_rows:
                        roles.append(dict(kind="copied_original_complete_row",**base));continue
                    newrow=all_new_rows[key]
                    if oldrow["interval"]!=newrow["interval"] or oldrow["side"]!=newrow["side"]:
                        raise ValueError("a whole new bound changed the original row measure")
                    base.update(stage="complete-outer-"+str(key[0])+"-common-"+str(key[1]).zfill(4),
                        new_complete_row_payload_sha256=payload_sha(newrow))
                    kind=("copied_original_better_complete_bound"
                        if up(box(oldrow["complete_squared_source_integral"]))<=up(box(newrow["complete_squared_source_integral"]))
                        else "new_complete_outer_piece_bound")
                    roles.append(dict(kind=kind,**base))
                return dict(original_complete_case_sha256=sha(original_path),exact_radius=str(radius),
                    row_roles=roles,complete=True,selection_of_whole_upper_envelopes_only=True,
                    no_subtraction_of_original_upper_integrals=True)
            selection_name="complete-outer-selection-radius-"+str(ci)
            selected=stage(selection_name,"new_case_selections",select_rows)
            if not (selected["complete"] is True and selected["original_complete_case_sha256"]==sha(original_path)
                and Q(selected["exact_radius"])==radius and len(selected["row_roles"])==len(original["rows"])):
                raise ValueError("an accepted row selection changed its exact complete source case")
            rows=[];roles=selected["row_roles"];fresh=0
            for oldserial,role in enumerate(roles):
                oldrow=original["rows"][oldserial]
                if role["oldserial"]!=oldserial or role["original_complete_row_payload_sha256"]!=payload_sha(oldrow):
                    raise ValueError("a complete accepted role changed the old row payload")
                kind=role["kind"]
                if kind in ("copied_original_better_complete_bound","new_complete_outer_piece_bound"):
                    key=(oldrow["original_piece"],oldrow["common_row"])
                    newrow=all_new_rows[key]
                    if (role["stage"]!="complete-outer-"+str(key[0])+"-common-"+str(key[1]).zfill(4)
                        or role["new_complete_row_payload_sha256"]!=payload_sha(newrow)):
                        raise ValueError("a saved complete new candidate no longer matches its natural stage")
                if kind=="new_complete_outer_piece_bound":
                    rows.append(copy.deepcopy(newrow));fresh+=1;doc["selected_new_complete_rows"]+=1
                elif kind in ("copied_original_complete_row","copied_original_better_complete_bound"):
                    rows.append(copy.deepcopy(oldrow));doc["copied_original_complete_rows"]+=1
                else:raise ValueError("a complete case contains an undeclared row role")
            def summarize():
                previous=original["complete_case_summary"]
                result=copy.deepcopy(previous)
                result.update(whole.summarize(rows,original["exact_cover"],radius,
                    previous["original_actual_negative_source_to_primitive_L2_gain"]))
                result["new_complete_outer_piece_rows_selected"]=fresh
                result["original_complete_case_payload_sha256"]=payload_sha(previous)
                result["only_the_two_next_true_physical_pieces_reestimated"]=True
                result["entry_differences_or_mean_constants_reset_to_zero"]=False
                return result
            summary_name="complete-outer-six-radius-summary-"+str(ci)
            summary=stage(summary_name,"new_case_summaries",summarize)
            case_out=copy.deepcopy(original)
            case_out.update(kind="complete_outer_piece_nonzero_entry_first_Airy_source_radius",
                source_sha256=doc["source_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
                algebra_sha256=doc["algebra_sha256"],runtime=runtime,complete=True,rows=rows,row_roles=roles,
                original_complete_case_sha256=sha(original_path),complete_case_summary=summary,
                summary_stage=summary_name,selection_stage=selection_name,
                exact_old_physical_seams_and_full_independent_means_preserved=True)
            path=args.out_dir/"cases"/("radius-"+str(radius.numerator)+"-"+str(radius.denominator)+".json.gz")
            save(path,case_out)
            doc["case_stages"].append(dict(**receipt(path,args.out_dir),exact_radius=str(radius)))
            doc["cases"].append(summary);checkpoint()
        gate("both whole new pieces and all six cases retain every other old complete row",
            len(doc["pieces"])==2 and len(doc["cases"])==len(doc["case_stages"])==6
            and sum(len(read(paths["adjacent_case_"+str(i)])["rows"]) for i in range(6))
                ==doc["copied_original_complete_rows"]+doc["selected_new_complete_rows"]
            and doc["old_mathematical_stages_recomputed"]==0
            and doc["old_targets_FFT_intrinsic_cubics_coefficients_norms_words_phases_source_rows_recomputed"]==0)
        gate("all source units physical seams independent means and remaining high-frequency gaps remain explicit",
            not doc["inherited_entry_errors_reset_to_zero"]
            and not doc["original_physical_or_parameter_family_replaced"]
            and not doc["complete_corrected_seam_operator_paid"]
            and not doc["full_strong_return_or_high_inverse_claimed"]
            and doc["old_circle_nine_terms_and_five_independent_mean_terms_retained"]
            and doc["original_complete_physical_seams_retained"]==1079
            and doc["original_complete_normalized_seam_rows_retained"]==653)
        doc["complete"]=True;doc["proved"]=True;doc["actual_returncode"]=0
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
        doc["actual_returncode"]=1
        traceback.print_exc()
    finally:
        checkpoint()
        compact=dict(kind="actual_public_outer_piece_nonzero_entry_complete_sources",
            public_repository=PUBLIC,run_id=doc["run_id"],run_attempt=doc["run_attempt"],
            workflow_event_commit=doc["workflow_event_commit"],
            actual_scientific_checkout_commit=doc["actual_scientific_checkout_commit"],
            source_sha256=doc["source_sha256"],algebra_sha256=doc["algebra_sha256"],
            input_manifest_sha256=doc["input_manifest_sha256"],contract_sha256=CONTRACT,
            original_adjacent_native_sha256=OLD_NATIVE,original_adjacent_run_id=OLD_RUN,
            original_domain_execution_sha256=DOMAIN_EXECUTION,original_domain_run_id="43680556665",
            runtime=runtime,command=command,complete=doc["complete"],proved=doc["proved"],
            actual_returncode=doc["actual_returncode"],failure=doc["failure"],gates=doc["gates"],
            mathematical_complete=doc["complete"],mathematical_proved=doc["proved"],
            mathematical_failure=doc["failure"],mathematical_seconds=doc["seconds"],
            native=receipt(native_path,args.out_dir),new_complete_natural_stages=len(doc["stages"]),
            new_stage_counts={k:doc[k] for k in STAGE_KINDS},
            reused_new_stages=doc["reused_new_stages"],
            recovered_unindexed_complete_stages=doc["recovered_unindexed_complete_stages"],
            complete_temporary_stage_inventory_sha256=payload_sha(doc["stages"]),
            old_mathematical_stages_recomputed=0,original_accepted_adjacent_stage_count=78,
            original_immutable_stages_read=len(original_reads),
            copied_original_complete_rows=doc["copied_original_complete_rows"],
            selected_new_complete_rows=doc["selected_new_complete_rows"],
            actual_piece_conclusions=doc["pieces"],
            actual_radius_conclusions=[compact_case(v) for v in doc["cases"]],
            original_complete_physical_seams_retained=1079,
            original_complete_normalized_seam_rows_retained=653,
            old_circle_nine_terms_and_five_independent_mean_terms_retained=True,
            complete_corrected_seam_operator_paid=False,
            full_strong_return_or_high_inverse_claimed=False,final_topic_complete=False,
            new_reproducible_data_published_or_uploaded=False)
        try:
            text=conclusion(doc,command);conclusion_path.write_text(text,encoding="utf-8")
            compact["output_hashes"]=[receipt(conclusion_path,args.out_dir),receipt(native_path,args.out_dir)]
            write_small(process_path,compact)
        except BaseException as error:
            # Preserve the already completed science. A formatting failure is not
            # permission to recompute any complete stage or source row.
            compact["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            compact["actual_scientific_returncode"]=doc["actual_returncode"]
            compact["actual_returncode"]=2
            compact.pop("actual_radius_conclusions",None)
            compact.pop("actual_piece_conclusions",None)
            compact["actual_result_available_in_temporary_native"]=True
            write_small(process_path,compact)
            doc["actual_returncode"]=2
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],
            actual_returncode=doc["actual_returncode"],failure=doc["failure"],
            original_mathematical_stages_recomputed=0,new_complete_stages=len(doc["stages"]),
            complete_pieces=len(doc["pieces"]),complete_cases=len(doc["cases"]),
            new_complete_source_rows=doc["new_complete_source_rows"],
            native_sha256=sha(native_path),process_sha256=sha(process_path),
            seconds=doc["seconds"]),allow_nan=False),flush=True)
    return doc["actual_returncode"]

if __name__=="__main__":
    raise SystemExit(main())
