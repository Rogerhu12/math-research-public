#!/usr/bin/env python3
"""Actual full strict-interval R46 operator budget, with all Fourier blocks.

Consumes a COMPLETE native WKB/energy field cover and the completed actual
all-time ray certificate. It composes triangular energies before applying
endpoint norm equivalence, then pays both exact WKB branches, full conormal
frame, both frequency cones, all mean outputs, and ordinary sources.

It proves only the displayed closed strictly negative interval. It does not
supply either actual turning connection, Ai/contact network, R104 return
coefficient identification, or a final effective cutoff.
"""
from __future__ import annotations
import argparse,math,time
from collections import Counter
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb_mat,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha
from fourfold_strict_actual_wkb_fields import record
from fourfold_strict_high_energy_triangular import (
    positive_matrix_bound,weighted_principal,matrix_rows)

CUT=Fraction(268136140016943,1125899906842624)

def upper(row):
    value=arb(row["ball"]).upper()
    if not value.is_finite():raise ValueError("nonfinite actual field bound")
    return value
def lower(row):
    value=arb(row["ball"]).lower()
    if not value.is_finite():raise ValueError("nonfinite actual lower bound")
    return value
def matrix_record(A):
    return [[record(A[i,j].real) for j in range(A.ncols())] for i in range(A.nrows())]
def identity(n):return acb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def matrix_positive_upper(A):
    return acb_mat([[abs(A[i,j]).upper() for j in range(A.ncols())] for i in range(A.nrows())])

def actual_spline_regularity(object_path):
    """Exact dyadic knot multiplicities for every installed scalar family."""
    obj=read(object_path)
    for name in ("origin_inputs","direction"):
        if sha(obj[name]["path"])!=obj[name]["sha256"]:
            raise ValueError("actual scalar family changed: "+name)
    rows=[]
    with np.load(obj["origin_inputs"]["path"],allow_pickle=False) as source:
        specs=[("base","base_knots",int(source["base_degree"]),0),
               ("raw","phase_knots",5,0),("raw_direction","phase_knots",5,0),
               ("shift","shift_knots",int(source["shift_degree"]),0)]
        for j in range(len(source["alpha"])):
            specs.append((f"mean{j}",f"mean{j}_knots",int(source[f"mean{j}_degree"]),0))
        for j in range(len(source["alpha"])+1):
            specs.append((f"height_integral{j}",f"height{j}_slope_knots",
                          int(source[f"height{j}_slope_degree"])+1,1))
        for name,key,degree,integrated in specs:
            knots=[Fraction(float(x)) for x in source[key]]
            # Antiderivation duplicates only the outer endpoints. Those lie
            # outside this strict interval; every interior multiplicity stays.
            counts=Counter(x for x in knots if -CUT<x<CUT)
            multiplicity=max(counts.values(),default=0)
            continuity=degree-multiplicity
            if continuity<4:raise ValueError("insufficient actual C4 scalar regularity: "+name)
            rows.append(dict(name=name,degree=degree,antiderivative=bool(integrated),
                maximum_interior_knot_multiplicity=multiplicity,
                minimum_global_continuity_order=continuity))
    return dict(object_path=str(object_path),origin_sha256=obj["origin_inputs"]["sha256"],
        direction_sha256=obj["direction"]["sha256"],exact_interval=[str(-CUT),str(CUT)],
        all_true_scalar_families_at_least_C4=True,rows=rows,
        implication="The actual infinite primitive is globally C4 in r with all paid angular derivatives; the fixed-type coefficients are C2 and piecewise W3,infinity, so the WKB conormal has no knot delta source.")

def wiener(p,M,strip):
    """Complete physical 4Z weighted l1, including the mean."""
    p=Fraction(p)
    if p<0 or not M>=0 or not strip>0:raise ValueError("invalid true Wiener domain")
    n=(p.numerator+p.denominator-1)//p.denominator
    pp=exact_arb(p);q=(-4*strip).exp()
    return (4**pp*M*math.factorial(n)*(2/(1-q)**(n+1)-1)).upper()
def multiplier(p,M,strip):
    p=abs(Fraction(p))
    return (2**(exact_arb(p)/2)*wiener(p,M,strip)).upper()

def actual_energy(row,order):
    e=row["energy"];ranges=e["positive_ranges"]
    amin,amax=lower(ranges["alpha"][0]),upper(ranges["alpha"][1])
    gmin,gmax=lower(ranges["gamma"][0]),upper(ranges["gamma"][1])
    lmin,lmax=lower(ranges["lambda"][0]),upper(ranges["lambda"][1])
    if not min(amin,gmin,lmin)>0:raise ValueError("actual strict energy positivity missing")
    moments={name:[upper(x) for x in d["true_derivative_A_norms"]]
             for name,d in row["complete_high_angular_moments"].items()}
    for name in ("alpha","v","gamma","tau","sigma"):
        if len(moments[name])<order+2:raise ValueError("unknown actual coefficient derivative")
    if len(moments["d"])<order+1:raise ValueError("unknown actual full potential derivative")
    matrices={side:acb_mat(order+1,order+1) for side in ("forward","backward")}
    for j in range(order+1):
        for side,A in matrices.items():
            base=upper(e["base_energy_rate_"+side])/2
            first=upper(e["first_characteristic_rate_"+side])
            A[j,j]=max(arb(0),base+j*first).upper()
        for ell in range(j):
            n=j-ell;c0=arb(math.comb(j,ell));c1=arb(math.comb(j+1,ell))
            vals=(c0*moments["v"][n]*(lmax/gmin).sqrt(),
                  c0*moments["alpha"][n]*(lmax/amin).sqrt(),
                  c1*moments["v"][n+1]*(gmax/gmin).sqrt(),
                  c1*moments["alpha"][n+1]*(gmax/amin).sqrt(),
                  c0*moments["d"][n]*(amax/lmin).sqrt(),
                  c1*moments["gamma"][n+1]*(amax/gmin).sqrt(),
                  c1*moments["v"][n+1]*(amax/amin).sqrt())
            z=sum((v*v for v in vals),arb(0)).sqrt().upper()
            for A in matrices.values():A[j,ell]=z
    length=exact_arb(Fraction(row["right"])-Fraction(row["left"]))
    maps={side:matrix_positive_upper((length*A).exp()) for side,A in matrices.items()}
    return maps,min(amin,gmin,lmin),max(amax,gmax,lmax),amax

def composition_constants(CJ,delta,max_order=25):
    """Real Bell/reciprocal recurrences; both actual flow maps and inverses."""
    c=(1/CJ).lower()
    rho=delta/2
    H=[arb(0)]+[(math.factorial(j-1)*CJ/rho**(j-1)).upper()
                  for j in range(1,max_order+2)]
    bell=[[arb(0) for _ in range(max_order+1)] for _ in range(max_order+1)]
    bell[0][0]=arb(1)
    for j in range(1,max_order+1):
        for ell in range(1,j+1):
            bell[j][ell]=sum((math.comb(j-1,m-1)*H[m]*bell[j-m][ell-1]
                             for m in range(1,j-ell+2)),arb(0)).upper()
    positive=[];negative=[]
    for k in range(12):
        value=(sum((math.comb(k,j)*sum(bell[j][:j+1],arb(0))**2
                    for j in range(k+1)),arb(0))/c).sqrt().upper()
        positive.append(value)
        negative.append((multiplier(k,CJ,delta)*value).upper())
    # Taylor majorants of 1/(t H'+1-t) at every real point and every t in [0,1].
    q=[(1/c).upper()]
    a=[H[j+1]/math.factorial(j) for j in range(max_order+1)]
    for n in range(1,max_order+1):
        q.append((sum((a[j]*q[n-j] for j in range(1,n+1)),arb(0))/c).upper())
    def cross_constant(M,constant=False,N=24):
        v=[M if j==0 else arb(0) if constant else M/rho**j for j in range(N+1)]
        for step in range(N):
            v=[((n+1)*sum((v[j]*q[n+1-j] for j in range(n+2)),arb(0))).upper()
               for n in range(N-step)]
        return v[0]
    def Nrange(left,right):
        lo=math.floor(Fraction(left));hi=math.ceil(Fraction(right))
        return max(positive[k] if k>=0 else negative[-k] for k in range(lo,hi+1)).upper()
    return dict(CJ=CJ,positive=positive,negative=negative,
        first_derivative_lower=c,derivative_bounds=H,
        Nrange=Nrange,cross_constant=cross_constant)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fields",type=Path,default=Path(
        "notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz"))
    ap.add_argument("--ray",type=Path,default=Path(
        "notes/2026-11-13-R106-integrated-source-ray-refinement.json"))
    ap.add_argument("--window",type=int,default=8)
    ap.add_argument("--bits",type=int,default=256)
    ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise ValueError("new output path required")
    if a.window!=8:raise ValueError("this explicit full set of composition orders is frozen at S=8")
    ctx.prec=a.bits;start=time.monotonic()
    fields,ray=read(a.fields),read(a.ray)
    if (not fields.get("complete") or not fields.get("proved") or fields["kind"]!=
            "actual_strict_R46_complete_WKB_and_energy_fields"):
        raise ValueError("complete actual strict WKB field cover required")
    source=Path(__file__).with_name("fourfold_strict_actual_wkb_fields.py")
    if fields["source_sha256"]!=sha(source):raise ValueError("actual WKB field source changed")
    for name,digest in fields["dependencies"].items():
        if sha(source.with_name(name))!=digest:raise ValueError("actual WKB dependency changed: "+name)
    if sha(fields["object_path"])!=fields["object_sha256"]:
        raise ValueError("actual geometric object changed")
    regularity=actual_spline_regularity(fields["object_path"])
    if fields["exact_covered_positive_interval"]!=["0",str(CUT)]:
        raise ValueError("the full exact positive strict interval is not present")
    ident=fields["identity"]
    if not ident["uniform_in_the_entire_real_parameter_interval"]:
        raise ValueError("the entire real parameter family is missing")
    ri=ray["proved_region"]
    if (not ray.get("complete") or ray["kind"]!=
        "R106_integrated_parameter_source_true_all_time_ray_refinement" or
        ri["leg"]!="forward" or ri["segments"]!=550 or
        ri["time_endpoints"]!=["-pi/2","pi/2"] or ri["label_period"]!="2*pi" or
        not all(g["passed"] for g in ray["gates"])):
        raise ValueError("whole actual all-time ray certificate required")
    for item in ray["provenance"]["inputs"]:
        if sha(item["path"])!=item["sha256"]:raise ValueError("actual whole ray input changed")
    if sha(ray["provenance"]["source"])!=ray["provenance"]["source_sha256"]:
        raise ValueError("actual whole ray producer changed")
    if (ri["parameter_center"]!=ident["exact_center_parameter"] or
            ri["parameter_half_width"]!=ident["exact_parameter_half_width"]):
        raise ValueError("actual ray and WKB field families differ")
    rb=lambda key:exact_arb(Fraction(ray["bounds"][key]["exact"]))
    J,m,J2,image=(rb(k) for k in ("true_label_J_modulus","true_label_J_real_lower",
                               "true_second_label_derivative","physical_image_strip"))
    S0=exact_arb(Fraction(ri["label_strip"]))
    Sg=exact_arb(Fraction(fields["physical_angle_strip"]))
    if not 0<m<=J or not image<Sg:raise ValueError("actual characteristic image exceeds field domain")
    CJ=(J/m).upper();delta=(m*S0/4).lower()
    logw=(2*J2/m**2).upper()
    comp=composition_constants(CJ,delta)
    positive=identity(11);backward=identity(11)
    rows=fields["cells"];cursor=Fraction(0)
    hm=[];hp=[];aplus=[]
    # The physical ordinary source is kept separately from all weak sources.
    IF=arb(0);saved_maps=[];phase_rows=[]
    for row in rows:
        left,right=Fraction(row["left"]),Fraction(row["right"])
        if left!=cursor or not left<right:raise ValueError("whole strict field cover has a gap")
        cursor=right
        for key in ("whole_real_radial_interval","whole_complex_angle_strip","whole_parameter_interval",
                    "actual_angular_jets_from_exact_position_ODE"):
            if not row.get(key):raise ValueError("incomplete actual field scope: "+key)
        maps,hmin,hmax,amax=actual_energy(row,10)
        positive=maps["forward"]*positive
        saved_maps.append(maps["backward"])
        hm.append(hmin);hp.append(hmax);aplus.append(amax)
        M={k:upper(v) for k,v in row["complete_complex_field_moduli"].items()}
        mu0=lower(row["geometry"]["mu_modulus_lower"])
        if not mu0>0:raise ValueError("actual complex mu lower bound missing")
        length=exact_arb(right-left)
        IF+=length*M["Fcal"]/mu0
        phase_rows.append((row,length,M,mu0,upper(row["geometry"]["m_modulus_upper"])))
    if cursor!=CUT:raise ValueError("strict physical cut not reached")
    for A in reversed(saved_maps):backward=A*backward
    whole=matrix_positive_upper(positive*backward)
    hmin=min(hm);hmax=max(hp)
    energy_levels=[]
    for k in range(11):
        N=positive_matrix_bound(weighted_principal(whole,k))
        energy_levels.append((N*(hmax/hmin).sqrt()).upper())
    E=max(energy_levels).upper()
    # The factor 2 below is the exact reflection of the positive half.
    Hphase=(CJ*IF).upper()
    integral_residual=arb(0);residual_rows=[]
    max_m=max(z[4] for z in phase_rows)
    max_mu=max(z[2]["mu"] for z in phase_rows)
    max_T=max(z[2]["T"] for z in phase_rows)
    endpoint=phase_rows[-1]
    for row,length,M,mu0,Mm in phase_rows:
        dmods=row["complete_complex_first_derivative_moduli"]
        velocity=M["v"]+M["nu"]
        velocity_theta=upper(dmods["v"]["angular"])+upper(dmods["nu"]["angular"])
        g=CJ*M["Fcal"]/(2*mu0)
        Dg=CJ/(2*mu0)*(M["Fcal_r"]+velocity*M["Fcal_theta"]
             +M["Fcal"]*(M["Lr"]+velocity*M["Ltheta"]+velocity_theta))
        gt=CJ/(2*mu0)*(M["Fcal_theta"]+M["Fcal"]*(M["Ltheta"]+logw))
        Pmh=(Mm*(M["Fcal"]*Hphase+M["a"]*Dg+2*M["mu"]*gt+M["Br"]*g)).upper()
        integral_residual+=2*length*Pmh
        residual_rows.append(dict(left=row["left"],right=row["right"],
            full_h_source_g_modulus=record(g.upper()),full_Dsigma_g_modulus=record(Dg.upper()),
            full_g_theta_modulus=record(gt.upper()),full_P_mh_modulus=record(Pmh)))
    Mm=multiplier(Fraction(21,2),max_m,Sg)
    Mr=multiplier(Fraction(21,2),max_mu.sqrt(),Sg)
    Mt=multiplier(Fraction(21,2),max_T,Sg)
    uf=2**(arb(1)/4)*Mm
    frame_F=(uf*uf+(Mt*uf+Mr)**2).sqrt().upper()
    frame_I=(Mr*Mr+arb(2).sqrt()*Mm*Mm*(1+Mt*Mt)).sqrt().upper()
    epM,epmu,epm=endpoint[2],endpoint[3],endpoint[4]
    defect=2**(arb(3)/4)*multiplier(Fraction(19,2),
                                  epm*epM["Fcal"]*epM["a"]/(2*epmu),Sg)
    Nsource=comp["Nrange"](Fraction(-13,2),Fraction(19,2))
    Norder=comp["Nrange"](Fraction(-11,2),Fraction(21,2))
    ordinary_residual=4*2**(arb(1)/4)*Nsource*multiplier(
                         Fraction(19,2),integral_residual,delta)
    Cerr=(frame_I*E*(defect+ordinary_residual+frame_F)+1).upper()
    B1=comp["cross_constant"](arb(1),constant=True)
    Bh=comp["cross_constant"](Hphase)
    X1=(arb(2)**20*B1*(1+arb(1)/4)).upper()
    Xh=(arb(2)**21*Bh*(1+arb(1)/3)).upper()
    X=(2**(arb(1)/4)*X1+2**(arb(3)/4)*Xh).upper()
    Lbudget=(2*multiplier(Fraction(19,2),
            CJ*epM["Fcal"]*epM["a"]/(2*epmu**2),delta)*Nsource).upper()
    ordering=(arb(2)**6*wiener(11,Hphase,delta)).upper()
    R2=(Cerr+4*(2*X+Lbudget+2**(arb(1)/4)*Norder*ordering)).upper()
    source_gain=(frame_I*E).upper()
    out=dict(kind="actual_full_strict_R46_complete_strong_operator_budget",
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.fields,a.ray)},identity=ident,
        exact_physical_interval=[str(-CUT),str(CUT)],window=[-8,8],
        actual_fourier_lattice="4Z; physical theta period pi/2; Sobolev weights (1+16k^2)^(s/2)",
        physical_momentum="p=a*u_r+b*u_theta; full R46 frame includes T=(a*Lr+b*Ltheta)/2",
        positive_cells=len(rows),actual_all_time_ray_included=True,
        actual_both_characteristic_branches="The paid branch and its exact theta reflection.",
        full_mean_retained=True,both_amplitude_rows_retained=True,both_frequency_cones_retained=True,
        complete_infinite_sources_and_cross_frequency_outputs=True,
        no_per_leaf_energy_norm_equivalence=True,
        positive_half_forward_energy_map=matrix_record(positive),
        positive_half_backward_energy_map=matrix_record(backward),
        whole_both_direction_energy_map=matrix_record(whole),
        half_integer_Cauchy_bounds={str(Fraction(2*k+1,2)):record(v) for k,v in enumerate(energy_levels)},
        uniform_Cauchy_window=[str(Fraction(-21,2)),str(Fraction(21,2))],
        uniform_true_Cauchy_bound=record(E),
        actual_relative_flow=dict(J_label_modulus=record(J),J_label_real_lower=record(m),
            J_second_label_modulus=record(J2),relative_derivative_modulus=record(CJ),
            relative_real_derivative_lower=record(comp["first_derivative_lower"]),
            full_physical_angle_strip=record(delta),
            inverse_label_log_derivative_bound=record(logw)),
        full_strict_phase_modulus=record(Hphase),
        full_both_sides_Pmh_integral=record(integral_residual.upper()),
        complete_residual_rows=residual_rows,
        actual_frame_bounds=dict(F=record(frame_F),inverse_F=record(frame_I)),
        initial_true_momentum_defect=record(defect.upper()),
        complete_ordinary_residual_budget=record(ordinary_residual.upper()),
        actual_source_correction_and_mean_budget=record(Cerr),
        full_cross_cone_and_mean_output_per_branch=record(X),
        full_remaining_momentum_term_per_branch=record(Lbudget),
        full_ordering_multiplier=record(ordering),
        full_composition_source_bound=record(Nsource),
        full_composition_ordering_bound=record(Norder),
        strong_remainder=dict(domain="E_s=(H^s)^2",range="E_(s+2)",
            window=[-8,8],bound=record(R2),
            exact_decomposition="C_strict=W0+R2, with the actual R46 W0 and actual h_sigma, S_sigma"),
        ordinary_source=dict(input="L1(dr; H^(s-1/2)), physical ordinary f",
            output="E_s in the actual full R46 frame",gain=record(source_gain)),
        actual_root_connections_proved=False,actual_positive_Airy_contact_proved=False,
        R104_full_b_identification_proved=False,full_return_Rstar_proved=False,
        effective_R104_cutoff_proved=False,nonlinear_family_complete=False,
        full_strict_normal_form_proved=True,
        actual_scalar_knot_regularity=regularity,
        limitations=["Only the exact displayed closed negative interval is included.",
          "The tiny negative canonical collar is not identified with this interval's physical endpoints.",
          "The large complete constants are not advertised as an effective final high inverse.",
          "No weak divergence-source load has been silently converted into an ordinary source."],
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_strict_actual_wkb_fields.py","fourfold_strict_high_energy_triangular.py",
            "fourfold_phase_beta_bulk_interval.py","fourfold_phase_root_fourier_fit.py")},
        wall_seconds=time.monotonic()-start)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),
        Cauchy=record(E),R2=record(R2),strict_phase=record(Hphase),
        ordinary_source_gain=record(source_gain)),flush=True)
if __name__=="__main__":main()

