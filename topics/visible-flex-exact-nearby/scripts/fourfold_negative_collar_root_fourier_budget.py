#!/usr/bin/env python3
"""Complete R43 negative-collar constants from actual canonical root Fourier data.

The canonical v0/v1 inputs retain a correlated full projected L2 error and
the complete true analytic complement. No finite polynomial is substituted
for the potential. The remaining radial Taylor error is paid by the actual
negative characteristic chart's complete complex potential modulus.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read, save, sha, stored
from fourfold_strict_high_energy_triangular import stirling_rows, power_tail


def record(value):
    x=arb(value)
    if not x.is_finite():raise ValueError("nonfinite complete collar bound")
    return {"ball":x.str(50),"lower":x.lower().str(50),"upper":x.upper().str(50)}


def validate_root(path, order):
    d=read(path)
    if not d.get("proved") or d["kind"]!=f"actual_canonical_v{order}_scaled_Wiener_enclosure":
        raise ValueError("complete actual canonical root trace required")
    if sha(d["source_path"])!=d["source_sha256"]:
        raise ValueError("actual canonical trace producer changed")
    if sha(d["coefficient_path"])!=d["coefficient_sha256"]:
        raise ValueError("actual canonical reference coefficients changed")
    for name in ("fit", "nominal"):
        if sha(d[name+"_path"])!=d[name+"_sha256"]:
            raise ValueError("actual canonical trace input changed: "+name)
    for name,digest in d["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("actual trace scientific dependency changed: "+name)
    c=np.load(d["coefficient_path"],allow_pickle=False)[f"nominal_v{order}_nonnegative"]
    if len(c)!=d["canonical_projection_cutoff"]+1:
        raise ValueError("complete saved canonical projection is missing")
    if order==0 and d["exact_reference_constant"]!=5050:
        raise ValueError("actual residual-v0 reference constant changed")
    return d,[arb(float(v)) for v in c]


def root_moment(d, c, power, order):
    """Whole parameter family, all Fourier modes; correlated low L2 fee."""
    p=Fraction(power);pp=exact_arb(p);n=math.ceil(p)
    error=stored(d["actual_projected_coefficient_L2_error"]).upper()
    strip=stored(d["actual_canonical_inverse_strip"]).lower()
    modulus=stored(d["actual_residual_v0_complex_modulus"] if order==0
                   else d["actual_v1_complex_modulus"]).upper()
    q=(-4*strip).exp();st=stirling_rows(n)
    finite=squares=arb(0);candidates=[]
    for k,coefficient in enumerate(c):
        w=(arb(1)+k*k)**(pp/2)
        multiplicity=1 if k==0 else 2
        finite+=multiplicity*w*abs(coefficient)
        squares+=multiplicity*w*w
        if k<64 or (k%32 and k!=len(c)-1):continue
        # <k>^p <= (k+1)^ceil(p), with every omitted positive mode.
        tail=2*modulus*sum((math.comb(n,j)*power_tail(k+1,q,j,st)
                           for j in range(n+1)),arb(0))
        low=(error*squares.sqrt()).upper()
        total=(finite+low+tail).upper()
        candidates.append((total,dict(split=k,finite_reference_sum=record(finite.upper()),
            complete_correlated_low_L2_fee=record(low),complete_actual_analytic_tail=record(tail.upper()),
            true_full_weighted_l1=record(total))))
    value,best=min(candidates,key=lambda row:row[0])
    return value,best


def analytic_moment(power,modulus,decay):
    n=math.ceil(Fraction(power));q=(-decay).exp()
    return (modulus*(2*math.factorial(n)/(1-q)**(n+1)-1)).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v0",type=Path,default=Path("notes/2026-11-12-ci-canonical-v0-scaled-Wiener.json"))
    ap.add_argument("--v1",type=Path,default=Path("notes/2026-11-12-ci-canonical-v1-scaled-Wiener.json"))
    ap.add_argument("--chart",type=Path,default=Path("notes/2026-11-13-actual-negative-canonical-collar-R43-v2.json"))
    ap.add_argument("--collar-dyadic-power",type=int,default=140)
    ap.add_argument("--window",type=int,default=8)
    ap.add_argument("--bits",type=int,default=320)
    ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.collar_dyadic_power<1 or a.window<0:
        raise ValueError("new output path and valid finite orders required")
    ctx.prec=a.bits;start=time.monotonic()
    d0,c0=validate_root(a.v0,0);d1,c1=validate_root(a.v1,1)
    if d0["identity"]!=d1["identity"]:
        raise ValueError("actual canonical root trace families differ")
    chart=read(a.chart)
    if (not chart.get("complete") or not chart.get("proved") or
        chart["kind"]!="actual_exact_negative_characteristic_collar_R43" or
        not chart["exact_negative_characteristic_coordinates"] or
        not all(g["passed"] for g in chart["gates"])):
        raise ValueError("complete actual negative characteristic chart required")
    if sha(Path(__file__).with_name("fourfold_negative_canonical_actual_collar.py"))!=chart["source_sha256"]:
        raise ValueError("actual negative collar producer changed")
    for path,digest in chart["inputs"].items():
        if sha(path)!=digest:raise ValueError("actual negative collar input changed")
    if d0["identity"]!=chart["identity"]:
        for key in ("center_object_sha256","origin_inputs_sha256","direction_sha256",
                    "exact_center_parameter","exact_parameter_interval"):
            if d0["identity"][key]!=chart["identity"][key]:
                raise ValueError("actual negative chart and root Fourier families differ: "+key)
    fit=read(d0["fit_path"])
    qmin=(4*stored(fit["true_frequency"]).lower()).lower()
    qmax=(4*stored(fit["true_frequency"]).upper()).upper()
    if not qmin>4:raise ValueError("actual quarter-circle normalization unresolved")
    radial=stored(chart["full_analytic_potential_radial_disk"]).lower()
    angle=stored(chart["complete_potential_analytic_strip"]).lower()
    M=stored(chart["chart_bounds"]["full_complex_potential_modulus_before_root_Taylor"]).upper()
    delta=arb(2)**(-a.collar_dyadic_power)
    if not 0<delta<radial/2:raise ValueError("requested negative collar leaves the actual chart")
    z=delta/radial
    r0=(M*z*z/(1-z)).upper()
    r1=(M/radial*z*(2-z)/(1-z)**2).upper()
    decay=(qmin*angle).lower()
    powers={"K":Fraction(a.window)+Fraction(7,3),
            "B":Fraction(a.window)+Fraction(3,2),
            "W":Fraction(a.window)+Fraction(8,3)}
    budgets={};M0={};M1={};full={}
    for name,p in powers.items():
        v0,b0=root_moment(d0,c0,p,0);v1,b1=root_moment(d1,c1,p,1)
        tail0=analytic_moment(p,r0,decay);tail1=analytic_moment(p,r1,decay)
        V=(v0+delta*v1+tail0).upper()
        Vxi=(v1+tail1).upper()
        budgets[name]=dict(power=str(p),actual_root_v0=b0,actual_root_v1=b1,
            full_radial_V_remainder=record(tail0),full_radial_Vxi_remainder=record(tail1),
            full_collar_V_weighted_l1=record(V),full_collar_Vxi_weighted_l1=record(Vxi))
        full[name]=(V,Vxi)
    K0=(100*arb.pi()*2**(exact_arb(powers["K"])/2)*full["K"][0]).upper()
    B1=(100*arb.pi()*2**(exact_arb(powers["B"])/2)*full["B"][0]).upper()
    if not delta*K0<arb(1)/10:
        raise ValueError("actual full-window Airy-Volterra shortness gate failed")
    W=(2**(exact_arb(Fraction(a.window)+Fraction(4,3))/2)
       *(full["W"][0]+full["W"][1])).upper()
    Cq=(4*(50*arb.pi()+5)*qmin**(-arb(4)/3)+150*arb.pi()+3/qmin).upper()
    strong=(2*Cq*W+2*(arb(1)/10).exp()*delta*B1*B1).upper()
    ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    minus_aip0=1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    airy_c=(ai0/minus_aip0).sqrt()
    source=(5*arb(2).sqrt()*arb.pi()/airy_c*(arb(1)/10).exp()).upper()
    out=dict(kind="actual_negative_R43_collar_from_complete_root_Fourier",
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.v0,a.v1,a.chart)},identity=chart["identity"],
        exact_negative_collar_height=str(Fraction(1,2**a.collar_dyadic_power)),
        Sobolev_output_window=[-a.window,a.window],paid_intermediate_window=a.window+2,
        actual_quarter_circle_frequency=[record(qmin),record(qmax)],
        canonical_normalized_angle="quarter circle x=q_quarter*phi, period 2*pi; mode n is R99's physical fourfold index",
        actual_complete_potential_radial_disk=record(radial),
        actual_complete_potential_angle_strip=record(angle),
        true_radial_V_remainder_modulus=record(r0),true_radial_Vxi_remainder_modulus=record(r1),
        complete_root_Fourier_and_radial_budgets=budgets,
        R43_constants={k:record(v) for k,v in dict(K0=K0,delta_K0=delta*K0,B1=B1,W=W,Cq=Cq,
            complete_four_thirds_remainder=strong,forward_and_inverse=(arb(1)/10).exp(),
            canonical_ordinary_L1_source_to_amplitude=source).items()},
        all_modes_all_parameters_and_mean_retained=True,both_amplitudes_and_all_cones_retained=True,
        true_projected_L2_errors_kept_correlated=True,all_infinite_root_and_radial_tails_retained=True,
        complete_returned_Rstar_proved=False,positive_Ai_contact_proved=False,
        finite_Schur_inverse_proved=False,README_completion_proved=False,
        scope="Actual negative characteristic collar only. This is a finite-window full strong operator bound, not an actual full feedback inverse or final cutoff.",
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_strict_high_energy_triangular.py",
            "fourfold_phase_root_fourier_fit.py","fourfold_phase_beta_bulk_interval.py")},
        seconds=time.monotonic()-start)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),seconds=out["seconds"],
        constants=out["R43_constants"]),flush=True)


if __name__=="__main__":main()
