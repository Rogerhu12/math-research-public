#!/usr/bin/env python3
"""Actual R96 complete canonical source/contact aggregation.

This is a new recovery source after executor loss. It consumes an actually
completed mixed cover, preserves the full uncompressed cap, root mean and
regular scalar slot, and never reconstructs missing interval rows.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import gzip,hashlib,json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_canonical_collar_centered_cover import ROOT_ORDERS
from fourfold_phase_airy_factorized_source_budget import terms as old_terms


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    with (gzip.open(p,"rt") if str(p).endswith(".gz") else Path(p).open()) as f:
        return json.load(f)
def exact(x):
    x=F(x);return arb(x.numerator)/x.denominator
def hi(x):
    if isinstance(x,dict):x=x["upper"]
    return arb(x).upper()
def lo(x):
    if isinstance(x,dict):x=x["lower"]
    return arb(x).lower()
def rec(x):return ball_record(arb(x))
def upper(x):return rec(arb(x).upper())


@dataclass(frozen=True)
class Term:
    name:str
    factors:tuple[str,...]
    power:F
    airy_derivative:int
    scalar:int=1
    cut:bool=False
    angular_flux:bool=False


def displayed_terms():
    scalar=[Term(t.name,t.factors,t.power,t.airy_derivative,t.scalar)
            for t in old_terms()[:9]]
    U=[((),F(-1,3),0), (("trial_C",),F(-4,3),0),
       (("trial_B",),F(-5,3),1)]
    Uy=[(("C_y",),F(-4,3),0), (("y","trial_B"),F(-1,3),0),
        ((),F(1,3),1), (("trial_C",),F(-2,3),1),
        (("B_y",),F(-5,3),1)]
    Up=[((),F(2,3),0), (("trial_C",),F(-1,3),0),
        (("C_phi",),F(-4,3),0), (("trial_B",),F(-2,3),1),
        (("B_phi",),F(-5,3),1)]
    for i,(fac,p,d) in enumerate(Uy):
        scalar.append(Term("cutoff_Uy_"+str(i),fac,p,d,cut=True))
    flux=[]
    for prefix,extra,table,angular in [
        ("E12_Uphi","cross_error",Up,False),
        ("E12_Uy_over_sqrt_y","cross_error",Uy,True),
        ("E22_Uphi_over_sqrt_y","tangential_error",Up,True)]:
        for i,(fac,p,d) in enumerate(table):
            flux.append(Term(prefix+"_"+str(i),(extra,)+fac,p,d,angular_flux=angular))
    for i,(fac,p,d) in enumerate(U):
        flux.append(Term("cutoff_Cey_U_"+str(i),fac,p,d,cut=True))
    if len(scalar)!=14 or len(flux)!=18:raise ValueError("incomplete true source split")
    return scalar,flux


def divided_radial_derivative(row,name,height):
    """True sup of d_s(f/s^k), using integral Taylor remainders."""
    k=ROOT_ORDERS[name]
    r=row["root_after_actual_angular_Taylor"][name]
    u=row["whole_slab_after_actual_angular_Taylor"][name]
    if r["first_order"]!=k or u["first_order"]!=k:
        raise ValueError("actual radial order changed")
    rc,uc=r["coefficients"],u["coefficients"]
    nmax=k+min(len(rc),len(uc))-1
    if nmax<k+1:raise ValueError("missing one true radial derivative: "+name)
    best=hi(uc[1][0])
    for n in range(k+2,nmax+1):
        total=sum(((i-k)*hi(rc[i-k][0])*height**(i-k-1)
                   for i in range(k+1,n)),arb(0))
        total+=(n-k)*hi(uc[n-k][0])*height**(n-k-1)
        best=min(best,total.upper())
    return best


def product(factors,table):
    k=F(0);c0=arb(1);c1=arb(0)
    for name in factors:
        a,b,c=table[name]
        k+=a;c0,c1=c0*b,c1*b+c0*c
    return k,c0,c1


def multiplier_cells(base,mixed,H,h,scalar,flux):
    scalar_bounds={t.name:{"k":None,"bound":arb(0)} for t in scalar}
    flux_bounds={t.name:{"k":None,"bound":arb(0)} for t in flux}
    eps=arb(0);G0=arb(0);amin_all=None;tmin_all=None;t1_all=arb(0)
    root_m=None;root_M=arb(0);density=arb(0);details=[]
    used=set(f for t in scalar+flux for f in t.factors if f!="y")
    for row in mixed["cells"]:
        original=base["cells"][row["base_index"]]
        if row["exact_quarter_interval"]!=original["exact_quarter_interval"]:
            raise ValueError("changed actual mixed cell")
        chart=original["positive_chart_coefficients"]
        ordinary=row["ordinary_physical_theta_derivatives"]
        amin=lo(chart["defining_ratio"]);Jmin=lo(chart["J"])
        ptmin=lo(chart["pt"]);ptmax=hi(chart["pt"])
        ys=hi(ordinary["ys"][0]);yt=hi(ordinary["yt"][0])
        ath=hi(ordinary["defining_ratio"][1])
        tmin=lo(chart["height"]);ttheta=hi(ordinary["height"][1])
        if not min(amin,Jmin,ptmin,tmin)>0:raise ValueError("missing true chart positivity")
        if not H<amin*h:raise ValueError("flat canonical collar leaves the actual image")
        amin_all=amin if amin_all is None else min(amin_all,amin)
        tmin_all=tmin if tmin_all is None else min(tmin_all,tmin)
        t1_all=max(t1_all,ttheta)
        root_m=ptmin if root_m is None else min(root_m,ptmin)
        root_M=max(root_M,ptmax)
        density=max(density,(hi(ordinary["J"][0])/tmin**2).sqrt().upper())
        div=row["derivative_sup_for_root_division"]
        e12=hi(div["cross_error"][0])*h**6
        e22=hi(div["tangential_error"][0])*h**7
        epscell=(e12/(amin*h).sqrt()+e22/(amin*h)).upper()
        eps=max(eps,epscell)
        g=hi(ordinary["height_normal_log"][0])
        denominator=ptmin-yt*e12
        if not denominator>0:raise ValueError("height-log angular denominator is not positive")
        gp=(ttheta/tmin+yt*g)/denominator
        gy=g+e12*gp
        g0=(gy**2+H*gp**2).sqrt().upper()
        G0=max(G0,g0)
        table={"y":(F(1),arb(1),arb(0))}
        for name in used:
            k=ROOT_ORDERS[name]
            b0,btheta=map(hi,div[name][:2])
            bs=divided_radial_derivative(row,name,h)
            c0=b0/amin**k
            c1=(ys*btheta+yt*bs+k*ath*b0)/(Jmin*amin**k)
            table[name]=(F(k),c0.upper(),c1.upper())
        for t in scalar:
            k,c0,c1=product(t.factors,table)
            val=c0**(arb(1)/3)*(c0+c1)**(arb(2)/3)
            z=scalar_bounds[t.name]
            if z["k"] is not None and z["k"]!=k:raise ValueError("scalar order mismatch")
            z["k"]=k;z["bound"]=max(z["bound"],val.upper())
        for t in flux:
            k,c0,c1=product(t.factors,table)
            if t.angular_flux:k-=F(1,2)
            z=flux_bounds[t.name]
            if z["k"] is not None and z["k"]!=k:raise ValueError("flux order mismatch")
            z["k"]=k;z["bound"]=max(z["bound"],c0.upper())
        details.append({"base_index":row["base_index"],
            "exact_quarter_interval":row["exact_quarter_interval"],
            "relative_principal_error_upper":upper(epscell),
            "height_covariant_gradient_upper":upper(g0),
            "height_normal_log_upper":upper(g),
            "height_angle_log_upper":upper(gp)})
    return scalar_bounds,flux_bounds,dict(epsilon=eps,G0=G0,
        actual_defining_ratio_lower=amin_all,actual_height_lower=tmin_all,
        actual_height_theta_upper=t1_all,root_angle_derivative_lower=root_m,
        root_angle_derivative_upper=root_M,scalar_L2_density_upper=density),details


def airy_certificate():
    ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    aip0=1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    if not (0<ai0<arb(36)/100 and 0<aip0<arb(26)/100):
        raise ValueError("actual Airy initial value gate failed")
    if not (arb(2)/3).exp()<2:raise ValueError("compact Airy joining gate failed")
    # Positive-axis contour gives the displayed large-z estimate; the
    # ODE energy identity plus these actual nonzero initial data proves
    # positivity and decreasing |Ai|, |Ai'| on the compact interval.
    if not 1/(2*arb.pi().sqrt())+1/(2*arb.pi())<arb(3)/4:
        raise ValueError("positive-axis contour constant failed")
    return dict(Ai0=rec(ai0),minus_Aiprime0=rec(aip0),
        common_real_axis_majorant="3/4 (1+z)^(1/4) exp(-2 z^(3/2)/3)",
        positive_axis_proof="R96: vertical contour, zero-exclusion energy, monotonicity, and explicit 0..1 join",
        compact_join_exp_gate=rec((arb(2)/3).exp())),(ai0/aip0).sqrt()


def moment(k,decay):
    k=F(k);total=arb(0)
    for eta in (F(0),F(1,2)):
        p=F(2,3)*(2*k+eta+1)
        if p<=0:raise ValueError("nonintegrable actual Airy moment")
        total+=arb(2)/3*decay**(-exact(p))*exact(p).gamma()
    return arb(3)/4*total.sqrt()


def monomial(r,c):
    r=F(r)
    if r<0:raise ValueError("negative monomial maximum exponent")
    if r==0:return arb(1)
    p=2*exact(r)/3
    return (p/(c*arb(1).exp()))**p


def diagonal(k,p,loss,L,H,tail_start=None):
    """All frequencies lambda>=L after input <lambda>^2, all output rows."""
    k,p,loss=F(k),F(p),F(loss)
    q=p+2-loss;e=F(2,3)*k-q+F(1,3);decay=arb(2)/3
    if tail_start is None:
        if e<=0:raise ValueError("intrinsic term lacks the claimed true gain")
        whole=moment(k,2*decay)*L**(-exact(e))
    else:
        b=decay*tail_start**(arb(3)/2)/2;r=-e
        if r<=0 or L>=(exact(r)/b).upper():
            spectral=L**exact(r)*(-b*L).exp()
        else:spectral=(exact(r)/(b*arb(1).exp()))**exact(r)
        whole=moment(k,decay)*spectral
    if q>=0:
        r=F(3,2)*q
        sup=arb(3)/4*(monomial(r,decay)+monomial(r+F(1,4),decay))
        power=2*k-3*q+1
        if tail_start is None:
            if power<=0:raise ValueError("finite canonical collar integral diverges")
            radial=H**exact(power)/exact(power)
        elif power==0:radial=(H/tail_start).log()
        else:radial=(H**exact(power)-tail_start**exact(power))/exact(power)
        finite=sup*radial.sqrt()
    else:
        sup=arb(3)/4*(1+monomial(F(1,4),decay))
        if not 2*k+1>0:raise ValueError("nonintegrable root power")
        finite=sup*L**exact(q)*H**exact(k+F(1,2))/exact(2*k+1).sqrt()
    return min(whole.upper(),finite.upper())


def contact(E,mu,Ereg,H,eps,GC,d):
    Ta=(E.sqrt()+GC*(2*H).sqrt()*mu)/d
    Treg=Ereg.sqrt()/d
    weak=(Ta**2+Treg**2).sqrt().upper()
    scalar=((4+H**2)/(1-eps)*weak**2+(4+2*H)).sqrt().upper()
    return dict(complete_weak_contact_upper=upper(weak),
        complete_scalar_contact_upper=upper(scalar),
        root_extension_energy=upper(E),regular_mean_extension_energy=upper(Ereg),
        root_L2_trace_factor=upper(mu))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base",type=Path,default=Path(
        "notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz"))
    ap.add_argument("--sharp",type=Path,default=Path(
        "ci-output/actual-canonical-mixed-recovery-complete.json.gz"))
    ap.add_argument("--q-input",type=Path,default=Path(
        "notes/2026-11-12-actual-root-v0-complex-strip.json.gz"))
    ap.add_argument("--whole",type=Path,default=Path(
        "notes/2026-11-12-actual-full-weak-source-budget.json"))
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    base,mixed,qdata,whole=map(load,(args.base,args.sharp,args.q_input,args.whole))
    if not base.get("proved") or base["failed_cells"] or base["pending"]:
        raise ValueError("original actual collar is incomplete")
    if not mixed.get("proved") or mixed["failed_cells"] or len(mixed["cells"])!=len(base["cells"]):
        raise ValueError("the actual mixed cover is incomplete; no prefix certificate allowed")
    cfg=base["configuration"];obj=cfg["object"]
    if mixed["base_cover_sha256"]!=sha(args.base) or mixed["actual_object"]!=obj:
        raise ValueError("actual mixed/base identity differs")
    if mixed["root_certificate_sha256"]!=cfg["root_certificate_sha256"]:
        raise ValueError("actual moving root differs")
    source=Path(__file__).parent
    if mixed["source_sha256"]!=sha(source/"fourfold_phase_canonical_collar_bivariate_recovery.py"):
        raise ValueError("actual mixed source differs")
    for name,value in mixed["dependencies"].items():
        if sha(source/name)!=value:raise ValueError("actual mixed dependency differs: "+name)
    for name,value in cfg["dependencies"].items():
        if sha(source/name)!=value:raise ValueError("actual base dependency differs: "+name)
    cursor=F(0);seen=set()
    for row in sorted(mixed["cells"],key=lambda r:F(r["exact_quarter_interval"][0])):
        a,b=map(F,row["exact_quarter_interval"]);i=row["base_index"]
        if a!=cursor or not b>a or i in seen:raise ValueError("actual angular cover gap/overlap")
        if list(map(F,row["exact_positive_radial_interval"]))!=[F(0),F(cfg["exact_collar_height"])]:
            raise ValueError("actual positive radial slab changed")
        seen.add(i);cursor=b
    if cursor!=F(1,2) or seen!=set(range(len(base["cells"]))):
        raise ValueError("actual half-quarter is incomplete")
    if not qdata.get("proved") or qdata["object"]!=obj:
        raise ValueError("true canonical period belongs to another actual family")
    if not whole.get("proved"):raise ValueError("complete whole positive cap input is missing")
    for key in ("origin_inputs_sha256","direction_sha256"):
        if whole[key]!=obj[key]:raise ValueError("whole cap belongs to another actual affine family")
    a,b=map(F,obj["exact_parameter_interval"]);c,d=map(F,whole["exact_parameter_interval"])
    if not c<=a<=b<=d:raise ValueError("whole-cap actual parameter box does not contain this box")
    if whole["input_sha256"].get(str(args.base))!=sha(args.base):
        raise ValueError("whole-cap and canonical base identity differs")
    h=exact(F(cfg["exact_collar_height"]));H=arb(49)/50*h;yin=H/2
    scalar,flux=displayed_terms()
    sb,fb,C,details=multiplier_cells(base,mixed,H,h,scalar,flux)
    eps,G0=C["epsilon"],C["G0"]
    if not eps<1:raise ValueError("canonical principal form is not positive")
    GC=(1+eps).sqrt()*G0;den=1-GC*H/(1-eps).sqrt()
    if not den>0:raise ValueError("actual height drift cannot be absorbed")
    Ereg=hi(whole["constants"]["regular_mean_extension_energy"])
    Egrad=max(1/H,arb(13)/12)
    Eall=((1+eps).sqrt()*Egrad.sqrt()+GC*(H/3).sqrt())**2
    all_contact=contact(Eall,arb(1),Ereg,H,eps,GC,den)
    qlo=lo(qdata["uniform_bounds"]["full_circle_frequency_lower"])
    if not qlo>0:raise ValueError("nonpositive true canonical frequency")
    airy,cair=airy_certificate()
    cut=arb(15)/(8*(H-yin))
    high=[];budgets=[]
    for N in [0,4,16,32,64,128,256,512,1024,4096,16384,65536]:
        L=4*qlo*(N+1);dn=max(arb(1),1/(H*L**(arb(2)/3)))
        EN=((1+eps).sqrt()*(dn+arb(1)/12).sqrt()
            +GC/(arb(3).sqrt()*L**(arb(2)/3)))**2
        mu=(1+L**2)**(-arb(1)/6)
        cn=contact(EN,mu,Ereg,H,eps,GC,den)
        high.append(dict(canonical_output_cutoff_N=N,frequency_lower=rec(L),**cn))
        common=cair*(1+L**-2);rows=[];S=arb(0);T=arb(0)
        for kind,tt,bb,loss in [("scalar",scalar,sb,F(2,3)),("weak_flux",flux,fb,F(0))]:
            for term in tt:
                z=bb[term.name]
                value=z["bound"]*diagonal(z["k"],term.power,loss,L,H,yin if term.cut else None)
                value*=common*abs(term.scalar)
                if term.cut:value*=cut
                elif kind=="weak_flux":value/=(1-eps).sqrt()
                value=value.upper()
                if kind=="scalar":S+=value
                else:T+=value
                rows.append(dict(name=term.name,source_kind=kind,radial_order=str(z["k"]),upper=upper(value)))
        A=hi(all_contact["complete_scalar_contact_upper"])*S+hi(all_contact["complete_weak_contact_upper"])*T
        B=hi(cn["complete_scalar_contact_upper"])*S+hi(cn["complete_weak_contact_upper"])*T
        rows.sort(key=lambda z:z["upper"]["mid_float"],reverse=True)
        budgets.append(dict(canonical_input_cutoff_N=N,true_canonical_frequency_lower=rec(L),
            complete_scalar_source_upper=upper(S),complete_weak_flux_source_upper=upper(T),
            all_root_and_regular_contact_upper=upper(A),
            same_N_high_canonical_root_and_regular_contact_upper=upper(B),
            largest_terms=rows[:10],all_terms=rows))
    sigma=arb(1)/3;tmin=C["actual_height_lower"];t1=C["actual_height_theta_upper"]
    m,M=C["root_angle_derivative_lower"],C["root_angle_derivative_upper"]
    physical=(tmin**(-(1-sigma))*(1/tmin+t1/tmin**2)**sigma
              *M**((1-sigma)/2)*max(M.sqrt(),1/m.sqrt())**sigma)
    C.update(canonical_flat_height=H,physical_collar_height=h,height_C_gradient_upper=GC,
        height_absorption_lower=den,all_root_extension_energy=Eall,regular_mean_extension_energy=Ereg,
        canonical_q_lower=qlo,cutoff_derivative_upper=cut,
        physical_root_dual_trace_conversion_upper=max(arb(1),physical))
    def term_records(tt,bb):
        return [dict(name=t.name,factors=list(t.factors),lambda_power=str(t.power),
            airy_derivative=t.airy_derivative,scalar=t.scalar,cutoff_derivative=t.cut,
            angular_flux=t.angular_flux,radial_order=str(bb[t.name]["k"]),
            complete_multiplier_bound=upper(bb[t.name]["bound"])) for t in tt]
    report=dict(kind="actual_complete_direct_canonical_full_cap_source_contact",proved=True,
        diagnostic_prefix_only=False,actual_cells=len(mixed["cells"]),required_cells=len(base["cells"]),
        source_sha256=sha(__file__),
        input_sha256={str(p):sha(p) for p in (args.base,args.sharp,args.q_input,args.whole)},
        dependency_sha256={name:sha(source/name) for name in (
            "fourfold_phase_beta_interval.py","fourfold_phase_canonical_collar_centered_cover.py",
            "fourfold_phase_airy_factorized_source_budget.py")},
        actual_object=obj,root_certificate_sha256=cfg["root_certificate_sha256"],
        physical_collar_height=cfg["exact_collar_height"],canonical_flat_height="49/102400",
        constants={k:rec(v) for k,v in C.items()},real_Airy_certificate=airy,
        all_root_contact=all_contact,high_root_contact_table=high,
        scalar_terms=term_records(scalar,sb),weak_flux_terms=term_records(flux,fb),
        complete_residual_budgets=budgets,actual_height_gradient_cells=details,
        scope=[
          "The harmonic extension is the complete uncompressed positive cap with its true Robin form.",
          "The root mean, regular mean and its flux, both Fourier signs and all output rows are retained.",
          "High root tables restrict only canonical boundary test traces; no high body projection is made.",
          "The ordinary source and weak flux have the exact paired Piola/height transformation of R96.",
          "The 14 scalar and 18 weak-flux terms include the entire displayed cutoff trial residual.",
          "Input mean and regular finite input slots use zero trial and remain actual finite Schur slots.",
          "No completed reflection bound, usable feedback cutoff or nonlinear exact zero is asserted.",
          "All mixed cells were actually recomputed; no missing interval output was restored from prose."])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(dict(proved=True,actual_cells=len(mixed["cells"]),report_sha256=sha(args.out),
        all_contact=all_contact,source_N64=budgets[4]),default=str),flush=True)


if __name__=="__main__":main()
