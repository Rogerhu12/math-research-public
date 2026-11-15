#!/usr/bin/env python3
"""Root-value-subtracted first Airy bounds from complete accepted natural stages.

No previous target, FFT, finite Taylor stage, exterior derivative row or seam is
re-evaluated. New scalar root norms, divided-forcing integrals and ordered
derivative majorants refer to the same original first correction.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L

PUBLIC="Rogerhu12/math-research-public"
EXT_SOURCE="e196557e61aa9b83249654a1a81ca3a003ca38e1e07f4ff4fdb19a877f86f4df"
EXT_NATIVE="7322737799bb339750e2df4fb9738da32690801cb669655a600200df5691ba35"
TAYLOR="18990ac2c1ed8e559d00982b75d663c08ad7e193455de1f8482511c36938b719"
TAYLOR_SOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
TAYLOR_MANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"
AUX="84e2bd1b7637299e94428b22cc19aba290d0b661f9dbe18dae918bf752f10077"
ROOT="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
SEAM="871aa54de8c4ee1caa47cdab39c8033bb9cd02e9d4d1f404b711ab8c28825642"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
DELTA=Q(1,10**8);H=Q(9,10**6);RC=Q(1,3000)
AUX_WIDTH=Q(3,128);ROOT_WIDTH=Q(23,1024);QUOTIENT_WIDTH=Q(11,512)
RAY_WIDTH=Q(5,256);VALUE_WIDTH=Q(1,64);DERIV_WIDTH=Q(1,128)
TABLE_WIDTH=Q(1,256);OUTPUT_WIDTH=Q(1,512);INPUT_WIDTH=Q(1,32)
LEADING_WIDTH=Q(3,64)
RADII=(Q(1,1000),Q(1,500),Q(1,200),Q(1,100),Q(3,200),Q(1,50))

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,compresslevel=6 if value.get("complete") else 1,mtime=0)
    tmp=path.with_name(path.name+".partial");tmp.write_bytes(raw);tmp.replace(path)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def box(v):
    if isinstance(v,arb):return v
    if isinstance(v,dict) and "ball" in v:return arb(v["ball"])
    return arb(v)
def up(v):return abs(box(v)).upper()
def rec(v):
    v=arb(v)
    if not v.is_finite():raise ValueError("nonfinite complete root-subtracted bound")
    return dict(ball=v.str(48))
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return v
def decode(v):
    if isinstance(v,dict) and set(v)=={"ball"}:return arb(v["ball"])
    if isinstance(v,dict):return {k:decode(x) for k,x in v.items()}
    if isinstance(v,list):return [decode(x) for x in v]
    return v
def ipow(x,n):
    if n<0:raise ValueError("negative integer exponent is not an outward product")
    v=arb(1)
    for _ in range(n):v*=x
    return v
def power(x,p):return (box(x).log()*ex(p)).exp()
def total(v):return sum(v,arb(0)).upper()
def mv(a,b):return [total(a[i][j]*b[j] for j in range(2)) for i in range(2)]
def va(*v):return [total(a[i] for a in v) for i in range(2)]
def vs(v,c):return [(a*c).upper() for a in v]
def ms(a,c):return [vs(v,c) for v in a]
def nonnegative(v):
    if isinstance(v,arb):return bool(v.is_finite() and v>=0)
    if isinstance(v,dict):return all(nonnegative(x) for x in v.values())
    if isinstance(v,(tuple,list)):return all(nonnegative(x) for x in v)
    return True
def receipt(path,base):
    return dict(file=str(path.relative_to(base)),bytes=path.stat().st_size,sha256=sha(path))
def checked(base,r):
    path=base/r["file"]
    if not path.is_file() or sha(path)!=r["sha256"] or path.stat().st_size!=r["bytes"]:
        raise ValueError("an exact original natural stage changed: "+r["file"])
    return read(path)
def geom(delta):
    if not delta>0:raise ValueError("an angular conversion lost its actual positive width")
    z=(-4*delta).exp();d=1-z
    if not d>0:raise ValueError("the complete Fourier denominator is not positive")
    return [(1+z)/d,8*z/(d*d),32*z*(1+z)/ipow(d,3),
        128*z*(1+4*z+z*z)/ipow(d,4)]
def full_norms(poly,width):
    values=[arb(0) for _ in range(5)]
    for j,c in enumerate(poly.c,poly.lo):
        q=4*abs(j);term=abs(c).upper()*L.fourier_weight(abs(j),str(width))
        values[0]+=term
        if j:
            for k in range(1,5):values[k]+=term*(q**k)
    return [v.upper() for v in values]

def complete_root_norms(stages,aux,roots,accepted_coefficients):
    """New scalar norms of seven already complete Fourier coefficient stages."""
    case=aux["cases"][1]
    if not (case["complete"] and case["proved"] and case["failure"] is None
        and all(g["passed"] for g in case["gates"])
        and Q(case["exact_fold_radius"])==Q(3,8000)
        and Q(case["exact_old_leading_width"])==AUX_WIDTH):
        raise ValueError("the original whole auxiliary product is not the paid one")
    f=decode(case["fold_evidence"]["complete_fold_and_leading_bounds"])
    lead=case["direct_leading_evidence"]
    aa=up(lead["direct_a0_ordinary_derivatives"]["0,0"])
    bb=up(lead["direct_b0_ordinary_derivatives"]["0,0"])
    force=decode(case["first_forcing_evidence"]["complete_degree_zero_first_forcing"])
    gap=box(f["gap"]).lower();Gi=up(f["Gi"]);TM=up(f["TM"])
    if not (gap>0 and H+roots[1]-roots[0]<RC<Q(case["exact_fold_radius"])
        and ROOT_WIDTH<AUX_WIDTH):
        raise ValueError("the complete inner Taylor tail lost a genuine old-product gap")
    deti=Gi*Gi/(gap*gap)
    global_fb=(deti*(aa*up(force["Fb"])+TM*bb*up(force["Fa"]))).upper()
    global_fa=(deti*(bb*up(force["Fb"])+aa*up(force["Fa"]))).upper()
    coefficient=decode(accepted_coefficients)
    if len(coefficient)!=7 or any(row["degree"]!=j for j,row in enumerate(coefficient)):
        raise ValueError("the new root coefficient norm prefix is incomplete")
    rootpoly=L.LP.restore(stages[0]["fb"])
    h=ex(H+roots[1]-roots[0]);z=h/ex(RC);den=1-z
    if not den>0:raise ValueError("the complete Taylor tail ratio is not below one")
    tails=[ipow(z,7)/den,(7*ipow(z,6)/den+ipow(z,7)/(den*den))/ex(RC)]
    margin=ex(AUX_WIDTH-ROOT_WIDTH)
    inner={}
    for name,whole in (("fb",global_fb),("fa",global_fa)):
        inner[name]={}
        for p,q in ((0,0),(0,1),(1,0),(1,1)):
            finite=total(ex(Q(math.factorial(j),math.factorial(j-p)))*
                ipow(h,j-p)*coefficient[j][name][q] for j in range(p,7))
            tail=(whole*tails[p]*math.factorial(q)/ipow(margin,q)).upper()
            inner[name][str((p,q))]=(finite+tail).upper()
    mean=rootpoly.mean();nonmean=rootpoly-rootpoly.constant_part()
    result=dict(exact_norm_width=str(ROOT_WIDTH),exact_auxiliary_rho_circle=str(RC),
        exact_auxiliary_outer_phi_width=str(AUX_WIDTH),exact_inner_cover_radius=str(H+roots[1]-roots[0]),
        complete_coefficient_norms=encode(coefficient),
        complete_normalized_forcing_old_product_suprema=encode(dict(fb=global_fb,fa=global_fa)),
        complete_inner_forcing_jets=encode(inner),
        exact_root_mean_ball=L.cpack(mean),complete_root_mean_absolute_bound=rec(abs(mean).upper()),
        complete_root_nonmean_norm=rec(nonmean.norm(ROOT_WIDTH)),
        complete_root_function_angular_norms=encode(coefficient[0]["fb"]),
        full_root_support=[rootpoly.lo,rootpoly.hi],
        no_root_coefficient_or_mean_removed=True,original_finite_stages_recomputed=0)
    if not nonnegative(decode(result)):raise ValueError("a new complete root norm is invalid")
    return result

def case_profile(case,refined,rootnorm,roots):
    """All gates refer to the same real parameter family and old product."""
    radius=Q(case["exact_radius"]);R=ex(radius+roots[1]-roots[0])
    v=decode(case["bounds"]);af=refined["actual_forcing"]
    if not (case["passed"] and refined["passed"] and all(g["passed"] for g in refined["gates"])
        and refined["exact_radius"]==str(radius)
        and af["leading_strip"]==str(LEADING_WIDTH) and af["output_strip"]==str(VALUE_WIDTH)):
        raise ValueError("an original complete real-radius certificate changed")
    Am=box(v["A_lower"]).lower();Ap=up(v["A_upper"]);ap=up(v["a_upper"])
    E=up(af["flow_variational_C"]["1"]);xm=(2-E).lower()
    c1=up(af["A_angular_constants"]["1"]);c2=up(af["A_angular_constants"]["2"])
    D0=up(v["D0"]);D1=up(v["D1"]);G=up(v["leading_G"]);Gi=up(v["leading_G_inverse"])
    gap=box(v["fold_noncharacteristic_gap"]).lower()
    if not min(Am,xm,gap)>0:raise ValueError("an original fold inverse lower gap vanished")
    Y2=(ex(Q(2,3))*power(Am,Q(-1,3))*c1).upper()
    Yphi2=(ex(Q(2,3))*power(Am,Q(-1,3))*c2+
        ex(Q(2,9))*R*power(Am,Q(-4,3))*c1*c1).upper()
    U0=(ap*power(Am,Q(-1,3))*E).upper()
    U1=(ap*power(Am,Q(-1,3))*(up(af["flow_variational_C"]["2"])+E*c1/(3*Am))).upper()
    J3=(ap*power(Ap,Q(1,3))*Y2).upper()
    Jphi3=(ap*power(Ap,Q(1,3))*Yphi2).upper()
    Jphi4=(ap*power(Am,Q(-2,3))*c1*Y2/3).upper()
    lift=(D0+J3*ipow(R,3)/xm).upper()
    domain=dict(fixed_X_lift=bool(R*lift<ex(ROOT_WIDTH-QUOTIENT_WIDTH)),
        root_polynomial_composition=bool(E*ex(QUOTIENT_WIDTH)<ex(ROOT_WIDTH)),
        negative_real_parameter_ray=bool(ex(VALUE_WIDTH)*(D1*R).exp()<ex(RAY_WIDTH)),
        positive_complete_optical_ray=bool(ex(VALUE_WIDTH)+D0*R+
            up(v["positive_optical_integral"])<ex(RAY_WIDTH)))
    inner=decode(rootnorm["complete_inner_forcing_jets"])
    hin=(inner["fb"]["(1, 0)"]+lift*inner["fb"]["(0, 1)"]).upper()
    p=dict(R=R,Am=Am,Ap=Ap,ap=ap,E=E,xmin=xm,G=G,Gi=Gi,gap=gap,
        D0=D0,D1=D1,Y2=Y2,Yphi2=Yphi2,U0=U0,U1=U1,
        J3=J3,Jphi3=Jphi3,Jphi4=Jphi4,lift=lift,Hinner=hin,
        Linner=(hin*power(Am,Q(-2,3))).upper(),
        inner_fa=inner["fa"]["(0, 0)"],
        rootnorm=decode(rootnorm["complete_root_function_angular_norms"]),
        rootmean=up(rootnorm["complete_root_mean_absolute_bound"]),
        rootnonmean=up(rootnorm["complete_root_nonmean_norm"]),
        C2=up(af["flow_variational_C"]["2"]),
        c1=c1,c2=c2)
    return dict(numeric=encode(p),domain_gates=domain,
        usable_negative=all(domain[k] for k in ("fixed_X_lift","root_polynomial_composition","negative_real_parameter_ray")),
        usable_positive=all(domain[k] for k in ("fixed_X_lift","root_polynomial_composition","positive_complete_optical_ray")),
        exact_value_width=str(VALUE_WIDTH),exact_derivative_width=str(DERIV_WIDTH),
        exact_ray_width=str(RAY_WIDTH),exact_quotient_width=str(QUOTIENT_WIDTH),
        exact_root_forcing_width=str(ROOT_WIDTH),exact_original_forcing_width=str(INPUT_WIDTH),
        same_real_delta_disk=True,negative_imaginary_width_bound_not_transferred_to_positive_side=True,
        original_positive_optical_integral_reused=case["bounds"]["positive_optical_integral"])

def normalized_seam(s,p):
    rho=ex(Q(s["exact_maximum_root_distance"]))
    y=p["Y2"]*rho*rho;T=rho*power(p["Ap"],Q(2,3))
    aa=p["G"]*(p["E"]*p["E"]+T*y*y);bb=2*p["G"]*p["E"]*y
    di=p["Gi"]*p["Gi"]/(p["gap"]*p["gap"])
    jump=decode(s["full_degree_zero_forcing_jump"])
    return (di*(aa*up(jump["F_b"])+T*bb*up(jump["F_a"]))).upper()

def fold_rows(p,af,c,rmin,rmax):
    """New low-order coefficient products only; old leading derivatives are read."""
    R=ex(rmax);h=ex(rmin);Am,Ap,ap=p["Am"],p["Ap"],p["ap"]
    A=[Ap]+[(R*up(af["A_angular_constants"][str(q)])).upper() for q in (1,2,3)]
    x=[p["E"]]+[(R*up(af["flow_variational_C"][str(q+1)])).upper() for q in (1,2,3)]
    T=[(R*power(Ap,Q(2,3))).upper(),
        (ex(Q(2,3))*R*power(Am,Q(-1,3))*A[1]).upper(),
        (ex(Q(2,3))*R*power(Am,Q(-1,3))*A[2]+ex(Q(2,9))*R*power(Am,Q(-4,3))*A[1]*A[1]).upper(),
        (ex(Q(2,3))*R*power(Am,Q(-1,3))*A[3]+ex(Q(2,3))*R*power(Am,Q(-4,3))*A[1]*A[2]
          +ex(Q(8,27))*R*power(Am,Q(-7,3))*ipow(A[1],3)).upper()]
    y=T[1:]
    q=[(ap*power(Am,Q(-1,3))).upper(),
       (ap*power(Am,Q(-4,3))*A[1]/3).upper(),
       (ap*(power(Am,Q(-4,3))*A[2]/3+ex(Q(4,9))*power(Am,Q(-7,3))*A[1]*A[1])).upper()]
    ar=up(af["radial_a_derivatives"]["first"])
    Ar=up(af["A_mixed_derivative_bounds"]["(1, 0)"])
    qr=(ar*power(Am,Q(-1,3))+ap*power(Am,Q(-4,3))*Ar/3).upper()
    D,Dr=c["D"],c["Dr"]
    def prod(a,b,j):return total(math.comb(j,i)*a[i]*b[j-i] for i in range(j+1))
    QTy=[total(math.comb(j,i)*q[i]*prod(T,y,j-i) for i in range(j+1)) for j in range(3)]
    Xr=[(QTy[j]+prod(D,x,j)).upper() for j in range(3)]
    Tr=[(prod(q,x,j)+prod(D,y,j)).upper() for j in range(3)]
    Xrr=(qr*T[0]*y[0]+q[0]*Tr[0]*y[0]+q[0]*T[0]*Tr[1]+Dr[0]*x[0]+D[0]*Xr[1]).upper()
    Trr=(qr*x[0]+q[0]*Xr[1]+Dr[0]*y[0]+D[0]*Tr[1]).upper()
    aa={k:up(v) for k,v in af["leading_a0_derivative_bounds"].items()}
    bb={k:up(v) for k,v in af["leading_b0_derivative_bounds"].items()}
    def get(v,r,j,width):
        key=str((r,j))
        if key in v:return v[key]
        available=[q for q in range(j) if str((r,q)) in v]
        if not available:raise ValueError("a complete original leading derivative is missing")
        k=max(available)
        return (v[str((r,k))]*math.factorial(j-k)/ipow(ex(LEADING_WIDTH-width),j-k)).upper()
    def Bj(j,width):
        av=get(aa,0,j,width);bv=get(bb,0,j,width)
        tb=total(math.comb(j,k)*T[k]*get(bb,0,j-k,width) for k in range(j+1))
        return [[av,tb],[bv,av]]
    def Brj(j,width):
        av=get(aa,1,j,width);bv=get(bb,1,j,width)
        tb=total(math.comb(j,k)*(Tr[k]*get(bb,0,j-k,width)+T[k]*get(bb,1,j-k,width)) for k in range(j+1))
        return [[av,tb],[bv,av]]
    Brr=[[get(aa,2,0,DERIV_WIDTH),
        (Trr*get(bb,0,0,DERIV_WIDTH)+2*Tr[0]*get(bb,1,0,DERIV_WIDTH)+T[0]*get(bb,2,0,DERIV_WIDTH)).upper()],
        [get(bb,2,0,DERIV_WIDTH),get(aa,2,0,DERIV_WIDTH)]]
    tmin=(h*power(Am,Q(2,3))).lower()
    if not tmin>0:raise ValueError("the actual strict T lower bound is not positive")
    return dict(T=T,x=x,q=q,qr=qr,Tr=Tr,Xr=Xr,Xrr=Xrr,Trr=Trr,tmin=tmin,
        B_value=Bj(0,VALUE_WIDTH),B=[Bj(j,TABLE_WIDTH) for j in range(4)],
        Br=[Brj(j,TABLE_WIDTH) for j in range(3)],Brr=Brr,
        B_D=[Bj(j,DERIV_WIDTH) for j in range(3)],
        Br_D=[Brj(j,DERIV_WIDTH) for j in range(2)])

def two_ray_amplitudes(p,ell,Lmax,fa_max):
    R=ex(ell);b=p["rootnorm"];T=(R*power(p["Ap"],Q(2,3))).upper()
    y=p["Y2"]*R*R
    Ga=(fa_max+2*T*b[1]).upper()
    Ga1=(fa_max/ex(ROOT_WIDTH-RAY_WIDTH)+2*(y*b[1]+T*b[2]*p["E"])).upper()
    L1=(Lmax/ex(QUOTIENT_WIDTH-RAY_WIDTH)).upper()
    eg=(p["D1"]*R).exp()
    A=(p["U0"]*Ga*R/2+p["J3"]*Lmax*ipow(R,4)/8+p["ap"]*p["ap"]*eg*
        (p["C2"]*Lmax*ipow(R,4)/20+p["E"]*L1*ipow(R,3)/9+
         (p["Yphi2"]*Ga+p["Y2"]*Ga1)*ipow(R,5)/35)).upper()
    B=(p["ap"]*power(p["Am"],Q(-1,3))*
        (p["E"]*Lmax*R/3+p["Y2"]*Ga*ipow(R,3)/7)+
        p["ap"]*eg*power(p["Am"],Q(-1,3))*
        (p["U0"]*Ga1*ipow(R,2)/5+p["U1"]*Ga*ipow(R,3)/14+
         (p["Jphi3"]*Lmax+p["J3"]*L1)*ipow(R,5)/44+
         p["Jphi4"]*Lmax*ipow(R,6)/65)).upper()
    return [A,B],Ga,Ga1,L1

def refined_derivative_row(row,c,p,af,Lmax,fa_max):
    rmin,rmax=map(Q,row["exact_root_distance_interval"]);R=ex(rmax)
    l=fold_rows(p,af,c,rmin,rmax)
    T,x,q,qr,Tr,Xr=l["T"],l["x"],l["q"],l["qr"],l["Tr"],l["Xr"]
    y=T[1:];D,Dr=c["D"],c["Dr"];tm=l["tmin"];b=p["rootnorm"]
    Z,ga,gaphi,Lphi=two_ray_amplitudes(p,rmax,Lmax,fa_max)
    delta=ex(VALUE_WIDTH-DERIV_WIDTH)
    Zp=vs(Z,1/delta);Zpp=vs(Z,2/(delta*delta))
    f=decode(row["normalized_forcing_f"]);fr=decode(row["normalized_forcing_f_rho"])
    gar=(up(fr[0])+2*(Tr[0]*b[1]+T[0]*b[2]*Xr[0])).upper()
    Lr=((up(fr[1])+b[1]*Xr[0]+Tr[0]*Lmax)/tm).upper()
    C=[[D[0],q[0]*T[0]],[q[0],D[0]]]
    Cr=[[Dr[0],qr*T[0]+q[0]*Tr[0]],[qr,Dr[0]]]
    Cp=[[D[1],q[1]*T[0]+q[0]*y[0]],[q[1],D[1]]]
    M=ms([[arb(0),q[0]*y[0]],[arb(0),q[0]*x[0]/tm]],arb(1)/2)
    def Md(qv,xv,yv,tv):
        return ms([[arb(0),qv*y[0]+q[0]*yv],
            [arb(0),(qv*x[0]+q[0]*xv)/tm+q[0]*x[0]*tv/(tm*tm)]],arb(1)/2)
    Mr=Md(qr,Xr[1],Tr[1],Tr[0]);Mp=Md(q[1],x[1],y[1],y[0])
    base=[(x[0]*ga+y[0]*T[0]*Lmax).upper(),(y[0]*ga+x[0]*Lmax).upper()]
    V=vs(base,q[0]/2)
    bp=[(x[1]*ga+x[0]*gaphi+(y[1]*T[0]+y[0]*y[0])*Lmax+y[0]*T[0]*Lphi).upper(),
        (y[1]*ga+y[0]*gaphi+x[1]*Lmax+x[0]*Lphi).upper()]
    br=[(Xr[1]*ga+x[0]*gar+(Tr[1]*T[0]+y[0]*Tr[0])*Lmax+y[0]*T[0]*Lr).upper(),
        (Tr[1]*ga+y[0]*gar+Xr[1]*Lmax+x[0]*Lr).upper()]
    Vp=va(vs(base,q[1]/2),vs(bp,q[0]/2))
    Vr=va(vs(base,qr/2),vs(br,q[0]/2))
    Zr=va(mv(C,Zp),mv(M,Z),V)
    Zrp=va(mv(Cp,Zp),mv(C,Zpp),mv(Mp,Z),mv(M,Zp),Vp)
    Zrr=va(mv(Cr,Zp),mv(C,Zrp),mv(Mr,Z),mv(M,Zr),Vr)
    Zstar=[[arb(0),p["rootmean"]+p["rootnonmean"]],
        [arb(0),b[1]*x[0]],
        [arb(0),b[2]*x[0]*x[0]+b[1]*x[1]],
        [arb(0),b[3]*ipow(x[0],3)+3*b[2]*x[0]*x[1]+b[1]*x[2]]]
    bprime=[b[1],b[2]*x[0],b[3]*x[0]*x[0]+b[2]*x[1]]
    Zstarr=[[arb(0),total(math.comb(j,k)*bprime[k]*Xr[j-k] for k in range(j+1))] for j in range(3)]
    Zstarrr=[arb(0),(b[2]*Xr[0]*Xr[0]+b[1]*l["Xrr"]).upper()]
    Wvalue=mv(l["B_value"],va(Z,Zstar[0]))
    dz=ex(VALUE_WIDTH-TABLE_WIDTH);dr=ex(DERIV_WIDTH-TABLE_WIDTH)
    Zj=[vs(Z,math.factorial(j)/ipow(dz,j)) for j in range(4)]
    Zrj=[Zr]+[vs(Zr,math.factorial(j)/ipow(dr,j)) for j in (1,2)]
    Zrj[1]=[min(a,b).upper() for a,b in zip(Zrj[1],Zrp)]
    Zrj[2]=[min(a,b/dr).upper() for a,b in zip(Zrj[2],Zrp)]
    W=[va(*(vs(mv(l["B"][k],va(Zj[j-k],Zstar[j-k])),math.comb(j,k))
        for k in range(j+1))) for j in range(4)]
    Wr=[va(*(vs(va(mv(l["Br"][k],va(Zj[j-k],Zstar[j-k])),
        mv(l["B"][k],va(Zrj[j-k],Zstarr[j-k]))),math.comb(j,k))
        for k in range(j+1))) for j in range(3)]
    Z_D=[Z,Zp,Zpp]
    W_D=[va(*(vs(mv(l["B_D"][k],va(Z_D[j-k],Zstar[j-k])),math.comb(j,k))
        for k in range(j+1))) for j in range(3)]
    Zr_D=[Zr,Zrp]
    Wr_D=[va(*(vs(va(mv(l["Br_D"][k],va(Z_D[j-k],Zstar[j-k])),
        mv(l["B_D"][k],va(Zr_D[j-k],Zstarr[j-k]))),math.comb(j,k))
        for k in range(j+1))) for j in range(2)]
    Wrd=Wr_D[0]
    Wrr=va(mv(l["Brr"],va(Z,Zstar[0])),
        vs(mv(l["Br_D"][0],va(Zr,Zstarr[0])),2),mv(l["B_D"][0],va(Zrr,Zstarrr)))
    gv=geom(ex(VALUE_WIDTH-OUTPUT_WIDTH));gr=geom(ex(DERIV_WIDTH-OUTPUT_WIDTH))
    gt=geom(ex(TABLE_WIDTH-OUTPUT_WIDTH))[0]
    tables={}
    for i,name in enumerate(("a1","b1")):
        sup={};wn={}
        for j in range(4):
            key="0,"+str(j);sup[key]=W[j][i]
            wn[key]=min((gt*W[j][i]).upper(),(gv[j]*Wvalue[i]).upper()).upper()
        for j in range(3):
            key="1,"+str(j);sup[key]=Wr[j][i]
            wn[key]=min((gt*Wr[j][i]).upper(),(gr[j]*Wrd[i]).upper()).upper()
        sup["2,0"]=Wrr[i];wn["2,0"]=(gr[0]*Wrr[i]).upper()
        tables[name]=dict(strip_sup=sup,Wiener=wn)
    # Reuse the accepted complete leading/potential coefficients. The actual
    # local numerator has no additional 1/n or missing factor mu.
    raw=[]
    for i in range(2):
        raw.append(total([Wrr[i],2*D[0]*Wr_D[1][i],
            (D[0]*D[0]+c["eta_upper"]*c["eta_upper"]*c["K"][0])*W_D[2][i],
            (Dr[0]+D[0]*D[1])*W_D[1][i],
            c["T0"]*(Wr_D[0][i]+D[0]*W_D[1][i]),c["V0"]*W_D[0][i],
            c["vartheta"]*q[0]*(T[0]*W_D[0][1] if i==0 else W_D[0][0])]))
    # Local W_D and Wr_D are separately paid on DERIV_WIDTH. The additional
    # TABLE_WIDTH products serve the complete source derivative tables only.
    result=dict(first_amplitude_budgets=encode(tables),
        exact_amplitude_output_phi_width=str(OUTPUT_WIDTH),
        complete_unnormalized_local_numerator=encode(raw),
        exact_local_numerator_phi_width=str(DERIV_WIDTH),
        complete_normalized_remainder_value=encode(Z),
        complete_normalized_remainder_rho=encode(Zr),
        complete_normalized_remainder_rhorho=encode(Zrr),
        exact_Ng_cancellation_used=True,complete_Ng=encode(V),
        complete_Ng_rho=encode(Vr),complete_Ng_phi=encode(Vp),
        complete_root_mean_preserved=True,
        complete_root_mean_only_removed_from_composition_derivatives=True,
        original_local_source_integral_not_reused_for_changed_numerator=True,
        full_local_or_nonlocal_source_integral_claimed=False)
    if not nonnegative(decode(result)):raise ValueError("a refined complete derivative bound is invalid")
    return result

def coefficient_norm_row(stage,degree):
    if stage["degree"]!=degree:raise ValueError("an original normalized forcing degree changed")
    fb=L.LP.restore(stage["fb"]);fa=L.LP.restore(stage["fa"])
    if max(fb.degree,fa.degree)>192*(degree+2):
        raise ValueError("the full original normalized forcing support changed")
    return dict(degree=degree,fb=encode(full_norms(fb,ROOT_WIDTH)),
        fa=encode(full_norms(fa,ROOT_WIDTH)),fb_range=[fb.lo,fb.hi],fa_range=[fa.lo,fa.hi],
        exact_norm_width=str(ROOT_WIDTH),original_complete_payload_sha256=payload_sha(stage))

def better_tables(old,new):
    old,new=decode(old),decode(new)
    if set(old)!=set(new):raise ValueError("different first-correction components were compared")
    out={}
    for name in old:
        out[name]={}
        for norm in old[name]:
            if set(old[name][norm])!=set(new[name][norm]):
                raise ValueError("different complete derivative windows were compared")
            out[name][norm]={key:min(up(old[name][norm][key]),up(new[name][norm][key])).upper()
                for key in old[name][norm]}
    return encode(out)

def local_source(raw,c,case,side):
    amplitude=decode(case["original_complete_analytic_amplitude_numeric"])
    profiles=decode(case["original_radial_reference_profiles_numeric"])
    fourier=up(case["new_complete_Fourier_factor"])
    def combine(name):return total(x*y for x,y in zip(profiles[name],raw))
    core=((ipow(combine("central"),2)+4*ipow(combine("negative"),2)).sqrt()
        if side=="negative" else max(combine("central"),combine("positive")))
    before=(up(amplitude["composition"])*fourier*core).upper()
    return before,(c["original_C_J_scalar"]*before).upper()

def case_summary(case,original):
    sides={}
    for side in ("negative","positive"):
        rows=[r for r in case["rows"] if r["side"]==side]
        if not rows:raise ValueError("the original strict side disappeared")
        first=rows[0]["first_amplitude_budgets"]
        maxima={}
        for name in first:
            maxima[name]={norm:{key:rec(max(up(r["first_amplitude_budgets"][name][norm][key])
                for r in rows).upper()) for key in first[name][norm]} for norm in first[name]}
        norm=total(up(r["complete_first_row_local_squared_source_integral"]) for r in rows).sqrt().upper()
        sides[side]=dict(complete_rows=len(rows),refined_rows=sum(r["new_root_subtracted_derivatives"] for r in rows),
            original_fallback_rows=sum(not r["new_root_subtracted_derivatives"] for r in rows),
            complete_first_row_local_L2_source=rec(norm),complete_w1_exterior_derivative_suprema=maxima,
            complete_normalized_forcing_seam_count=len(case["traversal_states"][side]["included_seam_indices"]))
    negative=up(sides["negative"]["complete_first_row_local_L2_source"])
    gain=up(original["actual_negative_source_to_primitive_L2_gain"])
    return dict(exact_radius=case["exact_radius"],exact_cover=case["exact_cover"],complete=True,
        complete_exterior_rows=len(case["rows"]),domain_gates=case["profile"]["domain_gates"],
        source_summary=sides,
        negative_local_component_Hminus4over3_to_primitive_L2=rec((negative*gain).upper()),
        positive_collar_local_source_L2=rec(arb(0)),
        positive_body_local_source_L2=sides["positive"]["complete_first_row_local_L2_source"],
        original_complete_local_source_bound_retained_where_new_path_failed=True,
        full_old_circle_nonlocal_and_independent_mean_integral_from_new_tables_claimed=False,
        all_original_physical_seam_sources_unchanged=True,
        zero_root_and_other_sources_for_this_linear_local_component=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","prepared","out"):
        parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics requires the actual public repository Actions")
    import scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise ValueError("the exact original numerical environment changed")
    if args.out.exists():raise FileExistsError("preserve every existing scientific result")
    ctx.prec=320
    start=time.monotonic()
    doc=dict(kind="complete_root_value_subtracted_first_Airy_derivatives_and_local_sources",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),algebra_sha256=sha(L.__file__),
        input_manifest_sha256=sha(args.manifest),runtime=runtime,
        complete=False,proved=False,failure=None,gates=[],root_stage=None,case_stages=[],cases=[],
        original_exterior_native_sha256=EXT_NATIVE,original_exterior_source_sha256=EXT_SOURCE,
        original_complete_Taylor_native_sha256=TAYLOR,original_complete_Taylor_source_sha256=TAYLOR_SOURCE,
        original_complete_auxiliary_native_sha256=AUX,original_complete_root_native_sha256=ROOT,
        original_complete_seam_native_sha256=SEAM,
        fixed_intrinsic_parameter="eta_0",exact_real_delta_radius=str(DELTA),
        physical_frequency="4|j|",actual_first_correction_density="n^(1/6)",
        input_cutoff=97,source_window="ordinary L2_r H^(-2/3) for the actual first row",
        original_target_FFT_Taylor_coefficient_derivative_seam_and_profile_stages_recomputed=0,
        new_root_coefficient_norm_rows=0,reused_root_coefficient_norm_rows=0,
        new_root_tail_stages=0,reused_root_tail_stages=0,new_case_profiles=0,reused_case_profiles=0,
        new_seam_normalizations=0,reused_seam_normalizations=0,
        new_divided_forcing_rows=0,reused_divided_forcing_rows=0,
        new_refined_derivative_rows=0,reused_refined_derivative_rows=0,
        new_local_source_rows=0,original_fallback_rows=0,reused_original_fallback_rows=0,
        exact_root_mean_and_all_old_fourier_outputs_retained=True,
        true_physical_seam_sources_unchanged=True,no_artificial_inner_interface_source=True,
        new_tables_full_old_circle_and_independent_mean_integrals_claimed=False,
        positive_weighted_port_or_full_high_inverse_or_strong_cutoff97_claimed=False)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(args.out,doc)
    def gate(name,truth):
        value=bool(truth);doc["gates"].append(dict(name=name,passed=value))
        if not value:raise ValueError("complete root subtraction gate failed: "+name)
    def save_stage(path,value):
        save(path,value)
        return receipt(path,args.out.parent)
    try:
        manifest=read(args.manifest)
        gate("the immutable manifest belongs to this exact public scalar consumer",
            manifest["public_repository"]==PUBLIC and manifest["mathematical_parameters"]["input_cutoff"]==97)
        for pin in manifest["files"]:
            path=args.repo_root/pin["path"]
            if not path.is_file() or sha(path)!=pin["sha256"] or path.stat().st_size!=pin["bytes"]:
                raise ValueError("a pinned original scientific file changed: "+pin["path"])
        paths={k:args.repo_root/v for k,v in manifest["input_paths"].items()}
        external={}
        for pin in manifest["external_completed_natives"]:
            path=args.prepared/pin["prepared_path"]
            if not path.is_file() or sha(path)!=pin["sha256"] or path.stat().st_size!=pin["bytes"]:
                raise ValueError("an actual original artifact input changed")
            external[pin["name"]]=path
        old=read(paths["exterior_index"]);oproc=read(paths["exterior_process"])
        root=read(external["root"]);seam=read(paths["seam_native"])
        taylor=read(paths["Taylor_native"]);tproc=read(paths["Taylor_process"])
        aux=read(paths["auxiliary_native"]);aproc=read(paths["auxiliary_process"])
        gate("all complete original mathematical processes really succeeded",
            all(x["complete"] and x["proved"] and x["failure"] is None
                and all(g["passed"] for g in x["gates"]) for x in (old,root,seam,taylor,aux))
            and all(p["complete"] and p["actual_returncode"]==0 and p["mathematical_complete"]
                and p["mathematical_failure"] is None for p in (oproc,tproc,aproc)))
        gate("all original native and exact source byte identities agree",
            sha(paths["exterior_index"])==oproc["native_sha256"]==EXT_NATIVE
            and old["source_sha256"]==oproc["mathematical_source_sha256"]==EXT_SOURCE
            and sha(paths["Taylor_native"])==tproc["native_sha256"]==TAYLOR
            and taylor["source_sha256"]==TAYLOR_SOURCE and taylor["input_manifest_sha256"]==TAYLOR_MANIFEST
            and sha(paths["auxiliary_native"])==aproc["native_sha256"]==AUX
            and sha(external["root"])==ROOT and sha(paths["seam_native"])==SEAM
            and sha(external["Taylor"])==TAYLOR)
        gate("the same fixed family true root physical seams and original finite supports are retained",
            old["background_definition_sha256"]==root["background_definition_sha256"]==taylor["background_definition_sha256"]==BASE
            and old["explicit_direction_definition_sha256"]==root["explicit_direction_definition_sha256"]==taylor["explicit_direction_definition_sha256"]==ZDEF
            and old["actual_intrinsic_parameter"]==taylor["actual_intrinsic_parameter"]==aux["actual_intrinsic_parameter"]=="eta_0"
            and Q(taylor["exact_complex_delta_radius"])==Q(aux["exact_complex_delta_radius"])==DELTA
            and old["exact_root_interval"]==root["exact_root_interval"]==taylor["exact_root_interval"]==aux["exact_root_interval"]
            and len(old["case_stages"])==len(root["cases"])==len(seam["refined_forcing_radius_cases"])==6
            and len(root["rows"])==1300 and len(seam["seams"])==1079
            and len(taylor["stages"])==75 and tproc["all_complete_Fourier_arrays_and_all_natural_prefix_files_verified"])
        roots=list(map(Q,root["exact_root_interval"]));rl,ru=roots
        inner=[str(rl-H),str(ru+H)]
        gate("the full physical inner interval remains inside the original root piece",
            old["exact_physical_inner_interval"]==inner==taylor["old_product_domain"]["exact_physical_interval"]
            and Q(taylor["exact_original_physical_piece_interval"][0])<rl-H
            and ru+H<Q(taylor["exact_original_physical_piece_interval"][1]))
        doc.update(exact_root_interval=list(map(str,roots)),exact_cover=old["exact_cover"],
            exact_physical_inner_interval=inner,fixed_positive_body_cut=old["fixed_positive_body_cut"],
            original_complete_physical_seams_reused=1079,
            original_complete_exterior_rows_reused=4359,
            original_complete_coefficient_rows_reused=1328,
            original_complete_Taylor_finite_stages_recomputed=0)
        if args.resume:
            prev=read(args.resume)
            gate("a restored prefix has exactly the same source inputs runtime and physical family",
                prev["source_sha256"]==doc["source_sha256"] and prev["algebra_sha256"]==doc["algebra_sha256"]
                and prev["input_manifest_sha256"]==doc["input_manifest_sha256"] and prev["runtime"]==runtime
                and all(prev[k]==doc[k] for k in ("original_exterior_native_sha256","original_complete_Taylor_native_sha256",
                    "original_complete_auxiliary_native_sha256","original_complete_root_native_sha256",
                    "original_complete_seam_native_sha256","exact_root_interval","exact_physical_inner_interval")))
            entries=([prev["root_stage"]] if prev.get("root_stage") else [])+prev.get("case_stages",[])
            for entry in entries:
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in ("root","cases"):
                    raise ValueError("an original natural prefix left its own stage directory")
                source=args.resume.parent/relative;target=args.out.parent/relative
                if sha(source)!=entry["sha256"] or source.stat().st_size!=entry["bytes"]:
                    raise ValueError("an exact accepted new prefix changed")
                target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
            doc["root_stage"]=copy.deepcopy(prev.get("root_stage"))
            doc["case_stages"]=copy.deepcopy(prev.get("case_stages",[]));doc["cases"]=copy.deepcopy(prev.get("cases",[]))
            doc["preserved_actual_prefix"]=dict(native_sha256=sha(args.resume),native_bytes=args.resume.stat().st_size,
                run_id=prev["run_id"],failure=prev["failure"],gates=prev["gates"],complete=prev["complete"])
        checkpoint()
        stages=[]
        for degree in range(7):
            name="normalized-forcing-degree-"+str(degree).zfill(3)
            entry=taylor["stages"][name]
            saved=checked(external["Taylor"].parent,entry)
            if not (saved["stage"]==name and saved["complete"] and saved["source_sha256"]==TAYLOR_SOURCE
                and saved["input_manifest_sha256"]==TAYLOR_MANIFEST
                and saved["algebra_sha256"]==sha(L.__file__)):
                raise ValueError("an original complete normalized forcing stage changed provenance")
            stages.append(saved["payload"])
        gate("all seven exact original normalized forcing degrees were restored without finite recomputation",len(stages)==7)
        rp=args.out.parent/"root"/"complete-root-forcing-norms-and-tail.json.gz"
        if doc["root_stage"]:
            rs=checked(args.out.parent,doc["root_stage"])
        else:
            rs=dict(kind="new_scalar_norms_of_exact_root_forcing_coefficients",
                source_sha256=doc["source_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
                complete=False,coefficient_rows=[],whole_product_tail=None)
        if (rs["source_sha256"]!=doc["source_sha256"] or rs["input_manifest_sha256"]!=doc["input_manifest_sha256"]
            or len(rs["coefficient_rows"])>7):
            raise ValueError("a restored new root norm stage changed identity")
        doc["reused_root_coefficient_norm_rows"]=len(rs["coefficient_rows"])
        for degree,stage in enumerate(stages):
            if degree<len(rs["coefficient_rows"]):
                saved=rs["coefficient_rows"][degree]
                if saved["degree"]!=degree or saved["original_complete_payload_sha256"]!=payload_sha(stage):
                    raise ValueError("a reused scalar root norm changed its exact finite input")
                continue
            rs["coefficient_rows"].append(coefficient_norm_row(stage,degree))
            doc["new_root_coefficient_norm_rows"]+=1
            doc["root_stage"]=save_stage(rp,rs);checkpoint()
        if rs["whole_product_tail"] is None:
            rs["whole_product_tail"]=complete_root_norms(stages,aux,roots,rs["coefficient_rows"])
            doc["new_root_tail_stages"]+=1
        else:doc["reused_root_tail_stages"]+=1
        rs["complete"]=True;doc["root_stage"]=save_stage(rp,rs);checkpoint()
        coeff=checked(paths["exterior_index"].parent,old["coefficient_stage"])
        if not (coeff["complete"] and len(coeff["rows"])==1328 and coeff["source_sha256"]==EXT_SOURCE):
            raise ValueError("the original complete exterior coefficient table changed")
        gate("the whole root mean and all1328 original complete coefficient rows are retained",
            rs["whole_product_tail"]["no_root_coefficient_or_mean_removed"] and len(coeff["rows"])==1328)
        for ci,radius in enumerate(RADII):
            original=checked(paths["exterior_index"].parent,old["case_stages"][ci])
            rc=root["cases"][ci];refined=seam["refined_forcing_radius_cases"][ci];af=refined["actual_forcing"]
            if not (original["complete"] and original["source_sha256"]==EXT_SOURCE
                and original["exact_radius"]==rc["exact_radius"]==refined["exact_radius"]==str(radius)
                and original["exact_cover"]==rc["exact_radial_cover"]==refined["exact_cover"]):
                raise ValueError("different actual radius cases were paired")
            cp=args.out.parent/"cases"/("radius-"+str(radius.numerator)+"-"+str(radius.denominator)+".json.gz")
            if ci<len(doc["case_stages"]):
                case=checked(args.out.parent,doc["case_stages"][ci])
                if not (case["source_sha256"]==doc["source_sha256"] and case["input_manifest_sha256"]==doc["input_manifest_sha256"]
                    and case["exact_radius"]==str(radius) and case["original_case_sha256"]==old["case_stages"][ci]["sha256"]):
                    raise ValueError("a restored new case changed original scientific identity")
            else:
                case=dict(kind="root_value_subtracted_complete_first_Airy_radius",
                    source_sha256=doc["source_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
                    original_case_sha256=old["case_stages"][ci]["sha256"],complete=False,
                    exact_radius=str(radius),exact_cover=original["exact_cover"],profile=None,
                    seam_normalizations=[],rows=[],traversal_states={})
                doc["case_stages"].append(save_stage(cp,case));checkpoint()
            if case["complete"]:
                summary=case["complete_case_summary"]
                if ci==len(doc["cases"]):doc["cases"].append(summary)
                elif doc["cases"][ci]!=summary:raise ValueError("a saved complete summary changed")
                doc["reused_case_profiles"]+=1
                doc["reused_seam_normalizations"]+=len(case["seam_normalizations"])
                doc["reused_refined_derivative_rows"]+=sum(r["new_root_subtracted_derivatives"] for r in case["rows"])
                doc["reused_divided_forcing_rows"]+=sum(r["new_root_subtracted_derivatives"] for r in case["rows"])
                doc["reused_original_fallback_rows"]+=sum(not r["new_root_subtracted_derivatives"] for r in case["rows"])
                checkpoint();continue
            if case["profile"] is None:
                case["profile"]=case_profile(rc,refined,rs["whole_product_tail"],roots);doc["new_case_profiles"]+=1
                doc["case_stages"][ci]=save_stage(cp,case);checkpoint()
            else:doc["reused_case_profiles"]+=1
            p=decode(case["profile"]["numeric"])
            selected=[(j,s) for j,s in enumerate(seam["seams"])
                if Q(original["exact_cover"][0])<=Q(s["radial"])<=Q(original["exact_cover"][1])
                and case["profile"]["usable_"+s["side"]]]
            nprev=len(case["seam_normalizations"])
            if nprev>len(selected):raise ValueError("a new seam normalization prefix exceeds the actual selected seams")
            doc["reused_seam_normalizations"]+=nprev
            for si,(index,s) in enumerate(selected):
                if si<nprev:
                    item=case["seam_normalizations"][si]
                    if item["original_seam_index"]!=index or item["radial"]!=s["radial"]:
                        raise ValueError("a reused seam normalization lost its physical identity")
                    continue
                case["seam_normalizations"].append(dict(original_seam_index=index,radial=s["radial"],side=s["side"],
                    original_complete_forcing_jump=copy.deepcopy(s["full_degree_zero_forcing_jump"]),
                    complete_normalized_fb_jump=rec(normalized_seam(s,p))))
                doc["new_seam_normalizations"]+=1;doc["case_stages"][ci]=save_stage(cp,case);checkpoint()
            ordering=sorted(original["rows"],key=lambda r:(0,-Q(r["interval"][1])) if r["side"]=="negative"
                else (1,Q(r["interval"][0])))
            for side in ("negative","positive"):
                if side not in case["traversal_states"]:
                    case["traversal_states"][side]=dict(cumulative_divided_forcing_numerator=rec(ex(H+ru-rl)*p["Hinner"]),
                        full_path_Lb=rec(p["Linner"]),full_path_fa=rec(p["inner_fa"]),
                        included_seam_indices=[],complete_rows=0)
            nprev=len(case["rows"])
            if nprev>len(ordering):raise ValueError("the actual new outward prefix exceeds its original cell cover")
            for index,row in enumerate(ordering):
                ident=dict(processing_serial=index,original_exterior_serial=row["serial"],common_row=row["common_row"],
                    interval=row["interval"],side=row["side"],original_root_row=row["original_root_row"],original_piece=row["original_piece"])
                if index<nprev:
                    saved=case["rows"][index]
                    if any(saved[k]!=v for k,v in ident.items()):raise ValueError("a reused new outward row changed physical identity")
                    key="reused_refined_derivative_rows" if saved["new_root_subtracted_derivatives"] else "reused_original_fallback_rows"
                    doc[key]+=1
                    if saved["new_root_subtracted_derivatives"]:doc["reused_divided_forcing_rows"]+=1
                    continue
                doc["last_attempted_row"]=dict(radius=str(radius),**ident);checkpoint()
                crow=coeff["rows"][row["common_row"]]
                if (crow["original_root_row"]!=row["original_root_row"] or crow["original_piece"]!=row["original_piece"]
                    or not Q(crow["interval"][0])<=Q(row["interval"][0])<Q(row["interval"][1])<=Q(crow["interval"][1])):
                    raise ValueError("the complete original coefficient and exterior row do not match")
                c=decode(crow["bounds"]);side=row["side"];state=case["traversal_states"][side]
                if not case["profile"]["usable_"+side]:
                    item=dict(**ident,new_root_subtracted_derivatives=False,
                        reason="the new path/domain gates for this side did not pass; the original actual bound is retained",
                        first_amplitude_budgets=copy.deepcopy(row["first_amplitude_budgets"]),
                        exact_amplitude_output_phi_width=row["exact_amplitude_output_phi_width"],
                        complete_unnormalized_local_numerator=copy.deepcopy(row["complete_unnormalized_local_numerator"]),
                        exact_local_numerator_phi_width=row["exact_local_numerator_phi_width"],
                        actual_first_row_local_source_singular_envelope=copy.deepcopy(row["actual_first_row_local_source_singular_envelope"]),
                        radial_weight_integral=copy.deepcopy(row["radial_weight_integral"]),
                        complete_first_row_local_squared_source_integral=copy.deepcopy(row["complete_first_row_local_squared_source_integral"]))
                    doc["original_fallback_rows"]+=1
                else:
                    if not (row["exact_normalized_forcing_value_phi_width"]==str(INPUT_WIDTH)
                        and row["exact_amplitude_output_phi_width"]==str(OUTPUT_WIDTH)
                        and row["exact_local_numerator_phi_width"]==str(DERIV_WIDTH)):
                        raise ValueError("an original forcing or derivative window changed")
                    f=decode(row["normalized_forcing_f"]);fr=decode(row["normalized_forcing_f_rho"])
                    left,right=map(Q,row["interval"]);rmin,rmax=map(Q,row["exact_root_distance_interval"])
                    hp=(up(fr[1])+p["lift"]*up(f[1])/ex(INPUT_WIDTH-ROOT_WIDTH)).upper()
                    newseams=[s for s in case["seam_normalizations"] if s["side"]==side
                        and left<=Q(s["radial"])<=right and s["original_seam_index"] not in state["included_seam_indices"]]
                    fee=total(up(s["complete_normalized_fb_jump"]) for s in newseams)
                    cumulative=(up(state["cumulative_divided_forcing_numerator"])+ex(right-left)*hp+fee).upper()
                    localL=(cumulative*power(p["Am"],Q(-2,3))/ex(rmin)).upper()
                    Lmax=max(up(state["full_path_Lb"]),localL).upper()
                    famax=max(up(state["full_path_fa"]),up(f[0])).upper()
                    fresh=refined_derivative_row(row,c,p,af,Lmax,famax)
                    raw=[min(up(a),up(b)).upper() for a,b in zip(row["complete_unnormalized_local_numerator"],
                        fresh["complete_unnormalized_local_numerator"])]
                    before,source=local_source(raw,c,original,side)
                    oldsource=up(row["actual_first_row_local_source_singular_envelope"])
                    source=min(source,oldsource).upper()
                    weight=up(row["radial_weight_integral"])
                    item=dict(**ident,new_root_subtracted_derivatives=True,
                        exact_root_distance_interval=row["exact_root_distance_interval"],
                        complete_new_root_subtracted_derivative_candidate=fresh,
                        full_path_divided_forcing_bound=rec(Lmax),cell_divided_forcing_bound=rec(localL),
                        open_piece_divided_forcing_integrand=rec(hp),new_complete_forcing_jump_sum=rec(fee),
                        newly_included_original_seam_indices=[s["original_seam_index"] for s in newseams],
                        cumulative_divided_forcing_numerator=rec(cumulative),
                        first_amplitude_budgets=better_tables(row["first_amplitude_budgets"],fresh["first_amplitude_budgets"]),
                        exact_amplitude_output_phi_width=str(OUTPUT_WIDTH),
                        complete_unnormalized_local_numerator=encode(raw),exact_local_numerator_phi_width=str(DERIV_WIDTH),
                        actual_source_before_J_singular_envelope=rec(before),
                        actual_first_row_local_source_singular_envelope=rec(source),
                        radial_weight_integral=copy.deepcopy(row["radial_weight_integral"]),
                        complete_first_row_local_squared_source_integral=rec((weight*source*source).upper()),
                        original_local_profile_Fourier_factor_and_radial_weight_reused=True)
                    state.update(cumulative_divided_forcing_numerator=rec(cumulative),full_path_Lb=rec(Lmax),
                        full_path_fa=rec(famax),included_seam_indices=state["included_seam_indices"]+
                        [s["original_seam_index"] for s in newseams])
                    doc["new_divided_forcing_rows"]+=1;doc["new_refined_derivative_rows"]+=1;doc["new_local_source_rows"]+=1
                state["complete_rows"]+=1;case["rows"].append(item)
                doc.pop("last_attempted_row",None);doc["case_stages"][ci]=save_stage(cp,case);checkpoint()
                if index%128==0:print(json.dumps(dict(radius=str(radius),accepted_outward_rows=len(case["rows"]),
                    total_rows=len(ordering),seconds=time.monotonic()-start)),flush=True)
            if len(case["rows"])!=len(original["rows"]):raise ValueError("the actual full exterior cover is incomplete")
            for side in ("negative","positive"):
                if case["profile"]["usable_"+side]:
                    needed={s["original_seam_index"] for s in case["seam_normalizations"] if s["side"]==side
                        and any(r["side"]==side and Q(r["interval"][0])<=Q(s["radial"])<=Q(r["interval"][1]) for r in original["rows"])}
                    if set(case["traversal_states"][side]["included_seam_indices"])!=needed:
                        raise ValueError("a true forcing seam is absent from the outward ledger")
            summary=case_summary(case,original)
            case.update(complete=True,complete_case_summary=summary,
                all_original_physical_seams_retained=True,original_coefficient_and_derivative_rows_recomputed=0)
            doc["case_stages"][ci]=save_stage(cp,case);checkpoint()
            if ci==len(doc["cases"]):doc["cases"].append(summary)
            elif ci<len(doc["cases"]):doc["cases"][ci]=summary
            else:raise ValueError("the complete radius summary prefix has a gap")
            checkpoint()
        gate("all six actual radius cases retain every original exterior row and physical side",
            len(doc["cases"])==6 and sum(c["complete_exterior_rows"] for c in doc["cases"])==4359
            and all(c["complete"] and Q(c["exact_radius"])==RADII[i] for i,c in enumerate(doc["cases"])))
        gate("no original successful mathematics was recomputed or missing source was silently certified",
            doc["original_target_FFT_Taylor_coefficient_derivative_seam_and_profile_stages_recomputed"]==0
            and doc["original_complete_Taylor_finite_stages_recomputed"]==0
            and doc["exact_root_mean_and_all_old_fourier_outputs_retained"]
            and not doc["new_tables_full_old_circle_and_independent_mean_integrals_claimed"]
            and not doc["positive_weighted_port_or_full_high_inverse_or_strong_cutoff97_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as e:
        doc["failure"]=dict(type=type(e).__name__,message=str(e));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_root_coefficient_norm_rows=doc["new_root_coefficient_norm_rows"],
            new_refined_derivative_rows=doc["new_refined_derivative_rows"],
            original_fallback_rows=doc["original_fallback_rows"],complete_cases=len(doc["cases"]),
            native_sha256=sha(args.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
