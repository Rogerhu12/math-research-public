#!/usr/bin/env python3
"""Complete genuine negative physical sources by exact reuse of accepted bounds.

Only new positive-linear comparisons, ordered derivative majorants and the two
complete physical source rows are evaluated. Every earlier target, fold, ray,
profile, norm, Taylor coefficient and successful RF/output table is read only.
All reproducible working data remain temporary under the current rule15.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

TOPIC="topics/visible-flex-exact-nearby/"
PUBLIC="Rogerhu12/math-research-public"
KIND="actual_complete_genuine_negative_physical_sources_v1"
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
    if min(len(a),len(b))<=k:raise ValueError("an ordered product lacks an angular derivative")
    return [up(sum((math.comb(n,i)*a[i]*b[n-i] for i in range(n+1)),arb(0)))
            for n in range(k+1)]
def scale(a,b):return [up(rb(b)*v) for v in a]
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


G_EXEC="1fe8a528ec5e22dedc0803a129591de2fd3f25d148c5e57cb1c619cc06463bc1"
G_SOURCE="617bf821e9cff5847b4257e448fe8556eda63acf5c018105a2dff32ac452cf8a"
G_MANIFEST="aadf3e2bcf02d818e12c8950b4b4eb523345a4a63777a16d39720f98040a5e3f"
OLD_NATIVE="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
OLD_PROCESS="f888e47e69f41b4b5c73656ac9afd321289a806ce948816d9612111a045d99e4"
OLD_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
OLD_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
CONTRACT="98d3a51630cc94f5116a847c72a5ba952aab88c3ccbda62a0fd575e71841f7b4"
SB=Q(1,64);CW=Q(1,32)
BRANCHES=("central","positive_characteristic","negative_characteristic")

def add(*vectors,k=None):
    if not vectors:raise ValueError("empty complete derivative sum")
    if k is None:k=min(map(len,vectors))-1
    if min(map(len,vectors))<=k:raise ValueError("a complete derivative sum is missing a term")
    return [up(sum((v[j] for v in vectors),arb(0))) for j in range(k+1)]

def const(v,k):return [up(v)]+[arb(0) for _ in range(k)]
def zeros(k):return [arb(0) for _ in range(k+1)]
def vadd(*v,k=None):return [add(*(a[i] for a in v),k=k) for i in range(2)]
def vmul(a,v,k):return [prod(a,v[i],k) for i in range(2)]
def vscale(v,a):return [scale(x,a) for x in v]
def vdiff(v):return [x[1:] for x in v]
def vmat(A,v,k):
    return [add(*(prod(A[i][j],v[j],k) for j in range(2)),k=k) for i in range(2)]
def matrix_add(A,B,k):
    return [[add(A[i][j],B[i][j],k=k) for j in range(2)] for i in range(2)]

def nonnegative(v,name):
    v=rb(v)
    if not v.is_finite() or v.lower()<0:raise ValueError("nonfinite or negative complete bound: "+name)
    return v.upper()

def lower_budget(v):
    v=rb(v).lower()
    return v if v.is_finite() and v>0 else None

def actual_amplitude_rows(S):
    case=next(c for c in S["cases"] if Q(c["exact_output_old_phi_width"])==0)
    fields={f["field"]:f for f in case["fields"]}
    if set(fields)!={"fa","fb","a1","b1"}:raise ValueError("the accepted complete S fields changed")
    out={}
    for name in ("a1","b1"):
        f=fields[name]
        if not (f["original_complete_bound_only_read"] and f["full_radial_and_Fourier_tails_retained"]
                and f["joint_sum_of_radial_coefficient_suprema"]):
            raise ValueError("the retained amplitude is not the original complete joint bound")
        rows={}
        for row in f["complete_mixed_derivative_rows"]:
            p=row["radial_derivative_order"]
            if p not in (0,1,2) or row["angular_derivative_orders"]!=[0,1,2,3]:
                raise ValueError("changed complete amplitude derivative orders")
            if len(row["complete_joint_Wiener_upper"])!=4:raise ValueError("a saved angular coefficient is missing")
            rows[p]=row["complete_joint_Wiener_upper"]
        if set(rows)!={0,1,2}:raise ValueError("incomplete saved radial derivative table")
        out[name]=rows
    return out

def positive_linear_calibration(S,G,f,gate):
    """C1--5: infer bounds for fixed positive coefficients, without old profiles."""
    saved=actual_amplitude_rows(S);rows=G["operator_rows"]
    gate("the four accepted operators use the identical complete profile and three fixed label branches",
        len(rows)==4 and rows[0]["amplitude"]=="original_complete_leading_w0"
        and [r["radial_derivative_order"] for r in rows]==[0,0,1,2]
        and all(r["mean_output_included"] is True and r["one_sided_radial_cover"]==str(H)
                and [d["branch"] for d in r["decomposition"]]==list(BRANCHES) for r in rows)
        and all(r["only_amplitude_radial_derivative"] is True for r in rows[1:]))
    betas=[];labels=[]
    for p in range(3):
        b=[lower_budget(v) for name in ("a1","b1") for v in saved[name][p][:3]]
        betas.append(b);labels.append("original_complete_w1V_radial_order_"+str(p))
    # These are lower bounds for the positive numbers supplied to the old
    # leading-majorant algorithm, not for the actual leading derivatives.
    Glo=lower_budget(f["G"]);j0=lower_budget(f["j"]);a0=lower_budget(f["BA"])
    if Glo is None or j0 is None or a0 is None:
        lead=[None]*6
    else:
        j=(ex(H/RG)*j0).lower();a1=(ex(H/RG)*a0).lower()
        Am_upper=up(f["Am"]);gap(Am_upper,"original leading bound-number A")
        y=(ex(Q(2,3)*H)*powr(Am_upper,Q(-1,3))*a1).lower()
        lead=[Glo,(2*Glo*j/ex(SG)).lower(),(4*Glo*j/ex(SG*SG)).lower(),
            (2*Glo*y).lower(),(2*Glo*y/ex(SG)).lower(),(4*Glo*y/ex(SG*SG)).lower()]
        lead=[v if v>0 else None for v in lead]
    betas=[lead]+betas;labels=["original_positive_leading_majorant"]+labels
    coeff=[];evidence=[]
    for branch in BRANCHES:
        Ks=[up(next(d["complete_operator_coefficient"] for d in r["decomposition"] if d["branch"]==branch))
            for r in rows]
        cc=[];origins=[]
        for ell in range(6):
            choices=[(up(Ks[p]/b[ell]),p) for p,b in enumerate(betas) if b[ell] is not None]
            if not choices:raise ValueError("no positive old algorithm-input lower endpoint")
            v,p=min(choices,key=lambda t:t[0])
            cc.append(v.upper());origins.append(dict(component=ell,original_budget=labels[p],
                denominator_is_lower_for_bound_number_only=True,
                positive_budget_parameter_lower=rec(betas[p][ell])))
        coeff.append(cc);evidence.append(dict(branch=branch,complete_positive_linear_coefficients=list(map(rec,cc)),
            exact_input_component_order=["a","a_phi","a_phiphi","b","b_phi","b_phiphi"],selected_inputs=origins))
    gate("all eighteen genuine positive-linear coefficients have strict budget-number denominators",
        len(coeff)==3 and all(v.is_finite() and v>0 for a in coeff for v in a))
    known=[up(r["complete_rho_minus_quarter_operator_coefficient"]) for r in rows]
    return coeff,known,evidence

class CompleteOperator:
    """Only the new positive comparison is evaluated; no old profile is present."""
    def __init__(self,coeff):
        self.coeff=coeff;self.evaluations=0
    def __call__(self,w,known=None):
        if len(w)!=2 or min(map(len,w))<3:raise ValueError("the two-column operator needs both complete derivative triples")
        b=list(w[0][:3])+list(w[1][:3])
        ans=up(sum((sum((a[i]*b[i] for i in range(6)),arb(0)) for a in self.coeff),arb(0)))
        self.evaluations+=1
        return min(ans,up(known)).upper() if known is not None else ans

def cauchy(M,width,k):
    if Q(width)<=0:raise ValueError("a complex derivative lacks positive width")
    return [up(math.factorial(q)*M/ex(Q(width)**q)) for q in range(k+1)]

def zero_cauchy(M,m,p,q):
    dr=ex(RG-H);gap(dr,"original leading radial Cauchy margin")
    numerator=sum((math.comb(m,ell)*ex(H**(m-ell))/(dr**(p-ell))
        for ell in range(min(p,m)+1)),arb(0))
    fact=math.factorial(p)*math.factorial(q)
    z=up(fact*M*numerator/(ex(RG**m)*ex(SG**q)))
    ordinary=up(fact*M/((dr**p)*ex(SG**q)))
    return min(z,ordinary).upper()

def complete_amplitude_inputs(S,G,f,majorants):
    rows=actual_amplitude_rows(S)
    aM=up(majorants["a0"][0]);bM=up(majorants["b0"][0])
    if majorants["a0"][1:]!=[str(RG),str(SG)] or majorants["b0"][1:]!=[str(RG),str(SG)]:
        raise ValueError("the complete leading product changed")
    leading=[];correction=[]
    for p,last in ((0,4),(1,3),(2,2)):
        aa=[];bb=[]
        for q in range(last+1):
            if p==q==0:
                aa.append(min(aM,up(1+ex(H/RG)*(aM+1))).upper())
            else:
                aa.append(min(zero_cauchy(aM+1,1,p,q),
                    up(math.factorial(p)*math.factorial(q)*aM/(ex(RG-H)**p*ex(SG)**q))).upper())
            bb.append(zero_cauchy(bM,2,p,q))
        leading.append([aa,bb])
        ww=[[up(v) for v in rows[name][p][:min(last,3)+1]] for name in ("a1","b1")]
        if p==0:
            for i,name in enumerate(("a1","b1")):
                ww[i].append(up(G["missing_derivative_conclusions"]["complete_real_fourth_angle_first_correction_upper"][name]))
        correction.append(ww)
    return leading,correction

def complete_coefficient_jets(c,f,Hv,P,G,gate):
    """New ordered-source coefficient jets on the unchanged old product."""
    inv=Hv["old_circle_inverse"];missing=G["missing_derivative_conclusions"]
    gate("the complete same-product inverse and its accepted real missing derivatives cover the true physical piece",
        Q(inv["exact_old_rho_radius"])>H and Q(inv["exact_inverse_phi_strip"])==SB
        and inv["full_physical_root_piece_covered"] is True and inv["full_mean_output_retained"] is True
        and inv["inverse_constant_subtraction"]=="-i epsilon times identity, retained exactly"
        and Q(inv["exact_full_physical_root_cover"])==H)
    Bfull=[up(v) for v in inv["complete_inverse_HV_angular_derivative_bounds"]]
    bnew=next(v for v in missing["genuine_inverse_missing_angular_orders"] if Q(v["exact_output_phi_strip"])==0)
    Bfull.extend(up(bnew[k]) for k in ("B_phi3_upper","B_phi4_upper"))
    V=[up(v) for v in inv["complete_composed_V_angular_derivative_bounds"]]
    if len(Bfull)!=5 or len(V)!=3:raise ValueError("accepted inverse or potential derivative orders changed")
    V.extend([up(V[2]/ex(SB)),up(2*V[2]/ex(SB*SB))])
    ratio=ex(H/RG);jj=up(ratio*up(f["j"]));yy=up(ratio*ratio*up(f["BT"]))
    x=[up(1+jj)]+[up(math.factorial(q)*jj/ex(SG**q)) for q in range(1,5)]
    y=cauchy(yy,SG,4)
    T=[up(ratio*up(f["TM"]))]+y[:4]
    Am=gap(f["Am"],"complete original A lower bound")
    q0=up(f["Q"]);q1=up(q0*up(f["BA"])*ratio/(3*Am))
    QQ=[q0]+[up(math.factorial(q-1)*q1/ex(SG**(q-1))) for q in range(1,5)]
    Qr=[up(math.factorial(q)*q0/(ex(RG-H)*ex(SG**q))) for q in range(3)]
    determinant=gap(inv["complete_deformed_determinant_modulus_lower"],"accepted full deformed determinant")
    b12=up(yy*(T[0]+V[0]/(N*N))/determinant);b21=up(yy/determinant)
    off12=[min(Bfull[q],up(math.factorial(q)*b12/ex(SB**q))).upper() for q in range(5)]
    off21=[min(Bfull[q],up(math.factorial(q)*b21/ex(SB**q))).upper() for q in range(5)]
    B=[[Bfull,off12],[off21,Bfull]]
    deltaH=up(jj+yy*max(arb(1),T[0]+V[0]/(N*N)))
    delta0=up(Bfull[0]*deltaH)
    deltaDiag=[delta0]+[min(Bfull[q],up(math.factorial(q)*delta0/ex(SB**q))).upper() for q in range(1,5)]
    deltaB=[[deltaDiag,off12],[off21,deltaDiag]]
    # Fixed matrix order: first the row (i epsilon y,x), then B e1.
    QV=prod(QQ,V,4);row=[y,x]
    rank=[[prod(QV,prod(B[i][0],row[j],4),4) for j in range(2)] for i in range(2)]
    principal=[[zeros(4),prod(QQ,T,4)],[QQ,zeros(4)]]
    pmat=matrix_add(principal,[[scale(v,Q(1,N*N)) for v in rr] for rr in rank],4)
    D=[up(v) for v in c["D"]];Dr=[up(v) for v in c["Dr"]]
    if len(D)<5 or len(Dr)<3:raise ValueError("original full drift jets are incomplete")
    T0=[up(c["T0"]),up(5*D[2]),up(5*D[3])]
    V0=cauchy(up(c["V0"]),CW,2);theta=cauchy(up(c["vartheta"]),CW,2)
    DQ=add(Qr,prod(D,QQ[1:],2),k=2)
    AT=add(prod(add(DQ,prod(QQ,D[1:],2),prod(T0,QQ,2),k=2),x,2),
        prod(prod(QQ,QQ[1:],2),prod(T,y,2),2),
        prod(prod(QQ,QQ,2),prod(y,y,2),2),k=2)
    mu=prod(prod(QQ,QQ,2),add(prod(x,x,2),prod(T,prod(y,y,2),2),k=2),2)
    pot=next(z for z in P["cases"] if Q(z["exact_complex_radial_radius"])==Q(1,6000))
    M1=up(pot["complete_modulus_upper"]["V_T"]);M2=up(pot["complete_modulus_upper"]["V_TT"])
    M3=up(missing["complete_V_TTT_on_actual_old_image_upper"])
    gate("the accepted third T derivative has its strict complete image margin",
        gap(missing["complete_V_TTT_image_margin_lower"],"old potential image margin")>0
        and Q(pot["exact_complex_z_square_halfwidth"])==Q(1,97*97))
    VT=[M1,up(M2*y[0]),up(M3*y[0]*y[0]+M2*y[1])]
    Rtheta=[[prod(theta,rank[i][j],2) for j in range(2)] for i in range(2)]
    return dict(B=B,deltaB=deltaB,P=pmat,Rtheta=Rtheta,Q=QQ,Qr=Qr,V=V,VT=VT,T=T,x=x,y=y,
        D=D,Dr=Dr,T0=T0,V0=V0,theta=theta,AT=AT,mu=mu,
        eta2K=up(up(c["ep"])*up(c["ep"])*up(c["K"])),
        complete_complex_product_width=str(SB),same_original_fold_and_genuine_profile=True)

def local_vectors(w0,w1,C,known,A):
    """V25, including the raw numerator and exact left E12 placement."""
    D=C["D"];Dr=C["Dr"];Qj=C["Q"];T=C["T"];V=C["V"]
    def Dword(w):
        return vadd(w[1],vmul(D,vdiff(w[0]),3),k=3)
    def correction(w):
        dw=Dword(w)
        inner=vadd(vmul(C["x"],dw,2),
            vmul(prod(prod(Qj,T,2),C["y"],2),vdiff(w[0]),2),k=2)
        first=vmul(scale(prod(Qj,V,2),2),inner,2)
        coeff=add(prod(C["mu"],C["VT"],2),prod(C["AT"],V,2),k=2)
        allv=vadd(first,vmul(coeff,w[0],2),k=2)
        return [allv[1],zeros(2)] # actual E12 is on the left
    dw=Dword(w1)
    rest=vadd(vmul(scale(D,2),vdiff(w1[1]),2),
        vmul(add(prod(D,D[1:],2),Dr,k=2),vdiff(w1[0]),2),
        vmul(prod(D,D,2),vdiff(vdiff(w1[0])),2),
        vscale(vdiff(vdiff(w1[0])),C["eta2K"]),
        vmul(C["T0"],dw,2),vmul(C["V0"],w1[0],2),
        vmul(prod(C["mu"],V,2),w1[0],2),k=2)
    off=[prod(T,w1[0][1],2),w1[0][0][:3]]
    rest=vadd(rest,vmul(prod(C["theta"],Qj,2),off,2),correction(w0),k=2)
    L1=vadd(w1[2],rest,k=2)
    L2=vadd(correction(w1),vmat(C["Rtheta"],w0[0],2),k=2)
    L3=vmat(C["Rtheta"],w1[0],2)
    value1=min(A(L1),up(known[3]+A(rest))).upper()
    values=[value1,A(L2),A(L3)]
    weighted=[values[0],up(values[1]/N),up(values[2]/(N*N))]
    return dict(raw_complete_operator_coefficients=values,
        input_weighted_complete_operator_coefficients=weighted,
        total=up(sum(weighted,arb(0))),
        raw_numerator_not_divided_by_mu=True,exact_input_weights=["1","1/388","1/150544"],
        original_complete_w1rr_operator_reused=True),dict(L1=L1,L1_without_w1rr=rest,L2=L2,L3=L3)

def complete_nonlocal_row(c,w,C,A,density,known):
    """V26--31 in the two different source windows, with every old mean."""
    U=c["U"];V=c["V"];D=c["D"]
    if min(len(U),len(V),len(D))<5:raise ValueError("the saved full coefficient angular jets are incomplete")
    eta=gap(c["eta_lower"],"original row eta gap");etam=up(c["eta_upper"])
    z=vmat(C["P"],w[0],4);h=vscale(z,1/eta);y=vmul(V,z,4)
    dw=vadd(w[1],vmul(D,vdiff(w[0]),3),k=3)
    g=vadd(dw,vscale(vdiff(h),etam),k=3)
    q=vadd(vmul(V,dw,3),vdiff(y),k=3)
    def GM(v,old=None):
        if density==1:
            value=A(v,known=old);return value,value
        Bv=vmat(C["B"],v,3);Ev=vmat(C["deltaB"],v,3)
        original=A(v,known=old)
        Bw=min(A(Bv),up(original+A(Ev))).upper()
        mean=min(A(vdiff(Bv)),up(A(vdiff(v))+A(vdiff(Ev)))).upper()
        return up(Bw+mean),mean
    Gw,Mw=GM(w[0],known);Gh,Mh=GM(h);Gg,Mg=GM(g);Gq,Mq=GM(q)
    _,My=GM(y)
    CJ=up(c["C_J_new"] if density==0 else c["C_J_scalar"])
    CV=up(c["C_V"])
    if density==1:CV=up(CV+c["C_R"]*CJ*c["C_B"])
    # The transported mean word contains two separately preserved mean summands.
    mean_primitive=up(c["cB"]*V[1]*V[0]*Mg/4)
    mean_T0=up(c["m0_T0"]*Mg)
    terms=dict(complete_SV=up(CV*Gw),complete_SQ=up(c["C_Q"]*Gh),
        complete_RQ_J_g=up(c["C_R"]*CJ*Gg),
        complete_RQ_JL_h=up(c["C_R"]*CJ*c["C_L"]*Gh),
        complete_primitive=up(c["cB"]*c["m3_vphi"]*c["C_I"]*Gq),
        old_mean_rQ=up(c["m0_rQ"]*Mh),old_mean_vphi=up(c["cB"]*V[1]*My),
        old_mean_transported=up(mean_primitive+mean_T0),old_mean_V0=up(c["m0_V0"]*Mw))
    uh=vmul(U,h,4)
    vn=list(V);vn[0]=min(up(V[0]),up(V[1]/4)).upper()
    vmw=vmul(vn,w[0],4)
    _,Muh=GM(uh);_,Mvm=GM(vmw)
    fac=up(c["exact_nonlocal_even_mean_row_factor"])
    physical=dict(complete_u_h=up(fac*Muh),
        complete_uJ_g=up(fac*c["m3_u"]*CJ*Gg),
        complete_uJL_h=up(fac*c["m3_u"]*CJ*c["C_L"]*Gh),
        complete_uJB_w=up(fac*c["m3_u"]*CJ*c["C_B"]*Gw),
        complete_K_vminus_w=up(fac*c["K"]*Mvm))
    total=up(sum(terms.values(),arb(0)));mean=up(sum(physical.values(),arb(0)))
    if any(not v.is_finite() or v.lower()<0 for v in [total,mean,*terms.values(),*physical.values()]):
        raise ValueError("a complete genuine nonlocal or physical mean cost is invalid")
    return dict(total=total,physical_mean=mean,nine_complete_words=terms,
        five_old_mean_summands=dict(rQ=terms["old_mean_rQ"],vphi=terms["old_mean_vphi"],
            primitive_of_v=mean_primitive,T0=mean_T0,V0=terms["old_mean_V0"]),
        five_independent_physical_mean_terms=physical,
        complete_amplitude_operator_bounds=dict(Gamma_w=Gw,Gamma_h=Gh,Gamma_g=Gg,Gamma_q=Gq,
            M_w=Mw,M_h=Mh,M_g=Mg,M_y=My,M_uh=Muh,M_vminus_w=Mvm),
        J_window_index=density,actual_J_factor=CJ,complete_SV_window_factor=CV)

def source_row(row,w0,w1,C,A,local,known):
    c=unpack(row["bounds"])
    for k,v in c.items():
        for z in v if isinstance(v,list) else [v]:nonnegative(z,"original row "+k)
    n0=complete_nonlocal_row(c,w0,C,A,0,known[0])
    n1=complete_nonlocal_row(c,w1,C,A,1,known[1])
    J=up(c["C_J_scalar"])
    loc=up(J*local["total"]);nl=up(J*(n0["total"]+n1["total"]))
    mean=up(n0["physical_mean"]+n1["physical_mean"])
    terms={"local_raw_"+str(i+1):up(J*v)
        for i,v in enumerate(local["input_weighted_complete_operator_coefficients"])}
    for i,nlrow in enumerate((n0,n1)):
        for key,val in nlrow["nine_complete_words"].items():terms["density"+str(i)+"_"+key]=up(J*val)
    means={}
    for i,nlrow in enumerate((n0,n1)):
        for key,val in nlrow["five_independent_physical_mean_terms"].items():
            means["density"+str(i)+"_"+key]=val
    return dict(common_row=row["common_row"],original_interval=row["interval"],
        original_root_row=row["original_root_row"],first=up(loc+nl),local=loc,nonlocal_total=nl,mean=mean,
        first_source_terms=terms,physical_mean_terms=means,density0=n0,density1=n1,
        exact_original_row_payload_sha256=hashlib.sha256(
            json.dumps(row,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest())

def clipped_negative_rows(rows):
    left=PIECE[0];right=ROOTS[1];out=[];cursor=left
    for row in rows:
        lo,hi=map(Q,row["interval"])
        a=max(lo,left);b=min(hi,right)
        if not a<b:continue
        if a!=cursor:raise ValueError("the exact old coefficient cover lost part of the negative physical piece")
        cuts=sorted(set([a,b]+[t for t in ROOTS if a<t<b]))
        for l,r in zip(cuts,cuts[1:]):
            out.append((row,l,r))
        cursor=b
    if cursor!=right or not out:raise ValueError("the complete negative physical cover is not closed")
    return out

def radial_weight(a,b):
    if not a<b:raise ValueError("empty new physical source integration interval")
    if b<=ROOTS[0]:
        return up(2*(ex(ROOTS[0]-a).sqrt()-ex(ROOTS[0]-b).sqrt())),"strict_negative"
    if ROOTS[0]<=a<b<=ROOTS[1]:
        return up(2*ex(b-a).sqrt()),"one_sided_uncertain_root"
    raise ValueError("a new source integral crossed an unsplit true-root endpoint")

def integrate_sources(original,w0,w1,C,A,local,known,doc,temporary):
    selected=clipped_negative_rows(original["coefficient_rows"])
    cache={};sums={k:arb(0) for k in ("first","local","nonlocal_total","mean","combined")}
    firstterms={};meanterms={};finalrows=[];weights=arb(0)
    for row,l,r in selected:
        index=row["common_row"]
        if index not in cache:
            cache[index]=source_row(row,w0,w1,C,A,local,known)
            doc["new_complete_original_row_source_budgets"]+=1
        out=cache[index];weight,kind=radial_weight(l,r);weights+=weight
        for k in ("first","local","nonlocal_total","mean"):sums[k]+=out[k]*out[k]*weight
        sums["combined"]+=(out["first"]*out["first"]+out["mean"]*out["mean"])*weight
        for k,val in out["first_source_terms"].items():firstterms[k]=firstterms.get(k,arb(0))+val*val*weight
        for k,val in out["physical_mean_terms"].items():meanterms[k]=meanterms.get(k,arb(0))+val*val*weight
        finalrows.append(dict(common_row=index,interval=list(map(str,(l,r))),root_weight_kind=kind,
            complete_first_row_coefficient=rec(out["first"]),complete_even_mean_coefficient=rec(out["mean"]),
            complete_local_coefficient=rec(out["local"]),complete_nonlocal_coefficient=rec(out["nonlocal_total"]),
            new_exact_physical_measure_weight=rec(weight),
            original_complete_row_payload_sha256=out["exact_original_row_payload_sha256"]))
        doc["new_genuine_source_radial_integrals"]+=1
    temporary["new_complete_original_row_sources"]=encode(cache)
    temporary["complete_source_row_conclusions"]=finalrows
    row_hash=hashlib.sha256(json.dumps(finalrows,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False).encode()).hexdigest()
    result={k+"_L2_upper":rec(up(v.sqrt())) for k,v in sums.items()}
    result.update(complete_first_source_term_L2_upper={k:rec(up(v.sqrt())) for k,v in firstterms.items()},
        complete_independent_mean_term_L2_upper={k:rec(up(v.sqrt())) for k,v in meanterms.items()},
        exact_negative_physical_cover=[str(PIECE[0]),str(ROOTS[1])],
        actual_dr_measure=True,one_sided_uncertain_root_band_retained=True,
        total_squared_envelope_radial_weight_upper=rec(up(weights)),
        temporary_complete_source_row_count=len(finalrows),
        temporary_complete_source_row_payload_sha256=row_hash,
        complete_source_row_array_published=False,
        old_nine_word_and_five_physical_mean_counts=[9,5],
        both_density_windows_retained=True,outer_J_window="H^(-5/3) -> H^(-2/3)",
        first_output_window="ordinary L2_r H^(-2/3)",
        independent_even_mean_window="ordinary L2_r of the constant source row",
        input_window="H^(-4/3), both genuine columns and both signs |j|>=97")
    return result

def render(doc):
    lines=["# Actual complete genuine negative physical source budget","",
        "Public Actions run "+str(doc.get("run_id"))+"/"+str(doc.get("run_attempt"))+".",
        "Source SHA256: "+doc["source_sha256"]+".",
        "Input manifest SHA256: "+doc["input_manifest_sha256"]+".",
        "Actual complete/proved: "+str(doc["complete"])+"/"+str(doc["proved"])+".",
        "Actual scientific return code: "+str(doc["actual_returncode"])+".","",
        "Original target, FFT, intrinsic, repair, fold, transport, Taylor, RF, profile and old norm reevaluations: 0.",
        "Both genuine columns, both signed input labels, full old-circle output, both J windows and the independent physical even mean remain.",
        "The actual result covers only the negative part of the one original physical root piece.",
        "True endpoint/reference seams, the positive affine graph, source-to-wave traces and final feedback remain separate.","",
        "## Actual scope and new work","",json.dumps(doc.get("scope",{}),sort_keys=True),
        "",json.dumps({k:doc[k] for k in (
            "original_complete_fold_stages_read","original_successful_small_receipts_read",
            "original_complete_coefficient_rows_read","original_selected_coefficient_rows_read",
            "new_positive_linear_calibrations","new_ordered_coefficient_jet_closures",
            "new_complete_local_vector_budgets","new_complete_original_row_source_budgets",
            "new_genuine_source_radial_integrals","new_positive_comparison_evaluations")},sort_keys=True)]
    con=doc.get("complete_source_conclusion")
    if con:
        lines+=["","## Complete two-row source conclusion","",
            "| Quantity | Directed complete upper bound |","|---|---|"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+k+" | "+con[k]["ball"]+" |")
        lines+=["","Exact negative cover: "+repr(con["exact_negative_physical_cover"])+".",
            "The root band is charged on its actual negative one-sided portion.",
            "Local and nonlocal are independent complete upper bounds; their numerical difference is not an error estimate.","",
            "## Complete first-row term bounds","",
            "| Retained term | Ordinary radial L2 upper |","|---|---|"]
        for k,v in con["complete_first_source_term_L2_upper"].items():lines.append("| "+k+" | "+v["ball"]+" |")
        lines+=["","## Independent physical even-mean terms","",
            "| Retained term | Ordinary radial L2 upper |","|---|---|"]
        for k,v in con["complete_independent_mean_term_L2_upper"].items():lines.append("| "+k+" | "+v["ball"]+" |")
        lines+=["","The "+str(con["temporary_complete_source_row_count"])+" complete original-row intersections and coefficients are temporary only.",
            "Complete temporary row-payload SHA256: "+con["temporary_complete_source_row_payload_sha256"]+"."]
    if "complete_local_vector_conclusion" in doc:
        lines+=["","## Three complete raw local vectors","",json.dumps(doc["complete_local_vector_conclusion"],sort_keys=True)]
    if "complete_positive_linear_operator_conclusion" in doc:
        lines+=["","## Complete positive linear coefficient readout","",
            "These bound fixed coefficients of the original algorithm; the positive denominators are lower endpoints of its input budget numbers, not of the true amplitudes.","",
            "| Fixed branch | Six complete positive coefficients |","|---|---|"]
        for r in doc["complete_positive_linear_operator_conclusion"]:
            lines.append("| "+r["branch"]+" | "+"; ".join(v["ball"] for v in r["complete_positive_linear_coefficients"])+" |")
    lines+=["","## Actual gates",""]+["- "+g["name"]+": "+str(g["passed"])+"." for g in doc["gates"]]
    lines+=["","Actual scalar science seconds: "+repr(doc.get("actual_mathematical_wall_seconds"))+".",
        "Actual failure: "+str(doc.get("failure"))+".",
        "Temporary native SHA256: "+str(doc.get("temporary_native_sha256"))+".",
        "No reproducible array, derivative table, native or scientific artifact is published.",
        "No positive growing-column operator, full negative BVP inverse or numerical cutoff-97 return contraction is claimed.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new scalar arithmetic is restricted to the actual public Actions runner")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the exact scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True)
    source=sha(__file__)
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        original_target_FFT_intrinsic_repair_fold_transport_Taylor_RF_profile_or_norm_recomputed=0,
        original_complete_output_enclosures_recomputed=0,original_natural_stage_bytes_modified=0,
        original_complete_fold_stages_read=0,original_successful_small_receipts_read=0,
        original_complete_coefficient_rows_read=0,original_selected_coefficient_rows_read=0,
        new_positive_linear_calibrations=0,new_ordered_coefficient_jet_closures=0,
        new_complete_local_vector_budgets=0,new_complete_original_row_source_budgets=0,
        new_genuine_source_radial_integrals=0,new_positive_comparison_evaluations=0,
        full_physical_negative_volume_source_paid=False,full_high_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    temporary={};A=None;started=time.monotonic()
    try:
        m=read(a.manifest)
        params=dict(cutoff_abs_j=J0,physical_frequency="4j",physical_root_piece=2549,
            exact_physical_cover=str(H),exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],
            original_fold_radius=str(RG),original_fold_phi_strip=str(SG),
            genuine_inverse_phi_strip=str(SB),complete_old_coefficient_strip=str(CW),
            original_successful_operator_run="43700281022/1",
            input_window="H^(-4/3) both genuine columns and both signs",
            first_source_window="ordinary L2_r H^(-2/3)",independent_mean_window="ordinary L2_r constants",
            arithmetic_bits=320,fixed_intrinsic_parameter="eta_0",real_parameter_values_only=True)
        gate("the new complete-source script, manifest and exact mathematical parameters have their reviewed identities",
            sha(a.manifest)==a.manifest_sha and m["public_repository"]==PUBLIC
            and m["scientific_source_sha256"]==source and m["mathematical_parameters"]==params)
        doc["mathematical_parameters"]=params
        pins={e["path"]:e for e in m["files"]}
        if len(pins)!=len(m["files"]):raise ValueError("duplicate immutable input path")
        paths={}
        for e in m["files"]:
            rel=Path(e["path"])
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):raise ValueError("an input left the topic")
            q=a.repo/rel
            if not q.is_file() or q.stat().st_size!=e["bytes"] or sha(q)!=e["sha256"]:
                raise ValueError("a complete immutable input changed: "+str(rel))
        for k,v in m["input_paths"].items():
            if v not in pins:raise ValueError("an input role is not pinned: "+k)
            paths[k]=a.repo/v
        gate("all accepted scalar, operator, original coefficient and contract byte identities remain exact",
            sha(paths["contract"])==CONTRACT and sha(paths["old_fold_majorants_stage"])==MAJORANTS
            and sha(paths["adjacent_process"])==APROC and sha(paths["adjacent_publication"])==APUB
            and sha(paths["amplitude_execution"])==S_EXEC and sha(paths["potential_execution"])==P_EXEC
            and sha(paths["columns_execution"])==H_EXEC and sha(paths["operator_execution"])==G_EXEC
            and sha(paths["old_operator_algorithm"])==G_SOURCE
            and sha(paths["original_norm_native"])==OLD_NATIVE and sha(paths["original_norm_process"])==OLD_PROCESS
            and sha(paths["old_coefficient_algorithm"])==OLD_SOURCE
            and sha(paths["old_circle_contract"])=="3e02303afa6f82da01ba768d4bccbbaa0c702ce63ad4582c36d131aa1a8510d9")
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        mr=next(v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz")
        gate("the one complete original fold product is restored with its actual legacy header and no reevaluation",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and mr["bytes"]==4501 and mr["sha256"]==MAJORANTS and ap["actual_returncode"]==0
            and ap["mathematical_complete"] and ap["mathematical_proved"] and ap["mathematical_failure"] is None
            and au["complete"] and ms["payload"]["majorants"]["A"][1:]==[str(RG),str(SG)])
        original=unpack(ms["payload"]);f=original["fold"];c=original["coefficients"];majorants=original["majorants"]
        doc["original_complete_fold_stages_read"]=1
        S=current_receipt(paths["amplitude_execution"],"43698106023",S_SOURCE,S_MANIFEST,gate)
        P=current_receipt(paths["potential_execution"],"43685624307",P_SOURCE,P_MANIFEST,gate)
        Hv=current_receipt(paths["columns_execution"],"43688459733",H_SOURCE,H_MANIFEST,gate)
        G=current_receipt(paths["operator_execution"],"43700281022",G_SOURCE,G_MANIFEST,gate)
        doc["original_successful_small_receipts_read"]=4
        gate("the original root, physical piece, complete parameter squares and both carrier signs remain identical",
            S["complete_domain_conclusion"]["exact_original_physical_piece_interval"]==list(map(str,PIECE))
            and S["complete_domain_conclusion"]["exact_original_true_root_interval"]==list(map(str,ROOTS))
            and S["complete_domain_conclusion"]["true_physical_root_piece_radius"]==str(H)
            and S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and S["original_accepted_target_FFT_intrinsic_fold_or_transport_recomputed"]==0
            and S["original_signed_Taylor_coefficients_recomputed"]==0
            and S["original_complete_output_tables_recomputed"]==0
            and G["domain_conclusion"]["exact_negative_root_cover"]==str(H)
            and G["domain_conclusion"]["exact_physical_root_piece_interval"]==list(map(str,PIECE))
            and G["domain_conclusion"]["exact_true_root_interval"]==list(map(str,ROOTS))
            and G["domain_conclusion"]["both_genuine_columns_and_both_signs"]
            and G["domain_conclusion"]["complete_output_mean_retained"]
            and G["original_target_FFT_intrinsic_fold_transport_or_Taylor_recomputed"]==0
            and G["original_RF_scalar_or_output_enclosures_recomputed"]==0)
        old=read(paths["original_norm_native"]);op=read(paths["original_norm_process"])
        gate("the complete original moment and two inverse-window rows have their actual zero-return provenance",
            old["complete"] and old["proved"] and old["failure"] is None
            and old["source_sha256"]==OLD_SOURCE and old["input_manifest_sha256"]==OLD_MANIFEST
            and old["runtime"]==dict(python="3.12.14",flint="0.9.0",numpy="2.3.5")
            and all(g["passed"] for g in old["gates"])
            and op["complete"] and op["actual_returncode"]==0 and op["failure"] is None
            and op["mathematical_complete"] and op["mathematical_failure"] is None
            and op["native_sha256"]==OLD_NATIVE and op["native_bytes"]==4837715
            and op["mathematical_source_sha256"]==OLD_SOURCE and op["manifest_sha256"]==OLD_MANIFEST
            and str(op["run_id"])=="43629465215" and str(op["run_attempt"])=="1"
            and all(g["passed"] for g in op["mathematical_gates"]))
        doc["original_successful_small_receipts_read"]+=1
        rows=old["coefficient_rows"]
        gate("all original coefficient rows retain exact common cover, whole means and the same real delta family",
            len(rows)==1328 and [r["common_row"] for r in rows]==list(range(1328))
            and all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:]))
            and [rows[0]["interval"][0],rows[-1]["interval"][1]]==op["exact_cover"]
            and op["exact_root_interval"]==list(map(str,ROOTS))
            and op["exact_real_delta_radius"]==str(Q(1,100000000))
            and old["exact_real_delta_radius"]==str(Q(1,100000000))
            and old["old_mean_and_all_Fourier_outputs_retained"] is True
            and old["root_native_sha256"]=="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
            and old["first_forcing_native_sha256"]=="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47")
        doc["original_complete_coefficient_rows_read"]=len(rows)
        selected=clipped_negative_rows(rows)
        doc["original_selected_coefficient_rows_read"]=len(set(r["common_row"] for r,_,_ in selected))
        gate("the original coefficient rows cover the entire actual negative part and both root-band endpoints",
            selected[0][1]==PIECE[0] and selected[-1][2]==ROOTS[1]
            and all(a1[2]==a2[1] for a1,a2 in zip(selected,selected[1:]))
            and H==max(ROOTS[1]-PIECE[0],PIECE[1]-ROOTS[0]) and H<Q(1,20000))
        coeff,known,evidence=positive_linear_calibration(S,G,f,gate);A=CompleteOperator(coeff)
        doc["new_positive_linear_calibrations"]=1
        doc["complete_positive_linear_operator_conclusion"]=evidence
        w0,w1=complete_amplitude_inputs(S,G,f,majorants)
        C=complete_coefficient_jets(c,f,Hv,P,G,gate)
        doc["new_ordered_coefficient_jet_closures"]=1
        temporary.update(new_complete_leading_mixed_jets=encode(w0),read_complete_first_correction_mixed_jets=encode(w1),
            new_complete_ordered_coefficient_jets=encode(C))
        local,local_vectors_numeric=local_vectors(w0,w1,C,known,A)
        doc["new_complete_local_vector_budgets"]=3
        doc["complete_local_vector_conclusion"]=encode(local)
        temporary["new_complete_local_vector_majorants"]=encode(local_vectors_numeric)
        gate("all three raw local vectors retain E12 order, complete reference corrections and exact input weights",
            local["raw_numerator_not_divided_by_mu"] is True
            and local["original_complete_w1rr_operator_reused"] is True
            and len(local["raw_complete_operator_coefficients"])==3
            and all(v.is_finite() and v.lower()>=0 for v in local["raw_complete_operator_coefficients"]))
        source_conclusion=integrate_sources(old,w0,w1,C,A,local,known,doc,temporary)
        doc["complete_source_conclusion"]=source_conclusion
        gate("the complete genuine source has all selected old rows, both J windows and the full independent physical mean",
            doc["new_complete_original_row_source_budgets"]==doc["original_selected_coefficient_rows_read"]
            and doc["new_genuine_source_radial_integrals"]==len(selected)
            and source_conclusion["both_density_windows_retained"]
            and source_conclusion["old_nine_word_and_five_physical_mean_counts"]==[9,5]
            and len(source_conclusion["complete_first_source_term_L2_upper"])==21
            and len(source_conclusion["complete_independent_mean_term_L2_upper"])==10
            and all(up(source_conclusion[k]).is_finite() for k in
                ("first_L2_upper","mean_L2_upper","combined_L2_upper","local_L2_upper","nonlocal_total_L2_upper")))
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,negative_side_only=True,
            original_fixed_intrinsic_parameter="eta_0",same_original_real_explicit_family=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            output_mean_and_complete_original_primitive_retained=True,
            first_physical_volume_source_paid=True,independent_even_mean_volume_source_paid=True,
            physical_J_only_on_its_proved_reflected_parity_domain=True,
            exact_n_inverse_factors_are_input_weights=True,
            old_profile_or_original_complete_operator_recomputed=False,
            budget_parameter_lower_is_not_true_amplitude_lower=True,
            all_actual_physical_seams_and_reference_matching_sources_retained=True,
            original_positive_graph_and_outer_source_ports_retained=True,
            positive_growing_column_operator_paid=False,physical_to_wave_readout_paid=False,
            full_negative_BVP_inverse_paid=False,cutoff97_strong_return_contraction_paid=False)
        doc["full_physical_negative_volume_source_paid"]=True
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as e:
        doc["failure"]=dict(type=type(e).__name__,message=str(e))
    finally:
        if A is not None:doc["new_positive_comparison_evaluations"]=A.evaluations
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,actual_conclusions=doc)
        native=a.out_dir/"temporary-complete-genuine-negative-sources.json.gz";save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True
        actual=doc["actual_returncode"]
        try:
            text=render(doc)
            if len(text.encode())>60000:raise ValueError("the complete source conclusion exceeds 60000 bytes")
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000:raise ValueError("the complete source process exceeds 60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(text)
        except BaseException as e:
            small={k:v for k,v in doc.items() if k not in
                ("complete_source_conclusion","complete_positive_linear_operator_conclusion","complete_local_vector_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(e).__name__,message=str(e))
            small["complete"]=small["proved"]=False;small["actual_returncode"]=1
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual genuine-source formatting failure\n\n"
                "Original scientific return code: "+str(actual)+". A formatter failure is not reclassified as failed mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\nFailure: "+str(e)+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            original_numerical_enclosures_recomputed=0,new_source_rows=doc["new_complete_original_row_source_budgets"],
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
