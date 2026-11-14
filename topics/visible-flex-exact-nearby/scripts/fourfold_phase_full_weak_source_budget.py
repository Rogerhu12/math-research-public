#!/usr/bin/env python3
"""Full uncompressed cap energy contact and actual Airy weak-flux budgets.

The scalar part produced by the exact height change is stated separately.
This report certifies the complete displayed weak-flux summands, not a
full reflected-wave remainder and not the still-running sharper collar.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_airy_factorized_source_budget import (
    sha,exact,hi,lo,load,majorant_certificate,maximum_monomial)


def moment(k,c):
    total=arb(0)
    for m,b in [(2*k,1),(2*k+1,2),(2*k+2,1)]:
        p=exact(F(2,3)*(m+1))
        total+=b*arb(2)/3*c**(-p)*p.gamma()
    return arb(3)/2*total.sqrt()


def diagonal(k,p,L,h,c,s0=None):
    """Complete L2_s L2_phi diagonal after the input (1+lambda^2)."""
    k,p=F(k),F(p)
    exponent=F(2,3)*k-p-F(5,3)
    q=p+2
    if s0 is None:
        if exponent<=0:raise ValueError("interior weak source lacks required gain")
        whole=moment(k,2*c)*L**(-exact(exponent))
    else:
        b=c*s0**(arb(3)/2)/2
        r=-exponent
        if r<=0 or L>=(exact(r)/b).upper():
            spectral=L**exact(r)*(-b*L).exp()
        else:
            spectral=(exact(r)/(b*arb(1).exp()))**exact(r)
        whole=moment(k,c)*spectral
    if q>=0:
        r=F(3,2)*q
        sup=arb(3)/2*(maximum_monomial(r,c)+maximum_monomial(r+1,c))
        power=2*k-3*q+1
        if s0 is None:
            if power<=0:raise ValueError("nonintegrable root weak-source comparison")
            radial=h**exact(power)/exact(power)
        elif power==0:
            radial=(h/s0).log()
        else:
            radial=(h**exact(power)-s0**exact(power))/exact(power)
        finite=sup*radial.sqrt()
    else:
        sup=arb(3)/2*(1+maximum_monomial(1,c))
        finite=sup*L**exact(q)*h**(exact(k)+arb(1)/2)/exact(2*k+1).sqrt()
    return min(whole.upper(),finite.upper())


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--collar",type=Path,default=Path("notes/2026-11-12-positive-family-root-collar.json"))
    ap.add_argument("--closed",type=Path,default=Path("notes/2026-11-12-actual-closed-approximate-exterior.json"))
    ap.add_argument("--robin",type=Path,default=Path("notes/2026-11-12-actual-exterior-robin-certificate.json"))
    ap.add_argument("--common",type=Path,default=Path("notes/2026-11-12-common-core-exterior-parameter-interval.json"))
    ap.add_argument("--canonical",type=Path,default=Path("notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz"))
    ap.add_argument("--frequency",type=Path,default=Path("notes/2026-11-12-actual-root-v0-complex-strip.json.gz"))
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    collar,closed,robin,common,can,freq=map(load,(
        args.collar,args.closed,args.robin,args.common,args.canonical,args.frequency))
    if not all(d.get("complete") for d in (collar,closed,robin)):
        raise ValueError("actual complete exterior inputs required")
    if sha(args.collar) not in closed["input_sha256"].values():
        raise ValueError("collar is not part of the actual closed exterior")
    if sha(args.closed) not in robin["input_sha256"].values():
        raise ValueError("full Robin does not belong to this exterior")
    interval=list(map(F,common["chosen_closed_interval"]))
    for d in (collar,closed,robin):
        a,b=map(F,d["exact_parameter_interval"])
        if not a<=interval[0]<=interval[1]<=b:
            raise ValueError("actual exterior parameter inclusion failed")
        for key in ("origin_inputs_sha256","direction_sha256"):
            if d[key]!=closed[key]:raise ValueError("different true affine objects")
    if not can.get("proved") or can["failed_cells"] or can["pending"]:
        raise ValueError("whole true canonical collar required")
    config=can["configuration"]
    if list(map(F,config["object"]["exact_parameter_interval"]))!=interval:
        raise ValueError("actual canonical and exterior common boxes differ")
    if not freq.get("proved") or freq["object"]!=config["object"]:
        raise ValueError("canonical frequency certificate identity mismatch")
    for key in ("origin_inputs_sha256","direction_sha256"):
        if config["object"][key]!=closed[key]:raise ValueError("different actual collar object")
    src=Path(__file__).parent
    for key,name in (
      ("source_sha256","fourfold_phase_canonical_collar_centered_cover.py"),
      ("engine_source_sha256","fourfold_phase_canonical_collar_finite.py"),
      ("phase_centered_engine_source_sha256","fourfold_phase_canonical_collar_centered.py"),
      ("phase_taylor_source_sha256","fourfold_phase_root_potential_complex_strip.py")):
        if config[key]!=sha(src/name):raise ValueError("actual canonical source changed")
    for name,value in config["dependencies"].items():
        if sha(src/name)!=value:raise ValueError("frozen actual dependency changed")
    cursor=F(0);height=F(config["exact_collar_height"])
    for row in sorted(can["cells"],key=lambda r:F(r["exact_quarter_interval"][0])):
        a,b=map(F,row["exact_quarter_interval"])
        if a!=cursor or not a<b:raise ValueError("actual angular cover gap/overlap")
        if list(map(F,row["exact_positive_radial_interval"]))!=[F(0),height]:
            raise ValueError("actual whole radial collar differs")
        cursor=b
    if cursor!=F(1,2):raise ValueError("actual half-quarter cover incomplete")
    local=collar["operator_constants"];global_values=closed["complete_finite_positive_operator"]
    ell=lo(local["length_lower"]);M=hi(local["M_upper"])
    length=lo(global_values["length_lower"]);MG=hi(global_values["matrix_upper"])
    mean_energy=(MG/length).upper()
    all_energy=(M*max(1/ell,arb(13)/12)).upper()
    all_contact=(all_energy+mean_energy).sqrt().upper()
    if not all_contact<63:raise ValueError("strict full weak contact 63 not justified")
    boundary=[]
    for N in (0,4,16,32,64,128,256,512,1024,4096):
        lam=arb(4*(N+1))
        d=max(arb(1),(1/(ell*lam**(arb(2)/3))).upper())
        energy=(M*(d+arb(1)/12)).upper()
        boundary.append(dict(physical_root_cutoff_N=N,
          root_frequency_lower=4*(N+1),full_uncompressed_root_energy=ball_record(energy),
          full_high_root_weak_contact=ball_record(energy.sqrt().upper()),
          full_high_root_and_regular_weak_contact=ball_record((energy+mean_energy).sqrt().upper())))
    # Actual relative canonical ellipticity: C=diag(1,y)+E.
    h=exact(height);eps=arb(0);measure=arb(0)
    amin=arb("inf");amax=arb(0)
    for row in can["cells"]:
        chart=row["positive_chart_coefficients"]
        a=lo(chart["defining_ratio"]["lower"]);amin=min(amin,a)
        amax=max(amax,hi(chart["defining_ratio"]["upper"]))
        e12=hi(row["derivative_sup_for_root_division"]["cross_error"][0])
        e22=hi(row["derivative_sup_for_root_division"]["tangential_error"][0])
        eps=max(eps,(e12*h**(arb(11)/2)/a.sqrt()+e22*h**6/a).upper())
        measure=max(measure,(hi(chart["J"]["upper"])/lo(chart["pt"]["lower"])).upper())
    if not 0<=eps<arb(1)/1000:
        raise ValueError("actual canonical energy comparison unresolved")
    delta=max(abs(amin-1).upper(),abs(amax-1).upper())
    if not 0<delta<arb(1)/4:raise ValueError("actual analytic Airy factorization fails")
    geometric=1/(1-4*delta)
    qlo=lo(freq["uniform_bounds"]["full_circle_frequency_lower"])
    yout=arb(49)/50*h;yin=yout/2;width=yout-yin
    if not yout<amin*h:raise ValueError("actual cutoff outside the positive chart")
    s0=yin/amax;chi1=arb(15)/(8*width)
    majorant,cA=majorant_certificate();decay=arb(4463)/10752
    U=[((),F(-1,3),0),(("trial_C",),F(-4,3),0),(("trial_B",),F(-5,3),1)]
    Uy=[(("C_y",),F(-4,3),0),(("y","trial_B"),F(-1,3),0),
        ((),F(1,3),1),(("trial_C",),F(-2,3),1),(("B_y",),F(-5,3),1)]
    Up=[((),F(2,3),0),(("trial_C",),F(-1,3),0),(("C_phi",),F(-4,3),0),
        (("trial_B",),F(-2,3),1),(("B_phi",),F(-5,3),1)]
    terms=[]
    for prefix,factor,table,radial_loss in (
        ("E12_Uphi","cross_error",Up,F(0)),
        ("E12_Uy_over_sqrt_y","cross_error",Uy,F(1,2)),
        ("E22_Uphi_over_sqrt_y","tangential_error",Up,F(1,2))):
        for i,(fac,p,derivative) in enumerate(table):
            terms.append(dict(name=prefix+"_"+str(i),factors=(factor,)+fac,p=p,
              airy_derivative=derivative,radial_loss=radial_loss,cutoff=False))
    for i,(fac,p,derivative) in enumerate(U):
        terms.append(dict(name="cutoff_Cey_U_"+str(i),factors=fac,p=p,
          airy_derivative=derivative,radial_loss=F(0),cutoff=True))
    for term in terms:
        bound=arb(0);power=None
        for row in can["cells"]:
            chart=row["positive_chart_coefficients"];factors={}
            for name,cols in row["derivative_sup_for_root_division"].items():
                factors[name]=(F(can["root_division_orders"][name]),hi(cols[0]))
            factors["y"]=(F(1),hi(row["ordinary_physical_theta_derivatives"]["defining_ratio"][0]))
            k=F(0);value=arb(1)
            for name in term["factors"]:
                order,v=factors[name];k+=order;value*=v
            if term["radial_loss"]:
                value/=lo(chart["defining_ratio"]["lower"]).sqrt()
                k-=term["radial_loss"]
            if term["cutoff"]:value*=chi1
            if power is not None and power!=k:raise ValueError("true radial order mismatch")
            power=k;bound=max(bound,value.upper())
        term["radial_order"]=power;term["coefficient_bound"]=bound
    budgets=[]
    for N in (0,4,16,32,64,128,256,512,1024,4096,16384,65536):
        lam=4*qlo*(N+1)
        common_factor=cA*measure.sqrt()*geometric*(1+lam**-2)
        rows=[];interior=arb(0);cut=arb(0)
        for term in terms:
            value=term["coefficient_bound"]*diagonal(
                term["radial_order"],term["p"],lam,h,decay,s0 if term["cutoff"] else None)
            value*=common_factor
            if term["cutoff"]:
                cut+=value
            else:
                value/=(1-eps).sqrt();interior+=value
            rows.append(dict(name=term["name"],upper=ball_record(value.upper())))
        total=(interior+cut).upper()
        budgets.append(dict(canonical_input_cutoff_N=N,
          true_canonical_frequency_lower=ball_record(lam),
          principal_error_weak_flux_upper=ball_record(interior.upper()),
          cutoff_weak_flux_upper=ball_record(cut.upper()),
          complete_displayed_weak_flux_upper=ball_record(total),
          full_root_and_regular_weak_contact_upper=ball_record((all_contact*total).upper()),
          all_terms=rows))
    report=dict(kind="actual_full_uncompressed_cap_weak_source_and_Airy_flux_budget",proved=True,
      source_sha256=sha(__file__),input_sha256={str(p):sha(p) for p in (
        args.collar,args.closed,args.robin,args.common,args.canonical,args.frequency)},
      dependency_sha256={name:sha(src/name) for name in (
        "fourfold_phase_beta_interval.py","fourfold_phase_airy_factorized_source_budget.py")},
      exact_parameter_interval=list(map(str,interval)),
      origin_inputs_sha256=closed["origin_inputs_sha256"],direction_sha256=closed["direction_sha256"],
      actual_half_quarter_cells=len(can["cells"]),
      constants={k:ball_record(v) for k,v in dict(
        collar_length_lower=ell,collar_matrix_upper=M,whole_length_lower=length,whole_matrix_upper=MG,
        all_root_extension_energy=all_energy,regular_mean_extension_energy=mean_energy,
        complete_uncompressed_weak_source_contact=all_contact,
        canonical_relative_principal_error_upper=eps,
        canonical_fixed_angle_radial_measure_upper=measure,Airy_C0_factorization_sum=geometric,
        cutoff_physical_support_lower=s0).items()},
      full_uncompressed_boundary_table=boundary,
      Airy_compact_majorant=majorant,
      weak_flux_terms=[dict(name=t["name"],factors=t["factors"],lambda_power=str(t["p"]),
        radial_order=str(t["radial_order"]),airy_derivative=t["airy_derivative"],
        coefficient_bound=ball_record(t["coefficient_bound"]),cutoff=t["cutoff"]) for t in terms],
      weak_flux_budgets=budgets,
      scope=[
       "The Poisson solution is the complete uncompressed actual cap with its true Robin form and fixed regular mean.",
       "Root zero mode, regular mean-flux output and all low/high body coupling are retained.",
       "The high-root table restricts only the boundary test trace; the body solution is not projected.",
       "Canonical input frequency is not identified with a physical Fourier output cutoff.",
       "The physical weak-flux norm equals the exact canonical inverse-principal energy norm.",
       "The exact transformed scalar remainder, including the height-log term, remains required.",
       "The 18 displayed flux summands are complete for chi E grad U + chi_prime U C e_y.",
       "No full Airy trial remainder, reflection norm or feedback inverse is claimed by this flux-only table."])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(dict(proved=True,complete_weak_contact=all_contact.str(25),
      relative_error=eps.str(25),source_N64=budgets[4]["complete_displayed_weak_flux_upper"],
      report_sha256=sha(args.out)),indent=2))


if __name__=="__main__":main()
