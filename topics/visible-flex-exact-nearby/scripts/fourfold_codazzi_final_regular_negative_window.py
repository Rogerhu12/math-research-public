#!/usr/bin/env python3
"""Exact actual-final exterior H^-3/2 graph and height-normalized ports.

Only previously published outward text bounds of the same ac1d centre are
consumed. Every inequality uses Fraction; displayed decimal ceilings are not
used in gates. No lost candidate/native data are reconstructed by this file.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
INPUTS = [
    "results/R133-supplement-final-moving-centre-actual-regular-boundary.md",
    "results/R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md",
    "results/R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md",
    "results/R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md",
    "results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md",
    "results/R133-supplement-residual-sensitive-vector-height-and-Airy-contact.md",
]

def ceil_decimal(x: F, digits=30):
    with localcontext() as ctx:
        ctx.prec = digits + 32
        ctx.rounding = ROUND_CEILING
        value = Decimal(x.numerator) / Decimal(x.denominator)
        return str(value.quantize(Decimal(1).scaleb(-digits)))

def record(x: F):
    return {"exact_rational": str(x), "decimal_upper": ceil_decimal(x)}

def run_budget():
    gates = []
    def gate(name, condition, **values):
        entry = {"name": name, "passed": bool(condition), **values}
        gates.append(entry)
        if not condition:
            raise AssertionError(name)

    one, eps = F(1), F(1, 2**512)
    P, Za = F("0.00000000001480385"), F("0.0000000000002533")
    mg, mlo, mup = F(29, 5), F("5.84461145233"), F(7)
    x, dmin, B = F(607, 1000), F("0.124999999985"), F(1, 2**60)
    ep, term = one, one
    for j in range(1, 9):
        term *= 4*dmin/j
        ep += term
    gate("complete_physical_tail_geometric_ratio", ep > 1/x)

    tails = []
    om = one-x
    for N in range(1, 65):
        n = F(N+1)
        sum2 = x**(N+1)*(n*n/om + 2*n*x/om**2 + x*(1+x)/om**3)
        sum3 = x**(N+1)*(n**3/om + 3*n*n*x/om**2
                         + 3*n*x*(1+x)/om**3 + x*(1+4*x+x*x)/om**4)
        z1 = 4*N*Za + 32*P/mg*sum2
        z2 = (4*N)**2*Za + 128*P/mg*sum3
        tails.append((N, z1, z2))
    best1 = min(tails, key=lambda t: t[1])
    best2 = min(tails, key=lambda t: t[2])
    Z1, Z2 = best1[1], best2[2]
    B1, B2 = 16*B, 512*B
    zbar, bbar, rhoZ, rhoB = F(1, 10**10), F(1, 10**11), F(9, 10**11), F(9, 10**12)
    gate("actual_point_inside_two_complete_background_discs", Za+rhoZ < zbar and B+rhoB < bbar)

    RC, RD, R0 = F(4096), F(16384), F(2048)
    def rows(z, b):
        rf = 10*(z+b)
        ff = rf+b
        kap = 36*RC*ff
        jf, jb = 9/(1-kap), (eps+kap)/(1-kap)
        return dict(rf=rf, F=ff, kap=kap, jf=jf, jb=jb,
                    T=eps+4*RD*ff*jf, C=4*R0*ff*jf,
                    U=eps+4*RD*ff*(1+jb), V=4*R0*ff*(1+jb),
                    image=9*z+eps*b+9*RC*ff**2)
    wide, small = rows(zbar, bbar), rows(F(1, 10**12), B)
    gate("complete_L2_module_and_complex_background_domain",
         2*wide['F'] < F(1, 2**25) and 6*wide['F'] < F(1, 2**20)
         and wide['kap'] < F(1, 1000) and wide['image'] < wide['rf'])
    Xi1, Xi2 = Z1/rhoZ+B1/rhoB, Z2/rhoZ+B2/rhoB
    ops = {}
    paid = dict(T=F(1,500), C=F(1,4000), U=F("0.000222223"), V=F("0.0000277779"))
    for k in ("T", "C", "U", "V"):
        ad1 = wide[k]*Xi1
        ad2 = wide[k]*(2*Xi1**2+Xi2)
        Htwo = small[k]+2*ad1+ad2
        ops[k] = dict(L2=small[k], ad1=ad1, ad2=ad2, Htwo=Htwo,
                      negative_three_halves_fourth_power=small[k]*Htwo**3,
                      paid_negative_three_halves=paid[k])
        gate("true_"+k+"_negative_three_halves_by_exact_fourth_power",
             small[k]*Htwo**3 < paid[k]**4)

    e1, e2, e3, e4 = 8*P, 32*P, 192*P, 1536*P
    amin, pi = 1-e1, F(22, 7)
    K0 = e2/amin + (1+pi)*e1
    Ktr1 = e3/amin+e2**2/amin**2+(1+pi*(1+e1))*e2
    Ktr2 = (e4/amin+3*e2*e3/amin**2+2*e2**3/amin**3
            +(1+pi*(1+e1))*e3+(2*pi+(1+e1)*pi*pi)*e2**2)
    KH = K0+8*Ktr1+16*Ktr2
    gate("complete_Hilbert_kernel_both_signs_two_commutators", KH < F("0.0000006"))

    bj, jmax, jmin, j2 = 3336*P, 1+e1, 1-e1, 128*P
    C2, Ci2 = (jmax*jmax+j2)/jmin, jmax*(jmin+j2)/jmin**3
    Cneg, Cineg = Ci2/(1-bj), C2*(1+bj)
    comp = F(10000001, 10000000)
    gate("true_composition_and_inverse_all_orders_minus_two_to_two",
         max(C2, Ci2, Cneg, Cineg) < comp)

    Us, Vs = F("0.000000001643190"), F("0.000000009603792")
    uA, wA, u1, v1 = 145*Us, 145*Vs, 3336*Us, 3336*Vs
    vA = mup+wA
    gate("complete_Btwo_inverse_v_Neumann", mg < mlo-wA)
    T, C, U, V = (paid[k] for k in ("T", "C", "U", "V"))
    qmin = F("0.9999999999993")
    gate("complete_physical_C_to_B_inverse", 1/(qmin-T) < F("1.002005"))

    lead = comp*(1+bj)/mg**2
    Btwo = vA**2+v1*vA/4
    E2 = (wA*(14+wA)+v1*vA/4)*comp*(1+C)
    chart_inv = lead/(1-lead*E2)
    gate("onto_full_nonmean_h2_chart_with_true_weighted_mean", lead*E2 < F(1,10**5) and chart_inv < F(3,100))
    first = 7*(comp*(T+eps+C)+KH*comp*(1+T+eps))
    rest = wA*comp*(1+T+eps)+(vA*(uA+u1/4)+(wA*(14+wA)+v1*vA/4)/mg)*comp*(1+C)
    E = (first+rest)*chart_inv
    mean = 49*C*chart_inv
    gate("complete_moving_negative_Robin_remainder", E < F("0.000469081"))
    Baff = vA*comp
    Caff = vA*(uA+u1/4)+Btwo/mg+E*Btwo
    A = F(17,2)*E
    Ninv, Do = 1/(1-A), F(51,16)
    reflection, head = A*Ninv, Do*E*Ninv
    fB, rB, rC = Do*(Baff*U+Caff*V)*Ninv, Do*Baff*Ninv, Do*Caff*Ninv
    meanFB, meanC = 49*(1+C*chart_inv*Btwo)*V, 49*(1+C*chart_inv*Btwo)
    gate("actual_height_normalized_high_outer_feedback", A < F("0.003988"))
    gate("complete_high_reflection", reflection < F("0.004004"))
    gate("complete_low_to_high_column", head < F("0.001502"))
    gate("independent_full_outer_height_source", fB < F("0.005732"))
    gate("ordinary_physical_Robin_residual", rB < F("22.402"))
    gate("independent_scalar_mean_residual_in_nonmean_graph", rC < F("27.111"))
    gate("true_mean_on_negative_Sobolev_input", mean < F("0.000364151"))
    gate("independent_fB_in_true_mean", meanFB < F("0.001361613"))
    gate("independent_scalar_mean_output", meanC < F("49.017844"))
    gate("scaled_mean_high_column_has_no_inverse_nR", 3*mean < F("0.001092453"))
    lift1 = vA*comp*(1+T+eps)+vA*(uA+u1/4)*comp*(1+C)
    lift2 = Btwo*comp*(1+C)
    gate("complete_two_row_moving_graph_lift", lift1**2+lift2**2 < 2500)
    nR = F("0.000007")**2/mg**2
    gate("actual_outer_height_normalization", nR < F("0.0000000000015"))
    assert len(gates) == 25

    values = dict(K0=K0, Ktr1=Ktr1, Ktr2=Ktr2, KH=KH, bj=bj,
                  composition_positive=C2, inverse_positive=Ci2,
                  composition_negative=Cneg, inverse_negative=Cineg,
                  u_Btwo=uA, vminusmean_Btwo=wA, u_phi_Btwo=u1, v_phi_Btwo=v1,
                  chart_inverse=chart_inv, Robin_remainder=E, feedback=A,
                  high_reflection=reflection, low_column=head,
                  fB_column=fB, Robin_residual_column=rB, mean_residual_column=rC,
                  mean_row=mean, mean_fB=meanFB, mean_residual=meanC,
                  mean_from_scaled_high=3*mean, nR_upper=nR)
    source = Path(__file__).resolve()
    return dict(
        kind="actual_final_regular_negative_Sobolev_window_and_height_ports",
        complete=True, gates=gates, arithmetic="Python Fraction exact rational; decimal displays rounded upward",
        candidate_sha256=CANDIDATE,
        producer={"path":"scripts/"+source.name,"sha256":hashlib.sha256(source.read_bytes()).hexdigest()},
        inputs=[{"path":p,"sha256":hashlib.sha256((TOPIC/p).read_bytes()).hexdigest()} for p in INPUTS],
        background=dict(physical_Z_A0=str(Za), independent_fB_dotA2_sigma=str(B),
                        independent_fB_background_sigma_at_least="1/16", physical_phase_strip="1/8",
                        Z_phi=record(Z1), Z_phi_phi=record(Z2), selected_tail_split_for_Zphi=best1[0],
                        selected_tail_split_for_Zphiphi=best2[0], rhoZ=str(rhoZ),rhoB=str(rhoB),
                        Xi1=record(Xi1),Xi2=record(Xi2)),
        full_tail_bounds=[dict(N=N, Z_phi=record(z1),Z_phi_phi=record(z2)) for N,z1,z2 in tails],
        full_L2_module_wide={k:record(v) for k,v in wide.items()},
        derivative_realizations={k:{kk:record(vv) for kk,vv in v.items()} for k,v in ops.items()},
        values={k:record(v) for k,v in values.items()},
        normative_contract=dict(
            derivative_window="same actual derivative on H^s for -2<=s<=2; paid numerical outer graph uses s=-3/2",
            independent_fB_direction="||<D>^(-3/2)|D|^2 delta fB||L2; physical nonmean",
            high_cutoff="all physical frequencies M=|4j| with |j|>=97",
            low_head="all 1<=|j|<=96; mean is an independent attached row",
            height_state="tilde Z=nR M^(-5/3) Zcurvature, nR=a(R)^2/m(R)^2",
            mean_state="tilde z=nR <h2>; no nonzero-frequency definition is used for mean",
            high_homogeneous="0.004004",
            low_affine="nR*0.001502*||y_L||H^(-3/2)",
            fB_affine="nR*0.005732*||delta fB||dotH^(2,-3/2)",
            Robin_affine="nR*22.402*||rB||H^(-3/2)",
            scalar_affine="nR*27.111*abs(rC)",
            scaled_mean_high="0.001092453*(||tilde Zs||+||tilde Zu||)",
            scaled_mean_low_source="nR*(0.000364151*||yL||H^(-3/2)+0.001361613*FB+49.017844*abs(rC))"),
        permissions=dict(actual_nonlinear_DN_derivative_negative_window=True,
                         complete_mean_and_all_frequency_boundary_rows=True,
                         raw_composition_minus_identity_same_order_small=False,
                         arbitrary_rough_nonlinear_background_ball=False,
                         whole_positive_body_inverse=False,negative_return_inverse=False,
                         finite_head_inverse=False,nu_Schur_nonzero=False,nonlinear_closed_surface=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = run_budget()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"complete":report['complete'],"gates":len(report['gates']),
                      "out":str(args.out), "values":{k:report['values'][k]['decimal_upper']
                        for k in ('Robin_remainder','high_reflection','nR_upper')}}))
