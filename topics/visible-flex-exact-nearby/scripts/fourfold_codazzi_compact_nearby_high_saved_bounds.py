#!/usr/bin/env python3
"""QN: full-tail nearby positive high graph from complete saved bounds.

All operations are rational comparisons or finite combinations of already
proved scalar bounds. No native row, Riccati solve or kernel sweep runs.
"""

from fractions import Fraction as F
import json
from fourfold_codazzi_compact_positive_high_saved_bounds import (
    read, upper, lower, response_rows,
)
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    body, collar, negative, outer = (
        read(k) for k in ("body", "collar", "negative", "raw_outer")
    )
    checks = {}

    def lt(name, x, bound):
        checks[name] = x < F(bound)
        if not checks[name]:
            raise AssertionError(name)

    rho, endpoint = F("1e-6"), F("1e-9")
    tau0, sigma0 = F("1.894e-7"), F("3.788e-7")
    tau = tau0+rho+tau0*rho
    sigma = sigma0+2*rho
    lt("new direct and inverse optical speed ratios", rho/(F("1.068")-F("2e-7")-rho), rho)
    lt("new terminal datum relative ratio", endpoint/(F("5.84461145233")-endpoint), rho)
    lt("all-body K over new W", 180/((1-tau0)*(1-rho)), 181)
    lt("full centre Aw factor below two", F(129,97)**5, 8)
    lt("negative-order near-frequency drift factor below 17", F(8,3)**3*2**8, 17**3)

    U,V,U1,V1 = [2*F(x) for x in (".629","6.407","5.438","5.438")]

    def whole_energy_increment(K, KW):
        du2,dv2 = 2*U*rho+rho*rho, 2*V*rho+rho*rho
        duv = (U+V)*rho+rho*rho
        ds = du2+K*dv2
        local = 2*(4*ds+2*(KW+4)*duv)
        primitive = ((U1+U)*rho+rho*rho
                     +K*((V1+V)*rho+rho*rho)
                     +KW*((U1+V)*rho+rho*rho)
                     +4*((V1+U)*rho+rho*rho))
        return F(35,2)*ds+local+primitive

    de = whole_energy_increment(F(4), F(181))
    lt("complete all-frequency body energy increment over beta", de, 18000*rho)
    dc = F(".211")*whole_energy_increment(F(".00061"), F(1))
    lt("complete all-frequency collar energy increment", dc, 92*rho)
    h = F("9e-6")
    lt("whole nearby base collar feedback", h*(144+dc), F(1,750))
    lt("whole nearby negative collar feedback", h*(F("432.18")+dc), F(1,250))
    coeff = collar["fresh_coefficient_bounds"]
    speed_change = F("1.12")*(F("2.001e-7")+rho)
    lt("nearby collar positive speed lower", F(1,2), lower(coeff["optical_speed_lower"])-speed_change)
    lt("nearby collar positive speed upper", upper(coeff["optical_speed_upper"])+speed_change, F(63,50))
    lt("nearby optical root lower slope", F(29), F("59.74380437")/F("1.26"))
    lt("nearby optical root upper slope", F("60.465470")/F(".5"), F(122))

    # Actual raw endpoint known finite-jet bounds, enlarged only by an
    # unweighted A^3 correction. No exponential weight is assigned to it.
    P, Us, Vs = map(F, ("1.480385e-11","1.643190e-9","9.603792e-9"))
    ml, mu = F("5.84461145233")-endpoint, 7+endpoint
    ua, wa = 145*Us+endpoint, 145*Vs+endpoint
    uphi, vphi = 3336*Us+endpoint, 3336*Vs+endpoint
    e_old = [8*P,32*P,192*P,1536*P]
    e = [v+endpoint*(F(1,4**n)+v)/ml for n,v in enumerate(e_old)]
    e1,e2,e3,e4 = e
    bj0=3336*P
    bj=bj0+endpoint*(1+bj0)/ml
    jlo,jhi,j2=1-e1,1+e1,4*e2
    comp2=(jhi*jhi+j2)/jlo
    invcomp2=jhi*(jlo+j2)/jlo**3
    comp=F("1.000001")
    for n,c in enumerate((comp2,invcomp2,invcomp2/(1-bj),comp2*(1+bj))):
        lt("complete real Hplusminus2 composition "+str(n),c,comp)
    lt("whole endpoint reciprocal multiplier gap",F("5.84"),ml-wa)
    invv=1/F("5.84")
    dC=comp*(invv*invv+vphi*invv**3*(2+wa/ml)/4)
    lt("whole real moving C differential H2",dC,F(".03"))
    lt("A1 embedding from normalized H2",1+F(500,1536),F(6,5)**2)
    bg=outer["background"]
    lt("complete physical Z input",F(bg["Z_A0"])+F(".036")*endpoint,F("4e-11"))
    lt("complete physical Z first angular derivative",F(bg["Z_phi_A0"])+F(".036")*endpoint,F("7e-11"))

    # Complexification is in function parameters in the zero-width algebra.
    exp_error=F(1,2**512)
    b=F(1,2**60)

    def long_budgets(z,bheight):
        rf=10*(z+bheight)
        ff=rf+bheight
        coupling=36*4096*ff
        jf=9/(1-coupling)
        jb=(exp_error+coupling)/(1-coupling)
        return {
            "F":ff,"rf":rf,"kappa":coupling,
            "T":exp_error+4*16384*ff*jf,
            "U":exp_error+4*16384*ff*(1+jb),
        }

    small=long_budgets(F("4e-11"),b)
    wide=long_budgets(F("1e-10"),F("1e-11"))
    rz,rb=F("5e-11"),F("9e-12")
    lt("actual Z function-parameter disc",F("4e-11")+rz,F("1e-10"))
    lt("actual independent height function-parameter disc",b+rb,F("1e-11"))
    # Existing wide-ball inequalities are reused, not rerun as a scientific
    # target; these exact combinations also display the unchanged domains.
    xi=F("7e-11")/rz+16*b/rb
    t1=small["T"]+xi*wide["T"]
    u1=small["U"]+xi*wide["U"]
    T,C,H,V=map(F,(".0012",".00015",".000134",".00001675"))
    lt("complete DN both H1 and Hminus1",t1,T)
    lt("complete height DN both H1 and Hminus1",u1,H)

    pi=F(22,7)
    kh0=e2/jlo+(1+pi)*e1
    kht1=e3/jlo+e2**2/jlo**2+(1+pi*(1+e1))*e2
    kht2=(e4/jlo+3*e2*e3/jlo**2+2*e2**3/jlo**3
          +(1+pi*(1+e1))*e3+(2*pi+(1+e1)*pi*pi)*e2*e2)
    kh=kh0+8*kht1+16*kht2
    lt("complete nearby Hilbert conjugation",kh,F("6e-7"))
    va=mu+wa
    b2=va*va+vphi*va/4
    g=F("5.8")
    lstar=comp*(1+bj)/(g*g)
    e2chart=(wa*(2*mu+wa)+vphi*va/4)*comp*(1+C)
    lt("actual onto nonmean h2 chart",lstar*e2chart,1)
    istar=lstar/(1-lstar*e2chart)
    lt("nearby physical nonmean chart inverse",istar,F(".03"))
    erobin=istar*(
        mu*(comp*(T+exp_error+C)+kh*comp*(1+T+exp_error))
        +wa*comp*(1+T+exp_error)
        +(va*(ua+uphi/4)+(wa*(2*mu+wa)+vphi*va/4)/g)*comp*(1+C)
    )
    boundary_loop=F(17,2)*erobin
    lt("complete physical exterior denominator",boundary_loop,1)
    outer_reflection=boundary_loop/(1-boundary_loop)
    lt("complete physical exterior reflection in both windows",outer_reflection,F(".0025"))
    pref=F(51,16)/(1-boundary_loop)
    ba=va*comp
    ca=va*(ua+uphi/4)+b2/g+erobin*b2
    outer_sources={
        "physical low h2 Hs":pref*erobin,
        "independent height":pref*(ba*H+ca*V),
        "independent Robin residual":pref*ba,
        "independent physical mean residual":pref*ca,
        "moving mean from y":mu*mu*C*istar,
        "moving mean from height":mu*mu*(1+C*istar*b2)*V,
        "moving mean from mean residual":mu*mu*(1+C*istar*b2),
    }
    for name,limit in (
        ("physical low h2 Hs",".001"),
        ("independent height",".004"),
        ("independent Robin residual","23"),
        ("independent physical mean residual","28"),
        ("moving mean from y",".000219"),
        ("moving mean from height",".000822"),
        ("moving mean from mean residual","49.012"),
    ):
        lt(name,outer_sources[name],F(limit))

    orders={o["homogeneous_angular_order"]:o["bounds"] for o in body["orders"]}
    energy_factor=F("1.003")/(1-rho)+de/2
    transfer=energy_factor/(1-2*sigma)
    lt("whole nearby base body plus true exterior",transfer*upper(orders[0]["interior_Volterra_norm"])+outer_reflection,F(".310"))
    lt("whole nearby negative body plus true exterior",transfer*upper(orders[1]["interior_Volterra_norm"])+outer_reflection,F(".801"))
    source_factor,frame_factor=F("1.000003"),F("1.0000006")
    lt("all nearby ordinary source branches",1/((1-tau)*(1-2*sigma)),source_factor**2)
    lt("all nearby reconstruction and raw jumps",1/(1-tau),frame_factor**2)
    lt("whole nearby base source",source_factor*upper(orders[0]["ordinary_source_to_unperturbed_Z_sup"]),F(".126142"))
    lt("whole nearby negative source",source_factor*upper(negative["constants"]["body_unperturbed_source_gain"]),F(".126142"))
    for n in (0,1):
        lt("whole nearby raw reconstruction "+str(n),frame_factor*upper(orders[n]["raw_reconstruction_L2_multiplier"]),F("2.518"))
    lt("whole nearby negative raw body jumps",frame_factor*upper(negative["constants"]["uniform_body_raw_Hminus2over3_jump_to_Y_gain"]),F("4.953"))

    base_loop,base_rows=response_rows(
        chi=F(".310"),qb=F(100,69),Bf=F(".126142"),
        qc=F(750,749),rc=F(1,749),Bc=F(".009"),Cb=F("2.518"))
    neg_loop,neg_rows=response_rows(
        chi=F(".801"),qb=F(1000,199),Bf=F(".126142"),
        qc=F(250,249),rc=F(1,249),Bc=F(".009000020"),Cb=F("2.518"))
    lt("whole nearby base interface",base_loop,F(".000600"))
    lt("whole nearby negative interface",neg_loop,F(".016166"))
    lt("whole nearby base old-root reflection",(tau+base_rows["root_outgoing"][0])/(1-tau),F(".453"))
    lt("whole nearby negative old-root reflection",(tau+neg_rows["root_outgoing"][0])/(1-tau),F("4.129"))
    lt("complete old frame input and output factors",(1+3*tau)*(1+4*tau),F("1.00001"))

    # Infinite nearby cross columns, including the new mean-input high tail.
    q0,qphi,qa13=F("6.407"),F("5.438"),F("8.732")
    qa1=q0+qphi
    qphi13=F("5.06")*qphi
    qphi1=129*qphi
    hl_base=(3072*F(3,2)*(2*qa13+rho)
             +8*18*(2*qa13+rho)
             +24*(qa13+qphi13+rho)+14)
    hl_neg=384*F(3,2)*(2*q0+rho)+18*(2*q0+rho)+3*(q0+qphi+rho)+14
    lh_base=6*(2*q0+rho)*97+18*(2*q0+rho)+3*(q0+qphi+rho)
    lh_neg=385*(6*(2*qa1+rho)*97+18*(2*qa1+rho)+3*(qa1+qphi1+rho))
    ll=hl_neg+14*384
    for name,val,lim in (("infinite low to high Hthird",hl_base,84000),
                         ("infinite low to high Hminus2third",hl_neg,7662),
                         ("infinite high L2 to low",lh_base,7725),
                         ("infinite high Hminus1 to low",lh_neg,6300000),
                         ("full nearby low to low including mean",ll,13038)):
        lt(name,val,F(lim))
    lt("actual nonzero new high to moving mean",12*(q0+rho),77)
    lt("actual constant moving mean input high column",
       18*(2*q0+rho)+3*(q0+qphi+rho)+14,281)

    def show_rows(rows,neg=False):
        names=("body_state_sup","root_outgoing","raw_L2")
        answer={k:[decimal_upper(v,6) for v in rows[k]] for k in names}
        key="outer_even_Hminus5over6_negative" if neg else "outer_even_Hminus5over6_base"
        answer["outer_even_Hminus5over6"]=[decimal_upper(v,6) for v in rows[key]]
        return answer

    print(json.dumps({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "domain":{"whole_positive_unweighted_A3":"1e-6","true_outer_unweighted_A3":"1e-9"},
        "complete_body_feedback":{"base":".310","negative":".801"},
        "complete_outer_reflection_upper":decimal_upper(outer_reflection),
        "complete_outer_independent_columns":{k:decimal_upper(v) for k,v in outer_sources.items()},
        "complete_base_rows":show_rows(base_rows),
        "complete_negative_rows":show_rows(neg_rows,True),
        "full_tail_same_source_state_high_inverse_proved":True,
        "spatial_analyticity_of_unknown_background_assumed":False,
        "true_outer_height_background_still_original_analytic_class":True,
        "old_low193_S_reference_and_193_observations_changed":False,
        "full_low_high_Schur_or_nonlinear_iteration_proved":False,
        "old_native_enclosures_reference_ODEs_and_sweeps":0,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
