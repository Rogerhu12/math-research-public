#!/usr/bin/env python3
"""Instantiate the complete real delta96 positive root collar from original natives."""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
REPAIR="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PINS={"root_germ":"397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864",
      "root_budget":"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"}
GERM_SOURCE="a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"
ROOT_SOURCE="4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)
def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator
def upper(value):return arb(value["upper"]).upper()
def lower(value):return arb(value["lower"]).lower()
def record(value):
    value=arb(value)
    if not value.is_finite():raise ValueError("nonfinite full-family collar bound")
    return dict(ball=value.str(60),lower=value.lower().str(60),upper=value.upper().str(60))
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,indent=2,allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    temporary=path.with_name(path.name+".partial");temporary.write_bytes(raw);temporary.replace(path)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in PINS:p.add_argument("--"+name.replace("_","-"),type=Path,required=True)
    p.add_argument("--out",type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError("preserve every actual delta96 collar result")
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the new mathematics runs only in this public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0"):
        raise RuntimeError("the directed arithmetic runtime changed")
    ctx.prec=256;started=time.monotonic()
    doc=dict(kind="actual_full_real_delta96_global_reference_positive_root_collar",
        complete=False,proved=False,source_sha256=sha(__file__),runtime=runtime,
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE,background_definition_sha256=REPAIR,
        explicit_direction_definition_sha256=DIRECTION,actual_intrinsic_parameter="eta_0",
        exact_real_direction_radius="1/100000000",background_degree=96,
        full_operator_band=192,first_high_index=97,complete_reflection_head_size=193,
        all_unknown_high_modes_and_true_independent_mean_retained=True,
        ordinary_source_has_no_radial_derivative=True,
        reference_is_uniform_in_any_allowed_positive_extension_and_terminal_scalar=True,
        actual_nonzero_delta_body_speed_certified_here=False,
        actual_nonzero_delta_outer_scalar_or_regular_graph_certified_here=False,
        complete_negative_return_or_true_PDE_response_or_nonlinear_solution_claimed=False,
        original_germ_response_or_M32_collar_recomputed=False,inputs={},gates=[],failure=None)
    def check(name,ok):
        ok=bool(ok);doc["gates"].append(dict(name=name,passed=ok))
        if not ok:raise ValueError("actual full delta96 collar gate failed: "+name)
    try:
        for key,pin in PINS.items():
            path=getattr(a,key)
            if sha(path)!=pin:raise ValueError("an original complete native changed: "+key)
            doc["inputs"][key]=dict(path=str(path),sha256=pin,bytes=path.stat().st_size)
        germ,rb=read(a.root_germ),read(a.root_budget)
        check("the actual completed original germ and full193 direction identities agree",
            germ["complete"] and germ["proved"] and germ["source_sha256"]==GERM_SOURCE
            and germ["candidate_sha256"]==CANDIDATE and germ["all_finite_candidate_modes_retained"]
            and rb["complete"] and rb["proved"] and rb["source_sha256"]==ROOT_SOURCE
            and str(rb["public_run_id"])=="43594466882"
            and rb["candidate_sha256"]==CANDIDATE and rb["background_definition_sha256"]==REPAIR
            and rb["explicit_direction_definition_sha256"]==DIRECTION
            and rb["actual_independent_even_mean_preserved"]
            and len(rb["response_repaired_complete_coefficient_upper"])==193
            and all(g["passed"] for g in rb["gates"]))
        q=Fraction
        h,sh,delta,N,Mc=q(9,10**6),q(3,1000),q(1,10**8),q(97),q(96)
        roots=list(map(q,germ["root_interval"]));cell=list(map(q,germ["exact_candidate_piece_interval"]))
        rectangle=list(map(q,germ["complex_radial_rectangle"]["real_interval"]))
        cut=q(1192029371497,5000000000000)
        expected=[q(1191984371497,5000000000000),q(2383968743003,10000000000000)]
        check("the full real family and true complete positive collar stay in one original root piece",
            roots==expected and roots==list(map(q,rb["exact_root_interval"]))
            and q(rb["exact_complex_parameter_radius"])==delta
            and q(rb["exact_outer_radial_radius"])==q(1,100000)
            and q(germ["complex_radial_radius"])==q(1,100000)
            and q(rb["exact_moving_Wiener_strip"])==q(1,1024)
            and cell[0]<rectangle[0]<roots[0]<roots[1]+h<rectangle[1]<cell[1]
            and germ["actual_candidate_piece"]==rb["exact_candidate_and_response_piece"]==2549
            and roots[1]<cut<=roots[0]+h and sh**2==h
            and germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and germ["domain_contains_disks_about_every_true_parameter_root"])
        U=[upper(v) for v in rb["full_family_U_angular_norms"]]
        V=[upper(v) for v in rb["full_family_V_angular_norms"]]
        b=upper(rb["beta_abs_upper"]);gamma=upper(rb["gamma_abs_upper"])
        gl=lower(rb["gamma_abs_lower"]);mgap=lower(rb["full_complex_mean_abs_lower"])
        mmax=upper(rb["full_complex_mean_abs_upper"])
        alo=(gl*mgap).lower();ahi=(gamma*mmax).upper()
        intrinsic=germ["complex_intrinsic_coefficients"]
        krlo,krhi=q("59.74380437"),q("60.465470")
        kmax=q(61,100000);K=exact(kmax)
        check("all full-family angular norms and true optical speed are uniformly bounded",
            len(U)==len(V)==5 and all(x.is_finite() for x in U+V)
            and alo>exact(q(1,2)) and ahi<exact(q(63,50))
            and b<exact(q(211,1000)) and gl>0 and mgap>0)
        check("the same intrinsic positive curvature and optical slope satisfy the root hypotheses",
            lower(intrinsic["K1"]["real"])>exact(krlo)
            and upper(intrinsic["K1"]["modulus_upper"])<exact(krhi)
            and krhi*h<kmax and kmax<q(1,1600)
            and krlo/q(63,50)>29 and krhi/q(1,2)<122)
        A=(b*(1+3*U[0]**2+K*V[0]**2)).upper()
        E=(b*(1+U[0]**2+3*K*V[0]**2)).upper()
        B=(2*b*U[0]*V[0]).upper()
        d1=(b*(U[0]**2+K*V[0]**2)).upper();d0=(d1/4).upper()
        local=(A+E+(1+K)*B).upper()
        primitive=(b*(U[1]+V[1])*(U[0]+K*V[0])/2).upper()
        mean=(gamma*(U[1]+K*V[1])).upper()
        FN=((U[1]+4*V[1])*(U[0]+V[0])).upper()
        check("the complete local reaction and full drift meet the declared family bounds",
            A<exact(q(1,2)) and E<exact(q(3,10)) and B<exact(q(1,2))
            and d1<exact(q(9,100)) and d0<exact(q(11,500)))
        check("both complete primitive rows and the genuine mean rank remain paid",
            local<2 and primitive<1 and mean<3 and FN<34)
        trial=q(20)+q(122,6400)
        check("any allowed positive extension and terminal scalar has the same two-row root reference bound",
            (q(66)-trial)**2*40*q(8,3)*(h/2)>1
            and q(66)**2+3<67**2 and 67<81 and 4*N>64)
        check("the true band192 frequency ratio and smallest primitive index are paid",
            2*N>2*Mc and (N+2*Mc)/N<3 and N-Mc==1
            and 3**5<7**3 and (q(5,3)**3)*3**5<12**3
            and 3**2<3**3)
        dmax,reaction,dyad,bmax=q(9,100),q(33,10),q(34),q(211,1000)
        EH=q(25,2)*dmax+28*reaction+6*bmax*dyad
        fresh=(exact(q(25,2))*d1+28*(A+E+5*B)+6*b*FN).upper()
        check("the entire unbounded high kernel closes with the new full-family constants",
            EH<144 and fresh<exact(EH) and h*EH<q(1,750))
        ih=q(750,749)
        GH,PH,TH,QH=q(41,500000),q(451,50000),q(677,25000),q(17,4)
        check("both high ordinary-source and independent incoming-port state contracts close",
            9*ih*h<GH and 3*ih*sh<PH)
        check("the full incoming and outgoing high raw traces close",
            9*ih*sh<TH and 9*(1+ih**2)<QH**2)
        CH0,CL,CH=q(23,2),q(58,5),q(253,2)
        lowgen=384*q(63,50)+384*q(11,500)+2+1+3
        check("the complete193 head and every output through288 satisfy both crossing contracts",
            384*q(11,500)+2+1<CH0
            and 384*q(11,500)+q(9,100)+2+1<CL
            and 96+2*96==288 and 1+1152**2<11**6
            and CH==11*CH0 and lowgen<500)
        EL=q(201,200)
        check("the actual all-radial low Cauchy propagator retains its mean and all columns",
            500*h<1 and 1/(1-500*h)<EL)
        GL,PL=h*EL,sh*EL
        loop=GL*CL*GH*CH;il=q(500000,499999)
        check("the new complete head-high return is below1over500000",loop<q(1,500000))
        ell=[il*GL,il*GL*CL*GH,il*PL,il*GL*CL*PH]
        high=[GH*CH*ell[0],GH*(1+CH*ell[1]),GH*CH*ell[2],PH+GH*CH*ell[3]]
        state_source=sum((row[j]**2 for row in (ell,high) for j in (0,1)),q(0))
        state_ports=sum((row[j]**2 for row in (ell,high) for j in (2,3)),q(0))
        check("the complete ordinary source-to-state bound is below1over12000",state_source<q(1,12000)**2)
        check("the complete full port-to-state bound is below1over100",state_ports<q(1,100)**2)
        lowtrace=[sh*EL*(1+CL*high[0]),sh*EL*CL*high[1],
                  EL+sh*EL*CL*high[2],sh*EL*CL*high[3]]
        hightrace=[TH*CH*ell[0],TH*(1+CH*ell[1]),TH*CH*ell[2],QH+TH*CH*ell[3]]
        left=[q(0),q(0),q(1),q(0)]
        trace_source=sum((row[j]**2 for row in (left,lowtrace,hightrace) for j in (0,1)),q(0))
        trace_ports=sum((row[j]**2 for row in (left,lowtrace,hightrace) for j in (2,3)),q(0))
        check("both endpoint complete ordinary-source trace bounds are below1over36",trace_source<q(1,36)**2)
        check("both endpoint complete input-port trace bounds are below9over2",trace_ports<q(9,2)**2)
        check("orders0through4 keep the same full high inverse with band192 commutators",
            h*(144+4*dmax)<q(1,750))
        triangle={str(j):[str(768**(j-l)*(math.comb(j,l)*(144+dmax/2)
                         +(math.comb(j,l-1)*dmax if l>=1 else 0)))
                         for l in range(j)] for j in range(1,5)}
        doc.update(
            exact_root_interval=list(map(str,roots)),exact_piece_interval=list(map(str,cell)),
            exact_moving_Wiener_strip="1/1024",exact_root_to_body_cut=str(cut),
            exact_maximum_collar_length=str(h),full_family_U_angular_norms=[record(x) for x in U],
            full_family_V_angular_norms=[record(x) for x in V],
            fresh_coefficient_bounds={k:record(v) for k,v in dict(
                optical_speed_lower=alo,optical_speed_upper=ahi,beta=b,gamma=gamma,
                local_A=A,local_E=E,local_B_and_C=B,d=d0,dphi=d1,raw_local=local,
                full_primitive=primitive,independent_mean_rank=mean,global_frame_dyad=FN).items()},
            fresh_full_high_remainder_upper=record(fresh),
            uniform_positive_extension_reference=dict(domain="[the true intrinsic root,25/8]",
                speed_on_actual_root="full-family -gamma*mean(v)",
                allowed_outside_root="any positive bounded frequency-independent extension bounded away from zero",
                forward_root_value="M^-1/3",terminal_scalar_range=["1/8","1/5"],
                actual_outer_terminal_value_not_certified_here=True,
                root_backward_value_upper="66 M^-1/3",both_root_Airy_rows_factor="9"),
            exact_rational_contract=dict(high_E_upper=str(EH),high_contraction_upper=str(h*EH),
                high_resolvent=str(ih),high_source_state=str(GH),high_port_state=str(PH),
                high_source_trace=str(TH),high_port_trace=str(QH),low_generator_upper=str(lowgen),
                low_propagator_upper=str(EL),low_Green_upper=str(GL),low_Poisson_upper=str(PL),
                low_to_high_L2=str(CH0),high_to_low_L2=str(CL),low_to_high_Hthird=str(CH),
                complete_head_feedback=str(loop),full_head_resolvent=str(il),
                input_order=["source_low_L2","source_high_Hthird","low_root_Cauchy_ports","high_two_incoming_ports"],
                state_response_matrix=[list(map(str,ell)),list(map(str,high))],
                trace_response_matrix=[list(map(str,row)) for row in (left,lowtrace,hightrace)],
                state_source_squared_Frobenius=str(state_source),state_port_squared_Frobenius=str(state_ports),
                trace_source_squared_Frobenius=str(trace_source),trace_port_squared_Frobenius=str(trace_ports),
                ordinary_source_to_full_state="1/12000",incoming_ports_to_full_state="1/100",
                ordinary_source_to_both_full_traces="1/36",incoming_ports_to_both_full_traces="9/2"),
            angular_bootstrap=dict(orders=[0,1,2,3,4],same_high_resolvent=str(ih),
                full_absolute_kernel_bound="144",physical_lag_bound=768,
                exact_triangular_coefficients=triangle,
                full_head_forcing="(253/2)*1153^j times the complete base head L2 norm",
                ordinary_source="H^(j+1/3), no radial derivative",
                same_width_analytic_or_negative_Sobolev_inverse_claimed=False),
            complete=True,proved=True)
    except Exception as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
        doc["seconds"]=time.monotonic()-started;save(a.out,doc);raise
    doc["seconds"]=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc["gates"]),
        fresh_full_high_remainder_upper=doc["fresh_full_high_remainder_upper"],
        exact_rational_contract=doc["exact_rational_contract"],seconds=doc["seconds"])),flush=True)

if __name__=="__main__":main()
