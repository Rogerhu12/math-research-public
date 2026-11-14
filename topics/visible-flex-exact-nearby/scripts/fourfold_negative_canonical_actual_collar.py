#!/usr/bin/env python3
"""Actual negative characteristic collar, complete V/V_xi and R43 constants.

All infinite angular modes, the mean and both amplitude branches are retained.
This local negative-collar theorem does not assert a complete returned R_star.
"""
from __future__ import annotations
import argparse,math,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored


LOG=Path("notes/2026-11-13-negative-canonical-log-density-bidisk.json.gz")
ROOT=Path("notes/2026-11-12-actual-root-complex-potential-variation.json.gz")


def norm_bound(r,modulus,decay):
    r=Fraction(r);m=math.ceil(r)
    if r<0:raise ValueError("use absolute Sobolev index")
    z=(-decay).exp()
    # <n>^r <= (n+1)^m <= m! binom(n+m,m), including n=0.
    return (arb(2)**(exact_arb(r)/2)*modulus*
            (2*math.factorial(m)/(1-z)**(m+1)-1)).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--window",type=int,default=8)
    p.add_argument("--collar-dyadic-power",type=int,default=224)
    p.add_argument("--bits",type=int,default=320)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.window<0 or a.collar_dyadic_power<1:
        raise ValueError("new output and nonnegative finite window required")
    ctx.prec=a.bits;tick=time.monotonic();g=read(LOG);r=read(ROOT)
    if not g.get("proved") or not g.get("complete") or not r.get("proved") or r["failed_cells"] or r["pending"]:
        raise ValueError("complete true root geometry inputs required")
    if g["source_sha256"]!=sha(Path(__file__).with_name("fourfold_negative_canonical_log_density.py")):
        raise ValueError("negative log-density producer changed")
    if r["source_sha256"]!=sha(Path(__file__).with_name("fourfold_phase_root_potential_complex_variation.py")):
        raise ValueError("actual v0/v1 root producer changed")
    for d in (g,r):
        for name,digest in d["dependencies"].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError("actual scientific dependency changed "+name)
    for key in ("center_object_sha256","origin_inputs_sha256","direction_sha256","exact_center_parameter"):
        if g["identity"][key]!=r["object"][key]:raise ValueError("root families differ")
    gl,gh=map(Fraction,g["identity"]["exact_parameter_interval"])
    rl,rh=map(Fraction,r["object"]["exact_parameter_interval"])
    if not rl<=gl<gh<=rh:raise ValueError("true root coefficient family is too small")
    R,S=exact_arb(Fraction(g["rho_radius"])),exact_arb(Fraction(g["physical_angle_strip"]))
    M={k:stored(v).upper() for k,v in g["complete_true_moduli"].items()}
    Q,K,Y=M["q"],M["kstar"],M["Yprime_extension"]
    root_bounds=r["uniform_bounds"]
    m=max(stored(g["root_angle_derivative_real_lower"]).lower(),
          stored(root_bounds["Y_prime_real_lower"]).lower())
    if not Fraction(r["exact_physical_angle_strip"])>=Fraction(g["physical_angle_strip"]):
        raise ValueError("root inverse-angle strip does not cover the input strip")
    # Exact fixed radii. The inverse map uses rho and y=Y0(theta).
    rf=arb(1)/10000
    sf=arb(1)/100
    stheta=arb(1)/800
    radius=arb(1)/10000000
    gates=[]
    def gate(name,ok):
        gates.append({"name":name,"passed":bool(ok)})
        if not ok:raise ValueError(name)
    gate("full characteristic radial disk",Fraction(1,10000)==Fraction(1,100)**2 and rf<R)
    movement=Q*rf+arb(2)/3*K*sf**3
    margin=S-stheta-movement
    gate("both complex characteristic flows stay in true angular strip",margin>0)
    exponent=(Q*rf+arb(2)/3*K*sf**3)/margin
    branch_lipschitz=exponent.exp()
    delta_modulus=Y*K*branch_lipschitz
    angular_error_modulus=Y*movement
    # Delta=(3/4)(Tplus-Tminus)/s^3 is even holomorphic and Delta(0)=1.
    epsilon4=(delta_modulus+1)*4*radius/rf
    gate("deflated characteristic difference has its real branch",epsilon4<arb(1)/4)
    power_difference=arb(2)/3*epsilon4/(1-epsilon4)**(arb(1)/3)
    Ex=(4*radius*power_difference).upper()
    Ey=(angular_error_modulus*4*radius/rf).upper()
    youter=m*stheta
    ytarget=youter/4
    contraction=max((Ex/radius).upper(),(Ey/ytarget).upper())
    gate("global holomorphic canonical inverse contraction",contraction<arb(1)/2)
    gate("inverse domain remains within full characteristic disk",4*radius<rf)
    epsilon2=(delta_modulus+1)*2*radius/rf
    ML=(M["logU"]/2-(1-epsilon2).log()/3).upper()
    potential_radius=radius/2
    potential_strip=ytarget/2
    Vcoarse=(ML*(4+ML)*(1/radius**2+potential_radius/ytarget**2)).upper()
    delta=arb(2)**(-a.collar_dyadic_power)
    gate("actual positive-length negative collar lies in true chart",0<delta<potential_radius/2)
    z=delta/potential_radius
    V0=stored(root_bounds["v0_complex_modulus_upper"]).upper()
    V1=stored(root_bounds["v1_complex_modulus_upper"]).upper()
    gate("actual root traces lie in their certified inverse-angle strip",
         potential_strip/m<exact_arb(Fraction(r["exact_physical_angle_strip"])))
    tail0=(Vcoarse*z*z/(1-z)).upper()
    # Stable form of (1-z)^-2-1; no subtraction of nearly equal balls.
    tail1=(Vcoarse/potential_radius*z*(2-z)/(1-z)**2).upper()
    MV=min(Vcoarse,(V0+delta*V1+tail0).upper())
    MVxi=(V1+tail1).upper()
    # Work on the actual D4 quarter circle. Fourfold scaling is explicit.
    qmin=(4*stored(root_bounds["full_circle_frequency_lower"]).lower()).lower()
    qmax=(4*stored(root_bounds["full_circle_frequency_upper"]).upper()).upper()
    gate("canonical quarter-circle frequency and mean convention",qmin>4 and qmax>=qmin)
    decay=(qmin*potential_strip).lower()
    Sbudget=a.window
    # Includes the intermediate/dual/output layers through S+2.
    Mk=norm_bound(Fraction(Sbudget)+Fraction(7,3),MV,decay)
    Mb=norm_bound(Fraction(Sbudget)+Fraction(3,2),MV,decay)
    K0=(100*arb.pi()*Mk).upper()
    B1=(100*arb.pi()*Mb).upper()
    gate("all intermediate Airy-Volterra layers are short",delta*K0<arb(1)/10)
    power=Fraction(Sbudget)+Fraction(8,3)
    # W_s uses a different outer factor from M_power.
    W=(norm_bound(power,MV+MVxi,decay)/
       arb(2)**(arb(2)/3)).upper()
    Cq=(4*(50*arb.pi()+5)*qmin**(-arb(4)/3)+150*arb.pi()+3/qmin).upper()
    strong=(2*Cq*W+2*(arb(1)/10).exp()*delta*B1*B1).upper()
    ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    minus_aip0=1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    airy_c=(ai0/minus_aip0).sqrt()
    source=(5*arb(2).sqrt()*arb.pi()/airy_c*(arb(1)/10).exp()).upper()
    report={"kind":"actual_exact_negative_characteristic_collar_R43",
        "complete":True,"proved":True,"source_sha256":sha(__file__),
        "inputs":{str(LOG):sha(LOG),str(ROOT):sha(ROOT)},"identity":g["identity"],
        "exact_negative_characteristic_coordinates":True,
        "positive_finite_chart_used":False,
        "quarter_circle_frequency_lower":ball_record(qmin),
        "quarter_circle_frequency_upper":ball_record(qmax),
        "complete_potential_analytic_strip":ball_record(potential_strip),
        "full_analytic_potential_radial_disk":ball_record(potential_radius),
        "larger_real_negative_collar_height":ball_record(potential_radius/2),
        "larger_real_collar_true_V_bound":ball_record(Vcoarse),
        "larger_real_collar_true_Vxi_bound":ball_record((2*Vcoarse/potential_radius).upper()),
        "negative_collar_height":str(Fraction(1,2**a.collar_dyadic_power)),
        "Sobolev_output_window":Sbudget,
        "paid_intermediate_window":Sbudget+2,
        "chart_bounds":{k:ball_record(v) for k,v in {
            "characteristic_rho_radius":rf,"physical_start_strip":stheta,
            "complex_physical_angle_movement":movement,"remaining_analytic_angle_margin":margin,
            "characteristic_variation_exponent":exponent,
            "deflated_difference_modulus":delta_modulus,
            "phi_minus_Y0_modulus_on_outer_disk":angular_error_modulus,
            "root_angle_real_derivative_lower":m,
            "canonical_inverse_target_radial_disk":radius,
            "canonical_inverse_target_angle_strip":ytarget,
            "canonical_inverse_contraction":contraction,
            "log_canonical_density_modulus":ML,
            "full_complex_potential_modulus_before_root_Taylor":Vcoarse}.items()},
        "root_Taylor_remainder":{k:ball_record(v) for k,v in
            {"V_minus_v0_xi_v1":tail0,"Vxi_minus_v1":tail1}.items()},
        "complete_true_V_modulus":ball_record(MV),
        "complete_true_Vxi_modulus":ball_record(MVxi),
        "all_Fourier_mode_decay":ball_record(decay),
        "R43_constants":{k:ball_record(v) for k,v in {
            "uniform_K0":K0,"delta_K0":delta*K0,"uniform_B1":B1,
            "uniform_W":W,"Cq":Cq,"full_negative_collar_four_thirds_remainder":strong,
            "homogeneous_forward_and_inverse":(arb(1)/10).exp(),
            "canonical_ordinary_L1_source_to_amplitude":source}.items()},
        "gates":gates,"mean_and_all_cones_retained":True,
        "complete_returned_R_star_proved":False,
        "strict_negative_R46_remainder_proved":False,
        "positive_Ai_contact_completion_proved":False,
        "scope":"Actual exact negative collar only. The very short chosen collar and large strong constant do not close the practical full-return cutoff or the physical source/frame wiring.",
        "seconds":time.monotonic()-tick}
    save(a.out,report)
    print({"out":str(a.out),"sha256":sha(a.out),"potential":report["complete_true_V_modulus"],
        "potential_xi":report["complete_true_Vxi_modulus"],"constants":report["R43_constants"]},flush=True)


if __name__=="__main__":main()
