#!/usr/bin/env python3
"""Complete common-radial reference potential from immutable successful root data.

New scalar ball algebra runs only in the public Actions repository. Original
target, FFT, intrinsic derivatives, characteristic coefficients and Fourier
polynomials are read byte-for-byte. Reproducible work files stay temporary;
only a small actual conclusion and its execution receipt may be published.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,acb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L

PUBLIC="Rogerhu12/math-research-public"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ALGEBRA="9eb4b99b9a6b569233a3b7c3da80da7d2738c4f0bd18040654ff5b7beace2d4b"
CONTRACT="cae161da962d9dc6e8f53934ebdf5b2410f75718439736f1b61d673ed6fe6fe5"
HIGHER="ec702cffb8d1dcb25cdb01eaa89127b1f0044ae1cd3cee9e6e293e8165250480"
HPROC="c7ff69243d3f724f539cd0ee95c2b0ba219caa5ffba47ff9b084387255e78e5b"
INTRINSIC="6276b4b8bd117b3092ce633b7164ff99968100f10b09cbaef8850d4c03f6b24f"
IPROC="a6783642ae2c49f66c3a7b54f1506389f24771790f3bd5a324646df8229f9728"
TAYLOR="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
TPROC="42ab23b97ce922b042b8291af46cfe8c44ffd7e90ba1e2a6049caef263b7224e"
TSOURCE="42048094f7c5e0ba3b83f10e9e6fcbc5cd4c5b3d67057f69241409a5a4be87a1"
TMANIFEST="5700ded5038d500d14f43dfa69994665d2688f220de155128fff1fec6286e3a5"
OLD_SOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
OLD_MANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"
BACKGROUND="a6f89d9bf9523d04fd0534f7224b7a8bb3ecc8b0b201ffccf3839585df56b0c8"
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
ROOTPIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
RC=Q(1,2000);SG=Q(3,128);RG=Q(3,8000);DELTA=Q(1,10**8)
SUPPORT_RADII=(Q(3,8000),Q(1,4000))
RADII=(Q(9,10**6),Q(1,20000),Q(1,10000),Q(1,6000))
CUTOFF=97;Z=Q(1,CUTOFF*CUTOFF);I=acb(0,1)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def jhash(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def save(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    b=(json.dumps(x,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":b=gzip.compress(b,compresslevel=6,mtime=0)
    t=p.with_name(p.name+".partial");t.write_bytes(b);t.replace(p)
def ex(q):return L.ex(Q(q))
def up(x):
    if isinstance(x,(int,Q)):x=ex(x)
    return abs(x).upper()
def rb(v):
    if isinstance(v,str):return arb(v)
    if isinstance(v,(int,Q)):return ex(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def rec(v):return dict(ball=L.rec(v,64))
def crec(z):return dict(real=rec(z.real),imag=rec(z.imag))
def unpack(x):
    if isinstance(x,dict):
        if set(x)=={"ball"}:return arb(x["ball"])
        return {k:unpack(v) for k,v in x.items()}
    if isinstance(x,list):return [unpack(v) for v in x]
    return x
def positive(x,label):
    x=arb(x)
    if not (x.is_finite() and x.lower()>0):raise ValueError(label+" lacks a strictly positive complete lower bound")
    return x
def inflate(z,r):
    r=up(r)
    return acb(z)+acb(arb(0,r),arb(0,r))
def ipow(z,n):
    if n<0:raise ValueError("negative integer power must keep its exact complete denominator")
    y=z*0+1
    for _ in range(n):y*=z
    return y
def jconst(v,count):return [acb(v)]+[acb(0) for _ in range(count-1)]
def take(v,count):
    if len(v)<count:raise ValueError("an unpaid Taylor coefficient was requested")
    return list(v[:count])
def jadd(a,b,count):return [a[k]+b[k] for k in range(count)]
def jsub(a,b,count):return [a[k]-b[k] for k in range(count)]
def jscale(a,v,count=None):
    if count is None:count=len(a)
    return [a[k]*v for k in range(count)]
def jmul(a,b,count):
    take(a,count);take(b,count)
    return [sum((a[k]*b[n-k] for k in range(n+1)),acb(0)) for n in range(count)]
def jdr(a):return [(k+1)*a[k+1] for k in range(len(a)-1)]
def jinv(a,count):
    take(a,count)
    if a[0].contains(0):raise ValueError("a complete reciprocal denominator contains zero")
    y=[1/a[0]]
    for n in range(1,count):
        y.append(-y[0]*sum((a[k]*y[n-k] for k in range(1,n+1)),acb(0)))
    return y
def jpow(a,p,count):
    take(a,count);p=Q(p)
    if not a[0].real>0:raise ValueError("the root-positive holomorphic power branch is unresolved")
    y=[(a[0].log()*acb(ex(p))).exp()]
    for n in range(1,count):
        q=ex(p*n)*a[n]*y[0]
        for k in range(1,n):q+=ex((p+1)*k-n)*a[k]*y[n-k]
        y.append(q/(n*a[0]))
    return y
def jdiv(a,b,count):return jmul(a,jinv(b,count),count)
def jlogder(a,count):return jdiv(jdr(a),a,count)

def derivative_tail(M,R,H,p,n0):
    """Complete omitted coefficients n>=n0 using a paid third derivative."""
    t=ex(H/R);one=1-t
    positive(one,"Cauchy radial margin")
    if p==0:c=1/(n0*(n0-1)*(n0-2)*one)
    elif p==1:c=1/((n0-1)*(n0-2)*one)
    elif p==2:c=1/((n0-2)*one)
    elif p==3:c=1/one
    elif p==4:c=(n0-3)/one+t/(one*one)
    elif p==5:
        c=(n0-3)*(n0-4)/one+(2*n0-7)*t/(one*one)+t*(1+t)/(one*one*one)
    else:raise ValueError("only the proved complete derivative orders zero through five are used")
    return up(M*ex(R**(3-p))*ipow(t,n0-p)*c)
def k_tail(M,R,H,p):
    t=ex(H/R);one=1-t
    positive(one,"root quotient Cauchy radial margin")
    if p==0:c=1/(16*15*14*one)
    elif p==1:c=1/(16*14*one)
    elif p==2:c=1/(16*one)
    elif p==3:c=1/one
    elif p==4:c=10/one+t/(one*one)
    else:raise ValueError("only the proved complete k orders zero through four are used")
    return up(M*ex(R**(2-p))*ipow(t,15-p)*c)
def disk_jet(coeff,H,count,tails=None):
    """Enclose f^(p)(x)/p! on the true disk |x|<=H, not its larger square.

    The finite constant coefficient remains signed. Each nonconstant term is
    bounded by its modulus on that disk before rectangular ball inflation.
    """
    if len(coeff)<count:raise ValueError("incomplete original polynomial support")
    hh=ex(H);out=[]
    for p in range(count):
        radius=arb(0)
        for n in range(p+1,len(coeff)):
            radius+=up(coeff[n])*math.comb(n,p)*ipow(hh,n-p)
        if tails is not None:radius+=tails[p]/math.factorial(p)
        out.append(inflate(coeff[p],radius))
    return out
def scalar_coefficients(raw,key):
    return [acb(rb(raw[key][n]))/math.factorial(n) for n in range(16)]
def scalar_jets(raw,third,key,H,count):
    cs=scalar_coefficients(raw,key)
    if key=="K":
        if not cs[0].contains(0):raise ValueError("the original exact K0 identity is absent")
        cs[0]=acb(0)
    tails=[derivative_tail(third[key],RC,H,p,16) for p in range(count)]
    return disk_jet(cs,H,count,tails)
def background_jets(raw,third,background,H,count=5):
    f={k:scalar_jets(raw,third,k,H,max(count,4)) for k in ("K","beta","gamma","s")}
    kc=[acb(rb(raw["K"][n+1]))/math.factorial(n+1) for n in range(15)]
    kk=disk_jet(kc,H,count,[k_tail(third["K"],RC,H,p) for p in range(count)])
    u={};v={}
    for mode in range(-96,97):
        cu=[background["u"][p].coefficient(mode)*((-1)**p) for p in range(4)]
        cv=[background["v"][p].coefficient(mode)*((-1)**p) for p in range(4)]
        cu+= [acb(0)]*max(0,count-len(cu))
        if mode==0:
            for p in range(4):cv[p]-=acb(rb(raw["s"][p]))/math.factorial(p)
        cv+=[acb(0)]*max(0,count-len(cv))
        u[mode]=disk_jet(cu,H,count)
        v[mode]=disk_jet(cv,H,count)
        if mode==0:v[mode]=jadd(v[mode],f["s"],count)
    if any(not z.contains(0) for z in u[0]):
        raise ValueError("the complete odd u mean identity is absent")
    # This is the exact original reflection-class identity, not a finite truncation.
    u[0]=[acb(0) for _ in range(count)]
    eta=jscale(jmul(f["gamma"],v[0],count),-1)
    return dict(intrinsic=f,k=kk,u=u,v=v,eta=eta)
def a_third_support(raw,third,background,H):
    c=background_jets(raw,third,background,H,4)
    a=jmul(c["eta"],jpow(c["k"],Q(1,2),4),4)
    positive(c["k"][0].real,"k on the supporting complex disk")
    positive(c["eta"][0].real,"eta on the supporting complex disk")
    return dict(exact_radius=str(H),a_third_modulus_upper=rec(up(6*a[3])),
        k_real_lower=rec(c["k"][0].real.lower()),eta_real_lower=rec(c["eta"][0].real.lower()),
        original_zero_through_fifteen_jets_recomputed=False,
        complete_complex_delta_square_retained=True)

def full_frequency_fields(c,z,count=5):
    f=c["intrinsic"];u=c["u"];v=c["v"]
    uu=jmul(u[0],u[0],count);vv=jmul(v[0],v[0],count)
    du=jconst(0,count);dv=jconst(0,count);mix=jconst(0,count)
    for mode in range(1,97):
        den=1-mode*mode*z
        if not den.real>0:raise ValueError("a full intermediate primitive denominator lost its gap")
        pu=jmul(u[mode],u[-mode],count);pv=jmul(v[mode],v[-mode],count)
        uu=jadd(uu,jscale(pu,2),count);vv=jadd(vv,jscale(pv,2),count)
        du=jadd(du,jscale(pu,2*mode*mode*z/den),count)
        dv=jadd(dv,jscale(pv,2*mode*mode*z/den),count)
        mix=jadd(mix,jscale(jmul(u[mode],v[-mode],count),mode/den),count)
    alpha=jscale(jmul(f["beta"],mix,count),-I)
    kvv=jmul(f["K"],vv,count)
    em=jscale(jmul(f["beta"],jadd(jconst(1,count),jadd(jscale(uu,3),kvv,count),count),count),-1)
    bm=jmul(f["beta"],jsub(jconst(1,count),jadd(uu,jscale(kvv,3),count),count),count)
    E=jsub(em,jscale(jmul(f["beta"],du,count),2),count)
    B=jsub(bm,jscale(jmul(jmul(f["beta"],f["K"],count),dv,count),2),count)
    D=jsub(E,B,count)
    theta=jscale(jdiv(alpha,c["eta"],count),z)
    finite_a=jadd(c["eta"],jscale(alpha,z),count)
    return dict(alpha=alpha,E=E,B=B,D=D,theta=theta,a=finite_a,
        mean_u2=uu,mean_v2=vv,Duu=du,Dvv=dv)

def potential_case(raw,third,background,a_coeff,support,old_fold,H):
    R=Q(support["exact_radius"])
    if not H<R:raise ValueError("the complete Abar Taylor tail has no positive radial margin")
    c=background_jets(raw,third,background,H,5)
    # Abar^(3) is at most (1/3) a_infinity^(3) on the same supporting disk.
    M3=up(rb(support["a_third_modulus_upper"])/3)
    abar_coeff=[a_coeff[p]*ex(Q(3,2*p+3)) for p in range(15)]
    abar=disk_jet(abar_coeff,H,5,[derivative_tail(M3,R,H,p,15) for p in range(5)])
    positive(c["k"][0].real,"k on the complete case disk")
    positive(c["eta"][0].real,"eta on the complete case disk")
    positive(abar[0].real,"Abar on the complete case disk")
    # This square contains the entire proved z disk and every j^-2, |j|>=97.
    z=acb(arb(0,ex(Z)),arb(0,ex(Z)))
    qf=full_frequency_fields(c,z,5)
    one_theta=jadd(jconst(1,5),qf["theta"],5)
    if one_theta[0].contains(0):raise ValueError("the full finite-frequency 1+theta gap failed")
    eta_log=jlogder(c["eta"],4)
    k_log=jlogder(c["k"],4)
    A_log=jlogder(abar,4)
    theta_log=jdiv(jdr(qf["theta"]),one_theta,4)
    ell=jsub(jadd(eta_log,jscale(k_log,ex(Q(1,2))),4),jscale(A_log,ex(Q(1,3))),4)
    q=jadd(jadd(take(qf["D"],4),eta_log,4),theta_log,4)
    cjet=jsub(jsub(jsub(jscale(k_log,ex(Q(1,4))),jscale(A_log,ex(Q(1,6))),4),
        jscale(qf["D"],ex(Q(1,2)),4),4),jscale(theta_log,ex(Q(1,2))),4)
    Ljet=jadd(ell,q,4)
    F=jscale(jmul(c["intrinsic"]["K"],
        jadd(jscale(jmul(c["eta"],qf["alpha"],3),2),
             jscale(jmul(qf["alpha"],qf["alpha"],3),z),3),3),16)
    W=jsub(jadd(jscale(jdr(cjet),-1),
        jscale(jmul(cjet,Ljet,3),ex(Q(1,2))),3),F,3)
    kappa=(c["eta"][0]*(c["k"][0].log()/2).exp()
        *(abar[0].log()*acb(ex(Q(-1,3)))).exp())
    if kappa.contains(0):raise ValueError("the complete common T derivative contains zero")
    kapstar=(a_coeff[0].log()*acb(ex(Q(2,3)))).exp()
    if not kapstar.real>0:raise ValueError("the original common root normalization is unresolved")
    V=W[0]/(kappa*kappa)
    VT=(W[1]-2*ell[0]*W[0])/(kappa*kappa*kappa)
    VTT=(2*W[2]-5*ell[0]*W[1]+(6*ell[0]*ell[0]-2*ell[1])*W[0])/ipow(kappa,4)
    var=up(kappa/kapstar-1)
    positive(1-var,"complete common T univalence margin")
    image=((1-var)*abs(kapstar).lower()*ex(H)).lower()
    positive(image,"complete common T image radius")
    Ap=up(old_fold["Ap"])
    if not Ap>0:raise ValueError("the original complete old-fold A upper bound is invalid")
    Ap23=(Ap.log()*ex(Q(2,3))).exp()
    # A factor two leaves a strict image margin for closed output domains.
    old_rho=(image/(2*Ap23)).lower()
    if old_rho>ex(RG):old_rho=ex(RG).lower()
    old_root_cover=max(ROOTS[1]-ROOTPIECE[0],ROOTPIECE[1]-ROOTS[0])
    BminusC=qf["B"][0]-cjet[0]
    G=up((ex(H)*up(BminusC)).exp())
    kaplo=abs(kappa).lower()
    positive(kaplo,"complete common T modulus lower bound")
    values=dict(V=V,V_T=VT,V_TT=VTT,c=cjet[0],c_r=cjet[1],c_rr=2*cjet[2],
        c_rrr=6*cjet[3],ell=ell[0],ell_r=ell[1],q=q[0],D=qf["D"][0],
        alpha=qf["alpha"][0],eta=c["eta"][0],k=c["k"][0],Abar=abar[0],
        kappa=kappa,W=W[0],W_r=W[1],W_rr=2*W[2],B_minus_c=BminusC)
    return dict(exact_complex_radial_radius=str(H),exact_support_radius=str(R),
        exact_complex_z_square_halfwidth=str(Z),all_integer_modes_abs_j_at_least=97,
        physical_angular_frequency="4j",both_carrier_signs_retained=True,
        exact_complex_delta_square_halfwidth=str(DELTA),fixed_intrinsic_parameter="eta_0",
        whole_complex_bilinear_family=True,physical_mean_is_not_z_zero_limit=True,
        potential_and_intermediate_complete_balls={k:crec(v) for k,v in values.items()},
        complete_modulus_upper={k:rec(up(v)) for k,v in values.items()},
        complete_gaps=dict(k_real_lower=rec(c["k"][0].real.lower()),
            eta_real_lower=rec(c["eta"][0].real.lower()),
            Abar_real_lower=rec(abar[0].real.lower()),kappa_modulus_lower=rec(kaplo),
            one_plus_theta_modulus_lower=rec(abs(one_theta[0]).lower()),
            full_primitive_intermediate_denominator_lower=rec(ex(Q(193,9409))),
            common_T_relative_derivative_upper=rec(var)),
        reference_image=dict(complete_image_disk_radius_lower=rec(image),
            guaranteed_old_fold_rho_radius_lower=rec(old_rho),
            old_fold_phi_width=str(SG),old_fold_original_radius=str(RG),
            exact_whole_physical_root_cover_radius=str(old_root_cover),
            entire_original_physical_root_piece_covered=bool(ex(old_root_cover)<old_rho),
            actual_old_phi_common_domain_only=True,
            old_fold_on_other_physical_cubics_identified_with_root_extension=False),
        gauge_and_complete_two_source_bounds=dict(
            G_and_G_inverse_modulus_upper=rec(G),
            G_r_modulus_upper=rec(up(up(BminusC)*G)),
            G_rr_modulus_upper=rec(up(up(qf["B"][1]-cjet[1]+BminusC*BminusC)*G)),
            g2_to_U_T=rec(up(G/kaplo)),
            g1_to_P_T_per_unit_n=rec(up(up(qf["a"][0])*G/(kaplo*kaplo))),
            g2_to_P_T=rec(up(up(cjet[0])*G/(kaplo*kaplo))),
            ordinary_g2_radial_derivative_used=False),
        independent_even_mean_equation_retained=True,
        actual_reference_seam_jumps_retained=True,
        actual_reference_columns_Y_and_YT_bound=False,
        old_circle_HV_inverse_paid=False,full_high_BVP_inverse_paid=False)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","out-dir"):ap.add_argument("--"+key,type=Path,required=True)
    ap.add_argument("--manifest-sha",required=True)
    args=ap.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new scalar potential mathematics runs only in the public Actions repository")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the exact reviewed scientific runtime changed")
    ctx.prec=320;ctx.cap=4
    args.out_dir.mkdir(parents=True,exist_ok=True)
    path=args.out_dir/"process.json";native=args.out_dir/"temporary-common-radial-potential.json.gz"
    start=time.monotonic()
    doc=dict(kind="actual_complete_common_radial_potential_budget",public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),algebra_sha256=sha(L.__file__),
        input_manifest_sha256=sha(args.manifest),runtime=runtime,complete=False,proved=False,
        actual_returncode=None,failure=None,gates=[],support_cases=[],cases=[],
        original_target_FFT_intrinsic_or_point_derivatives_recomputed=0,
        original_saved_characteristic_or_Fourier_coefficients_recomputed=0,
        original_reproducible_inputs_modified=0,new_scalar_potential_cases=0,
        original_mean_and_reference_interface_conditions_retained=True,
        full_reference_columns_or_high_inverse_claimed=False,
        reproducible_data_published_to_repository=False,
        reproducible_data_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def checkpoint():
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-start
        save(native,doc)
    def gate(name,condition):
        ok=bool(condition);doc["gates"].append(dict(name=name,passed=ok));checkpoint()
        if not ok:raise ValueError(name)
    try:
        manifest=read(args.manifest)
        gate("the new source, complete algebra and manifest have their exact reviewed identities",
            doc["input_manifest_sha256"]==args.manifest_sha and doc["algebra_sha256"]==ALGEBRA
            and manifest["public_repository"]==PUBLIC
            and doc["source_sha256"]==manifest["scientific_source_sha256"]
            and manifest["mathematical_parameters"]["exact_radial_radii"]==list(map(str,RADII))
            and manifest["mathematical_parameters"]["support_radii"]==list(map(str,SUPPORT_RADII)))
        for f in manifest["files"]:
            p=args.repo/f["path"]
            if not p.is_file() or p.stat().st_size!=f["bytes"] or sha(p)!=f["sha256"]:
                raise ValueError("an immutable scientific input changed: "+f["path"])
        paths={k:args.repo/v for k,v in manifest["input_paths"].items()}
        gate("all exact immutable historical inputs and the current proof were verified",
            sha(paths["contract"])==CONTRACT and sha(paths["higher_native"])==HIGHER
            and sha(paths["higher_process"])==HPROC and sha(paths["intrinsic_domain_native"])==INTRINSIC
            and sha(paths["intrinsic_domain_process"])==IPROC and sha(paths["Taylor_native"])==TAYLOR
            and sha(paths["Taylor_process"])==TPROC and sha(paths["background_stage"])==BACKGROUND
            and sha(paths["old_fold_majorants_stage"])==MAJORANTS
            and sha(paths["adjacent_process"])==APROC and sha(paths["adjacent_publication"])==APUB)
        high,hproc,ind,iproc,tn,tp=[read(paths[k]) for k in
            ("higher_native","higher_process","intrinsic_domain_native","intrinsic_domain_process",
             "Taylor_native","Taylor_process")]
        gate("the original higher and complete Taylor runs really succeeded without recomputing old stages",
            high["complete"] and high["proved"] and high["failure"] is None
            and hproc["actual_returncode"]==0 and hproc["native_sha256"]==HIGHER
            and tn["complete"] and tn["proved"] and tn["failure"] is None
            and tn["source_sha256"]==TSOURCE and tn["input_manifest_sha256"]==TMANIFEST
            and tn["runtime"]==runtime and tn["algebra_sha256"]==ALGEBRA
            and tn["actual_intrinsic_parameter"]=="eta_0"
            and Q(tn["exact_complex_delta_radius"])==DELTA
            and tp["actual_returncode"]==0 and tp["native_sha256"]==TAYLOR
            and tp["scientific_metadata"]["exact_root_interval"]==list(map(str,ROOTS))
            and tp["scientific_metadata"]["exact_original_physical_piece_interval"]==list(map(str,ROOTPIECE))
            and all(g["passed"] for g in high["gates"]+tn["gates"]))
        icase=next(v for v in ind["cases"] if Q(v["exact_auxiliary_radius"])==RC)
        rect=icase["exact_complex_rectangle"]
        gate("the whole true-root disk remains inside the original successful complex intrinsic rectangle",
            icase["complete"] and icase["proved"] and icase["failure"] is None
            and Q(rect["real_interval"][0])<=ROOTS[0]-RC
            and Q(rect["real_interval"][1])>=ROOTS[1]+RC
            and Q(rect["imaginary_half_width"])>=RC
            and iproc["native_sha256"]==INTRINSIC
            and Q(iproc["cases"][1]["exact_auxiliary_radius"])==RC
            and iproc["cases"][1]["proved"] and iproc["cases"][1]["failure"] is None
            and high["intrinsic_stage"]["complete"]
            and high["at_the_certified_true_root"]["exact_K0"]=="0")
        raw=high["intrinsic_stage"]["ordinary_old_radial_jets"]
        third={k:up(rb(iproc["cases"][1]["complete_intrinsic"]["ordinary_jet_modulus_upper"][k][3]))
            for k in ("K","beta","gamma","s")}
        bs=read(paths["background_stage"])
        old_entry=tn["original_stages"]["complete-background-root-series"]
        gate("the exact old nine-coefficient background keeps both repaired means and its old header",
            bs["complete"] and bs["stage"]=="complete-background-root-series"
            and bs["source_sha256"]==OLD_SOURCE and bs["input_manifest_sha256"]==OLD_MANIFEST
            and bs["algebra_sha256"]==ALGEBRA and bs["runtime"]==runtime
            and old_entry["sha256"]==BACKGROUND and old_entry["bytes"]==paths["background_stage"].stat().st_size
            and bs["payload"]["complete_mean_at_all_orders_retained"]
            and bs["payload"]["positive_order_value_repair_derivatives_exactly_zero"])
        background={k:L.unpack_series(v) for k,v in bs["payload"]["series"].items()}
        gate("the complete original 65 and 193 Fourier slots and all old coefficients are retained",
            all(len(v)==9 for v in background.values())
            and all(v.degree<=96 for v in background["u"]+background["v"])
            and len(raw["K"])==len(raw["beta"])==len(raw["gamma"])==len(raw["s"])==16
            and all(v.scalar_value().is_finite() for v in background["a"]))
        a_coeff=[v.scalar_value()*((-1)**p) for p,v in enumerate(background["a"])]
        pub=read(paths["Taylor_publication"]);published={v["file"]:v for v in pub["files"]}
        for degree in range(9,15):
            name="background-main-degree-"+str(degree).zfill(3);p=paths["background_main_"+str(degree)]
            r=tn["stages"][name];old=read(p);receipt=published["consumers/"+r["file"]]
            gate("the original characteristic coefficient degree"+str(degree)+" is read without reevaluation",
                old["complete"] and old["stage"]==name and old["stage_kind"]=="new_output"
                and old["source_sha256"]==TSOURCE and old["input_manifest_sha256"]==TMANIFEST
                and old["algebra_sha256"]==ALGEBRA and old["runtime"]==runtime
                and r["sha256"]==sha(p) and r["bytes"]==p.stat().st_size
                and receipt["sha256"]==r["sha256"] and receipt["bytes"]==r["bytes"]
                and old["payload"]["degree"]==degree)
            a_coeff.append(L.LP.restore(old["payload"]["a"]).scalar_value()*((-1)**degree))
        ms=read(paths["old_fold_majorants_stage"])
        ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        mr=next(v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz")
        # This stage is one of the explicitly retained old28, with its original header.
        gate("the old whole-product fold bound keeps its unique original accepted identity",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and mr["bytes"]==paths["old_fold_majorants_stage"].stat().st_size
            and mr["sha256"]==MAJORANTS and ap["actual_returncode"]==0
            and ap["mathematical_complete"] and ap["mathematical_proved"]
            and ap["mathematical_failure"] is None and au["complete"]
            and ms["payload"]["majorants"]["A"][1:]==[str(RG),str(SG)])
        old_fold=unpack(ms["payload"])["fold"]
        support=None
        for R in SUPPORT_RADII:
            ans=dict(exact_radius=str(R),proved=False,failure=None)
            try:
                result=a_third_support(raw,third,background,R)
                ans.update(result);ans["proved"]=True
                if support is None:support=copy.deepcopy(ans)
            except Exception as e:ans["failure"]=type(e).__name__+": "+str(e)
            doc["support_cases"].append(ans);checkpoint()
            if support is not None:break
        gate("one complete wider disk pays the new Abar third-derivative tail",support is not None)
        for H in RADII:
            row=dict(exact_complex_radial_radius=str(H),complete=False,proved=False,failure=None)
            try:
                result=potential_case(raw,third,background,a_coeff,support,old_fold,H)
                row.update(result);row["complete"]=row["proved"]=True
            except Exception as e:row["failure"]=type(e).__name__+": "+str(e)
            doc["cases"].append(row);doc["new_scalar_potential_cases"]+=1;checkpoint()
        gate("every requested complete potential case has its actual successful gap and image gates",
            len(doc["cases"])==len(RADII) and all(v["complete"] and v["proved"] for v in doc["cases"]))
        gate("the physical independent mean and full reference interfaces remain outside the nonzero-mode potential",
            all(v["physical_mean_is_not_z_zero_limit"] and v["independent_even_mean_equation_retained"]
                and v["actual_reference_seam_jumps_retained"] and not v["full_high_BVP_inverse_paid"]
                for v in doc["cases"]))
        doc["complete"]=doc["proved"]=True;doc["actual_returncode"]=0
    except Exception as e:
        doc["failure"]=type(e).__name__+": "+str(e);doc["actual_returncode"]=1
    finally:
        checkpoint()
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True
        # Rule15 is a content rule, independent of the text-size limit. Complete
        # signed intermediate certificates remain in the temporary native only.
        compact={k:v for k,v in doc.items() if k!="cases"}
        compact["cases"]=[]
        for row in doc["cases"]:
            public={k:v for k,v in row.items() if k not in (
                "potential_and_intermediate_complete_balls","complete_modulus_upper")}
            if "complete_modulus_upper" in row:
                public["complete_modulus_upper"]={
                    k:row["complete_modulus_upper"][k]
                    for k in ("V","V_T","V_TT","c","kappa","W")}
            compact["cases"].append(public)
        b=(json.dumps(compact,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(b)>60000:raise ValueError("the actual small process exceeds the reviewed sixty-kilobyte limit")
        save(path,compact)
        lines=["# Actual complete common-radial potential budget","",
            "Public Actions run "+str(doc["run_id"])+"/"+str(doc["run_attempt"])+".",
            "Actual child return code: "+str(doc["actual_returncode"])+".",
            "Source SHA256: "+doc["source_sha256"]+".",
            "Input manifest SHA256: "+doc["input_manifest_sha256"]+".",
            "Original target/FFT/intrinsic/characteristic coefficients recomputed: 0.",
            "All saved outputs below are small conclusions; reproducible work files remain temporary.","",
            "The complete complex-delta square, both carrier signs and all |j| >= 97 are retained.",
            "The physical even mean and actual reference seam conditions remain independent.",
            "No full reference columns, positive Green map, old-circle inverse or high BVP inverse is claimed.","",
            "## Actual supporting domains",""]
        for v in doc["support_cases"]:
            lines+=["- Radius "+v["exact_radius"]+": proved="+str(v["proved"])+", failure="+str(v["failure"])+"."]
        for v in doc["cases"]:
            lines+=["","## Complex radial radius "+v["exact_complex_radial_radius"],"",
                "Complete="+str(v["complete"])+", proved="+str(v["proved"])+", failure="+str(v["failure"])+"."]
            if v["proved"]:
                for k in ("V","V_T","V_TT","c","kappa","W"):
                    lines.append("- Complete modulus upper "+k+": "+v["complete_modulus_upper"][k]["ball"]+".")
                lines+=["","Complete gaps and image/source bounds:","",
                    json.dumps(dict(gaps=v["complete_gaps"],image=v["reference_image"],
                        sources=v["gauge_and_complete_two_source_bounds"]),sort_keys=True)]
        lines+=["","## Actual gates",""]
        lines+=["- "+g["name"]+": "+str(g["passed"])+"." for g in doc["gates"]]
        lines+=["","Actual mathematics seconds: "+repr(doc["actual_mathematical_wall_seconds"])+".",
            "Failure: "+str(doc["failure"])+".",""]
        text="\n".join(lines)
        if len(text.encode())>60000:raise ValueError("the actual conclusion exceeds the reviewed sixty-kilobyte limit")
        (args.out_dir/"conclusion.md").write_text(text,encoding="utf-8")
        print(json.dumps(dict(actual_returncode=doc["actual_returncode"],proved=doc["proved"],
            gates=len(doc["gates"]),new_scalar_potential_cases=doc["new_scalar_potential_cases"],
            original_numerical_stages_recomputed=0,conclusion_sha256=sha(args.out_dir/"conclusion.md"),
            process_sha256=sha(path)),sort_keys=True),flush=True)
    return doc["actual_returncode"]

if __name__=="__main__":sys.exit(main())
