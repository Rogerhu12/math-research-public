#!/usr/bin/env python3
"""Anchored auxiliary folds and direct complex leading derivatives.

Only the two completed auxiliary cases and unchanged true-root anchors
are consumed. No intrinsic target, primitive, cubic or transport is rerun.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import flint
from flint import acb,arb,ctx

PUBLIC="Rogerhu12/math-research-public"
AUXSHA="6276b4b8bd117b3092ce633b7164ff99968100f10b09cbaef8850d4c03f6b24f"
AUXSOURCE="70f848effb2e57c64b2c9e8100d6ac0af01968c13c939a4874c6f44b0a759d21"
AUXMANIFEST="404e8352112f38cd5b96dc42ebe49c9c11ebab3a2f2fc53db3f1e247314285da"
ROOTSHA="397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
BUDGETSHA="10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
RADII=(Q(1,10000),Q(1,2000))
DELTA=Q(1,10**8);WIDTH=Q(1,32);SG=Q(3,128);SF=Q(1,64)
SV=Q(3,256);SX=Q(1,1024);SI=Q(1,128);SO=Q(1,512)
HREAL=Q(9,10**6);LAM=Q(9,2)
KEY2=[(i,j) for i in range(3) for j in range(3-i)]
KEY3=[(i,j) for i in range(3) for j in range(4-i)]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);x=p.read_bytes()
    return json.loads(gzip.decompress(x) if p.suffix==".gz" else x)
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    q=p.with_name(p.name+".partial");q.write_bytes(raw);q.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def box(v):
    if "lower" in v and "upper" in v:return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def up(v):return abs(v).upper()
def cb(v):return acb(box(v["real"]),box(v["imag"]))
def bup(v):return up(box(v))
def interval(a,b):return ex(a).union(ex(b))
def square(r):
    r=arb(r).upper();return acb(arb(0,r),arb(0,r))
def intersection(a,b):
    l=max(a.lower(),b.lower());h=min(a.upper(),b.upper())
    if l>h:raise ValueError("two enclosures of the same auxiliary function are disjoint")
    return l.union(h)
def cintersection(a,b):return acb(intersection(a.real,b.real),intersection(a.imag,b.imag))
def power(a,p):return (arb(a).log()*ex(p)).exp()
def powr(a,p):return power(a,p).upper()
def ipow(a,n):
    v=arb(1)
    for _ in range(n):v=v*a
    return v
def rec(v):
    v=arb(v)
    if not v.is_finite():raise ValueError("nonfinite new anchored bound")
    return dict(ball=v.str(48),lower=v.lower().str(48),upper=v.upper().str(48))
def compact(v):return dict(ball=arb(v).str(48))
def crecord(v):return dict(real=rec(v.real),imag=rec(v.imag),modulus_upper=rec(up(v)))
def encode(v):
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return compact(v)
def decode(v):
    if isinstance(v,dict):
        if "ball" in v:return box(v)
        return {k:decode(x) for k,x in v.items()}
    if isinstance(v,list):return [decode(x) for x in v]
    return v
def bell(n,k,values):
    @lru_cache(maxsize=None)
    def B(a,b):
        if a==b==0:return arb(1)
        if a<=0 or b<=0 or b>a:return arb(0)
        return sum((math.comb(a-1,i-1)*values[i]*B(a-i,b-1)
            for i in range(1,a-b+2)),arb(0))
    return B(n,k).upper()
def multiply(a,b,keys):
    return {(i,j):sum((a.get((p,q),arb(0))*b.get((i-p,j-q),arb(0))
        for p in range(i+1) for q in range(j+1)),arb(0)).upper() for i,j in keys}
def normjet(d,keys=KEY2):
    return {k:(d.get(k,arb(0))/(math.factorial(k[0])*math.factorial(k[1]))).upper() for k in keys}
def ordinary(d):return {k:(v*math.factorial(k[0])*math.factorial(k[1])).upper() for k,v in d.items()}
def power_derivatives(A,p,amin,amax):
    da=normjet(A,KEY3);da[(0,0)]=arb(0)
    powers={0:{(0,0):arb(1)}};out={(0,0):powr(amax,p)}
    c=Q(1)
    for n in range(1,4):
        powers[n]=multiply(powers[n-1],da,KEY3);c*=Q(p-n+1,n)
        scale=ex(abs(c))*powr(amin if p-n<0 else amax,p-n)
        for k in KEY3:
            if k!=(0,0):out[k]=out.get(k,arb(0))+scale*powers[n][k]
    return ordinary(out)

def original_anchor(germ,rb):
    intr=germ["complex_intrinsic_coefficients"]
    k=box(intr["K1"]["real"]);gamma=box(intr["gamma"]["real"])
    # These reality restrictions are only at the real true root.
    mean0=box(germ["moving_mean_v"]["real"])+ex(Q(rb["exact_background_root_offsets"][32]))
    zmean=bup(rb["response_repaired_complete_coefficient_upper"][96])
    mean=acb(mean0)+square(ex(DELTA)*zmean)
    eta=-acb(gamma)*mean;a=eta*acb(k).sqrt()
    if not (k>0 and gamma>0 and mean.real<0 and eta.real>0 and a.real>0):
        raise ValueError("the unchanged true-root anchor lost its full parameter gap")
    return dict(k=k,gamma=gamma,mean=mean,eta=eta,a=a)

def anchored_coefficients(acase,anchor,R,check):
    intr=acase["complete_complex_intrinsic_evidence"]["ordinary_intrinsic_jets"]
    fam=acase["complete_family_budget"]
    jets={k:[cb(v) for v in a] for k,a in intr.items()}
    etaj=[cb(v) for v in fam["complete_eta_ordinary_jets"]]
    K2,K3=up(jets["K"][2]),up(jets["K"][3])
    eta1,eta2=up(etaj[1]),up(etaj[2])
    kr=cintersection(acb(anchor["k"])+square(ex(R)*K2),jets["K"][1])
    k=cintersection(acb(anchor["k"])+square(ex(R)*K2/2),jets["K"][1])
    eta=cintersection(anchor["eta"]+square(ex(R)*eta1),etaj[0])
    check("anchored_k_eta_and_current_Kr_are_the_same_function_enclosures",
        k.real>0 and eta.real>0 and kr.real>0)
    km,kp=k.real.lower(),up(k);em,ep=eta.real.lower(),up(eta)
    a=eta*k.sqrt();am,ap=a.real.lower(),up(a)
    check("the_anchored_full_complex_characteristic_gap_is_strict",am>0)
    k1,k2=K2/2,K3/3
    a1=(eta1*kp.sqrt()+ep*k1/(2*km.sqrt())).upper()
    a2=(eta2*kp.sqrt()+eta1*k1/km.sqrt()
        +ep*(k2/(2*km.sqrt())+k1*k1*powr(km,Q(-3,2))/4)).upper()
    table=fam["strips"][str(WIDTH)]
    U=[[bup(x) for x in row] for row in table["full_family_U_ordinary_radial_angular_jets"]]
    V=[[bup(x) for x in row] for row in table["full_family_V_ordinary_radial_angular_jets"]]
    VN=[[bup(x) for x in row] for row in table["full_family_V_nonmean_ordinary_radial_angular_jets"]]
    mean=up(cb(fam["complete_mean_ordinary_jets"][0]))
    beta,br=up(jets["beta"][0]),up(jets["beta"][1])
    K=min(up(jets["K"][0]),ex(R)*kp).upper();Kr=up(kr)
    def prod(a,b,n):
        return sum((math.comb(n,j)*a[j]*b[n-j] for j in range(n+1)),arb(0)).upper()
    S=[(prod(U[0],U[0],q)+K*prod(V[0],V[0],q)).upper() for q in range(5)]
    Sr=[(2*prod(U[0],U[1],q)+Kr*prod(V[0],V[0],q)+2*K*prod(V[0],V[1],q)).upper()
        for q in range(3)]
    nonmean=(U[0][0]*U[0][0]+K*(2*mean*VN[0][0]+VN[0][0]*VN[0][0])).upper()
    D=[(beta*nonmean/4).upper(),(beta*nonmean).upper()]
    D.extend((beta*S[q-1]).upper() for q in range(2,6))
    Dr=[((br*S[0]+beta*Sr[0])/4).upper()]
    Dr.extend((br*S[q-1]+beta*Sr[q-1]).upper() for q in range(1,3))
    u0,u1=U[0][:2];v0,v1=V[0][:2];ur,vr=U[1][0],V[1][0]
    eratio=(eta1/em).upper()
    ell=(2*beta*u0*v0).upper()
    ellp=(2*beta*(u1*v0+u0*v1)).upper()
    ellr=(2*br*u0*v0+2*beta*(ur*v0+u0*vr)).upper()
    epoly=(2*beta*(3*u0*u1+K*v0*v1)).upper()
    b0=(beta*(1+u0*u0+3*K*v0*v0)).upper()
    b0p=(2*beta*(u0*u1+3*K*v0*v1)).upper()
    b0r=(br*(1+u0*u0+3*K*v0*v0)
        +beta*(2*u0*ur+3*Kr*v0*v0+6*K*v0*vr)).upper()
    tq=(eratio+D[1]+beta*(1+3*u0*u0+K*v0*v0)).upper()
    rq=(ellr+D[0]*ellp+ep*epoly+2*beta*ep*u1*u0+ell*(eratio+D[1])).upper()
    theta=(rq/em+2*beta*K*v0*v1).upper()
    V0=(tq*b0+b0r+D[0]*b0p+K*(ell*ell+4*beta*ep*v0*u1)).upper()
    T0=(eratio+4*beta*S[0]+5*D[1]).upper()
    out=dict(km=km,kp=kp,em=em,ep=ep,am=am,ap=ap,k1=k1,k2=k2,a1=a1,a2=a2,
        D=D,Dr=Dr,U=U,V=V,beta=beta,beta_r=br,K=K,Kr=Kr,T0=T0,V0=V0,
        vartheta=theta,rQ=rq,ell=ell,b0=b0,eta_log_r=eratio,
        log_EG_r=(2*beta*S[0]).upper(),log_EG_rr=(2*(br*S[0]+beta*Sr[0])).upper())
    evidence=dict(complete_subdomain_k=crecord(k),complete_subdomain_eta=crecord(eta),
        complete_current_Kr=crecord(kr),complete_characteristic_a=crecord(a),
        original_root_anchor={k:crecord(acb(v)) for k,v in anchor.items()},
        actual_root_identity_used_before_K_modulus=True,
        complete_coefficient_majorants=encode(out))
    return out,dict(a=a,k=k,eta=eta),evidence

def fold_budget(c,cboxes,anchor,R,check):
    r=ex(R);D=c["D"];E=(D[1]*r).exp().upper();j=(E-1).upper()
    M0=(D[0]*r+ex(Q(2,3))*c["ap"]*powr(r,Q(3,2))).upper();B=(3*M0).upper()
    check("all_auxiliary_direct_inverse_and_common_foot_paths_fit",
        B<ex(WIDTH-SG) and B<ex(SG-SF))
    delta=(ex(Q(3,5))*r*c["a1"]+c["ap"]*j).upper()
    Abox=cintersection(anchor["a"]+square(delta),cboxes["a"]+square(c["ap"]*j))
    Am=Abox.real.lower();Ap=min(up(Abox),c["ap"]*E,up(anchor["a"])+delta).upper()
    check("the_anchored_even_divided_phase_has_its_actual_cube_root_gap",Am>0)
    BA=(ex(Q(3,5))*c["ap"]*D[2]*r*(4*D[1]*r).exp()).upper()
    BT=(ex(Q(2,5))*c["ap"]*D[2]*powr(Am,Q(-1,3))*r*r*(4*D[1]*r).exp()).upper()
    TM=(r*powr(Ap,Q(2,3))).upper()
    de=(2*j+j*j+TM*BT*BT).upper();gap=(1-de).lower()
    check("the_complete_auxiliary_Jacobian_and_principal_factor_are_nonzero",de<ex(Q(1,4)))
    jac=(c["am"]*power(Ap,Q(-1,3))*gap).lower()
    mu=(c["am"]*c["am"]*power(Ap,Q(-2,3))*gap).lower()
    Xbox=acb(1)+square(j)
    Ainverse=(Abox.log()*acb(-ex(Q(1,3)))).exp()
    Er=(up(acb(ex(LAM))-cboxes["a"]*Ainverse*Xbox)+D[0]*BT).upper()
    eps=(Er/ex(LAM)).upper()
    Xr=(D[0]*E+ex(Q(2,3))*c["ap"]*r*r*BA).upper()
    rowr=(eps+BT*B/(ex(LAM)*r)).upper();rowp=(Xr*r/B+j).upper()
    check("the_true_auxiliary_inverse_is_a_radial_self_map",eps<ex(Q(1,4)))
    check("both_normalized_true_inverse_rows_contract",rowr<ex(Q(1,2)) and rowp<ex(Q(1,2)))
    hEG=(r*c["log_EG_r"]).upper()
    ksmax,ksmin=up(anchor["k"]),anchor["k"].lower()
    esmax,esmin=up(anchor["eta"]),anchor["eta"].real.lower()
    G=(powr(ksmax/esmin,Q(1,6))*powr(Ap,Q(1,6))*powr(c["km"],Q(-1,4))*hEG.exp()).upper()
    Gi=(powr(esmax/ksmin,Q(1,6))*powr(Am,Q(-1,6))*powr(c["kp"],Q(1,4))*hEG.exp()).upper()
    branchgap=(1-j-TM.sqrt()*BT).lower()
    check("both_complete_leading_Airy_branches_are_invertible",branchgap>0)
    Bi=(Gi/(branchgap*branchgap)).upper()
    M=(G*(E*E+TM*BT*BT)).upper()
    B2=(ex(Q(4,5))*G*E*c["ap"]*D[2]*powr(Am,Q(-5,3))*(4*D[1]*r).exp()).upper()
    out=dict(E=E,j=j,M0=M0,B=B,Am=Am,Ap=Ap,BA=BA,BT=BT,TM=TM,gap=gap,
        jac=jac,mu=mu,Er=Er,Xr=Xr,row_r=rowr,row_phi=rowp,
        G=G,Gi=Gi,M=M,B2=B2,Bi=Bi,Q=(c["ap"]*powr(Am,Q(-1,3))).upper())
    return out,dict(anchored_A_box=crecord(Abox),anchored_A_difference_radius=rec(delta),
        complete_fold_and_leading_bounds=encode(out),
        exact_inverse_fixed_point="rho_new=-tau/lambda+(T+lambda*rho)/lambda; phi_new=chi-(X-phi)",
        exact_canonical_radius=str(LAM*R/2),exact_canonical_width=str(SF))

def direct_leading(c,f,R,check):
    """The finite L12--L24 mixed-jet calculus on this analytic auxiliary piece."""
    r=ex(R);D,Dr=c["D"],c["Dr"];E,j=f["E"],f["j"]
    ap,a1,a2=c["ap"],c["a1"],c["a2"];Am,Ap=f["Am"],f["Ap"]
    C={1:E}
    for n in range(2,6):
        vals={1:E,**{q:r*C[q] for q in range(2,n)}}
        C[n]=(E*sum((D[k]*bell(n,k,vals) for k in range(2,n+1)),arb(0))).upper()
    X={1:E,**{n:(r*C[n]).upper() for n in range(2,6)}}
    ca={}
    for n in range(1,5):
        vals={1:E,**{q:r*C[q] for q in range(2,n+1)}}
        ca[n]=(ex(Q(3,5))*ap*sum((C[k+1]*bell(n,k,vals)
            for k in range(1,n+1)),arb(0))).upper()
    ag={0:Ap,**{n:(r*ca[n]).upper() for n in range(1,5)}}
    xr={}
    for n in range(1,4):
        xr[n]=(sum((math.comb(n,l)*D[l]*X[n-l+1] for l in range(n+1)),arb(0))
            +ex(Q(2,3))*ap*r*r*ag[n+1]).upper()
    xrr={}
    for n in (1,2):
        q=n+1
        rho2Ar=(r*r*sum((math.comb(q,l)*D[l]*ag[q-l+1] for l in range(q+1)),arb(0))
            +ex(Q(3,2))*r*(ap*X[q+1]+ag[q])).upper()
        xrr[n]=(sum((math.comb(n,l)*(Dr[l]*X[n-l+1]+D[l]*xr[n-l+1])
            for l in range(n+1)),arb(0))
            +ex(Q(2,3))*(a1*r*r*ag[n+1]+2*ap*r*ag[n+1]+ap*rho2Ar)).upper()
    P0=(D[0]*(1+E)).upper()
    P1=(2*D[1]*E+r*C[2]*D[0]).upper()
    P2=(D[2]*(E*E+E)+3*D[1]*r*C[2]+D[0]*r*C[3]).upper()
    P00=((1+E)*Dr[0]+D[1]*P0+D[0]*P1).upper()
    P11=(2*E*Dr[1]+D[2]*E*P0+2*D[1]*P1+D[0]*P2+r*C[2]*Dr[0]).upper()
    A={(0,0):Ap,**{(0,n):ag[n] for n in (1,2,3)}}
    A[1,0]=(ex(Q(3,5))*a1*E+ex(Q(3,5))*ap*xr[1]+ap*X[2]*P0).upper()
    A[2,0]=(ex(Q(3,7))*a2*E+2*a1*(ex(Q(3,7))*xr[1]+ex(Q(3,5))*X[2]*P0)
        +ap*(ex(Q(3,7))*xrr[1]+ex(Q(6,5))*xr[2]*P0+X[3]*P0*P0+X[2]*P00)).upper()
    A[1,1]=(ex(Q(3,5))*a1*X[2]*E
        +ap*(ex(Q(3,5))*xr[2]*E+X[3]*P0*E+X[2]*P1)).upper()
    A[1,2]=(ex(Q(3,5))*a1*(X[3]*E*E+X[2]*r*C[2])
        +ap*(ex(Q(3,5))*xr[3]*E*E+X[4]*P0*E*E+2*X[3]*E*P1
            +ex(Q(3,5))*xr[2]*r*C[2]+X[3]*P0*r*C[2]+X[2]*P2)).upper()
    A[2,1]=(ex(Q(3,7))*a2*X[2]*E
        +2*a1*(ex(Q(3,7))*xr[2]*E+ex(Q(3,5))*X[3]*P0*E+ex(Q(3,5))*X[2]*P1)
        +ap*(ex(Q(3,7))*xrr[2]*E+ex(Q(6,5))*xr[3]*P0*E+X[4]*P0*P0*E
            +X[3]*P00*E+ex(Q(6,5))*xr[2]*P1+2*X[3]*P0*P1+X[2]*P11)).upper()
    # The analytic auxiliary extension has no seams. Original physical seams are not removed.
    lr=(A[1,0]/(6*Am)+c["k1"]/(4*c["km"])+c["log_EG_r"]).upper()
    lp=(A[0,1]/(6*Am)).upper()
    lrr=((A[2,0]/Am+ipow(A[1,0]/Am,2))/6
        +(c["k2"]/c["km"]+ipow(c["k1"]/c["km"],2))/4+c["log_EG_rr"]).upper()
    lrp=((A[1,1]/Am+A[1,0]*A[0,1]/(Am*Am))/6).upper()
    lpp=((A[0,2]/Am+ipow(A[0,1]/Am,2))/6).upper()
    G=f["G"]
    gd={(0,0):G,(1,0):G*lr,(0,1):G*lp,
        (2,0):G*(lrr+lr*lr),(1,1):G*(lrp+lr*lp),(0,2):G*(lpp+lp*lp)}
    F=power_derivatives(A,Q(2,3),Am,Ap)
    td={(i,k):(r*F[i,k]+(i*F[i-1,k] if i else 0)).upper() for i,k in KEY2}
    tpd={(i,k):(r*F[i,k+1]+(i*F[i-1,k+1] if i else 0)).upper() for i,k in KEY2}
    xd={(0,0):X[1],(0,1):X[2],(0,2):X[3],
        (1,0):xr[1],(1,1):xr[2],(2,0):xrr[1]}
    gj,xj,tj,tpj=map(normjet,(gd,xd,td,tpd))
    xx=multiply(xj,xj,KEY2);tt=multiply(tj,multiply(tpj,tpj,KEY2),KEY2)
    av=ordinary(multiply(gj,{k:xx[k]+tt[k] for k in KEY2},KEY2))
    bv=ordinary({k:2*v for k,v in multiply(gj,multiply(xj,tpj,KEY2),KEY2).items()})
    Xrr=(Dr[0]*E+D[0]*xr[1]+ex(Q(2,3))*
        (a1*r*r*ag[1]+2*ap*r*ag[1]+ap*r*r*A[1,1])).upper()
    chain=dict(Tr=td[1,0],Xr=f["Xr"],Tp=td[0,1],Xp=E,
        Trr=td[2,0],Xrr=Xrr,Trp=td[1,1],Xrp=xr[1],Tpp=td[0,2],Xpp=X[2])
    check("all_direct_leading_mixed_jets_and_fold_chain_bounds_are_finite",
        all(v.is_finite() and v.lower()>=0 for v in list(av.values())+list(bv.values())+list(chain.values())))
    return av,bv,chain,dict(
        auxiliary_seam_fee_exactly_zero_only_for_the_analytic_extension=True,
        actual_global_physical_seams_retained=True,
        radial_Cauchy_used_for_leading_second_derivatives=False,
        finite_variational_C=encode(C),A_mixed_derivatives=encode(A),G_mixed_derivatives=encode(gd),
        direct_a0_ordinary_derivatives=encode({str(i)+","+str(j):v for (i,j),v in av.items()}),
        direct_b0_ordinary_derivatives=encode({str(i)+","+str(j):v for (i,j),v in bv.items()}),
        full_direct_fold_chain=encode(chain))

def local_pair(a,b,c,f):
    D,Dr=c["D"],c["Dr"]
    def diagonal(v):
        return dict(radial_second=v[2,0],radial_angular=(2*D[0]*v[1,1]).upper(),
            angular_second=((D[0]*D[0]+c["ep"]*c["ep"]*c["K"])*v[0,2]).upper(),
            drift_derivative=((Dr[0]+D[0]*D[1])*v[0,1]).upper(),
            first_transport=(c["T0"]*(v[1,0]+D[0]*v[0,1])).upper(),
            scalar_potential=(c["V0"]*v[0,0]).upper())
    aa,bb=diagonal(a),diagonal(b)
    aa["exact_QK_cross"]=(c["vartheta"]*f["Q"]*f["TM"]*b[0,0]).upper()
    bb["exact_QK_cross"]=(c["vartheta"]*f["Q"]*a[0,0]).upper()
    total=[(sum(row.values(),arb(0))/f["mu"]).upper() for row in (aa,bb)]
    return total,[{k:(v/f["mu"]).upper() for k,v in row.items()} for row in (aa,bb)]

def canonical_to_old(v,c):
    return {(0,0):v[0,0],
        (1,0):(v[1,0]*c["Tr"]+v[0,1]*c["Xr"]).upper(),
        (0,1):(v[1,0]*c["Tp"]+v[0,1]*c["Xp"]).upper(),
        (2,0):(v[2,0]*c["Tr"]*c["Tr"]+2*v[1,1]*c["Tr"]*c["Xr"]
            +v[0,2]*c["Xr"]*c["Xr"]+v[1,0]*c["Trr"]+v[0,1]*c["Xrr"]).upper(),
        (1,1):(v[2,0]*c["Tr"]*c["Tp"]+v[1,1]*(c["Tr"]*c["Xp"]+c["Xr"]*c["Tp"])
            +v[0,2]*c["Xr"]*c["Xp"]+v[1,0]*c["Trp"]+v[0,1]*c["Xrp"]).upper(),
        (0,2):(v[2,0]*c["Tp"]*c["Tp"]+2*v[1,1]*c["Tp"]*c["Xp"]
            +v[0,2]*c["Xp"]*c["Xp"]+v[1,0]*c["Tpp"]+v[0,1]*c["Xpp"]).upper()}

def forced_case(av,bv,chain,c,f,R,roots,original_cell,scalar_cell,check):
    RT=LAM*R/2;Ri=RT/2
    optical=(ex(Q(2,3))*powr(ex(RT),Q(3,2))).upper()
    check("all_canonical_forcing_characteristics_and_the_quotient_Cauchy_margin_fit",
        ex(SV)+optical+ex(SX)<ex(SF))
    forcing,firstparts=local_pair(av,bv,c,f);Fb,Fa=forcing
    B0=(f["M"]+f["B2"]*powr(ex(RT),Q(5,2))).upper();Bi=f["Bi"]
    common=(B0*Bi).upper()
    a1=(common*ex(RT)*Fa/2+
        (common*ipow(ex(RT),2)/(2*ex(SX))+
        f["B2"]*Bi*(1+common/6)*ipow(ex(RT),3))*Fb).upper()
    b1=(common*Fb+
        (common*ipow(ex(RT),2)/(5*ex(SX))+
        f["B2"]*Bi*(ex(Q(1,2))+common/7)*ipow(ex(RT),3))*Fa).upper()
    left,right=roots[0]-HREAL,roots[1]+HREAL
    h=ex(HREAL+roots[1]-roots[0])
    check("the_physical_inner_cover_belongs_to_the_original_root_scalar_and_cubic_germs",
        original_cell[0]<left<right<original_cell[1]
        and scalar_cell[0]<left<right<scalar_cell[1])
    check("the_actual_physical_inner_cover_maps_to_the_paid_smaller_canonical_rectangle",
        h*powr(f["Ap"],Q(2,3))<ex(Ri)
        and ex(SO)+f["M0"]<ex(SI) and h<ex(R)
        and SI<SV and Ri<RT)
    dt,dx=ex(RT-Ri),ex(SV-SI)
    canonical=[]
    for w in (a1,b1):
        canonical.append({(p,q):(w*math.factorial(p)*math.factorial(q)/
            (ipow(dt,p)*ipow(dx,q))).upper() for p,q in KEY2})
    olda,oldb=[canonical_to_old(v,chain) for v in canonical]
    residual,parts=local_pair(olda,oldb,c,f)
    check("the_complete_first_amplitudes_and_local_next_residual_bounds_are_finite",
        all(v.is_finite() and v.lower()>=0 for v in forcing+[a1,b1]+residual))
    return dict(exact_forcing_T_radius=str(RT),exact_forcing_X_width=str(SF),
        exact_amplitude_X_width=str(SV),exact_quotient_Cauchy_X_margin=str(SX),
        exact_inner_T_radius=str(Ri),exact_inner_X_width=str(SI),
        exact_physical_inner_radius=str(HREAL),exact_physical_inner_cover=[str(left),str(right)],
        exact_physical_output_phi_width=str(SO),
        positive_Cauchy_margins=encode(dict(radial=dt,angular=dx)),
        complete_degree_zero_first_forcing=encode(dict(Fb=Fb,Fa=Fa)),
        complete_first_forcing_parts=encode(firstparts),
        separated_first_amplitudes=encode(dict(a1=a1,b1=b1,B0=B0,Bi=Bi)),
        canonical_first_amplitude_derivatives=encode([
            {str(i)+","+str(j):v for (i,j),v in row.items()} for row in canonical]),
        original_first_amplitude_derivatives=encode([
            {str(i)+","+str(j):v for (i,j),v in row.items()} for row in (olda,oldb)]),
        complete_local_L0_w1_bounds=encode(dict(first=residual[0],second=residual[1])),
        complete_local_L0_w1_parts=encode(parts),
        exact_QK_identity_used_for_both_cross_terms=True,
        auxiliary_and_original_first_amplitude_germs_identified_only_on_original_piece=True,
        artificial_physical_interface_source_inserted=False,
        complete_old_circle_I_J_source_on_w1_paid=False,
        independent_even_mean_operator_budget_paid=False,
        complete_global_strong_return_norm_paid=False)

class CaseGateFailure(ValueError):pass

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    args=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new anchored budgets run only in the public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0"):
        raise RuntimeError("the exact reviewed numerical runtime changed")
    if args.out.exists():raise FileExistsError("preserve every actual new budget and partial case")
    ctx.prec=320;ctx.cap=4;started=time.monotonic()
    doc=dict(kind="actual_anchored_auxiliary_root_fold_direct_leading_and_first_forcing",
        complete=False,proved=False,failure=None,source_sha256=sha(__file__),runtime=runtime,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        root_germ_sha256=ROOTSHA,root_budget_sha256=BUDGETSHA,auxiliary_native_sha256=AUXSHA,
        background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        actual_intrinsic_parameter="eta_0",exact_complex_delta_radius=str(DELTA),
        original_targets_primitives_cubics_and_completed_domain_jets_recomputed=0,
        true_root_anchor_and_complete_parameter_mean_retained=True,
        physical_background_outside_original_piece_changed=False,
        original_physical_seam_and_source_equations_retained=True,
        old_circle_I_J_and_independent_mean_source_on_w1_paid=False,
        complete_strong_return_or_cutoff97_inverse_claimed=False,
        original_auxiliary_audit_global_proved_false_retained=True,
        new_coefficient_cases=0,reused_coefficient_cases=0,
        new_fold_cases=0,reused_fold_cases=0,
        new_direct_leading_cases=0,reused_direct_leading_cases=0,
        new_first_forcing_cases=0,reused_first_forcing_cases=0,gates=[],cases=[])
    def checkpoint():
        doc["seconds"]=time.monotonic()-started;save(args.out,doc)
    def check_input(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("unchanged anchored input gate failed: "+name)
    try:
        manifest=read(args.manifest);doc["input_manifest_sha256"]=sha(args.manifest)
        for entry in manifest["files"]:
            path=args.repo_root/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a fixed scientific input changed: "+entry["path"])
        paths={k:args.repo_root/v for k,v in manifest["input_paths"].items()}
        germ,rb,aux,aproc=[read(paths[k]) for k in ("root_germ","root_budget","auxiliary_native","auxiliary_process")]
        check_input("the_exact_original_root_and_completed_auxiliary_audit_bytes_match",
            sha(paths["root_germ"])==ROOTSHA and sha(paths["root_budget"])==BUDGETSHA
            and sha(paths["auxiliary_native"])==AUXSHA and aproc["native_sha256"]==AUXSHA
            and aproc["actual_returncode"]==1 and aproc["complete"] is False
            and aux["complete"] is True and aux["proved"] is False
            and aux["source_sha256"]==AUXSOURCE and aux["input_manifest_sha256"]==AUXMANIFEST
            and str(aux["run_id"])=="43640181602"
            and aux["failure"]["type"]=="RuntimeError"
            and aux["all_requested_domains_attempted"] is True)
        check_input("the_same_physical_repair_full_direction_and_complete_real_intrinsic_box_are_retained",
            germ["complete"] and germ["proved"] and germ["failure"] is None
            and rb["complete"] and rb["proved"] and rb["failure"] is None
            and rb["background_definition_sha256"]==aux["background_definition_sha256"]==BASE
            and rb["explicit_direction_definition_sha256"]==aux["explicit_direction_definition_sha256"]==ZDEF
            and rb["actual_intrinsic_parameter"]==aux["actual_intrinsic_parameter"]=="eta_0"
            and Q(rb["exact_complex_parameter_radius"])==DELTA
            and Q(aux["exact_complex_delta_radius"])==DELTA
            and germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and germ["actual_candidate_piece"]==aux["original_polynomial_piece"]==2549
            and len(rb["exact_background_root_offsets"])==65
            and len(rb["response_repaired_complete_coefficient_upper"])==193
            and aux["original_completed_small_domain_results_recomputed"]==0
            and aux["auxiliary_extension_only"] is True
            and aux["physical_background_identity_outside_original_piece_claimed"] is False)
        roots=list(map(Q,germ["root_interval"]))
        original_cell=list(map(Q,germ["exact_candidate_piece_interval"]))
        scalar_cell=list(map(Q,germ["original_scalar_germ"]))
        check_input("all_actual_root_and_original_piece_endpoints_agree",
            roots==list(map(Q,aux["exact_root_interval"]))
            and original_cell==list(map(Q,aux["exact_original_piece_interval"]))
            and scalar_cell==list(map(Q,aux["original_scalar_germ"]))
            and rb["exact_intrinsic_parameter"]==germ["exact_center_parameter"]
            and germ["exact_center_parameter"]==aux["exact_intrinsic_affine_center"])
        doc.update(exact_root_interval=list(map(str,roots)),
            exact_original_piece_interval=list(map(str,original_cell)),
            exact_original_scalar_germ=list(map(str,scalar_cell)))
        if args.resume:
            previous=read(args.resume)
            check_input("every_accepted_new_prefix_has_identical_source_manifest_runtime_and_original_natives",
                previous["source_sha256"]==sha(__file__)
                and previous["input_manifest_sha256"]==sha(args.manifest)
                and previous["runtime"]==runtime
                and previous["root_germ_sha256"]==ROOTSHA
                and previous["root_budget_sha256"]==BUDGETSHA
                and previous["auxiliary_native_sha256"]==AUXSHA)
            doc["cases"]=previous["cases"]
            if "complete_original_root_anchor" in previous:
                doc["complete_original_root_anchor"]=previous["complete_original_root_anchor"]
        if "complete_original_root_anchor" in doc:
            anchor={k:cb(v) for k,v in doc["complete_original_root_anchor"].items()}
            for k in ("k","gamma"):anchor[k]=anchor[k].real
            doc["original_anchor_reused"]=True
        else:
            anchor=original_anchor(germ,rb)
            doc["complete_original_root_anchor"]={k:crecord(acb(v)) for k,v in anchor.items()}
            doc["original_anchor_reused"]=False
            checkpoint()
        for ci,Ra in enumerate(RADII):
            acase=next(x for x in aux["cases"] if Q(x["exact_auxiliary_radius"])==Ra)
            check_input("selected_auxiliary_domain_"+str(Ra)+"_was_actually_and_completely_proved",
                acase["complete"] is True and acase["proved"] is True and acase["failure"] is None
                and acase["intrinsic_evaluation_complete"] is True
                and acase["intrinsic_domain_failure"] is None
                and len(acase["polynomial_component_jets"]["candidate"])==65
                and len(acase["polynomial_component_jets"]["response"])==193
                and acase["exact_identity_with_original_family_only_on_original_germ_intersection"] is True)
            R=3*Ra/4
            if ci<len(doc["cases"]):
                case=doc["cases"][ci]
                if Q(case["exact_input_auxiliary_radius"])!=Ra or Q(case["exact_fold_radius"])!=R:
                    raise ValueError("a saved new fold case changed its exact domain")
                if case.get("attempt_complete"):
                    doc["reused_coefficient_cases"]+=int("coefficient_evidence" in case)
                    doc["reused_fold_cases"]+=int("fold_evidence" in case)
                    doc["reused_direct_leading_cases"]+=int("direct_leading_evidence" in case)
                    doc["reused_first_forcing_cases"]+=int("first_forcing_evidence" in case)
                    continue
            else:
                case=dict(exact_input_auxiliary_radius=str(Ra),exact_fold_radius=str(R),
                    exact_coefficient_width=str(WIDTH),exact_old_leading_width=str(SG),
                    complete=False,proved=False,attempt_complete=False,failure=None,gates=[])
                doc["cases"].append(case)
            def check(name,truth):
                passed=bool(truth);case["gates"].append(dict(name=name,passed=passed))
                if not passed:raise CaseGateFailure(name)
            doc["last_attempted_case"]=ci;checkpoint()
            try:
                if "coefficient_evidence" in case:
                    c=decode(case["coefficient_evidence"]["complete_coefficient_majorants"])
                    cboxes={k:cb(v) for k,v in case["complete_coefficient_complex_boxes"].items()}
                    doc["reused_coefficient_cases"]+=1
                else:
                    c,cboxes,ce=anchored_coefficients(acase,anchor,R,check)
                    case["coefficient_evidence"]=ce
                    case["complete_coefficient_complex_boxes"]={k:crecord(v) for k,v in cboxes.items()}
                    doc["new_coefficient_cases"]+=1;checkpoint()
                if "fold_evidence" in case:
                    f=decode(case["fold_evidence"]["complete_fold_and_leading_bounds"])
                    doc["reused_fold_cases"]+=1
                else:
                    f,fe=fold_budget(c,cboxes,anchor,R,check)
                    case["fold_evidence"]=fe;doc["new_fold_cases"]+=1;checkpoint()
                if "direct_leading_evidence" in case:
                    le=case["direct_leading_evidence"]
                    av={tuple(map(int,k.split(","))):box(v) for k,v in le["direct_a0_ordinary_derivatives"].items()}
                    bv={tuple(map(int,k.split(","))):box(v) for k,v in le["direct_b0_ordinary_derivatives"].items()}
                    chain=decode(le["full_direct_fold_chain"])
                    doc["reused_direct_leading_cases"]+=1
                else:
                    av,bv,chain,le=direct_leading(c,f,R,check)
                    case["direct_leading_evidence"]=le
                    doc["new_direct_leading_cases"]+=1;checkpoint()
                if "first_forcing_evidence" in case:
                    doc["reused_first_forcing_cases"]+=1
                else:
                    case["first_forcing_evidence"]=forced_case(av,bv,chain,c,f,R,roots,original_cell,scalar_cell,check)
                    doc["new_first_forcing_cases"]+=1;checkpoint()
                case.update(complete=True,proved=True,attempt_complete=True)
            except CaseGateFailure as error:
                case.update(complete=False,proved=False,attempt_complete=True,
                    failure=dict(type=type(error).__name__,message=str(error)))
            checkpoint()
        doc["complete"]=(len(doc["cases"])==len(RADII) and all(x["attempt_complete"] for x in doc["cases"]))
        doc["proved"]=(doc["complete"] and all(x["proved"] for x in doc["cases"]))
        doc.pop("last_attempted_case",None)
        if not doc["proved"]:
            raise RuntimeError("one or more proposed new anchored cases failed; every accepted prefix is retained")
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            cases=len(doc["cases"]),native_sha256=sha(args.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
