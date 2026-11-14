#!/usr/bin/env python3
"""Complete R87 Ai source budget using convergent multiplier factorization.

All Fourier rows are retained.  The source norm is the actual R85 shear
L2_s H^{-2/3} norm.  The current narrow cutoff is included exactly; this
program does not claim a full reflection norm or a usable feedback cutoff.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
from flint import arb, ctx
from fourfold_phase_beta_interval import ball_record


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def exact(x):
    x=F(x)
    return arb(x.numerator)/x.denominator


def hi(x):
    if isinstance(x,dict):
        x=x["upper"]
    return arb(x).upper()


def lo(x):
    if isinstance(x,dict):
        x=x["lower"]
    return arb(x).lower()


def load(path):
    with (gzip.open(path,"rt") if str(path).endswith(".gz") else Path(path).open()) as f:
        return json.load(f)


@dataclass(frozen=True)
class Term:
    name: str
    factors: tuple[str,...]
    power: F
    airy_derivative: int
    scalar: int=1
    cutoff_derivative: int=0


def terms():
    """Every summand of R87(87.20),(87.21) and [Pcan,chi]U."""
    out=[]
    def append(name,factors,p,d,c=1,cut=0):
        out.append(Term(name,tuple(factors),F(p),d,c,cut))
    for name,p,d,c in [
        ("DB_without_Cphi",F(-1,3),0,1),("DB_Cphi",F(-1,3),0,1),
        ("DC",F(-2,3),1,2),
        ("LC_normal",F(-4,3),0,1),("LC_angle",F(-4,3),0,1),
        ("LC_potential",F(-4,3),0,1),("LB_normal",F(-5,3),1,1),
        ("LB_angle",F(-5,3),1,1),("LB_potential",F(-5,3),1,1)]:
        append(name,(name,),p,d,c)
    # Tuples contain coefficient factors, lambda power including c lambda^-1/3,
    # Ai derivative (0 or 1), and an absolute scalar.  Ai''=y lambda^(2/3) Ai
    # has already been used exactly.
    U=[
        ((),F(-1,3),0,1),(("trial_C",),F(-4,3),0,1),
        (("trial_B",),F(-5,3),1,1)]
    Uy=[
        (("C_y",),F(-4,3),0,1),(("y","trial_B"),F(-1,3),0,1),
        ((),F(1,3),1,1),(("trial_C",),F(-2,3),1,1),
        (("B_y",),F(-5,3),1,1)]
    Up=[
        ((),F(2,3),0,1),(("trial_C",),F(-1,3),0,1),
        (("C_phi",),F(-4,3),0,1),(("trial_B",),F(-2,3),1,1),
        (("B_phi",),F(-5,3),1,1)]
    Uyp=[
        (("C_y",),F(-1,3),0,1),(("C_yphi",),F(-4,3),0,1),
        (("y","trial_B"),F(2,3),0,1),
        (("y","B_phi"),F(-1,3),0,1),
        ((),F(4,3),1,1),(("trial_C",),F(1,3),1,1),
        (("C_phi",),F(-2,3),1,1),(("B_y",),F(-2,3),1,1),
        (("B_yphi",),F(-5,3),1,1)]
    Upp=[
        ((),F(5,3),0,1),(("trial_C",),F(2,3),0,1),
        (("C_phi",),F(-1,3),0,2),(("C_phiphi",),F(-4,3),0,1),
        (("trial_B",),F(1,3),1,1),(("B_phi",),F(-2,3),1,2),
        (("B_phiphi",),F(-5,3),1,1)]
    for prefix,factor,table,scalar in [
        ("E12_Uyp","cross_error",Uyp,2),
        ("E12y_Up","E12_normal",Up,1),
        ("E12p_Uy","E12_angle",Uy,1),
        ("E22_Upp","tangential_error",Upp,1),
        ("E22p_Up","E22_angle",Up,1)]:
        for j,(fac,p,d,c) in enumerate(table):
            append(f"{prefix}_{j}",(factor,)+fac,p,d,scalar*c)
    for prefix,table,extra,scalar,cut in [
        ("cut_Uy",Uy,(),2,1),("cut_U",U,(),1,2),
        ("cut_E12_Up",Up,("cross_error",),2,1),
        ("cut_E12p_U",U,("E12_angle",),1,1)]:
        for j,(fac,p,d,c) in enumerate(table):
            append(f"{prefix}_{j}",extra+fac,p,d,scalar*c,cut)
    return out


def multiply(a,b):
    # (radial vanishing order, sup coefficient, sup theta derivative)
    return a[0]+b[0],a[1]*b[1],a[2]*b[1]+a[1]*b[2]


def actual_multiplier_bounds(d,tt,cut_bounds):
    result={t.name:{"plain":arb(0),"cut":arb(0),"radial_order":None} for t in tt}
    for row in d["cells"]:
        chart=row["positive_chart_coefficients"]
        ordinary=row["ordinary_physical_theta_derivatives"]
        pt0=lo(chart["pt"]["lower"])
        pt1=hi(ordinary["pt"][1])
        sf0,sf1=[hi(x) for x in ordinary["physical_source_factor"][:2]]
        # Exact source density after the slice change:
        # f_shear = H'(varphi) [J/(tau phi_theta) f_can] o H.
        z0=sf0/pt0
        z1=sf1/pt0+sf0*pt1/pt0**2
        base=(0,z0,z1)
        factors={}
        for name,cols in row["derivative_sup_for_root_division"].items():
            factors[name]=(d["root_division_orders"][name],hi(cols[0]),hi(cols[1]))
        factors["y"]=(1,hi(ordinary["defining_ratio"][0]),
                        hi(ordinary["defining_ratio"][1]))
        yt0=hi(ordinary["yt"][0])
        for term in tt:
            v=base
            for f in term.factors:
                v=multiply(v,factors[f])
            k,c0,c1=v
            r=result[term.name]
            if r["radial_order"] is not None and r["radial_order"]!=k:
                raise ValueError("radial order changed between cells")
            r["radial_order"]=k
            plain=c0**(arb(1)/3)*(c0+c1/pt0)**(arb(2)/3)
            r["plain"]=max(r["plain"],plain.upper())
            m=term.cutoff_derivative
            cm0=cut_bounds[m]
            cm1=cut_bounds[m+1]*yt0
            ck0=c0*cm0
            ck1=(c1*cm0+c0*cm1)/pt0
            cut=ck0**(arb(1)/3)*(ck0+ck1)**(arb(2)/3)
            r["cut"]=max(r["cut"],cut.upper())
    return result


def airy_moment(k,decay):
    """L2 norm of (3/2) z^k (1+z) exp(-decay z^(3/2)/2)."""
    total=arb(0)
    for m,c in [(2*k,1),(2*k+1,2),(2*k+2,1)]:
        p=arb(2*(m+1))/3
        total+=c*(arb(2)/3)*decay**(-p)*p.gamma()
    return arb(3)/2*total.sqrt()


def maximum_monomial(r,c):
    # sup_{z>=0} z^r exp(-c z^(3/2)), r>=0.
    r=F(r)
    if r==0:return arb(1)
    if r<0:raise ValueError("negative monomial exponent")
    p=2*exact(r)/3
    return (p/(c*arb(1).exp()))**p


def diagonal_bound(k,p,L,h,decay,tail_start=None):
    """L2 -> L2_s H^-2/3 bound after input <D>^2, apart from 1+L^-2."""
    p=F(p)
    q=p+F(4,3)
    e=F(2*k,3)-p-1
    moment=airy_moment(k,2*decay)
    if tail_start is None:
        if e<=0:raise ValueError("interior term has no genuine gain")
        whole=moment*L**(-exact(e))
        # A second, finite-collar bound avoids replacing a tiny collar by a
        # half-line before maximizing over all input frequencies.
        if q>=0:
            power=F(2*k)-3*q+1
            if power<=0:raise ValueError("nonintegrable finite-collar comparison")
            r=F(3,2)*q
            sup=arb(3)/2*(maximum_monomial(r,decay)+maximum_monomial(r+1,decay))
            finite=sup*h**(exact(power)/2)/exact(power).sqrt()
        else:
            sup=arb(3)/2*(1+maximum_monomial(1,decay))
            finite=sup*L**exact(q)*h**(arb(k)+arb(1)/2)/arb(2*k+1).sqrt()
        return min(whole.upper(),finite.upper())
    # On s>=s0, split half the exponential off before integrating:
    # ||diag|| <= M_k(c) lambda^{-e} exp(-c s0^(3/2) lambda/2).
    b=decay*tail_start**(arb(3)/2)/2
    r=-e
    if r<=0:
        spectral=L**exact(r)*(-b*L).exp()
    else:
        critical=exact(r)/b
        if L>=critical.upper():
            spectral=L**exact(r)*(-b*L).exp()
        else:
            spectral=(exact(r)/(b*arb(1).exp()))**exact(r)
    exponential=airy_moment(k,decay)*spectral
    # The cutoff also has the upper endpoint h.  Maximizing the diagonal
    # multiplier pointwise in s before integrating is a second valid bound;
    # s0>0 permits negative radial exponents without a root singularity.
    if q>=0:
        r=F(3,2)*q
        sup=arb(3)/2*(maximum_monomial(r,decay)+maximum_monomial(r+1,decay))
        power=F(2*k)-3*q+1
        if power==0:
            radial=(h/tail_start).log()
        else:
            radial=(h**exact(power)-tail_start**exact(power))/exact(power)
        finite=sup*radial.sqrt()
    else:
        sup=arb(3)/2*(1+maximum_monomial(1,decay))
        finite=sup*L**exact(q)*h**(arb(k)+arb(1)/2)/arb(2*k+1).sqrt()
    return min(exponential.upper(),finite.upper())


def majorant_certificate():
    x=F(5,4);a=[F(0) for _ in range(27)];a[0]=a[1]=F(1,2)
    for n in range(24):a[n+3]=a[n]/((n+3)*(n+2))
    f=sum(a[n]*x**n for n in range(21))
    f+=F(100,99)*sum(a[n]*x**n for n in range(21,24))
    fp=sum(n*a[n]*x**(n-1) for n in range(1,21))
    fp+=F(100,99)*sum(n*a[n]*x**(n-1) for n in range(21,24))
    if not f<F(3,2) or not fp<F(3,2):
        raise ValueError("compact Airy majorant failed")
    if not x**3/F(21*23)<F(1,100):
        raise ValueError("majorant geometric remainder ratio failed")
    ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    aip0=1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    if not ai0<arb(1)/2 or not aip0<arb(1)/2:
        raise ValueError("actual Airy initial majorants failed")
    return {"positive_series_value_upper":str(f),"positive_series_derivative_upper":str(fp),
            "Ai0":ball_record(ai0),"minus_Aiprime0":ball_record(aip0)},(ai0/aip0).sqrt()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input",type=Path,default=Path(
        "notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz"))
    ap.add_argument("--q-input",type=Path,default=Path(
        "notes/2026-11-12-actual-root-v0-complex-strip.json.gz"))
    ap.add_argument("--shear-input",type=Path,default=Path(
        "notes/2026-11-12-positive-family-root-collar.json"))
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    d=load(args.input)
    if not d.get("proved") or d["failed_cells"] or d["pending"]:
        raise ValueError("actual whole collar is incomplete")
    config=d["configuration"]
    if config["first_cell"]!=0 or 2*config["last_cell"]!=config["initial_angle_cells"]:
        raise ValueError("not the actual half-quarter cover")
    if config["radial_cells"]!=1:raise ValueError("this aggregation expects one full radial slab")
    h=exact(F(config["exact_collar_height"]))
    cursor=F(0)
    for row in sorted(d["cells"],key=lambda r:F(r["exact_quarter_interval"][0])):
        a,b=map(F,row["exact_quarter_interval"])
        if a!=cursor or not b>a:raise ValueError("angle cover gap/overlap")
        if list(map(F,row["exact_positive_radial_interval"]))!=[F(0),F(config["exact_collar_height"])]:
            raise ValueError("radial slab differs")
        cursor=b
    if cursor!=F(1,2):raise ValueError("angle cover incomplete")
    src=Path(__file__).parent
    for key,name in [
      ("source_sha256","fourfold_phase_canonical_collar_centered_cover.py"),
      ("engine_source_sha256","fourfold_phase_canonical_collar_finite.py"),
      ("phase_centered_engine_source_sha256","fourfold_phase_canonical_collar_centered.py"),
      ("phase_taylor_source_sha256","fourfold_phase_root_potential_complex_strip.py")]:
        if config[key]!=sha(src/name):raise ValueError("frozen actual source changed")
    for name,value in config["dependencies"].items():
        if sha(src/name)!=value:raise ValueError("frozen dependency changed")
    amin=min(lo(r["positive_chart_coefficients"]["defining_ratio"]["lower"]) for r in d["cells"])
    amax=max(hi(r["positive_chart_coefficients"]["defining_ratio"]["upper"]) for r in d["cells"])
    ptmin=min(lo(r["positive_chart_coefficients"]["pt"]["lower"]) for r in d["cells"])
    ptmax=max(hi(r["positive_chart_coefficients"]["pt"]["upper"]) for r in d["cells"])
    delta0=max(abs(amin-1).upper(),abs(amax-1).upper())
    delta1=max((hi(r["ordinary_physical_theta_derivatives"]["defining_ratio"][1])/
                lo(r["positive_chart_coefficients"]["pt"]["lower"])).upper() for r in d["cells"])
    radius=arb(1)/4
    if not 0<delta0<radius:raise ValueError("Airy argument factorization does not converge")
    ratio=delta0/radius
    geometric=(1+(delta1/delta0)*ratio/(1-ratio))**(arb(2)/3)/(1-ratio)
    decay=arb(4463)/10752
    majorant,c=majorant_certificate()
    # Actual R66 angular shear derivative/inverse derivative bound.
    Jshear=arb("1.276240798")
    sd=load(args.shear_input)
    if not sd.get("complete") or sd["failed_cells"] or sd["pending"]:
        raise ValueError("actual physical shear collar is incomplete")
    for key in ("origin_inputs_sha256","direction_sha256"):
        if sd[key]!=config["object"][key]:
            raise ValueError("physical shear belongs to another actual family")
    a0,a1=map(F,config["object"]["exact_parameter_interval"])
    b0,b1=map(F,sd["exact_parameter_interval"])
    if not b0<=a0<=a1<=b1:
        raise ValueError("actual Airy parameter box not in physical shear box")
    if not h<lo(sd["operator_constants"]["length_lower"]):
        raise ValueError("actual Airy collar extends beyond the proved shear collar")
    for key in ("J_upper","J_inverse_upper"):
        if not hi(sd["operator_constants"][key])<Jshear:
            raise ValueError("actual shear derivative bound exceeded")
    bmin=ptmin/Jshear;bmax=ptmax*Jshear
    density=bmax**(arb(1)/6)*max(bmax.sqrt(),1/bmin.sqrt())**(arb(2)/3)
    # Rational/dyadic cutoff definition, chosen strictly inside the actual
    # positive chart.  Its constants are exact, not midpoint endpoints.
    yout=arb(49)/50*h
    yin=yout/2
    if not yout<amin*h:raise ValueError("cutoff is not inside the true chart")
    width=yout-yin
    cuts=[arb(1),arb(15)/(8*width),arb(6)/width**2,arb(60)/width**3]
    s0=yin/amax
    tt=terms();coeff=actual_multiplier_bounds(d,tt,cuts)
    # q_- below is a deliberately rounded-down consequence of the complete
    # same-object q certificate; it is also checked against that report.
    qdata=load(args.q_input)
    if not qdata.get("proved") or qdata["object"]!=config["object"]:
        raise ValueError("canonical q is not from the same actual completed family")
    qlower=arb("8.3278864767")
    qrecord=qdata["uniform_bounds"]["full_circle_frequency_lower"]
    if not qlower<lo(qrecord):
        raise ValueError("chosen lower q bound is not supported")
    results=[]
    for N in [0,4,16,32,64,128,256,512,1024,4096,16384,65536]:
        L=4*qlower*(N+1)
        common=c*density*geometric*(1+L**-2)
        rows=[];total=arb(0)
        for term in tt:
            data=coeff[term.name];k=data["radial_order"]
            if term.cutoff_derivative:
                val=data["cut"]*diagonal_bound(k,term.power,L,h,decay,s0)
            else:
                bare=diagonal_bound(k,term.power,L,h,decay)
                direct=data["cut"]*bare
                split=data["plain"]*bare+data["cut"]*diagonal_bound(
                    k,term.power,L,h,decay,s0)
                val=min(direct.upper(),split.upper())
            val*=abs(term.scalar)*common
            total+=val
            rows.append({"name":term.name,"upper":ball_record(val.upper())})
        rows.sort(key=lambda r:r["upper"]["mid_float"],reverse=True)
        results.append({"canonical_cutoff_N":N,"physical_canonical_frequency_lower":ball_record(L),
          "full_trial_source_upper":ball_record(total.upper()),
          "full_R85_contact_upper":ball_record((800*total).upper()),
          "largest_terms":rows[:10],"all_terms":rows})
    report={"kind":"actual_complete_narrow_cutoff_airy_source_by_analytic_factorization",
      "proved":True,"source_sha256":sha(__file__),
      "input_sha256":{str(args.input):sha(args.input),str(args.q_input):sha(args.q_input),
                      str(args.shear_input):sha(args.shear_input)},
      "object":config["object"],"root_certificate_sha256":config["root_certificate_sha256"],
      "actual_half_quarter_cells":len(d["cells"]),"exact_collar_height":config["exact_collar_height"],
      "Airy_contour_real_scale":"7/8","Airy_disk_radius":"1/4","Airy_decay":"4463/10752",
      "Airy_compact_majorant":majorant,"actual_a_min":ball_record(amin),"actual_a_max":ball_record(amax),
      "delta0":ball_record(delta0),"delta1_in_phi":ball_record(delta1),
      "factorization_sum":ball_record(geometric),"true_density_pullback":ball_record(density),
      "cutoff_y_outer_over_h":"49/50","cutoff_y_inner_over_h":"49/100",
      "cutoff_physical_support_lower":ball_record(s0),
      "term_definition":[dict(name=t.name,factors=t.factors,lambda_power=str(t.power),
          airy_derivative=t.airy_derivative,scalar=t.scalar,cutoff_derivative=t.cutoff_derivative,
          radial_order=coeff[t.name]["radial_order"],
          coefficient_plain_multiplier=ball_record(coeff[t.name]["plain"]),
          coefficient_cut_multiplier=ball_record(coeff[t.name]["cut"])) for t in tt],
      "budgets":results,
      "scope":["The full canonical trial residual, all E cross terms, and the actual quintic cutoff commutator are included.",
       "All output Fourier rows, including the mean and both signs, are retained.",
       "The input mean and regular finite input slots use the zero trial and remain genuine finite feedback slots.",
       "The source norm is actual R85 L2_s H^{-2/3} in the root-anchored physical shear angle.",
       "This report is not a full reflected-wave norm: actual contact-to-wave frame constants and the complete low/high Schur remain.",
       "Canonical input cutoff N is not a physical-theta Fourier projection."]}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"proved":True,"terms":len(tt),"factorization_sum":str(geometric),
       "source_N64":str(results[4]["full_trial_source_upper"]["upper"]),
       "report_sha256":sha(args.out)},indent=2))


if __name__=="__main__":
    main()
