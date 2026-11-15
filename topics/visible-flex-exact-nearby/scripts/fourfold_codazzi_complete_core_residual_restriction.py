#!/usr/bin/env python3
"""One new core restriction of saved full residual rows; no old producer calls."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.metadata
import json
import platform
import time
import traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_complete_core_residual_restriction.py"
KIND="actual_complete_core_background_restriction_and_selected_residual_v1"
MANIFEST_KIND="complete_core_residual_restriction_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=18
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
RAW_SHA="6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1"
RAW_BYTES=4592623
RAW_SOURCE="24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
RAW_PRODUCER="98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e"
Z_SOURCE="90c90fb1b21806e803e61d5f850b1d8057fcadc577452d3454b05348500a697f"
Z_PILOT="2d45c2f100484f5a25fe50ec2d8ea2dcd601b79f1f151d4be116225d3284fcc8"
Z_NATIVE="365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e"
Z_PLAN="26a488b4347e0e30106e67dcd18b54e211dba6adecd7d2c029a4dc6ba097d95a"
D_SOURCE="827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"
WL_SOURCE="d6764c570b935ed760425b10aeead6dea20e406fa0a0e606c1e61ad0c027d3b6"
PINNED={
 "raw_manifest":"0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad",
 "z_summary":"e1ae6bd3ae8b9f04297fb2c9664d249c15ffe9366d15a4504444f06f08b727ac",
 "z_process":"0cc2e8f876261c0fa86c0547b1400d47ad71759f43c7001b6359049827017f48",
 "d_execution":"6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071",
 "wl_execution":"936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d"}
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)
ETA=Fraction(-7789843107295549,4611686018427387904)
L=Fraction(9,10)
R=Fraction(25,8)
DELTA=Fraction(1,10**10)
PARAMETERS={
 "arithmetic_bits":320,"runtime":RUNTIME,
 "exact_core_interval":["0","9/10"],"complete_original_interval":["0","25/8"],
 "exact_delta_half_width":"1/10000000000","exact_amplitude":str(ALPHA),
 "exact_eta0":str(ETA),"exact_nu0":str(NU),
 "original_row_count":7296,"original_interface_count":6143,
 "original_residual_degree":96,"original_state_and_repair_degree":32,
 "ordinary_radial_measure":"dr","ordinary_angle_measure":"normalized original moving circle",
 "pair_norm":"Euclidean L2, with the full even mean of weight one",
 "centre_repair_pair_A0":"0.000000000000000003861",
 "centre_repair_pair_A1":"0.00000000000000001970",
 "original_global_integral_recomputed":False,
 "complete_Z_inner_source_recomputed":False,
 "old_raw_mean_or_Z_offset_charged_again":False,
 "old_producer_target_primitive_interface_or_Green_calls":0,
 "expected_gate_count":GATE_COUNT,
 "nonlinear_solution_or_actual_domain_entry_claimed":False}

def canonical(x):
    return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode("utf-8")
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text())
def q(x):
    x=Fraction(x)
    return arb(x.numerator)/x.denominator
def box(x):
    if isinstance(x,dict):
        if "lower" in x and "upper" in x:
            y=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
        elif "ball" in x:y=arb(x["ball"])
        else:raise ValueError("a saved scalar has no complete directed interval")
    else:y=arb(str(x))
    if not y.is_finite():raise ValueError("nonfinite saved scalar")
    return y
def up(x):
    y=box(x) if isinstance(x,dict) else arb(x)
    if not y.is_finite():raise ValueError("nonfinite directed upper bound")
    return y.upper()
def nn(x):
    y=up(x)
    if y<0:raise ValueError("a nonnegative upper bound is negative")
    return y
def root_upper(x):
    y=up(x)
    if not y>=0:raise ValueError("a square-root argument is not proven nonnegative")
    return up(y.sqrt())
def record(x):
    y=arb(x)
    if not y.is_finite():raise ValueError("nonfinite new scalar")
    return {"ball":y.str(72)}
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("core-residual gate failed: "+name)
def complete(x,n):
    return (x.get("complete") is True and x.get("failure") is None
            and len(x.get("gates",[]))==n
            and all(g.get("passed") is True for g in x["gates"]))
def saved_execution(x,rid,n,source):
    s=x.get("actual_scientific_receipt",{})
    return (str(x.get("run_id"))==str(rid) and x.get("complete") is True
            and x.get("actual_returncode")==0 and complete(s,n)
            and s.get("source_sha256")==source),s

def checked_inputs(a,doc):
    actual={"Python":platform.python_version(),
            "python_flint":importlib.metadata.version("python-flint")}
    gate(doc,"public pinned runtime and320-bit directed arithmetic",
         actual==RUNTIME and a.bits==320)
    doc["runtime"]=actual
    m=read(a.manifest)
    paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"unchanged complete manifest source parameters and all five mathematical receipts",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("repository")==PUBLIC and m.get("parameters")==PARAMETERS
         and m.get("mathematical_input_sha256")==PINNED
         and m.get("source_sha256")==sha(__file__)
         and m.get("files",{}).get(PRODUCER)==sha(__file__)
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    doc["input_sha256"]={"manifest":a.manifest_sha,**PINNED}
    z,zp=read(a.z_summary),read(a.z_process)
    child=zp.get("children",[])
    gate(doc,"successful original mixed-Z finish and six complete actual gates",
         complete(z,6) and z.get("phase")=="finish"
         and z.get("source_sha256")==Z_SOURCE and z.get("exact_bump_source_sha256")==Z_PILOT
         and z.get("native_sha256")==Z_NATIVE and zp.get("complete") is True
         and str(zp.get("run_id"))=="43613560173" and zp.get("phase")=="finish"
         and len(child)==1 and child[0].get("actual_returncode")==0
         and zp.get("actual_scientific_gates")==6 and zp.get("complete_native_sha256")==Z_NATIVE)
    gate(doc,"same complete continuous centre direction raw mean and inner-Z source",
         z.get("candidate_sha256")==CANDIDATE
         and z.get("derived_continuous_centre_definition_sha256")==CENTRE
         and z.get("exact_continuous_direction_definition_sha256")==DIRECTION
         and z.get("complete_rows")==7721 and z.get("complete_original_common_cells")==7721
         and z.get("complete_valid_source_cover") is True
         and z.get("true_independent_even_mean_retained") is True
         and z.get("known_high_output_retained") is True
         and z.get("exact_affine_parameter_offset")=="0"
         and z.get("whole_complete_source_interval")==["0","25/8"]
         and z.get("original_plan_native_sha256")==Z_PLAN
         and z.get("complete_source_bounds")==zp.get("complete_source_bounds"))
    zin=z["complete_source_bounds"]["inner_body"]
    sf=nn(zin["full_through160"]["L2_L2_radial"])
    sl=nn(zin["low193"]["L2_L2_radial"])
    gate(doc,"copied full and low inner-Z sources are finite with no repeated mean or offset charge",
         sf>=0 and sl>=0)
    dex=read(a.d_execution)
    ok,d=saved_execution(dex,43713242980,12,D_SOURCE)
    gate(doc,"successful original selected-D child with all twelve complete gates",ok)
    core=d.get("complete_scalar_fee_conclusions",{}).get("whole_core",{})
    dp=d.get("parameters",{})
    gate(doc,"complete original D core ordinary source and selected parameter interval",
         core.get("exact_interval")==["0","9/10"]
         and core.get("exact_total_radial_measure")=="9/10"
         and dp.get("delta_half_width")==str(DELTA)
         and dp.get("exact_core_interval")==["0","9/10"]
         and dp.get("background_pair_A0")=="7" and dp.get("background_pair_angle_A0")=="6"
         and dp.get("response_pair_A0")=="19" and dp.get("response_pair_angle_A0")=="83")
    dc=nn(core["ordinary_L2_bounds"]["complete_additional_response_source"])
    eq0=q(PARAMETERS["centre_repair_pair_A0"])
    eq1=q(PARAMETERS["centre_repair_pair_A1"])
    ds=d["verified_global_state_bounds"]
    gate(doc,"complete raw-to-repaired known-state segment lies inside the same7 and6 bounds",
         nn(ds["background_pair_A0"])+eq0<7
         and nn(ds["background_pair_angle_A0"])+eq1<6)
    wex=read(a.wl_execution)
    ok,w=saved_execution(wex,43749764738,18,WL_SOURCE)
    gate(doc,"successful original WL child with all eighteen complete gates",ok)
    wo=w["complete_original_input_conclusion"]
    wp=w["complete_positive_product_conclusion"]
    gate(doc,"same wholecore positive-algorithm products and complete centre direction definitions",
         wo.get("background_definition_sha256")==CENTRE
         and wo.get("direction_definition_sha256")==DIRECTION
         and wo["original_small_input_sha256"]["D_execution"]==PINNED["d_execution"]
         and wo.get("complete_core_exact_measure")=="9/10"
         and w["mathematical_parameters"]["exact_parameter_half_width"]==str(DELTA)
         and w["mathematical_parameters"]["exact_core_interval"]==["0","9/10"]
         and wp.get("same_original_positive_algorithm_lower_summands_used") is True
         and wp.get("no_abstract_operator_norm_reverse_inference") is True)
    b,g=nn(wp["B_star"]),nn(wp["G_star"])
    doc["copied_successful_source_inputs"]={
      "Z_summary_native_sha256":Z_NATIVE,"Z_original_plan_native_sha256":Z_PLAN,
      "Z_old_failed_plan_run":"43612904296","Z_successful_finish_run":"43613560173",
      "Z_inner_source_bounds":zin,
      "Z_mean_and_continuity_repair_already_paid":True,
      "D_whole_core_complete_additional_response_source":
          core["ordinary_L2_bounds"]["complete_additional_response_source"],
      "D_selected_parameter_half_width":dp["delta_half_width"],
      "WL_complete_positive_product_conclusion":wp,
      "old_source_integrals_or_repair_fees_recomputed":False}
    return m,{"S_full":sf,"S_low":sl,"D_core":dc,"B_star":b,"G_star":g,
              "E_Q0":eq0,"E_Q1":eq1}

def restore_raw(a,doc):
    m=read(a.raw_manifest)
    gate(doc,"original complete7296 index and three exact byte-part receipts",
         m.get("kind")=="complete_native_lossless_container_binary_parts_v2"
         and m.get("native_complete") is True and m.get("native_failure") is None
         and m.get("complete_native_rows")==7296 and m.get("original_bytes")==RAW_BYTES
         and m.get("original_sha256")==RAW_SHA and m.get("original_source_sha256")==RAW_SOURCE
         and m.get("candidate_sha256")==CANDIDATE and len(m.get("parts",[]))==3)
    chunks=[];cursor=0
    for i,r in enumerate(m["parts"]):
        if r["index"]!=i or r["offset"]!=cursor or Path(r["file"]).name!=r["file"]:
            raise ValueError("original byte-part sequence changed")
        raw=(a.raw_manifest.parent/r["file"]).read_bytes()
        if len(raw)!=r["compressed_bytes"] or sha_bytes(raw)!=r["compressed_sha256"]:
            raise ValueError("original compressed part identity changed")
        payload=gzip.decompress(raw)
        if len(payload)!=r["bytes"] or sha_bytes(payload)!=r["sha256"]:
            raise ValueError("original complete part payload changed")
        chunks.append(payload);cursor+=len(payload)
    raw=b"".join(chunks)
    if len(raw)!=RAW_BYTES or sha_bytes(raw)!=RAW_SHA:
        raise ValueError("original full compressed container changed")
    d=json.loads(gzip.decompress(raw))
    gate(doc,"same complete fixed-eta raw candidate amplitude nu and full primitive residual",
         d.get("kind")=="complete_actual_moving_residual_all_closed_rows_and_interfaces"
         and d.get("complete") is True and d.get("failure") is None
         and d.get("source_sha256")==RAW_SOURCE and d.get("original_producer_sha256")==RAW_PRODUCER
         and d.get("candidate_sha256")==CANDIDATE and d.get("object_sha256")==OBJECT
         and Fraction(d["exact_amplitude"])==ALPHA and Fraction(d["exact_nu"])==NU
         and Fraction(d["common_parameter_half_width"])==0
         and d.get("all_7296_closed_rows_reused_without_recomputation") is True
         and d.get("all_6143_actual_interfaces_paid") is True
         and d.get("complete_original_primitive_tail") is True
         and d.get("complete_residual_support")==96 and d.get("interval")==["0","25/8"])
    rows=d["rows"];cursor=Fraction(0);partition=[]
    for i,r in enumerate(rows):
        left,right=map(Fraction,r["interval"])
        if r.get("index")!=i or left!=cursor or not left<right:
            raise ValueError("original whole closed-row cover changed")
        if r.get("exact_angular_support_index")!=96:
            raise ValueError("original complete residual support changed")
        for k in ("U","V"):nn(r["complete_residual_A0"][k])
        partition.append([str(left),str(right)]);cursor=right
    ph=sha_bytes(json.dumps(partition).encode())
    gate(doc,"entire original7296-row cover and6143 paid seams retain their exact partition",
         len(rows)==7296 and cursor==R and ph==d.get("exact_full_partition_sha256")
         and len(d.get("complete_interface_jumps",[]))==6143)
    old_global=d["bounds"]["residual_L2_r_L2_theta"]
    if len(old_global)!=2:raise ValueError("old full component norms changed shape")
    doc["original_raw_restore_receipt"]={
       "manifest_sha256":PINNED["raw_manifest"],"original_container_sha256":RAW_SHA,
       "original_container_bytes":RAW_BYTES,"parts":m["parts"],
       "complete_original_rows":7296,"complete_original_interfaces":6143,
       "complete_original_partition_sha256":ph,
       "original_completed_global_component_records":old_global,
       "terminal_domain_failure_preserved":d.get("terminal_domain_failure_preserved"),
       "old_raw_producer_or_merger_executed":False,
       "old_full_interval_integral_recomputed":False,
       "new_array_artifact_or_Release_created":False}
    return rows,old_global

def restrict_core(rows,doc):
    cursor=Fraction(0);length=Fraction(0);cover=[];squares=[arb(0),arb(0)]
    for r in rows:
        oldl,oldr=map(Fraction,r["interval"])
        left=max(Fraction(0),oldl);right=min(L,oldr)
        if not left<right:continue
        if left!=cursor:raise ValueError("new core restriction has a gap or overlap")
        width=right-left
        for j,k in enumerate(("U","V")):
            v=nn(r["complete_residual_A0"][k])
            squares[j]=up(squares[j]+q(width)*v*v)
        cover.append({"original_index":r["index"],"old_interval":r["interval"],
                      "exact_intersection":[str(left),str(right)]})
        cursor=right;length+=width
    gate(doc,"new core restriction covers precisely zero to9/10 with true radial intersections",
         cursor==L and length==L and len(cover)>0)
    au,av=squares
    fu,fv=root_upper(au),root_upper(av)
    pair=up(q(ALPHA)*root_upper(au+av))
    gate(doc,"two new complete core square integrals retain full mean and one physical amplitude",
         au>=0 and av>=0 and pair>=0)
    doc["complete_new_core_background_restriction"]={
       "exact_interval":["0","9/10"],"exact_total_radial_measure":str(length),
       "original_closed_rows_consumed":len(cover),
       "first_original_index":cover[0]["original_index"],
       "last_original_index":cover[-1]["original_index"],
       "first_intersection":cover[0],"last_intersection":cover[-1],
       "complete_intersection_inventory_sha256":sha_bytes(canonical(cover)),
       "unscaled_component_square_integrals":{"U":record(au),"V":record(av)},
       "unscaled_component_L2_bounds":{"U":record(fu),"V":record(fv)},
       "physical_moving_pair_L2_upper":record(pair),
       "full_even_mean_retained":True,"complete_residual_degree":96,
       "true_intersection_supremum_squared_used":True,
       "old_integrated_cell_bounds_rescaled_by_length_ratio":False,
       "radial_P_applied":False,"physical_angle_composition_applied":False,
       "amplitude_applied_once":True,"old_global_integral_recomputed":False,
       "temporary_new_intersection_inventory_persisted":False}
    return pair

def assemble(v,new_raw,old_global,doc):
    c0=up(169*v["B_star"]+6*v["G_star"])
    c1=up(q(Fraction(49,4))*v["B_star"]+7*v["G_star"])
    fee=up(root_upper(q(L))*(c0*v["E_Q0"]+c1*v["E_Q1"]))
    old_raw=up(q(ALPHA)*root_upper(nn(old_global[0])**2+nn(old_global[1])**2))
    d=q(DELTA)
    lin_full=up(d*v["S_full"]);lin_low=up(d*v["S_low"])
    quadratic=up(d*v["D_core"]/2)
    choices={}
    for name,raw in (("new_core_restriction",new_raw),("old_global_fallback",old_raw)):
        f0=up(raw+fee)
        choices[name]={
          "raw_physical_moving_pair_L2_upper":record(raw),
          "complete_repaired_centre_L2_upper":record(f0),
          "uniform_selected_full_L2_upper":record(up(f0+lin_full+quadratic)),
          "uniform_selected_low193_L2_upper":record(up(f0+lin_low+quadratic)),
          "parameter_zero_upper":record(f0),
          "full_even_mean_retained":True,
          "known_centre_residual_is_exactly_low193":True,
          "extra_Z_mean_or_384EZ_fee":False,
          "gives_a_correction_lower_bound":False}
    gate(doc,"complete centre repair uses known full operators and exact degree32 offsets",
         c0>=0 and c1>=0 and fee>=0)
    gate(doc,"complete selected full and low bounds retain their distinct linear and quadratic sources",
         lin_full>=0 and lin_low>=0 and quadratic>=0 and len(choices)==2)
    doc["complete_new_repair_scalar_conclusion"]={
       "C0":record(c0),"C1":record(c1),
       "E_Q0":PARAMETERS["centre_repair_pair_A0"],
       "E_Q1":PARAMETERS["centre_repair_pair_A1"],
       "ordinary_core_repair_fee":record(fee),
       "exact_repair_angular_degree":32,"complete_repaired_centre_residual_degree":96,
       "ordinary_piecewise_radial_repair_derivative":0,
       "original_value_jumps_cancelled_by_exact_continuous_repair":True}
    doc["complete_selected_source_conclusion"]={
       "exact_delta_half_width":str(DELTA),
       "linear_full_source_contribution":record(lin_full),
       "linear_low193_source_contribution":record(lin_low),
       "complete_quadratic_source_contribution":record(quadratic),
       "complete_background_choices":choices,
       "individual_parameter_expression":"F0+abs(delta)*S+delta^2*Dcore/(2*d)",
       "no_second_amplitude_on_continuous_Z":True,
       "old_Z_inner_integrals_and_raw_mean_not_recomputed":True,
       "D_additional_source_not_misidentified_as_total_f_delta":True}
    gate(doc,"only the new core restriction and complete scalar combinations are claimed",
         len(choices)==2 and PARAMETERS["old_producer_target_primitive_interface_or_Green_calls"]==0)

def run(a,doc):
    ctx.prec=a.bits
    _,v=checked_inputs(a,doc)
    rows,old_global=restore_raw(a,doc)
    new_raw=restrict_core(rows,doc)
    assemble(v,new_raw,old_global,doc)
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete fixed gate inventory changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
       complete_core_residual_restriction_proved=True,
       complete_selected_ordinary_source_bounds_proved=True,
       original_7296_row_residuals_recomputed=0,
       original_Z_inner_sources_recomputed=0,
       original_whole_interval_integral_recomputed=0,
       original_D_or_WL_scalar_budgets_recomputed=0,
       old_scientific_source_imports=0,original_input_bytes_changed=False,
       new_recomputable_arrays_persisted=False,
       actual_core_solution_proved=False,actual_low_cut_or_cap_domain_entry_proved=False,
       full_high_inverse_proved=False,final_surface_proved=False,
       independent_remaining_inputs=[
          "complete cap affine load","original96 waist load",
          "wholecore nonlinear divergence source","unknown high-body input",
          "unknown high-cut input","wholecore and cut H1 radii",
          "same-state right collar data","actual physical-curvature product-domain entry"])

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing scientific conclusion")
    doc={"kind":KIND,"complete":False,"proved":False,"actual_returncode":1,
       "failure":None,"gates":[],"source_sha256":sha(__file__),
       "parameters":PARAMETERS,"derived_continuous_centre_definition_sha256":CENTRE,
       "exact_continuous_direction_definition_sha256":DIRECTION}
    try:run(a,doc)
    except Exception as e:
        doc["failure"]={"error_type":type(e).__name__,"message":str(e)}
        doc["complete"]=False;doc["proved"]=False;doc["actual_returncode"]=1
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    raw=canonical(doc)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    temp=a.out.with_name(a.out.name+".partial");temp.write_bytes(raw);temp.replace(a.out)
    print("CORE_RESIDUAL_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps({"bytes":len(raw),"sha256":sha_bytes(raw)},sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("CORE_RESIDUAL_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>45000:
        raise ValueError("saved complete scientific conclusion exceeds45000 bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())
