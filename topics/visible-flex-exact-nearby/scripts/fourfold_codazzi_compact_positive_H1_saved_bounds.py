#!/usr/bin/env python3
"""QH: real H2 exterior DN and actual positive H1 graph.

Only exact rational transformations of completed scalar conclusions run.
No coefficient rows, Fourier tails, reference ODEs or kernel sweeps run.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

from fourfold_codazzi_compact_positive_high_saved_bounds import (
    read, upper, strict_sqrt_upper,
)
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    body, negative = read("body"), read("negative")
    old_path = (Path(__file__).resolve().parents[1] / "notes" /
                "2026-11-14-R133-final-regular-negative-window-rational.json")
    raw = old_path.read_bytes()
    if sha256(raw).hexdigest() != (
            "2c2c9c9f1973207061a03f892256350670dc486b893906ce773a8b4e0616edb7"):
        raise AssertionError("completed original second-translation conclusion")
    old = json.loads(raw)
    if not old["complete"]:
        raise AssertionError("complete original second-translation conclusion")
    # This reads the final proved bound only. The old tail list is not used.
    old_z2 = F(old["background"]["Z_phi_phi"]["exact_rational"])
    checks = {}

    def lt(name, x, y):
        checks[name] = x < F(y)
        if not checks[name]:
            raise AssertionError(name)

    endpoint, rho = F("1e-9"), F("1e-6")
    P, Us, Vs = map(F, ("1.480385e-11", "1.643190e-9", "9.603792e-9"))
    ml0, ml, mu = F("5.84461145233"), F("5.84461145233")-endpoint, 7+endpoint
    t = 1/F("5.84")
    old_der = [8*Vs, 128*Vs, 3072*Vs, 98304*Vs]
    v1,v2,v3 = [x+endpoint for x in old_der[:3]]
    eold = [8*P,32*P,192*P,1536*P]
    jets = [v+endpoint*(F(1,4**n)+v)/ml for n,v in enumerate(eold)]
    jlo,jhi = 1-jets[0],1+jets[0]
    # Exact Lipschitz bound for B3(v,m)=C_{theta theta theta} o theta.
    l3 = (3*mu**2*v3*t**5 + mu**3*t**5 + 5*mu**3*v3*t**6
          +10*(3*mu**2*v1*v2*t**6 + mu**3*(v1+v2)*t**6
               +6*mu**3*v1*v2*t**7)
          +15*(3*mu**2*v1**3*t**7 + 3*mu**3*v1**2*t**7
               +7*mu**3*v1**3*t**8))
    a1,a2,a3,a4 = old_der
    # The fourth derivative occurs only in the known analytic centre.
    g3 = 7**3*(a4*t**5+(15*a1*a3+10*a2*a2)*t**6
               +105*a1*a1*a2*t**7+105*a1**4*t**8)
    shift = (1+Vs/ml0)/(4*ml*jlo)
    physical_third = jhi*l3 + shift*g3
    lt("third physical derivative difference per endpoint A3", physical_third, ".051")
    lt("fourfold mean-zero H1 to A0 embedding", F(22,7)**2/48, F(".46")**2)
    z2 = old_z2+F(".46")*physical_third*endpoint
    lt("actual whole second physical translation", z2, "1.9e-9")

    epsilon,b = F(1,2**512),F(1,2**60)

    def dn(z,bh):
        ff=10*z+11*bh
        coupling=36*4096*ff
        jf=9/(1-coupling)
        jb=(epsilon+coupling)/(1-coupling)
        return (epsilon+4*16384*ff*jf,
                epsilon+4*16384*ff*(1+jb))

    smallT,smallU=dn(F("4e-11"),b)
    wideT,wideU=dn(F("1e-10"),F("1e-11"))
    rz,rb=F("5e-11"),F("9e-12")
    xi1=F("7e-11")/rz+16*b/rb
    xi2=F("1.9e-9")/rz+512*b/rb
    real_translation=2*xi1+2*xi1**2+xi2
    t2=smallT+wideT*real_translation
    u2=smallU+wideU*real_translation
    lt("actual DN on every Hs with abs s at most two", t2, ".030")
    lt("actual height DN on every Hs with abs s at most two", u2, ".003334")
    lt("actual mean curvature row Hplusminus2", (t2-epsilon)/8, ".00375")
    lt("actual height to mean row Hplusminus2", (u2-epsilon)/8, ".00041675")
    T,C,U,V=map(F,(".0021",".0002625",".000234",".00002925"))
    lt("actual DN Hseven-sixths by interpolation", F(".0012")**5*F(".030"), T**6)
    lt("actual height DN Hseven-sixths by interpolation", F(".000134")**5*F(".003334"), U**6)

    # All real composition, multiplier and Hilbert qualifications are QN's
    # completed Hplusminus2 bounds on the same endpoint domain.
    ua,wa=145*Us+endpoint,145*Vs+endpoint
    uphi,vphi=3336*Us+endpoint,3336*Vs+endpoint
    bj=3336*P+endpoint*(1+3336*P)/ml
    comp,kh,g=F("1.000001"),F("6e-7"),F("5.8")
    va=mu+wa
    b2=va*va+vphi*va/4
    lstar=comp*(1+bj)/(g*g)
    echart=(wa*(2*mu+wa)+vphi*va/4)*comp*(1+C)
    lt("actual Hseven-sixths onto chart denominator", lstar*echart,1)
    istar=lstar/(1-lstar*echart)
    lt("actual Hseven-sixths nonmean chart inverse", istar,".03")
    E=istar*(
        mu*(comp*(T+epsilon+C)+kh*comp*(1+T+epsilon))
        +wa*comp*(1+T+epsilon)
        +(va*(ua+uphi/4)+(wa*(2*mu+wa)+vphi*va/4)/g)*comp*(1+C))
    ao=F(17,2)*E
    lt("actual positive H1 exterior denominator",ao,1)
    reflection=ao/(1-ao)
    lt("actual positive H1 complete exterior reflection",reflection,".0043")
    ba=va*comp
    ca=va*(ua+uphi/4)+b2/g+E*b2
    pref=F(51,16)/(1-ao)
    affine={
        "physical low h2 Hseven-sixths":pref*E,
        "independent height Hseven-sixths":pref*(ba*U+ca*V),
        "independent Robin residual Hseven-sixths":pref*ba,
        "independent physical mean residual":pref*ca,
        "moving mean from nonmean y":mu*mu*C*istar,
        "moving mean from independent height":mu*mu*(1+C*istar*b2)*V,
        "moving mean from mean residual":mu*mu*(1+C*istar*b2),
    }
    for k,vlim in (
        ("physical low h2 Hseven-sixths",".002"),
        ("independent height Hseven-sixths",".0061"),
        ("independent Robin residual Hseven-sixths","23"),
        ("independent physical mean residual","28"),
        ("moving mean from nonmean y",".000383"),
        ("moving mean from independent height",".001435"),
        ("moving mean from mean residual","49.020")):
        lt(k,affine[k],vlim)

    tau0,sigma0=F("1.894e-7"),F("3.788e-7")
    tau=tau0+rho+tau0*rho
    sigma=sigma0+2*rho
    # QN's already proved whole-row increment D < 18000 rho is used.
    transfer=(F("1.003")/(1-rho)+9000*rho)/(1-2*sigma)
    orders={o["homogeneous_angular_order"]:o["bounds"] for o in body["orders"]}
    interior=transfer*upper(orders[1]["interior_Volterra_norm"])
    lt("positive order-one body and true exterior",interior+reflection,".803")
    lt("nearby source branches",1/((1-tau)*(1-2*sigma)),F("1.000003")**2)
    lt("positive Hfour-thirds ordinary source gain",
       F("1.000003")*upper(negative["constants"]["body_unperturbed_source_gain"]),".126142")
    lt("positive H1 body reconstruction",
       F("1.0000006")*upper(orders[1]["raw_reconstruction_L2_multiplier"]),"2.518")
    lt("positive Hfour-thirds original raw jumps",
       F("1.0000006")*upper(negative["constants"]["uniform_body_raw_Hminus2over3_jump_to_Y_gain"]),"4.953")
    lt("positive H1 true collar gate",
       F("9e-6")*(F("432.18")+92*rho),F(1,250))
    lt("positive H1 collar raw reconstruction",
       9*(1+F(1,388**2)),F("3.00001")**2)
    lt("positive one-third extra mixed root output",
       9**3*(1+F(1,388**2))**2,F("9.00005")**3)
    lt("physical Hseven-sixths high Bessel conversion",
       (1+F(1,388**2))**7,F(17,16)**12)
    # H^{7/6} h2 at the actual endpoint costs less than five, retaining
    # both branches. H^{1/6} costs the already conservative 5/388.
    lt("actual positive Hseven-sixths outer trace",
       16**6*(1+F(1,388**2))**7,5**12)

    qc,rc,qb=F(250,249),F(1,249),F(1000,197)
    chi,Bf,Bc,Cb=F(".803"),F(".126142"),F(".009000020"),F("2.518")
    rb_body=chi*qb
    loop=rc*rb_body
    lt("whole positive H1 collar-body loop",loop,".016371")
    resolvent=1/(1-loop)
    rows={k:[] for k in (
        "body_frame_sup","root_outgoing","raw_L2r_H1",
        "outer_even_Hone_sixth","outer_even_Hseven_sixths")}
    for port in range(7):
        s,fc,fb,boundary,jc,js,ju=[F(int(i==port)) for i in range(7)]
        x=resolvent*(qc*s+qc*(Bc*fc+jc)+js+rc*(qb*(Bf*fb+boundary)+ju))
        y=rb_body*x+qb*(Bf*fb+boundary)+ju
        outgoing=rc*s+qc*y+qc*(Bc*fc+jc)
        sb=qb*(x+Bf*fb+boundary)
        sc=qc*(s+y+Bc*fc+jc)
        raw2=F("9e-6")*F("3.00001")**2*sc*sc+Cb*Cb*sb*sb
        rows["body_frame_sup"].append(sb)
        rows["root_outgoing"].append(outgoing)
        rows["raw_L2r_H1"].append(strict_sqrt_upper(raw2))
        rows["outer_even_Hone_sixth"].append(F(5,388)*sb)
        rows["outer_even_Hseven_sixths"].append(5*sb)
    old_root=(tau+rows["root_outgoing"][0])/(1-tau)
    lt("actual positive H1 original-coordinate root reflection",old_root,"4.182")
    lt("complete unchanged root input-output conversion",(1+3*tau)*(1+4*tau),"1.00001")
    lt("additive old root reflection covered by displayed factor",
       (tau+rows["root_outgoing"][0])/(1-tau),
       F("1.00001")*rows["root_outgoing"][0])
    print(json.dumps({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "physical_third_difference_per_endpoint_A3":decimal_upper(physical_third,9),
        "physical_second_translation_A0_upper":decimal_upper(z2,18),
        "actual_Hplusminus2_DN":{
            "T":decimal_upper(t2,9),"C":decimal_upper((t2-epsilon)/8,9),
            "U":decimal_upper(u2,9),"V":decimal_upper((u2-epsilon)/8,9)},
        "actual_Hseven_sixths_DN":{"T":str(T),"C":str(C),"U":str(U),"V":str(V)},
        "actual_outer_reflection_upper":decimal_upper(reflection,9),
        "actual_outer_independent_columns":{k:decimal_upper(v,9) for k,v in affine.items()},
        "actual_body_interior_upper":decimal_upper(interior,9),
        "complete_positive_H1_feedback":".803",
        "complete_positive_H1_rows":{
            k:[decimal_upper(v,6) for v in vals] for k,vals in rows.items()},
        "actual_original_coordinate_root_reflection":decimal_upper(old_root,9),
        "raw_ordinary_source":"L2_r H^{4/3}; all original jumps H^{4/3}",
        "actual_raw_state":"L2_r H^1",
        "endpoint_DN_background":"real unweighted A^3 <= 1e-9",
        "whole_background":"real unweighted A^3 <= 1e-6",
        "independent_outer_height_background":"dot A^2_sigma <= 2^-60; sigma >= 1/16",
        "unknown_spatial_analyticity_assumed":False,
        "fourth_derivative_of_unknown_background_used":False,
        "actual_infinite_high_inverse_with_complete_given_head":True,
        "complete_low_high_Schur_or_all_order_tame_inverse_proved":False,
        "old_native_rows_tail_evaluations_reference_ODEs_and_sweeps":0,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
