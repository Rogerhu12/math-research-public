#!/usr/bin/env python3
"""Exact regular-transport reduction of the complete first genuine local vector.

Only new complete scalar bounds and one positive comparison are evaluated.
Every accepted target, fold, transport, RF, Taylor, column, operator, source
row, directed-word ratio and radial integral is restored without recomputation.
Intermediate data remain temporary; only small final conclusions are published.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_regular_transport_reduction_of_first_genuine_local_vector_v1"
CONTRACT="c559a2af9288b0c36021c5670c3c1c70eac38b514c9b9d066dd913982fa4479a"
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
C_EXEC="bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3"
C_SOURCE="b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0"
C_MANIFEST="8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9"
D_EXEC="2c5cba2e7351267e090d0ca6c06cfecbb21309c039a7844937ee64026254f1d0"
D_SOURCE="1aa46093bba5150d636cc7c6ef4f5b080447fc2c75d7438b2e52ae5fa6b5d0af"
D_MANIFEST="5ce9aceb3be46e795696c09028f39091fdc9a4f969dba0e0b317408974083e9b"
RG=Q(3,8000);SG=Q(3,128);CW=Q(1,32)
RT=Q(1,2000);SF=Q(1,128);SA=Q(3,512)
R=Q(1,3000);SIGMA=Q(5,1024);SP=Q(1,256);RF=Q(3,20000)
H=Q(893368603925465506687,21990232555520000000000000)
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
BRANCHES=("central","positive_characteristic","negative_characteristic")
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(x):
    v=Q(x);return arb(v.numerator)/arb(v.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):return abs(rb(v)).upper()
def gap(v,label):
    v=rb(v).lower()
    if not v.is_finite() or not v>0:raise ValueError("missing complete positive gap: "+label)
    return v
def bound(v,label):
    v=rb(v)
    if not v.is_finite() or v.lower()<0:raise ValueError("invalid complete upper bound: "+label)
    return v.upper()
def powr(v,p):return (rb(v).log()*ex(p)).exp()
def rec(v):return dict(ball=rb(v).str(64))
def unpack(v):
    if isinstance(v,dict):
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:unpack(x) for k,x in v.items()}
    if isinstance(v,list):return [unpack(x) for x in v]
    return v
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,v,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    b=(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    t=p.with_name(p.name+".partial");t.write_bytes(gzip.compress(b,mtime=0) if compressed else b);t.replace(p)
def matmul(A,B):
    return [[up(sum((A[i][k]*B[k][j] for k in range(2)),arb(0))) for j in range(2)] for i in range(2)]
def matvec(A,v):
    return [up(sum((A[i][k]*v[k] for k in range(2)),arb(0))) for i in range(2)]
def receipt(path,run,source,manifest,gate):
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 is restored with its exact scientific identity",
        str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("source_sha256")==source
        and r.get("input_manifest_sha256")==manifest and r.get("runtime")==RUNTIME
        and r.get("gates") and all(g.get("passed") is True for g in r["gates"]))
    return r

def domain_and_connection(f,c,m,S,P,gate):
    """New finite scalar arithmetic on a strict subproduct of the accepted one."""
    potential=next(v for v in P["cases"] if Q(v["exact_complex_radial_radius"])==Q(1,6000))
    IT=gap(potential["reference_image"]["complete_image_disk_radius_lower"],"common potential image")
    inverse_gap=gap(S["complete_domain_conclusion"]["canonical_inverse_radial_gap"],"accepted inverse radial contraction")
    preimage=up(ex(R)/inverse_gap)
    B=bound(f["B"],"old inverse angle displacement")
    j=bound(f["j"],"old x-1");BA=bound(f["BA"],"old A_phi")
    BT=bound(f["BT"],"old T_phi");Qp=bound(f["Q"],"old Q")
    Ap=bound(f["Ap"],"old A modulus");Am=gap(f["Am"],"old A gap")
    mu_min=gap(f["mu"],"old principal mu gap")
    if m["chi"][1:]!=[str(RG),str(SG)]:raise ValueError("original complete chi product changed")
    chi=bound(m["chi"][0],"complete chi")
    imageT=up(ex(H)*powr(Ap,Q(2,3)))
    imageX=up(ex(SP)+ex(H/RG)*chi)
    gates=dict(physical_T_margin=(ex(R)-imageT).lower(),
        physical_X_margin=(ex(SIGMA)-imageX).lower(),
        canonical_radial_margin=ex(RT-R).lower(),
        canonical_forcing_angle_margin=ex(SF-SIGMA).lower(),
        canonical_amplitude_angle_margin=ex(SA-SIGMA).lower(),
        inverse_old_radial_margin=(ex(RF)-preimage).lower(),
        inverse_old_angle_margin=(ex(SG-SIGMA)-B).lower(),
        old_coefficient_angle_margin=(ex(CW-SIGMA)-B).lower(),
        old_Q_radial_derivative_margin=(ex(RG)-preimage).lower(),
        common_potential_image_margin=(IT-ex(RT)).lower(),
        original_A_gap=Am,original_mu_gap=mu_min,
        original_inverse_radial_gap=inverse_gap)
    gate("the unchanged physical product and every regular sT segment lie inside the paid canonical and old products",
        H<RG and 0<R<RT and 0<SP<SIGMA<SA<SF
        and all(v.is_finite() and v>0 for v in gates.values())
        and potential["complete"] and potential["proved"] and potential["failure"] is None
        and potential["all_integer_modes_abs_j_at_least"]==97
        and Q(potential["exact_complex_z_square_halfwidth"])==Q(1,97*97)
        and potential["both_carrier_signs_retained"] and potential["whole_complex_bilinear_family"])
    t=up(preimage/ex(RG))
    x=up(1+t*j)
    yT=up(ex(Q(2,3))*t*BA/Am)
    y=min(up(t*t*BT),up(ex(R)*yT)).upper()
    Qphi=up(Qp*yT/2)
    Qr=up(Qp/gates["old_Q_radial_derivative_margin"])
    D0=bound(c["D"][0],"old d");D1=bound(c["D"][1],"old d_phi")
    T0=bound(c["T0"],"old complete T0")
    DQ=up(Qr+D0*Qphi)
    common=up(DQ+Qp*D1+T0*Qp)
    cT=up((common*x+Qp*Qphi*ex(R)*y+Qp*Qp*y*y)/mu_min)
    Xi=up((common*y+Qp*Qp*x*yT/2)/mu_min)
    mu=up(Qp*Qp*(x*x+ex(R)*y*y))
    M=bound(f["M"],"complete leading a0")
    B2=bound(f["B2"],"complete analytic b0/T^2")
    Bi=bound(f["Bi"],"complete inverse leading branch")
    dT=ex(RT-R);dA=ex(SA-SIGMA)
    aX=up(M/dA)
    if (M-1).lower()>=0:
        aX=min(aX,up(2*(M-1)*ex(R)/(dT*dA))).upper()
    bp=up(B2*ex(R*R));bT=up(B2*(2*ex(R)+ex(R*R)/dT))
    bX=up(bp/dA)
    MM=[[M,up(ex(R)*bp)],[bp,M]]
    MX=[[aX,up(ex(R)*bX)],[bX,aX]]
    KK=[[arb(0),ex(R)],[arb(1),arb(0)]]
    KMX=matmul(KK,MX);KM=matmul(KK,MM)
    CC=[[up(KMX[i][j]+Xi*KM[i][j]/2+B2*ex(R)*KK[i][j]/2)
         for j in range(2)] for i in range(2)]
    V=bound(potential["complete_modulus_upper"]["V"],"complete potential")
    VT=bound(potential["complete_modulus_upper"]["V_T"],"complete potential derivative")
    return dict(M=MM,C=CC,Mstar=M,B2=B2,Bi=Bi,b=bp,bT=bT,cT=cT,Xi=Xi,mu=mu,V=V,VT=VT,
        preimage_radius=preimage,gaps=gates,physical_T_image=imageT,physical_X_image=imageX,
        original_positive_A_lower=Am,original_positive_mu_lower=mu_min,
        original_inverse_radial_gap=inverse_gap,original_potential_image=IT,
        dT=dT,dF=ex(SF-SIGMA),dA=dA,
        exact_complete_old_phi_output_width=str(SP),exact_complete_canonical_radius=str(R),
        exact_complete_canonical_angle_strip=str(SIGMA))

def regular_local_vector(S,C):
    """P21--24: normalize the old complete amplitudes; no new transport solve."""
    amps=S["complete_amplitude_conclusion"];forcing=S["complete_forcing_conclusion"]
    aa=bound(amps["a1"],"accepted complete genuine a1")
    bb=bound(amps["b1"],"accepted complete genuine b1")
    Fa=bound(forcing["fa"],"accepted normalized fa")
    Fb=bound(forcing["fb"],"accepted normalized fb")
    A=up(C["Bi"]*C["Bi"]*(C["Mstar"]*aa+ex(RT**3)*C["B2"]*bb))
    B=up(C["Bi"]*C["Bi"]*(ex(RT**2)*C["B2"]*aa+C["Mstar"]*bb))
    AX=up(A/C["dA"]);BX=up(B/C["dA"]);BXX=up(2*B/(C["dA"]*C["dA"]))
    breg=up(ex(Q(2,3))*(Fb/C["dT"]+AX))
    PA=up((Fa/C["dT"]+Fb/C["dF"]+BX)/2)
    PB=up(2*Fb/(5*C["dT"]*C["dT"])+3*Fa/(5*C["dF"])+ex(R)*BXX/7)
    product=[up(A*Fb+ex(R)*B*Fa),up(A*Fa+B*Fb)]
    principal=matvec(C["M"],[up(PA+product[0]),up(PB+product[1])])
    connection=matvec(C["C"],[Fa,breg])
    cross=[up(C["b"]*AX),up(C["b"]*BX)]
    # E12 acts on the left: the last vector has no a0 or a0_T contribution.
    e12=[up((B+C["V"])*(2*C["bT"]+C["cT"]*C["b"])+C["VT"]*C["b"]),arb(0)]
    raw=[up(C["mu"]*(principal[i]+connection[i]+cross[i]+e12[i])) for i in range(2)]
    diagnostics=dict(normalized_A=A,normalized_B=B,normalized_fa=Fa,normalized_fb=Fb,
        A_X=AX,B_X=BX,B_XX=BXX,regular_b=breg,principal_A=PA,principal_B=PB,
        raw_component_summands={name:[up(C["mu"]*v) for v in values]
            for name,values in (("complete_principal_and_forcing",principal),
                ("complete_leading_connection",connection),("complete_cross_commutator",cross),
                ("complete_left_E12",e12))})
    return raw,diagnostics

def read_positive_coefficients(C,gate):
    rows=C["complete_positive_linear_operator_conclusion"]
    gate("the eighteen accepted positive coefficients retain their identical profile branches and input ordering",
        len(rows)==3 and [r["branch"] for r in rows]==list(BRANCHES)
        and all(r["exact_input_component_order"]==["a","a_phi","a_phiphi","b","b_phi","b_phiphi"]
            and len(r["complete_positive_linear_coefficients"])==6
            and len(r["selected_inputs"])==6
            and all(v["denominator_is_lower_for_bound_number_only"] for v in r["selected_inputs"]) for r in rows)
        and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
        and C["scope"]["all_input_abs_j_at_least97"]
        and C["scope"]["budget_parameter_lower_is_not_true_amplitude_lower"])
    return [[bound(v,"accepted complete positive coefficient") for v in r["complete_positive_linear_coefficients"]]
        for r in rows]

def positive_operator(raw,coeff):
    jets=[up(math.factorial(q)*v/ex(SP**q)) for v in raw for q in range(3)]
    branches=[up(sum((c[j]*jets[j] for j in range(6)),arb(0))) for c in coeff]
    return up(sum(branches,arb(0))),dict(real_old_angle_jets=jets,complete_branch_comparisons=branches)

def choose_complete(old,new):
    if up(new)<up(old):return rec(up(new)),bool(up(new)<rb(old).lower())
    return old,False

def compare_and_combine(C,D,value):
    oldlocal=C["complete_local_vector_conclusion"]
    if D["accepted_complete_local_vector_conclusion"]!=oldlocal:
        raise ValueError("the accepted full local vector budget changed between successful runs")
    beta=gap(oldlocal["raw_complete_operator_coefficients"][0],"accepted complete local algorithm budget")
    candidate=up(value/beta);q=min(arb(1),candidate).upper()
    old=D["complete_source_conclusion"]
    terms=dict(old["complete_first_source_term_L2_upper"])
    revised,changed=choose_complete(terms["local_raw_1"],up(q*up(terms["local_raw_1"])))
    terms["local_raw_1"]=revised
    con=dict(old)
    con["complete_first_source_term_L2_upper"]=terms
    local=up(sum((up(terms["local_raw_"+str(j)]) for j in (1,2,3)),arb(0)))
    con["local_L2_upper"],ilocal=choose_complete(old["local_L2_upper"],local)
    first=up(up(con["local_L2_upper"])+up(old["nonlocal_total_L2_upper"]))
    con["first_L2_upper"],ifirst=choose_complete(old["first_L2_upper"],first)
    pair=up((up(con["first_L2_upper"])**2+up(old["mean_L2_upper"])**2).sqrt())
    con["combined_L2_upper"],ipair=choose_complete(old["combined_L2_upper"],pair)
    con["complete_local_budget_read_unchanged"]=False
    con["only_complete_first_local_vector_replaced"]=True
    con["all_other_source_terms_and_mean_balls_read_verbatim"]=True
    con["old_source_row_or_radial_integral_recomputed"]=False
    con["strictly_smaller_complete_aggregates"]=dict(local=ilocal,first=ifirst,combined=ipair)
    comparison=dict(accepted_complete_first_local_operator_budget=oldlocal["raw_complete_operator_coefficients"][0],
        positive_lower_for_same_algorithm_budget=rec(beta),
        new_complete_first_local_operator_upper=rec(value),
        complete_uniform_comparison_factor=rec(q),
        accepted_complete_local_raw_1_L2=old["complete_first_source_term_L2_upper"]["local_raw_1"],
        retained_complete_local_raw_1_L2=revised,strict_complete_term_improvement=changed,
        denominator_is_not_a_true_function_or_operator_lower=True,
        original_outer_J_and_actual_radial_weight_retained=True)
    return con,comparison

def render(doc):
    lines=["# Actual regular-transport reduction of the first genuine local vector","",
        "Public run: "+str(doc["run_id"])+"/"+str(doc["run_attempt"])+".",
        "Actual scientific child code: "+str(doc["actual_returncode"])+".",
        "Complete: "+str(doc["complete"])+". Proved: "+str(doc["proved"])+".","",
        "Scientific SHA256: "+doc["source_sha256"]+".",
        "Input manifest SHA256: "+doc["input_manifest_sha256"]+".","",
        "The accepted forcing, first correction, genuine columns, positive comparison coefficients,",
        "directed words and radial integrals are restored exactly. Only new scalar bounds are evaluated.",
        "The first local vector is combined through its exact regular transport before a modulus is taken.",
        "No separate old w1rr estimate is regenerated or subtracted from an upper bound.","",
        "## Actual work counts",""]
    for k in ("original_complete_fold_stages_read","original_successful_small_receipts_read",
        "original_positive_linear_coefficients_read","original_complete_source_terms_read",
        "new_complete_subproduct_budgets","new_complete_regular_local_vector_budgets",
        "new_fixed_positive_operator_comparisons","new_complete_uniform_factors","new_complete_scalar_recombinations",
        "old_numerical_enclosures_recomputed","old_source_rows_or_radial_integrals_recomputed"):
        lines.append("- "+k+": "+str(doc[k])+".")
    if "complete_domain_conclusion" in doc:
        lines+=["","## Complete-domain inclusion and gaps","",
            json.dumps(doc["complete_domain_conclusion"],sort_keys=True)]
    if "complete_raw_local_vector_conclusion" in doc:
        lines+=["","## Complete first local vector","",
            json.dumps(doc["complete_raw_local_vector_conclusion"],sort_keys=True)]
    if "complete_comparison_conclusion" in doc:
        lines+=["","## Same-vector positive comparison","",
            json.dumps(doc["complete_comparison_conclusion"],sort_keys=True)]
    if "complete_source_conclusion" in doc:
        con=doc["complete_source_conclusion"]
        lines+=["","## Complete physical source bounds","",
            "| Complete channel | Ordinary radial L2 upper ball |","|---|---|"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+k+" | "+con[k]["ball"]+" |")
        for title,key in (("All retained first-row terms","complete_first_source_term_L2_upper"),
                          ("Independent physical even-mean terms","complete_independent_mean_term_L2_upper")):
            lines+=["","## "+title,"","| Term | Complete L2 upper ball |","|---|---|"]
            lines += ["| "+k+" | "+v["ball"]+" |" for k,v in con[key].items()]
    lines+=["","## Actual gates",""]+["- "+g["name"]+": "+str(g["passed"])+"." for g in doc["gates"]]
    lines+=["","## Scope","",json.dumps(doc.get("scope",{}),sort_keys=True),
        "","Actual new scalar seconds: "+repr(doc.get("actual_mathematical_wall_seconds"))+".",
        "Failure: "+str(doc.get("failure"))+".",
        "Temporary native SHA256: "+str(doc.get("temporary_native_sha256"))+".",
        "Intermediate scalar matrices and comparison diagnostics remain temporary.",
        "The genuine positive graph, physical-to-wave traces, all seams and the full high inverse remain separate.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new scalar arithmetic is restricted to the public Actions runner")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the fixed accepted scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True);source=sha(__file__);started=time.monotonic()
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_complete_fold_stages_read=0,original_successful_small_receipts_read=0,
        original_positive_linear_coefficients_read=0,original_complete_source_terms_read=0,
        new_complete_subproduct_budgets=0,new_complete_regular_local_vector_budgets=0,
        new_fixed_positive_operator_comparisons=0,new_complete_uniform_factors=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,old_forcing_transport_Taylor_RF_or_profile_recomputed=0,
        old_operator_words_or_positive_calibration_recomputed=0,old_source_rows_or_radial_integrals_recomputed=0,
        original_natural_stage_bytes_modified=0,full_physical_negative_volume_source_paid=False,
        full_high_inverse_claimed=False,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    temporary={}
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    try:
        m=read(a.manifest)
        params=dict(cutoff_abs_j=97,physical_frequency="4j",physical_root_piece=2549,
            exact_full_physical_cover=str(H),exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],
            exact_root_interval=list(map(str,ROOTS)),original_fold_radius=str(RG),original_fold_phi_strip=str(SG),
            original_canonical_radius=str(RT),original_canonical_forcing_strip=str(SF),
            original_canonical_amplitude_strip=str(SA),new_canonical_radius=str(R),
            new_canonical_strip=str(SIGMA),actual_old_phi_strip=str(SP),complete_old_coefficient_strip=str(CW),
            input_window="H^(-4/3) both genuine columns and both signs",
            first_source_window="ordinary L2_r H^(-2/3)",independent_mean_window="ordinary L2_r constants",
            original_complete_source_run="43703879926/1",original_positive_calibration_run="43702688640/1",
            original_scalar_forcing_run="43698106023/1",fixed_intrinsic_parameter="eta_0",
            real_parameter_values_for_final_operator_only=True,complete_complex_delta_square_for_scalar_bounds=True,
            original_radial_integrations_recomputed=0,arithmetic_bits=320)
        doc["mathematical_parameters"]=params
        gate("the new scalar source and manifest retain their exact reviewed identities and domains",
            sha(a.manifest)==a.manifest_sha and m["public_repository"]==PUBLIC
            and m["scientific_source_sha256"]==source and m["mathematical_parameters"]==params)
        pins={e["path"]:e for e in m["files"]}
        if len(pins)!=len(m["files"]):raise ValueError("duplicate immutable input")
        for e in m["files"]:
            rel=Path(e["path"]);f=a.repo/rel
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):raise ValueError("input outside topic")
            if not f.is_file() or f.stat().st_size!=e["bytes"] or sha(f)!=e["sha256"]:
                raise ValueError("changed exact input "+str(rel))
        if any(v not in pins for v in m["input_paths"].values()):raise ValueError("unpinned required input role")
        paths={k:a.repo/v for k,v in m["input_paths"].items()}
        expected=dict(contract=CONTRACT,old_fold_majorants_stage=MAJORANTS,adjacent_process=APROC,adjacent_publication=APUB,
            amplitude_execution=S_EXEC,potential_execution=P_EXEC,complete_genuine_execution=C_EXEC,
            directed_source_execution=D_EXEC,complete_genuine_source=C_SOURCE,
            directed_source_algorithm=D_SOURCE,original_scalar_algorithm=S_SOURCE)
        gate("all accepted complete scalar, source and original leading byte identities are unchanged",
            all(sha(paths[k])==v for k,v in expected.items()))
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        mr=next(v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz")
        gate("the complete original leading product is read with its actual immutable legacy header",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and mr["bytes"]==4501 and mr["sha256"]==MAJORANTS and ap["actual_returncode"]==0
            and ap["mathematical_complete"] and ap["mathematical_proved"] and ap["mathematical_failure"] is None
            and au["complete"] and ms["payload"]["majorants"]["A"][1:]==[str(RG),str(SG)])
        old=unpack(ms["payload"]);f=old["fold"];c=old["coefficients"];majorants=old["majorants"]
        doc["original_complete_fold_stages_read"]=1
        S=receipt(paths["amplitude_execution"],"43698106023",S_SOURCE,S_MANIFEST,gate)
        P=receipt(paths["potential_execution"],"43685624307",P_SOURCE,P_MANIFEST,gate)
        C=receipt(paths["complete_genuine_execution"],"43702688640",C_SOURCE,C_MANIFEST,gate)
        D=receipt(paths["directed_source_execution"],"43703879926",D_SOURCE,D_MANIFEST,gate)
        doc["original_successful_small_receipts_read"]=4
        sd=S["complete_domain_conclusion"];sa=S["complete_amplitude_conclusion"];ds=D["complete_source_conclusion"]
        gate("the fixed root, actual physical piece, full parameter squares and normalized forcing are exactly those already accepted",
            sd["exact_original_physical_piece_interval"]==list(map(str,PIECE))
            and sd["exact_original_true_root_interval"]==list(map(str,ROOTS))
            and sd["true_physical_root_piece_radius"]==str(H)
            and sd["same_potential_T_segment_proved"] and sd["actual_inverseimage_and_both_regular_paths_proved"]
            and S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and sa["canonical_radius"]==str(RT) and sa["canonical_strip"]==str(SA)
            and sa["exact_regular_root_normalization_retained"] and not sa["old_transport_or_Taylor_coefficients_recomputed"]
            and S["original_accepted_target_FFT_intrinsic_fold_or_transport_recomputed"]==0
            and S["original_signed_Taylor_coefficients_recomputed"]==0 and S["original_complete_output_tables_recomputed"]==0
            and len(C["gates"])==17 and len(D["gates"])==12
            and C["original_complete_output_enclosures_recomputed"]==0
            and D["old_numerical_enclosures_recomputed"]==0 and D["old_radial_integrals_recomputed"]==0
            and D["new_bound_number_denominator_evaluations"]==96 and D["new_complete_uniform_comparisons"]==16
            and ds["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and ds["actual_dr_measure"] and ds["one_sided_uncertain_root_band_retained"]
            and ds["both_density_windows_retained"] and ds["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        coef=domain_and_connection(f,c,majorants,S,P,gate);doc["new_complete_subproduct_budgets"]=1
        doc["complete_domain_conclusion"]=encode(dict(
            exact_complete_canonical_radius=R,exact_complete_canonical_strip=SIGMA,exact_actual_old_phi_strip=SP,
            exact_full_physical_cover=H,exact_original_physical_piece_interval=list(map(str,PIECE)),
            exact_original_true_root_interval=list(map(str,ROOTS)),
            physical_T_image_upper=coef["physical_T_image"],physical_X_image_upper=coef["physical_X_image"],
            complete_positive_domain_gaps=coef["gaps"],actual_sT_segments_remain_in_original_product=True,
            original_leading_and_reference_gauges_unchanged=True))
        raw,diagnostic=regular_local_vector(S,coef);doc["new_complete_regular_local_vector_budgets"]=1
        gate("the exact leading connection and complete regular local vector yield finite bounds without small-root division",
            all(v.is_finite() and v.lower()>=0 for v in raw)
            and all(v.is_finite() and v.lower()>=0 for row in coef["C"] for v in row)
            and coef["Bi"]>0 and coef["B2"].is_finite()
            and diagnostic["raw_component_summands"]["complete_left_E12"][1]==0)
        coeff=read_positive_coefficients(C,gate);doc["original_positive_linear_coefficients_read"]=18
        op,opdetail=positive_operator(raw,coeff);doc["new_fixed_positive_operator_comparisons"]=1
        result,comparison=compare_and_combine(C,D,op)
        doc["new_complete_uniform_factors"]=1;doc["new_complete_scalar_recombinations"]=3
        doc["original_complete_source_terms_read"]=31
        doc["complete_raw_local_vector_conclusion"]=dict(
            raw_first_component_supremum_upper=rec(raw[0]),raw_second_component_supremum_upper=rec(raw[1]),
            complete_all_output_operator_coefficient=rec(op),raw_numerator_not_divided_by_mu=True,
            exact_left_E12_second_component_zero=True,all_input_modes_and_both_carriers_retained=True,
            original_eighteen_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]),
            old_complete_forcing_and_amplitude_solutions_recomputed=False,
            original_complete_positive_comparison_coefficients_recomputed=False)
        doc["complete_comparison_conclusion"]=comparison;doc["complete_source_conclusion"]=result
        temporary.update(connection_and_complete_domain=encode(coef),regular_transport=encode(diagnostic),
            positive_comparison=encode(opdetail))
        gate("one complete same-vector comparison preserves every other first-row and independent-mean term verbatim",
            len(result["complete_first_source_term_L2_upper"])==21
            and len(result["complete_independent_mean_term_L2_upper"])==10
            and all(v==result["complete_first_source_term_L2_upper"][k]
                for k,v in ds["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and result["complete_independent_mean_term_L2_upper"]==ds["complete_independent_mean_term_L2_upper"]
            and result["mean_L2_upper"]==ds["mean_L2_upper"]
            and result["nonlocal_total_L2_upper"]==ds["nonlocal_total_L2_upper"]
            and up(comparison["complete_uniform_comparison_factor"])<=1
            and rb(comparison["complete_uniform_comparison_factor"]).lower()>=0)
        gate("all complete local and two-row physical bounds are finite on the original exact radial measure",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["outer_J_window"]==ds["outer_J_window"])
        doc["scope"]=dict(D["scope"])
        doc["scope"].update(exact_regular_transport_first_local_vector_reduced=True,
            original_complete_first_correction_unchanged=True,old_w1rr_not_separately_recomputed_or_subtracted=True,
            leading_connection_reduced_before_modulus=True,complete_left_E12_uses_only_b0_and_b0_T=True,
            canonical_sT_segment_inclusion_actually_verified=True,one_new_complete_local_bound_only=True,
            original_18_positive_coefficients_recomputed=False,original_96_directed_comparisons_recomputed=False,
            original_source_rows_and_actual_radial_integrals_recomputed=False,
            physical_to_wave_readout_paid=False,full_negative_BVP_inverse_paid=False,
            positive_growing_column_operator_paid=False,cutoff97_strong_return_contraction_paid=False)
        doc["full_physical_negative_volume_source_paid"]=True
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,
            complete_conclusions=doc)
        native=a.out_dir/"temporary-regular-transport-first-local-vector.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            text=render(doc)
            data=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(data)>60000 or len(text.encode())>60000:raise ValueError("small final conclusion exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(text)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in
                ("complete_domain_conclusion","complete_raw_local_vector_conclusion",
                 "complete_comparison_conclusion","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual regular-transport source formatting failure\n\n"
                "The original scientific child code was "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_local_vector_bounds=doc["new_complete_regular_local_vector_budgets"],
            old_numerical_enclosures_recomputed=0,old_radial_integrals_recomputed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
