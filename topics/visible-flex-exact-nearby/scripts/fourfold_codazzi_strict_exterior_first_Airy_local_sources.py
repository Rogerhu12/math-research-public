#!/usr/bin/env python3
"""Complete strict exterior first-correction derivatives and local Airy sources.

Only completed root/forcing/seam/Fourier natives are consumed. No original
target, FFT, cubic point, characteristic, or successful amplitude is rerun.
All new scalar calculations require the public repository Actions.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
FORCE_SHA="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47"
SEAM_SHA="871aa54de8c4ee1caa47cdab39c8033bb9cd02e9d4d1f404b711ab8c28825642"
FOLD_SHA="0ceafc2ba2adb8c1e14ab74c3059b0a0fde39446855df0889dec741f1cb61cfe"
TAYLOR_SHA="18990ac2c1ed8e559d00982b75d663c08ad7e193455de1f8482511c36938b719"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
H=Q(9,1000000);DELTA=Q(1,100000000);CUTOFF=97
SIGMA_OLD=Q(3,64);SIGMA_JET=Q(1,32);SIGMA_W=Q(1,64)
SIGMA_TRANSPORT=Q(1,128);SIGMA_OUTPUT=Q(1,512)
RADII=(Q(1,1000),Q(1,500),Q(1,200),Q(1,100),Q(3,200),Q(1,50))
K3=[(p,q) for p in range(4) for q in range(4-p)]
K4=[(p,q) for p in range(4) for q in range(5-p)]

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,compresslevel=9,mtime=0)
    temporary=path.with_name(path.name+".partial")
    temporary.write_bytes(raw);temporary.replace(path)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def box(v):
    if isinstance(v,str):return arb(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def up(x):return abs(x).upper()
def lo(x):return arb(x).lower()
def rec(x):return {"ball":arb(x).str(48)}
def encode(v):
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return rec(v)
def decode(v):
    if isinstance(v,list):return [decode(x) for x in v]
    if isinstance(v,dict):
        if "ball" in v or "lower" in v:return box(v)
        return {k:decode(x) for k,x in v.items()}
    raise ValueError("a saved numerical tensor changed its schema")
def nonnegative(v):
    if isinstance(v,dict):return all(nonnegative(x) for x in v.values())
    if isinstance(v,list):return all(nonnegative(x) for x in v)
    return v.is_finite() and v.lower()>=0
def ipow(x,n):
    if n<0:return 1/ipow(x,-n)
    value=arb(1)
    for _ in range(n):value=value*x
    return value
def power(x,p):return (arb(x).log()*ex(p)).exp()
def total(xs):return sum(xs,arb(0)).upper()
def mm(a,b):return [[total(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mv(a,b):return [total(a[i][k]*b[k] for k in range(2)) for i in range(2)]
def va(*vs):return [total(v[i] for v in vs) for i in range(2)]
def vs(v,c):return [(x*c).upper() for x in v]
def ma(*matrices):return [va(*(a[i] for a in matrices)) for i in range(2)]
def ms(a,c):return [vs(row,c) for row in a]
def jet_product(a,b,keys):
    return {(p,q):total(math.comb(p,i)*math.comb(q,j)*a.get((i,j),arb(0))*b.get((p-i,q-j),arb(0))
        for i in range(p+1) for j in range(q+1)) for p,q in keys}
def jet_add(a,b,keys):return {k:(a.get(k,arb(0))+b.get(k,arb(0))).upper() for k in keys}
def jet_scale(a,c):return {k:(v*c).upper() for k,v in a.items()}
def normalized_power(a,p,amin,keys):
    """Complete ordinary jets of A^p/A^p(0) as derivative majorants.

    The value is exactly one; nonzero derivative products use the true
    |A| lower gap. This is a pointwise chain-rule bound, not a new Taylor
    approximation of the physical field.
    """
    if not amin>0:raise ValueError("a true power denominator lost its gap")
    delta={k:(arb(0) if k==(0,0) else a.get(k,arb(0))/(math.factorial(k[0])*math.factorial(k[1]))) for k in keys}
    out={(0,0):arb(1)};current={(0,0):arb(1)};coefficient=Q(1)
    def mul_normalized(u,v):
        return {(r,s):total(u.get((i,j),arb(0))*v.get((r-i,s-j),arb(0))
            for i in range(r+1) for j in range(s+1)) for r,s in keys}
    for ell in range(1,max(sum(k) for k in keys)+1):
        current=mul_normalized(current,delta)
        coefficient*=Q(p-ell+1,ell)
        factor=ex(abs(coefficient))*power(amin,-ell)
        for key in keys:
            if key!=(0,0):out[key]=out.get(key,arb(0))+factor*current[key]
    return {k:(out.get(k,arb(0))*math.factorial(k[0])*math.factorial(k[1])).upper() for k in keys}

def coefficient_row(row,rootrow):
    """New first coefficient derivatives from complete saved ordinary jets."""
    st=row["strips"]["1/16"];rs=rootrow["strips"]["1/16"]
    U=[[up(box(x)) for x in rs["U"]]]+[[up(box(x)) for x in a] for a in st["U_radial"]]
    V=[[up(box(x)) for x in rs["V"]]]+[[up(box(x)) for x in a] for a in st["V_radial"]]
    if len(U)!=4 or len(V)!=4 or any(len(x)<2 for x in U+V):
        raise ValueError("a complete original radial/angle derivative row is missing")
    intrinsic=row["complete_intrinsic_ordinary_jets"]
    beta=[up(box(x)) for x in intrinsic["beta"]]
    curvature=[up(box(x)) for x in intrinsic["K"]]
    eta=[up(box(x)) for x in row["full_actual_eta_derivatives"]]
    mean=[up(box(x)) for x in row["full_actual_mean_derivatives"]]
    rb=rootrow["bounds"]
    emin=lo(box(rb["eta_lower"]));emax=up(box(rb["eta_upper"]))
    if not emin>0:raise ValueError("the same true mean lost its positive eta gap")
    D=[up(box(x)) for x in st["D"]];Dr=[up(box(x)) for x in st["Dr"]]
    if len(D)!=6 or len(Dr)!=3:raise ValueError("the actual old drift row lost its full saved orders")
    nonmean=[min(V[p][0],V[p][1]/4).upper() for p in range(3)]
    Sn=[]
    for p in range(3):
        u=total(math.comb(p,i)*U[i][0]*U[p-i][0] for i in range(p+1))
        v=arb(0)
        for k in range(p+1):
            m=p-k
            v+=math.comb(p,k)*curvature[k]*total(math.comb(m,i)*
                (mean[i]*nonmean[m-i]+nonmean[i]*mean[m-i]+nonmean[i]*nonmean[m-i])
                for i in range(m+1))
        Sn.append((u+v).upper())
    drr=(beta[2]*Sn[0]+2*beta[1]*Sn[1]+beta[0]*Sn[2]).upper()
    Drr=[(drr/4).upper(),drr]
    b,b1,b2=beta[:3];k,k1,k2=curvature[:3]
    u,ur,urr=U[0][0],U[1][0],U[2][0]
    v,vr,vrr=V[0][0],V[1][0],V[2][0]
    uphi,urphi=U[0][1],U[1][1];vphi,vrphi=V[0][1],V[1][1]
    ell=2*b*u*v
    ellp=2*b*(uphi*v+u*vphi)
    ellr=2*b1*u*v+2*b*(ur*v+u*vr)
    ellrr=2*b2*u*v+4*b1*(ur*v+u*vr)+2*b*(urr*v+2*ur*vr+u*vrr)
    ellrp=2*b1*(uphi*v+u*vphi)+2*b*(urphi*v+ur*vphi+uphi*vr+u*vrphi)
    ep=2*b*(3*u*uphi+k*v*vphi)
    erp=2*b1*(3*u*uphi+k*v*vphi)+2*b*(3*(ur*uphi+u*urphi)
        +k1*v*vphi+k*(vr*vphi+v*vrphi))
    eta_log_r=eta[1]/emin
    eta_log_rr=eta[2]/emin+eta[1]*eta[1]/(emin*emin)
    H0=eta_log_r+D[1];H1=eta_log_rr+Dr[1]
    rq=up(box(st["rQ0"]))
    rqr=(ellrr+Dr[0]*ellp+D[0]*ellrp+eta[1]*ep+emax*erp
        +2*((b1*emax+b*eta[1])*uphi*u+b*emax*(urphi*u+uphi*ur))
        +ellr*H0+ell*H1).upper()
    vartheta_r=(rqr/emin+rq*eta[1]/(emin*emin)
        +2*((b1*k+b*k1)*v*vphi+b*k*(vr*vphi+v*vrphi))).upper()
    sm=up(box(rs["Smean"]))
    smr=(2*u*ur+k1*v*v+2*k*v*vr).upper()
    smrr=(2*(ur*ur+u*urr)+k2*v*v+4*k1*v*vr+2*k*(vr*vr+v*vrr)).upper()
    T0r=(eta_log_rr+4*(b1*sm+b*smr)+5*Dr[1]).upper()
    tq=H0+b*(1+3*u*u+k*v*v)
    tqr=H1+b1*(1+3*u*u+k*v*v)+b*(6*u*ur+k1*v*v+2*k*v*vr)
    P0=1+u*u+3*k*v*v
    P1=2*u*ur+3*k1*v*v+6*k*v*vr
    P2=2*(ur*ur+u*urr)+3*k2*v*v+12*k1*v*vr+6*k*(vr*vr+v*vrr)
    bp=2*b*(u*uphi+3*k*v*vphi)
    brp=2*b1*(u*uphi+3*k*v*vphi)+2*b*(ur*uphi+u*urphi
        +3*k1*v*vphi+3*k*(vr*vphi+v*vrphi))
    bloc=b*P0;br=b1*P0+b*P1;brr=b2*P0+2*b1*P1+b*P2
    ac=ell*ell+4*b*emax*v*uphi
    acr=2*ell*ellr+4*((b1*emax+b*eta[1])*v*uphi+b*emax*(vr*uphi+v*urphi))
    V0r=(tqr*bloc+tq*br+brr+Dr[0]*bp+D[0]*brp+k1*ac+k*acr).upper()
    out=dict(U=U,V=V,beta=beta,K=curvature,eta=eta,mean=mean,
        eta_lower=emin,eta_upper=emax,D=D,Dr=Dr,Drr=Drr,
        T0=up(box(st["T0"])),T0r=T0r,V0=up(box(st["V0"])),V0r=V0r,
        vartheta=up(box(st["vartheta"])),vartheta_r=vartheta_r,
        rQ=rq,rQ_r=rqr,full_S_mean=sm,full_S_mean_r=smr,full_S_mean_rr=smrr,
        log_EG_r=up(box(st["log_EG_r"])),
        log_EG_rr=up(box(st["log_EG_rr"])),
        log_EG_rrr=(2*(b2*sm+2*b1*smr+b*smrr)).upper(),
        original_C_J_scalar=up(box(rootrow["strips"]["1/64"]["J_Hminus5over3_to_Hminus2over3"])))
    if not nonnegative(out):raise ValueError("a complete new coefficient derivative is nonfinite")
    return out

def leading_third_row(case,refined,scalar,c,rhomin,rhomax):
    """New pointwise strict third jets; no completed lower tensor is recomputed."""
    v={k:box(x) for k,x in case["bounds"].items()}
    af=refined["actual_forcing"];mixed=af["A_mixed_derivative_bounds"]
    if af["leading_strip"]!="3/64" or af["output_strip"]!="1/64":
        raise ValueError("the complete original amplitude strips changed")
    R=ex(rhomax);h=ex(rhomin);loss=ex(SIGMA_OLD-SIGMA_JET)
    Am=lo(v["A_lower"]);Ap=up(v["A_upper"])
    km=lo(v["k_lower"]);kp=up(v["k_upper"])
    ap=up(v["a_upper"]);G=up(v["leading_G"]);Gi=up(v["leading_G_inverse"])
    gap=lo(v["fold_noncharacteristic_gap"]);mu=lo(v["principal_mu_abs_lower"])
    if not (h>0 and R>=h and Am>0 and km>0 and gap>0 and mu>0 and loss>0):
        raise ValueError("a strict complete root denominator was lost")
    D,Dr,Drr=c["D"],c["Dr"],c["Drr"]
    C={int(k):up(box(x)) for k,x in af["flow_variational_C"].items()}
    ca={int(k):up(box(x)) for k,x in af["A_angular_constants"].items()}
    A={(0,0):Ap}
    for q in range(1,5):A[0,q]=(R*ca[q]).upper()
    for p,q in ((1,0),(1,1),(1,2),(2,0),(2,1)):
        A[p,q]=up(box(mixed[str((p,q))]))
    A[1,3]=(A[1,2]/loss).upper()
    A[2,2]=(A[2,1]/loss).upper()
    a1=up(box(af["radial_a_derivatives"]["first"]))
    a2=up(box(af["radial_a_derivatives"]["second"]))
    k1=up(box(af["divided_curvature_derivatives"]["first"]))
    k2=up(box(af["divided_curvature_derivatives"]["second"]))
    k3=((c["K"][3]+3*k2)/h).upper()
    X={1:C[1],**{q:(R*C[q]).upper() for q in (2,3,4)}}
    xr={}
    for n in (1,2,3):
        xr[n]=(total(math.comb(n,l)*D[l]*X[n-l+1] for l in range(n+1))
            +ex(Q(2,3))*ap*R*R*A[0,n+1]).upper()
    xrr={}
    for n in (1,2):
        xrr[n]=(total(math.comb(n,l)*(Dr[l]*X[n-l+1]+D[l]*xr[n-l+1])
            for l in range(n+1))+ex(Q(2,3))*
            ((a1*R*R+2*ap*R)*A[0,n+1]+ap*R*R*A[1,n+1])).upper()
    A[3,0]=((7*A[2,0]+4*(Dr[0]*A[0,1]+D[0]*A[1,1])
        +2*R*(Drr[0]*A[0,1]+2*Dr[0]*A[1,1]+D[0]*A[2,1])
        +3*(a2*X[1]+2*a1*xr[1]+ap*xrr[1]))/(2*h)).upper()
    # Differentiate D.9 in the actual angle before taking norms. Radial
    # constants therefore do not become fictitious angular derivatives.
    A[3,1]=((7*A[2,1]+4*(Dr[1]*A[0,1]+Dr[0]*A[0,2]
          +D[1]*A[1,1]+D[0]*A[1,2])
        +2*R*(Drr[1]*A[0,1]+Drr[0]*A[0,2]+2*Dr[1]*A[1,1]
          +2*Dr[0]*A[1,2]+D[1]*A[2,1]+D[0]*A[2,2])
        +3*(a2*X[2]+2*a1*xr[2]+ap*xrr[2]))/(2*h)).upper()
    x3=(Drr[1]*X[1]+Drr[0]*X[2]+2*Dr[1]*xr[1]+2*Dr[0]*xr[2]
        +D[1]*xrr[1]+D[0]*xrr[2]+ex(Q(2,3))*
        ((a2*R*R+4*a1*R+2*ap)*A[0,2]
         +(2*a1*R*R+4*ap*R)*A[1,2]+ap*R*R*A[2,2])).upper()
    xjet={(0,q):X[q+1] for q in range(4)}
    xjet.update({(1,q):xr[q+1] for q in range(3)})
    xjet.update({(2,q):xrr[q+1] for q in range(2)})
    xjet[3,0]=x3
    Aj=normalized_power(A,Q(1,6),Am,K3)
    kj={(0,0):kp,(1,0):k1,(2,0):k2,(3,0):k3}
    kj=normalized_power(kj,Q(-1,4),km,K3)
    L1,L2,L3=c["log_EG_r"],c["log_EG_rr"],c["log_EG_rrr"]
    ej={(0,0):arb(1),(1,0):L1,(2,0):(L2+L1*L1).upper(),
        (3,0):(L3+3*L1*L2+L1*L1*L1).upper()}
    gj=jet_scale(jet_product(jet_product(Aj,kj,K3),ej,K3),G)
    # Scalar E_G is independent of angle. Its full mean is in L1,L2,L3.
    pj=jet_scale(normalized_power(A,Q(2,3),Am,K4),power(Ap,Q(2,3)).upper())
    tj={(p,q):(R*pj[p,q]+(p*pj[p-1,q] if p else 0)).upper() for p,q in K4}
    yj={(p,q):tj[p,q+1] for p,q in K3}
    tj3={k:tj[k] for k in K3}
    x2=jet_product(xjet,xjet,K3)
    ty2=jet_product(tj3,jet_product(yj,yj,K3),K3)
    aa=jet_product(gj,jet_add(x2,ty2,K3),K3)
    bb=jet_scale(jet_product(gj,jet_product(xjet,yj,K3),K3),2)
    # These original entries are complete wider-strip results, copied by
    # value and used as independent bounds, never recalculated.
    original_a=af["leading_a0_derivative_bounds"]
    original_b=af["leading_b0_derivative_bounds"]
    for key in K3:
        label=str(key)
        if label in original_a:aa[key]=min(aa[key],up(box(original_a[label]))).upper()
        if label in original_b:bb[key]=min(bb[key],up(box(original_b[label]))).upper()
    q=(ap*power(Am,Q(-1,3))).upper()
    qr=(a1*power(Am,Q(-1,3))+ap*power(Am,Q(-4,3))*A[1,0]/3).upper()
    qp=(ap*power(Am,Q(-4,3))*A[0,1]/3).upper()
    tmin=(h*power(Am,Q(2,3))).lower()
    if not tmin>0:raise ValueError("the actual strict T gap was lost")
    mu_r=(2*q*qr*(xjet[0,0]*xjet[0,0]+tj[0,0]*yj[0,0]*yj[0,0])
        +q*q*(2*xjet[0,0]*xjet[1,0]+tj[1,0]*yj[0,0]*yj[0,0]
          +2*tj[0,0]*yj[0,0]*yj[1,0])).upper()
    # mu=Q^2 B_plus. The minus belongs only to the exact leading a0.
    state=dict(A=A,x=xjet,T=tj3,y=yj,G=gj,a0=aa,b0=bb,
        Q=q,Qrho=qr,Qphi=qp,Tlower=tmin,mu_lower=mu,mu_rho=mu_r,
        G_inverse=Gi,fold_gap=gap,k_third=k3,rho_lower=h,rho_upper=R)
    if not nonnegative({str(k):v for k,v in state.items()}):
        raise ValueError("a strict third leading or fold jet is invalid")
    return state

def numerator_and_first_forcing(c,l,af):
    """Complete local numerator and its first old-radial derivative."""
    aa,bb=l["a0"],l["b0"];D,Dr=c["D"],c["Dr"]
    v0=c["vartheta"]*l["Q"]
    v1=c["vartheta_r"]*l["Q"]+c["vartheta"]*l["Qrho"]
    c2=D[0]*D[0]+c["eta_upper"]*c["eta_upper"]*c["K"][0]
    c2r=2*D[0]*Dr[0]+2*c["eta_upper"]*c["eta"][1]*c["K"][0]+c["eta_upper"]*c["eta_upper"]*c["K"][1]
    c1=Dr[0]+D[0]*D[1]+c["T0"]*D[0]
    c1r=c["Drr"][0]+Dr[0]*D[1]+D[0]*Dr[1]+c["T0r"]*D[0]+c["T0"]*Dr[0]
    values=[];derivatives=[]
    for i,w in enumerate((aa,bb)):
        other=bb if i==0 else aa
        cross=v0*(l["T"][0,0] if i==0 else 1)*other[0,0]
        crossr=(v1*(l["T"][0,0] if i==0 else 1)*other[0,0]
            +v0*((l["T"][1,0]*other[0,0] if i==0 else 0)
             +(l["T"][0,0] if i==0 else 1)*other[1,0]))
        n=(w[2,0]+2*D[0]*w[1,1]+c2*w[0,2]+c1*w[0,1]
            +c["T0"]*w[1,0]+c["V0"]*w[0,0]+cross).upper()
        nr=(w[3,0]+2*Dr[0]*w[1,1]+2*D[0]*w[2,1]
            +c2r*w[0,2]+c2*w[1,2]+c1r*w[0,1]+c1*w[1,1]
            +c["T0r"]*w[1,0]+c["T0"]*w[2,0]
            +c["V0r"]*w[0,0]+c["V0"]*w[1,0]+crossr).upper()
        # The original pair bound is an independent bound for each component.
        f=min((n/l["mu_lower"]).upper(),up(box(af["complete_actual_L0_v0_pair_sup"]))).upper()
        fr=((nr+l["mu_rho"]*f)/l["mu_lower"]).upper()
        values.append(f);derivatives.append(fr)
    return values,derivatives

def first_correction_row(c,l,af):
    """E.9--E.18, preserving ordered matrices and all original components."""
    aa,bb=l["a0"],l["b0"];T=l["T"];x=l["x"];y=l["y"]
    q,qr,qp=l["Q"],l["Qrho"],l["Qphi"]
    tmin=l["Tlower"];D,Dr=c["D"],c["Dr"]
    W=[up(box(af["actual_first_a_amplitude_sup"])),up(box(af["actual_first_b_amplitude_sup"]))]
    Btb=jet_product(T,bb,K3)
    def leading_matrix(key):return [[aa[key],Btb[key]],[bb[key],aa[key]]]
    B=leading_matrix((0,0));Br=leading_matrix((1,0));Brr=leading_matrix((2,0))
    Bp=leading_matrix((0,1));Brp=leading_matrix((1,1))
    inv=ms([[aa[0,0],Btb[0,0]],[bb[0,0],aa[0,0]]],
        l["G_inverse"]*l["G_inverse"]/(l["fold_gap"]*l["fold_gap"]))
    Z0=mv(inv,W)
    dz=ex(SIGMA_W-SIGMA_TRANSPORT)
    Z1=vs(Z0,1/dz);Z2=vs(Z0,2/(dz*dz))
    F,Fr=numerator_and_first_forcing(c,l,af)
    g=mv(inv,F)
    gr=va(mv(inv,Fr),mv(mm(mm(inv,Br),inv),F))
    f=[g[1],g[0]];fr=[gr[1],gr[0]]
    fp=vs(f,1/ex(SIGMA_JET-SIGMA_TRANSPORT))
    C=[[D[0],q*T[0,0]],[q,D[0]]]
    Cr=[[Dr[0],qr*T[0,0]+q*T[1,0]],[qr,Dr[0]]]
    Cp=[[D[1],qp*T[0,0]+q*T[0,1]],[qp,D[1]]]
    M=ms([[arb(0),q*y[0,0]],[arb(0),q*x[0,0]/tmin]],arb(1)/2)
    N=ms([[q*x[0,0],q*y[0,0]],[q*y[0,0],q*x[0,0]/tmin]],arb(1)/2)
    def derivatives(qv,xv,yv,tv):
        L=qv*y[0,0]+q*yv
        Hh=(qv*x[0,0]+q*xv)/tmin+q*x[0,0]*tv/(tmin*tmin)
        return ms([[arb(0),L],[arb(0),Hh]],arb(1)/2),ms([[qv*x[0,0]+q*xv,L],[L,Hh]],arb(1)/2)
    Mr,Nr=derivatives(qr,x[1,0],y[1,0],T[1,0])
    Mp,Np=derivatives(qp,x[0,1],y[0,1],T[0,1])
    Zr=va(mv(C,Z1),mv(M,Z0),mv(N,f))
    Zrp=va(mv(Cp,Z1),mv(C,Z2),mv(Mp,Z0),mv(M,Z1),mv(Np,f),mv(N,fp))
    Zrr=va(mv(Cr,Z1),mv(C,Zrp),mv(Mr,Z0),mv(M,Zr),mv(Nr,f),mv(N,fr))
    Wr=va(mv(Br,Z0),mv(B,Zr))
    Wrp=va(mv(Brp,Z0),mv(Br,Z1),mv(Bp,Zr),mv(B,Zrp))
    Wrr=va(mv(Brr,Z0),vs(mv(Br,Zr),2),mv(B,Zrr))
    Wphi=[W,vs(W,1/dz),vs(W,2/(dz*dz))]
    raw=[];parts=[]
    for i in range(2):
        z=dict(radial_second=Wrr[i],radial_angular=2*D[0]*Wrp[i],
            angular_second=(D[0]*D[0]+c["eta_upper"]*c["eta_upper"]*c["K"][0])*Wphi[2][i],
            drift_derivative=(Dr[0]+D[0]*D[1])*Wphi[1][i],
            first_transport=c["T0"]*(Wr[i]+D[0]*Wphi[1][i]),
            scalar_potential=c["V0"]*W[i],
            exact_QK_cross=c["vartheta"]*q*(T[0,0]*W[1] if i==0 else W[0]))
        z={k:up(v) for k,v in z.items()};parts.append(z);raw.append(total(z.values()))
    return dict(W=W,Wr=Wr,Wrphi=Wrp,Wrr=Wrr,
        original_degree_zero_forcing=F,new_degree_zero_forcing_rho=Fr,
        # Both normalized forcing vectors are ordered (fa,fb), as in E.7.
        # Their values hold on SIGMA_JET; angular Cauchy bounds use SIGMA_TRANSPORT.
        normalized_degree_zero_forcing_f=f,normalized_degree_zero_forcing_f_rho=fr,
        normalized_degree_zero_forcing_f_phi=fp,
        normalized_degree_zero_forcing_f_rho_phi=vs(fr,1/ex(SIGMA_JET-SIGMA_TRANSPORT)),
        normalized_first_correction=Z0,normalized_first_correction_rho=Zr,
        normalized_first_correction_rhorho=Zrr,
        unnormalized_local_first_correction_numerator=raw,
        normalized_local_L0_first_correction=vs(raw,1/l["mu_lower"]),
        unnormalized_local_numerator_parts=parts,
        exact_ordered_C=C,exact_ordered_M=M,exact_ordered_N=N)

def geometric_sums(delta):
    if not delta>0:raise ValueError("a true angular loss is not positive")
    z=(-4*delta).exp();den=1-z
    if not den>0:raise ValueError("the complete Fourier geometric denominator is not positive")
    return [(1+z)/den,8*z/(den*den),32*z*(1+z)/(den*den*den),
        128*z*(1+4*z+z*z)/ipow(den,4)]

def output_derivative_tables(actual):
    """Complete sup/Wiener first-correction tables on the old strip 1/512."""
    dv=ex(SIGMA_W-SIGMA_OUTPUT);dr=ex(SIGMA_TRANSPORT-SIGMA_OUTPUT)
    lv,lr=geometric_sums(dv),geometric_sums(dr)
    result={}
    for component,name in enumerate(("a1","b1")):
        sup={};wiener={}
        for q in range(4):
            key="0,"+str(q)
            sup[key]=(actual["W"][component]*math.factorial(q)/ipow(dv,q)).upper()
            wiener[key]=(actual["W"][component]*lv[q]).upper()
        for q in range(3):
            key="1,"+str(q)
            s=(actual["Wr"][component]*math.factorial(q)/ipow(dr,q)).upper()
            w=(actual["Wr"][component]*lr[q]).upper()
            if q:
                s=min(s,(actual["Wrphi"][component]*math.factorial(q-1)/ipow(dr,q-1)).upper()).upper()
                w=min(w,(actual["Wrphi"][component]*lr[q-1]).upper()).upper()
            sup[key]=s;wiener[key]=w
        sup["2,0"]=actual["Wrr"][component]
        wiener["2,0"]=(actual["Wrr"][component]*lr[0]).upper()
        result[name]=dict(strip_sup=sup,Wiener=wiener)
    return result

def complete_fourier_factor(tau):
    """All input j>=97, all output modes including zero, and a true lag tail."""
    if not tau>0:raise ValueError("the actual inverse-phase strip is not positive")
    q=(-4*tau).exp();J=CUTOFF;L=J
    while not (q*power(ex(Q(L+1,L)),Q(4,3))).upper()<1:
        L+=1
        if L>100000:raise ValueError("the genuine complete exponential tail did not contract")
    ratio=(q*power(ex(Q(L+1,L)),Q(4,3))).upper()
    def lam(n):return ex(1+16*n*n).sqrt()
    center=power(lam(J),Q(-1,3))
    small=total(ipow(q,l)*power(lam(J),Q(4,3))/power(lam(J-l),Q(5,3)) for l in range(1,J))
    middle=total(ipow(q,l)*power(lam(l),Q(4,3)) for l in range(J,L))
    tail=(ipow(q,L)*power(lam(L),Q(4,3))/(1-ratio)).upper()
    bound=(center+2*small+2*middle+2*tail).upper()
    return bound,dict(inverse_phase_strip=rec(tau),tail_first_lag=L,
        exact_input_cutoff=J,complete_finite_small_lags=rec(2*small),
        complete_finite_large_lags=rec(2*middle),complete_infinite_lag_tail=rec(2*tail),
        geometric_tail_ratio=rec(ratio),complete_factor=rec(bound),
        mean_output_and_both_lag_signs_retained=True)

def radial_weight(left,right,roots,side):
    rl,ru=roots
    if side=="negative":
        if not left<right<=rl-H:raise ValueError("the negative strict interval crossed the complete inner window")
        return (2*(ex(rl-left).sqrt()-ex(rl-right).sqrt())).upper()
    if not ru+H<=left<right:raise ValueError("the positive strict interval crossed the complete inner window")
    return (2*(ex(right-ru).sqrt()-ex(left-ru).sqrt())).upper()

def local_source(raw,c,amplitude,profiles,fourier,side):
    """Actual J P S(Nraw), not S(mu^-1 Nraw) and not a projected output."""
    def profile(name):return total(x*y for x,y in zip(profiles[name],raw))
    central=profile("central")
    core=((central*central+4*ipow(profile("negative"),2)).sqrt().upper()
        if side=="negative" else max(central,profile("positive")).upper())
    A=(amplitude["composition"]*fourier*core).upper()
    return A,(c["original_C_J_scalar"]*A).upper()

def completed_case_summary(out):
    """Restore the exact saved summary if interrupted after the complete case."""
    return dict(exact_radius=out["exact_radius"],exact_cover=out["exact_cover"],
        complete=True,complete_exterior_rows=out["expected_exterior_rows"],source_summary=out["summary"],
        complete_Fourier_factor=out["new_complete_Fourier_factor"],
        Fourier_tail_first_lag=out["new_complete_Fourier_evidence"]["tail_first_lag"],
        negative_local_component_Hminus4over3_to_primitive_L2=out["negative_local_component_Hminus4over3_to_primitive_L2"],
        positive_collar_local_source_L2=out["positive_collar_local_source_L2"],
        positive_body_local_source_L2=out["positive_body_local_source_L2"],
        new_radial_weight_rows=out["new_radial_weight_rows"],
        reused_original_radial_weight_rows=out["reused_original_radial_weight_rows"])

def receipts_from_index(path,doc,out):
    """Copy accepted natural stage files without modifying their original bytes."""
    import shutil
    entries=[]
    if doc.get("coefficient_stage"):entries.append(doc["coefficient_stage"])
    entries.extend(doc.get("case_stages",[]))
    for entry in entries:
        source=path.parent/entry["file"];target=out.parent/entry["file"]
        if not source.is_file() or sha(source)!=entry["sha256"] or source.stat().st_size!=entry["bytes"]:
            raise ValueError("an immutable completed exterior prefix file changed")
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():raise FileExistsError("a restored exterior prefix would replace an existing result")
        shutil.copyfile(source,target)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","prepared","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics runs only in the public repository Actions")
    import numpy as np,scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise RuntimeError("the exact original directed runtime changed")
    if a.out.exists():raise FileExistsError("preserve every completed or failed exterior result")
    ctx.prec=320;start=time.monotonic()
    doc=dict(kind="actual_complete_strict_exterior_first_Airy_derivatives_and_local_sources",
        complete=False,proved=False,failure=None,gates=[],source_sha256=sha(__file__),
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        runtime=runtime,root_native_sha256=ROOT_SHA,first_forcing_native_sha256=FORCE_SHA,
        first_seam_native_sha256=SEAM_SHA,complete_cancelled_fold_native_sha256=FOLD_SHA,
        complete_old_rho_Taylor_native_sha256=TAYLOR_SHA,
        background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        actual_intrinsic_parameter="eta_0",exact_real_delta_radius=str(DELTA),
        old_target_FFT_intrinsic_cubic_point_and_ray_stages_recomputed=0,
        old_complete_forcing_coefficient_rows_recomputed=0,old_complete_amplitude_cases_recomputed=0,
        old_complete_Taylor_algebra_stages_recomputed=0,old_complete_physical_seam_operators_recomputed=0,
        new_coefficient_derivative_rows=0,reused_coefficient_derivative_rows=0,
        new_strict_exterior_rows=0,reused_strict_exterior_rows=0,
        exact_physical_inner_radius=str(H),exact_original_leading_strip=str(SIGMA_OLD),
        exact_new_leading_third_strip=str(SIGMA_JET),
        exact_local_numerator_strip=str(SIGMA_TRANSPORT),exact_amplitude_output_strip=str(SIGMA_OUTPUT),
        true_local_source="J P S(Nraw), Nraw=mu L0 w1",
        source_window="H^-4/3 -> ordinary radial L2 H^-2/3, first original row only",
        old_circle_nonlocal_and_independent_even_mean_budget_paid=False,
        all_original_physical_seams_and_mean_equations_retained=True,
        artificial_interface_source_introduced=False,
        complete_strong_return_norm_or_cutoff97_inverse_claimed=False,
        positive_given_head_source_conversion_is_full_high_inverse=False,
        coefficient_stage=None,case_stages=[],cases=[])
    def gate(name,truth):
        good=bool(truth);doc["gates"].append(dict(name=name,passed=good))
        if not good:raise ValueError("actual strict exterior gate failed: "+name)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(a.out,doc)
    def stage_save(path,payload):
        save(path,payload)
        return dict(file=str(path.relative_to(a.out.parent)),sha256=sha(path),bytes=path.stat().st_size)
    try:
        manifest=read(a.manifest);doc["input_manifest_sha256"]=sha(a.manifest)
        gate("the exact manifest belongs to this public strict exterior consumer",
            manifest["public_repository"]==PUBLIC and manifest["mathematical_parameters"]["exact_inner_radius"]==str(H))
        for entry in manifest["files"]:
            path=a.repo_root/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a pinned complete scientific input changed: "+entry["path"])
        paths={key:a.repo_root/value for key,value in manifest["input_paths"].items()}
        external={x["name"]:a.prepared/x["prepared_path"] for x in manifest["external_completed_natives"]}
        for entry in manifest["external_completed_natives"]:
            path=external[entry["name"]]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a complete original external native changed its exact bytes")
        root,force=read(external["root"]),read(external["forcing"])
        seam,fold,taylor=[read(paths[k]) for k in ("seam_native","fold_native","Taylor_native")]
        forceproc,foldproc,tproc=[read(paths[k]) for k in ("forcing_process","fold_process","Taylor_process")]
        gate("all five successful complete originals and their byte identities are retained",
            sha(external["root"])==ROOT_SHA and sha(external["forcing"])==FORCE_SHA
            and sha(paths["seam_native"])==SEAM_SHA and sha(paths["fold_native"])==FOLD_SHA
            and sha(paths["Taylor_native"])==TAYLOR_SHA
            and all(d["complete"] and d["proved"] and d["failure"] is None
                and all(x["passed"] for x in d["gates"]) for d in (root,force,seam,fold,taylor)))
        gate("actual zero-return process receipts bind the complete forcing fold and Taylor inputs",
            all(p["complete"] and p["actual_returncode"]==0 and p["mathematical_complete"]
                and p["mathematical_failure"] is None and all(x["passed"] for x in p["mathematical_gates"])
                for p in (forceproc,foldproc,tproc))
            and forceproc["native_sha256"]==FORCE_SHA and foldproc["native_sha256"]==FOLD_SHA
            and tproc["native_sha256"]==TAYLOR_SHA
            and str(forceproc["run_id"])=="43624260519" and str(foldproc["run_id"])=="43642808159"
            and str(tproc["run_id"])=="43653825736")
        gate("the complete original fixed family and all natural coefficient and seam rows agree",
            root["background_definition_sha256"]==BASE and root["explicit_direction_definition_sha256"]==ZDEF
            and force["root_native_sha256"]==ROOT_SHA and seam["root_native_sha256"]==ROOT_SHA
            and seam["first_forcing_native_sha256"]==FORCE_SHA
            and fold["root_native_sha256"]==ROOT_SHA and fold["first_seam_native_sha256"]==SEAM_SHA
            and taylor["background_definition_sha256"]==BASE and taylor["explicit_direction_definition_sha256"]==ZDEF
            and taylor["actual_intrinsic_parameter"]=="eta_0" and taylor["exact_complex_delta_radius"]==str(DELTA)
            and len(root["rows"])==1300 and len(force["rows"])==1328 and len(seam["seams"])==1079
            and len(root["cases"])==len(seam["refined_forcing_radius_cases"])==len(fold["cases"])==6)
        roots=list(map(Q,root["exact_root_interval"]));rl,ru=roots
        gate("the true uncertain root inner physical endpoints and complete 75-stage Taylor are unchanged",
            root["exact_root_interval"]==force["exact_root_interval"]==fold["exact_root_interval"]==taylor["exact_root_interval"]
            and taylor["old_product_domain"]["exact_physical_interval"]==[str(rl-H),str(ru+H)]
            and Q(taylor["old_product_domain"]["exact_physical_rho_cover_radius"])==H+ru-rl
            and len(taylor["stages"])==75 and tproc["all_complete_Fourier_arrays_and_all_natural_prefix_files_verified"]
            and taylor["original_target_FFT_or_high_root_stages_recomputed"]==0)
        bodycut=Q(fold["fixed_positive_body_cut"])
        gate("all strict positive exterior cells are beyond the original fixed positive body cut",
            bodycut==Q(1192029371497,5000000000000) and bodycut<=ru+H)
        doc.update(exact_root_interval=list(map(str,roots)),exact_cover=root["exact_cover"],
            exact_physical_inner_interval=[str(rl-H),str(ru+H)],fixed_positive_body_cut=str(bodycut),
            original_complete_forcing_rows_reused=1328,original_complete_root_rows_reused=1300,
            original_complete_physical_seams_reused=1079,original_complete_Taylor_stages_reused=75,
            original_complete_saved_amplitude_cases_reused=6)
        if a.resume:
            previous=read(a.resume)
            gate("every restored new prefix has the identical source manifest runtime and original inputs",
                previous["source_sha256"]==sha(__file__) and previous["input_manifest_sha256"]==sha(a.manifest)
                and previous["runtime"]==runtime
                and all(previous[k]==doc[k] for k in ("root_native_sha256","first_forcing_native_sha256",
                    "first_seam_native_sha256","complete_cancelled_fold_native_sha256","complete_old_rho_Taylor_native_sha256",
                    "exact_root_interval","exact_physical_inner_interval")))
            receipts_from_index(a.resume,previous,a.out)
            doc["coefficient_stage"]=previous.get("coefficient_stage")
            doc["case_stages"]=list(previous.get("case_stages",[]))
            doc["cases"]=list(previous.get("cases",[]))
        checkpoint()
        cp=a.out.parent/"coefficients"/"complete-new-first-coefficient-derivatives.json.gz"
        if doc["coefficient_stage"]:
            coefficients=read(cp)
            if coefficients["source_sha256"]!=sha(__file__) or coefficients["input_manifest_sha256"]!=sha(a.manifest):
                raise ValueError("a restored new coefficient table changed identity")
        else:
            coefficients=dict(kind="complete_new_strict_first_coefficient_derivatives",
                source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),complete=False,rows=[])
        reused=len(coefficients["rows"]);doc["reused_coefficient_derivative_rows"]=reused
        if reused>1328:raise ValueError("a restored new coefficient prefix exceeds the actual cover")
        for i,row in enumerate(force["rows"]):
            oi=row["original_root_row"];rr=root["rows"][oi]
            a0,b0=map(Q,row["interval"]);r0,r1=map(Q,rr["interval"])
            if not r0<=a0<b0<=r1 or row["original_piece"]!=rr["candidate_and_response_piece"]:
                raise ValueError("a genuine original forcing/root piece changed")
            identity=dict(common_row=i,interval=row["interval"],original_root_row=oi,original_piece=row["original_piece"])
            if i<reused:
                if any(coefficients["rows"][i][k]!=v for k,v in identity.items()):
                    raise ValueError("an accepted coefficient prefix changed its original row")
                continue
            doc["last_attempted_coefficient_row"]=identity
            c=coefficient_row(row,rr)
            coefficients["rows"].append(dict(**identity,bounds=encode(c)))
            doc["new_coefficient_derivative_rows"]+=1
            doc.pop("last_attempted_coefficient_row",None)
            doc["coefficient_stage"]=stage_save(cp,coefficients);checkpoint()
        coefficients["complete"]=True
        doc["coefficient_stage"]=stage_save(cp,coefficients);checkpoint()
        gate("every complete coefficient row is reused and all new first derivatives are finite",
            len(coefficients["rows"])==1328 and coefficients["complete"])

        for ci,(case,refined,accepted) in enumerate(zip(root["cases"],seam["refined_forcing_radius_cases"],fold["cases"])):
            radius=Q(case["exact_radius"]);cl,cr=map(Q,case["exact_radial_cover"])
            if (radius!=RADII[ci] or not case["passed"] or not refined["passed"]
                or not all(g["passed"] for g in refined["gates"]) or not accepted["complete"]
                or case["exact_radius"]!=refined["exact_radius"] or case["exact_radius"]!=accepted["exact_radius"]
                or case["exact_radial_cover"]!=refined["exact_cover"] or case["exact_radial_cover"]!=accepted["exact_cover"]):
                raise ValueError("a complete original radius or amplitude case changed")
            af=refined["actual_forcing"]
            path=a.out.parent/"cases"/("radius-"+str(radius.numerator)+"-"+str(radius.denominator)+".json.gz")
            if ci<len(doc["case_stages"]):
                out=read(path)
                if (out["source_sha256"]!=sha(__file__) or out["input_manifest_sha256"]!=sha(a.manifest)
                    or out["exact_radius"]!=str(radius) or out["exact_cover"]!=case["exact_radial_cover"]):
                    raise ValueError("a restored natural exterior case changed identity")
                doc["reused_strict_exterior_rows"]+=len(out["rows"])
            else:
                out=dict(kind="complete_strict_exterior_first_Airy_radius",
                    source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),
                    complete=False,exact_radius=str(radius),exact_cover=case["exact_radial_cover"],
                    exact_inner_interval=[str(rl-H),str(ru+H)],rows=[],
                    original_complete_analytic_amplitude_numeric=accepted["original_complete_analytic_amplitude_numeric"],
                    original_radial_reference_profiles_numeric=accepted["original_radial_reference_profiles_numeric"],
                    original_complete_scalar_jet_numeric=accepted["new_scalar_jet_numeric"],
                    complete_new_Fourier_factor=False,new_radial_weight_rows=0,reused_original_radial_weight_rows=0)
                doc["case_stages"].append(stage_save(path,out));checkpoint()
            if (out["original_complete_analytic_amplitude_numeric"]!=accepted["original_complete_analytic_amplitude_numeric"]
                or out["original_radial_reference_profiles_numeric"]!=accepted["original_radial_reference_profiles_numeric"]
                or out["original_complete_scalar_jet_numeric"]!=accepted["new_scalar_jet_numeric"]):
                raise ValueError("a complete saved original tensor was changed")
            if out["complete"]:
                recovered=completed_case_summary(out)
                if ci<len(doc["cases"]):
                    if doc["cases"][ci]!=recovered:
                        raise ValueError("a saved complete case summary differs from its exact natural stage")
                elif ci==len(doc["cases"]):
                    doc["cases"].append(recovered)
                else:
                    raise ValueError("a completed exterior case summary prefix has a gap")
                checkpoint();continue
            amplitude=decode(out["original_complete_analytic_amplitude_numeric"])
            profiles=decode(out["original_radial_reference_profiles_numeric"])
            scalar=decode(out["original_complete_scalar_jet_numeric"])
            if out["complete_new_Fourier_factor"]:
                fourier=up(box(out["new_complete_Fourier_factor"]))
            else:
                E=up(box(af["flow_variational_C"]["1"]))
                tau=((2-E)*ex(SIGMA_TRANSPORT)).lower()
                fourier,fe=complete_fourier_factor(tau)
                out.update(complete_new_Fourier_factor=True,new_complete_Fourier_factor=rec(fourier),
                    new_complete_Fourier_evidence=fe,
                    original_phase_composition_copied_without_recalculation=accepted["original_complete_analytic_amplitude_numeric"]["composition"])
                doc["case_stages"][ci]=stage_save(path,out);checkpoint()
            layout=[]
            for saved in accepted["rows"]:
                index=saved["common_row"];original=force["rows"][index]
                if saved["interval"]!=original["interval"]:
                    raise ValueError("a complete original six-case row was not the same true forcing cell")
                left,right=map(Q,saved["interval"])
                for side,L,R in (("negative",left,min(right,rl-H)),("positive",max(left,ru+H),right)):
                    if L<R:
                        if not cl<=L<R<=cr:raise ValueError("an exterior interval left its actual radius")
                        layout.append((index,L,R,side,saved))
            for side,begin,end in (("negative",cl,rl-H),("positive",ru+H,cr)):
                cursor=begin
                for _,L,R,which,_ in layout:
                    if which!=side:continue
                    if L!=cursor:raise ValueError("the exact strict exterior cover has a gap")
                    cursor=R
                if cursor!=end:raise ValueError("a strict exterior endpoint is absent")
            prefix=len(out["rows"])
            if prefix>len(layout):raise ValueError("a restored strict prefix exceeds its true partition")
            for si,(index,L,R,side,saved) in enumerate(layout):
                original=force["rows"][index]
                identity=dict(serial=si,common_row=index,interval=[str(L),str(R)],side=side,
                    original_root_row=original["original_root_row"],original_piece=original["original_piece"])
                if si<prefix:
                    if any(out["rows"][si][k]!=v for k,v in identity.items()):
                        raise ValueError("an accepted exterior row changed its exact physical identity")
                    continue
                doc["last_attempted_exterior_row"]=dict(radius=str(radius),**identity);checkpoint()
                c=decode(coefficients["rows"][index]["bounds"])
                rmin,rmax=((rl-R,ru-L) if side=="negative" else (L-ru,R-rl))
                if not rmin>=H:raise ValueError("the genuine strict root distance was not paid")
                leading=leading_third_row(case,refined,scalar,c,rmin,rmax)
                actual=first_correction_row(c,leading,af)
                if not nonnegative(actual):raise ValueError("a complete new exterior amplitude result is not finite")
                tables=output_derivative_tables(actual)
                raw=actual["unnormalized_local_first_correction_numerator"]
                beforeJ,source=local_source(raw,c,amplitude,profiles,fourier,side)
                oldweight=(saved["interval"]==identity["interval"] and
                    not saved[side].get("exact_zero_radial_part"))
                if oldweight:
                    weight=up(box(saved[side]["radial_weight_integral"]))
                    weight_record=saved[side]["radial_weight_integral"]
                    out["reused_original_radial_weight_rows"]+=1
                else:
                    weight=radial_weight(L,R,roots,side);weight_record=rec(weight)
                    out["new_radial_weight_rows"]+=1
                if not weight>0:raise ValueError("an actual nonzero strict radial integral lost positivity")
                item=dict(**identity,exact_root_distance_interval=[str(rmin),str(rmax)],
                    original_complete_coefficient_row_reused=True,
                    new_third_jet_evidence=encode(dict(k_rhorhorho=leading["k_third"],
                        A_rhorhorho=leading["A"][3,0],A_rhorhorhophi=leading["A"][3,1],
                        Xphi_rhorhorho=leading["x"][3,0],Tphi_rhorhorho=leading["y"][3,0],
                        a0_rhorhorho=leading["a0"][3,0],b0_rhorhorho=leading["b0"][3,0])),
                    complete_degree_zero_forcing=encode(actual["original_degree_zero_forcing"]),
                    new_complete_degree_zero_forcing_rho=encode(actual["new_degree_zero_forcing_rho"]),
                    normalized_forcing_f=encode(actual["normalized_degree_zero_forcing_f"]),
                    normalized_forcing_f_rho=encode(actual["normalized_degree_zero_forcing_f_rho"]),
                    normalized_forcing_f_phi=encode(actual["normalized_degree_zero_forcing_f_phi"]),
                    normalized_forcing_f_rho_phi=encode(actual["normalized_degree_zero_forcing_f_rho_phi"]),
                    exact_normalized_forcing_value_phi_width=str(SIGMA_JET),
                    exact_normalized_forcing_derivative_phi_width=str(SIGMA_TRANSPORT),
                    first_amplitude_budgets=encode(tables),
                    exact_amplitude_output_phi_width=str(SIGMA_OUTPUT),
                    exact_local_numerator_phi_width=str(SIGMA_TRANSPORT),
                    complete_unnormalized_local_numerator=encode(raw),
                    complete_normalized_local_L0_w1=encode(actual["normalized_local_L0_first_correction"]),
                    complete_unnormalized_local_numerator_parts=encode(actual["unnormalized_local_numerator_parts"]),
                    actual_source_before_J_singular_envelope=rec(beforeJ),
                    original_C_J_scalar=rec(c["original_C_J_scalar"]),
                    actual_first_row_local_source_singular_envelope=rec(source),
                    radial_weight_integral=weight_record,original_radial_weight_reused=oldweight,
                    complete_first_row_local_squared_source_integral=rec((weight*source*source).upper()),
                    ordinary_amplitude_squared_integrals=encode([ex(R-L)*v*v for v in raw]),
                    full_old_circle_nonlocal_and_independent_even_mean_included=False)
                out["rows"].append(item);doc["new_strict_exterior_rows"]+=1
                doc.pop("last_attempted_exterior_row",None)
                # Every accepted new row is committed to its natural case
                # checkpoint before the next mathematical row is attempted.
                doc["case_stages"][ci]=stage_save(path,out);checkpoint()
                if si%128==0:
                    print(json.dumps(dict(radius=str(radius),complete_exterior_rows=len(out["rows"]),
                        expected_exterior_rows=len(layout),seconds=time.monotonic()-start)),flush=True)
            totals={}
            for side in ("negative","positive"):
                chosen=[x for x in out["rows"] if x["side"]==side]
                sq=total(up(box(x["complete_first_row_local_squared_source_integral"])) for x in chosen)
                amp=[total(up(box(x["ordinary_amplitude_squared_integrals"][i])) for x in chosen) for i in range(2)]
                maxima={}
                for name in ("a1","b1"):
                    maxima[name]={}
                    for norm in ("strip_sup","Wiener"):
                        keys=chosen[0]["first_amplitude_budgets"][name][norm]
                        maxima[name][norm]={key:max(up(box(x["first_amplitude_budgets"][name][norm][key])) for x in chosen).upper()
                            for key in keys}
                totals[side]=dict(complete_exterior_rows=len(chosen),
                    complete_first_row_local_L2_source=rec(sq.sqrt().upper()),
                    ordinary_unnormalized_amplitude_L2_bounds=encode([v.sqrt().upper() for v in amp]),
                    complete_w1_exterior_derivative_suprema=encode(maxima),
                    exact_enclosing_interval=[str(cl),str(rl-H)] if side=="negative" else [str(ru+H),str(cr)])
            gain=up(box(accepted["actual_negative_source_to_primitive_L2_gain"]))
            negative=up(box(totals["negative"]["complete_first_row_local_L2_source"]))
            out.update(complete=True,expected_exterior_rows=len(layout),summary=totals,
                actual_negative_source_to_primitive_L2_gain=accepted["actual_negative_source_to_primitive_L2_gain"],
                negative_local_component_Hminus4over3_to_primitive_L2=rec((gain*negative).upper()),
                positive_collar_local_source_L2=rec(arb(0)),
                positive_body_local_source_L2=totals["positive"]["complete_first_row_local_L2_source"],
                independent_mean_and_all_old_circle_nonlocal_terms_are_separate=True,
                original_physical_seam_operators_retained_without_recomputation=True,
                positive_given_head_or_full_high_inverse_claimed=False,
                zero_root_and_other_sources_for_this_linear_local_component=True,
                no_artificial_interface_source_or_renormalization=True)
            doc["case_stages"][ci]=stage_save(path,out)
            summary=completed_case_summary(out)
            if ci<len(doc["cases"]):doc["cases"][ci]=summary
            else:doc["cases"].append(summary)
            checkpoint()
        gate("all six strict radius cases preserve both complete source sides and true row covers",
            len(doc["cases"])==6 and all(x["complete"] for x in doc["cases"])
            and all(Q(x["exact_radius"])==r for x,r in zip(doc["cases"],RADII)))
        gate("all new natural complete stages fit unchanged original-file publication rules",
            all(e["bytes"]<5_000_000 for e in [doc["coefficient_stage"],*doc["case_stages"]]))
        gate("no successful old target coefficient amplitude Fourier or seam stage was recomputed",
            all(doc[k]==0 for k in ("old_target_FFT_intrinsic_cubic_point_and_ray_stages_recomputed",
                "old_complete_forcing_coefficient_rows_recomputed","old_complete_amplitude_cases_recomputed",
                "old_complete_Taylor_algebra_stages_recomputed","old_complete_physical_seam_operators_recomputed")))
        gate("all original mean nonlocal physical-seam and strong-return limitations remain explicit",
            not doc["old_circle_nonlocal_and_independent_even_mean_budget_paid"]
            and doc["all_original_physical_seams_and_mean_equations_retained"]
            and not doc["artificial_interface_source_introduced"]
            and not doc["complete_strong_return_norm_or_cutoff97_inverse_claimed"])
        doc.update(complete=True,proved=True)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            complete_cases=sum(bool(c.get("complete")) for c in doc["cases"]),
            new_coefficient_derivative_rows=doc["new_coefficient_derivative_rows"],
            reused_coefficient_derivative_rows=doc["reused_coefficient_derivative_rows"],
            new_strict_exterior_rows=doc["new_strict_exterior_rows"],
            reused_strict_exterior_rows=doc["reused_strict_exterior_rows"],
            native_sha256=sha(a.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
