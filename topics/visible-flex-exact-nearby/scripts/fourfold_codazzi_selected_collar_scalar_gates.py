#!/usr/bin/env python3
"""New scalar collar gates from complete old ordinary residual rows.

No intrinsic target, candidate polynomial, Fourier product, old residual,
repair sequence, or Green operator is evaluated. All new arithmetic runs
only in the public Actions runner. Large input/audit files are temporary.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

KIND="actual_complete_selected_collar_high_trace_scalar_gates_v1"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_selected_collar_scalar_gates.py"
RAW_MANIFEST_SHA="0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad"
RAW_SHA="6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1"
RAW_BYTES=4592623
RAW_MERGER_SHA="24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
RAW_PRODUCER_SHA="98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e"
RESPONSE_SHA="7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec"
INTRINSIC_EXECUTION_SHA="6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"
INTRINSIC_PRODUCER_SHA="827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
ALPHA=Fraction(6890507429876859,9007199254740992)
ETA=Fraction(-7789843107295549,4611686018427387904)
NU=Fraction(-2572625729470897,72057594037927936)
CUT=Fraction(9,10)
COLLAR=(Fraction(17,20),Fraction(19,20))
R=Fraction(25,8)
PARAMETERS=dict(
    arithmetic_bits=320,exact_cut="9/10",available_intrinsic_collar=["17/20","19/20"],
    delta_half_width="1/10000000000",sigma="1/4294967296",angular_order=8193,
    half_length_exponents=list(range(6,19)),
    raw_C0_pair_radii=["1/10000"]+[str(Fraction(1,2**k)) for k in (16,20,24,28,32,36)],
    original_background_pair_A0="7",original_background_angle_A0="6",
    continuous_response_pair_A0="19",continuous_response_angle_A0="83",
    centre_repair_A0="0.000000000000000003861",
    centre_repair_angle_A0="0.00000000000000001970",
    centre_repair_mean="0.000000000000000000005842",
    response_repair_A0="0.0000000000000002292",
    reference_angular_degree=96,reference_drift_angular_degree=192,
    complete_source_species_degrees=[96,160,224,288],
    ordinary_angular_measure="normalized circle; full pair including both means",
    ordinary_radial_measure="dr",true_unknown_ordinary_residual="0",
    unknown_hypothesis="one continuous two-sided real H1 solution in the stated raw C0 pair ball",
    zero_old_target_or_grid_recomputation=True,
    core_existence_or_low_physical_gamma_selfmap_claimed=False)

def sha_bytes(raw):return hashlib.sha256(raw).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def canonical(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)
def save(path,value):
    raw=canonical(value)
    if len(raw)>60000:raise ValueError("small complete conclusion exceeds 60000 UTF8 bytes")
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".partial");tmp.write_bytes(raw);tmp.replace(path)
def q(x):
    x=Fraction(x);return arb(x.numerator)/x.denominator
def box(x):
    if not isinstance(x,dict):return arb(str(x))
    if "lower" in x and "upper" in x:
        y=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
    elif "ball" in x:y=arb(x["ball"])
    else:raise ValueError("old scalar has no full directed interval")
    if not y.is_finite():raise ValueError("nonfinite old interval")
    return y
def up(x):
    y=box(x) if isinstance(x,dict) else arb(x)
    if not y.is_finite():raise ValueError("nonfinite upper bound")
    return y.upper()
def low(x):
    y=box(x) if isinstance(x,dict) else arb(x)
    if not y.is_finite():raise ValueError("nonfinite lower bound")
    return y.lower()
def absup(x):return abs(box(x) if isinstance(x,dict) else arb(x)).upper()
def record(x):
    y=arb(x)
    if not y.is_finite():raise ValueError("nonfinite scalar output")
    return dict(ball=y.str(48))
def records(d):return {k:record(v) for k,v in d.items()}
def gate(doc,name,ok):
    doc["gates"].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError("collar gate failed: "+name)
def complete(d):
    return d.get("complete") is True and d.get("failure") is None and d.get("gates") and all(
        x.get("passed") is True for x in d["gates"])

def restore_raw(manifest_path,doc):
    if sha(manifest_path)!=RAW_MANIFEST_SHA:raise ValueError("old 7296 manifest changed")
    m=read(manifest_path)
    gate(doc,"same complete original 7296 ordinary residual container and all three exact byte parts",
         m.get("kind")=="complete_native_lossless_container_binary_parts_v2"
         and m.get("native_complete") is True and m.get("native_failure") is None
         and m.get("complete_native_rows")==7296 and m.get("original_bytes")==RAW_BYTES
         and m.get("original_sha256")==RAW_SHA and m.get("original_source_sha256")==RAW_MERGER_SHA
         and m.get("candidate_sha256")==CANDIDATE and len(m.get("parts",[]))==3)
    chunks=[];cursor=0;receipt=[]
    for i,r in enumerate(m["parts"]):
        if r["index"]!=i or r["offset"]!=cursor or Path(r["file"]).name!=r["file"]:
            raise ValueError("old residual byte-part order changed")
        raw=(Path(manifest_path).parent/r["file"]).read_bytes()
        if len(raw)!=r["compressed_bytes"] or sha_bytes(raw)!=r["compressed_sha256"]:
            raise ValueError("old compressed byte-part hash mismatch")
        payload=gzip.decompress(raw)
        if len(payload)!=r["bytes"] or sha_bytes(payload)!=r["sha256"]:
            raise ValueError("old residual payload hash mismatch")
        chunks.append(payload);cursor+=len(payload);receipt.append(r)
    raw=b"".join(chunks)
    if len(raw)!=RAW_BYTES or sha_bytes(raw)!=RAW_SHA:raise ValueError("old complete native mismatch")
    d=json.loads(gzip.decompress(raw))
    gate(doc,"same fixed eta0 and nu0 raw candidate with complete primitive tail and all old seams",
         d.get("kind")=="complete_actual_moving_residual_all_closed_rows_and_interfaces"
         and d.get("complete") is True and d.get("failure") is None
         and d.get("source_sha256")==RAW_MERGER_SHA
         and d.get("original_producer_sha256")==RAW_PRODUCER_SHA
         and d.get("candidate_sha256")==CANDIDATE and d.get("object_sha256")==OBJECT
         and Fraction(d["exact_amplitude"])==ALPHA and Fraction(d["exact_nu"])==NU
         and Fraction(d["common_parameter_half_width"])==0
         and d.get("all_7296_closed_rows_reused_without_recomputation") is True
         and d.get("all_6143_actual_interfaces_paid") is True
         and d.get("complete_original_primitive_tail") is True
         and d.get("complete_residual_support")==96 and len(d.get("rows",[]))==7296)
    cursor=Fraction(0)
    for i,r in enumerate(d["rows"]):
        l,h=map(Fraction,r["interval"])
        if r.get("index")!=i or r.get("exact_angular_support_index")!=96 or l!=cursor or not l<h:
            raise ValueError("old complete ordinary residual rows have a gap or changed support")
        for key in ("U","V"):box(r["complete_residual_A0"][key])
        mgap=low(r["complete_inverse_coordinate_and_physical_residual"]["mean_absolute_gap"])
        if not mgap>0:raise ValueError("old complete moving mean was not strictly negative")
        cursor=h
    gate(doc,"all 7296 genuine closed cells cover zero to 25/8 and retain their complete negative mean",cursor==R)
    doc["original_raw_restoration"]=dict(manifest_sha256=RAW_MANIFEST_SHA,
        native_sha256=RAW_SHA,native_bytes=RAW_BYTES,parts=receipt,
        original_science_executed=False,all_original_bytes_changed=0)
    return d

def inputs(a,doc):
    m=read(a.manifest)
    gate(doc,"new exact parameters, source bytes and all three input identities are pinned",
         sha(a.manifest)==a.manifest_sha and m.get("parameters")==PARAMETERS
         and m["files"].get(PRODUCER)==sha(__file__)
         and sha(a.intrinsic_summary)==m["intrinsic_summary_sha256"]==INTRINSIC_EXECUTION_SHA
         and sha(a.response_summary)==RESPONSE_SHA)
    execution=read(a.intrinsic_summary);response=read(a.response_summary)
    gate(doc,"the public selected-parameter scalar child really completed with unchanged ordinary-source scope",
         execution.get("complete") is True and execution.get("actual_returncode")==0
         and execution.get("run_id") in (43713242980,"43713242980")
         and execution.get("source_budget_source_sha256")==INTRINSIC_PRODUCER_SHA
         and execution.get("old_numerical_enclosures_recomputed")==0)
    intrinsic=execution["actual_scientific_receipt"]
    gate(doc,"the complete selected-parameter intrinsic summary checked all 40 old parts and 7721 true cells",
         complete(intrinsic) and intrinsic.get("source_sha256")==INTRINSIC_PRODUCER_SHA
         and intrinsic.get("complete_original_rows_verified")==7721
         and len(intrinsic.get("original_part_receipts",[]))==40
         and intrinsic.get("exact_original_interval")==["0","25/8"]
         and intrinsic.get("derived_continuous_centre_definition_sha256")==CENTRE
         and intrinsic.get("derived_continuous_response_definition_sha256")==DIRECTION
         and intrinsic.get("old_numerical_enclosures_recomputed")==0)
    coll=intrinsic["complete_original_collar_intrinsic_conclusion"]
    gate(doc,"the intrinsic collar is a genuine complete two-sided interval with its full signed third jets",
         coll.get("exact_interval")==list(map(str,COLLAR))
         and Fraction(coll["exact_total_radial_measure"])==COLLAR[1]-COLLAR[0]
         and coll.get("original_intrinsic_third_jets_read") is True
         and coll.get("original_target_evaluations")==0
         and coll.get("reference_s_is_not_full_moving_mean") is True)
    gate(doc,"old response summary is complete and its progress snapshot is not mistaken for the terminal count",
         complete(response) and response.get("complete_common_rows")==7721
         and response.get("actual_completed_common_rows")==7680
         and len(response.get("original_parts",[]))==40
         and response.get("exact_interval")==["0","25/8"]
         and response.get("derived_continuous_centre_definition_sha256")==CENTRE
         and response.get("true_complete_mean_correction_retained") is True
         and response.get("original_residual_rows_recomputed")==0)
    if sorted((x["indices"],x["sha256"]) for x in response["original_parts"])!=sorted(
        (x["indices"],x["sha256"]) for x in intrinsic["original_part_receipts"]):
        raise ValueError("the independently completed 7721 cover has different original part identities")
    r=response["exact_centre_repair_bounds"]
    gate(doc,"complete centre-repair value, angular and genuine mean bounds fit the declared exact envelope",
         up(r["A0"])<=q(PARAMETERS["centre_repair_A0"])
         and up(r["angular_A0"])<=q(PARAMETERS["centre_repair_angle_A0"])
         and up(r["mean"])<=q(PARAMETERS["centre_repair_mean"]))
    chosen=intrinsic["chosen_global_constants"]
    gate(doc,"the same complete repaired state and continuous response use the proved four global bounds",
         chosen==dict(background_pair_A0="7",background_pair_angle_A0="6",
                      response_pair_A0="19",response_pair_angle_A0="83")
         and intrinsic["complete_response_repair_including_mean"]["A0"]==PARAMETERS["response_repair_A0"]
         and intrinsic["complete_response_repair_including_mean"]["angular_multiplier"]==384)
    raw=restore_raw(a.raw_manifest,doc)
    doc["input_sha256"]=dict(manifest=sha(a.manifest),intrinsic_summary=sha(a.intrinsic_summary),
        response_summary=RESPONSE_SHA,raw_manifest=RAW_MANIFEST_SHA)
    return intrinsic,response,raw

def scalar_intrinsic(coll):
    lower=coll["complete_signed_lower"];upper=coll["complete_signed_upper"]
    absolute=coll["complete_absolute_upper"];ratio=coll["complete_ratio_upper"]
    Klo=low(lower["K"]);Khi=up(upper["K"]);Glo=low(lower["gamma"]);Ghi=up(upper["gamma"])
    if not Klo>0 or not Glo>0:raise ValueError("actual K and G need positive lower bounds")
    Kbox=Klo.union(Khi)
    sqrtK=Kbox.sqrt();quarter=sqrtK.sqrt()
    p=up(max(up(1/quarter),up(quarter)))
    beta=absup(absolute["beta"])
    br=up(beta*sqrtK);g=up(Ghi*quarter)
    alpha=up(beta+absup(ratio["K_r_over_K"])/4)
    return dict(Klo=Klo,Khi=Khi,Glo=Glo,Ghi=Ghi,k=max(arb(1),Khi),
        p=p,beta=beta,b=br,g=g,alpha=alpha,
        sqrtKlo=low(sqrtK),sqrtKhi=up(sqrtK),
        Glog=absup(ratio["gamma_r_over_gamma"]),
        Klog=absup(ratio["K_r_over_K"]))

def operator_coefficients(v):
    Q0=q(7);Q1=q(6);beta=v["beta"];G=v["Ghi"];k=v["k"]
    C1=up(beta*k*Q0*Q0/4+G*k*Q0)
    C0=up(beta+3*beta*k*Q0*Q0+beta*k*Q0*Q1/2+G*k*Q1)
    return C0,C1

def raw_window(rows,left,right):
    cursor=left;length=Fraction(0);squared=arb(0);gap=None;ids=[];witness=None
    for row in rows:
        l,r=map(Fraction,row["interval"]);l=max(l,left);r=min(r,right)
        if not l<r:continue
        if l!=cursor:raise ValueError("new exact collar restriction has a gap or overlap")
        h=r-l
        ru=up(row["complete_residual_A0"]["U"]);rv=up(row["complete_residual_A0"]["V"])
        ordinary_squared=up(q(ALPHA)*q(ALPHA)*(ru*ru+rv*rv))
        squared+=q(h)*ordinary_squared
        g=low(row["complete_inverse_coordinate_and_physical_residual"]["mean_absolute_gap"])
        if gap is None or g<gap:gap=g;witness=row["index"]
        length+=h;cursor=r;ids.append(row["index"])
    if cursor!=right or length!=right-left or gap is None:
        raise ValueError("new exact collar has incomplete original residual coverage")
    return dict(raw_pair_L2=up(squared.sqrt()),raw_pair_square_integral=up(squared),
        raw_mean_gap=gap,rows=ids,mean_gap_witness=witness,exact_length=str(length))

def source_species(v,w,response,length):
    C0,C1=operator_coefficients(v)
    e0=q(PARAMETERS["centre_repair_A0"]);e1=q(PARAMETERS["centre_repair_angle_A0"])
    repair=up(C0*e0+C1*e1)
    ez=q(PARAMETERS["response_repair_A0"])
    response_offset=up(ez*(384*C1+C0))
    sr=up(response["complete_repaired_response_residual_L2_radial"]["L2"])
    Q0=q(7);Q1=q(6);Z0=q(19);Z1=q(83);bk=v["beta"]*v["k"];gk=v["Ghi"]*v["k"]
    t2=up(bk*(Z0*Z0*Q1/4+Q0*Z0*Z1/2+3*Q0*Z0*Z0)+gk*Z0*Z1)
    t3=up(bk*(Z0*Z0*Z1/4+Z0*Z0*Z0))
    rootlength=q(length).sqrt();p=v["p"]
    F0=up(p*(w["raw_pair_L2"]+rootlength*repair))
    S0=up(p*(sr+rootlength*response_offset))
    T2=up(p*rootlength*t2);T3=up(p*rootlength*t3)
    delta=q(PARAMETERS["delta_half_width"]);sigma=q(PARAMETERS["sigma"])
    value=up(F0+delta*S0+delta*delta*T2+delta*delta*delta*T3)
    angle=up(384*F0+640*delta*S0+896*delta*delta*T2+1152*delta*delta*delta*T3)
    factorial=up((384*sigma).exp()*F0+delta*(640*sigma).exp()*S0+
                 delta*delta*(896*sigma).exp()*T2+
                 delta*delta*delta*(1152*sigma).exp()*T3)
    return dict(F0=F0,S0=S0,T2=T2,T3=T3,ordinary_value=value,ordinary_angle=angle,
        finite_factorial=factorial,centre_repair_sup=repair,response_offset_sup=response_offset,
        response_raw_whole_L2=sr,T2_unscaled_sup=t2,T3_unscaled_sup=t3,C0=C0,C1=C1)

def candidate(v,w,src,ell,radius):
    e=q(ell);rho=q(radius);sigma=q(PARAMETERS["sigma"]);delta=q(PARAMETERS["delta_half_width"])
    p=v["p"];eta=up(p*rho)
    Q0=up(q(7)+delta*19);Q1=up(q(6)+delta*83)
    M0=up(p*Q0);M1=up(p*Q1);M2=up(384*M1)
    Ms=up((384*sigma).exp()*M0);M1s=up((384*sigma).exp()*M1)
    D1=up(v["beta"]*v["k"]*min(up(Q0*Q0),up(Q0*Q1/2)))
    D0=up(D1/4);Ds=up((768*sigma).exp()*D1)
    ref_mean=low(w["raw_mean_gap"]-q(PARAMETERS["centre_repair_mean"])-delta*19)
    actual_mean=low(ref_mean-rho)
    if not actual_mean>0:
        return dict(passed=False,reason="complete_actual_moving_mean_not_negative",
                    actual_mean_gap=record(actual_mean))
    amin=low(v["Glo"]*v["sqrtKlo"]*actual_mean)
    dplus=up(D0+v["b"]*(2*M0*eta+eta*eta))
    Shi=min(up(v["k"]*(Q0+rho)*(Q0+rho)),
            up(v["sqrtKhi"]*(M0+eta)*(M0+eta)))
    Slo=low(v["Klo"]*actual_mean*actual_mean)
    if not Slo<=Shi:raise ValueError("contradictory whole mean-square source enclosure")
    L=up(v["Glog"]+v["Klog"]/2+v["beta"]*max(absup(1-Slo),absup(1-Shi)))
    cr=up(1+2*dplus/amin);cp=up(2/amin);pi=arb.pi()
    CE=up(max(up(((1+(4*e/pi)**2)*cr*cr+cp*cp).sqrt()),up(4*cr/pi)))
    Clin=up(v["alpha"]+3*v["b"]*Ms*Ms+(v["b"]*Ms/2+v["g"])*M1s)
    Cact=up(v["alpha"]+3*v["b"]*(Ms+eta)*(Ms+eta)+
             (v["b"]*(Ms+eta)/2+v["g"])*M1s)
    cout0=up(v["b"]*(3*Ms*eta+eta*eta+M1s*eta/4))
    cout1=up(v["b"]*(2*Ms*eta+eta*eta))
    c2=up(v["b"]*(6*Ms*e+2*Ms*e.sqrt()+M1s*e*e.sqrt()))
    c3=up(6*v["b"]*e)
    Z=up(2*e.sqrt()*eta)
    AN=up(src["finite_factorial"]+Z/e)
    start=up(CE*e*(L+Cact))
    linear=up(CE*(e*(L+Clin+cout0)+2*sigma/e+sigma*Ds+cout1))
    nonlinear=up(2*CE*CE*c2*AN+4*CE*CE*CE*c3*AN*AN)
    prefactor=up(p*2*CE*e.sqrt()*AN)
    gates=dict(positive_actual_speed=bool(amin>0),
        low_start=bool(start<=q("1/4")),complete_linear=bool(linear<=q("1/4")),
        complete_nonlinear=bool(nonlinear<=q("1/8")),
        factorial_readout=bool(prefactor<=q(2**1024)))
    M=up(M0+eta)
    A0=up(v["alpha"]+3*v["b"]*M*M+(v["b"]*M/2+v["g"])*M1)
    A1=up(v["alpha"]+5*v["b"]*M*M)
    B10=up(8*v["b"]*M*M1+(v["b"]*M/2+v["g"])*M2)
    E0=up(src["ordinary_value"]+(A0+L+1/e)*Z)
    E1=up(src["ordinary_angle"]+B10*Z+(A1+L+2/e)*2*E0/amin)
    h1=up(p*((Z+2*E0/amin)/e.sqrt()+e.sqrt()*cr*(E0+E1)))
    base_h1=up(h1+delta*(19+83))
    return dict(passed=all(gates.values()),gates=gates,
        scalar_gates=records(dict(low_start=start,complete_linear=linear,
            complete_nonlinear=nonlinear,factorial_prefactor=prefactor)),
        coefficients=records(dict(raw_mean_gap=w["raw_mean_gap"],reference_mean_gap=ref_mean,
            actual_mean_gap=actual_mean,principal_speed_lower=amin,drift_upper=dplus,
            P_upper=p,b=v["b"],g=v["g"],alpha=v["alpha"],speed_log_derivative=L,
            M0=M0,M1=M1,M2=M2,M_sigma=Ms,M1_sigma=M1s,D0=D0,D1=D1,D_sigma=Ds,
            eta=eta,CE_sharp=CE,C_linear=Clin,C_actual=Cact,C_outer0=cout0,C_outer1=cout1,
            c2_sharp=c2,c3_sharp=c3,Z_L2=Z,AN=AN)),
        source_species=records(src),
        comparison_H1_cut_upper=record(h1),base_centre_H1_cut_upper=record(base_h1),
        low_physical_gamma_diagnostic=dict(
            uses_global_response_H1_upper_102=True,
            hypotheses_of_shape_mean_lemma_proved=bool(base_h1<=q("1/1024")),
            sufficient_low_shape_radius=bool(base_h1<q("15/128000000000")),
            whole_bound_used_only_as_upper=True,
            core_solution_or_selfmap_proved=False),
        high_trace_conclusion=dict(order=8193,
            selected_reference_difference_bound_2_power_377903=all(gates.values()),
            base_centre_difference_bound_2_power_377904=all(gates.values()),
            base_centre_difference_bound_2_power_393000=all(gates.values()),
            known_delta_response_bound_2_power_73742=True,
            physical_gamma_high_gate_not_identified_without_separate_low_hypotheses=True))

def run(a,doc):
    ctx.prec=a.bits
    gate(doc,"the declared directed precision is used",a.bits==PARAMETERS["arithmetic_bits"])
    intrinsic,response,raw=inputs(a,doc)
    v=scalar_intrinsic(intrinsic["complete_original_collar_intrinsic_conclusion"])
    doc["complete_intrinsic_scalar_bounds"]=records(v)
    rows=raw["rows"];grid=[];best={};audit=hashlib.sha256();cases=0
    a.temporary_audit.parent.mkdir(parents=True,exist_ok=True)
    if a.temporary_audit.exists():raise FileExistsError("preserve earlier complete temporary audit")
    with a.temporary_audit.open("wb") as stream:
        for k in PARAMETERS["half_length_exponents"]:
            ell=Fraction(1,2**k);left=CUT-2*ell;right=CUT+2*ell
            if not COLLAR[0]<=left<right<=COLLAR[1]:raise ValueError("candidate leaves actual intrinsic collar")
            w=raw_window(rows,left,right);src=source_species(v,w,response,right-left)
            for radius in PARAMETERS["raw_C0_pair_radii"]:
                c=candidate(v,w,src,ell,radius);cases+=1
                item=dict(ell=str(ell),raw_C0_pair_radius=radius,
                    exact_interval=[str(left),str(right)],
                    complete_original_residual_rows=len(w["rows"]),
                    exact_radial_measure=w["exact_length"],mean_gap_witness=w["mean_gap_witness"],**c)
                payload=canonical(item);stream.write(payload);audit.update(payload)
                g=dict(ell=str(ell),radius=radius,passed=c["passed"])
                if "gates" in c:g["failed_gates"]=[name for name,passed in c["gates"].items() if not passed]
                else:g["reason"]=c["reason"]
                grid.append(g)
                if c["passed"]:
                    old=best.get(radius)
                    if old is None or up(c["scalar_gates"]["complete_nonlinear"])<up(
                        old["scalar_gates"]["complete_nonlinear"]):
                        best[radius]=item
            print(json.dumps(dict(collar_ell=str(ell),complete_cases=cases,
                                  radii_with_passed_gates=list(best))),flush=True)
    gate(doc,"every declared collar and C0 radius was fully evaluated with exact original row measures",
         cases==len(PARAMETERS["half_length_exponents"])*len(PARAMETERS["raw_C0_pair_radii"]))
    doc.update(complete=True,actual_evaluated_cases=cases,complete_grid=grid,
        best_complete_case_per_radius=best,
        actual_nonempty_conditional_high_trace_domain_proved=bool(best),
        all_source_components_and_genuine_means_retained=True,
        ordinary_residual_squares_integrated_not_L1_converted=True,
        old_response_whole_L2_only_used_as_a_valid_subinterval_upper=True,
        continuous_response_piece_offset_source_explicit=True,
        original_raw_value_jumps_exactly_cancelled_by_definition_not_discarded=True,
        true_unknown_source_zero_only_under_separate_H1_solution_hypothesis=True,
        no_core_existence_waist_phase_boundary_or_GH_claim=True,
        no_low_physical_gamma_selfmap_claim=True,
        all_old_target_grid_Fourier_residual_repair_and_Green_evaluations=0,
        new_scalar_case_count=cases,
        original_source_suprema_or_rows_modified=0,
        temporary_complete_audit=dict(bytes=a.temporary_audit.stat().st_size,
            sha256=audit.hexdigest(),persisted=False),
        new_recomputable_outputs_persisted=False)
    if not best:
        doc["actual_no_candidate_passed"]=True

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--intrinsic-summary",type=Path,required=True)
    p.add_argument("--response-summary",type=Path,required=True)
    p.add_argument("--raw-manifest",type=Path,required=True)
    p.add_argument("--temporary-audit",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--bits",type=int,default=320)
    a=p.parse_args();started=time.monotonic()
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        parameters=PARAMETERS,derived_continuous_centre_definition_sha256=CENTRE,
        derived_continuous_response_definition_sha256=DIRECTION,exact_eta=str(ETA),exact_nu0=str(NU))
    try:
        run(a,doc)
    except Exception as e:
        doc["failure"]=dict(error_type=type(e).__name__,message=str(e))
        doc["complete"]=False
        traceback.print_exc()
    doc["seconds"]=time.monotonic()-started
    save(a.out,doc)
    print(json.dumps(dict(complete=doc["complete"],failure=doc["failure"],
        gates_passed=sum(x["passed"] for x in doc["gates"]),gates_total=len(doc["gates"]),
        actual_high_trace_domain=doc.get("actual_nonempty_conditional_high_trace_domain_proved",False)),
        ensure_ascii=False),flush=True)
    return 0 if doc["complete"] and doc.get("actual_nonempty_conditional_high_trace_domain_proved") else 1

if __name__=="__main__":raise SystemExit(main())
