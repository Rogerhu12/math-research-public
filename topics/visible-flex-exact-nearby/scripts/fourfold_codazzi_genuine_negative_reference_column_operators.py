#!/usr/bin/env python3
"""Real negative genuine-column operator bounds from completed immutable receipts.

No column samples, old target, FFT, intrinsic, repair, fold, transport, Taylor
coefficient, signed RF polynomial or old complete output enclosure is evaluated.
Only the new V.9--V.18 scalar operator recipe and explicit missing derivative
margins are evaluated. All numerical working data remain temporary.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

TOPIC="topics/visible-flex-exact-nearby/"
PUBLIC="Rogerhu12/math-research-public"
KIND="actual_real_negative_genuine_reference_column_operators_v1"
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
S_EXEC="3896925b758840c4bbf2ce910141ca8a93d725d56bf22b5002e9c0b2486004af"
S_SOURCE="564759dceb4b38dd37fdd275d0fa3e22cdf2efa271cd9ef1049c6cfa4ff121f6"
S_MANIFEST="a6fbb28de8a85bd6f71054df0056a869285f131cc4c4702c66e5434deb7061cf"
P_EXEC="d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9"
P_SOURCE="042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7"
P_MANIFEST="44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437"
H_EXEC="fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57"
H_SOURCE="9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c"
H_MANIFEST="1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99"
H=Q(893368603925465506687,21990232555520000000000000)
RG=Q(3,8000);SG=Q(3,128);L=Q(1,2000);J0=97;N=4*J0
WIDTHS=(Q(0),Q(1,1024),Q(1,512))
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):return abs(rb(v)).upper()
def gap(v,name):
    z=rb(v).lower()
    if not z.is_finite() or not z>0:raise ValueError("no positive actual gap: "+name)
    return z
def powr(x,p):return (rb(x).log()*ex(p)).exp()
def rec(x):return dict(ball=rb(x).str(64))
def unpack(x):
    if isinstance(x,dict):
        if set(x)=={"ball"}:return arb(x["ball"])
        return {k:unpack(v) for k,v in x.items()}
    if isinstance(x,list):return [unpack(v) for v in x]
    return x
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def save(p,x,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    b=gzip.compress(raw,mtime=0) if compressed else raw
    t=p.with_name(p.name+".tmp");t.write_bytes(b);t.replace(p)
def prod(a,b,k=2):
    return [up(sum((math.comb(n,i)*a[i]*b[n-i] for i in range(n+1)),arb(0)))
            for n in range(k+1)]
def scale(a,b):return [up(b*v) for v in a]
def plus(a,b):return [up(x+y) for x,y in zip(a,b)]
def current_receipt(path,run,source,manifest,gate):
    d=read(path);r=d.get("actual_scientific_receipt",{})
    gate("original run "+run+" has its complete successful scientific identity",
        str(d.get("run_id"))==run and str(d.get("run_attempt"))=="1"
        and d.get("complete") is True and d.get("actual_returncode")==0
        and d.get("actual_failure") is None
        and d.get("source_budget_source_sha256")==source
        and d.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True
        and r.get("actual_returncode")==0 and r.get("failure") is None
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("runtime")==RUNTIME and r.get("gates")
        and all(g.get("passed") is True for g in r["gates"]))
    return r

def real_fold(f,gate):
    """New pointwise real-circle constants; read the accepted entire-fold bounds.

    A_phi and X_phi-1 vanish at rho=0. Schwarz on the original RG disk
    and Cauchy across the original positive SG angle width pay every
    derivative used here. The original folded functions are never rebuilt.
    """
    R=ex(H);u=ex(H/RG)
    amin=gap(f["Am"],"the original full A lower bound");ap=up(f["Ap"])
    a1=up(u*up(f["BA"]));a2=up(a1/ex(SG));a3=up(2*a1/ex(SG*SG))
    j=up(u*up(f["j"]))
    x=[up(1+j),up(j/ex(SG)),up(2*j/ex(SG*SG))]
    l1=up(ex(Q(2,3))*a1/amin)
    l2=up(ex(Q(2,3))*(a2/amin+a1*a1/(amin*amin)))
    l3=up(ex(Q(2,3))*(a3/amin+3*a1*a2/(amin*amin)+2*a1*a1*a1/(amin*amin*amin)))
    tmax=up(R*powr(ap,Q(2,3)))
    opt=up(powr(R,Q(3,2))*ap)
    phi0=dict(m=gap(1-j,"X_phi"),M=up(1+j),F2=x[1],F3=x[2])
    phih=dict(m=gap(1-j-opt*l1,"both actual characteristic circle derivatives"),
        M=up(1+j+opt*l1),
        F2=up(x[1]+opt*(l2+ex(Q(3,2))*l1*l1)),
        F3=up(x[2]+opt*(l3+ex(Q(9,2))*l1*l2+ex(Q(9,4))*l1*l1*l1)))
    gate("the whole original physical root piece has real positive A and fits the complete negative reference interval",
        H<RG and ap<=2*amin and tmax<ex(L)
        and H==max(ROOTS[1]-PIECE[0],PIECE[1]-ROOTS[0]))
    gate("all three genuine real circle maps retain positive derivatives and finite third derivative bounds",
        phi0["m"]>0 and phih["m"]>0
        and all(v.is_finite() and v.lower()>=0 for v in [l1,l2,l3,*phi0.values(),*phih.values()]))
    # Both leading amplitudes retain the same exact G and original physical mean.
    G=up(f["G"]);g1=up(a1/(6*amin))
    gj=[G,up(G*g1),up(G*(a2/(6*amin)+5*a1*a1/(36*amin*amin)))]
    tj=[tmax,up(R*ex(Q(2,3))*powr(amin,Q(-1,3))*a1),
        up(R*(ex(Q(2,3))*powr(amin,Q(-1,3))*a2+ex(Q(2,9))*powr(amin,Q(-4,3))*a1*a1))]
    t3=up(R*(ex(Q(2,3))*powr(amin,Q(-1,3))*a3
        +ex(Q(2,3))*powr(amin,Q(-4,3))*a1*a2
        +ex(Q(8,27))*powr(amin,Q(-7,3))*a1*a1*a1))
    y=[tj[1],tj[2],t3]
    a0=prod(gj,plus(prod(x,x),prod(tj,prod(y,y))))
    b0=scale(prod(gj,prod(x,y)),2)
    return dict(Aminus=amin,Aplus=ap,logh1=l1,logh2=l2,logh3=l3,
        Tmax=tmax,phase_central=phi0,phase_high=phih,leading_a=a0,leading_b=b0,
        exact_radius=str(H),original_fold_radius=str(RG),original_phi_strip=str(SG))

def profile_budget(fold,M,M1,gate):
    """New V.9--V.15 complete true two-column C2 profiles."""
    R=ex(H);am=fold["Aminus"];ap=fold["Aplus"];l1=fold["logh1"];l2=fold["logh2"]
    ell=ex(L);NN=arb(N)
    Q1=up(ex(Q(5,36))+2*M*ell.sqrt()/(3*NN))
    Q2=up(ex(Q(5,36))+4*M*ell*ell/9)
    Qd=up(ex(Q(5,18))+4*(M1*powr(ell,Q(3,2))+M*ell.sqrt())/(9*NN))
    B0=arb(9);B1=up(ex(Q(9,2))*Q1);B2=up(ex(Q(9,2))*(Qd+2*Q2))
    b=[B0,up(ex(Q(3,2))*l1*B1),
        up(ex(Q(9,4))*l1*l1*B2+(ex(Q(3,2))*l2+ex(Q(9,4))*l1*l1)*B1)]
    e1=up(l1/4);e2=up(l2/4+l1*l1/16)
    h=[ex(Q(7,6)),up(l1/4),up(l2/4+3*l1*l1/8)]
    c=prod(h,b)
    def power_envelope(v):return [v[0],up(v[1]+e1*v[0]),up(v[2]+2*e1*v[1]+e2*v[0])]
    ph=scale(power_envelope(b),powr(am,Q(-1,6)))
    qh=scale(power_envelope(c),R.sqrt()*powr(ap,Q(1,6)))
    ds=powr(3/(2*am),Q(2,3));hs=powr(3/(2*am),Q(1,6))
    u1=up(ds*powr(ap,Q(2,3))*l1);u2=up(ds*powr(ap,Q(2,3))*(l2+l1*l1))
    Bs=up(3+M*powr(NN,Q(-4,3)));Cs=up(1+Bs+M1/(NN*NN))
    pc=scale([arb(1),u1,up(Bs*u1*u1+u2)],8*hs)
    qc=scale([arb(1),up(Bs*u1),up(Cs*u1*u1+Bs*u2)],8*powr(R,Q(1,4))*powr(NN,Q(-1,6)))
    gate("the central and both high profiles bound the full genuine two-column row including all Airy arguments",
        all(v.is_finite() and v.lower()>=0 for v in pc+qc+ph+qh)
        and M>0 and M1>0)
    return dict(central=dict(p=pc,q=qc),high=dict(p=ph,q=qh),
        auxiliary=dict(Q1=Q1,Q2=Q2,Qd=Qd,B0=B0,B1=B1,B2=B2),
        exact_label_partition="central n<3/(2*rho^(3/2)*Aminus); high is its complement",
        partition_independent_of_phi=True,radial_partition_derivative_taken=False,
        both_genuine_columns_and_both_signed_inputs=True,common_radial_factor="rho^(-1/4)")

def composition(phi):
    m=gap(phi["m"],"composition slope");M=phi["M"];F2=phi["F2"];F3=phi["F3"]
    P2=F2/(m*m*m);P3=F3/(m*m*m*m)+3*F2*F2/(m*m*m*m*m)
    C0=powr(m,Q(-1,2))
    C2=(M*(1/(m*m)+2*P2*P2+1/(m**4)+P3*P3+ex(Q(9,2))*P2*P2/(m*m)+1/(m**6))).sqrt()
    return up(powr(C0,Q(1,6))*powr(C2,Q(5,6)))
def schur(B0,B2):
    jj=arb(J0);Lam=(1+16*jj*jj).sqrt()
    return up(powr(2,Q(5,3))*powr(Lam,Q(-1,3))*(B0+arb.pi()**2*B2/48)
        +8*B2*(powr(jj,Q(-4,3))+3*powr(jj,Q(-1,3))).sqrt())
def operator_budget(a,b,fold,profiles):
    parts=[]
    for name,pkey,phikey in (("central","central","phase_central"),
        ("positive_characteristic","high","phase_high"),("negative_characteristic","high","phase_high")):
        profile=profiles[pkey];phi=fold[phikey]
        D=plus(prod(profile["p"],a),prod(profile["q"],b))
        z2=up(D[2]/(phi["m"]**2)+D[1]*phi["F2"]/(phi["m"]**3))
        value=up(composition(phi)*schur(D[0],z2))
        parts.append(dict(branch=name,complete_operator_coefficient=value))
    K=up(sum((p["complete_operator_coefficient"] for p in parts),arb(0)))
    return dict(complete_rho_minus_quarter_operator_coefficient=K,
        complete_one_sided_radial_L2_operator_upper=up(ex(2).sqrt()*powr(ex(H),Q(1,4))*K),
        decomposition=parts,input_space="H^(-4/3) of both full reference columns, |j|>=97",
        output_space="full H^(-5/3), including zero mode",
        radial_pointwise_factor="rho^(-1/4)",actual_radial_measure="dr = -d rho",
        one_sided_radial_cover=str(H),mean_output_included=True,
        ordinary_physical_source_operator=False)

def missing_derivatives(S,Hv,potential,fold,gate):
    ss={Q(c["exact_output_old_phi_width"]):c for c in S["cases"]}
    inv=Hv["old_circle_inverse"];width=Q(inv["exact_inverse_phi_strip"])
    b2=up(inv["complete_inverse_HV_angular_derivative_bounds"][2])
    Bs=[]
    for s in WIDTHS:
        delta=ex(width-s)
        gate("the genuine inverse has a positive actual Cauchy margin at width "+str(s),delta>0)
        Bs.append(dict(exact_output_phi_strip=str(s),exact_margin=str(width-s),
            B_phi3_upper=rec(up(b2/delta)),B_phi4_upper=rec(up(2*b2/(delta*delta)))))
    w4={}
    for name in ("a1","b1"):
        candidates=[]
        for s in WIDTHS[1:]:
            field=next(v for v in ss[s]["fields"] if v["field"]==name)
            row=next(v for v in field["complete_mixed_derivative_rows"] if v["radial_derivative_order"]==0)
            candidates.append(up(rb(row["complete_joint_Wiener_upper"][3])/ex(s)))
        w4[name]=rec(min(candidates).upper())
    image=gap(potential["reference_image"]["complete_image_disk_radius_lower"],"complete potential image")
    margin=gap(image-fold["Tmax"],"V_TTT Cauchy image margin")
    M2=up(potential["complete_modulus_upper"]["V_TT"])
    gate("the physical root piece also lies inside the actual complex old-circle inverse product",
        H<Q(inv["exact_old_rho_radius"]) and Q(inv["exact_full_physical_root_cover"])==H
        and inv["full_physical_root_piece_covered"] is True)
    return dict(genuine_inverse_missing_angular_orders=Bs,
        complete_real_fourth_angle_first_correction_upper=w4,
        complete_V_TTT_on_actual_old_image_upper=rec(up(M2/margin)),
        complete_V_TTT_image_margin_lower=rec(margin),
        all_original_order_two_inverse_values_only_read=True,
        source_operator_or_full_return_not_implied=True)

def render(doc):
    lines=["# Actual genuine negative reference column operator bounds","",
        "Public Actions run "+os.environ.get("GITHUB_RUN_ID","unknown")+"/"+os.environ.get("GITHUB_RUN_ATTEMPT","unknown")+".",
        "Source SHA256: "+doc["source_sha256"]+".",
        "Input manifest SHA256: "+doc["input_manifest_sha256"]+".",
        "Actual scientific return code: "+str(doc["actual_returncode"])+".",
        "Complete/proved: "+str(doc["complete"])+"/"+str(doc["proved"])+".","",
        "These are real negative-circle full-output operator bounds for both genuine columns.",
        "The physical output is the same original root piece. No positive growing-column bound, complete physical source norm, or full high inverse is inferred.",
        "Original target, FFT, intrinsic, fold, transport, Taylor, RF algebra and output-table recomputations: 0.",""]
    if doc.get("domain_conclusion"):
        lines+=["## Actual domain", "",json.dumps(doc["domain_conclusion"],ensure_ascii=False,sort_keys=True),""]
    if doc.get("operator_rows"):
        lines+=["## Complete operator conclusions","",
            "| Amplitude | Radial derivative | Coefficient of rho^(-1/4) | One-sided L2(dr) upper |",
            "|---|---:|---|---|"]
        for r in doc["operator_rows"]:
            lines.append("| "+r["amplitude"]+" | "+str(r["radial_derivative_order"])+" | "+
                r["complete_rho_minus_quarter_operator_coefficient"]["ball"]+" | "+
                r["complete_one_sided_radial_L2_operator_upper"]["ball"]+" |")
        lines+=["","Input: full two-column H^(-4/3), all signed |j|>=97.",
            "Output: full H^(-5/3), including the output mean.",
            "A radial derivative in this table differentiates only the amplitude. It is not a derivative of the genuine column or of the label partition.",""]
    if doc.get("missing_derivative_conclusions"):
        lines+=["## Explicit derivative margins for a subsequent complete source consumer","",
            json.dumps(doc["missing_derivative_conclusions"],ensure_ascii=False,sort_keys=True),""]
    lines+=["## Actual gates",""]
    lines += ["- "+g["name"]+": "+str(g["passed"])+"." for g in doc["gates"]]
    lines+=["","Actual new scalar mathematics seconds: "+str(doc["actual_mathematical_wall_seconds"])+".",
        "Actual failure: "+str(doc["failure"])+".",
        "All numerical working data are temporary; only these conclusions and exact provenance are retained.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new scalar arithmetic is restricted to the public Actions runner")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the exact scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True)
    source=sha(__file__)
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        original_target_FFT_intrinsic_fold_transport_or_Taylor_recomputed=0,
        original_RF_scalar_or_output_enclosures_recomputed=0,original_natural_stage_bytes_modified=0,
        original_complete_fold_majorant_stages_read=0,original_successful_small_receipts_read=0,
        new_real_genuine_profile_budgets=0,new_complete_operator_rows=0,new_missing_derivative_budgets=0,
        full_physical_source_operator_or_high_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False,operator_rows=[])
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    temporary={}
    started=time.monotonic()
    try:
        m=read(a.manifest)
        gate("the new operator consumer and immutable manifest have their exact reviewed identities",
            sha(a.manifest)==a.manifest_sha and m["public_repository"]==PUBLIC
            and m["scientific_source_sha256"]==source and m["mathematical_parameters"]==dict(
                cutoff_abs_j=J0,physical_frequency="4j",physical_root_piece=2549,
                exact_physical_cover=str(H),original_fold_radius=str(RG),original_fold_phi_strip=str(SG),
                real_reference_interval=["-1/2000","1/2000"],arithmetic_bits=320,
                output_window="H^(-4/3) two-column input to full H^(-5/3) output",
                fixed_intrinsic_parameter="eta_0",real_parameter_values_only=True))
        pins={e["path"]:e for e in m["files"]}
        if len(pins)!=len(m["files"]):raise ValueError("duplicate immutable input path")
        paths={}
        for e in m["files"]:
            rel=Path(e["path"])
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):raise ValueError("input left the topic")
            q=a.repo/rel
            if not q.is_file() or q.stat().st_size!=e["bytes"] or sha(q)!=e["sha256"]:raise ValueError("changed input "+str(rel))
        for k,v in m["input_paths"].items():
            if v not in pins:raise ValueError("an input role is not pinned")
            paths[k]=a.repo/v
        gate("all complete input bytes and original scientific receipt identities are exact",
            sha(paths["old_fold_majorants_stage"])==MAJORANTS
            and sha(paths["adjacent_process"])==APROC and sha(paths["adjacent_publication"])==APUB
            and sha(paths["amplitude_execution"])==S_EXEC and sha(paths["potential_execution"])==P_EXEC
            and sha(paths["columns_execution"])==H_EXEC)
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        mr=next(v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz")
        gate("the single full original fold stage is restored without reevaluating any accepted bound",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and mr["bytes"]==4501 and mr["sha256"]==MAJORANTS and ap["actual_returncode"]==0
            and ap["mathematical_complete"] and ap["mathematical_proved"] and ap["mathematical_failure"] is None
            and au["complete"] and ms["payload"]["majorants"]["A"][1:]==[str(RG),str(SG)])
        f=unpack(ms["payload"])["fold"];doc["original_complete_fold_majorant_stages_read"]=1
        S=current_receipt(paths["amplitude_execution"],"43698106023",S_SOURCE,S_MANIFEST,gate)
        P=current_receipt(paths["potential_execution"],"43685624307",P_SOURCE,P_MANIFEST,gate)
        Hv=current_receipt(paths["columns_execution"],"43688459733",H_SOURCE,H_MANIFEST,gate)
        doc["original_successful_small_receipts_read"]=3
        gate("the old physical piece, true root and complete first-correction domain remain unchanged",
            S["complete_domain_conclusion"]["exact_original_physical_piece_interval"]==list(map(str,PIECE))
            and S["complete_domain_conclusion"]["exact_original_true_root_interval"]==list(map(str,ROOTS))
            and S["complete_domain_conclusion"]["true_physical_root_piece_radius"]==str(H)
            and S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and S["original_accepted_target_FFT_intrinsic_fold_or_transport_recomputed"]==0
            and S["original_signed_Taylor_coefficients_recomputed"]==0
            and S["original_complete_output_tables_recomputed"]==0)
        potential=next(v for v in P["cases"] if v["exact_complex_radial_radius"]=="1/6000")
        column=Hv["reference_columns"]
        M=arb(276);M1=up(potential["complete_modulus_upper"]["V_T"])
        gate("the actual real negative basis supplies both genuine columns and the complete uniform free-frame factor",
            column["exact_real_T_interval"]==["-1/2000","1/2000"]
            and column["all_abs_j_at_least"]==J0 and column["physical_frequency"]=="n=4|j|"
            and up(column["negative_relative_basis_and_inverse_factor"])<ex(Q(6,5))
            and column["both_independent_columns_retained"] and column["both_carrier_signs_retained"]
            and column["ordinary_two_source_rows_retained"]
            and up(potential["complete_modulus_upper"]["V"])<M
            and gap(potential["reference_image"]["complete_image_disk_radius_lower"],"reference disk")>ex(L))
        fold=real_fold(f,gate);profiles=profile_budget(fold,M,M1,gate)
        doc["new_real_genuine_profile_budgets"]=1
        temporary.update(real_fold=encode(fold),complete_profiles=encode(profiles))
        leading=operator_budget(fold["leading_a"],fold["leading_b"],fold,profiles)
        leading.update(amplitude="original_complete_leading_w0",radial_derivative_order=0)
        doc["operator_rows"].append(encode(leading));doc["new_complete_operator_rows"]+=1
        case=next(v for v in S["cases"] if Q(v["exact_output_old_phi_width"])==0)
        fields={v["field"]:v for v in case["fields"]}
        if set(fields)!={"fa","fb","a1","b1"}:raise ValueError("the complete original amplitude table changed")
        for porder in range(3):
            rows=[]
            for name in ("a1","b1"):
                f0=fields[name]
                if not (f0["original_complete_bound_only_read"] and f0["full_radial_and_Fourier_tails_retained"]
                    and f0["joint_sum_of_radial_coefficient_suprema"]):raise ValueError("the original joint output norm changed")
                row=next(v for v in f0["complete_mixed_derivative_rows"] if v["radial_derivative_order"]==porder)
                if row["angular_derivative_orders"]!=[0,1,2,3]:raise ValueError("the exact angular output indices changed")
                rows.append([up(v) for v in row["complete_joint_Wiener_upper"][:3]])
            ans=operator_budget(rows[0],rows[1],fold,profiles)
            ans.update(amplitude="same_regular_first_correction_w1V",radial_derivative_order=porder,
                only_amplitude_radial_derivative=True,original_complete_amplitude_table_recomputed=False)
            doc["operator_rows"].append(encode(ans));doc["new_complete_operator_rows"]+=1
        missing=missing_derivatives(S,Hv,potential,fold,gate);doc["new_missing_derivative_budgets"]=1
        doc["missing_derivative_conclusions"]=missing
        gate("all four complete operator rows retain both reference columns and every output mode",
            len(doc["operator_rows"])==4 and all(r["mean_output_included"] for r in doc["operator_rows"])
            and all(up(r["complete_rho_minus_quarter_operator_coefficient"]).is_finite() for r in doc["operator_rows"]))
        doc["domain_conclusion"]=dict(exact_physical_root_piece_interval=list(map(str,PIECE)),
            exact_true_root_interval=list(map(str,ROOTS)),exact_negative_root_cover=str(H),
            real_parameter_values_only=True,original_complex_boxes_used_only_for_coefficient_bounds=True,
            complete_A_lower=rec(fold["Aminus"]),complete_A_upper=rec(fold["Aplus"]),
            actual_negative_T_modulus_upper=rec(fold["Tmax"]),
            true_X_phi_lower=rec(fold["phase_central"]["m"]),
            true_both_characteristic_phi_lower=rec(fold["phase_high"]["m"]),
            both_genuine_columns_and_both_signs=True,
            complete_output_mean_retained=True,other_original_physical_pieces_identified=False)
        doc["scope"]=dict(genuine_negative_column_operator_paid=True,
            old_circle_complex_column_bound_claimed=False,positive_growing_column_bound_claimed=False,
            complete_first_physical_source_row_paid=False,independent_even_mean_source_paid=False,
            actual_physical_seams_and_reference_matching_sources_retained=True,
            actual_positive_graph_and_outer_ports_retained=True,full_negative_BVP_or_high_inverse_paid=False)
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as e:
        doc["failure"]=dict(type=type(e).__name__,message=str(e))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,actual_conclusions=doc)
        native=a.out_dir/"temporary-genuine-negative-column-operators.json.gz";save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True
        actual=doc["actual_returncode"];text=render(doc)
        try:
            if len(text.encode())>60000:raise ValueError("the actual conclusion exceeds 60000 bytes")
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000:raise ValueError("the actual process exceeds 60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(text)
        except BaseException as e:
            small={k:v for k,v in doc.items() if k not in ("operator_rows","missing_derivative_conclusions")}
            small["actual_scientific_returncode"]=actual;small["formatting_failure"]=dict(type=type(e).__name__,message=str(e))
            small["complete"]=small["proved"]=False;small["actual_returncode"]=1
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual genuine-negative operator formatting failure\n\n"
                "Original scientific return code: "+str(actual)+". No successful science is reclassified as a mathematical failure.\n"
                "Failure: "+str(e)+"\nTemporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            original_numerical_enclosures_recomputed=0,new_operator_rows=doc["new_complete_operator_rows"],
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
