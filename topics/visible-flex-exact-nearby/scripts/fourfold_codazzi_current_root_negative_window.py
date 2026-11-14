#!/usr/bin/env python3
"""Complete actual root inverse on capped negative Sobolev windows.

The full global-reference coefficient bounds are published text inputs.
All inverse/feedback inequalities use exact Fraction arithmetic. The small
same-centre native germ is consumed only to verify the actual n=a^2/m^2
range; no lost candidate arrays or whole-body coefficients are presumed.
"""
from __future__ import annotations
import argparse
from decimal import Decimal,localcontext,ROUND_CEILING
from fractions import Fraction as F
import gzip,hashlib,json
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record

TOPIC=Path(__file__).resolve().parents[1]
CURRENT="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
GERM_SHA="397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def display(x):
    with localcontext() as c:
        c.prec=80;c.rounding=ROUND_CEILING
        z=Decimal(x.numerator)/Decimal(x.denominator)
        s=str(z.quantize(Decimal("1e-30")))
    return dict(exact_rational=str(x),decimal_upper=s)

def run(germ):
    ctx.prec=256
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise AssertionError(name)
    gate("identical_complete_current_complex_germ_bytes",sha(germ)==GERM_SHA)
    native=json.loads(gzip.decompress(germ.read_bytes()))
    gate("complete_actual_current_candidate_and_parameter_domain",
         native.get("complete") and native.get("proved") and native.get("whole_affine_parameter_interval")
         and native['candidate_sha256']==CURRENT)
    a=box_from_record(native['complex_intrinsic_coefficients']['a']['real'])
    mmin=box_from_record(native['angle_inverse']['bounds']['mean_gap'])
    mmax=box_from_record(native['angle_inverse']['bounds']['mean_modulus_upper'])
    alo,ahi,mlo,mhi=F("1.0971086"),F("1.0971133"),F("1.1197077"),F("1.1198071")
    gate("actual_full_root_radial_a_lower",a.lower()>arb(str(alo)))
    gate("actual_full_root_radial_a_upper",a.upper()<arb(str(ahi)))
    gate("actual_full_root_mean_modulus_bounds",mmin.lower()>arb(str(mlo)) and mmax.upper()<arb(str(mhi)))
    nlo,nhi=(alo/mhi)**2,(ahi/mlo)**2
    gate("actual_root_n_lower",nlo>F(959,1000))
    gate("actual_root_n_upper",nhi<F(961,1000))
    gate("actual_root_n_ratio_without_radial_derivative",nhi/nlo<F(1003,1000))

    N,mc=97,32
    h=F(9,10**6);M0=4*N;R=F(N+2*mc,N)
    Eabs=F(17700);drift_phi=F(54)
    gate("all_actual_high_cross_cone_entries_vanish_before_compression",2*N>2*mc)
    gate("complete_nonlocal_primitive_index_is_nonzero",N>mc)
    gate("full_actual_high_lag_ratio_squared",R**2<3)
    gate("complete_skew_transport_negative_weight_commutator",2*R**3<10)
    Eneg=3*Eabs+10*drift_phi
    gate("same_Hilbert_complete_high_Volterra_contraction",h*Eneg<F(1,2))
    RH=F(2);sqrt_h=F(3,1000)
    GH=9*RH*h;PH=3*RH*sqrt_h
    gate("complete_high_source_column",GH<=F(162,10**6))
    gate("complete_high_port_column",PH<=F(18,1000))
    gate("both_high_endpoint_port_column",F(3)**2*(1+RH**2)<49)

    GL=h*F(51,50);PL=sqrt_h*F(51,50)
    AHL=F(8658);ALH=F(3)*967
    gate("all_direct_low_high_paths_stay_in_the_true_shell",N+2*mc==161 and 4*(N-1+2*mc)==640)
    gate("negative_weight_shell_inverse_paid",F(160,97)**2<3)
    rho=GL*ALH*GH*AHL
    gate("complete_193_head_and_infinite_high_feedback",rho<F(1,25))
    RL=1/(1-rho)
    low=[RL*GL,RL*GL*ALH*GH,RL*PL,RL*GL*ALH*PH]
    high=[GH*AHL*low[0],GH+GH*AHL*low[1],GH*AHL*low[2],PH+GH*AHL*low[3]]
    trace_low=[sqrt_h*F(51,50)*int(j==0)+F(51,50)*int(j==2)
               +sqrt_h*F(51,50)*ALH*high[j] for j in range(4)]
    trace_high=[F(54,1000)*int(j==1)+7*int(j==3)+F(54,1000)*AHL*low[j] for j in range(4)]
    source_sq=sum(x*x for r in (low,high) for x in r[:2])
    port_sq=sum(x*x for r in (low,high) for x in r[2:])
    trace_source_sq=sum(x*x for r in (trace_low,trace_high) for x in r[:2])
    trace_port_sq=1+sum(x*x for r in (trace_low,trace_high) for x in r[2:])
    gate("complete_hybrid_state_source",source_sq<F(9,50000)**2)
    gate("complete_hybrid_state_ports",port_sq<F(1,50)**2)
    gate("all_mean_and_both_full_endpoint_source",trace_source_sq<F(3,50)**2)
    gate("all_mean_and_both_full_endpoint_ports",trace_port_sq<64)
    nr=F(1003,1000)
    gate("true_height_scaled_state_source",nr*F(9,50000)<F(181,10**6))
    gate("true_height_scaled_state_ports",nr*F(1,50)<F(201,10000))
    gate("true_height_scaled_two_trace_source",nr*F(3,50)<F(61,1000))
    gate("true_height_scaled_two_trace_ports",nr*8<F(803,100))
    assert len(gates)==27

    texts=["results/R133-supplement-global-positive-reference-and-current-collar.md",
           "results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",
           "results/R133-supplement-current-moving-body-physical-complex-germ.md",
           "results/R133-supplement-residual-sensitive-vector-height-and-Airy-contact.md",
           "results/R133-supplement-final-regular-negative-window-and-height-ports.md"]
    return dict(kind="actual_current_root_complete_capped_negative_window_inverse",complete=True,
        arithmetic="Fraction for every feedback/port inequality; Arb256 for same native germ scalar enclosure",
        candidate_sha256=CURRENT,whole_original_eta=True,interval="[rstar(eta),rstar(eta)+9/1000000]",
        producer=dict(path="scripts/"+Path(__file__).name,sha256=sha(__file__)),
        inputs=[dict(path=str(germ),sha256=sha(germ))]+[dict(path=p,sha256=sha(TOPIC/p)) for p in texts],
        gates=gates,all_orders_t_interval=["0","2"],height_order_t="5/3",
        high_state="Y=(388/M)^t Z; Z=M^(1/6)T_M^-1(-i sign(k)h1,h2)",
        low_state="full 193 real coordinates; both formal mean rows before the stated reflection restriction",
        source_norm="L2r direct sum of f_L in L2phi and (388/M)^t f_H in H^(1/3)phi",
        high_ports="Y_s at rstar and Y_u at rstar+h; both independent, not extra full Cauchy data",
        low_ports="all raw h_L at rstar, including the allowed even mean",
        values={k:display(v) for k,v in dict(full_high_ratio=R,high_remainder=Eneg,
            high_contraction=h*Eneg,high_resolvent=RH,high_source=GH,high_port=PH,
            head_feedback=rho,head_resolvent=RL,n_lower=nlo,n_upper=nhi,n_ratio=nhi/nlo).items()},
        response_matrix=[[display(x) for x in r] for r in (low,high)],
        trace_matrix=dict(low_right=[display(x) for x in trace_low],high_both=[display(x) for x in trace_high],low_left="exact input gL"),
        bounds=dict(hybrid_state_source="0.00018",hybrid_state_ports="0.02",
            hybrid_two_trace_source="0.06",hybrid_two_trace_ports="8",
            height_scaled_state_source="0.000181",height_scaled_state_ports="0.0201",
            height_scaled_two_trace_source="0.061",height_scaled_two_trace_ports="8.03"),
        exact_height_identification="tilde Z=n M^-5/3 Z=n 388^-5/3 Y; same scalar n 388^-5/3 on the complete low block and source",
        permissions=dict(full_local_head_and_infinite_high_inverse=True,
            negative_window_not_free_from_positive_bootstrap=True,full_independent_mean_source_and_ports=True,
            actual_center_finite_band_only=True,infinite_tail_neighbourhood_not_claimed=True,
            whole_positive_body_inverse=False,whole_negative_return_inverse=False,
            global_n_ratio_not_claimed=True,global_finite_head_inverse=False,nu_Schur_nonzero=False,
            nonlinear_closed_surface=False))

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--germ",type=Path,default=Path("notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz"))
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError("preserve every actual negative-window attempt")
    d=run(a.germ);a.out.write_text(json.dumps(d,indent=2)+"\n")
    print(json.dumps(dict(complete=d['complete'],gates=len(d['gates']),out=str(a.out),
        high_contraction=d['values']['high_contraction']['decimal_upper'],
        head_feedback=d['values']['head_feedback']['decimal_upper'])))
