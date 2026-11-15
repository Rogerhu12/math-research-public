#!/usr/bin/env python3
"""New complete free-Airy first-omitted cut scalars; all old mathematics is read only."""
from __future__ import annotations
import argparse, copy, gzip, hashlib, importlib.metadata, json, math, os, platform, time, traceback
from fractions import Fraction as Q
from pathlib import Path
from flint import arb, ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
SOURCE=REL+"scripts/fourfold_codazzi_free_Airy_first_omitted_cut_scalars.py"
KIND="actual_complete_free_Airy_first_omitted_cut_scalars_v1"
MANIFEST_KIND="complete_free_Airy_first_omitted_cut_scalar_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0","arithmetic_bits":320}
OLD_RUNTIME={"python":"3.12.14","python_flint":"0.9.0","numpy":"2.3.5","scipy":"1.17.0"}
GATE_COUNT=24
PINNED={
 "old_fold_majorants_stage": "29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144",
 "adjacent_process": "9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b",
 "adjacent_publication": "0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c",
 "whole_native": "6668c9b2c8f1632e3bd8af392a803335f076c64e1d7fb74dfc9e1605f0e1ee2d",
 "whole_process": "242d82b6f1ead216bf8e90679a9952a2aaad0e9d7ba29293739911e70ab4d145",
 "whole_publication": "fc3a190d8b701ef84188f2a37ee846c4f3669b5ac409faa5a6b72850162d1099",
 "original_fold_algorithm": "410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783",
 "original_whole_algorithm": "66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81",
 "original_whole_manifest": "d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac",
 "free_radius_stage": "8b31b1c0030f892ec763d32ecf7b4968d468c5f93b30bbfe7408d6bf0b4892d5",
 "new_contract": "24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af",
 "primitive_contract": "38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e",
 "ordered_contract": "66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00",
 "original_Taylor_algorithm": "42048094f7c5e0ba3b83f10e9e6fcbc5cd4c5b3d67057f69241409a5a4be87a1",
 "original_IN_algorithm": "726bdd98802c88e9c162f598ff983bc8a762d8cc8f8216164c56e6b960119874",
 "RR_execution": "a75da290077cf0e134834be5e35a0fa7cd55cd79104f5128d87eaee898af162b",
 "TN_execution": "7abb04effcb8009dafaeec65cf3474e5d045b92c555bb92118544cd47256ee3d",
 "TC_execution": "37c2a5ae3b77e7f0895aa0c3130d8707868816f1d26a119a880272f9b92f902e",
 "ST_execution": "b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637"
}
ACCEPTED={
 "RR_execution": {
  "run_id": "43750683671",
  "source": "2a51b8c45974808e65754ebaa0b476650596e7d8a1e36541e9afd3987146c4c9",
  "manifest": "8822511f1f1c853efd8eec4944bcb74b6954c7fa04c143d9dafc9b470bdd1b4a",
  "gates": 28
 },
 "TN_execution": {
  "run_id": "43752771157",
  "source": "4dbc776babf0e8be12440bb21ac0765e2676c9cea02912326d46f53cfb627256",
  "manifest": "9e5688400b91714b189e2ed3865cf5448b54bf26d0ff8fef76ba3af06161646e",
  "gates": 16
 },
 "TC_execution": {
  "run_id": "43754703603",
  "source": "e05b4a9cbe5d66e03a1fb22b70c75ee48cdc885d1bd83c523d9a0173b92b0d71",
  "manifest": "0e78cfa73d9d2ce8d53fc8eb1c0bdffef276739360aa66f55f13ea13f5ab3c45",
  "gates": 18
 },
 "ST_execution": {
  "run_id": "43757644616",
  "source": "743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5",
  "manifest": "e43b2c7036088cd8d1401c580c1aa6ef694d283057dcce7c65839f92fc1b0e80",
  "gates": 25
 }
}
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
CUT=Q(76285779072683,320000000000000)
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
RG=Q(3,8000);SG=Q(3,128);CW=Q(1,32)
R0=Q(1,6000);SIGMA0=Q(1,128);SAVED_H=Q(9,1000000)
SAVED_WIDTH=Q(1,512);WIDTH=Q(1,1024);J_C=97;N=4*J_C;JET=6
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
WHOLE_TAYLOR="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
WHOLE_NRAW="fbe1bce690f33335d2b024fe38a751743e0017e7d275b4d1fb0712be155f177e"
PARAMETERS={
 "arithmetic_bits":320,"runtime":RUNTIME,"exact_strict_cut":str(CUT),
 "exact_root_interval":list(map(str,ROOTS)),"fixed_intrinsic_parameter":"eta_0",
 "exact_real_delta_radius":"1/100000000","physical_root_piece":2549,
 "exact_fold_radius":str(RG),"exact_fold_strip":str(SG),"exact_coefficient_strip":str(CW),
 "exact_saved_free_radius":str(SAVED_H),"exact_saved_free_width":str(SAVED_WIDTH),
 "exact_new_amplitude_width":str(WIDTH),"maximum_explicit_angular_derivative":JET,
 "input_cutoff_abs_j":J_C,"physical_frequency":"n=4|j|","physical_signs":[-1,1],
 "oscillatory_branches":[-1,1],"reference_column":"same terminal Ai free P8 first column",
 "radial_density_convention":"R_c=n_g(r_c)*T(q(r_c)); no extra reaction gauge",
 "old_original_primitive_L2_norm":"1/4","old_complete_J_L2_upper":"0.825332620",
 "old_contour_T_upper":"19/1000000","new_mean_exponent_lower":"1/2048",
 "Ai_initial_modulus_upper":"1","Airy_error_domain":"all real t>0 and n>0",
 "Airy_error_derivatives_taken":False,"original_saved_norms_recomputed":False,
 "normalizer_cutoff_is_separate_from_input_cutoff":True,
 "finite_S_L_is_paid_as_a_complete_strong_norm":True,
 "complete_physical_means_and_intermediate_projection_ranks_retained":True,
 "expected_structural_gates":GATE_COUNT}

def canonical(x):
    return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha(p):return sha_bytes(Path(p).read_bytes())
def read(p):
    p=Path(p);s=p.read_bytes()
    return json.loads(gzip.decompress(s) if p.suffix==".gz" else s)
def save(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(canonical(x));tmp.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def ball(x):
    if isinstance(x,arb):return x
    if isinstance(x,(int,Q)):return ex(x)
    if isinstance(x,dict):return arb(x["ball"])
    return arb(x)
def upper(x):
    x=ball(x)
    if not x.is_finite():raise ArithmeticError("nonfinite new complete positive scalar")
    y=x.upper()
    if y<0:raise ArithmeticError("negative new complete positive scalar")
    return y
def oldupper(x,label="old complete upper"):
    x=ball(x)
    if not x.is_finite() or x.lower()<0:raise ValueError("invalid "+label)
    return x.upper()
def positive_lower(x,label):
    x=ball(x).lower()
    if not x.is_finite() or not x>0:raise ValueError("missing positive "+label)
    return x
def rec(x):
    x=ball(x)
    if not x.is_finite():raise ArithmeticError("nonfinite scalar cannot be recorded")
    return {"ball":x.str(48)}
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def decode(x):
    if isinstance(x,dict):
        if set(x)=={"ball"}:return arb(x["ball"])
        return {k:decode(v) for k,v in x.items()}
    if isinstance(x,list):return [decode(v) for v in x]
    return x
def psha(x):return sha_bytes(json.dumps(x,sort_keys=True,separators=(",",":"),allow_nan=False).encode())
def power(x,p):
    x=ball(x);p=Q(p)
    if not x.is_finite() or not x.lower()>0:raise ValueError("nonpositive real power base")
    return upper((x.log()*ex(p)).exp())
def sqrt_upper(x):return upper(upper(x).sqrt())
def high(*xs):return max(upper(x) for x in xs)
def low_upper(*xs):return min(upper(x) for x in xs)
def finite_tree(x):
    if isinstance(x,arb):return x.is_finite() and x.upper()>=0
    if isinstance(x,dict):return all(finite_tree(v) for v in x.values())
    if isinstance(x,(list,tuple)):return all(finite_tree(v) for v in x)
    return True
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("free Airy cut gate failed: "+name)
def add(*xs):
    m=min(map(len,xs))
    return [upper(sum((x[k] for x in xs),arb(0))) for k in range(m)]
def scale(x,a):return [upper(v*ball(a)) for v in x]
def mul(x,y):
    return [upper(sum((math.comb(k,j)*x[j]*y[k-j] for j in range(k+1)),arb(0)))
            for k in range(min(len(x),len(y)))]
def product(*xs):
    z=[arb(1)]+[arb(0)]*(min(map(len,xs))-1)
    for x in xs:z=mul(z,x)
    return z
def diff(x):
    if len(x)<2:raise ValueError("insufficient complete angular derivative")
    return x[1:]
def cauchy(saved,width,n=JET):
    """Only new derivative losses; each saved value is already a complete old bound."""
    width=Q(width)
    if width<=0:raise ValueError("no genuine complex strip margin")
    saved=[oldupper(x) for x in saved]
    return [low_upper(*(saved[k]*math.factorial(q-k)/ex(width**(q-k))
                         for k in range(min(q,len(saved)-1)+1))) for q in range(n+1)]
def Ijet(x,Hinv,order):
    out=mul(Hinv,x)
    for _ in range(order):out=mul(Hinv,diff(out))
    return out
def poly_norm(coeffs,start=0):
    return upper(sum((ex(Q(1,N**(k-start)))*a[0] for k,a in enumerate(coeffs) if k>=start),arb(0)))
def h2_component_sum_bound(a):
    # a[q] already bounds the SUM of scalar component L2 norms. Triangle in R^3
    # bounds their H2 sum by a0+sqrt(2)*a1+a2, with no Euclidean-vector substitution.
    if len(a)<3:raise ValueError("complete component H2 derivatives absent")
    return upper(a[0]+arb(2).sqrt()*a[1]+a[2])
def w43(a):return upper(3*h2_component_sum_bound(a))

def accepted_receipt(role,path,doc):
    identity=ACCEPTED[role];e=read(path);r=e.get("actual_scientific_receipt",{})
    gate(doc,"read successful complete "+role+" with its exact source manifest runtime and all gates",
        str(e.get("run_id"))==identity["run_id"] and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==identity["source"]
        and e.get("input_manifest_sha256")==identity["manifest"]
        and r.get("complete") is True and r.get("proved") is True and r.get("failure") is None
        and r.get("actual_returncode")==0 and r.get("runtime")==OLD_RUNTIME
        and r.get("source_sha256")==identity["source"] and r.get("input_manifest_sha256")==identity["manifest"]
        and len(r.get("gates",[]))==identity["gates"] and all(g.get("passed") is True for g in r["gates"]))
    return r

def checked_inputs(args,doc):
    actual={"Python":platform.python_version(),"python_flint":importlib.metadata.version("python-flint"),"arithmetic_bits":ctx.prec}
    gate(doc,"the public repository exact Python flint and320-bit runtime are actual",
         os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==PUBLIC and actual==RUNTIME)
    doc["runtime"]=actual;m=read(args.manifest);root=args.repo_root
    paths={k:root/m["input_paths"][k] for k in PINNED}
    files=m["files"];filemap={v["path"]:v for v in files}
    gate(doc,"all current texts and exact temporary historical originals match the frozen complete manifest",
         m.get("kind")==MANIFEST_KIND and m.get("public_repository")==PUBLIC
         and m.get("mathematical_input_sha256")==PINNED and m.get("parameters")==PARAMETERS
         and m.get("source_sha256")==sha(__file__) and m.get("runtime")==RUNTIME
         and len(files)==len(filemap)==len(PINNED)+1
         and set(filemap)=={m["input_paths"][k] for k in (*PINNED,"new_source")}
         and m["input_paths"]["new_source"]==SOURCE and m.get("legacy_artifact_inputs")==[]
         and all(sha(paths[k])==v for k,v in PINNED.items())
         and all((root/v["path"]).stat().st_size==v["bytes"] and sha(root/v["path"])==v["sha256"] for v in files))
    doc["input_sha256"]={"manifest":sha(args.manifest),**PINNED}
    FA=paths["new_contract"].read_text();I=paths["primitive_contract"].read_text()
    O=paths["ordered_contract"].read_text();orig=paths["original_whole_algorithm"].read_text()
    gate(doc,"the full old primitive J ordered coefficient and global real-Airy remainder identities are fixed",
         all(s in FA for s in ("FA.6","FA.13","FA.16","FA.34a","0.002921264998045","1/2048","component"))
         and all(s in I for s in ("I.8","I.13","I.15","0.825332620","\\|I_\\rho\\|"))
         and all(s in O for s in ("\\tag{O.2}","\\ell=-2buv",
                 "N_B&=-2bK P M_{v_\\phi}I M_vP","A&=\\eta\\partial+L","B&=PM_{b_0}P+N_B"))
         and "def radius_budget(" in orig
         and "old_first_correction_or_numerator_coefficients_recomputed=False" in orig)
    receipts={k:accepted_receipt(k,paths[k],doc) for k in ACCEPTED}
    rr,tn,tc=(receipts[k] for k in ("RR_execution","TN_execution","TC_execution"))
    coeff=rr["complete_physical_cut_coefficient_conclusion"][0]
    tcgeom=tc["complete_density_coordinate_conclusion"];domain=tcgeom["accepted_phase_domain_read_verbatim"]
    tnc=tn["complete_selected_normalizer_conclusion"];tnr=tn["complete_strong_remainder_conclusion"]
    gate(doc,"all three saved receivers use the identical P22 root family and full original means",
         tc["mathematical_parameters"]["exact_strict_cut"]==str(CUT)
         and tc["mathematical_parameters"]["exact_real_delta_radius"]=="1/100000000"
         and tc["mathematical_parameters"]["exact_root_interval"]==list(map(str,ROOTS))
         and tc["mathematical_parameters"]["fixed_intrinsic_parameter"]=="eta_0"
         and domain["exact_strict_cut"]==str(CUT)
         and list(map(Q,domain["exact_rho_interval"]))==[ROOTS[0]-CUT,ROOTS[1]-CUT]
         and coeff["root_mean_value_q_bounds"]["exact_root_distance"]==domain["exact_rho_interval"]
         and coeff["both_mean_coordinates_retained"] and domain["all_complete_physical_means_and_both_reference_columns_retained"]
         and tcgeom["real_fourfold_degree_one_maps"] and tcgeom["independent_physical_mean_block_is_identity"]
         and domain["no_real_angle_jet_promoted_to_complex_strip"])
    windows=tnc["complete_selected_cutoff_window_verdicts"]
    gate(doc,"read U_Phi and its inverse distinctly and retain both successful TN windows and the full finite difference",
         all(windows[k]["both_strict_tests_passed"] for k in ("L2","Hminus4_3"))
         and tnc["selected_cutoff_in_original_moving_circle"]
         and tnc["same_inverse_on_common_trigonometric_domain"]
         and tnc["all_HL_LH_blocks_and_both_independent_means_retained"]
         and tnc["finite_modes_97_through_J_minus_1_retained"]
         and tnc["first_bandwidth"]==192 and tnc["second_bandwidth"]==384
         and "complete_density_Hminus4_3_upper" in tcgeom
         and "complete_inverse_density_Hminus4_3_upper" in tcgeom
         and "complete_ordered_inverse_strong_remainder_upper" in tnr
         and "complete_uncompressed_first_symbol_finite_difference_upper" in tnr)
    doc["complete_saved_receiver_identity"]={
        k:{"run_id":ACCEPTED[k]["run_id"],"source_sha256":ACCEPTED[k]["source"],
           "manifest_sha256":ACCEPTED[k]["manifest"],"science_payload_sha256":psha(v)}
        for k,v in receipts.items()}
    doc["complete_saved_cut_receiver_conclusion"]={
        "RR_ng_q_and_means_read_verbatim":copy.deepcopy(coeff),
        "TC_U_Phi_Hminus4_3_read_verbatim":copy.deepcopy(tcgeom["complete_density_Hminus4_3_upper"]),
        "TC_inverse_U_Phi_Hminus4_3_separate_not_used":copy.deepcopy(tcgeom["complete_inverse_density_Hminus4_3_upper"]),
        "TN_ordered_L2_inverse_read_verbatim":copy.deepcopy(windows["L2"]["ordered_inverse_upper"]),
        "TN_ordered_L2_forward_read_verbatim":copy.deepcopy(windows["L2"]["complete_forward_upper"]),
        "TN_S_read_verbatim":copy.deepcopy(tnc["complete_S_upper"]),
        "TN_S_phi_read_verbatim":copy.deepcopy(tn["complete_normalizer_coefficient_conclusion"][0]["complete_coefficients"]["complete_S_phi_upper"]),
        "TN_strong_RN_read_verbatim":copy.deepcopy(tnr["complete_ordered_inverse_strong_remainder_upper"]),
        "TN_strong_finite_FS_read_verbatim":copy.deepcopy(tnr["complete_uncompressed_first_symbol_finite_difference_upper"]),
        "TN_exact_moving_cutoff_abs_j":tnc["exact_cutoff_abs_j"],
        "TN_full_finite_support_through":tnc["exact_cutoff_abs_j"]+191,
        "input_cutoff_abs_j":J_C,"same_cut_does_not_mean_same_cutoff":True}
    return m,paths,receipts

def original_fold(paths,doc):
    ms=read(paths["old_fold_majorants_stage"]);pr=read(paths["adjacent_process"]);pub=read(paths["adjacent_publication"])
    entries=[v for v in pub["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
    gate(doc,"the original4501-byte complete fold and full coefficient domain are consumed without a producer call",
         len(entries)==1 and entries[0]["bytes"]==4501 and entries[0]["sha256"]==PINNED["old_fold_majorants_stage"]
         and ms["complete"] and ms["stage"]==ms["name"]=="complete-original-reference-holomorphic-majorants"
         and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
         and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==OLD_RUNTIME
         and pr["actual_returncode"]==0 and pr["mathematical_complete"] and pr["mathematical_proved"]
         and pr["mathematical_failure"] is None and pub["complete"]
         and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi")))
    x=decode(ms["payload"])
    doc["original_complete_fold_payload_sha256"]=psha(ms["payload"])
    return x["fold"],x["coefficients"]

def original_free_radius(paths,doc):
    native=read(paths["whole_native"]);pr=read(paths["whole_process"]);pub=read(paths["whole_publication"])
    gate(doc,"the old whole-piece child and all ten mathematical gates succeeded before its preserved formatter failure",
        pr["actual_returncode"]==0 and pr["mathematical_complete"] and pr["mathematical_proved"]
        and pr["mathematical_failure"] is None and pr["mathematical_source_sha256"]==PINNED["original_whole_algorithm"]
        and pr["manifest_sha256"]==PINNED["original_whole_manifest"] and pr["native_sha256"]==PINNED["whole_native"]
        and pr["failure"]=={"type":"TypeError","message":"dict() got multiple values for keyword argument 'complete'"}
        and native["complete"] and native["proved"] and native["failure"] is None
        and native["source_sha256"]==PINNED["original_whole_algorithm"]
        and native["input_manifest_sha256"]==PINNED["original_whole_manifest"]
        and native["runtime"]==OLD_RUNTIME and native["gates"]==pr["mathematical_gates"]
        and len(native["gates"])==10 and all(v["passed"] for v in native["gates"])
        and pub["complete"] is False and pub["actual_returncode"]==1)
    gate(doc,"the saved free correction has the same complete193 direction fixed eta piece and full parameter disk",
         native["fixed_intrinsic_parameter"]=="eta_0"
         and Q(native["exact_complex_coefficient_delta_radius"])==Q(1,10**8)
         and native["exact_root_interval"]==list(map(str,ROOTS))
         and native["exact_original_physical_piece_interval"]==list(map(str,PIECE))
         and Q(native["exact_holomorphic_rho_radius"])==R0
         and Q(native["exact_holomorphic_phi_width"])==SIGMA0
         and native["original_Taylor_native_sha256"]==WHOLE_TAYLOR
         and native["original_Nraw_native_sha256"]==WHOLE_NRAW
         and native["original_targets_FFT_intrinsic_cubics_folds_signed_coefficients_and_saved_norms_recomputed"]==0)
    name="complete-radius-budget-9-1000000";entry=native["stages"][name]
    pe=[v for v in pub["files"] if v["file"]=="consumers/"+entry["file"]]
    stage=read(paths["free_radius_stage"])
    gate(doc,"one complete old h9e-6 radius stage has its original native process publication and exact bytes",
         len(pe)==1 and pe[0]["bytes"]==entry["bytes"]==paths["free_radius_stage"].stat().st_size==20924
         and pe[0]["sha256"]==entry["sha256"]==PINNED["free_radius_stage"]
         and stage["complete"] and stage["stage"]==name and stage["stage_kind"]=="radius_budget_stages"
         and stage["source_sha256"]==PINNED["original_whole_algorithm"]
         and stage["input_manifest_sha256"]==PINNED["original_whole_manifest"]
         and stage["runtime"]==OLD_RUNTIME and stage["original_Taylor_native_sha256"]==WHOLE_TAYLOR
         and stage["original_Nraw_native_sha256"]==WHOLE_NRAW)
    b=stage["payload"];rows=[v for v in b["budgets"] if Q(v["exact_output_phi_width"])==SAVED_WIDTH]
    gate(doc,"the old full p0-p2 q0-q3 holomorphic budgets are read at width1/512 on a strict radial superset",
         b["complete"] and Q(b["exact_physical_rho_cover"])==SAVED_H
         and Q(b["exact_holomorphic_rho_radius"])==R0 and Q(b["exact_holomorphic_phi_width"])==SIGMA0
         and len(rows)==1 and 0<ROOTS[0]-CUT<ROOTS[1]-CUT<SAVED_H<R0
         and rows[0]["all_saved_finite_norms_and_complete_angular_factors_reused"]
         and rows[0]["old_first_correction_or_numerator_coefficients_recomputed"] is False
         and all(str(p)+","+str(q) in rows[0]["first_amplitude_budgets"][a]["strip_sup"]
                 for a in ("a1","b1") for p in range(3) for q in range(4)))
    saved={a:{str(p):[copy.deepcopy(rows[0]["first_amplitude_budgets"][a]["strip_sup"][str(p)+","+str(q)])
                     for q in range(4)] for p in (0,1)} for a in ("a1","b1")}
    doc["complete_saved_free_amplitude_conclusion"]={
        "original_run":"43669106351/1","native_sha256":PINNED["whole_native"],
        "radius_stage_sha256":PINNED["free_radius_stage"],"radius_payload_sha256":psha(b),
        "physical_rho_superset":str(SAVED_H),"physical_output_strip":str(SAVED_WIDTH),
        "p0_and_p1_q0_through_q3_read_verbatim":saved,
        "radial_r_and_rho_derivatives_have_equal_absolute_bounds":True,
        "free_w1_is_not_genuine_w1V":True,"old_coefficient_sum_tail_or_norm_calls":0}
    return {p:[[oldupper(v) for v in saved[a][str(p)]] for a in ("a1","b1")] for p in (0,1)}

def new_domain_and_jets(f,c,saved,receipts,doc):
    """New restriction and Cauchy products at P22, not a rerun of any old fold budget."""
    rho_lo,rho_hi=ROOTS[0]-CUT,ROOTS[1]-CUT
    tc=receipts["TC_execution"]["complete_density_coordinate_conclusion"]
    pd=tc["accepted_phase_domain_read_verbatim"]
    rr=receipts["RR_execution"]["complete_physical_cut_coefficient_conclusion"][0]
    tlo=positive_lower(pd["complete_T_modulus_lower"],"same cut real negative T")
    thi=oldupper(pd["complete_T_modulus_upper"])
    # The frozen IN producer defines tplus=rho_plus*Ap^(2/3) from the original
    # full RG x SG fold bound; only its phase derivatives were real-circle bounds.
    tau=ex(rho_hi/RG);xm=upper(tau*oldupper(f["j"]))
    yh=upper(tau*tau*oldupper(f["BT"]));xh=upper(1+xm)
    dh=(1-upper(2*xm+xm*xm+thi*yh*yh)).lower()
    em=positive_lower(c["em"],"original full complex eta lower")
    gate(doc,"the new point inverse and complete old-strip domains are positive at the identical strict cut",
         0<rho_lo<rho_hi<Q(4,1000000) and rho_hi<SAVED_H<RG
         and 0<WIDTH<SAVED_WIDTH<SG<CW and dh>0 and tlo>0 and thi>0
         and pd["actual_fixed_cut_all_tau_segments"] and pd["inner_profiles_use_outer_A_at_effective_tau_rho"])
    hinv0=upper((2*xh+(1+thi)*yh)/dh)
    qfold=oldupper(f["Q"])
    m0=upper(qfold*(2*thi*yh+xh*(1+thi)))
    Hinv=cauchy([hinv0],SG-WIDTH);MM=cauchy([m0],SG-WIDTH)
    a0full=oldupper(f["M"]);b0full=upper(2*oldupper(f["G"])*oldupper(f["E"])*oldupper(f["BT"]))
    # a0(0)=1; b0 has the exact second-order root zero. These are the fixed P8/I21 normalization.
    a0h=low_upper(a0full,1+tau*(a0full+1));b0h=upper(tau*tau*b0full)
    dr=ex(RG-rho_hi)
    a0r=upper(a0full/dr)
    b0r=upper(b0full/ex(RG*RG)*(2*ex(rho_hi)+ex(rho_hi*rho_hi)/dr))
    w0=add(cauchy([a0h],SG-WIDTH),cauchy([b0h],SG-WIDTH))
    w0r=add(cauchy([a0r],SG-WIDTH),cauchy([b0r],SG-WIDTH))
    w1=add(*(cauchy(v,SAVED_WIDTH-WIDTH) for v in saved[0]))
    w1r=add(*(cauchy(v,SAVED_WIDTH-WIDTH) for v in saved[1]))
    u=cauchy(c["U"][0],CW-WIDTH);v=cauchy(c["V"][0],CW-WIDTH)
    drift=cauchy(c["D"],CW-WIDTH);b=oldupper(c["beta"]);K=oldupper(c["K"])
    ell=scale(mul(u,v),2*b)
    one=[arb(1)]+[arb(0)]*JET
    bloc=scale(add(one,mul(u,u),scale(mul(v,v),3*K)),b)
    ell_old=cauchy([c["ell"]],CW-WIDTH);bloc_old=cauchy([c["b0"]],CW-WIDTH)
    ell=[low_upper(a,z) for a,z in zip(ell,ell_old)]
    bloc=[low_upper(a,z) for a,z in zip(bloc,bloc_old)]
    qlo=positive_lower(rr["root_mean_value_q_bounds"]["q_lower"],"complete real q lower")
    qhi=oldupper(rr["root_mean_value_q_bounds"]["q_upper"])
    ng=oldupper(rr["complete_ng_upper"])
    Rwave=upper(ng*arb(2).sqrt()*(1/qlo.sqrt()+qhi.sqrt()))
    data=dict(Hinv=Hinv,M=MM,w0=w0,w1=w1,w0r=w0r,w1r=w1r,u=u,v=v,
              drift=drift,ell=ell,bloc=bloc,b=b,K=K,eta_lower=em,
              eta_upper=oldupper(c["ep"]),Rwave=Rwave,tlo=tlo,thi=thi,yhol=yh,
              tphi= yh,tphiphi=upper(yh/ex(SG)),kappa_lower=positive_lower(tc["phase_derivative_lower"],"true phase derivative"),
              kappa=[oldupper(tc["phase_derivative_upper"]),oldupper(tc["phase_second_derivative_upper"]),
                     oldupper(pd["complete_new_three_phase_third_derivative_upper"])])
    gate(doc,"all initial complete component-sum jets and physical radial readout bounds are finite and correctly sized",
         finite_tree(data) and all(len(data[k])==JET+1 for k in ("Hinv","M","w0","w1","w0r","w1r","u","v","drift","ell","bloc")))
    doc["complete_new_cut_domain_conclusion"]=encode({
        "rho_lower":rho_lo,"rho_upper":rho_hi,"physical_holomorphic_strip":WIDTH,
        "original_fold_full_strip":SG,"old_free_budget_strip":SAVED_WIDTH,
        "point_determinant_lower":dh,"complete_H_inverse_holomorphic_entry_sum":hinv0,
        "complete_M_holomorphic_entry_sum":m0,"complete_x_deviation_holomorphic":xm,
        "complete_y_holomorphic":yh,"complete_negative_T_real_lower":tlo,
        "complete_T_holomorphic_upper_read_from_original_full_Ap":thi,
        "complete_eta_full_complex_lower":em,"complete_radial_wave_entry_sum":Rwave,
        "radial_wave_exact_convention":"n_g*T(q), ungauged Q6; no extra reaction factor",
        "complete_w0_component_root_restrictions":[a0h,b0h],
        "complete_w0_radial_component_bounds":[a0r,b0r],
        "highest_explicit_angular_order":JET,
        "real_TC_phase_jets_never_used_as_holomorphic_suprema":True})
    doc["complete_new_initial_angular_jet_conclusion"]=encode({
        k:data[k] for k in ("Hinv","M","w0","w1","w0r","w1r","u","v","drift","ell","bloc")})
    return data

def complete_finite_primitive_calculus(d,doc):
    H,M=d["Hinv"],d["M"];w0,w1=d["w0"],d["w1"]
    u,v=d["u"],d["v"];vp=diff(v);b,K=d["b"],d["K"]
    def IP(a,k=0):return Ijet(a,H,k)
    def AA(a):return add(scale(diff(a),d["eta_upper"]),mul(d["ell"],a))
    def DW(a,ar):return add(ar,mul(d["drift"],diff(a)),mul(d["bloc"],a))
    def inverse(a):return scale(mul(H,a),1/d["eta_lower"])
    g=[]
    g.append(inverse(mul(M,w0)))
    g.append(inverse(add(mul(M,w1),DW(w0,d["w0r"]),AA(g[0]))))
    g.append(inverse(add(DW(w1,d["w1r"]),scale(mul(vp,IP(mul(v,w0))),2*b*K),
                         AA(g[1]),scale(mul(vp,IP(mul(u,g[0]))),2*b))))
    g.append(inverse(add(scale(mul(vp,add(IP(mul(v,w1)),IP(mul(v,w0),1))),2*b*K),
                         AA(g[2]),scale(mul(vp,add(IP(mul(u,g[1])),IP(mul(u,g[0]),1))),2*b))))
    W=[w0,w1]
    Ug=[[IP(mul(u,a),l) for l in range(3)] for a in g]
    Vw=[[IP(mul(v,a),l) for l in range(3)] for a in W]
    # Exact FA13 cancellation, not subtraction of interval upper bounds:
    # degrees -1,0,1,2 are identically zero; only the displayed positive tails remain.
    rcoef={k:arb(0) for k in range(3,7)}
    rcoef[3]=AA(g[3])[0]
    for k,row in enumerate(Ug):
        for l,a in enumerate(row):
            degree=k+l+1
            if degree>=3:rcoef[degree]=upper(rcoef[degree]+2*b*vp[0]*a[0])
    for k,row in enumerate(Vw):
        for l,a in enumerate(row):
            degree=k+l+1
            if degree>=3:rcoef[degree]=upper(rcoef[degree]+2*b*K*vp[0]*a[0])
    r3=upper(sum((ex(Q(1,N**(k-3)))*rcoef[k] for k in rcoef),arb(0)))
    tail_u=upper(sum((ex(Q(1,N**k))*diff(row[2])[0] for k,row in enumerate(Ug)),arb(0)))
    tail_v=upper(sum((ex(Q(1,N**k))*diff(row[2])[0] for k,row in enumerate(Vw)),arb(0)))
    ugpoly=upper(sum((ex(Q(1,N**(k+l+1)))*a[0] for k,row in enumerate(Ug) for l,a in enumerate(row)),arb(0)))
    vwpoly=upper(sum((ex(Q(1,N**(k+l+1)))*a[0] for k,row in enumerate(Vw) for l,a in enumerate(row)),arb(0)))
    gn=poly_norm(g);wn=poly_norm(W)
    sixmeans=[
        upper(d["ell"][0]*gn),
        upper(2*b*vp[0]*ugpoly),
        upper(b*vp[0]*u[0]*gn/2),
        upper(d["bloc"][0]*wn),
        upper(2*b*K*vp[0]*vwpoly),
        upper(b*K*vp[0]*v[0]*wn/2)]
    mean_total=upper(sum(sixmeans,arb(0)))
    V=[scale(add(g[k],W[k]) if k<len(W) else g[k],d["Rwave"]) for k in range(4)]
    Bij={}
    for k,a in enumerate(V):
        for l in range(3):
            z=IP(a,l);degree=k+l
            Bij[degree]=add(Bij[degree],z) if degree in Bij else z
    B=[Bij[k] for k in range(6)]
    outertail=upper(sum((ex(Q(1,N**k))*diff(IP(a,2))[0] for k,a in enumerate(V)),arb(0)))
    gate(doc,"four new complete inverse coefficients six exact means two inner tails and all six outer coefficients are present",
         [len(x) for x in g]==[7,6,5,4] and len(sixmeans)==6 and len(B)==6
         and len(B[0])>=3 and len(B[1])>=3
         and finite_tree([g,rcoef,r3,tail_u,tail_v,sixmeans,V,B,outertail]))
    gate(doc,"every primitive has its differentiated coefficient and all low residual degrees are canceled only by FA13",
         len(Ug)==4 and len(Vw)==2 and all(len(x)==3 for x in Ug+Vw)
         and set(rcoef)=={3,4,5,6}
         and all(len(x[2])>=2 for x in Ug+Vw)
         and all(len(IP(x,2))>=2 for x in V))
    doc["complete_new_finite_primitive_conclusion"]=encode({
        "g0_through_g3_complete_component_sum_angular_jets":g,
        "exact_vanishing_residual_degrees":[-1,0,1,2],"positive_residual_coefficients_3_through_6":rcoef,
        "complete_R3_weighted_upper":r3,
        "six_original_mean_positive_terms":sixmeans,"complete_six_mean_sum":mean_total,
        "complete_inner_I_remainders":{"uG":tail_u,"vW":tail_v},
        "complete_outer_density_amplitude_jets":V,"complete_B0_through_B5_angular_jets":B,
        "complete_outer_primitive_derivative_remainder":outertail,
        "old_original_means_set_to_zero":False,"number_of_complete_old_I_expansions":3,
        "all_matrix_and_vector_jets_are_entry_sum_majorants":True})
    return dict(g=g,W=W,V=V,B=B,r3=r3,tail_u=tail_u,tail_v=tail_v,
                mean_total=mean_total,outertail=outertail)

def complete_real_Airy_profiles(d,doc):
    """DLMF9.7(iii), four alternating real series, valid even when n*omega is small."""
    u=[Q(1)];vv=[Q(1)]
    for k in range(1,6):
        u.append(u[-1]*Q((6*k-5)*(6*k-3)*(6*k-1),(2*k-1)*216*k))
        vv.append(Q(6*k+1,1-6*k)*u[k])
    om=(ex(Q(2,3))*((d["tlo"].log()*ex(Q(3,2))).exp())).lower()
    if not om>0:raise ValueError("positive same-cut optical denominator absent")
    ta=power(d["tlo"],Q(-1,4));tb=power(d["thi"],Q(1,4))
    invpi=upper(1/arb.pi().sqrt())
    pa=upper(invpi*ta*(1+ex(u[1])/(N*om)+ex(u[2])/(N*N*om*om)+ex(u[3])/(N**3*om**3)))
    pb=upper(invpi*tb*(1+ex(abs(vv[1]))/(N*om)+ex(abs(vv[2]))/(N*N*om*om)+ex(abs(vv[3]))/(N**3*om**3)))
    pstar=high(pa,pb);p1=upper(invpi/om*high(ex(u[1])*ta,ex(abs(vv[1]))*tb))
    p2=upper(invpi*high(ta*(ex(u[2])/om**2+ex(u[3])/(N*om**3)),
                        tb*(ex(abs(vv[2]))/om**2+ex(abs(vv[3]))/(N*om**3))))
    def exponential_envelope(alpha):
        c=Q(1,2048)
        def one(p):
            x=max(Q(N),Q(p)/c)
            return upper(power(ex(x),p)*(-ex(c*x)).exp())
        return upper(20*(one(alpha)+ex(Q(19,1000000))*one(Q(alpha)+Q(2,3))))
    e19=exponential_envelope(Q(19,6));e13=exponential_envelope(Q(13,6))
    gate(doc,"the complete real Airy profiles and original-mean envelopes cover all n>=388 without a large-phase assumption",
         u[1]==Q(5,72) and vv[1]==Q(-7,72)
         and all(u[k]>0 and vv[k]<0 for k in range(1,6))
         and -u[2]<0<u[4] and -u[3]<0<u[5]
         and -vv[2]>0>vv[4] and -vv[3]>0>vv[5]
         and Q("0.002921264998045")-Q(1,512)>Q(1,2048)
         and finite_tree([pa,pb,pstar,p1,p2,e19,e13]) and om>0)
    doc["complete_new_real_Airy_profile_conclusion"]=encode({
        "exact_DLMF_u0_through_u5":u,"exact_DLMF_v0_through_v5":vv,
        "complete_omega_real_lower":om,"complete_scaled_Ai_upper":pa,
        "complete_scaled_Ai_argument_derivative_upper":pb,"complete_scaled_profile_upper":pstar,
        "complete_first_inverse_frequency_profile_upper":p1,
        "complete_first_omitted_scaled_remainder_coefficient":p2,
        "complete_original_mean_E19over6":e19,"complete_original_mean_E13over6":e13,
        "real_variable_error_theorem_for_all_t_positive":True,
        "n_omega_ge_one_required":False,"Airy_error_ball_differentiations":0,
        "physical_cutoff_frequency":N,"mean_contour_physical_width":str(WIDTH),
        "complete_mean_exponent_lower":"1/2048","Ai_initial_modulus_upper":"1"})
    return dict(P=pstar,P1=p1,P2=p2,E19=e19,E13=e13)

def complete_cut_reconstruction(d,a,p,doc):
    B=a["B"];b,vphi,K=d["b"],d["v"][1],d["K"]
    inner=upper(b*vphi/2*(a["tail_u"]+K*a["tail_v"]))
    local=upper(p["P"]*(a["r3"]+inner))
    means=upper(p["E19"]*a["mean_total"])
    CJres=upper(local+means)
    Jstar=ex(Q("0.825332620"))
    fees=[upper(d["Rwave"]*Jstar*CJres/4),
          upper(p["P"]*a["outertail"]/4),
          upper(p["E13"]*poly_norm(B))]
    crecon=upper(sum(fees,arb(0)))
    airy_fees=[upper(p["P"]*poly_norm(B,2)),
               upper(p["P1"]*B[1][0]),
               upper(p["P2"]*(B[0][0]+B[1][0]/N))]
    cairy=upper(sum(airy_fees,arb(0)));cpre=upper(crecon+cairy)
    gate(doc,"the complete J residual three outer-reconstruction fees and all Airy polynomial remainder groups are finite",
         len(fees)==len(airy_fees)==3 and finite_tree([inner,local,means,CJres,fees,crecon,airy_fees,cairy,cpre]))
    doc["complete_new_cut_reconstruction_conclusion"]=encode({
        "complete_J_residual_inner_primitive_fee":inner,"complete_J_residual_local_and_inner_fee":local,
        "complete_J_residual_six_mean_fee":means,"complete_J_residual_coefficient":CJres,
        "original_complete_J_L2_upper":"0.825332620",
        "three_complete_reconstruction_fees":{
            "full_J_error_after_outer_old_I":fees[0],
            "full_outer_old_I_tail":fees[1],"full_outer_old_mean":fees[2]},
        "complete_reconstruction_coefficient":crecon,
        "three_complete_Airy_remainder_fees":{
            "B2_through_B5_complete_profiles":airy_fees[0],
            "B1_times_first_Airy_correction":airy_fees[1],
            "B0_plus_zB1_times_full_Airy_remainder":airy_fees[2]},
        "complete_Airy_remainder_coefficient":cairy,
        "complete_unnormalized_first_omitted_column_coefficient":cpre,
        "column_power":"n^-2","old_Hminus5_3_J_constant_not_used_as_L2_J":True})
    return cpre

def real_power_jet(d,p):
    """Derivatives of the known t coefficient only, never derivatives of the Airy remainder."""
    p=Q(p)
    def pw(k):
        r=p-k
        return power(d["tlo"] if r<0 else d["thi"],r)
    return [pw(0),upper(abs(ex(p))*pw(1)*d["tphi"]),
            upper(abs(ex(p*(p-1)))*pw(2)*d["tphi"]**2+abs(ex(p))*pw(1)*d["tphiphi"])]
def reciprocal_phase_jet(d):
    k=d["kappa"];lo=d["kappa_lower"]
    inv=[upper(1/lo)]
    for q in (1,2):
        inv.append(upper(sum((math.comb(q,j)*k[j]*inv[q-j] for j in range(1,q+1)),arb(0))/lo))
    return inv

def complete_first_frame_and_leading(d,a,cpre,receipts,doc):
    # B entries already include n_g T(q), and their jets are complete entry sums.
    ta=real_power_jet(d,Q(-1,4));tb=real_power_jet(d,Q(1,4))
    omega_inv=scale(real_power_jet(d,Q(-3,2)),ex(Q(3,2)))
    lead=add(ta,tb);first=mul(omega_inv,add(scale(ta,ex(Q(5,72))),scale(tb,ex(Q(7,72)))))
    normal=1/(2*arb.pi().sqrt())
    A0=scale(mul(lead,a["B"][0]),normal)
    A1=scale(add(mul(lead,a["B"][1]),mul(first,a["B"][0])),normal)
    ki=reciprocal_phase_jet(d);A0ki=mul(A0,ki);A1ki=mul(A1,ki);A0ki2=mul(A0ki,ki)
    b0prime=diff(A0ki);bp_over_k=mul(b0prime,ki)
    E0=upper(diff(A0ki2)[0]+2*bp_over_k[0]+diff(bp_over_k)[0]/4)
    E1=upper(2*A1ki[0]+A1ki[1]/4)
    tn=receipts["TN_execution"];tc=receipts["TC_execution"]["complete_density_coordinate_conclusion"]
    tnc=tn["complete_selected_normalizer_conclusion"];tnr=tn["complete_strong_remainder_conclusion"]
    S=oldupper(tnc["complete_S_upper"])
    Sp=oldupper(tn["complete_normalizer_coefficient_conclusion"][0]["complete_coefficients"]["complete_S_phi_upper"])
    frame=upper(2*S*(E0+E1))
    Uminus=oldupper(tc["complete_density_Hminus4_3_upper"])
    Lminus=upper(4*Uminus*(w43(A0ki)+w43(A1ki)/N))
    Sminus=upper(3*sqrt_upper(S*S+2*Sp*Sp+(768*Sp)**2))
    corrected=upper(Lminus+4*Sminus/N*Uminus*w43(A0ki2))
    hs=upper(2*power(ex(4),Q(-2,3))*sqrt_upper(
        power(ex(J_C),Q(-4,3))+3*power(ex(J_C),Q(-1,3))))
    w=tnc["complete_selected_cutoff_window_verdicts"]["L2"]
    K0=oldupper(w["ordered_inverse_upper"]);forward=oldupper(w["complete_forward_upper"])
    RN=oldupper(tnr["complete_ordered_inverse_strong_remainder_upper"])
    FS=oldupper(tnr["complete_uncompressed_first_symbol_finite_difference_upper"])
    terms=[upper(K0*hs*cpre),upper(hs*frame),upper((FS+RN)*Lminus)]
    freecut=upper(sum(terms,arb(0)))
    rawcut=upper(forward*freecut)
    st=receipts["ST_execution"]["complete_endpoint_and_source_conclusion"]
    nglower=positive_lower(st["complete_new_cut_ng_lower"],"same actual P22 n_g lower")
    Kc=upper(corrected/nglower)
    gate(doc,"the complete first frame both sign inputs corrected negative-window map and same-cut forward conversion are paid once",
         d["kappa_lower"]>0 and tnc["first_bandwidth"]==192
         and st["exact_full_radial_length"]==str(CUT)
         and st["both_independent_means_and_complete_finite_blocks_retained"]
         and st["saved_TN_L2_forward_normalizer_read_verbatim"]==w["complete_forward_upper"]
         and st["saved_complete_cut_ng_upper_read_verbatim"]==receipts["RR_execution"]["complete_physical_cut_coefficient_conclusion"][0]["complete_ng_upper"]
         and finite_tree([A0,A1,ki,E0,E1,frame,Lminus,Sminus,corrected,hs,terms,freecut,rawcut,Kc]))
    doc["complete_new_first_frame_and_leading_conclusion"]=encode({
        "complete_common_each_sign_each_branch_A0_angular_jets":A0,
        "complete_common_each_sign_each_branch_A1_angular_jets":A1,
        "complete_phase_reciprocal_angular_jets":ki,
        "complete_E0_per_branch":E0,"complete_E1_per_branch":E1,
        "complete_frame_column_coefficient":frame,
        "vector_H2_is_scalar_component_sum":True,
        "component_sum_H2_bound":"a0+sqrt(2)*a1+a2 with aq the sum of component L2 bounds",
        "complete_U_Phi_Hminus4_3_upper_read_verbatim":copy.deepcopy(tc["complete_density_Hminus4_3_upper"]),
        "inverse_U_Phi_Hminus4_3_not_substituted":True,
        "complete_uncorrected_leading_Hminus4_3_upper":Lminus,
        "complete_S_Hminus4_3_multiplier_upper":Sminus,
        "complete_corrected_Bfree1_Hminus4_3_upper":corrected,
        "complete_both_sign_Hilbert_Schmidt_factor":hs,
        "complete_normalized_free_cut_strong_terms":{
            "TN_inverse_times_full_n2_remainder":terms[0],
            "full_first_frame_remainder":terms[1],
            "full_finite_FS_and_strong_RN_times_same_leading":terms[2]},
        "complete_normalized_free_cut_Hminus4_3_to_L2_upper":freecut,
        "complete_same_TN_forward_L2_times_free_cut_upper":rawcut,
        "same_cut_ng_lower_read_verbatim":copy.deepcopy(st["complete_new_cut_ng_lower"]),
        "complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once":Kc,
        "input_cutoff_abs_j":J_C,"moving_normalizer_cutoff_abs_j":tnc["exact_cutoff_abs_j"],
        "full_finite_FS_support_through":tnc["exact_cutoff_abs_j"]+191,
        "FS_is_norm_paid_not_deleted":True,"old_TN_normalizer_or_TC_coordinate_target_recomputed":False,
        "independent_external_physical_means_and_all_finite_cross_blocks_retained":True,
        "waist_leading_receiver_incoming_outgoing_or_full_R0_claimed":False})
    return freecut,corrected

def render(doc):
    head="# Actual free-Airy first-omitted strict-cut scalar consumer\n\n"
    if not doc.get("complete"):
        return head+"The new target is incomplete. Complete available scientific fields and the exact failure are retained in execution.json.\n"
    z=doc["complete_new_first_frame_and_leading_conclusion"]
    labels=[
      ("Normalized free cut strong bound", "complete_normalized_free_cut_Hminus4_3_to_L2_upper"),
      ("Same-cut raw error after one forward TN fee","complete_same_TN_forward_L2_times_free_cut_upper"),
      ("Original uncorrected leading negative-window bound","complete_uncorrected_leading_Hminus4_3_upper"),
      ("Corrected B_free^[1] negative-window bound","complete_corrected_Bfree1_Hminus4_3_upper"),
      ("SF26 Kc minus after one n_g inverse","complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once")]
    rows="\n".join("| "+name+" | "+z[key]["ball"]+" |" for name,key in labels)
    return head+(
      "This is the new finite scalar recipe of FA, evaluated once from the immutable original free-radius budget "
      "and successful RR/TN/TC/ST receipts. Both physical signs, both oscillatory branches, all six old means, "
      "the two inner primitive tails and complete outer reconstruction remain present.\n\n"
      "| Complete scalar | Directed upper enclosure |\n|---|---|\n"+rows+"\n\n"
      "Input cutoff |j| >=97 and the saved moving normalizer cutoff are different. "
      "The complete finite F_S map is norm-paid, including its mean and cross rows. "
      "The TC factor used is U_Phi on H^(-4/3), with its inverse recorded separately. "
      "The last two rows concern the corrected first-order map and its ungauged SF26 convention; "
      "they do not replace an incoming inverse or a waist leading receiver.\n\n"
      "Old scientific calls: 0. Original Taylor coefficients, radius budgets, profile integrals, J, "
      "normalizers and coordinate targets were read unchanged. No Airy remainder ball was differentiated. "
      "Complete source identity, all gates, intermediate scalar budgets and temporary native identity are in execution.json.\n")

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--workdir",type=Path,required=True)
    p.add_argument("--process",type=Path,required=True)
    p.add_argument("--conclusion",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=320;start=time.monotonic()
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=None,failure=None,gates=[],
       source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),public_repository=PUBLIC,
       run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
       workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
       runtime=RUNTIME,arithmetic_bits=320,mathematical_parameters=PARAMETERS,
       old_numerical_enclosures_recomputed=0,old_scientific_source_imports=0,
       old_Taylor_fold_profile_radius_J_normalizer_or_coordinate_calls=0,
       old_binary_inputs_restored_only_temporarily=True,original_input_bytes_modified=False,
       new_recomputable_arrays_persisted=False,new_reference_columns=1,new_physical_signs=2,
       new_oscillatory_branches=2,new_inverse_amplitude_coefficients=0,new_exact_mean_terms=0,
       new_inner_primitive_tail_groups=0,new_outer_polynomial_coefficients=0,
       complete_free_cut_strong_bound_proved=False,
       full_incoming_inverse_claimed=False,full_return_R0_claimed=False,
       finite_Schur_inverse_claimed=False,actual_PDE_solution_claimed=False,final_surface_claimed=False)
    args.workdir.mkdir(parents=True,exist_ok=True)
    def checkpoint():
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-start
        save(args.process,doc)
        print(json.dumps(dict(kind="free_Airy_cut_checkpoint",stage=doc.get("stage"),
              complete=doc["complete"],gates=len(doc["gates"]),saved_bytes=len(canonical(doc)),
              saved_sha256=sha_bytes(canonical(doc))),sort_keys=True),flush=True)
    checkpoint()
    try:
        doc["stage"]="immutable-original-inputs"
        m,paths,receipts=checked_inputs(args,doc)
        f,c=original_fold(paths,doc);saved=original_free_radius(paths,doc)
        doc["original_successful_small_receipts_read"]=4
        doc["original_complete_fold_and_radius_stages_read"]=2
        checkpoint()
        doc["stage"]="new-cut-domain-and-complete-coefficient-jets"
        d=new_domain_and_jets(f,c,saved,receipts,doc);checkpoint()
        doc["stage"]="new-finite-original-J-and-I-calculus"
        a=complete_finite_primitive_calculus(d,doc)
        doc.update(new_inverse_amplitude_coefficients=4,new_exact_mean_terms=6,
                   new_inner_primitive_tail_groups=2,new_outer_polynomial_coefficients=6)
        checkpoint()
        doc["stage"]="new-global-real-Airy-and-complete-mean-envelopes"
        p=complete_real_Airy_profiles(d,doc);checkpoint()
        doc["stage"]="new-complete-two-row-density-reconstruction"
        cpre=complete_cut_reconstruction(d,a,p,doc);checkpoint()
        doc["stage"]="new-first-frame-leading-and-strong-cut-receiver"
        complete_first_frame_and_leading(d,a,cpre,receipts,doc);checkpoint()
        gate(doc,"all exact old bytes remain unchanged and no successful old numerical target was called",
             all(sha(paths[k])==v for k,v in PINNED.items())
             and all(doc[k]==0 for k in ("old_numerical_enclosures_recomputed","old_scientific_source_imports",
                       "old_Taylor_fold_profile_radius_J_normalizer_or_coordinate_calls")))
        gate(doc,"the full original means finite map and all new scalar groups survive in the saved conclusion",
             doc["new_inverse_amplitude_coefficients"]==4 and doc["new_exact_mean_terms"]==6
             and doc["new_inner_primitive_tail_groups"]==2 and doc["new_outer_polynomial_coefficients"]==6
             and doc["complete_new_first_frame_and_leading_conclusion"]["FS_is_norm_paid_not_deleted"]
             and doc["complete_new_first_frame_and_leading_conclusion"]["independent_external_physical_means_and_all_finite_cross_blocks_retained"])
        gate(doc,"all twenty-four structural gates are complete for the exact new strong-cut scalar scope",
             len(doc["gates"])==GATE_COUNT-1 and all(g["passed"] for g in doc["gates"])
             and doc["new_reference_columns"]==1 and doc["new_physical_signs"]==doc["new_oscillatory_branches"]==2)
        doc.update(complete=True,proved=True,actual_returncode=0,
                   complete_free_cut_strong_bound_proved=True,stage="complete-new-free-Airy-strong-cut-scalars")
    except Exception as error:
        doc.update(actual_returncode=1,failure=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc()))
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-start
    # Complete small science is atomic before compression, presentation or any size guard.
    save(args.process,doc)
    native=dict(complete_small_conclusion=doc,numerical_arrays_are_temporary_only=True)
    raw=canonical(native);args.out.parent.mkdir(parents=True,exist_ok=True)
    tmp=args.out.with_name(args.out.name+".partial");tmp.write_bytes(gzip.compress(raw,mtime=0));tmp.replace(args.out)
    doc["temporary_native_sha256"]=sha(args.out);doc["temporary_native_bytes"]=args.out.stat().st_size
    save(args.process,doc)
    args.conclusion.parent.mkdir(parents=True,exist_ok=True);args.conclusion.write_text(render(doc))
    print(json.dumps(dict(kind="free_Airy_cut_complete_small_science_identity",
        bytes=len(canonical(doc)),sha256=sha_bytes(canonical(doc)),complete=doc["complete"],
        actual_returncode=doc["actual_returncode"]),sort_keys=True),flush=True)
    if len(canonical(doc))>45000:
        raise RuntimeError("complete new science is already saved but exceeds the small presentation budget")
    if not doc["complete"]:raise SystemExit(1)

if __name__=="__main__":main()
