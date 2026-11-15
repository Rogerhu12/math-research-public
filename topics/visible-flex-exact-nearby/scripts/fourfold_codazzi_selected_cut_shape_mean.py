#!/usr/bin/env python3
"""Read accepted complete cut coefficients; compute new scalar shape/mean bounds.

No old target, trial evaluation, matrix, angle composition, repair sequence,
boundary row, or Green operator is recomputed. Public Actions only.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_selected_cut_shape_mean.py"
KIND="actual_complete_selected_cut_shape_mean_scalar_conclusion_v1"
BOUNDARY_SHA="b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263"
BOUNDARY_BYTES=89319
BOUNDARY_PROCESS_SHA="6ff7f39ab70150f99eebb8a880fb0f52867574b25e122b59d95c1a0105e2609e"
BOUNDARY_SOURCE_SHA="79796ab53f20088da1ef11261be81e2ce548c16772c991eb9d5e8148b2b23204"
BASE_SHA="119dedb2e62f23553b81dea9eb787d8298c1224eebc2cc38790ec50274df0ca7"
BASE_SOURCE_SHA="36f8d6e47eaea2e9154d1e1683158a25a90bddcf158bfb488f4c51ab44ebea5c"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
TRIAL="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)
PARAMETERS=dict(arithmetic_bits=320,exact_cut="9/10",raw_response_side="left",
    response_sine_modes=96,response_cosine_modes=96,independent_even_mean=True,
    response_degree=96,base_degree=32,
    delta_half_width="1/10000000000",
    response_repair_pair_A0="0.0000000000000002292",
    physical_gamma_radius="1/1000000000",physical_gamma_fraction="1/128",
    physical_gamma_low_neighbourhood_H1="1/1024",
    old_base_jacobian_angle_A0_bound="1/16",
    ordinary_circle_measure="normalized circle in the same original moving angle",
    physical_response_amplitudes_not_scaled_by_alpha=True,
    full_raw_mean_not_replaced_by_original_mean_flow_correction=True,
    zero_old_target_trial_angle_repair_matrix_or_Green_recomputation=True,
    no_core_existence_unknown_correction_or_low_selfmap_claim=True)

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)
def save(path,value,small=False):
    raw=canonical(value)
    if small and len(raw)>55000:raise ValueError("the complete small conclusion exceeds55000 UTF8 bytes")
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".partial");t.write_bytes(raw);t.replace(p)
def exact(x):
    x=Fraction(x);return arb(x.numerator)/x.denominator
def box(x):
    if not isinstance(x,dict):raise ValueError("a saved directed coefficient interval is required")
    if "lower" in x and "upper" in x:
        y=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
    elif "ball" in x:y=arb(x["ball"])
    else:raise ValueError("a bare coefficient midpoint is not an accepted input")
    if not y.is_finite():raise ValueError("a saved coefficient interval is nonfinite")
    return y
def upper(x):
    y=arb(x)
    if not y.is_finite():raise ValueError("nonfinite scalar upper")
    return y.upper()
def modulus(x):return abs(arb(x)).upper()
def rec(x):
    y=arb(x)
    if not y.is_finite():raise ValueError("nonfinite scalar output")
    return dict(ball=y.str(48))
def recorded(d):return {k:rec(v) for k,v in d.items()}
def gate(doc,name,ok):
    doc["gates"].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError("cut shape/mean identity gate failed: "+name)
def complete(d):
    return d.get("complete") is True and d.get("failure") is None and bool(d.get("gates")) and all(
        g.get("passed") is True for g in d["gates"])
def trig_norm(amplitudes,offset=0,derivative=0):
    """L2 norm of physical sin/cos amplitudes, with a separate genuine mean."""
    s=modulus(offset)**2 if derivative==0 else arb(0)
    for j,c in enumerate(amplitudes,1):
        weight=arb(4*j)**derivative
        s+=weight**2*modulus(c)**2/2
    return s.upper().sqrt().upper()
def trig_A0(amplitudes,offset=0,derivative=0):
    s=modulus(offset) if derivative==0 else arb(0)
    return upper(s+sum((arb(4*j)**derivative*modulus(c)
                        for j,c in enumerate(amplitudes,1)),arb(0)))
def trig_H1(amplitudes,offset=0):
    s=modulus(offset)**2
    s+=sum(((1+arb(4*j)**2)*modulus(c)**2/2
            for j,c in enumerate(amplitudes,1)),arb(0))
    return s.upper().sqrt().upper()

def inputs(a,doc):
    manifest=read(a.manifest)
    gate(doc,"new exact scalar parameters and scientific source are immutable",
         sha(a.manifest)==a.manifest_sha and manifest["parameters"]==PARAMETERS
         and manifest["files"].get(PRODUCER)==sha(__file__))
    gate(doc,"both saved native identities and the actual original boundary process are exact",
         sha(a.boundary)==BOUNDARY_SHA and Path(a.boundary).stat().st_size==BOUNDARY_BYTES
         and sha(a.boundary_process)==BOUNDARY_PROCESS_SHA and sha(a.base_cut)==BASE_SHA)
    old=read(a.boundary);process=read(a.boundary_process);base=read(a.base_cut)
    gate(doc,"the original public boundary run completed all ten gates without changing the physical trial",
         process.get("repository")=="Rogerhu12/math-research-public"
         and str(process.get("run_id"))=="43599771405"
         and process.get("complete") is True and process.get("failure") is None
         and process.get("complete_native_sha256")==BOUNDARY_SHA
         and process.get("actual_public_complete_boundary_source_gates")==10
         and bool(process.get("children"))
         and all(c.get("actual_returncode")==0 for c in process["children"]))
    gate(doc,"the stored boundary is the same raw physical full193 trial at the same repaired centre",
         complete(old) and len(old["gates"])==10
         and old.get("kind")=="actual_known_response_waist_and_true_homogeneous_cap_sources_v1"
         and old.get("source_sha256")==BOUNDARY_SOURCE_SHA
         and old.get("candidate_sha256")==CANDIDATE
         and old.get("derived_definition_sha256")==CENTRE
         and old.get("full_physical_response_trial_sha256")==TRIAL
         and old.get("exact_affine_parameter_offset")=="0"
         and old.get("exact_interior_interval")==["0","9/10"])
    trace=old["cut_trace"]
    gate(doc,"the original cut is the complete left interior trace with all signed physical amplitudes",
         trace.get("exact_radius")=="9/10" and trace.get("interior_trace_side")=="left"
         and trace.get("all_96_odd_and_97_even_including_mean_retained") is True
         and trace.get("original_physical_trial_not_multiplied_by_alpha") is True
         and len(trace.get("complete_193_raw_physical_amplitudes",[]))==193)
    raw=[box(x) for x in trace["complete_193_raw_physical_amplitudes"]]
    gate(doc,"the accepted base cut stores the same exact repaired finite32 endpoint and complete mean",
         complete(base)
         and base.get("kind")=="actual_repaired_moving96_physical128_complete_C_port_matrix"
         and base.get("source_sha256")==BASE_SOURCE_SHA
         and base.get("candidate_sha256")==CANDIDATE
         and base.get("derived_definition_sha256")==CENTRE
         and base.get("exact_cut")=="9/10"
         and Fraction(base["exact_alpha"])==ALPHA and Fraction(base["exact_nu"])==NU
         and base.get("whole_original_eta") is True
         and Fraction(base["parameter_half_width"])==Fraction(1,10**9)
         and len(base.get("exact_cut_finite_candidate",[]))==65
         and len(base.get("exact_cut_physical_offset",[]))==65
         and len(base.get("complete_phase_sine_coefficients",[]))==32)
    values=list(map(Fraction,base["exact_cut_finite_candidate"]))
    offsets=list(map(Fraction,base["exact_cut_physical_offset"]))
    mean=box(base["complete_actual_mean"])
    gate(doc,"the actual repaired base mean is negative with the original shape neighbourhood margin",
         -mean>exact(Fraction(25,8))
         and box(base["actual_physical_angle_Jacobian_lower"])>0)
    # The following is exact arithmetic on saved values, not a new endpoint evaluation.
    vcos=[exact(ALPHA*values[32+j]+offsets[32+j]) for j in range(1,33)]
    jcos=[v/mean for v in vcos]
    for j,(jc,phase) in enumerate(zip(jcos,base["complete_phase_sine_coefficients"]),1):
        if not (jc-4*j*box(phase)).contains(0):
            raise ValueError("the saved base phase and exact finite endpoint are inconsistent")
    gate(doc,"the exact base shape agrees with every saved phase coefficient including the true mean",True)
    doc["original_input_scope"]=dict(
        raw_native_sha256=BOUNDARY_SHA,raw_native_bytes=BOUNDARY_BYTES,
        raw_process_sha256=BOUNDARY_PROCESS_SHA,base_native_sha256=BASE_SHA,
        base_native_bytes=Path(a.base_cut).stat().st_size,
        raw_trace_piece=trace["original_response_piece"],
        base_trace_piece=base["actual_candidate_piece"],
        same_true_cut="9/10",raw_side="left",
        base_endpoint_continuity_from_exact_repair=True,
        base_whole_eta_box_used_only_as_enclosure_of_fixed_eta0=True,
        complete_response_mean_flow_correction_not_consumed=True,
        raw_and_continuous_direction_not_identified=True,
        derived_continuous_direction_definition_sha256=DIRECTION)
    return raw,jcos,mean

def scalar_bounds(raw,jcos,mean):
    xi=raw[:96];mu=raw[96];zeta=raw[97:]
    E=exact(PARAMETERS["response_repair_pair_A0"]);E1=384*E
    M=upper(modulus(mu)+E)
    xi0=trig_A0(xi);xi1=trig_A0(xi,derivative=1)
    zeta0=trig_A0(zeta,mu);zeta1=trig_A0(zeta,derivative=1)
    phi=trig_norm(zeta,derivative=1)
    h1=trig_H1(zeta,mu)
    jA1=trig_A0(jcos,derivative=1);jL1=trig_norm(jcos,derivative=1)
    # J.4 is an independent proved bound for the same fixed eta0 base.
    jL1=upper(min(jL1,exact(Fraction(1,16))))
    shape=[z-mu*(jcos[k] if k<32 else arb(0)) for k,z in enumerate(zeta)]
    shape_raw=trig_norm(shape,derivative=1)
    shape_A0_raw=trig_A0(shape)
    shape_A1_raw=trig_A0(shape,derivative=1)
    jA0_nonmean=trig_A0(jcos)
    Dz=upper(phi+E1)
    correlated=upper(shape_raw+E1+jL1*E)
    triangular=upper(Dz+jL1*M)
    shape_bound=upper(min(correlated,triangular))
    gamma_per_delta=upper(shape_bound/16+M/576)
    # This second formula remains a separate complete bound, not an entrywise minimum.
    gamma_per_delta=upper(min(gamma_per_delta,Dz/16+13*M/2304))
    Zh1=upper(h1+(1+arb(384)**2).sqrt()*E)
    raw_pair=upper(trig_norm(xi)**2+trig_norm(zeta,mu)**2).sqrt().upper()
    bounds=dict(
        xi_A0=upper(xi0+E),xi_phi_A0=upper(xi1+E1),
        zeta_A0=upper(zeta0+E),zeta_phi_A0=upper(zeta1+E1),
        zeta_nonmean_A0=upper(trig_A0(zeta)+E),
        zeta_mean_absolute=M,
        pair_A0=upper(xi0+zeta0+E),
        pair_phi_A0=upper(xi1+zeta1+E1),
        pair_L2=upper(raw_pair+E),
        xi_L2=upper(trig_norm(xi)+E),
        xi_phi_L2=upper(trig_norm(xi,derivative=1)+E1),
        zeta_L2=upper(trig_norm(zeta,mu)+E),zeta_phi_L2=Dz,zeta_H1=Zh1,
        base_j0_nonmean_A0_from_saved_coefficients=jA0_nonmean,
        base_j0_phi_A0_from_saved_coefficients=jA1,
        base_j0_phi_L2_used=jL1,
        correlated_raw_shape_phi_L2=shape_raw,
        complete_correlated_shape_phi_L2=correlated,
        complete_triangular_shape_phi_L2=triangular,
        complete_shape_phi_L2=shape_bound,
        complete_shape_A0=upper(shape_A0_raw+(1+jA0_nonmean)*E),
        complete_shape_phi_A0=upper(shape_A1_raw+E1+jA1*E),
        physical_gamma_A0_per_abs_delta=gamma_per_delta,
        exact_continuous_repair_pair_A0_fee=E,
        exact_continuous_repair_pair_phi_A0_fee=E1,
        exact_continuous_repair_shape_A0_fee=upper((1+jA0_nonmean)*E),
        exact_continuous_repair_shape_phi_L2_fee=upper(E1+jL1*E))
    d=exact(PARAMETERS["delta_half_width"])
    gamma_target=exact(PARAMETERS["physical_gamma_radius"])*exact(PARAMETERS["physical_gamma_fraction"])
    contribution=upper(d*gamma_per_delta)
    room=(gamma_target-contribution).lower()
    nroom=(exact(PARAMETERS["physical_gamma_low_neighbourhood_H1"])-d*Zh1).lower()
    positive=bool(room>0 and nroom>0)
    allowed=min((15*room).lower(),nroom).lower() if positive else arb(0)
    conclusion=dict(
        exact_delta_half_width=PARAMETERS["delta_half_width"],
        selected_parameter_known_gamma_A0_upper=rec(contribution),
        exact_target_gamma_A0=rec(gamma_target),
        remaining_gamma_budget_lower=rec(room),
        remaining_total_H1_neighbourhood_lower=rec(nroom),
        positive_remaining_low_gamma_budget_proved=positive,
        sufficient_unknown_comparison_zeta_H1_radius_lower=rec(allowed),
        unknown_comparison_was_not_evaluated=True,
        sufficient_condition="for the same real cut, the unknown v-Qdelta_v H1 norm is at most the displayed nonnegative lower radius; J.18 and the total H1 neighbourhood then imply the physical gamma A0 gate",
        no_core_solution_or_selfmap_is_asserted=True)
    signed_mu=mu+arb(0,E.upper())
    audit=dict(
        raw_signed_full193_physical_amplitudes=[rec(x) for x in raw],
        raw_signed_even_mean=rec(mu),
        complete_continuous_even_mean_enclosure=rec(signed_mu),
        original_base_signed_mean=rec(mean),
        complete_base_j0_nonmean_cosine_intervals=[rec(x) for x in jcos],
        signed_correlated_raw_shape_cosine_intervals=[rec(x) for x in shape],
        ordinary_physical_frequency_factor=4,
        physical_sine_cosine_square_Gram="1/2",
        independent_even_mean_square_Gram="1",
        odd_mean_exactly_zero_by_the_original_reflection_sector=True,
        shape_mean_exactly_zero_by_subtracting_the_same_complete_even_mean=True)
    return bounds,conclusion,audit,signed_mu

def run(a,doc):
    raw,jcos,mean=inputs(a,doc)
    bounds,condition,audit,signed_mu=scalar_bounds(raw,jcos,mean)
    gate(doc,"all full193 component norms and the signed correlated shape were evaluated with complete repair fees",
         len(raw)==193 and len(jcos)==32 and len(audit["signed_correlated_raw_shape_cosine_intervals"])==96
         and all(x.is_finite() and x>=0 for x in bounds.values()))
    save(a.temporary_audit,audit)
    doc.update(
        complete_scalar_bounds=recorded(bounds),
        complete_continuous_even_mean_signed=rec(signed_mu),
        original_base_mean_signed=rec(mean),
        conditional_low_gamma_entry=condition,
        all_193_raw_amplitudes_used_before_absolute_values=True,
        known_base32_shape_subtracted_before_norm=True,
        physical_response_alpha_factor_applied=False,
        mean_corrected_qstar_not_substituted_for_Z=True,
        exact_continuous_response_offset_paid_once=True,
        original_response_slots={"odd_nonmean":96,"even_mean":1,"even_nonmean":96},
        actual_new_scalar_coefficient_consumption_complete=True,
        old_target_trial_angle_repair_matrix_Green_recomputations=0,
        old_native_bytes_changed=0,
        no_core_existence_unknown_correction_or_low_selfmap_claim=True,
        temporary_complete_signed_audit=dict(bytes=Path(a.temporary_audit).stat().st_size,
            sha256=sha(a.temporary_audit),persisted=False),
        complete=True)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","boundary","boundary-process","base-cut","out","temporary-audit"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    a=p.parse_args();ctx.prec=PARAMETERS["arithmetic_bits"];ctx.cap=6
    if a.out.exists():raise FileExistsError("preserve every earlier actual scientific conclusion")
    started=time.monotonic()
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        parameters=PARAMETERS,input_sha256=dict(manifest=sha(a.manifest),
            boundary=sha(a.boundary),boundary_process=sha(a.boundary_process),base_cut=sha(a.base_cut)))
    code=0
    try:run(a,doc)
    except BaseException as error:
        code=1;doc["failure"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    finally:
        doc["seconds"]=time.monotonic()-started
        save(a.out,doc,small=True)
    print(json.dumps(dict(complete=doc["complete"],gates=len(doc["gates"]),
        source_sha256=doc["source_sha256"],summary_sha256=sha(a.out)),sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":main()
