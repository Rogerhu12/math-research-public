#!/usr/bin/env python3
"""Actual correlated first-Airy sources on physical pieces 2548 and 2550.

No old target, FFT, root value, finite Taylor coefficient, saved Fourier norm,
matrix word, phase profile or completed exterior source is recomputed.
Only the two exact cubic differences, complete mixed difference budgets and
their new same-solution source rows are evaluated in public Actions.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,io,json,math,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,acb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L
import fourfold_codazzi_adjacent_piece_correlated_Airy_algebra as A
import fourfold_codazzi_whole_physical_root_piece_first_Airy_sources as whole

PUBLIC="Rogerhu12/math-research-public"
CONTRACT="ff1400ce64788b56781f64efc11a58ed8629433cb4a9d81dcbce4552c472587b"
WHOLE="6668c9b2c8f1632e3bd8af392a803335f076c64e1d7fb74dfc9e1605f0e1ee2d"
WPROC="242d82b6f1ead216bf8e90679a9952a2aaad0e9d7ba29293739911e70ab4d145"
WSOURCE="66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81"
WMANIFEST="d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac"
HIGHER="ec702cffb8d1dcb25cdb01eaa89127b1f0044ae1cd3cee9e6e293e8165250480"
HPROC="c7ff69243d3f724f539cd0ee95c2b0ba219caa5ffba47ff9b084387255e78e5b"
INTRINSIC="6276b4b8bd117b3092ce633b7164ff99968100f10b09cbaef8850d4c03f6b24f"
IPROC="a6783642ae2c49f66c3a7b54f1506389f24771790f3bd5a324646df8229f9728"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CSHARD="3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"
RESPONSE="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
ZSHARD="ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917"
ROOTS=whole.ROOTS;GERM=whole.GERM;RHO=whole.RHO;SIGMA=whole.SIGMA
RG=Q(3,8000);SG=Q(3,128);RC=Q(1,2000);DELTA=Q(1,10**8)
WIDE=Q(5,256);PHASE_FLOW=Q(1,64);FORCING=Q(3,512)
CORRECTION_FLOW=Q(5,1024);FINAL=Q(3,1024)
WIDTHS=(Q(0),Q(1,512));PIECES=(2548,2550);CUTOFF=97
full=whole.full;inner=whole.inner
sha=whole.sha;read=whole.read;save=whole.save;payload_sha=whole.payload_sha
record=whole.record;box=whole.box;up=whole.up;ex=A.ex;ipow=A.ipow
I=acb(0,1)

def pack(v):
    if isinstance(v,A.J):return v.record()
    if isinstance(v,arb):return {"ball":L.rec(v,90)}
    if isinstance(v,acb):return {"real":pack(v.real),"imag":pack(v.imag)}
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):pack(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [pack(x) for x in v]
    if isinstance(v,(bool,str,int)) or v is None:return v
    raise TypeError("unrecorded scientific value "+type(v).__name__)
def unpack(v):
    if isinstance(v,dict):
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:unpack(x) for k,x in v.items()}
    if isinstance(v,list):return [unpack(x) for x in v]
    return v
def dyadic(x):
    n,d=float(x).as_integer_ratio();return Q(n,d)
def exact_cubic_at(c,t):
    c=list(map(dyadic,c));a,b,d,e=c
    return [((a*t+b)*t+d)*t+e,3*a*t*t+2*b*t+d,3*a*t+b,a]
def checked(path,entry):
    if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
        raise ValueError("an immutable original mathematical input changed: "+str(path))
    return read(path)
def native_success(native,proc):
    return (native.get("complete") is True and native.get("proved") is True
        and native.get("failure") is None and all(g["passed"] for g in native["gates"])
        and proc.get("actual_returncode")==0 and proc.get("mathematical_complete") is True
        and proc.get("mathematical_failure") is None)
def positive_tail_bound(v):
    if not (v.is_finite() and v.lower()>=0):raise ValueError("nonfinite or negative complete majorant")
    return v.upper()

def exact_cubic_difference(piece,shards,alpha):
    """C0 repairs cancel exactly; all three true derivative differences remain."""
    out={};interval=None;entry=None
    for key,count,first in (("candidate",65,1346),("response",193,2265)):
        nodes,coeff=shards[key];local=piece-first;root=2549-first
        cell=(dyadic(nodes[local]),dyadic(nodes[local+1]))
        rootcell=(dyadic(nodes[root]),dyadic(nodes[root+1]))
        seam=rootcell[0] if piece==2548 else rootcell[1]
        if piece==2548 and cell[1]!=seam or piece==2550 and cell[0]!=seam:
            raise ValueError("these cubics are not genuine adjacent physical pieces")
        if interval is not None and (cell!=interval or seam!=entry):
            raise ValueError("centre and full direction do not have the same physical seams")
        interval,entry=cell,seam
        rows=[]
        for j in range(count):
            here=exact_cubic_at(coeff[:,local,j],seam-cell[0])
            there=exact_cubic_at(coeff[:,root,j],seam-rootcell[0])
            scale=alpha if key=="candidate" else Q(1)
            raw=[scale*(a-b) for a,b in zip(here,there)]
            # This is the exact value repair recurrence, not a contains-zero test.
            repair_difference=-raw[0]
            rows.append(dict(component=j,exact_raw_entry_jump=str(raw[0]),
                exact_required_physical_constant_repair_difference=str(repair_difference),
                exact_repaired_difference_coefficients=["0",*map(str,raw[1:])],
                exact_zero_uses_complete_continuity_repair_identity=True))
        out[key]=rows
    return dict(piece=piece,complete=True,interval=list(map(str,interval)),
        exact_entry_seam=str(entry),parameter="the same repaired centre plus delta times the same complete repaired direction",
        candidate_components=65,response_components=193,physical_mean_components=[32,96],
        raw_signed_components=out,ordinary_value_repair_only=True,
        no_derivative_jump_deleted=True,independent_intrinsic_s_cancels_in_difference=True,
        physical_offset_not_multiplied_by_alpha_twice=True)

def cubic_difference_jets(payload):
    left,right=map(Q,payload["interval"]);seam=Q(payload["exact_entry_seam"])
    t=ex(left-seam).union(ex(right-seam))
    delta=acb(arb(0,ex(DELTA)),arb(0,ex(DELTA)))
    rows=payload["raw_signed_components"];candidate=rows["candidate"];response=rows["response"]
    cj=[[ex(Q(r["exact_repaired_difference_coefficients"][j])) for r in candidate] for j in range(4)]
    zj=[[ex(Q(r["exact_repaired_difference_coefficients"][j])) for r in response] for j in range(4)]
    u=[];v=[]
    for p in range(4):
        cu=[];cv=[]
        for j in range(4):
            uf=[acb(0) for _ in range(193)];vf=[acb(0) for _ in range(193)]
            vf[96]=acb(cj[j][32])+delta*zj[j][96]
            for k in range(1,97):
                us=acb(cj[j][k-1] if k<=32 else 0)+delta*zj[j][k-1]
                vs=acb(cj[j][32+k] if k<=32 else 0)+delta*zj[j][96+k]
                uf[96+k]=us/(2*I);uf[96-k]=-us/(2*I)
                vf[96+k]=vs/2;vf[96-k]=vs/2
            cu.append(L.LP(-96,uf));cv.append(L.LP(-96,vf))
        a=L.LP.zero();b=L.LP.zero()
        for j in range(3,p-1,-1):
            factor=(-1)**p*math.factorial(j)//math.factorial(j-p)
            a=a.scale(acb(t))+cu[j].scale(factor);b=b.scale(acb(t))+cv[j].scale(factor)
        u.append(a);v.append(b)
    return u,v

def reference_majorants(case,domain):
    """Only bounds already paid on the stated complete old product are used."""
    c=whole.decode(case["characteristic_refinement_evidence"]["complete_refined_coefficient_majorants"])
    f=whole.decode(case["fold_evidence"]["complete_fold_and_leading_bounds"])
    direct=whole.decode(case["direct_leading_evidence"]["direct_b0_ordinary_derivatives"])
    forcing=whole.decode(case["first_forcing_evidence"]["complete_degree_zero_first_forcing"])
    wa=up(box(domain["full_canonical_a1_sup"]));wb=up(box(domain["full_canonical_b1_sup"]))
    det_inv=f["Bi"]*f["Bi"]
    ai=f["M"]*det_inv;bi=direct["0,0"]*det_inv;ti=f["TM"]*bi
    result={
        "A":(f["Ap"],RG,SG),
        "chi":(ex(RG)*(c["D"][0]*f["E"]+f["Q"]*f["TM"]*f["BT"]),RG,SG),
        "G":(f["G"],RG,SG),"a0":(f["M"],RG,SG),"b0":(direct["0,0"],RG,SG),
        "T":(f["TM"],RG,SG),"Q":(f["Q"],RG,SG),"Xp":(f["E"],RG,SG),
        "F0":(forcing["Fb"],RHO,SIGMA),"F1":(forcing["Fa"],RHO,SIGMA),
        "f0":(bi*forcing["Fb"]+ai*forcing["Fa"],RHO,SIGMA),
        "f1":(ai*forcing["Fb"]+ti*forcing["Fa"],RHO,SIGMA),
        "Z0":(ai*wa+ti*wb,RHO,SIGMA),"Z1":(bi*wa+ai*wb,RHO,SIGMA),
        "w1a":(wa,RHO,SIGMA),"w1b":(wb,RHO,SIGMA)}
    return {k:(up(v[0]),v[1],v[2]) for k,v in result.items()},f,c


def joint_coefficient_norms(poly,width,order):
    """One complete coefficient pass, all angular orders, no circular transform."""
    result=[arb(0) for _ in range(order+1)]
    for j,z in enumerate(poly.c,poly.lo):
        term=up(z)*L.fourier_weight(abs(j),str(width))
        for q in range(order+1):
            result[q]+=term;term*=4*abs(j)
    return [record(v.upper()) for v in result]

def complete_radius_augmented(original,correction,analytic_coefficients):
    """Reference signed Nraw plus its complete correlated difference."""
    w=correction["w"];dn=correction["dN"];rows=[]
    for old in original["budgets"]:
        width=Q(old["exact_output_phi_width"])
        vals=whole.decode(old["first_amplitude_budgets"])
        out={}
        for j,key in enumerate(("a1","b1")):
            sup={};wiener={};parts={}
            for p in range(3):
                for q in range(4):
                    if p+q>w[j].n:raise ValueError("missing full first-correction mixed jet")
                    diff=w[j].get(p,q,"delta")
                    dw,factor=A.superscript_conversion(diff,FINAL,width)
                    tag=str(p)+","+str(q)
                    sup[tag]=(vals[key]["strip_sup"][tag]+diff).upper()
                    wiener[tag]=(vals[key]["Wiener"][tag]+dw).upper()
                    parts[tag]=dict(original_complete_reference=vals[key]["parts"][tag],
                        complete_actual_difference_strip_sup=diff,
                        complete_joint_Fourier_difference=dw,
                        exact_difference_strip=str(FINAL),
                        complete_two_sided_geometric_sum=factor)
            out[key]=dict(strip_sup=sup,Wiener=wiener,parts=parts)
        rv=whole.decode(old["complete_Nraw_derivative_budgets"]);nv={space:{k:{} for k in ("a","b")}
            for space in ("strip_sup","Wiener")}
        for j,key in enumerate(("a","b")):
            for q in range(3):
                diff=dn[j].get(0,q)
                dw,_=A.superscript_conversion(diff,FINAL,width)
                nv["strip_sup"][key][str(q)]=(rv["strip_sup"][key][str(q)]+diff).upper()
                nv["Wiener"][key][str(q)]=(rv["Wiener"][key][str(q)]+dw).upper()
        rows.append(dict(exact_output_phi_width=str(width),exact_rho_cover=original["exact_physical_rho_cover"],
            first_amplitude_budgets=pack(out),complete_Nraw_derivative_budgets=pack(nv),
            original_correlated_reference_radius_budget_payload_sha256=payload_sha(old),
            reference_and_difference_added_before_any_source_norm=True,
            complete_Nraw_not_divided_by_mu=True,
            strip_sup_and_joint_sum_of_radial_suprema_separately_paid=True))
    return dict(complete=True,budgets=rows,exact_physical_rho_cover=original["exact_physical_rho_cover"],
        complete_actual_complex_coefficient_jets=pack(analytic_coefficients),
        exact_complex_coefficient_strip=str(FORCING),
        all_original_known_reference_coefficients_and_full_tails_retained=True)

def source_row(piece_id,common,conversion,budget,profile):
    real=whole.decode(common["bounds"]);p=whole.decode(profile["payload"]["numeric"])
    # The profile is the actual physical phase on R=1/1000, not the auxiliary phase.
    rv=dict(U=[real["U"]],V=[real["V"]],D=real["D"],em=real["eta_lower"])
    def row(width):return next(v for v in budget["budgets"] if Q(v["exact_output_phi_width"])==width)
    rbudget=row(Q(0));abudget=row(Q(1,512))
    rj=inner.amplitude_jets(rbudget,rv,p["PQ"])
    # These are fresh joint Fourier majorants of the same actual two-piece
    # cubic differences on FORCING. No real-circle bound is promoted to a strip.
    cv=whole.decode(budget["complete_actual_complex_coefficient_jets"])
    if not Q(budget["exact_complex_coefficient_strip"])>Q(1,512):
        raise ValueError("the actual complete coefficient strip was lost")
    aj=inner.amplitude_jets(abudget,cv,p["PQ"])
    side="negative" if piece_id==2548 else "positive"
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
    for name in ("repo-root","manifest","out"):parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new neighboring-piece mathematics runs only in the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise RuntimeError("the immutable completed mathematical runtime changed")
    if args.out.exists():raise FileExistsError("preserve every earlier complete or failed mathematical native")
    ctx.prec=320;ctx.cap=4;start=time.monotonic()
    doc=dict(kind="actual_correlated_adjacent_piece_first_Airy_sources",complete=False,proved=False,
        failure=None,gates=[],stages={},pieces=[],case_stages=[],cases=[],runtime=runtime,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),algebra_sha256=sha(A.__file__),Laurent_algebra_sha256=sha(L.__file__),
        input_manifest_sha256=sha(args.manifest),contract_sha256=CONTRACT,
        original_whole_piece_native_sha256=WHOLE,original_whole_piece_source_sha256=WSOURCE,
        original_whole_piece_manifest_sha256=WMANIFEST,original_Taylor_native_sha256=whole.TAYLOR,
        original_higher_intrinsic_native_sha256=HIGHER,original_auxiliary_intrinsic_native_sha256=INTRINSIC,
        fixed_intrinsic_parameter="eta_0",exact_real_delta_radius=str(DELTA),
        exact_complex_coefficient_delta_radius=str(DELTA),exact_root_interval=list(map(str,ROOTS)),
        original_root_piece=2549,physical_neighbor_pieces=list(PIECES),input_cutoff=CUTOFF,
        exact_positive_body_cut=str(whole.BODY),actual_first_correction_density="n^(1/6), n=4|j|",
        source_window="ordinary L2_r of the complete H^(-2/3) old-circle first row and independent even mean",
        original_targets_FFT_intrinsic_root_cubics_finite_coefficients_and_saved_norms_recomputed=0,
        original_matrix_words_phase_profiles_or_old_exterior_source_rows_recomputed=0,
        new_exact_cubic_difference_stages=0,new_intrinsic_consumption_stages=0,
        new_reference_coefficient_norm_stages=0,new_piece_comparison_stages=0,
        new_reference_radius_budgets=0,new_complete_source_rows=0,new_case_summaries=0,
        reused_new_stages=0,recovered_unindexed_complete_stages=0,
        copied_original_complete_rows=0,original_complete_physical_seams_retained=1079,
        original_complete_normalized_seam_rows_retained=653,
        all_original_failed_large_radius_results_retained=True,
        old_circle_nine_terms_and_five_independent_mean_terms_retained=True,
        original_physical_or_parameter_family_replaced=False,
        complete_corrected_seam_operator_paid=False,full_strong_return_or_high_inverse_claimed=False)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(args.out,doc)
    def gate(name,value):
        ok=bool(value);doc["gates"].append(dict(name=name,passed=ok))
        if not ok:raise ValueError("adjacent-piece gate failed: "+name)
    def stage(name,kind,build):
        if not name.replace("-","").replace("_","").isalnum():raise ValueError("unsafe stage name")
        path=args.out.parent/"stages"/(name+".json.gz")
        if name in doc["stages"]:
            value=checked(path,doc["stages"][name]);doc["reused_new_stages"]+=1
        elif path.exists():
            value=read(path);doc["recovered_unindexed_complete_stages"]+=1
        else:
            payload=pack(build())
            value=dict(name=name,stage=name,stage_kind=kind,complete=True,
                source_sha256=doc["source_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
                algebra_sha256=doc["algebra_sha256"],runtime=runtime,
                payload_sha256=payload_sha(payload),payload=payload)
            save(path,value)
            doc[kind]+=1
        if not (value.get("complete") is True and value.get("name")==name and value.get("stage")==name
            and value.get("stage_kind")==kind and value.get("source_sha256")==doc["source_sha256"]
            and value.get("input_manifest_sha256")==doc["input_manifest_sha256"]
            and value.get("algebra_sha256")==doc["algebra_sha256"] and value.get("runtime")==runtime
            and value.get("payload_sha256")==payload_sha(value.get("payload"))):
            raise ValueError("a complete new natural stage changed its scientific identity")
        doc["stages"][name]=dict(file=str(path.relative_to(args.out.parent)),bytes=path.stat().st_size,
            sha256=sha(path),stage_kind=kind)
        checkpoint();return value["payload"]
    try:
        manifest=read(args.manifest)
        gate("the immutable public task selects precisely the two true physical neighbors",
            manifest["public_repository"]==PUBLIC and manifest["mathematical_parameters"]["physical_pieces"]==list(PIECES)
            and manifest["mathematical_parameters"]["original_root_piece"]==2549)
        pins={}
        for pin in manifest["files"]:
            path=args.repo_root/pin["path"]
            if not path.is_file() or path.stat().st_size!=pin["bytes"] or sha(path)!=pin["sha256"]:
                raise ValueError("a pinned complete mathematical input changed: "+pin["path"])
            pins[str(path.resolve())]=pin
        paths={key:args.repo_root/value for key,value in manifest["input_paths"].items()}
        old,wp,tn,tp,hn,hp,aux,ap,ind,ip,nn,npdoc=[read(paths[key]) for key in
            ("whole_native","whole_process","Taylor_native","Taylor_process","higher_native","higher_process",
            "auxiliary_native","auxiliary_process","intrinsic_domain_native","intrinsic_domain_process",
            "Nraw_native","Nraw_process")]
        gate("all original successful mathematics is consumed with its exact native and process identities",
            sha(paths["whole_native"])==WHOLE and sha(paths["whole_process"])==WPROC
            and sha(paths["Taylor_native"])==whole.TAYLOR and sha(paths["Taylor_process"])==whole.TPROC
            and sha(paths["higher_native"])==HIGHER and sha(paths["higher_process"])==HPROC
            and sha(paths["auxiliary_native"])==whole.AUX and sha(paths["auxiliary_process"])==whole.APROC
            and sha(paths["intrinsic_domain_native"])==INTRINSIC and sha(paths["intrinsic_domain_process"])==IPROC
            and sha(paths["Nraw_native"])==whole.NRAW and sha(paths["Nraw_process"])==whole.NPROC
            and all(native_success(x,p) for x,p in ((tn,tp),(hn,hp),(aux,ap),(nn,npdoc)))
            and old["complete"] and old["proved"] and old["failure"] is None
            and old["source_sha256"]==WSOURCE and old["input_manifest_sha256"]==WMANIFEST
            and wp["actual_returncode"]==0 and wp["mathematical_complete"]
            and all(g["passed"] for g in old["gates"]) and len(old["gates"])==10)
        gate("the original complete family root parameter and preserved physical seam ledger agree",
            sha(paths["contract"])==CONTRACT
            and tn["exact_root_interval"]==old["exact_root_interval"]==aux["exact_root_interval"]==list(map(str,ROOTS))
            and tn["exact_fixed_intrinsic_parameter"]==hn["exact_fixed_intrinsic_parameter"]
            and old["original_complete_physical_seams_retained"]==1079
            and old["original_complete_normalized_seam_rows_retained"]==653
            and tn["old_product_domain"]==old["original_complete_holomorphic_product"]
            and old["original_Taylor_native_sha256"]==whole.TAYLOR
            and old["original_Nraw_native_sha256"]==whole.NRAW
            and tn["complete_branch_identity"]["same_complex_delta_without_conjugation"])
        doc["exact_fixed_intrinsic_parameter"]=tn["exact_fixed_intrinsic_parameter"]
        doc["original_complete_branch_identity"]=copy.deepcopy(tn["complete_branch_identity"])
        doc["both_original_Airy_carrier_branches_retained"]=True
        doc["original_formatter_failure_preserved"]=copy.deepcopy(wp.get("failure"))
        doc["original_complete_case_summaries"]=copy.deepcopy(old["cases"])
        doc["original_complete_natural_stage_receipts"]=copy.deepcopy(old["stages"])
        doc["original_complete_case_receipts"]=copy.deepcopy(old["case_stages"])
        if args.resume:
            previous=read(args.resume)
            same=("source_sha256","algebra_sha256","Laurent_algebra_sha256","input_manifest_sha256",
                "runtime","original_whole_piece_native_sha256","original_Taylor_native_sha256",
                "original_higher_intrinsic_native_sha256","original_auxiliary_intrinsic_native_sha256")
            gate("every resumed new natural prefix retains its exact reviewed scientific identity",
                all(previous.get(k)==doc.get(k) for k in same))
            # Include atomically completed files that preceded their index update. Partial files
            # are never accepted. Each is checked again when its named stage is consumed.
            for source in sorted((args.resume.parent/"stages").glob("*.json.gz")):
                value=read(source)
                if not (value.get("complete") is True and value.get("source_sha256")==doc["source_sha256"]
                    and value.get("input_manifest_sha256")==doc["input_manifest_sha256"]
                    and value.get("algebra_sha256")==doc["algebra_sha256"] and value.get("runtime")==runtime
                    and value.get("payload_sha256")==payload_sha(value.get("payload"))
                    and source.name==value.get("name","")+".json.gz"):
                    raise ValueError("a proposed completed new prefix has an invalid original identity")
                target=args.out.parent/"stages"/source.name
                target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
            doc["stages"]=copy.deepcopy(previous["stages"])
            for name,entry in doc["stages"].items():checked(args.out.parent/entry["file"],entry)
            doc["preserved_original_new_prefix"]=dict(native_sha256=sha(args.resume),complete=previous["complete"],
                failure=previous["failure"],gates=previous["gates"],original_stage_count=len(previous["stages"]))
        checkpoint()
        cp,zp=[read(paths[k]) for k in ("candidate_index","response_index")]
        alpha=Q(cp["metadata"]["exact_float_amplitude"])
        gate("the same complete 65 and 193 cubics retain their actual amplitude and independent mean",
            sha(paths["candidate_index"])==CANDIDATE and sha(paths["response_index"])==RESPONSE
            and cp["coefficient_shape"]==[4,6144,65] and zp["coefficient_shape"]==[4,6144,193]
            and alpha==Q(6890507429876859,9007199254740992)
            and zp["metadata"]["finite_head_mean_was_not_removed_from_the_solve"])
        shards={}
        for key,index,first,end,count,expected in (
            ("candidate",cp,1346,2692,65,CSHARD),("response",zp,2265,2718,193,ZSHARD)):
            path=paths[key+"_shard"]
            parts=index.get("parts",index.get("shards",[]))
            part=next(x for x in parts if x["first_interval"]==first)
            if not (part["last_interval_exclusive"]==end and part["sha256"]==sha(path)==expected
                and part["file"]==path.name and part["bytes"]==path.stat().st_size):
                raise ValueError("an original complete cubic shard changed")
            with np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False) as z:
                nodes=z["radial_nodes"].copy();coeff=z["piece_coefficients"].copy()
            if not (nodes.shape==(end-first+1,) and coeff.shape==(4,end-first,count)
                and np.isfinite(nodes).all() and np.isfinite(coeff).all() and (np.diff(nodes)>0).all()):
                raise ValueError("the whole original cubic component arrays are incomplete")
            shards[key]=(nodes,coeff)
        def accepted(native,key,base,oldsource,newsource,newmanifest):
            oldkey=key in native.get("original_stages",{})
            entry=(native["original_stages"] if oldkey else native["stages"])[key]
            path=base/entry["file"]
            if str(path.resolve()) not in pins:raise ValueError("an accepted old finite file is not pinned: "+key)
            value=checked(path,entry)
            source=oldsource if oldkey else newsource
            m=whole.numerator.OLD_MANIFEST if oldkey else newmanifest
            if not (value["complete"] and value.get("stage",value.get("name"))==key
                and value["source_sha256"]==source and value["input_manifest_sha256"]==m):
                raise ValueError("an accepted original finite degree changed its own source or manifest")
            return value["payload"]
        def tstage(key):
            return accepted(tn,key,paths["Taylor_native"].parent,whole.numerator.OLD_SOURCE,whole.TSOURCE,whole.TMANIFEST)
        def nstage(key):
            return accepted(nn,key,paths["Nraw_native"].parent,whole.numerator.OLD_SOURCE,whole.NSOURCE,whole.NMANIFEST)
        background={k:L.unpack_series(v) for k,v in tstage("complete-background-root-series")["series"].items()}
        coeff={"chi":[],"A":[]}
        for degree in range(15):
            row=tstage("fold-degree-"+str(degree).zfill(3))
            if row["degree"]!=degree:raise ValueError("a saved fold degree moved")
            for key in coeff:coeff[key].append(L.LP.restore(row[key]))
        for key in ("G","a0","b0","T","Q","Xp"):
            row=tstage("leading-complete-"+key)
            coeff[key]=L.unpack_series(row["coefficients"])
            if row["name"]!=key or len(coeff[key])!=9:raise ValueError("a complete original leading prefix changed")
            for degree in range(9,15):
                v=tstage("leading-"+key+"-degree-"+str(degree).zfill(3))
                if v["name"]!=key or v["degree"]!=degree:raise ValueError("a saved appended leading degree changed")
                coeff[key].append(L.LP.restore(v["coefficient"]))
        for key in ("F0","F1","f0","f1","Z0","Z1","w1a","w1b"):coeff[key]=[]
        for degree in range(13):
            force=tstage("forcing-degree-"+str(degree).zfill(3))
            normal=tstage("normalized-forcing-degree-"+str(degree).zfill(3))
            transp=tstage("transport-degree-"+str(degree).zfill(3))
            first=tstage("first-correction-degree-"+str(degree).zfill(3))
            for name,row,key in (("F0",force,"Fb"),("F1",force,"Fa"),("f0",normal,"fa"),("f1",normal,"fb"),
                ("Z0",transp,"A"),("Z1",transp,"B"),("w1a",first,"a1"),("w1b",first,"b1")):
                if row["degree"]!=degree:raise ValueError("a saved complete reference coefficient moved degree")
                coeff[name].append(L.LP.restore(row[key]))
        gate("only complete original coefficients through fourteen and twelve are loaded, including all means",
            all(len(coeff[k])==15 for k in ("chi","A","G","a0","b0","T","Q","Xp"))
            and all(len(coeff[k])==13 for k in ("F0","F1","f0","f1","Z0","Z1","w1a","w1b"))
            and coeff["chi"][0].is_zero() and coeff["w1a"][0].is_zero())
        tnorm={};nnorm={}
        for width in WIDTHS:
            tag=str(width.numerator)+"_"+str(width.denominator)
            tnorm[str(width)]=[tstage("full-Fourier-norm-"+tag+"-degree-"+str(j).zfill(3)) for j in range(13)]
            nnorm[str(width)]=[nstage("full-Nraw-Fourier-norm-"+tag+"-degree-"+str(j).zfill(3)) for j in range(11)]
        multi=nstage("complete-local-numerator-whole-product-multipliers")
        multipliers=whole.decode(multi["complete_multiplier_bounds"])
        amp={k:up(box(tn["old_product_domain"]["full_canonical_"+v+"_sup"]))
            for k,v in (("a","a1"),("b","b1"))}
        case=aux["cases"][1]
        gate("the complete auxiliary leading and first-correction products retain their original domains",
            case["complete"] and case["proved"] and case["failure"] is None
            and all(g["passed"] for g in case["gates"])
            and Q(case["exact_fold_radius"])==RG and Q(case["exact_old_leading_width"])==SG
            and Q(tn["old_product_domain"]["exact_rho_radius"])==RHO
            and Q(tn["old_product_domain"]["exact_phi_width"])==SIGMA)
        majorant_record=stage("complete-original-reference-holomorphic-majorants",
            "new_piece_comparison_stages",lambda:dict(zip(("majorants","fold","coefficients"),
                reference_majorants(case,tn["old_product_domain"]))))
        decoded=unpack(majorant_record)
        majors={k:(v[0],Q(v[1]),Q(v[2])) for k,v in decoded["majorants"].items()}
        fold=decoded["fold"]
        def complete_reference(H,width,leading_only=False):
            ans={}
            for name,cs in coeff.items():
                if leading_only and name in ("F0","F1","f0","f1","Z0","Z1","w1a","w1b"):continue
                M,R,S=majors[name]
                if not (Q(H)<R and width<S):raise ValueError("a reference coefficient request leaves its paid product")
                tag=str(width.numerator)+"-"+str(width.denominator)
                name_stage="reference-Fourier-norms-"+name+"-"+tag
                def build(cs=cs,name=name,width=width):
                    return dict(field=name,exact_width=str(width),
                        norms=[joint_coefficient_norms(v,width,8) for v in cs],
                        full_coefficients_and_all_outputs_retained=True,
                        joint_sum_after_each_complete_coefficient_modulus=True,
                        original_finite_coefficients_recomputed=False)
                payload=stage(name_stage,"new_reference_coefficient_norm_stages",build)
                if payload["field"]!=name or Q(payload["exact_width"])!=width:
                    raise ValueError("an accepted new norm changed field or width")
                norms=[[up(box(v)) for v in row] for row in payload["norms"]]
                ans[name]=A.mixed_sup_from_norms(norms,H,R,S,width,M,8,3)
            if not leading_only:
                ans["F"]=[ans.pop("F0"),ans.pop("F1")]
                ans["f"]=[ans.pop("f0"),ans.pop("f1")]
                ans["Z"]=[ans.pop("Z0"),ans.pop("Z1")]
                ans["w1"]=[ans.pop("w1a"),ans.pop("w1b")]
            return ans
        bstar_row=stage("complete-root-bstar-polynomial-norms-at-one-thirtytwo",
            "new_reference_coefficient_norm_stages",lambda:dict(exact_width="1/32",
                complete_bstar=joint_coefficient_norms(coeff["f1"][0],Q(1,32),2),
                complete_root_mean_retained=True,full_exact_root_coefficient_recomputed=False))
        bstar=[up(box(x)) for x in bstar_row["complete_bstar"]]
        intrinsic_case=next(v for v in ind["cases"] if Q(v["exact_auxiliary_radius"])==RC)
        rect=intrinsic_case["exact_complex_rectangle"]
        gate("the entire true-root-centred intrinsic disk lies in the same proved complex rectangle",
            intrinsic_case["complete"] and intrinsic_case["proved"] and intrinsic_case["failure"] is None
            and Q(rect["real_interval"][0])<=ROOTS[0]-RC
            and Q(rect["real_interval"][1])>=ROOTS[1]+RC
            and Q(rect["imaginary_half_width"])>=RC
            and ip["native_sha256"]==INTRINSIC
            and Q(ip["cases"][1]["exact_auxiliary_radius"])==RC
            and ip["cases"][1]["proved"] and ip["cases"][1]["failure"] is None
            and hn["intrinsic_stage"]["complete"]
            and hn["at_the_certified_true_root"]["exact_K0"]=="0")
        original_raw=hn["intrinsic_stage"]["ordinary_old_radial_jets"]
        third={key:ip["cases"][1]["complete_intrinsic"]["ordinary_jet_modulus_upper"][key][3]
            for key in ("K","beta","gamma","s")}
        # The summary is used only after its complete native/source/domain identity above.
        # Match each complete native third-jet enclosure to the already stored process value.
        doc["original_intrinsic_third_derivative_upper_records"]=copy.deepcopy(third)
        norm=read(paths["moment_native"]);converted=read(paths["conversions"])
        nr=norm["coefficient_rows"];zr=converted["rows"]
        gate("all complete moment and old-circle matrix words remain the same accepted rows",
            sha(paths["moment_native"])==whole.MOMENT and sha(paths["conversions"])==whole.CONVERSIONS
            and len(nr)==len(zr)==1328 and norm["complete"] and norm["proved"]
            and converted["complete"]
            and all(n["common_row"]==z["common_row"]==j and n["interval"]==z["interval"]
                and z["original_moment_row_payload_sha256"]==payload_sha(n)
                for j,(n,z) in enumerate(zip(nr,zr))))
        bcase=read(paths["bstar_case_0"])
        profile=bcase["complete_new_profile"]
        gate("the original actual physical phase supplies complete all-output profiles on both neighboring pieces",
            bcase["complete"] and Q(bcase["exact_radius"])==Q(1,1000)
            and profile["complete"] and profile["payload_sha256"]==payload_sha(profile["payload"])
            and profile["payload"]["exact_old_phi_width"]==str(Q(1,512))
            and profile["payload"]["exact_input_cutoff"]==CUTOFF)
        all_new_rows={}
        for piece in PIECES:
            raw=stage("exact-signed-cubic-difference-"+str(piece),"new_exact_cubic_difference_stages",
                lambda piece=piece:exact_cubic_difference(piece,shards,alpha))
            left,right=map(Q,raw["interval"]);entry=Q(raw["exact_entry_seam"])
            side="negative" if piece==2548 else "positive"
            rinterval=(ROOTS[0]-right,ROOTS[1]-left)
            h=min(abs(x) for x in rinterval);H=max(abs(x) for x in rinterval)
            gate("physical piece "+str(piece)+" retains its whole scalar germ strict-side and auxiliary product identities",
                GERM[0]<=left<right<=GERM[1] and 0<h<=H<RHO
                and (right<=ROOTS[0] if side=="negative" else left>=ROOTS[1])
                and (entry==whole.PIECE[0] if piece==2548 else entry==whole.PIECE[1]))
            ib=stage("same-intrinsic-root15-and-third-tail-"+str(piece),"new_intrinsic_consumption_stages",
                lambda rinterval=rinterval:dict(exact_rho_interval=list(map(str,rinterval)),
                    exact_Cauchy_radius=str(RC),
                    complete_jets=A.intrinsic_boxes(original_raw,third,rinterval,RC),
                    old_root_derivatives_and_complex_targets_recomputed=False))
            intrinsic=unpack(ib["complete_jets"])
            def compare():
                du,dv=cubic_difference_jets(raw)
                rho=ex(rinterval[0]).union(ex(rinterval[1]))
                ubar,vbar=A.evaluate_old_background(background,intrinsic,rho)
                cwide=A.background_pairs(ubar,vbar,du,dv,intrinsic,WIDE)
                cforce=A.background_pairs(ubar,vbar,du,dv,intrinsic,FORCING)
                refwide=complete_reference(H,WIDE,True)
                refforce=complete_reference(H,FORCING,False)
                length=ex(right-left)
                phase=A.phase_comparison(cwide,refwide,ex(h),ex(H),length,WIDE,PHASE_FLOW,
                    FORCING,fold["Am"].lower(),side,local_coefficients=cforce,local_reference=refforce)
                phase.update(h=ex(h),H=ex(H),side=side)
                if not ex(FORCING)+refforce["chi"].get()+phase["X"].get(which="delta")<ex(Q(1,32)):
                    raise ValueError("complete root bstar compositions leave their actually paid polynomial strip")
                force=A.forcing_comparison(cforce,phase,refforce,fold["mu"].lower(),fold["Bi"])
                correction=A.correction_comparison(cforce,phase,force,refforce,bstar,length,
                    FORCING,CORRECTION_FLOW,FINAL)
                return dict(piece=piece,interval=list(map(str,(left,right))),side=side,
                    exact_entry_seam=str(entry),exact_min_root_distance=str(h),exact_max_root_distance=str(H),
                    exact_characteristic_widths=dict(wide=str(WIDE),phase_flow=str(PHASE_FLOW),
                        forcing=str(FORCING),correction_flow=str(CORRECTION_FLOW),final=str(FINAL)),
                    phase={k:pack(v) for k,v in phase.items()},
                    complete_background_difference_jets={k:pack(v) for k,v in cforce.items()},
                    complete_actual_complex_coefficient_jets=pack(dict(
                        U=[[cforce["u"].get(0,q,"actual") for q in range(4)]],
                        V=[[cforce["v"].get(0,q,"actual") for q in range(4)]],
                        D=[cforce["d"].get(0,q,"actual") for q in range(4)],
                        em=cforce["eta_gap_actual"])),
                    forcing={k:pack(v) for k,v in force.items()},
                    correction={k:pack(v) for k,v in correction.items()},
                    complete_barred_nonzero_entry_traces_retained=True,
                    only_exact_same_construction_entry_differences_zero=True,
                    actual_physical_radial_derivative_jumps_retained=True,
                    all_jets_are_strip_suprema_before_explicit_joint_Fourier_conversion=True)
            comparison=stage("complete-correlated-phase-forcing-and-w1-"+str(piece),
                "new_piece_comparison_stages",compare)
            cor=comparison["correction"]
            correction={k:[A.J.restore(v) for v in cor[k]] for k in ("w","Z","dN")}
            original_radius=stage("complete-reference-radius-"+str(H.numerator)+"-"+str(H.denominator),
                "new_reference_radius_budgets",lambda H=H:whole.radius_budget(H,tnorm,nnorm,
                    tn["first_correction_derivative_budgets"],nn["complete_correlated_Nraw_budgets"],
                    multipliers,amp))
            budget=stage("complete-adjacent-piece-amplitude-and-Nraw-"+str(piece),
                "new_piece_comparison_stages",lambda:complete_radius_augmented(original_radius,correction,
                    unpack(comparison["complete_actual_complex_coefficient_jets"])))
            plan=[n for n in nr if left<=Q(n["interval"][0])<Q(n["interval"][1])<=right]
            if not plan or Q(plan[0]["interval"][0])!=left or Q(plan[-1]["interval"][1])!=right:
                raise ValueError("the original complete common grid does not cover the genuine whole neighbor")
            if any(a["interval"][1]!=b["interval"][0] for a,b in zip(plan,plan[1:])):
                raise ValueError("the original complete common neighbor grid has a gap")
            piece_rows=[]
            for n in plan:
                j=n["common_row"]
                row=stage("complete-neighbor-"+str(piece)+"-common-"+str(j).zfill(4),
                    "new_complete_source_rows",lambda n=n,j=j:source_row(piece,n,zr[j],budget,profile))
                if not (row["common_row"]==j and row["interval"]==n["interval"] and row["original_piece"]==piece
                    and row["original_moment_row_payload_sha256"]==payload_sha(n)):
                    raise ValueError("a complete new source row moved to a different physical interval")
                all_new_rows[(piece,j)]=row;piece_rows.append(row)
            summary=stage("complete-neighbor-piece-summary-"+str(piece),
                "new_piece_comparison_stages",lambda:whole.channel_sum(piece_rows))
            doc["pieces"].append(dict(piece=piece,interval=list(map(str,(left,right))),side=side,
                complete_summary_stage="complete-neighbor-piece-summary-"+str(piece),
                exact_entry_seam=str(entry),complete_common_rows=len(piece_rows),
                complete_comparison_stage="complete-correlated-phase-forcing-and-w1-"+str(piece),
                full_complete_source_summary=summary))
            checkpoint()
        for ci,radius in enumerate(whole.RADII):
            original_path=paths["whole_case_"+str(ci)]
            original=checked(original_path,old["case_stages"][ci])
            if not (original["complete"] and original["source_sha256"]==WSOURCE
                and original["input_manifest_sha256"]==WMANIFEST and Q(original["exact_radius"])==radius
                and original["complete_case_summary"]==old["cases"][ci]):
                raise ValueError("a complete original six-radius natural case changed its full identity")
            def select_rows():
                roles=[]
                for oldserial,oldrow in enumerate(original["rows"]):
                    key=(oldrow["original_piece"],oldrow["common_row"])
                    if key in all_new_rows:
                        newrow=all_new_rows[key]
                        if oldrow["interval"]!=newrow["interval"] or oldrow["side"]!=newrow["side"]:
                            raise ValueError("a new complete row changed its original physical measure")
                        stage_name="complete-neighbor-"+str(key[0])+"-common-"+str(key[1]).zfill(4)
                        common=dict(oldserial=oldserial,stage=stage_name,
                            original_complete_row_payload_sha256=payload_sha(oldrow),
                            new_complete_row_payload_sha256=payload_sha(newrow))
                        if up(box(oldrow["complete_squared_source_integral"]))<=up(box(newrow["complete_squared_source_integral"])):
                            roles.append(dict(kind="copied_original_better_complete_bound",**common))
                        else:roles.append(dict(kind="new_complete_neighbor_bound",**common))
                    else:
                        roles.append(dict(kind="copied_original_complete_row",oldserial=oldserial,
                            original_complete_row_payload_sha256=payload_sha(oldrow)))
                return dict(original_complete_case_sha256=sha(original_path),exact_radius=str(radius),
                    row_roles=roles,complete=True,
                    selection_of_whole_upper_envelopes_only=True,
                    no_subtraction_of_original_upper_integrals=True)
            selected=stage("complete-neighbor-selection-radius-"+str(ci),
                "new_piece_comparison_stages",select_rows)
            if not (selected["complete"] and selected["original_complete_case_sha256"]==sha(original_path)
                and selected["exact_radius"]==str(radius) and len(selected["row_roles"])==len(original["rows"])):
                raise ValueError("a complete new row selection changed its original case")
            rows=[];roles=selected["row_roles"];fresh=0
            for oldserial,role in enumerate(roles):
                oldrow=original["rows"][oldserial]
                if role["oldserial"]!=oldserial or role["original_complete_row_payload_sha256"]!=payload_sha(oldrow):
                    raise ValueError("a saved row selection changed original byte lineage")
                kind=role["kind"]
                if kind in ("copied_original_better_complete_bound","new_complete_neighbor_bound"):
                    key=(oldrow["original_piece"],oldrow["common_row"]);newrow=all_new_rows[key]
                    stage_name="complete-neighbor-"+str(key[0])+"-common-"+str(key[1]).zfill(4)
                    if role["stage"]!=stage_name or role["new_complete_row_payload_sha256"]!=payload_sha(newrow):
                        raise ValueError("a saved complete new candidate changed its independent stage")
                if kind=="new_complete_neighbor_bound":
                    rows.append(copy.deepcopy(newrow));fresh+=1
                elif kind in ("copied_original_complete_row","copied_original_better_complete_bound"):
                    rows.append(copy.deepcopy(oldrow));doc["copied_original_complete_rows"]+=1
                else:raise ValueError("an accepted case used an undeclared row role")
            def summarize():
                result=copy.deepcopy(original["complete_case_summary"])
                result["source_summary"]={side:whole.channel_sum([r for r in rows if r["side"]==side])
                    for side in ("negative","positive")}
                collar=[r for r in rows if r["side"]=="positive" and Q(r["interval"][1])<=whole.BODY]
                body=[r for r in rows if r["side"]=="positive" and Q(r["interval"][0])>=whole.BODY]
                if len(collar)+len(body)!=len([r for r in rows if r["side"]=="positive"]):
                    raise ValueError("a true positive body cut was lost")
                result["source_summary"]["positive_collar"]=whole.channel_sum(collar)
                result["source_summary"]["positive_body"]=whole.channel_sum(body)
                result["complete_rows"]=len(rows)
                ng=up(box(result["original_actual_negative_source_to_primitive_L2_gain"]))
                result["negative_first_correction_source_component_Hminus4over3_to_primitive_L2"]=record(
                    (ng*up(box(result["source_summary"]["negative"]["complete_first_correction_ordinary_L2_source"]))).upper())
                for side,key in (("positive_collar","positive_collar_first_correction_source_L2"),
                    ("positive_body","positive_body_first_correction_source_L2")):
                    result[key]=copy.deepcopy(result["source_summary"][side]["complete_first_correction_ordinary_L2_source"])
                result["new_complete_neighbor_rows_selected"]=fresh
                result["original_complete_case_payload_sha256"]=payload_sha(original["complete_case_summary"])
                result["only_two_genuine_neighboring_pieces_reestimated"]=True
                return result
            summary=stage("complete-six-radius-summary-"+str(ci),"new_case_summaries",summarize)
            case_out=copy.deepcopy(original)
            case_out.update(kind="complete_correlated_adjacent_piece_first_Airy_source_radius",
                source_sha256=doc["source_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
                algebra_sha256=doc["algebra_sha256"],runtime=runtime,complete=True,rows=rows,row_roles=roles,
                original_complete_case_sha256=sha(original_path),complete_case_summary=summary,
                summary_stage="complete-six-radius-summary-"+str(ci),
                selection_stage="complete-neighbor-selection-radius-"+str(ci),
                exact_old_physical_seams_and_full_independent_means_preserved=True)
            path=args.out.parent/"cases"/("radius-"+str(radius.numerator)+"-"+str(radius.denominator)+".json.gz")
            save(path,case_out)
            doc["case_stages"].append(dict(file=str(path.relative_to(args.out.parent)),
                bytes=path.stat().st_size,sha256=sha(path),exact_radius=str(radius)))
            doc["cases"].append(summary);checkpoint()
        gate("both actual neighbors and all six complete source cases retain every other original row and seam",
            len(doc["pieces"])==2 and len(doc["cases"])==len(doc["case_stages"])==6
            and doc["original_complete_physical_seams_retained"]==1079
            and doc["original_complete_normalized_seam_rows_retained"]==653
            and all(doc[k]==0 for k in (
                "original_targets_FFT_intrinsic_root_cubics_finite_coefficients_and_saved_norms_recomputed",
                "original_matrix_words_phase_profiles_or_old_exterior_source_rows_recomputed")))
        gate("all source units and remaining unproved high-frequency conclusions remain explicit",
            not doc["original_physical_or_parameter_family_replaced"]
            and not doc["complete_corrected_seam_operator_paid"] and not doc["full_strong_return_or_high_inverse_claimed"]
            and doc["old_circle_nine_terms_and_five_independent_mean_terms_retained"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_stages=len(doc["stages"]),complete_pieces=len(doc["pieces"]),complete_cases=len(doc["cases"]),
            new_complete_source_rows=doc["new_complete_source_rows"],
            copied_original_complete_rows=doc["copied_original_complete_rows"],
            original_mathematical_stages_recomputed=0,native_sha256=sha(args.out),seconds=doc["seconds"]),
            allow_nan=False),flush=True)
if __name__=="__main__":main()
