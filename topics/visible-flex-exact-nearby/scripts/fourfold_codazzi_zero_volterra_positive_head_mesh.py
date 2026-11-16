"""WHV: three new complete maxima and zero-Volterra mesh bounds."""
from __future__ import annotations
import argparse, copy, os, re, sys
from fractions import Fraction
from pathlib import Path
from fourfold_codazzi_zero_volterra_positive_head_readonly import (
 admit, canonical, digest, require, PARAMETERS, PROBLEM_ID)

KIND="complete_zero_volterra_positive_head_mesh_v1"
MAXIMA={"H_b":"low_to_high_source","L_b":"high_to_low_raw","G_b":"head_generator"}
BASE_RECORDS=("pi Lambda0 A_c_weight A_b_weight A_c A_b_from_H A_b_from_L "
 "C_P L_star A_infty C_K ell_upper C_V0 C_D0 C_R0 C_T0 mesh_numerator epsilon").split()
RETAINED={"same_selected_positive_member":True,"ordinary_dr_fixed_raw_fiber":True,
 "all193_states_physical_mean_and_original_affine_ports_retained":True,
 "cokernel_requires_inverse_adjoint_left_factor":True,
 "endpoint_is_bounded_integral_row_not_trace_on_L2":True,
 "original_chart_b_not_identified_with_raw_endpoint":True,
 "full_L2_input_in_all_finite_dual_rows":True,"unknown_mH_retained":True,
 "physical96_and_Theta_and_nu_and_all_cross_rows_retained":True,
 "negative_radial_head_eliminated":False,"finite_matrix_allocated":False,
 "finite_signed_inverse_proved":False,"practical_finite_inverse_claimed":False}

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 for key in ("repo","manifest","manifest-sha","out","native","native-receipts"):
  parser.add_argument("--"+key,required=True)
 parser.add_argument("--bits",type=int,required=True)
 parser.add_argument("--preflight-only",action="store_true")
 args=parser.parse_args()
 require(args.bits==320,"320-bit contract")
 work=admit(args.repo,args.manifest,args.manifest_sha,args.native,args.native_receipts)
 if args.preflight_only:
  print(canonical({"kind":"complete_WH_V_readonly_preflight","complete":True,
                   "admission":work["admission"]}).decode(),end="",flush=True)
  return
 out=Path(args.out)
 require(not out.exists(),"completed or partial target already exists")
 checkout=os.environ.get("ACTUAL_CHECKOUT_COMMIT","")
 require(re.fullmatch("[0-9a-f]{40}",checkout),"actual checkout identity")
 manifest=work["manifest"]
 doc={"kind":KIND,"complete":False,"failure":None,"stage":"readonly_admission",
  "problem_id":PROBLEM_ID,"parameters":PARAMETERS,
  "actual_checkout_commit":checkout,"manifest_sha256":args.manifest_sha,
  "scientific_modules":work["scientific_modules"],
  "original_input_sha256":{x["role"]:x["sha256"] for x in manifest["core_current_files"]},
  "inventory_sha256":manifest["inventory"]["sha256"],
  "mathematical_contract_sha256":manifest["mathematical_contract"]["sha256"],
  "original_admission":work["admission"],
  "copied_original_records":copy.deepcopy(work["literals"]),
  "copied_original_scope":copy.deepcopy(work["old_scope"]),
  "maxima":{},"new_records":{},"complete_body_source_choice":None,
  "required_N_diagnostic":None,"strict_mesh_gate":None,"resolvent_admitted":False,
  "current_target":None,"completed_targets":[],
  "actual_progress":{"old_targets_recomputed":0,"new_maxima_completed":0,
   "new_scalar_records_completed":0,"new_required_N_diagnostics_completed":0,
   "new_strict_comparisons_completed":0,"matrix_allocations":0},
  "gates":copy.deepcopy(work["admission"]["checks"]),"retained_scope":RETAINED}
 out.parent.mkdir(parents=True,exist_ok=True)
 def publish():
  raw=canonical(doc)
  try:
   tmp=out.with_name(out.name+".tmp")
   with open(tmp,"wb") as handle:
    handle.write(raw);handle.flush();os.fsync(handle.fileno())
   os.replace(tmp,out)
  finally:
   sys.stdout.write(raw.decode("utf-8"));sys.stdout.flush()
  require(len(raw)<=16000,"complete scientific JSON exceeds frozen byte limit")
 def start(name):
  require(name not in doc["completed_targets"],"new target would repeat")
  doc["current_target"]=name;doc["stage"]="started:"+name;publish()
 def finish(name):
  doc["completed_targets"].append(name)
  doc["current_target"]=None;doc["stage"]="saved:"+name;publish()
 publish()
 try:
  import flint
  from flint import arb,ctx
  require(sys.version_info[:3]==(3,12,14) and flint.__version__=="0.9.0",
          "directed runtime")
  ctx.prec=320
  doc["runtime"]={"python":"3.12.14","python_flint":"0.9.0","bits":320}
  def upper(value):
   require(value.is_finite(),"nonfinite new bound")
   require(value.lower()>=0,"negative norm upper")
   return value.upper()
  def old(record):
   return upper(arb(record["upper"]))
  def read(name):
   return upper(arb(doc["new_records"][name]["ball"]))
  def exact(value):
   f=Fraction(value);return arb(f.numerator)/arb(f.denominator)
  def scalar(name,function,interval=False):
   start(name)
   value=function()
   require(value.is_finite(),"nonfinite scalar "+name)
   if not interval:value=upper(value)
   doc["new_records"][name]={"ball":value.str(75)}
   doc["actual_progress"]["new_scalar_records_completed"]+=1
   finish(name)
   return arb(doc["new_records"][name]["ball"]) if interval else read(name)
  def gate(name):
   doc["gates"].append({"name":name,"passed":True})
  for name,field in MAXIMA.items():
   start(name);winner=None;best=None
   for row in work["rows"]:
    value=old(row["bounds"][field])
    if best is None or value>best:
     best=value;winner=row
   require(winner is not None,"empty complete maximum")
   doc["maxima"][name]={"saved_field":field,"rows_compared":4650,
    "winning_original_row":winner["original_row"],
    "winning_interval":copy.deepcopy(winner["interval"]),
    "complete_original_record":copy.deepcopy(winner["bounds"][field]),
    "winning_complete_row_sha256":digest(canonical(winner)),
    "tie_break":"first original row"}
   doc["actual_progress"]["new_maxima_completed"]+=1
   gate("complete_saved_row_maximum_"+name);finish(name)
  maxima={name:old(item["complete_original_record"])
          for name,item in doc["maxima"].items()}
  copied=doc["copied_original_records"]
  pi=scalar("pi",lambda:arb.pi(),True)
  lam=scalar("Lambda0",lambda:arb(1+388*388).sqrt(),True)
  require(pi.lower()>0 and lam.lower()>0,"positive exact geometric constants")
  scalar("A_c_weight",lambda:lam**(arb(-2)/3))
  scalar("A_b_weight",lambda:1/lam)
  scalar("A_c",lambda:read("A_c_weight")*exact(copied["A_c_raw"]))
  scalar("A_b_from_H",lambda:read("A_b_weight")*maxima["H_b"])
  scalar("A_b_from_L",lambda:read("A_c_weight")*maxima["L_b"])
  start("complete_body_source_choice")
  selected="A_b_from_H" if read("A_b_from_H")<=read("A_b_from_L") else "A_b_from_L"
  doc["complete_body_source_choice"]={"selected":selected,
   "complete_record":copy.deepcopy(doc["new_records"][selected]),
   "candidates":["A_b_from_H","A_b_from_L"],"tie_break":"first candidate"}
  finish("complete_body_source_choice")
  ab=upper(arb(doc["complete_body_source_choice"]["complete_record"]["ball"]))
  scalar("C_P",lambda:((old(copied["C_c"])*read("A_c"))**2+
                       (old(copied["C_b"])*ab)**2).sqrt())
  scalar("L_star",lambda:max(exact(copied["L_c_raw"]),maxima["L_b"]))
  scalar("A_infty",lambda:max(exact(copied["G_c"]),maxima["G_b"]))
  scalar("C_K",lambda:old(copied["shell_1153"])*read("L_star")*read("C_P"))
  gate("complete_typed_source_candidates_and_coupling")
  scalar("ell_upper",lambda:exact(copied["R"])-exact(copied["rstar_interval"][0]))
  scalar("C_V0",lambda:2*read("ell_upper")/pi.lower())
  scalar("C_D0",lambda:arb(1))
  scalar("C_R0",lambda:read("ell_upper").sqrt())
  scalar("C_T0",lambda:read("C_V0")*(read("A_infty")+read("C_K")))
  scalar("mesh_numerator",lambda:read("ell_upper")/pi.lower()*
                                (read("A_infty")+read("C_K")))
  scalar("epsilon",lambda:read("mesh_numerator")/arb(PARAMETERS["radial_mesh_N"]))
  gate("complete_zero_Volterra_and_predeclared_mesh")
  start("required_N_diagnostic")
  bound=read("mesh_numerator")
  if bound<arb(10**256-1):
   required=int(bound.floor().fmpz())+1
   diagnostic={"required_N_decimal":str(required),"exceeds_256_digits":False,
    "within_declared_cap":required<=PARAMETERS["resource_cap_N"]}
  else:
   diagnostic={"required_N_decimal":None,"exceeds_256_digits":True,
               "within_declared_cap":False}
  diagnostic.update({"formula":"floor(saved numerator upper)+1",
    "tested_N":4096,"resource_cap_N":4096,"tested_output_dimension":193*4096,
    "diagnostic_is_not_a_finite_inverse":True})
  doc["required_N_diagnostic"]=diagnostic
  doc["actual_progress"]["new_required_N_diagnostics_completed"]=1
  finish("required_N_diagnostic")
  start("strict_mesh_comparison")
  passed=bool(read("epsilon")<1)
  doc["strict_mesh_gate"]={"passed":passed,"comparison":"saved epsilon upper < 1",
   "epsilon_record":copy.deepcopy(doc["new_records"]["epsilon"])}
  doc["actual_progress"]["new_strict_comparisons_completed"]=1
  finish("strict_mesh_comparison")
  if passed:
   scalar("resolvent",lambda:1/(arb(1)-read("epsilon")).lower())
   doc["resolvent_admitted"]=True
  require(("resolvent" in doc["new_records"])==passed,"conditional resolvent")
  gate("retained_comparison_and_only_conditional_resolvent")
  require(set(doc["new_records"])==set(BASE_RECORDS)|({"resolvent"} if passed else set())
          and doc["actual_progress"]["new_maxima_completed"]==3
          and len(doc["gates"])==13,"complete scalar graph")
  gate("complete_scientific_schema")
  doc["complete"]=True;doc["stage"]="complete";publish()
 except BaseException as error:
  doc["complete"]=False
  message=str(error).encode("utf-8","replace")[:1000].decode("utf-8","ignore")
  doc["failure"]={"type":type(error).__name__,"message":message}
  doc["stage"]="failed:"+str(doc["current_target"] or doc["stage"])
  publish()
  raise

if __name__=="__main__":main()
