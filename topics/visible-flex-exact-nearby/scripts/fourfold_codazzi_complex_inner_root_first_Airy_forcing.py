#!/usr/bin/env python3
"""Pay the actual complex inner-root first Airy forcing and local next residual.

Only new exact first derivatives of two original cubic shards and scalar domain,
Cauchy and forcing budgets are evaluated. Original intrinsic targets, folds,
leading amplitudes and all completed real rows are never recomputed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import flint
from flint import acb,arb,ctx
PUBLIC="Rogerhu12/math-research-public"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
ROOT_SHA="397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
BUDGET_SHA="10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"
FOLD_SHA="9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd"
LEADING_SHA="1c00bf9f6d80343b96bdabf2ce2b07f1f3461851ad0783b9a2a59a495d141cdd"
DELTA=Q(1,10**8);RN=Q(1,100000);RG=Q(9,10**6)
SN=Q(1,1024);SG=Q(3,256);SF=Q(1,128);SV=Q(3,512);SX=Q(1,1024)
SI=Q(1,256);SO=Q(1,512)
RADII=(Q(1,200000),Q(1,100000),Q(1,50000))
DERIVATIVE_ORDERS=((0,0),(1,0),(2,0),(0,1),(0,2),(1,1))

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":raw=gzip.compress(raw,compresslevel=9,mtime=0)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(raw);tmp.replace(p)
def ex(x):
    q=Q(x);return arb(q.numerator)/q.denominator
def dyadic(x):return Q.from_float(float(x))
def up(x):return abs(x).upper()
def upper(d):return arb(d["upper"]).upper()
def lower(d):return arb(d["lower"]).lower()
def box(d):
    if "lower" in d and "upper" in d:return lower(d).union(upper(d))
    return arb(d["ball"])
def cb(d):return acb(box(d["real"]),box(d["imag"]))
def rec(x):
    x=arb(x)
    if not x.is_finite():raise ValueError("a genuine complex-root bound is not finite")
    return dict(ball=x.str(48),lower=x.lower().str(48),upper=x.upper().str(48))
def compact(x):return dict(ball=arb(x).str(48))
def encode(v):
    if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return compact(v)
def decode(v):
    if isinstance(v,list):return [decode(x) for x in v]
    if isinstance(v,dict):
        if "ball" in v:return box(v)
        return {k:decode(x) for k,x in v.items()}
    raise ValueError("a saved complete scalar tensor changed schema")
def ipow(x,n):
    if n<0:raise ValueError("bounded integer multiplication requires nonnegative exponent")
    y=arb(1)
    for _ in range(n):y=y*x
    return y
def power(x,p):
    if not x>0:raise ValueError("a positive fractional-power gap was lost")
    q=Q(p);return (x.log()*q.numerator/q.denominator).exp()
def mv(a,b):
    return [sum((a[i][k]*b[k] for k in range(2)),arb(0)).upper() for i in range(2)]
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(2)),arb(0)).upper()
    for j in range(2)] for i in range(2)]
def wc(vals,frequencies,width,order=0):
    return sum((x*ex(f**order)*(ex(f)*width).exp()
        for x,f in zip(vals,frequencies) if order==0 or f),arb(0)).upper()

def coefficient_budget(germ,rb,fold,leading,derivatives):
    fb=fold["bounds"];lb=leading["bounds"]
    sigma=(ex(SF)+upper(fb["flow_displacement"])).upper()
    if not ex(SN)<sigma<ex(SG):raise ValueError("the actual forcing inverse image leaves the old product")
    basef=(128*(sigma-ex(SN))).exp().upper()
    zf=(384*(sigma-ex(SN))).exp().upper()
    U=[];V=[]
    for k in range(5):
        bu=upper(germ["moving_U_derivative_Astrip"][k])+upper(rb["background_repair_angular_norms_u"][k])
        bv=upper(germ["moving_v_derivative_Astrip"][k])+upper(rb["background_repair_angular_norms_v"][k])
        U.append((basef*bu+ex(DELTA)*zf*upper(rb["direction_angular_norms_u"][k])).upper())
        V.append((basef*bv+ex(DELTA)*zf*upper(rb["direction_angular_norms_v"][k])).upper())
    pd=[upper(v["modulus_upper"]) for v in derivatives["candidate"]]
    zd=[upper(v["modulus_upper"]) for v in derivatives["response"]]
    Mr=(upper(germ["moving_mean_v_radial"]["modulus_upper"])+ex(DELTA)*zd[96]).upper()
    Ur=[];Vr=[]
    for k in range(5):
        Ur.append((wc(pd[:32],[4*j for j in range(1,33)],sigma,k)
            +ex(DELTA)*wc(zd[:96],[4*j for j in range(1,97)],sigma,k)).upper())
        Vr.append((wc(pd[33:],[4*j for j in range(1,33)],sigma,k)
            +ex(DELTA)*wc(zd[97:],[4*j for j in range(1,97)],sigma,k)
            +(Mr if k==0 else arb(0))).upper())
    intr=germ["complex_intrinsic_coefficients"]
    metric=cb(intr["a"]);E=cb(intr["E"]);beta=cb(intr["beta"])
    if not (metric.real>0 and E.real>0):raise ValueError("an original complex intrinsic denominator was lost")
    br=up(cb(intr["a2"])/metric-beta*beta)
    gr=up(cb(intr["E1"])/(2*E)-beta)
    b=upper(rb["beta_abs_upper"]);K=upper(rb["K_abs_upper"]);Kr=upper(intr["K1"]["modulus_upper"])
    mgap=lower(rb["full_complex_mean_abs_lower"]);mmax=upper(rb["full_complex_mean_abs_upper"])
    eta_minus=(lower(rb["gamma_abs_lower"])*mgap).lower()
    eta_plus=(upper(rb["gamma_abs_upper"])*mmax).upper()
    if not (mgap>0 and eta_minus>0):raise ValueError("the same complete complex parameter mean or eta gap vanished")
    eratio=(gr+Mr/mgap).upper()
    u0,u1=U[:2];v0,v1=V[:2];ur,vr=Ur[0],Vr[0]
    S=(u0*u0+K*v0*v0).upper()
    Sr=(2*u0*ur+Kr*v0*v0+2*K*v0*vr).upper()
    d0=min((b*S/4).upper(),upper(fb["drift"])).upper()
    d1=min((b*S).upper(),upper(fb["drift_phi"])).upper()
    dr=((br*S+b*Sr)/4).upper()
    ell=(2*b*u0*v0).upper()
    ellp=(2*b*(u1*v0+u0*v1)).upper()
    ellr=(2*br*u0*v0+2*b*(ur*v0+u0*vr)).upper()
    ep=(2*b*(3*u0*u1+K*v0*v1)).upper()
    b0=(b*(1+u0*u0+3*K*v0*v0)).upper()
    b0p=(2*b*(u0*u1+3*K*v0*v1)).upper()
    b0r=(br*(1+u0*u0+3*K*v0*v0)+b*(2*u0*ur+3*Kr*v0*v0+6*K*v0*vr)).upper()
    tq=(eratio+d1+b*(1+3*u0*u0+K*v0*v0)).upper()
    rq=(ellr+d0*ellp+eta_plus*ep+2*b*eta_plus*u1*u0+ell*(eratio+d1)).upper()
    vartheta=(rq/eta_minus+2*b*K*v0*v1).upper()
    V0=(tq*b0+b0r+d0*b0p+K*(ell*ell+4*b*eta_plus*v0*u1)).upper()
    Un=upper(rb["full_family_U_angular_norms"][0]);Vn=upper(rb["full_family_V_angular_norms"][0])
    Smean=(Un*Un+K*Vn*Vn).upper()
    T0=(eratio+4*b*Smean+5*d1).upper()
    j=upper(fb["derivative_excess"]);Tp=upper(fb["T_modulus_upper"])
    BT=upper(fb["T_phi"]);Bp=upper(fb["quotient_A_phi"])
    Am=lower(fb["quotient_A_real_gap"]);Ap=upper(fb["quotient_A_modulus_upper"])
    ap=upper(fb["a_modulus_upper"])
    gap=(1-upper(fb["principal_D_minus_one"])).lower()
    mu=lower(fb["mu_modulus_lower"])
    if not (gap>0 and mu>0 and Am>0):raise ValueError("the actual principal fold lost a complete denominator")
    B=[[((1+j)/gap).upper(),(Tp*BT/gap).upper()],
       [(BT/gap).upper(),((1+j)/gap).upper()]]
    DX=(ex(Q(2,3))*ap*ex(RG)*ex(RG)*Bp).upper()
    DT=(ap*power(Am,Q(-1,3))*(1+j)).upper()
    HD=[[DX,(DT*Tp).upper()],[DT,DX]]
    return dict(sigma=sigma,U=U,V=V,Ur=Ur,Vr=Vr,true_mean_r=Mr,
        beta=b,beta_r=br,K=K,K_r=Kr,gamma_log_r=gr,eta_log_r=eratio,
        eta_lower=eta_minus,eta_upper=eta_plus,d0=d0,d1=d1,dr=dr,
        ell=ell,ell_phi=ellp,ell_r=ellr,e_phi=ep,b0=b0,b0_phi=b0p,b0_r=b0r,
        tQ=tq,rQ=rq,vartheta=vartheta,V0=V0,T0=T0,scalar_mean_S=Smean,
        A_lower=Am,A_upper=Ap,mu_lower=mu,j=j,Tplus=Tp,Tphi=BT,
        H_inverse=B,HD=HD,H_inverse_HD=mm(B,HD),
        M=upper(lb["leading_a0"]),B2=upper(lb["leading_b0_divided_by_T_squared"]),
        branch_inverse=upper(lb["both_leading_branch_inverses"]),
        T_rho_error=upper(fb["radial_derivative_error"]),X_rho=upper(fb["X_rho"]),
        flow_displacement=upper(fb["flow_displacement"]))

def local_scalar(W,c):
    return (W["2,0"]+2*c["d0"]*W["1,1"]
        +(c["d0"]*c["d0"]+c["eta_upper"]*c["eta_upper"]*c["K"])*W["0,2"]
        +(c["dr"]+c["d0"]*c["d1"])*W["0,1"]
        +c["T0"]*(W["1,0"]+c["d0"]*W["0,1"])+c["V0"]*W["0,0"]).upper()
def local_pair(Wa,Wb,c):
    direct=[local_scalar(Wa,c),local_scalar(Wb,c)]
    cross=mv(c["H_inverse_HD"],[Wa["0,0"],Wb["0,0"]])
    result=[((direct[i]+c["vartheta"]*cross[i])/c["mu_lower"]).upper() for i in range(2)]
    return result,dict(local_differential=direct,complete_one_gain_cross=cross)

def canonical_to_old(W,f):
    T,X,Tp,Xp=f["T_rho"],f["X_rho"],f["T_phi"],f["X_phi"]
    return {
        "0,0":W["0,0"],
        "1,0":(W["1,0"]*T+W["0,1"]*X).upper(),
        "0,1":(W["1,0"]*Tp+W["0,1"]*Xp).upper(),
        "2,0":(W["2,0"]*T*T+2*W["1,1"]*T*X+W["0,2"]*X*X
            +W["1,0"]*f["T_rhorho"]+W["0,1"]*f["X_rhorho"]).upper(),
        "1,1":(W["2,0"]*T*Tp+W["1,1"]*(T*Xp+Tp*X)+W["0,2"]*X*Xp
            +W["1,0"]*f["T_rhophi"]+W["0,1"]*f["X_rhophi"]).upper(),
        "0,2":(W["2,0"]*Tp*Tp+2*W["1,1"]*Tp*Xp+W["0,2"]*Xp*Xp
            +W["1,0"]*f["T_phiphi"]+W["0,1"]*f["X_phiphi"]).upper()}

def consume_case(RT,c,roots):
    rF=(ex(RT)*power(c["A_lower"],Q(-2,3))).upper()
    dphi=(ex(SG)-c["sigma"]).lower();drad=(ex(RG)-rF).lower()
    if not (ex(RT)<=ex(Q(81,4000000)) and rF<ex(RG) and dphi>0 and drad>0 and c["M"]>=1):
        raise ValueError("the genuine full forcing inverse image does not fit inside the old product")
    x=(rF/ex(RG)).upper()
    Aosc=(2*(c["M"]-1)*x/(1-x)).upper()
    Brho=(c["B2"]*power(c["A_upper"],Q(4,3))).upper()
    Wa={};Wb={}
    for p,q in DERIVATIVE_ORDERS:
        key=str(p)+","+str(q)
        if p==0:
            value=min(c["M"],1+Aosc).upper() if q==0 else (
                math.factorial(q)*Aosc/ipow(dphi,q)).upper()
        else:
            value=(2*(c["M"]-1)*math.factorial(p)*math.factorial(q)/
                (ipow(ex(RG),p)*ipow(1-x,p+1)*ipow(dphi,q))).upper()
        Wa[key]=value
        series=sum((math.comb(p,i)*math.factorial(2)//math.factorial(2-i)
            *ipow(rF,2-i)*math.factorial(p-i)/ipow(drad,p-i)
            for i in range(min(p,2)+1)),arb(0))
        Wb[key]=(Brho*math.factorial(q)*series/ipow(dphi,q)).upper()
    forcing,forcing_parts=local_pair(Wa,Wb,c)
    Fb,Fa=forcing
    optical=(ex(Q(2,3))*power(ex(RT),Q(3,2))).upper()
    if not ex(SV)+optical+ex(SX)<ex(SF):
        raise ValueError("the two true forcing characteristics leave their full angular product")
    B0=(c["M"]+c["B2"]*power(ex(RT),Q(5,2))).upper()
    Bi=c["branch_inverse"];common=(B0*Bi).upper()
    a1=(common*ex(RT)*Fa/2+
        (common*ipow(ex(RT),2)/(2*ex(SX))+
         c["B2"]*Bi*(1+common/6)*ipow(ex(RT),3))*Fb).upper()
    b1=(common*Fb+
        (common*ipow(ex(RT),2)/(5*ex(SX))+
         c["B2"]*Bi*(ex(Q(1,2))+common/7)*ipow(ex(RT),3))*Fa).upper()
    Ri=RT/2;h=RT/10;hcover=ex(h+roots[1]-roots[0])
    if not (hcover*power(c["A_upper"],Q(2,3))<ex(Ri)
        and ex(SO)+c["flow_displacement"]<ex(SI)
        and hcover<ex(RG) and SI<SV and Ri<RT):
        raise ValueError("the actual real root cover leaves the genuine inner Cauchy rectangle")
    gt=ex(RT-Ri);gx=ex(SV-SI);mr=(ex(RG)-hcover).lower();mx=ex(SG-SO)
    canonical=[]
    for w in (a1,b1):
        canonical.append({str(p)+","+str(q):(w*math.factorial(p)*math.factorial(q)/
            (ipow(gt,p)*ipow(gx,q))).upper() for p,q in DERIVATIVE_ORDERS})
    Er=c["T_rho_error"];Xr=c["X_rho"];BT=c["Tphi"];j=c["j"]
    fold=dict(T_rho=(ex(Q(9,2))+Er).upper(),X_rho=Xr,T_phi=BT,X_phi=(1+j).upper(),
        T_rhorho=(Er/mr).upper(),X_rhorho=(Xr/mr).upper(),
        T_rhophi=min(Er/mx,BT/mr).upper(),X_rhophi=min(Xr/mx,j/mr).upper(),
        T_phiphi=(BT/mx).upper(),X_phiphi=(j/mx).upper())
    old_a=canonical_to_old(canonical[0],fold);old_b=canonical_to_old(canonical[1],fold)
    residual,residual_parts=local_pair(old_a,old_b,c)
    allvalues=list(Wa.values())+list(Wb.values())+forcing+[a1,b1]+list(old_a.values())+list(old_b.values())+residual
    if not all(v.is_finite() and v.lower()>=0 for v in allvalues):
        raise ValueError("a complete first-amplitude or local residual bound is invalid")
    return dict(exact_forcing_T_radius=str(RT),exact_forcing_X_width=str(SF),
        exact_amplitude_X_width=str(SV),exact_quotient_Cauchy_X_margin=str(SX),
        exact_inner_T_radius=str(Ri),exact_inner_X_width=str(SI),
        exact_original_output_phi_width=str(SO),exact_nominal_real_root_radius=str(h),
        exact_original_real_cover=[str(roots[0]-h),str(roots[1]+h)],
        actual_root_distance_upper=compact(hcover),
        complete=True,forcing_inverse_image_radius=compact(rF),
        forcing_old_angular_width=compact(c["sigma"]),
        positive_domain_margins=encode(dict(old_radial=drad,old_angular=dphi,
            characteristic_remaining=ex(SF-SV-SX)-optical,canonical_radial=gt,canonical_angular=gx,
            original_radial=mr,original_angular=mx)),
        leading_constant_free_a_derivatives=encode(Wa),leading_quadratic_b_derivatives=encode(Wb),
        complete_first_forcing=encode(dict(Fb=Fb,Fa=Fa)),
        first_forcing_separate_parts=encode(forcing_parts),
        separated_first_amplitude_suprema=encode(dict(a1=a1,b1=b1,B0=B0,B0_inverse=Bi)),
        canonical_first_amplitude_derivatives=encode(dict(a=canonical[0],b=canonical[1])),
        actual_old_fold_first_and_second_chain_bounds=encode(fold),
        original_first_amplitude_derivatives=encode(dict(a=old_a,b=old_b)),
        complete_local_L0_w1_amplitude_bounds=encode(dict(first=residual[0],second=residual[1])),
        local_L0_w1_separate_parts=encode(residual_parts),
        exact_same_first_amplitude_as_real_piecewise_transport=True,
        artificial_interface_source_inserted=False,
        complete_inner_local_L0_w1_amplitude_budget_paid=True,
        full_frequency_source_operator_norm_paid=False,
        complete_two_sided_L0_w1_and_old_inverse_source_paid=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("repo-root","manifest","out"):p.add_argument("--"+k,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematical work requires the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5"):
        raise RuntimeError("the exact declared numerical environment changed")
    if a.out.exists():raise FileExistsError("retain every actual result and accepted prefix")
    ctx.prec=320;started=time.monotonic()
    doc=dict(kind="actual_complex_inner_root_first_Airy_forcing_and_local_next_residual_v1",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),runtime=runtime,complete=False,proved=False,failure=None,gates=[],
        background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        exact_complex_parameter_radius=str(DELTA),actual_intrinsic_parameter="eta_0",
        root_germ_sha256=ROOT_SHA,root_budget_native_sha256=BUDGET_SHA,
        original_fold_native_sha256=FOLD_SHA,original_leading_native_sha256=LEADING_SHA,
        original_target_fold_ray_and_leading_amplitude_solves_recomputed=0,
        original_completed_zeroth_order_coefficient_values_recomputed=0,
        new_original_cubic_derivative_components=0,reused_original_cubic_derivative_components=0,
        new_coefficient_budget_cases=0,new_forcing_cases=0,reused_forcing_cases=0,
        all65_base_and193_direction_components_retained=True,independent_even_mean_retained=True,
        independent_even_mean_operator_budget_paid=False,complete_old_circle_remainder_on_w1_paid=False,
        real_only_intrinsic_jets_used_for_complex_derivatives=False,
        artificial_root_interface_or_background_analytic_extension_inserted=False,
        complete_full_frequency_strong_return_norm_paid=False,
        numerical_cutoff97_inverse_or_true_PDE_branch_claimed=False,
        polynomial_derivatives={"candidate":[],"response":[]},cases=[])
    def checkpoint():
        doc["seconds"]=time.monotonic()-started;save(a.out,doc)
    def gate(name,value):
        passed=bool(value);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual complex inner forcing gate failed: "+name)
    try:
        manifest=read(a.manifest);doc["input_manifest_sha256"]=sha(a.manifest)
        for f in manifest["files"]:
            fp=a.repo_root/f["path"]
            if not fp.is_file() or sha(fp)!=f["sha256"] or fp.stat().st_size!=f["bytes"]:
                raise ValueError("a complete original pinned input changed: "+f["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        germ,rb,fold,leading,cp,zp=[read(paths[k]) for k in
            ("root_germ","root_budget","fold_process","leading_process","candidate_index","response_index")]
        gate("the exact complete root germ and full parameter scalarization retain their original identities",
            sha(paths["root_germ"])==ROOT_SHA and sha(paths["root_budget"])==BUDGET_SHA
            and germ["complete"] and germ["proved"] and germ["failure"] is None
            and rb["complete"] and rb["proved"] and rb["failure"] is None
            and germ["candidate_sha256"]==rb["candidate_sha256"]==CANDIDATE
            and germ["object_sha256"]==OBJECT and rb["background_definition_sha256"]==BASE
            and rb["explicit_direction_definition_sha256"]==ZDEF
            and germ["source_sha256"]=="a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"
            and rb["source_sha256"]=="4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"
            and str(rb["public_run_id"])=="43594466882" and all(g["passed"] for g in rb["gates"]))
        for name,d,rid,ns,ss,count in (
            ("fold",fold,"43602612900",FOLD_SHA,"2c680f47bc5209bd78f0643d7d425485bc597f05ad96c932109d93f2b26b2ab6",16),
            ("leading",leading,"43612196888",LEADING_SHA,"dc343805acfdae67302ae2501517955eb88eef706daff17711feaf7457fb9919",22)):
            gate("actual_complete_original_"+name+"_receipt_and_all_gates",
                d["complete"] and d["actual_returncode"]==0 and d["mathematical_complete"]
                and d["public_repository"]==PUBLIC and str(d["run_id"])==rid
                and d["native_sha256"]==ns and d["mathematical_source_sha256"]==ss
                and len(d["mathematical_gates"])==count and all(g["passed"] for g in d["mathematical_gates"]))
        budget_process=read(paths["root_budget_process"])
        gate("the_original_root_budget_has_its_actual_public_zero_return_receipt",
            budget_process["complete"] and budget_process["actual_returncode"]==0
            and budget_process["mathematical_complete"] and str(budget_process["run_id"])=="43594466882"
            and budget_process["native_sha256"]==BUDGET_SHA
            and len(budget_process["mathematical_gates"])==13
            and all(g["passed"] for g in budget_process["mathematical_gates"])
            and rb["actual_intrinsic_parameter"]=="eta_0"
            and rb["exact_intrinsic_parameter"]==germ["exact_center_parameter"])
        roots=list(map(Q,germ["root_interval"]));cell=list(map(Q,germ["exact_candidate_piece_interval"]))
        rect=list(map(Q,germ["complex_radial_rectangle"]["real_interval"]))
        imag=Q(germ["complex_radial_rectangle"]["imaginary_half_width"])
        scalarcell=list(map(Q,germ["original_scalar_germ"]))
        gate("the original saved complex rectangle itself is wholly inside the identical actual root piece",
            rect==[roots[0]-RN,roots[1]+RN] and imag==RN
            and cell[0]<rect[0]<rect[1]<cell[1]
            and scalarcell[0]<rect[0]<rect[1]<scalarcell[1]
            and germ["actual_candidate_piece"]==rb["exact_candidate_and_response_piece"]==2549
            and Q(germ["complex_radial_radius"])==Q(rb["exact_outer_radial_radius"])==RN
            and list(map(Q,rb["exact_root_interval"]))==roots
            and Q(rb["exact_complex_parameter_radius"])==DELTA
            and Q(germ["moving_phi_strip"])==Q(rb["exact_moving_Wiener_strip"])==SN
            and germ["domain_contains_disks_about_every_true_parameter_root"]
            and germ["compact_bump_identically_zero_on_entire_actual_germ"] and rect[0]>Q(9,50))
        gate("the original whole old product and separate canonical inverse domains are retained",
            Q(leading["exact_original_radial_radius"])==RG
            and Q(leading["actual_canonical_outer_T"])==Q(fold["canonical_radial_radius"])==Q(81,4000000)
            and Q(leading["actual_canonical_outer_X"])==Q(fold["inverse_canonical_angular_width"])==SF
            and leading["exact_complex_parameter_radius"]==str(DELTA)
            and leading["original_native_sha256"]["fold"]==FOLD_SHA
            and leading["complete_leading_two_amplitude_formula_proved"]
            and leading["complete_leading_amplitude_bounds_paid"])
        gate("both original exact finite indices retain every component and the correct physical normalization",
            sha(paths["candidate_index"])==CANDIDATE
            and sha(paths["response_index"])=="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
            and cp["coefficient_shape"]==[4,6144,65] and zp["coefficient_shape"]==[4,6144,193]
            and cp["metadata"]["modes"]==32 and zp["metadata"]["modes"]==96
            and cp["metadata"]["physical_frequency_factor"]==zp["metadata"]["physical_frequency_factor"]==4
            and zp["metadata"]["background_candidate_sha256"]==CANDIDATE
            and zp["metadata"]["finite_head_mean_was_not_removed_from_the_solve"]
            and len(rb["exact_background_root_offsets"])==65
            and len(rb["response_repaired_complete_coefficient_upper"])==193)
        if a.resume:
            previous=read(a.resume)
            gate("accepted complex derivative and forcing prefixes have all identical scientific pins",
                previous["source_sha256"]==sha(__file__) and previous["input_manifest_sha256"]==sha(a.manifest)
                and previous["runtime"]==runtime and previous["root_germ_sha256"]==ROOT_SHA
                and previous["root_budget_native_sha256"]==BUDGET_SHA
                and previous["original_fold_native_sha256"]==FOLD_SHA
                and previous["original_leading_native_sha256"]==LEADING_SHA)
            doc["polynomial_derivatives"]=previous["polynomial_derivatives"]
            doc["cases"]=previous["cases"]
            if previous.get("complete_coefficient_budget"):
                doc["complete_coefficient_budget"]=True
                doc["complete_coefficient_budget_numeric"]=previous["complete_coefficient_budget_numeric"]
        doc["reused_original_cubic_derivative_components"]=sum(map(len,doc["polynomial_derivatives"].values()))
        doc["reused_forcing_cases"]=sum(bool(c.get("complete")) for c in doc["cases"])
        radial=acb(ex(rect[0]).union(ex(rect[1])),arb(0,ex(imag)))
        for name,index,mode,first,end,partsha in (
            ("candidate",cp,32,1346,2692,"3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"),
            ("response",zp,96,2265,2718,"ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917")):
            part=next(x for x in index["parts"] if x["first_interval"]<=2549<x["last_interval_exclusive"])
            path=paths[name+"_shard"];local=2549-first
            gate("the_complete_original_"+name+"_shard_has_its_exact_range_and_bytes",
                part["first_interval"]==first and part["last_interval_exclusive"]==end
                and part["sha256"]==sha(path)==partsha and part["bytes"]==path.stat().st_size
                and part["file"]==path.name)
            with np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False) as z:
                nodes=z["radial_nodes"].copy();coeff=z["piece_coefficients"].copy()
            gate("the_original_"+name+"_piece_has_the_full_complex_domain_and_every_finite_component",
                nodes.shape==(end-first+1,) and coeff.shape==(4,end-first,2*mode+1)
                and np.isfinite(nodes).all() and np.isfinite(coeff).all()
                and (np.diff(nodes)>0).all()
                and [dyadic(nodes[local]),dyadic(nodes[local+1])]==cell)
            x=radial-acb(ex(cell[0]));scale=ex(Q(cp["metadata"]["exact_float_amplitude"])) if name=="candidate" else arb(1)
            saved=doc["polynomial_derivatives"][name]
            if len(saved)>2*mode+1:raise ValueError("an accepted derivative prefix has too many components")
            for j in range(2*mode+1):
                if j<len(saved):
                    if saved[j]["component"]!=j:raise ValueError("an accepted exact derivative changed component")
                    continue
                z=((3*acb(ex(dyadic(coeff[0,local,j])))*x
                    +2*acb(ex(dyadic(coeff[1,local,j]))))*x
                    +acb(ex(dyadic(coeff[2,local,j]))))*scale
                if not z.is_finite():raise ValueError("a true original complex cubic derivative is not finite")
                saved.append(dict(component=j,real=rec(z.real),imag=rec(z.imag),modulus_upper=rec(up(z))))
                doc["new_original_cubic_derivative_components"]+=1
                if j%32==0:checkpoint()
            checkpoint()
        gate("every original positive-order component is retained and every value repair has zero radial derivative",
            len(doc["polynomial_derivatives"]["candidate"])==65
            and len(doc["polynomial_derivatives"]["response"])==193)
        if doc.get("complete_coefficient_budget"):
            c=decode(doc["complete_coefficient_budget_numeric"])
        else:
            c=coefficient_budget(germ,rb,fold,leading,doc["polynomial_derivatives"])
            doc["complete_coefficient_budget_numeric"]=encode(c)
            doc["complete_coefficient_budget"]=True;doc["new_coefficient_budget_cases"]+=1;checkpoint()
        gate("the true complete complex coefficient radial and mean costs have positive forcing-domain gaps",
            c["eta_lower"]>0 and c["mu_lower"]>0 and c["A_lower"]>0
            and ex(SN)<c["sigma"]<ex(SG) and c["M"]>=1
            and all(x.is_finite() for x in c["U"]+c["V"]+c["Ur"]+c["Vr"]))
        for i,RT in enumerate(RADII):
            if i<len(doc["cases"]):
                if doc["cases"][i]["exact_forcing_T_radius"]!=str(RT):
                    raise ValueError("an accepted actual forcing rectangle changed")
                if doc["cases"][i]["complete"]:continue
                raise ValueError("an unsupported partial atomic scalar case was encountered")
            out=consume_case(RT,c,roots);doc["cases"].append(out);doc["new_forcing_cases"]+=1;checkpoint()
        gate("all three forcing rectangles and complete inner local first-amplitude residuals are paid",
            len(doc["cases"])==3 and all(d["complete"] and d["complete_inner_local_L0_w1_amplitude_budget_paid"]
                for d in doc["cases"]))
        doc.update(exact_root_interval=list(map(str,roots)),
            exact_original_complex_radial_rectangle=germ["complex_radial_rectangle"],
            exact_original_root_piece_interval=list(map(str,cell)),
            constant_background_and_direction_repairs_have_zero_piece_derivative=True,
            complete_old_product_leading_constants_reused=True,
            complete=True,proved=True)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(dict(complete=doc["complete"],failure=doc["failure"],
            derivative_components=sum(map(len,doc["polynomial_derivatives"].values())),
            complete_cases=len(doc["cases"]),seconds=doc["seconds"])),flush=True)
if __name__=="__main__":main()
