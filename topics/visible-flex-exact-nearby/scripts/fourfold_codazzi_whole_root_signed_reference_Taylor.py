#!/usr/bin/env python3
"""Whole original root-piece signed common-reference forcing and correction.

Read every accepted original Taylor coefficient and its publication identity.
Only the new radial reference, its common-T composition, signed additions,
and complete new derivative bounds are evaluated. The exact first-correction
difference is the scalar Fuchsian integral, so no old transport is solved again.
New arrays are temporary; rule15 permits only the small final conclusions.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,acb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L
import fourfold_codazzi_common_radial_potential_budget as P

PUBLIC="Rogerhu12/math-research-public"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ALGEBRA="9eb4b99b9a6b569233a3b7c3da80da7d2738c4f0bd18040654ff5b7beace2d4b"
POTENTIAL_SOURCE="042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7"
POTENTIAL_MANIFEST="44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437"
POTENTIAL_EXECUTION="d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9"
CONTRACT="c0408ef408c2d5df0a730edb19cb92e710e0ca097bdc98027988d1a853e87c60"
TAYLOR="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
TPROC="42ab23b97ce922b042b8291af46cfe8c44ffd7e90ba1e2a6049caef263b7224e"
TPUB="dc7d7f0fca329f4e16af276ea762ab9316285e803d0816b6b8ec01fe3896e7d3"
TSOURCE="42048094f7c5e0ba3b83f10e9e6fcbc5cd4c5b3d67057f69241409a5a4be87a1"
TMANIFEST="5700ded5038d500d14f43dfa69994665d2688f220de155128fff1fec6286e3a5"
OLD_SOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
OLD_MANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
FA_NORMS="0a06b46b740e721742965002eced73e49b51be36abbf285a21f38c2e9efdef5a"
ROOTS=("1191984371497/5000000000000","2383968743003/10000000000000")
PIECE=("2147184947341121/9007199254740992","4295308144604611/18014398509481984")
H=Q(893368603925465506687,21990232555520000000000000)
RS=Q(3,40000);R0=Q(1,6000);RG=Q(3,8000);SG=Q(3,128);SIGMA=Q(1,128)
DELTA=Q(1,10**8);Z=Q(1,9409);ORDER=12;COUNT=15
WIDTHS=(Q(0),Q(1,1024),Q(1,512))
RADIAL_ORDERS=(0,1,2);ANGULAR_ORDERS=(0,1,2,3)
I=acb(0,1)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def jhash(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def save(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    b=(json.dumps(x,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":b=gzip.compress(b,compresslevel=6,mtime=0)
    q=p.with_name(p.name+".partial");q.write_bytes(b);q.replace(p)
def ex(v):return L.ex(Q(v))
def cv(v):return acb(ex(v)) if isinstance(v,(int,Q)) else acb(v)
def up(v):return abs(cv(v)).upper()
def rb(v):
    if isinstance(v,dict):return arb(v["ball"])
    return arb(v)
def rec(v):return dict(ball=L.rec(v,64))
def crec(v):return dict(real=rec(cv(v).real),imag=rec(cv(v).imag))
def positive(v,name):
    v=arb(v)
    if not v.is_finite() or not v.lower()>0:raise ValueError(name+" lacks a positive full lower bound")
    return v
def ipow(v,n):
    if n<0:raise ValueError("an integer exponent became negative")
    out=v*0+1
    for _ in range(n):out*=v
    return out
def require(v,count):
    if len(v)<count:raise ValueError("an uncomputed original Taylor degree was requested")
def scalar_series(v,count):
    require(v,count);return [x.scalar_value() for x in v[:count]]
def rdr(v):return [-x for x in P.jdr(v)]
def coeff_product(a,b,n):
    require(a,n+1);require(b,n+1)
    return sum((a[k]*b[n-k] for k in range(n+1)),L.LP.zero())
def overlaps(a,b):
    a=cv(a);b=cv(b)
    return a.real.overlaps(b.real) and a.imag.overlaps(b.imag)
def stage_names():
    out=["complete-background-root-series"]
    out+=["leading-complete-"+k for k in ("T","a0","b0")]
    out+=["background-inputs-degree-"+str(p).zfill(3) for p in range(9,15)]
    out+=["background-main-degree-"+str(p).zfill(3) for p in range(9,15)]
    out+=["leading-"+k+"-degree-"+str(p).zfill(3) for k in ("T","a0","b0") for p in range(9,13)]
    out+=["normalized-forcing-degree-"+str(p).zfill(3) for p in range(13)]
    out+=["first-correction-degree-"+str(p).zfill(3) for p in range(13)]
    if len(out)!=54 or len(set(out))!=54:raise AssertionError("the fixed original selection changed")
    return out

def reference_potential_coefficients(c):
    """T5, in old rho coefficients; every displayed r derivative is -d/drho."""
    z=acb(arb(0,ex(Z)),arb(0,ex(Z)))
    intrinsic={k:scalar_series(c[k],COUNT) for k in ("K","beta","gamma","s","eta","k")}
    data=dict(intrinsic=intrinsic,eta=intrinsic["eta"],
        u={j:[a.coefficient(j) for a in c["u"][:COUNT]] for j in range(-96,97)},
        v={j:[a.coefficient(j) for a in c["v"][:COUNT]] for j in range(-96,97)})
    fields=P.full_frequency_fields(data,z,COUNT)
    eta=intrinsic["eta"];k=intrinsic["k"];K=intrinsic["K"]
    ainf=scalar_series(c["a"],COUNT)
    abar=[ainf[p]*ex(Q(3,2*p+3)) for p in range(COUNT)]
    if K[0]!=0:raise ValueError("the accepted exact true-root K0 is not zero")
    etalog=P.jdiv(rdr(eta),eta,14)
    klog=P.jdiv(rdr(k),k,14)
    ablog=P.jdiv(rdr(abar),abar,14)
    theta=fields["theta"]
    den=P.jadd(P.jconst(1,COUNT),theta,COUNT)
    thetalog=P.jdiv(rdr(theta),den,14)
    ell=P.jadd(etalog,P.jscale(klog,ex(Q(1,2))),14)
    ell=P.jsub(ell,P.jscale(ablog,ex(Q(1,3))),14)
    q=P.jadd(P.jadd(fields["D"],etalog,14),thetalog,14)
    cc=P.jsub(P.jscale(klog,ex(Q(1,4))),P.jscale(ablog,ex(Q(1,6))),14)
    cc=P.jsub(cc,P.jscale(fields["D"],ex(Q(1,2)),14),14)
    cc=P.jsub(cc,P.jscale(thetalog,ex(Q(1,2))),14)
    kappa=P.jmul(ainf,P.jpow(abar,Q(-1,3),COUNT),COUNT)
    W=P.jscale(rdr(cc),-1)
    W=P.jadd(W,P.jscale(P.jmul(cc,P.jadd(ell,q,13),13),ex(Q(1,2))),13)
    alpha=fields["alpha"]
    freq=P.jadd(P.jscale(P.jmul(eta,alpha,13),2),
        P.jscale(P.jmul(alpha,alpha,13),z),13)
    W=P.jsub(W,P.jscale(P.jmul(K,freq,13),16),13)
    pot=P.jdiv(W,P.jmul(kappa,kappa,13),13)
    apower=P.jpow(abar,Q(2,3),14)
    bart=[acb(0)]+[-apower[p-1] for p in range(1,15)]
    minimum=min((1-j*j*z).real.lower() for j in range(1,97))
    positive(minimum,"the complete mode-dependent primitive denominators")
    if not all(v.is_finite() for v in pot):raise ValueError("a new signed potential coefficient is nonfinite")
    work=dict(z=L.cpack(z),barA=[L.cpack(x) for x in abar],
        barT=[L.cpack(x) for x in bart],ell=[L.cpack(x) for x in ell],
        q=[L.cpack(x) for x in q],c=[L.cpack(x) for x in cc],
        kappa=[L.cpack(x) for x in kappa],W=[L.cpack(x) for x in W],
        V_of_barT=[L.cpack(x) for x in pot])
    public=dict(complete_intermediate_mode_denominator_lower=rec(minimum),
        exact_complex_z_square_halfwidth=str(Z),all_input_labels_abs_at_least=97,
        intermediate_modes=list(range(1,97)),both_carrier_signs=True,
        no_complex_conjugation=True,rho_to_r_derivative_sign=-1,
        maximum_original_K_derivative=15,new_intrinsic_derivatives_evaluated=0,
        original_radial_speed_series_read_without_recomputation=True,
        degree_zero_potential=crec(pot[0]),
        potential_coefficients_are_not_a_new_ordinary_mean_equation=True)
    return pot,bart,public,work

def inverse_composition_and_integral(pot,bart,T):
    """T18--T20; sigma and the radial Fuchsian integral are the only new series."""
    require(T,13);require(pot,13);require(bart,14)
    if not T[0].is_zero() or bart[0]!=0:raise ValueError("the exact common root was moved")
    if not overlaps(T[1].scalar_value(),bart[1]) or bart[1].contains(0):
        raise ValueError("the shared nonzero first common-T coefficient is absent")
    sigma=[L.LP.zero(),L.LP.one()]
    powers=[[L.LP.zero() for _ in range(13)] for _ in range(13)]
    powers[0][0]=L.LP.one();powers[1][1]=L.LP.one()
    for n in range(2,13):
        for k in range(2,n+1):
            powers[k][n]=sum((sigma[i]*powers[k-1][n-i]
                for i in range(1,n-k+2)),L.LP.zero())
        tail=sum((powers[k][n].scale(bart[k]) for k in range(2,n+1)),L.LP.zero())
        sn=(T[n]-tail).divide_scalar(bart[1])
        sigma.append(sn);powers[1][n]=sn
    composed=[]
    for n in range(13):
        composed.append(sum((powers[k][n].scale(pot[k]) for k in range(n+1)),L.LP.zero()))
    bb=[pot[0]]
    for n in range(1,13):
        rhs=bart[1]*pot[n]
        # The k=n+1 term is exactly zero because b0=v0; it is not a ball subtraction.
        for k in range(2,n+1):
            rhs+=bart[k]*(k*pot[n+1-k]-(2*n+2-k)*bb[n+1-k])
        bb.append(rhs/((2*n+1)*bart[1]))
    bc=[]
    for n in range(13):
        bc.append(sum((powers[k][n].scale(bb[k]) for k in range(n+1)),L.LP.zero()))
    if not overlaps(composed[0].scalar_value(),pot[0]) or not overlaps(bc[0].scalar_value(),pot[0]):
        raise ValueError("the scalar Fuchsian root constant changed")
    return composed,bc,dict(sigma=L.pack_series(sigma),
        radial_integral_b=[L.cpack(x) for x in bb],
        composed_potential=L.pack_series(composed),composed_integral=L.pack_series(bc),
        exact_sigma_zero_and_first=[0,1],exact_root_integral_constant_equals_V0=True,
        no_T_jacobian_multiplied_into_scalar_composition=True)

def signed_new_fields(old,leading,composed,bc):
    count=13
    tb=[coeff_product(leading["T"],leading["b0"],n) for n in range(count)]
    da=[coeff_product(tb,bc,n) for n in range(count)]
    db=[coeff_product(leading["a0"],bc,n) for n in range(count)]
    out=dict(fa=list(old["fa"]),fb=[old["fb"][n]+composed[n] for n in range(count)],
        a1=[old["a1"][n]+da[n] for n in range(count)],
        b1=[old["b1"][n]+db[n] for n in range(count)])
    if any(jhash(a.record())!=jhash(b.record()) for a,b in zip(out["fa"],old["fa"])):
        raise ValueError("the unchanged complete second forcing row was altered")
    return out,dict(delta_a1=L.pack_series(da),delta_b1=L.pack_series(db),
        complete_new_fields={k:L.pack_series(v) for k,v in out.items()},
        exact_canonical_difference_A=0,
        exact_canonical_difference_B="one half integral_0^1 s^(-1/2) V(sT) ds",
        old_normalized_transport_recomputed=False,
        old_correction_relabelled_as_new=False)

def joint_new_coefficient_norms(poly,width):
    ans=[arb(0) for _ in ANGULAR_ORDERS]
    for j,z in enumerate(poly.c,poly.lo):
        term=up(z)*L.fourier_weight(abs(j),str(width))
        for q in ANGULAR_ORDERS:
            ans[q]+=term;term*=4*abs(j)
    return [v.upper() for v in ans]

def angular_sum(delta,q):
    if delta<=0:raise ValueError("a joint Fourier tail requires strictly positive angular loss")
    r=(-4*ex(delta)).exp();d=1-r;positive(d,"angular geometric denominator")
    if q==0:value=(1+r)/d
    elif q==1:value=8*r/(d*d)
    elif q==2:value=32*r*(1+r)/(d*d*d)
    elif q==3:value=128*r*(1+4*r+r*r)/(d*d*d*d)
    else:raise ValueError("the proved angular tail is only requested through three")
    return up(value)

def radial_tail(M,R,p):
    """All degrees n>=13, after p ordinary radial derivatives."""
    if not H<R:raise ValueError("the whole original physical piece exceeds its Cauchy disk")
    t=ex(H/R);d=1-t;positive(d,"complete radial tail margin")
    if p==0:value=ipow(t,13)/d
    elif p==1:value=ipow(t,12)*(13/d+t/(d*d))
    elif p==2:value=ipow(t,11)*(156/d+26*t/(d*d)+2*t*t/(d*d*d))
    else:raise ValueError("only the paid first two radial derivatives are requested")
    return up(M*ex(R**(-p))*value)

def derivative_budget(name,series,norms,width,oldM,newM):
    rows=[];means=[]
    for p in RADIAL_ORDERS:
        oldtail=radial_tail(oldM,R0,p)
        newtail=radial_tail(newM,RS,p) if newM!=0 else arb(0)
        fulltail=oldtail+newtail
        vals=[];finite_vals=[];tail_vals=[]
        for q in ANGULAR_ORDERS:
            finite=arb(0)
            for n in range(p,13):
                finite+=norms[n][q]*ex(Q(math.factorial(n),math.factorial(n-p))*H**(n-p))
            tail=fulltail*angular_sum(SIGMA-width,q)
            finite_vals.append(rec(up(finite)));tail_vals.append(rec(up(tail)))
            vals.append(rec(up(finite+tail)))
        # The unchanged fa uses its already accepted q=0 coefficient norms also
        # for the scalar mean; none of its old norms is reevaluated.
        finite_mean=arb(0)
        for n in range(p,13):
            mm=norms[n][0] if name=="fa" else up(series[n].mean())
            finite_mean+=mm*ex(Q(math.factorial(n),math.factorial(n-p))*H**(n-p))
        means.append(rec(up(finite_mean+fulltail)))
        rows.append(dict(radial_derivative_order=p,
            angular_derivative_orders=list(ANGULAR_ORDERS),
            complete_joint_Wiener_upper=vals,
            signed_finite_sum_upper=finite_vals,complete_two_radius_tail_upper=tail_vals))
    return dict(field=name,exact_output_old_phi_width=str(width),
        complete_mixed_derivative_rows=rows,
        complete_amplitude_mean_radial_derivative_upper=means,
        old_tail_radius=str(R0),added_term_tail_radius=str(RS),
        common_outer_angle_strip=str(SIGMA),
        unchanged_fa_finite_norm_width="3/512" if name=="fa" else None,
        finite_signed_addition_precedes_modulus_and_sum=True,
        joint_sum_of_radial_coefficient_suprema=True,
        full_output_zero_mode_retained=True,
        amplitude_mean_is_not_independent_physical_even_mean=True)

def read_original_payloads(paths,tn,tp,pub,runtime,manifest):
    sm=tp["scientific_metadata"]
    if not (tn["complete"] and tn["proved"] and tn["failure"] is None
        and tn["source_sha256"]==TSOURCE and tn["input_manifest_sha256"]==TMANIFEST
        and tn["runtime"]==runtime and tn["algebra_sha256"]==ALGEBRA
        and tp["actual_returncode"]==0 and tp["native_sha256"]==TAYLOR
        and tp["mathematical_complete"] and tp["mathematical_proved"]
        and tp["mathematical_failure"] is None and tp["original75_stage_bytes_unchanged"]
        and all(v["passed"] for v in tn["gates"])
        and pub["actual_returncode"]==0 and pub["complete"]):
        raise ValueError("the original complete Taylor execution identity changed")
    if not (sm["background_definition_sha256"]==BASE and sm["explicit_direction_definition_sha256"]==ZDEF
        and sm["actual_intrinsic_parameter"]=="eta_0"
        and sm["exact_complex_delta_radius"]==str(DELTA)
        and sm["exact_root_interval"]==list(ROOTS)
        and sm["exact_original_physical_piece_interval"]==list(PIECE)):
        raise ValueError("the original repaired finite family or true physical root changed")
    published={e["file"]:e for e in pub["files"]}
    pins={str(Path(e["path"])):e for e in manifest["files"]}
    ans={};receipts=[]
    for name in stage_names():
        old=name in tn["original_stages"]
        entry=tn["original_stages"][name] if old else tn["stages"][name]
        rel=Path(entry["file"])
        if rel!=Path("stages")/(name+".json.gz"):raise ValueError("an original natural path changed")
        path=paths["Taylor_native"].parent/rel
        pubentry=published["consumers/"+str(rel)]
        matching=[v for k,v in pins.items() if path.as_posix().endswith("/"+k)]
        if len(matching)!=1:raise ValueError("a selected original stage is not uniquely manifest-pinned")
        pin=matching[0]
        if not (path.stat().st_size==entry["bytes"]==pubentry["bytes"]==pin["bytes"]
            and sha(path)==entry["sha256"]==pubentry["sha256"]==pin["sha256"]):
            raise ValueError("an original accepted stage lost its exact bytes")
        saved=read(path);source=OLD_SOURCE if old else TSOURCE;manifestsha=OLD_MANIFEST if old else TMANIFEST
        if not (saved["stage"]==name and saved["complete"]
            and saved["source_sha256"]==source and saved["input_manifest_sha256"]==manifestsha
            and saved["algebra_sha256"]==ALGEBRA and saved["runtime"]==runtime
            and (old or saved["stage_kind"]=="new_output")):
            raise ValueError("an original accepted stage lost its exact scientific header")
        ans[name]=saved["payload"]
        receipts.append(dict(name=name,bytes=entry["bytes"],sha256=entry["sha256"],
            source_sha256=source,input_manifest_sha256=manifestsha,
            payload_sha256=jhash(saved["payload"])))
    bg=ans["complete-background-root-series"]
    if not (bg["complete_mean_at_all_orders_retained"]
        and bg["positive_order_value_repair_derivatives_exactly_zero"]
        and bg["original_65_and_193_rows_retained"] and bg["zero_bump_germ_and_fixed_eta0"]):
        raise ValueError("the original repair and physical mean identities changed")
    c={k:L.unpack_series(v) for k,v in bg["series"].items()}
    for n in range(9,15):
        r=ans["background-inputs-degree-"+str(n).zfill(3)]
        if r["degree"]!=n:raise ValueError("an original background input degree changed")
        for key in ("K","beta","gamma","s","u","v","k"):
            c[key].append(L.LP.restore(r["coefficients"][key]))
        r=ans["background-main-degree-"+str(n).zfill(3)]
        if r["degree"]!=n:raise ValueError("an original radial speed degree changed")
        for key in ("eta","a","S"):c[key].append(L.LP.restore(r[key]))
    leading={}
    for key in ("T","a0","b0"):
        r=ans["leading-complete-"+key]
        if r["name"]!=key:raise ValueError("an original leading series name changed")
        leading[key]=L.unpack_series(r["coefficients"])
        if len(leading[key])!=9:raise ValueError("an original leading prefix is not complete")
        for n in range(9,13):
            r=ans["leading-"+key+"-degree-"+str(n).zfill(3)]
            if r["degree"]!=n or r["name"]!="leading-"+key:
                raise ValueError("an original appended leading coefficient changed")
            leading[key].append(L.LP.restore(r["coefficient"]))
    old={k:[] for k in ("fa","fb","a1","b1")}
    for n in range(13):
        r=ans["normalized-forcing-degree-"+str(n).zfill(3)]
        if r["degree"]!=n:raise ValueError("an original normalized forcing degree changed")
        for key in ("fa","fb"):old[key].append(L.LP.restore(r[key]))
        r=ans["first-correction-degree-"+str(n).zfill(3)]
        if r["degree"]!=n:raise ValueError("an original reconstructed correction degree changed")
        for key in ("a1","b1"):old[key].append(L.LP.restore(r[key]))
    if any(len(c[k])!=15 for k in ("K","beta","gamma","s","u","v","k","eta","a","S")):
        raise ValueError("the complete original degree-fourteen input is absent")
    if any(v.degree>96 for v in c["u"]+c["v"]):
        raise ValueError("an original background complete support changed")
    return c,leading,old,receipts

def read_original_majorants(paths,runtime):
    ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
    if not (ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
        and ap["mathematical_failure"] is None and au["complete"] and au["actual_returncode"]==0):
        raise ValueError("the original complete adjacent-piece execution did not succeed")
    pub={v["file"]:v for v in au["files"]}
    payloads={};receipts=[]
    specs=(("majorants_stage","complete-original-reference-holomorphic-majorants",MAJORANTS,4501),
           ("fa_norms_stage","reference-Fourier-norms-f0-3-512",FA_NORMS,5444))
    for key,name,digest,size in specs:
        path=paths[key];saved=read(path);r=pub["consumers/stages/"+name+".json.gz"]
        if not (sha(path)==r["sha256"]==digest and path.stat().st_size==r["bytes"]==size
            and saved["name"]==saved["stage"]==name and saved["complete"]
            and saved["source_sha256"]==LEGACY_SOURCE and saved["algebra_sha256"]==LEGACY_HELPER
            and saved["input_manifest_sha256"]==LEGACY_MANIFEST and saved["runtime"]==runtime):
            raise ValueError("a uniquely accepted old28 scalar stage lost its original identity")
        payloads[key]=saved["payload"]
        receipts.append(dict(name=name,bytes=size,sha256=digest,payload_sha256=jhash(saved["payload"])))
    majorants={}
    for key,value in payloads["majorants_stage"]["majorants"].items():
        majorants[key]=(up(rb(value[0])),Q(value[1]),Q(value[2]))
    fn=payloads["fa_norms_stage"]
    if not (fn["field"]=="f0" and Q(fn["exact_width"])==Q(3,512)
        and len(fn["norms"])==13 and all(len(v)==9 for v in fn["norms"])
        and fn["full_coefficients_and_all_outputs_retained"]
        and fn["original_finite_coefficients_recomputed"] is False):
        raise ValueError("the unchanged complete second forcing coefficient norms changed")
    fanorms=[[up(rb(v)) for v in row[:4]] for row in fn["norms"]]
    for key in ("f0","f1","w1a","w1b"):
        if majorants[key][1:]!=(R0,SIGMA):
            raise ValueError("an original forcing or correction bound has a different full old product")
    for key in ("a0","b0","T"):
        if majorants[key][1:]!=(RG,SG):raise ValueError("an original leading full product changed")
    return majorants,fanorms,receipts

def current_potential_conclusion(paths,runtime):
    e=read(paths["potential_execution"]);p=e["actual_scientific_receipt"]
    if not (e["complete"] and e["actual_returncode"]==0 and p["complete"] and p["proved"]
        and p["actual_returncode"]==0 and p["failure"] is None
        and e["source_budget_source_sha256"]==p["source_sha256"]==POTENTIAL_SOURCE
        and e["input_manifest_sha256"]==p["input_manifest_sha256"]==POTENTIAL_MANIFEST
        and p["runtime"]==runtime and p["algebra_sha256"]==ALGEBRA
        and all(g["passed"] for g in p["gates"])):
        raise ValueError("the complete common-potential execution identity changed")
    found=[v for v in p["cases"] if Q(v["exact_complex_radial_radius"])==R0]
    if len(found)!=1:raise ValueError("the common-potential disk is not uniquely identified")
    c=found[0];im=c["reference_image"]
    if not (c["complete"] and c["proved"] and c["failure"] is None
        and Q(c["exact_complex_z_square_halfwidth"])==Z
        and Q(c["exact_complex_delta_square_halfwidth"])==DELTA
        and c["fixed_intrinsic_parameter"]=="eta_0" and c["whole_complex_bilinear_family"]
        and c["all_integer_modes_abs_j_at_least"]==97 and c["both_carrier_signs_retained"]
        and Q(im["old_fold_phi_width"])==SG and Q(im["old_fold_original_radius"])==RG
        and Q(im["exact_whole_physical_root_cover_radius"])==H
        and im["entire_original_physical_root_piece_covered"]
        and rb(im["guaranteed_old_fold_rho_radius_lower"]).lower()>ex(RS)
        and H<RS<R0 and SIGMA<SG and max(WIDTHS)<Q(3,512)<SIGMA):
        raise ValueError("the actual common-T image does not cover the new whole-piece product")
    for k in ("k_real_lower","eta_real_lower","Abar_real_lower","kappa_modulus_lower","one_plus_theta_modulus_lower"):
        positive(rb(c["complete_gaps"][k]),"accepted complete potential "+k)
    M=[up(rb(c["complete_modulus_upper"][k])) for k in ("V","V_T","V_TT")]
    public=dict(exact_new_old_rho_radius=str(RS),exact_old_potential_radius=str(R0),
        exact_whole_physical_piece_cover_radius=str(H),exact_old_phi_outer_strip=str(SIGMA),
        old_common_T_inverse_image_lower=c["reference_image"]["guaranteed_old_fold_rho_radius_lower"],
        original_potential_conclusion_run_id=e["run_id"],
        original_potential_execution_sha256=POTENTIAL_EXECUTION,
        complete_Fuchsian_integral_T_derivative_modulus_upper=[rec(M[q]/(2*q+1)) for q in range(3)],
        same_complex_delta_and_z_squares=True,original_complete_potential_bounds_recomputed=False,
        same_reference_T_not_old_r_substituted=True)
    return M,public

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest","out-dir"):parser.add_argument("--"+k,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new whole-piece signed mathematics runs only in the authorized public Actions repository")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),
        python_flint=flint.__version__,numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the exact reviewed public runtime changed")
    ctx.prec=320;ctx.cap=4
    args.out_dir.mkdir(parents=True,exist_ok=True)
    native=args.out_dir/"temporary-whole-root-signed-reference-Taylor.json.gz"
    if native.exists():raise FileExistsError("preserve an earlier actual complete or failed temporary execution")
    started=time.monotonic()
    doc=dict(kind="actual_whole_original_root_piece_signed_reference_Taylor",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),algebra_sha256=sha(L.__file__),
        original_potential_source_sha256=sha(P.__file__),
        input_manifest_sha256=sha(args.manifest),runtime=runtime,
        complete=False,proved=False,actual_returncode=None,failure=None,gates=[],
        original_target_FFT_intrinsic_cubic_or_point_derivatives_recomputed=0,
        original_fold_forcing_or_saved_Taylor_coefficients_recomputed=0,
        original_natural_stage_bytes_modified=0,
        original_complete_Taylor_stages_read=0,original_complete_majorant_or_norm_stages_read=0,
        original_unchanged_fa_coefficient_norms_recomputed=0,old_normalized_transport_recomputed=0,
        new_complete_signed_Taylor_degrees=0,new_complete_whole_piece_width_cases=0,
        new_ordinary_source_or_full_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False,
        cases=[])
    def checkpoint():
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started;save(native,doc)
    def gate(name,value):
        ok=bool(value);doc["gates"].append(dict(name=name,passed=ok));checkpoint()
        if not ok:raise ValueError(name)
    try:
        manifest=read(args.manifest);par=manifest["mathematical_parameters"]
        gate("the new whole-piece proof, original algebra, potential helper and manifest have exact identities",
            doc["input_manifest_sha256"]==args.manifest_sha
            and doc["source_sha256"]==manifest["scientific_source_sha256"]
            and doc["algebra_sha256"]==ALGEBRA
            and doc["original_potential_source_sha256"]==POTENTIAL_SOURCE
            and manifest["public_repository"]==PUBLIC
            and par["Taylor_order"]==ORDER
            and par["exact_new_old_rho_radius"]==str(RS)
            and par["exact_complex_delta_square_halfwidth"]==str(DELTA)
            and par["exact_complex_z_square_halfwidth"]==str(Z)
            and par["exact_output_old_phi_widths"]==list(map(str,WIDTHS))
            and par["radial_derivative_orders"]==list(RADIAL_ORDERS)
            and par["angular_derivative_orders"]==list(ANGULAR_ORDERS))
        for entry in manifest["files"]:
            p=args.repo/entry["path"]
            if not p.is_file() or p.stat().st_size!=entry["bytes"] or sha(p)!=entry["sha256"]:
                raise ValueError("an exact reviewed immutable input changed: "+entry["path"])
        paths={k:args.repo/v for k,v in manifest["input_paths"].items()}
        gate("every exact historical input and the current whole-piece contract was byte-checked",
            sha(paths["contract"])==CONTRACT and sha(paths["Taylor_native"])==TAYLOR
            and sha(paths["Taylor_process"])==TPROC and sha(paths["Taylor_publication"])==TPUB
            and sha(paths["adjacent_process"])==APROC and sha(paths["adjacent_publication"])==APUB
            and sha(paths["potential_execution"])==POTENTIAL_EXECUTION
            and sha(paths["potential_source"])==POTENTIAL_SOURCE)
        tn,tp,pub=[read(paths[k]) for k in ("Taylor_native","Taylor_process","Taylor_publication")]
        c,leading,old,receipts=read_original_payloads(paths,tn,tp,pub,runtime,manifest)
        doc["original_complete_Taylor_stages_read"]=len(receipts)
        doc["original_Taylor_stage_receipts_sha256"]=jhash(receipts)
        doc["temporary_work"]=dict(original_selected_stage_receipts=receipts)
        gate("all54 original complete Taylor stages keep their exact old or extension headers and full payloads",
            len(receipts)==54 and all(len(v)==13 for v in leading.values())
            and all(len(v)==13 for v in old.values())
            and c["K"][0].is_zero()
            and all(c["u"][p].mean()==0 for p in range(COUNT)))
        majorants,fa_norms,smallreceipts=read_original_majorants(paths,runtime)
        doc["original_complete_majorant_or_norm_stages_read"]=len(smallreceipts)
        doc["original_majorant_and_norm_receipts"]=smallreceipts
        gate("the uniquely accepted old28 full-product majorant and unchanged fa norms are consumed without reevaluation",
            len(smallreceipts)==2 and len(fa_norms)==13
            and majorants["a0"][1:]==(RG,SG) and majorants["f0"][1:]==(R0,SIGMA))
        Vbound,domain=current_potential_conclusion(paths,runtime)
        doc["complete_domain_conclusion"]=domain
        gate("the actual common-T image covers Rs3over40000 and the entire original physical root piece",
            H<RS<R0 and
            H==max(Q(ROOTS[1])-Q(PIECE[0]),Q(PIECE[1])-Q(ROOTS[0])))
        gate("the original exact leading root zeros justify only their stated radial factors",
            leading["T"][0].is_zero() and leading["b0"][0].is_zero() and leading["b0"][1].is_zero()
            and overlaps(leading["a0"][0].scalar_value(),1)
            and not leading["T"][1].scalar_value().contains(0))
        pot,bart,radial_public,radial_work=reference_potential_coefficients(c)
        doc["new_radial_reference_conclusion"]=radial_public
        doc["temporary_work"]["new_radial_reference"]=radial_work
        checkpoint()
        composed,bc,composition_work=inverse_composition_and_integral(pot,bart,leading["T"])
        new,signed_work=signed_new_fields(old,leading,composed,bc)
        doc["temporary_work"]["new_composition"]=composition_work
        doc["temporary_work"]["new_signed_correction"]=signed_work
        doc["new_complete_signed_Taylor_degrees"]=13
        doc["new_complete_Fourier_support"]={key:
            [dict(degree=n,first=v.lo,last=v.hi) for n,v in enumerate(values)]
            for key,values in new.items() if key!="fa"}
        gate("the exact scalar Fuchsian integral retains its root constant and both complete signed branches",
            len(pot)==len(composed)==len(bc)==13
            and all(len(v)==13 for v in new.values())
            and overlaps(new["b1"][0].mean(),new["fb"][0].mean())
            and all(jhash(new["fa"][n].record())==jhash(old["fa"][n].record()) for n in range(13)))
        oldM=dict(fa=majorants["f0"][0],fb=majorants["f1"][0],
            a1=majorants["w1a"][0],b1=majorants["w1b"][0])
        newM=dict(fa=arb(0),fb=Vbound[0],
            a1=up(majorants["T"][0]*majorants["b0"][0]*Vbound[0]*ex((RS/RG)**3)),
            b1=up(majorants["a0"][0]*Vbound[0]))
        doc["complete_tail_conclusion"]=dict(
            first_omitted_Taylor_degree=13,
            old_radius=str(R0),new_added_term_radius=str(RS),outer_old_phi_strip=str(SIGMA),
            unchanged_original_full_product_modulus={k:rec(v) for k,v in oldM.items()},
            complete_added_term_full_product_modulus={k:rec(v) for k,v in newM.items()},
            exact_delta_a1_radial_zero_order=3,
            no_radius_scaling_applied_to_other_terms=True,
            no_uncomputed_finite_coefficient_was_set_to_zero=True,
            angular_tails_from_joint_double_Cauchy=True)
        doc["temporary_work"]["new_complete_coefficient_norms"]={}
        for width in WIDTHS:
            norms={"fa":fa_norms}
            for name in ("fb","a1","b1"):
                norms[name]=[joint_new_coefficient_norms(poly,width) for poly in new[name]]
                doc["temporary_work"]["new_complete_coefficient_norms"][name+"@"+str(width)]=[
                    [rec(v) for v in row] for row in norms[name]]
            case=dict(exact_output_old_phi_width=str(width),complete=False,proved=False,
                exact_whole_piece_cover_radius=str(H),
                fields=[derivative_budget(name,new[name],norms[name],width,oldM[name],newM[name])
                    for name in ("fa","fb","a1","b1")])
            case["complete"]=case["proved"]=True;doc["cases"].append(case)
            doc["new_complete_whole_piece_width_cases"]+=1;checkpoint()
        gate("all three whole-piece derivative tables retain the signed finite sums and both complete tails",
            len(doc["cases"])==3 and all(v["complete"] and v["proved"] for v in doc["cases"])
            and all(len(v["fields"])==4 for v in doc["cases"]))
        doc["exact_branch_identity"]=dict(
            same_complex_delta_without_conjugation=True,
            fa_minus="-fa_plus",fb_minus="fb_plus",
            first_correction_a1_minus="-a1_plus",first_correction_b1_minus="b1_plus",
            both_original_reference_columns_and_all_output_modes_retained=True)
        doc["scope"]=dict(
            entire_original_physical_piece2549=True,fixed_intrinsic_parameter="eta_0",
            both_root_sides_with_original_uncertain_root_interval=True,
            new_reference_first_correction_identified_by_exact_integral=True,
            same_T_actual_composition_not_same_old_r_substitution=True,
            same_original_rho_orientation_and_input_frequency=True,
            independent_physical_even_mean_equation_retained=True,
            complete_old_circle_I_J_remainder_retained=True,
            all_actual_physical_and_reference_seam_jumps_retained=True,
            complete_ordinary_source_ports_retained=True,
            complete_new_genuine_reference_source_norm_proved=False,
            full_high_BVP_inverse_proved=False,
            old_first_correction_relabelled_as_new=False,
            original_free_Airy_columns_silently_replaced_on_other_pieces=False)
        gate("the genuine-reference remainder, physical even mean, two source ports and true seams remain explicit obligations",
            doc["scope"]["independent_physical_even_mean_equation_retained"]
            and doc["scope"]["complete_old_circle_I_J_remainder_retained"]
            and doc["scope"]["all_actual_physical_and_reference_seam_jumps_retained"]
            and doc["scope"]["complete_ordinary_source_ports_retained"]
            and not doc["scope"]["complete_new_genuine_reference_source_norm_proved"]
            and not doc["scope"]["full_high_BVP_inverse_proved"])
        doc["complete"]=doc["proved"]=True;doc["actual_returncode"]=0
    except Exception as error:
        doc["failure"]=type(error).__name__+": "+str(error);doc["actual_returncode"]=1
    finally:
        checkpoint()
        compact={k:v for k,v in doc.items() if k not in ("temporary_work","new_complete_Fourier_support")}
        public_cases=[]
        for case in doc["cases"]:
            fields=[]
            for field in case["fields"]:
                v=dict(field)
                v["complete_mixed_derivative_rows"]=[{k:x for k,x in row.items()
                    if k not in ("signed_finite_sum_upper","complete_two_radius_tail_upper")}
                    for row in field["complete_mixed_derivative_rows"]]
                fields.append(v)
            v=dict(case);v["fields"]=fields;public_cases.append(v)
        compact["cases"]=public_cases
        compact["complete_new_Fourier_support_sha256"]=jhash(doc.get("new_complete_Fourier_support",{}))
        compact["temporary_native_sha256"]=sha(native);compact["temporary_native_bytes"]=native.stat().st_size
        compact["temporary_native_is_not_published"]=True
        compact_raw=(json.dumps(compact,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(compact_raw)>60000:raise ValueError("the small whole-piece process exceeds60000 bytes")
        save(args.out_dir/"process.json",compact)
        lines=["# Actual whole original root-piece signed common-reference Taylor bounds","",
            "Public Actions run "+str(doc["run_id"])+"/"+str(doc["run_attempt"])+".",
            "Actual mathematical return code: "+str(doc["actual_returncode"])+".",
            "Source SHA256: "+doc["source_sha256"]+".",
            "Manifest SHA256: "+doc["input_manifest_sha256"]+".",
            "Original targets, FFTs, intrinsic derivatives, repairs, fold and accepted Taylor coefficients recomputed: 0.",
            "Original normalized transport and accepted fa coefficient norms recomputed: 0.",
            "The complete original54 Taylor stages and two accepted scalar/norm stages are consumed by their exact bytes.",
            "New signed coefficient arrays and supporting algebra remain temporary.","",
            "## Exact domain and scope","",
            "- Physical piece2549, original interval ["+", ".join(PIECE)+"].",
            "- Certified original root interval ["+", ".join(ROOTS)+"], fixed eta0 and full original complex delta square1e-8.",
            "- All input |j|>=97, both carrier signs, complete complex z square1/9409, every Fourier output and amplitude mean.",
            "- Whole physical cover radius "+str(H)+"; new common-T composition radius "+str(RS)+".",
            "- Original tail radius "+str(R0)+" and new added-term tail radius "+str(RS)+" are separate.",
            "- Outer old-angle strip "+str(SIGMA)+"; radial derivatives0,1,2 and angular derivatives0,1,2,3.",
            "The new correction is the old correction plus (T b0,a0) times the exact scalar Fuchsian integral of V(T).",
            "No old transport is solved again, and no first correction is merely renamed.",
            "The potential is evaluated at the actual T through the true inverse radial map; no extra Jacobian or second radial sign is inserted.",
            "The independent physical even mean, full old-circle I/J remainder, source ports and actual seam jumps remain.",
            "These are complete amplitude/forcing bounds, not a complete new source norm or high BVP inverse.",""]
        if doc.get("complete_domain_conclusion"):
            d=doc["complete_domain_conclusion"]
            lines+=["## Actual domain and scalar integral conclusions","",
                "- Accepted common-T old-rho image lower bound: "+d["old_common_T_inverse_image_lower"]["ball"]+".",
                "- Complete Fuchsian integral T derivative bounds0,1,2: "+
                    ", ".join(v["ball"] for v in d["complete_Fuchsian_integral_T_derivative_modulus_upper"])+".",
                "The three derivative masses are exactly1,1/3,1/5 on the same star-shaped common-T disk.",""]
        for case in doc["cases"]:
            lines+=["## Output old-angle width "+case["exact_output_old_phi_width"],"",
                "| field | radial order | angular0 | angular1 | angular2 | angular3 |",
                "|---|---|---|---|---|---|"]
            for field in case["fields"]:
                for row in field["complete_mixed_derivative_rows"]:
                    lines.append("| "+field["field"]+" | "+str(row["radial_derivative_order"])+" | "+
                        " | ".join(v["ball"] for v in row["complete_joint_Wiener_upper"])+" |")
            lines+=["","Complete amplitude means (radial derivative orders0,1,2):",""]
            for field in case["fields"]:
                lines.append("- "+field["field"]+": "+
                    ", ".join(v["ball"] for v in field["complete_amplitude_mean_radial_derivative_upper"])+".")
            lines+=["","The unchanged fa finite terms use the accepted3/512 norm; every displayed output width is smaller.",
                "All other finite signed sums are formed before taking moduli. No unrelated upper bounds are subtracted.",""]
        lines+=["## Actual gates",""]+["- "+v["name"]+": "+str(v["passed"])+"." for v in doc["gates"]]
        if doc["failure"]:lines+=["","Actual failure: "+doc["failure"]]
        text="\n".join(lines)+"\n"
        if len(text.encode())>60000:raise ValueError("the small actual conclusion exceeds60000 bytes")
        (args.out_dir/"conclusion.md").write_text(text,encoding="utf-8")
    print(json.dumps(dict(complete=doc["complete"],actual_returncode=doc["actual_returncode"],
        original_complete_Taylor_stages_read=doc["original_complete_Taylor_stages_read"],
        original_complete_majorant_or_norm_stages_read=doc["original_complete_majorant_or_norm_stages_read"],
        old_numerical_enclosures_recomputed=0,
        new_complete_signed_Taylor_degrees=doc["new_complete_signed_Taylor_degrees"],
        new_complete_whole_piece_width_cases=doc["new_complete_whole_piece_width_cases"],
        actual_seconds=doc["actual_mathematical_wall_seconds"]),sort_keys=True),flush=True)
    raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
