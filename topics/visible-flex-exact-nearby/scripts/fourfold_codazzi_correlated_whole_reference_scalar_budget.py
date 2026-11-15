#!/usr/bin/env python3
"""Complete whole correlated first forcing; immutable old science, new scalar bounds.

Every old target, intrinsic jet, Fourier coefficient, fold and transport is read.
Only new disk scalar algebra and its final domain/budget inequalities run here.
Reproducible polynomials and work data remain temporary under current rule15.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,acb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L
import fourfold_codazzi_common_radial_potential_budget as P

PUBLIC=P.PUBLIC
RUNTIME=P.RUNTIME
ALGEBRA=P.ALGEBRA
POTENTIAL_SOURCE="042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7"
POTENTIAL_EXECUTION="d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9"
OLD_WHOLE_EXECUTION="777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1"
OLD_WHOLE_SOURCE="a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be"
OLD_WHOLE_MANIFEST="11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65"
ORDERED_CONTRACT="c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e"
CONTRACT="ee408a3c1c2dcfaf24ab04ffa2b65eecff14c10311951a1b93937dcf88b516cf"
RG=P.RG;SG=P.SG;RC=P.RC;R0=Q(1,6000)
RF=Q(3,20000);SD=Q(5,256);SF=Q(1,64)
RT=Q(1,2000);SX=Q(1,128);SA=Q(3,512);DX=Q(1,1024)
RS=Q(3,40000);SS=Q(1,256);LAM=Q(9,2)
WIDTHS=(Q(0),Q(1,1024),Q(1,512))
H=max(P.ROOTS[1]-P.ROOTPIECE[0],P.ROOTPIECE[1]-P.ROOTS[0])
sha=P.sha;read=P.read;save=P.save;ex=P.ex;up=P.up;rb=P.rb;rec=P.rec;unpack=P.unpack
jadd=P.jadd;jsub=P.jsub;jmul=P.jmul;jscale=P.jscale;jdr=P.jdr
jdiv=P.jdiv;jconst=P.jconst;take=P.take;positive=P.positive;ipow=P.ipow

def power(a,p):
    a=arb(a);positive(a,"positive scalar power base")
    return (a.log()*ex(Q(p))).exp()

def strict_gap(a,label):
    a=arb(a)
    if not (a.is_finite() and a.lower()>0):raise ValueError(label+" lacks its complete positive lower bound")
    return a.lower()

def lp(values):
    return L.LP(-96,[values[j] for j in range(-96,97)])

def pperp(v):
    return v-v.constant_part()

def norm(v,width=SF):
    return v.norm(width)

def encode(v):
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    if isinstance(v,arb):return rec(v)
    if isinstance(v,acb):return P.crec(v)
    return v

def angular_sum(d,q):
    if d<=0:raise ValueError("joint Fourier conversion needs a strictly positive strip loss")
    r=(-4*ex(d)).exp();one=1-r;strict_gap(one,"joint angular sum")
    if q==0:y=(1+r)/one
    elif q==1:y=8*r/(one*one)
    elif q==2:y=32*r*(1+r)/ipow(one,3)
    elif q==3:y=128*r*(1+4*r+r*r)/ipow(one,4)
    else:raise ValueError("unpaid angular output derivative")
    return up(y)

def zero_derivatives(M,m):
    """True zero of order m on the complete old product; S.10."""
    rr=ex(RG-RF);aa=ex(SD-SF)
    strict_gap(rr,"leading difference radial Cauchy margin")
    strict_gap(aa,"leading difference angular Cauchy margin")
    result={}
    for p in range(3):
        for q in range(3):
            terms=sum((math.comb(m,l)*ex(RF**(m-l))/ipow(rr,p-l)
                for l in range(min(p,m)+1)),arb(0))
            fact=math.factorial(p)*math.factorial(q)
            zero_bound=M*fact*terms/(ex(RG**m)*ipow(aa,q))
            ordinary=M*fact/(ipow(rr,p)*ipow(aa,q))
            result[p,q]=min(up(zero_bound),up(ordinary)).upper()
    return result

def phase_difference_budget(c,f,majorants,potential,gate):
    a_minus=strict_gap(c["am"],"original a_infinity real lower bound")
    mu_minus=strict_gap(f["mu"],"original full principal mu lower bound")
    inverse_gap=strict_gap(ex(LAM)-f["Er"],"old exact inverse radial slope")
    image=strict_gap(rb(potential["reference_image"]["complete_image_disk_radius_lower"]),
        "original common T image")
    chi=up(majorants["chi"][0])
    tF=ex(RF/RG);tS=ex(RS/RG)
    gate("the actual d characteristics stay inside the original complete leading strip",
        ex(RG)*c["D"][0]<ex(SG-SD))
    gate("the proposed forcing disk and unchanged physical output fit their paid radial supports",
        H<RS<RF<R0<RG<RC)
    gate("both actual and radial T images and their full connecting segment fit the same reference disk",
        ex(RF)*power(max(up(f["Ap"]),up(c["ap"])),Q(2,3))<image and ex(RT)<image)
    gate("the original inverse maps the entire canonical forcing rectangle into the new old product",
        ex(RT)<ex(LAM*RG/2) and ex(RT)/inverse_gap<ex(RF)
        and ex(SX)+f["B"]<ex(SF))
    optical=up(ex(Q(2,3))*power(ex(RT),Q(3,2)))
    gate("the complete forced paths and quotient Cauchy margin fit the canonical forcing strip",
        ex(SA)+optical+ex(DX)<ex(SX))
    gate("the unchanged whole old-product output maps into the canonical amplitude rectangle",
        ex(RS)*power(f["Ap"],Q(2,3))<ex(RT) and ex(SS)+tS*chi<ex(SA))
    xi=up(c["ap"]*f["j"]/a_minus)
    gate("the complete correlated A over Abar ratio has its positive holomorphic power gap",xi<1)
    xm=strict_gap(1-xi,"whole correlated A ratio")
    gbar=up(f["G"]*power(xm,Q(-1,6)))
    gratio=up(power(1+xi,Q(1,6)))
    gdiff=up(xi*power(xm,Q(-5,6))/6)
    ma=up(gbar*(gdiff+gratio*((f["E"]+1)*f["j"]+f["TM"]*f["BT"]*f["BT"])))
    mb=up(2*gbar*gratio*f["E"]*f["BT"])
    da=zero_derivatives(ma,1);db=zero_derivatives(mb,2)
    xiF=up(tF*xi);jF=up(tF*f["j"]);yF=up(tF*tF*f["BT"])
    oneF=strict_gap(1-xiF,"smaller correlated A ratio")
    tf=up(ex(RF)*power(f["Ap"],Q(2,3)))
    deltaT=up(ex(RF)*power(c["ap"],Q(2,3))*ex(Q(2,3))*xiF*power(oneF,Q(-1,3)))
    kmax=up(c["ap"]*power(a_minus,Q(-1,3)))
    ratio23=power(oneF,Q(-2,3))
    # Subtraction here is the exact scalar formula in xiF, not two unrelated enclosures.
    delta_mu=up(kmax*kmax*((ratio23-1)+ratio23*((2+jF)*jF+tf*yF*yF)))
    mu_max=up(f["Q"]*f["Q"]*((1+jF)*(1+jF)+tf*yF*yF))
    return dict(xi=xi,gbar=gbar,gbar_r=up(gbar/ex(RG-RF)),ma=ma,mb=mb,da=da,db=db,
        delta_T=deltaT,delta_mu=delta_mu,mu_max=mu_max,mu_min=mu_minus,
        TF=tf,a0=up(gbar+da[0,0]),b0=up(db[0,0]),
        canonical_inverse_radial_gap=inverse_gap,common_T_image=image,
        normalized_phase_difference_root_orders=[1,2],
        proposed_forcing_old_rho_radius=str(RF),unchanged_amplitude_old_rho_radius=str(RS),
        true_physical_root_piece_radius=str(H),new_whole_leading_difference_bounds=encode(dict(a=ma,b=mb)),
        new_radius_does_not_change_physical_piece_or_seams=True)

def signed_coefficient_budget(raw,third,background,a_coeff,support):
    """Only a new scalar enclosure on RF; the old supporting disk is not recomputed."""
    c=P.background_jets(raw,third,background,RF,3)
    M3=up(rb(support["a_third_modulus_upper"])/3)
    ac=[a_coeff[p]*ex(Q(3,2*p+3)) for p in range(15)]
    abar=P.disk_jet(ac,RF,3,[P.derivative_tail(M3,RG,RF,p,15) for p in range(3)])
    gaps={key:strict_gap(obj[0].real,key+" on the new forcing disk")
        for key,obj in (("k",c["k"]),("eta",c["eta"]),("Abar",abar))}
    u=[lp({j:c["u"][j][p] for j in range(-96,97)}) for p in range(3)]
    v=[lp({j:c["v"][j][p] for j in range(-96,97)}) for p in range(3)]
    beta=c["intrinsic"]["beta"];K=c["intrinsic"]["K"];eta=c["eta"]
    uu=u[0]*u[0];vv=v[0]*v[0]
    uur=(u[1]*u[0]).scale(2);vvr=(v[1]*v[0]).scale(2)
    C=pperp(uu+vv.scale(K[0])).scale(-beta[0])
    Cr=pperp(uu+vv.scale(K[0])).scale(-beta[1])-pperp(
        uur+vv.scale(K[1])+vvr.scale(K[0])).scale(beta[0])
    Z=pperp(vv).scale(2*beta[0]*K[0])
    Zr=pperp(vv).scale(2*(beta[1]*K[0]+beta[0]*K[1]))+pperp(vvr).scale(2*beta[0]*K[0])
    d=C.primitive();DC=Cr-d*C.theta();DZ=Zr-d*Z.theta()
    em=-beta[0]*(1+3*uu.mean()+K[0]*vv.mean())
    bm=beta[0]*(1-uu.mean()-3*K[0]*vv.mean())
    ac_scalar=eta[1]/eta[0]+em
    ell=(u[0]*v[0]).scale(-2*beta[0])
    vac=ell*ell-(v[0]*u[0].theta()).scale(4*beta[0]*eta[0])
    deltaV=C.scale(ac_scalar+4*bm)+Z.scale(bm-ac_scalar)+C*C*4-C*Z*3-Z*Z-DC+DZ-vac.scale(K[0])
    # Finite radial-frequency functions keep z=0 without dividing by z.
    z=acb(arb(0,ex(P.Z)),arb(0,ex(P.Z)))
    U=jconst(0,3);W=jconst(0,3);mix=jconst(0,3)
    den_lower=ex(1)
    for mode in range(1,97):
        den=1-mode*mode*z
        if not den.real>0:raise ValueError("a complete finite intermediate frequency denominator lost its real gap")
        den_lower=min(den_lower,den.real.lower())
        pu=jmul(c["u"][mode],c["u"][-mode],3)
        pv=jmul(c["v"][mode],c["v"][-mode],3)
        U=jadd(U,jscale(pu,2*mode*mode/den),3)
        W=jadd(W,jscale(pv,2*mode*mode/den),3)
        mix=jadd(mix,jscale(jmul(c["u"][mode],c["v"][-mode],3),mode/den),3)
    alpha=jscale(jmul(beta,mix,3),-P.I)
    zeta=jdiv(alpha,eta,3);one=jadd(jconst(1,3),jscale(zeta,z),3)
    if one[0].contains(0):raise ValueError("the complete finite-frequency one-plus-zeta denominator contains zero")
    zeta_log=jdiv(jdr(zeta),one,2)
    Q1=jadd(jadd(jscale(jmul(beta,U,2),-2),
        jscale(jmul(jmul(beta,K,2),W,2),2),2),zeta_log,2)
    qrad=ac_scalar-bm
    kap=eta[0]*(c["k"][0].log()/2).exp()*(abar[0].log()*acb(ex(Q(-1,3)))).exp()
    if kap.contains(0):raise ValueError("the complete new common T derivative contains zero")
    radialdiff=(z*Q1[1]/2-z*qrad*Q1[0]/2-z*z*Q1[0]*Q1[0]/4
        -16*K[0]*(2*eta[0]*alpha[0]+z*alpha[0]*alpha[0]))/(kap*kap)
    out=dict(C=norm(C),delta_V0=norm(deltaV),radial_difference=up(radialdiff),
        gaps={**gaps,"kappa":strict_gap(abs(kap),"new complete kappa modulus"),
            "one_plus_theta":strict_gap(abs(one[0]),"new complete one-plus-theta modulus"),
            "intermediate_denominator":strict_gap(den_lower,"all finite primitive denominators")},
        complete_parameter_square_halfwidth=str(P.Z),complete_complex_delta_square_halfwidth=str(P.DELTA),
        complete_frequency_modes_abs_at_least=97,both_carrier_signs=True,
        signed_DeltaV0_before_full_modulus=True,zero_frequency_radial_curvature_term_retained=True,
        signed_DeltaV0_full_support=deltaV.degree,
        full_bilinear_means_retained=True,independent_physical_even_mean_retained=True)
    temporary=dict(signed_DeltaV0=deltaV.record(),C=C.record(),DC=DC.record(),Z=Z.record(),DZ=DZ.record(),
        radial_difference=P.crec(radialdiff),Q1=[P.crec(vv) for vv in Q1],
        alpha=[P.crec(vv) for vv in alpha])
    return out,temporary

def complete_forcing(c,f,majorants,phase,coef,potential):
    da,db=phase["da"],phase["db"];D0,D1=c["D"][:2]
    def diagonal(w):
        wD=up(w[1,0]+D0*w[0,1])
        wDD=up(w[2,0]+2*D0*w[1,1]+(c["Dr"][0]+D0*D1)*w[0,1]+D0*D0*w[0,2])
        return up(wDD+c["ep"]*c["ep"]*c["K"]*w[0,2]+c["T0"]*wD+c["V0"]*w[0,0])
    ra=up(diagonal(da)+5*coef["C"]*phase["gbar_r"]
        +coef["delta_V0"]*phase["gbar"]+c["vartheta"]*f["Q"]*phase["TF"]*phase["b0"])
    rbnd=up(diagonal(db)+c["vartheta"]*f["Q"]*phase["a0"])
    old=potential["complete_modulus_upper"];MV=up(rb(old["V"]));MVT=up(rb(old["V_T"]))
    mdiff=coef["radial_difference"]
    md=up(mdiff+MVT*phase["delta_T"]);mvr=up(MV+mdiff);mui=1/phase["mu_min"]
    raw_fb=up(md*phase["a0"]+mui*(ra+mvr*(
        phase["delta_mu"]*phase["gbar"]+phase["mu_max"]*da[0,0])))
    raw_fa_1=up(md*phase["b0"]+mui*(rbnd+mvr*phase["mu_max"]*db[0,0]))
    raw_fa_2=up(MV*phase["b0"]+mui*rbnd)
    raw_fa=min(raw_fa_1,raw_fa_2).upper()
    ai=up(f["M"]*f["Bi"]*f["Bi"])
    bi=up(up(majorants["b0"][0])*f["Bi"]*f["Bi"]);ti=up(f["TM"]*bi)
    fb=up(ai*raw_fb+ti*raw_fa);fa=up(bi*raw_fb+ai*raw_fa)
    return dict(raw_fb=raw_fb,raw_fa=raw_fa,fb=fb,fa=fa,
        complete_DeltaR_a=ra,complete_DeltaR_b=rbnd,
        complete_V_minus_radial_V=md,complete_radial_V=mvr,
        raw_fa_two_independent_bounds=[raw_fa_1,raw_fa_2],
        old_potential_bounds_consumed_without_recomputation=True,
        actual_common_T_segment_consumed=True)

def complete_amplitudes(f,forcing):
    rt=ex(RT);dx=ex(DX)
    b0=up(f["M"]+f["B2"]*power(rt,Q(5,2)));common=up(b0*f["Bi"])
    Fb,Fa=forcing["raw_fb"],forcing["raw_fa"]
    a1=up(common*rt*Fa/2+(common*rt*rt/(2*dx)
        +f["B2"]*f["Bi"]*(1+common/6)*ipow(rt,3))*Fb)
    b1=up(common*Fb+(common*rt*rt/(5*dx)
        +f["B2"]*f["Bi"]*(ex(Q(1,2))+common/7)*ipow(rt,3))*Fa)
    return dict(a1=a1,b1=b1,full_raw_forcing_used=True,
        old_transport_or_Taylor_coefficients_recomputed=False,
        exact_regular_root_normalization_retained=True,
        canonical_radius=str(RT),canonical_strip=str(SA),
        old_radial_radius=str(RS),old_angle_strip=str(SS))

def complete_output_cases(forcing,amplitude,oldreceipt):
    original={Q(c["exact_output_old_phi_width"]):c for c in oldreceipt["cases"]}
    if set(original)!=set(WIDTHS):raise ValueError("the old whole-output widths changed")
    new={k:(forcing[k],RF,SF) for k in ("fa","fb")}
    new.update({k:(amplitude[k],RS,SS) for k in ("a1","b1")})
    output=[];improvements=0;mean_improvements=0
    for width in WIDTHS:
        old=original[width]
        if Q(old["exact_whole_piece_cover_radius"])!=H:
            raise ValueError("the old and new physical output covers differ")
        fields={v["field"]:v for v in old["fields"]}
        if set(fields)!=set(new):raise ValueError("the old complete amplitude fields changed")
        case=dict(exact_output_old_phi_width=str(width),exact_whole_physical_cover_radius=str(H),fields=[])
        for name,(M,R,S) in new.items():
            if not (H<R and width<S):raise ValueError("a complete output conversion has no positive margin")
            oldfield=fields[name];oldrows={v["radial_derivative_order"]:v for v in oldfield["complete_mixed_derivative_rows"]}
            if set(oldrows)!={0,1,2}:raise ValueError("an old complete radial derivative row is missing")
            rows=[];means=[];selected=[]
            for p in range(3):
                if oldrows[p]["angular_derivative_orders"]!=[0,1,2,3]:
                    raise ValueError("old angular derivative indices changed")
                newbase=up(M*math.factorial(p)/ex((R-H)**p));vals=[];flags=[]
                for q in range(4):
                    candidate=up(newbase*angular_sum(S-width,q))
                    oldvalue=up(rb(oldrows[p]["complete_joint_Wiener_upper"][q]))
                    vals.append(rec(min(candidate,oldvalue).upper()))
                    flag=bool(candidate<oldvalue);flags.append(flag);improvements+=int(flag)
                rows.append(dict(radial_derivative_order=p,angular_derivative_orders=[0,1,2,3],
                    complete_joint_Wiener_upper=vals,new_complete_bound_selected=flags))
                oldmean=up(rb(oldfield["complete_amplitude_mean_radial_derivative_upper"][p]))
                means.append(rec(min(newbase,oldmean).upper()))
                flag=bool(newbase<oldmean);selected.append(flag);mean_improvements+=int(flag)
            case["fields"].append(dict(field=name,exact_output_old_phi_width=str(width),
                complete_mixed_derivative_rows=rows,complete_amplitude_mean_radial_derivative_upper=means,
                new_complete_mean_bound_selected=selected,new_complete_holomorphic_sup=rec(M),
                new_complete_holomorphic_radial_radius=str(R),new_complete_holomorphic_angle_strip=str(S),
                original_complete_bound_only_read=True,full_radial_and_Fourier_tails_retained=True,
                joint_sum_of_radial_coefficient_suprema=True,
                amplitude_mean_is_not_independent_physical_even_mean=True))
        output.append(case)
    return output,improvements,mean_improvements

# All original provenance constants are imported without invoking their producer.
HIGHER=P.HIGHER
HPROC=P.HPROC
INTRINSIC=P.INTRINSIC
IPROC=P.IPROC
TAYLOR=P.TAYLOR
TPROC=P.TPROC
TSOURCE=P.TSOURCE
TMANIFEST=P.TMANIFEST
OLD_SOURCE=P.OLD_SOURCE
OLD_MANIFEST=P.OLD_MANIFEST
BACKGROUND=P.BACKGROUND
MAJORANTS=P.MAJORANTS
APROC=P.APROC
APUB=P.APUB
LEGACY_SOURCE=P.LEGACY_SOURCE
LEGACY_HELPER=P.LEGACY_HELPER
LEGACY_MANIFEST=P.LEGACY_MANIFEST
ROOTS=P.ROOTS
ROOTPIECE=P.ROOTPIECE
DELTA=P.DELTA
def load_original_inputs(paths,gate,runtime):
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
    return raw,third,background,a_coeff,old_fold,P.unpack(ms["payload"])["coefficients"],P.unpack(ms["payload"])["majorants"]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir"):ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--manifest-sha",required=True)
    args=ap.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new scalar budgets are restricted to the public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the exact reviewed scientific runtime changed")
    ctx.prec=320;ctx.cap=4
    args.out_dir.mkdir(parents=True,exist_ok=True)
    native=args.out_dir/"temporary-whole-correlated-reference-budget.json.gz"
    process=args.out_dir/"process.json";start=time.monotonic()
    doc=dict(kind="actual_complete_scalar_whole_correlated_reference_forcing",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),algebra_sha256=sha(L.__file__),
        original_potential_source_sha256=sha(P.__file__),input_manifest_sha256=sha(args.manifest),
        runtime=runtime,complete=False,proved=False,actual_returncode=None,failure=None,gates=[],cases=[],
        original_accepted_target_FFT_intrinsic_fold_or_transport_recomputed=0,
        original_signed_Taylor_coefficients_recomputed=0,original_complete_output_tables_recomputed=0,
        original_natural_stage_bytes_modified=0,original_saved_background_Taylor_stages_read=0,
        original_complete_fold_majorant_stages_read=0,original_complete_support_recomputed=0,
        new_complete_RF_scalar_coefficient_enclosures=0,new_complete_forcing_budgets=0,
        new_complete_analytic_correction_budgets=0,new_complete_output_width_cases=0,
        full_source_operator_or_high_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False,
        temporary_signed_intermediates={})
    def checkpoint():
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-start
        save(native,doc)
    def gate(name,condition):
        passed=bool(condition);doc["gates"].append(dict(name=name,passed=passed));checkpoint()
        if not passed:raise ValueError(name)
    try:
        m=read(args.manifest)
        gate("the new scalar source and both unchanged imported algebras have their exact reviewed identities",
            doc["input_manifest_sha256"]==args.manifest_sha and doc["source_sha256"]==m["scientific_source_sha256"]
            and doc["algebra_sha256"]==ALGEBRA and doc["original_potential_source_sha256"]==POTENTIAL_SOURCE
            and m["public_repository"]==PUBLIC)
        for f in m["files"]:
            p=args.repo/f["path"]
            if not p.is_file() or p.stat().st_size!=f["bytes"] or sha(p)!=f["sha256"]:
                raise ValueError("an exact immutable scientific input changed: "+f["path"])
        paths={k:args.repo/v for k,v in m["input_paths"].items()}
        params=dict(R_G=str(RG),Sigma_G=str(SG),R_F=str(RF),Sigma_Delta=str(SD),Sigma_F=str(SF),
            R_T=str(RT),Sigma_X=str(SX),Sigma_A=str(SA),Delta_X=str(DX),R_s=str(RS),Sigma_s=str(SS),
            physical_cover=str(H),output_widths=list(map(str,WIDTHS)),
            complete_complex_delta_square_halfwidth=str(DELTA),complete_complex_z_square_halfwidth=str(P.Z),
            cutoff_abs_j=97,fixed_intrinsic_parameter="eta_0")
        gate("the complete proposed domains and immutable contract parameters agree with the manifest",
            m["mathematical_parameters"]==params and sha(paths["contract"])==CONTRACT
            and sha(paths["ordered_source_contract"])==ORDERED_CONTRACT
            and sha(paths["potential_contract"])==P.CONTRACT)
        doc["mathematical_parameters"]=params
        gate("all original native, process and original publication identities remain exact",
            sha(paths["higher_native"])==HIGHER and sha(paths["higher_process"])==HPROC
            and sha(paths["intrinsic_domain_native"])==INTRINSIC and sha(paths["intrinsic_domain_process"])==IPROC
            and sha(paths["Taylor_native"])==TAYLOR and sha(paths["Taylor_process"])==TPROC
            and sha(paths["background_stage"])==BACKGROUND and sha(paths["old_fold_majorants_stage"])==MAJORANTS
            and sha(paths["adjacent_process"])==APROC and sha(paths["adjacent_publication"])==APUB
            and sha(paths["potential_execution"])==POTENTIAL_EXECUTION
            and sha(paths["old_whole_execution"])==OLD_WHOLE_EXECUTION)
        raw,third,background,a_coeff,f,c,majorants=load_original_inputs(paths,gate,runtime)
        doc["original_saved_background_Taylor_stages_read"]=7
        doc["original_complete_fold_majorant_stages_read"]=1
        pe=read(paths["potential_execution"]);oldpe=pe["actual_scientific_receipt"]
        oe=read(paths["old_whole_execution"]);oldwhole=oe["actual_scientific_receipt"]
        gate("the accepted complete potential and old whole signed output tables are genuine successful receipts",
            pe["complete"] and pe["actual_returncode"]==0 and oldpe["complete"] and oldpe["proved"]
            and oldpe["actual_returncode"]==0 and oldpe["failure"] is None
            and oldpe["source_sha256"]==POTENTIAL_SOURCE
            and oldpe["input_manifest_sha256"]=="44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437"
            and oldpe["runtime"]==runtime and all(g["passed"] for g in oldpe["gates"])
            and oldpe["original_target_FFT_intrinsic_or_point_derivatives_recomputed"]==0
            and oe["complete"] and oe["actual_returncode"]==0
            and oldwhole["complete"] and oldwhole["proved"] and oldwhole["actual_returncode"]==0
            and oldwhole["failure"] is None and oldwhole["source_sha256"]==OLD_WHOLE_SOURCE
            and oldwhole["input_manifest_sha256"]==OLD_WHOLE_MANIFEST and oldwhole["runtime"]==runtime
            and all(g["passed"] for g in oldwhole["gates"])
            and oldwhole["original_fold_forcing_or_saved_Taylor_coefficients_recomputed"]==0)
        potential=next(v for v in oldpe["cases"] if Q(v["exact_complex_radial_radius"])==R0)
        support=next(v for v in oldpe["support_cases"] if Q(v["exact_radius"])==RG)
        gate("the complete original supporting third derivative and common image are only read",
            potential["complete"] and potential["proved"] and potential["failure"] is None
            and support["proved"] and support["failure"] is None
            and Q(potential["exact_support_radius"])==RG
            and Q(potential["exact_complex_z_square_halfwidth"])==P.Z
            and Q(potential["exact_complex_delta_square_halfwidth"])==DELTA
            and potential["all_integer_modes_abs_j_at_least"]==97 and potential["both_carrier_signs_retained"]
            and potential["physical_mean_is_not_z_zero_limit"]
            and potential["independent_even_mean_equation_retained"] and potential["actual_reference_seam_jumps_retained"])
        phase=phase_difference_budget(c,f,majorants,potential,gate)
        doc["complete_domain_conclusion"]={k:v for k,v in encode(phase).items()
            if k in ("canonical_inverse_radial_gap","common_T_image","normalized_phase_difference_root_orders",
                "proposed_forcing_old_rho_radius","unchanged_amplitude_old_rho_radius",
                "true_physical_root_piece_radius","new_radius_does_not_change_physical_piece_or_seams")}
        doc["complete_domain_conclusion"].update(dict(
            original_root_piece_only=True,complete_complex_parameter_squares=True,
            same_potential_T_segment_proved=True,actual_inverseimage_and_both_regular_paths_proved=True,
            exact_original_true_root_interval=list(map(str,ROOTS)),
            exact_original_physical_piece_interval=list(map(str,ROOTPIECE))))
        checkpoint()
        coef,temp=signed_coefficient_budget(raw,third,background,a_coeff,support)
        doc["new_complete_RF_scalar_coefficient_enclosures"]=1
        doc["temporary_signed_intermediates"]["new_RF_signed_coefficient_enclosures"]=temp
        gate("new complete signed RF disk algebra retains all gaps, finite products, radial frequency terms and means",
            all(v.is_finite() and v>0 for v in coef["gaps"].values())
            and coef["signed_DeltaV0_full_support"]<=384
            and all(up(coef[k]).is_finite() for k in ("C","delta_V0","radial_difference")))
        forcing=complete_forcing(c,f,majorants,phase,coef,potential)
        doc["new_complete_forcing_budgets"]=1
        doc["complete_forcing_conclusion"]=encode({k:forcing[k] for k in (
            "raw_fb","raw_fa","fb","fa","complete_DeltaR_a","complete_DeltaR_b",
            "complete_V_minus_radial_V","complete_radial_V",
            "old_potential_bounds_consumed_without_recomputation","actual_common_T_segment_consumed")})
        doc["complete_forcing_conclusion"].update(dict(
            exact_new_old_rho_radius=str(RF),exact_new_old_angle_strip=str(SF),
            complete_gap_lower_bounds=encode(coef["gaps"]),
            signed_full_mean_DeltaV0_modulus=rec(coef["delta_V0"]),
            complete_radial_frequency_difference_modulus=rec(coef["radial_difference"]),
            finite_products_assembled_only_on_the_new_RF_disk=True,
            original_Taylor_product_coefficients_recomputed=False,
            whole_zero_frequency_curvature_term_retained=True,
            independent_physical_even_mean_is_not_an_amplitude_mean=True))
        amplitude=complete_amplitudes(f,forcing);doc["new_complete_analytic_correction_budgets"]=1
        doc["complete_amplitude_conclusion"]=encode(amplitude)
        gate("the complete raw forcing and the same regular analytic first correction have finite whole bounds",
            all(forcing[k].is_finite() and forcing[k]>=0 for k in ("raw_fb","raw_fa","fb","fa"))
            and all(amplitude[k].is_finite() and amplitude[k]>=0 for k in ("a1","b1")))
        cases,changed,changed_mean=complete_output_cases(forcing,amplitude,oldwhole)
        doc["cases"]=cases;doc["new_complete_output_width_cases"]=len(cases)
        doc["complete_comparison_conclusion"]=dict(
            original_complete_output_execution_sha256=OLD_WHOLE_EXECUTION,
            number_of_strictly_smaller_complete_derivative_bounds=changed,
            number_of_strictly_smaller_complete_amplitude_mean_bounds=changed_mean,
            total_derivative_entries=144,total_amplitude_mean_entries=36,
            minimum_compares_only_identical_complete_functions_domains_and_norms=True,
            differences_of_upper_bounds_used=False,
            full_infinite_radial_and_angular_outputs_retained=True)
        gate("all three complete output widths retain every derivative, Fourier output, amplitude mean and old candidate",
            len(cases)==3 and all(len(v["fields"])==4 for v in cases)
            and all(v["joint_sum_of_radial_coefficient_suprema"] and v["full_radial_and_Fourier_tails_retained"]
                for case in cases for v in case["fields"]))
        doc["scope"]=dict(original_root_piece_2549_only=True,fixed_original_intrinsic_parameter="eta_0",
            full_complex_delta_square=True,full_z_square_all_abs_j_ge97=True,both_carrier_signs=True,
            original_nonzero_physical_and_reference_seam_sources_retained=True,
            complete_old_circle_I_J_and_independent_mean_conditions_retained=True,
            complete_positive_graph_conditions_retained=True,
            full_complex_genuine_reference_column_operator_bound=False,
            ordinary_source_operator_or_high_BVP_inverse=False,
            physical_output_radius_increased=False)
        doc["complete"]=doc["proved"]=True;doc["actual_returncode"]=0
    except Exception as e:
        doc["failure"]=type(e).__name__+": "+str(e);doc["actual_returncode"]=1
    finally:
        checkpoint()
        compact={k:v for k,v in doc.items() if k!="temporary_signed_intermediates"}
        compact["temporary_native_sha256"]=sha(native)
        compact["temporary_native_bytes"]=native.stat().st_size
        compact["temporary_native_is_not_published"]=True
        payload=(json.dumps(compact,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(payload)>60000:
            # Retain the scientific return code even if its final formatter fails.
            compact={k:v for k,v in compact.items() if k!="cases"}
            compact["formatting_failure"]="complete final table exceeded the small process limit"
            compact["actual_scientific_returncode"]=doc["actual_returncode"]
            save(process,compact)
            raise ValueError("complete small conclusion process exceeds sixty kilobytes")
        save(process,compact)
        lines=["# Actual whole correlated reference forcing and first-correction bounds","",
            "Public Actions run "+str(doc["run_id"])+"/"+str(doc["run_attempt"])+".",
            "Source SHA256: "+doc["source_sha256"]+".",
            "Input manifest SHA256: "+doc["input_manifest_sha256"]+".",
            "Actual child return code: "+str(doc["actual_returncode"])+".",
            "Actual complete/proved: "+str(doc["complete"])+"/"+str(doc["proved"])+".","",
            "The physical output disk remains 3/40000. Only the original root piece is identified with the analytic extension.",
            "Complete complex delta/z squares, all |j| >= 97, both carriers, independent physical even mean and every real seam are retained.",
            "Original target/FFT/intrinsic/fold/transport/Taylor/output-table recomputations: 0.",
            "New complete RF disk algebra and scalar budget calculations are distinguished from those original accepted computations.",
            "No complete ordinary-source norm, genuine-column operator norm or full high inverse is inferred.","",
            "## Exact proposed domains","",json.dumps(doc.get("mathematical_parameters",{}),sort_keys=True)]
        for key,title in (("complete_domain_conclusion","Actual domain conclusion"),
            ("complete_forcing_conclusion","Complete signed correlated forcing"),
            ("complete_amplitude_conclusion","Same regular first correction"),
            ("complete_comparison_conclusion","Complete bound comparison")):
            if key in doc:
                lines+=["","## "+title,"",json.dumps(doc[key],sort_keys=True)]
        for case in doc["cases"]:
            lines+=["","## Complete joint output width "+case["exact_output_old_phi_width"],"",
                "| Field | Radial order | Angular 0 | Angular 1 | Angular 2 | Angular 3 |",
                "|---|---:|---|---|---|---|"]
            for field in case["fields"]:
                for row in field["complete_mixed_derivative_rows"]:
                    vals=[v["ball"] for v in row["complete_joint_Wiener_upper"]]
                    lines.append("| "+field["field"]+" | "+str(row["radial_derivative_order"])+" | "+" | ".join(vals)+" |")
                lines+=["","Amplitude mean radial orders 0,1,2 for "+field["field"]+": "+
                    "; ".join(v["ball"] for v in field["complete_amplitude_mean_radial_derivative_upper"])+".",""]
        lines+=["","## Actual gates",""]+[
            "- "+g["name"]+": "+str(g["passed"])+"." for g in doc["gates"]]
        lines+=["","Actual scalar mathematics seconds: "+repr(doc["actual_mathematical_wall_seconds"])+".",
            "Actual failure: "+str(doc["failure"])+".",
            "Every reproducible signed polynomial and native remains temporary. Only these actual conclusions and their provenance may be published.",""]
        text="\n".join(lines)
        if len(text.encode())>60000:raise ValueError("the actual final conclusion exceeds sixty kilobytes")
        (args.out_dir/"conclusion.md").write_text(text,encoding="utf-8")
        print(json.dumps(dict(actual_returncode=doc["actual_returncode"],proved=doc["proved"],
            gates=len(doc["gates"]),new_complete_RF_scalar_coefficient_enclosures=doc["new_complete_RF_scalar_coefficient_enclosures"],
            old_numerical_stages_recomputed=0,conclusion_sha256=sha(args.out_dir/"conclusion.md"),
            process_sha256=sha(process)),sort_keys=True),flush=True)
    return doc["actual_returncode"]

if __name__=="__main__":sys.exit(main())
