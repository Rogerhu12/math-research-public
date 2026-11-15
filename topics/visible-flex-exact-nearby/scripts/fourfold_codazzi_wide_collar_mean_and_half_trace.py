#!/usr/bin/env python3
"""Wide ordinary collar half-trace coefficients; no old H or source reevaluation."""
from __future__ import annotations
import argparse,gzip,hashlib,json,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

KIND="actual_wide_collar_mean_and_projected_half_trace_v1"
MANIFEST_KIND="wide_collar_mean_and_half_trace_public_inputs_v1"
PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_wide_collar_mean_and_half_trace.py"
RAW_MANIFEST_SHA="0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad"
RAW_SHA="6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1"
RAW_BYTES=4592623
RAW_MERGER_SHA="24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
RAW_PRODUCER_SHA="98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e"
COLLAR_SHA="618bd148e7d75e82c49af5f434235b3792747652a3ff9fb98adc03f560ac2080"
COLLAR_SOURCE="e39646a5430b062fc48c469439f5bba00a8a1a806777b43fd82d1aebea46ecee"
NR_EXECUTION="401d41d80b394970736136f4f39e3a5dcb2ecc1728378dfc43ae2b11da6d184e"
NR_SOURCE="129f7f7955bb8d11385b9804353f0e389761ba38cc74467436a9600283376934"
MC_EXECUTION="c5424be21b98cf5e195ea7246ccba46cf746d1f16d9c118042fda1fad433e408"
MC_SOURCE="7547ece2825854a18e59c27294b12e8dbdcb13671c8fb0d8fba6af218d86f7f2"
D_EXECUTION="6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"
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
NARROW_RADII=["1/1048576","1/16777216","1/268435456","1/4294967296","1/68719476736"]
PARAMETERS=dict(
    arithmetic_bits=320,exact_cut="9/10",exact_wide_interval=["17/20","19/20"],
    delta_half_width="1/10000000000",ordinary_wide_radii=["1/10000"]+NARROW_RADII,
    narrow_MA_radii=NARROW_RADII,narrow_MA_interval=["589819/655360","589829/655360"],
    single_cutoff="continuous triangular hat, value one at the same cut, zero at both wide endpoints",
    cutoff_derivative_upper="20",finite_cut_degree=96,far_cut_degree=288,
    finite_physical_frequency=384,middle_physical_frequency=1152,
    centre_repair_mean="0.000000000000000000005842",
    continuous_response_pair_A0="19",angular_order_at_cut_from_MA_only=8193,
    ordinary_angle_measure="normalized original moving circle; full even mean has weight one",
    ordinary_radial_measure="dr",true_unknown_ordinary_residual="0",
    wide_unknown_hypothesis="one real continuous two-sided H1 state in its separate wide raw C0 pair ball",
    narrow_high_domain_is_independent=True,old_91_or_high_factorial_cases_reevaluated=0,
    old_target_or_source_recomputation=0,actual_unknown_body_or_cut_bound_supplied=False)

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
        mgap=low(r["complete_inverse_coordinate_and_physical_residual"]["mean_absolute_gap"])
        if not mgap>0:raise ValueError("old complete moving mean was not strictly negative")
        cursor=h
    gate(doc,"all 7296 genuine closed cells cover zero to 25/8 and retain their complete negative mean",cursor==R)
    doc["original_raw_restoration"]=dict(manifest_sha256=RAW_MANIFEST_SHA,
        native_sha256=RAW_SHA,native_bytes=RAW_BYTES,parts=receipt,
        original_science_executed=False,all_original_bytes_changed=0)
    return d

def nn(x):
    y=up(x)
    if y<0:raise ValueError("a positive saved bound became negative")
    return y

def intrinsic_bounds(old):
    v={k:nn(x) for k,x in old["complete_intrinsic_scalar_bounds"].items()}
    for name in ("Glo","Klo","sqrtKlo"):
        v[name]=low(old["complete_intrinsic_scalar_bounds"][name])
        if not v[name]>0:raise ValueError("a saved intrinsic lower bound is not positive")
    return v

def inputs(a,doc):
    gate(doc,"the new directed precision and positive scalar parameters are fixed",a.bits==320)
    m=read(a.manifest)
    gate(doc,"the new manifest and source are immutable",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("repository")==PUBLIC and m.get("parameters")==PARAMETERS
         and m["files"].get(PRODUCER)==sha(__file__))
    old=read(a.collar_conclusion)
    best=old.get("best_complete_case_per_radius",{})
    gate(doc,"the original complete collar receipt is used only for its retained coefficients and identities",
         sha(a.collar_conclusion)==COLLAR_SHA and complete(old)
         and old.get("source_sha256")==COLLAR_SOURCE and old.get("actual_evaluated_cases")==91
         and len(old.get("complete_grid",[]))==91
         and old["input_sha256"]["intrinsic_summary"]==D_EXECUTION
         and set(best)==set(NARROW_RADII)
         and all(c.get("exact_interval")==PARAMETERS["narrow_MA_interval"]
             and c.get("ell")=="1/262144" and c.get("raw_C0_pair_radius")==rho
             for rho,c in best.items()))
    ex=read(a.nonmean_execution);nr=ex.get("actual_scientific_receipt",{})
    gate(doc,"the successful complete NR restriction is copied without its old row computation",
         sha(a.nonmean_execution)==NR_EXECUTION and str(ex.get("run_id"))=="43720373326"
         and ex.get("actual_returncode")==0 and ex.get("complete") is True
         and complete(nr) and nr.get("source_sha256")==NR_SOURCE and nr.get("actual_returncode")==0
         and len(nr.get("gates",[]))==13 and nr.get("cases_evaluated")==5
         and nr.get("complete_source_and_trace_coefficient_tables_proved") is True
         and nr.get("old_numerical_enclosures_recomputed")==0
         and nr.get("actual_low_curvature_entry_proved") is False)
    exm=read(a.corrected_mean_execution);mc=exm.get("actual_scientific_receipt",{})
    gate(doc,"the successful complete raw mean correction and exactly five narrow high domains are copied",
         sha(a.corrected_mean_execution)==MC_EXECUTION and str(exm.get("run_id"))=="43717700427"
         and exm.get("actual_returncode")==0 and exm.get("complete") is True
         and complete(mc) and mc.get("source_sha256")==MC_SOURCE
         and len(mc.get("gates",[]))==12 and mc.get("corrected_cases_evaluated")==5
         and mc.get("corrected_cases_passed")==5
         and mc.get("independent_raw_mean_and_continuity_repair_both_paid") is True
         and mc.get("other_old_ten_passing_cases_reauthorized") is False)
    gate(doc,"all three saved results retain the same repaired centre direction and full raw mean",
         all(x.get("derived_continuous_centre_definition_sha256")==CENTRE
             and x.get("derived_continuous_response_definition_sha256")==DIRECTION for x in (old,nr,mc))
         and nr["corrected_raw_mean_windows_copied_without_recomputation"]==mc["complete_raw_mean_windows"]
         and nr["corrected_raw_mean_execution_sha256"]==MC_EXECUTION
         and set(mc["corrected_retained_cases"])==set(NARROW_RADII)
         and all(mc["corrected_retained_cases"][rho].get("passed") is True
             and mc["corrected_retained_cases"][rho]["original_complete_case_sha256"]==
                    hashlib.sha256(canonical(best[rho])).hexdigest()
             and mc["corrected_retained_cases"][rho]["high_trace_conclusion"]==
                    nr["complete_retained_three_band_cases"][rho]["corrected_high_window_authorization"]
             and mc["corrected_retained_cases"][rho]["high_trace_conclusion"].get(
                    "selected_reference_difference_bound_2_power_377903") is True for rho in NARROW_RADII))
    nw=nr["complete_new_nonmean_windows"]["whole_available_positive_collar"]
    gate(doc,"the old wide nonmean source is on the exact same complete interval and ordinary units",
         nw["exact_interval"]==PARAMETERS["exact_wide_interval"]
         and nw["exact_radial_measure"]=="1/10" and nw["original_closed_rows_consumed"]==140
         and nw.get("alpha_applied") is False and nw.get("true_radial_intersections") is True
         and nw.get("complete_cell_L2_not_rescaled_by_fraction") is True
         and nw.get("original_nonmean_degree_upper")==160
         and all(best[rho]["source_species"]["T2_unscaled_sup"]==
                 best[NARROW_RADII[0]]["source_species"]["T2_unscaled_sup"]
             and best[rho]["source_species"]["T3_unscaled_sup"]==
                 best[NARROW_RADII[0]]["source_species"]["T3_unscaled_sup"]
             for rho in NARROW_RADII))
    raw=restore_raw(a.raw_manifest,doc)
    doc["input_sha256"]=dict(manifest=sha(a.manifest),old_collar_conclusion=COLLAR_SHA,
         saved_nonmean_execution=NR_EXECUTION,corrected_mean_execution=MC_EXECUTION,
         original_raw_manifest=RAW_MANIFEST_SHA)
    return old,nr,mc,raw

def mean_window(rows):
    left,right=COLLAR;cursor=left;length=Fraction(0);indices=[];gap=None;witness=None;witness_ball=None
    for row in rows:
        l,r=map(Fraction,row["interval"]);l=max(l,left);r=min(r,right)
        if not l<r:continue
        if l!=cursor:raise ValueError("the wide old-row restriction has a gap or overlap")
        val=row["complete_inverse_coordinate_and_physical_residual"]["mean_absolute_gap"]
        g=low(val)
        if not g>0:raise ValueError("the original full moving mean was not strictly negative")
        if gap is None or g<gap:gap=g;witness=row["index"];witness_ball=val
        indices.append(row["index"]);length+=r-l;cursor=r
    if cursor!=right or length!=right-left or gap is None:
        raise ValueError("the wide moving mean cover is incomplete")
    return dict(exact_interval=list(map(str,COLLAR)),exact_radial_measure=str(length),
        original_closed_rows_consumed=len(indices),original_indices=indices,
        original_indices_sha256=sha_bytes(canonical(indices)),minimum_row_index=witness,
        original_minimum_row_full_interval=witness_ball,raw_full_moving_mean_gap_lower=record(gap),
        full_moving_mean_is_negative=True,alpha_applied_again=False,
        intrinsic_reference_s_not_substituted=True,old_row_values_or_residuals_recomputed=False)

def sources(old,nr):
    v=intrinsic_bounds(old)
    rho=NARROW_RADII[0];oc=old["best_complete_case_per_radius"][rho]
    prev=nr["complete_retained_three_band_cases"][rho]["source_restriction"]
    win=nr["complete_new_nonmean_windows"]["whole_available_positive_collar"]
    length=q(COLLAR[1]-COLLAR[0]);p=v["p"]
    repair=nn(prev["old_complete_repair_sup"]);offset=nn(prev["canonical_continuity_offset_sup"])
    fee=up(p*length.sqrt()*(repair+offset))
    S=up(nn(win["P_scaled_raw_nonmean_L2"])+fee)
    Sphi=up(min(nn(win["P_scaled_raw_nonmean_angular_L2_upper"])+640*fee,640*S))
    t2=nn(oc["source_species"]["T2_unscaled_sup"]);t3=nn(oc["source_species"]["T3_unscaled_sup"])
    T2=up(p*length.sqrt()*t2);T3=up(p*length.sqrt()*t3)
    d=q(PARAMETERS["delta_half_width"])
    F=up(d*S+d*d*T2+d*d*d*T3)
    Fphi=up(d*Sphi+896*d*d*T2+1152*d*d*d*T3)
    return dict(exact_interval=list(map(str,COLLAR)),
        copied_NR_complete_wide_nonmean=win,
        saved_operator_repair_source_sup=prev["old_complete_repair_sup"],
        saved_continuity_offset_source_sup=prev["canonical_continuity_offset_sup"],
        complete_scaled_repair_and_offset_fee=record(fee),
        complete_S96_upper=record(S),complete_S96_angle_upper=record(Sphi),
        saved_pointwise_T2=oc["source_species"]["T2_unscaled_sup"],
        saved_pointwise_T3=oc["source_species"]["T3_unscaled_sup"],
        complete_wide_T2_L2_upper=record(T2),complete_wide_T3_L2_upper=record(T3),
        complete_known_F96_upper=record(F),complete_known_F96_angle_upper=record(Fphi),
        known_H288_source_exactly_zero=True,known_H288_angle_source_exactly_zero=True,
        all_mean_and_repair_fees_retained=True,ordinary_mean_killed_only_by_high_projection=True,
        narrow_L2_source_not_relabelled_as_wide=True,unknown_ordinary_source_still_required_if_not_true_solution=True)

def ordinary_coefficients(old,mean,source,radius):
    v=intrinsic_bounds(old)
    ref=old["best_complete_case_per_radius"][NARROW_RADII[0]]["coefficients"]
    rho=q(radius);d=q(PARAMETERS["delta_half_width"]);p=v["p"]
    mean_raw=low(mean["raw_full_moving_mean_gap_lower"])
    mean_ref=low(mean_raw-q(PARAMETERS["centre_repair_mean"])-19*d)
    mean_actual=low(mean_ref-rho)
    if not mean_actual>0:raise ValueError("the declared wide C0 radius does not preserve the actual negative mean")
    amin=low(v["Glo"]*v["sqrtKlo"]*mean_actual)
    if not amin>0:raise ValueError("the actual projected energy has no positive speed")
    M0=nn(ref["M0"]);M1=nn(ref["M1"]);M2=nn(ref["M2"]);eta=up(p*rho);M=up(M0+eta)
    b=v["b"];g=v["g"];alpha=v["alpha"]
    drift=up(nn(ref["D0"])+b*(2*M0*eta+eta*eta))
    Shi=up(min(v["k"]*(q(7)+19*d+rho)**2,v["sqrtKhi"]*M*M))
    Slo=low(v["Klo"]*mean_actual*mean_actual)
    L=up(v["Glog"]+v["Klog"]/2+v["beta"]*max(abs(1-Slo),abs(1-Shi)))
    cp=up(2/amin);cr=up(1+2*drift/amin)
    A0=up(alpha+3*b*M*M+(b*M/2+g)*M1)
    Astar=up(alpha+3*b*M0*M0+(b*M0/2+g)*M1)
    Ad=up(b*eta*(3*M0+eta+M1/4));dd=up(b*(2*M0+eta)*eta/2)
    A1=up(alpha+5*b*M*M);B10=up(8*b*M*M1+(b*M/2+g)*M2)
    kcut=q(PARAMETERS["cutoff_derivative_upper"])
    k96=up((1+q(Fraction(1,388**2))).sqrt());k288=up((1+q(Fraction(1,1156**2))).sqrt())
    la96=up(arb(1+384**2).sqrt());la288=up(arb(1+1152**2).sqrt())
    v96=up(p*(k96*cp*cr).sqrt());v288=up(p*(k288*cp*cr).sqrt())
    middle=up(la288.sqrt()*v96)
    e96L=up(A0+384*drift);e96H=up(A0+L+kcut)
    farL=up(Ad+384*dd);farH=up(Astar+Ad+((1152*drift)**2+(L+kcut)**2).sqrt())
    known=up(middle*nn(source["complete_known_F96_upper"]))
    rstar=q(Fraction(63,320))*d
    return dict(raw_wide_C0_pair_radius=radius,exact_wide_interval=list(map(str,COLLAR)),
        raw_mean_gap=mean["raw_full_moving_mean_gap_lower"],reference_mean_gap=record(mean_ref),
        actual_mean_gap=record(mean_actual),principal_speed_lower=record(amin),
        speed_log_derivative=record(L),drift_upper=record(drift),
        P_upper=record(p),M0=record(M0),M1=record(M1),M2=record(M2),eta=record(eta),
        alpha=record(alpha),b=record(b),g=record(g),complete_A0=record(A0),
        complete_Astar=record(Astar),complete_A_difference=record(Ad),complete_d_difference=record(dd),
        complete_A1=record(A1),complete_B10=record(B10),cp=record(cp),cr=record(cr),
        triangular_cutoff_derivative_upper="20",
        E96_positive_body_coefficients=records(dict(ZL=e96L,ZH=e96H)),
        E288_positive_body_coefficients=records(dict(ZL=farL,ZH=farH)),
        E288_exact_three_band_coefficients=records(dict(
            ZH=Astar,Zfull=Ad,ZL=384*dd,Zmiddle=1152*drift,Zfar=L+kcut)),
        half_trace_factors=records(dict(V96_per_E96=v96,V288_per_E288=v288)),
        finite_raw_cut_L2_to_H1=record(la96),middle_H1_per_E96=record(middle),
        known_middle_source_upper=record(known),full_W_low_sufficient_radius=record(rstar),
        signed_budget_after_known_middle=record(rstar-known),
        wide_factorial_gate_recomputed=False,wide_high_domain_claimed=False,
        admissible_narrow_MA_radii_if_same_state_satisfies_them=NARROW_RADII,
        far_interpolation=dict(prefactor="2^24",exponent_numerator=16384,exponent_denominator=16385,
            high_bound="2^377903",high_domain="independent same-state narrow MA domain"),
        all_body_variables_P_scaled=True,full_finite_mean_retained=True,
        actual_unknown_body_bound_supplied=False,actual_unknown_cut_bound_supplied=False,
        actual_low_physical_gamma_entry_proved=False,
        direct_two_energy_cutoff_fees_not_changed=True)

def run(a,doc):
    ctx.prec=a.bits
    old,nr,mc,raw=inputs(a,doc)
    mean=mean_window(raw["rows"])
    gate(doc,"the new wide full-moving-mean restriction has complete true radial coverage",
         mean["exact_interval"]==PARAMETERS["exact_wide_interval"]
         and mean["exact_radial_measure"]=="1/10" and mean["original_closed_rows_consumed"]>0
         and low(mean["raw_full_moving_mean_gap_lower"])>0)
    source=sources(old,nr)
    tables={rho:ordinary_coefficients(old,mean,source,rho) for rho in PARAMETERS["ordinary_wide_radii"]}
    gate(doc,"all six ordinary wide tables retain their independent narrow high input and all unknowns",
         len(tables)==6 and all(low(t["principal_speed_lower"])>0
             and t["wide_factorial_gate_recomputed"] is False and t["wide_high_domain_claimed"] is False
             and t["actual_low_physical_gamma_entry_proved"] is False
             and t["full_finite_mean_retained"] is True for t in tables.values()))
    authorizations={rho:dict(
        exact_interval=mc["corrected_retained_cases"][rho]["exact_interval"],
        raw_C0_pair_radius=rho,original_complete_case_sha256=mc["corrected_retained_cases"][rho]["original_complete_case_sha256"],
        high_trace_conclusion=mc["corrected_retained_cases"][rho]["high_trace_conclusion"])
        for rho in NARROW_RADII}
    gate(doc,"the complete known source has the exact four finite supports and both old mean windows are preserved",
         old["parameters"]["complete_source_species_degrees"]==[96,160,224,288]
         and source["known_H288_source_exactly_zero"] is True
         and nr["corrected_raw_mean_windows_copied_without_recomputation"]==mc["complete_raw_mean_windows"]
         and len(authorizations)==5)
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_new_wide_mean=mean,complete_wide_known_source=source,
        complete_wide_ordinary_coefficient_tables=tables,new_ordinary_tables_evaluated=6,
        independent_narrow_MA_authorizations=authorizations,
        complete_raw_mean_windows_copied_without_recomputation=mc["complete_raw_mean_windows"],
        old_91_case_verdicts_or_saved_tables_modified=False,old_91_cases_recomputed=0,
        successful_NR_nonmean_restrictions_recomputed=False,successful_MC_mean_restrictions_recomputed=False,
        old_high_factorial_domain_extended=False,old_high_factorial_recursion_recomputed=0,
        old_target_Fourier_residual_repair_mean_flow_or_Green_calls=0,
        old_numerical_enclosures_recomputed=0,all_original_bytes_modified=0,
        only_new_original_row_quantity="wide minimum of full moving mean_absolute_gap",
        ordinary_energy_and_same_cut_narrow_high_domains_separate=True,
        actual_core_solution_proved=False,actual_unknown_body_or_cut_bounds_supplied=False,
        actual_low_physical_gamma_entry_proved=False,new_recomputable_outputs_persisted=False)
    if len(doc["gates"])!=13:raise ValueError("the complete fixed gate inventory changed")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True);p.add_argument("--manifest-sha",required=True)
    p.add_argument("--collar-conclusion",type=Path,required=True)
    p.add_argument("--nonmean-execution",type=Path,required=True)
    p.add_argument("--corrected-mean-execution",type=Path,required=True)
    p.add_argument("--raw-manifest",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True);p.add_argument("--bits",type=int,default=320)
    a=p.parse_args();started=time.monotonic()
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        parameters=PARAMETERS,derived_continuous_centre_definition_sha256=CENTRE,
        derived_continuous_response_definition_sha256=DIRECTION,exact_eta=str(ETA),exact_nu0=str(NU))
    try:run(a,doc)
    except Exception as e:
        doc["failure"]=dict(error_type=type(e).__name__,message=str(e));doc["complete"]=False
        traceback.print_exc()
    doc["seconds"]=time.monotonic()-started
    save(a.out,doc)
    print(json.dumps(dict(complete=doc["complete"],failure=doc["failure"],
        gates_passed=sum(x["passed"] for x in doc["gates"]),gates_total=len(doc["gates"]),
        actual_wide_ordinary_tables=doc.get("new_ordinary_tables_evaluated",0),
        actual_low_physical_gamma_entry_proved=False)),flush=True)
    return 0 if doc["complete"] else 1

if __name__=="__main__":raise SystemExit(main())
