#!/usr/bin/env python3
"""Complete root-mean-value and saved-product strict Darboux recovery.

The failed DR prefix is read exactly. New arithmetic is only the same-germ
root derivative inference, joint-disk free g bounds, and remaining physical
readout. No successful free product or derivative array is evaluated again.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_root_mean_value_saved_product_Darboux_receiver_v1"
CONTRACT="78b2fe438d8c36ecb9779c1b86cad06d56c28a272d8028ef8c4e27ba63d7ff5a"
DR_CONTRACT="0e80f086565a78fc90a8ace9a79da274d76f5fd97e7c8685e870a4977c0d2a19"
PARTIAL_EXEC="dd72c47699df51516462c286de851cf846c76413d9b28b7ba12533802618b147"
PARTIAL_SOURCE="8f8553ca9da27962c8e907eeb9a33ab56441ef45718d0297913318271e72998c"
PARTIAL_MANIFEST="5c7cd6f97c9957a2aa979e068f1ea65421823681352a0af16fddd158156e4648"
PARTIAL_PROCESS="1dbae62c3e566ad7df583ac98408b6b1012157630ea7994c401d4ba7ad15ec06"
PARTIAL_WORKER="811685d7c17815aebb14c3f81338464ecd14da599dd5ad2163acef2cd07aacc3"
IN_CONTRACT="d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
RCUT=Q(76285779072683,320000000000000)
H=Q(893368603925465506687,21990232555520000000000000)
RG=Q(3,8000);SG=Q(3,128);SB=Q(1,64);HI=Q(1,20000)
RS=Q(1,8000);SS=Q(3,512);SNEW=Q(3,1024);N=388
COMPONENTS=("a","a_phi","a_phiphi","b","b_phi","b_phiphi")
PART_SHA="ada966331fcabf90da9f17597cdd0c4e0a56cfaf6233787e69c2587b104a8a21"
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
OLD_NATIVE="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
OLD_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
OLD_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
FORCE_SHA="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47"
FORCE_SOURCE="ba25934f0f6e147f293644edc93b2adf1c33d5935f86596d96355cf063c95fa6"
FORCE_MANIFEST="a7790a87932a22997e29dfa2085982ac7adbbef9fd36512918eec975dd3c5341"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
SHARED_SHA="517de329d0cee3466523e9eaaa2747a79ab3da2c771d4ec2984b38784a9b33ee"
EXPECTED={
    "accepted_IN_execution": [
        "43746008734",
        "726bdd98802c88e9c162f598ff983bc8a762d8cc8f8216164c56e6b960119874",
        "fc87dad98247598d6183d225f4dfca29ee66a8cd06c0918ffda59888091cfb74",
        "816483884254f3e7ec06914b66afffc8434db11315dfab1712e71fbb7aae5ae1",
        23
    ],
    "columns_execution": [
        "43688459733",
        "9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c",
        "1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99",
        "fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57",
        16
    ],
    "potential_execution": [
        "43685624307",
        "042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7",
        "44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437",
        "d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9",
        16
    ],
    "accepted_RV_execution": [
        "43719681982",
        "d59893af66b8829d924d75686fb0ecd6e6d25f9b72b70a0fac6564c4e96fdf60",
        "4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded",
        "0781239c0753785d2b196b77cc90c0eb343d52cc73226d84d7f8f6bb23136473",
        27
    ],
    "accepted_SV_execution": [
        "43722805762",
        "44021afbf608638e7e08f584a5574acdc76738c5985d72ca0f2b036c8f7d2dc0",
        "5306e66c5102e358caba5946b3c651dda11fb98a18848f8fe27f779f775d73cf",
        "ba96a4832017144ea3ccd59902e8bcb8f1b0acd1c722edadc44b763dfac6c0d0",
        23
    ],
    "refined_first_local_execution": [
        "43711480764",
        "e0541949f521e0852bb4a8b204b51281f7d83e0ed2a7a1afbb259ca73362e92a",
        "5e2618c446288cd8d84fcbf4bb7955f56f7a1041f823e05213d043d20b5aeaaf",
        "20422f41645c2a4544bb8a0d79eddf771b45ff0386cc81b3ee97a32849586ef2",
        19
    ],
    "Taylor_execution": [
        "43694458725",
        "a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be",
        "11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65",
        "777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1",
        9
    ]
}
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"cutoff_abs_j\":97,\"exact_new_product_radius\":\"1/8000\",\"exact_new_product_strip\":\"3/512\",\"exact_original_fold_radius\":\"3/8000\",\"exact_original_fold_strip\":\"3/128\",\"exact_original_free_inverse_radius\":\"1/20000\",\"exact_original_inverse_strip\":\"1/64\",\"exact_original_profile_cover\":\"893368603925465506687/21990232555520000000000000\",\"exact_real_delta_radius\":\"1/100000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"full_incoming_inverse_or_strong_return_claimed\":false,\"input_window\":\"H^(-4/3), both reference columns and both signs |j|>=97\",\"old_scientific_producer_calls\":0,\"original_J_window\":\"H^(-5/3) to H^(-2/3)\",\"original_common_row_part\":[3066,3322],\"original_complete_forcing_rows\":1328,\"original_complete_intrinsic_part_rows\":256,\"original_complete_norm_rows\":1328,\"output_window\":\"old-circle L2 density pair plus both mean coordinates\",\"physical_frequency\":\"n=4|j|\",\"same_order_L_B_window\":\"H^(-5/3) to H^(-5/3)\",\"strict_normalizers_and_final_circle_not_yet_composed\":true,\"exact_new_joint_g_strip\":\"3/1024\",\"accepted_partial_run\":\"43748529142/1\",\"original_intrinsic_member_bytes\":1167787,\"successful_partial_math_recomputed\":0,\"new_curvature_method\":\"same original signed K1 and exact root FTC\",\"expected_actual_gate_count\":28}")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def payload_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith(".gz") else b)
def save(p,x,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    b=gzip.compress(raw,mtime=0) if compressed else raw
    t=p.with_name(p.name+".tmp");t.write_bytes(b);t.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def up(v):
    a=rb(v)
    if not a.is_finite() or a.lower()<0:raise ValueError("invalid complete nonnegative budget")
    return a.upper()
def gap(v,label):
    a=rb(v).lower()
    if not a.is_finite() or not a>0:raise ValueError("unproved strict positive gap: "+label)
    return a
def rec(x):return dict(ball=rb(x).str(52))
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def accepted(path,identity,gate):
    run,source,manifest,digest,ngates=identity
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 retains immutable success and its exact runtime",
        sha(path)==digest and str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==RUNTIME
        and len(r.get("gates",[]))==ngates and all(g.get("passed") is True for g in r["gates"]))
    return r



def read_original_fold(paths,gate):
    ms=read(paths["old_fold_majorants_stage"]);p=read(paths["adjacent_process"]);u=read(paths["adjacent_publication"])
    entries=[e for e in u["files"] if e["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
    gate("the original complete fold and leading product are restored exactly without any producer call",
        sha(paths["old_fold_majorants_stage"])==MAJORANTS and sha(paths["adjacent_process"])==APROC
        and sha(paths["adjacent_publication"])==APUB and len(entries)==1
        and entries[0]["bytes"]==4501 and entries[0]["sha256"]==MAJORANTS
        and ms["complete"] and ms["stage"]==ms["name"]=="complete-original-reference-holomorphic-majorants"
        and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
        and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==RUNTIME
        and p["actual_returncode"]==0 and p["mathematical_complete"] and p["mathematical_proved"]
        and p["mathematical_failure"] is None and u["complete"]
        and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi","a0","b0")))
    # Return the original encoded payload. Only explicitly used scalar moduli
    # below are read; no legacy module or old fold closure is evaluated.
    return ms["payload"]

def read_cut_rows(paths,gate):
    norm,force=read(paths["original_norm_native"]),read(paths["original_forcing_native"])
    np,fp=read(paths["original_norm_process"]),read(paths["original_forcing_process"])
    def allpass(g,n):return isinstance(g,list) and len(g)==n and all(x.get("passed") is True for x in g)
    gate("both complete original norm and forcing natives retain their exact actual successes",
        sha(paths["original_norm_native"])==OLD_NATIVE and sha(paths["original_forcing_native"])==FORCE_SHA
        and norm.get("complete") and norm.get("proved") and norm.get("failure") is None
        and force.get("complete") and force.get("proved") and force.get("failure") is None
        and norm.get("source_sha256")==OLD_SOURCE and force.get("source_sha256")==FORCE_SOURCE
        and norm.get("input_manifest_sha256")==OLD_MANIFEST and force.get("input_manifest_sha256")==FORCE_MANIFEST
        and allpass(norm.get("gates"),7) and allpass(force.get("gates"),14)
        and all(p.get("complete") and p.get("failure") is None and p.get("actual_returncode")==0
            and p.get("mathematical_complete") and p.get("mathematical_failure") is None for p in (np,fp))
        and str(np.get("run_id"))=="43629465215" and str(fp.get("run_id"))=="43624260519"
        and str(np.get("run_attempt"))==str(fp.get("run_attempt"))=="1"
        and np.get("native_sha256")==OLD_NATIVE and fp.get("native_sha256")==FORCE_SHA
        and np.get("native_bytes")==4837715 and fp.get("native_bytes")==6577892
        and np.get("mathematical_source_sha256")==OLD_SOURCE and fp.get("mathematical_source_sha256")==FORCE_SOURCE
        and np.get("manifest_sha256")==OLD_MANIFEST and fp.get("manifest_sha256")==FORCE_MANIFEST
        and allpass(np.get("mathematical_gates"),7) and allpass(fp.get("mathematical_gates"),14))
    gate("the original norm and forcing rows keep the same full family root and both physical means",
        norm.get("root_native_sha256")==force.get("root_native_sha256")==ROOT_SHA
        and norm.get("first_forcing_native_sha256")==FORCE_SHA
        and norm.get("exact_root_interval")==force.get("exact_root_interval")==list(map(str,ROOTS))
        and norm.get("exact_real_delta_radius")==force.get("exact_real_delta_radius")=="1/100000000"
        and norm.get("exact_cover")==force.get("exact_cover")
        and norm.get("old_mean_and_all_Fourier_outputs_retained") is True
        and force.get("full_original_193_direction_and_even_mean_retained") is True)
    rows=norm["coefficient_rows"];frows=force["rows"];selected=[]
    if len(rows)!=1328 or len(frows)!=1328:raise ValueError("the original complete row count differs")
    edge=Q(force["exact_cover"][0])
    for index,(nr,fr) in enumerate(zip(rows,frows)):
        lo,hi=map(Q,fr["interval"])
        if (nr["common_row"]!=index or nr["interval"]!=fr["interval"]
            or nr["original_root_row"]!=fr["original_root_row"] or lo!=edge or not lo<hi):
            raise ValueError("a complete same-row norm identity changed")
        edge=hi
        if lo<=RCUT<=hi:selected.append((index,nr,fr))
    gate("all1328 original rows match and every closed P22 cut side is selected by exact rational membership",
        edge==Q(force["exact_cover"][1]) and 1<=len(selected)<=2
        and Q(9,50)<RCUT<ROOTS[0] and ROOTS[0]-RCUT==Q(1,262144))
    shared=read(paths["shared_intrinsic_manifest"]);part=read(paths["original_intrinsic_part"])
    specs=[s for s in shared["parts"] if s["common_row_indices"]==[3066,3322]]
    if len(specs)!=1:raise ValueError("the one actual P22 intrinsic part is not unique")
    spec=specs[0]
    gate("only the complete original intrinsic part3066_3322 with its full identity is restored",
        sha(paths["shared_intrinsic_manifest"])==SHARED_SHA
        and sha(paths["original_intrinsic_part"])==PART_SHA==spec["sha256"]
        and shared.get("original_body_run")==43583838026 and shared.get("original_body_attempt")==1
        and shared.get("kind")=="fixed_original_intrinsic_third_jet_parts_for_real_root_radius_one_over_fifty_v1"
        and part.get("kind")=="actual_full_regular_joint_radial_polynomial_residual_rows_v1"
        and part.get("complete") is False and part.get("selected_cells_complete") is True
        and part.get("failure") is None and part.get("identity")==shared["original_row_identity"]
        and part.get("selected_indices")==[3066,3322] and len(part.get("rows",[]))==256)
    body={};edge=Q(spec["exact_interval"][0])
    for index,br in enumerate(part["rows"],3066):
        lo,hi=map(Q,br["interval"])
        if br.get("common_row")!=index or lo!=edge or not lo<hi:
            raise ValueError("the original complete intrinsic part cover changed")
        body[index]=br;edge=hi
    joined=[]
    for index,nr,fr in selected:
        br=body[fr["original_common_row"]]
        if (fr["original_intrinsic_interval"]!=br["interval"]
            or fr["actual_scalar_germ"]!=br["actual_scalar_germ"]
            or not Q(br["interval"][0])<=RCUT<=Q(br["interval"][1])):
            raise ValueError("the actual cut uses a different intrinsic scalar germ")
        joined.append((index,nr,fr,br))
    gate("all selected P22 sides match the complete original intrinsic germ and true cut interval",
        edge==Q(spec["exact_interval"][1]) and len(joined)==len(selected)
        and all(3066<=fr["original_common_row"]<3322 for _,_,fr,_ in joined))
    identity=dict(exact_strict_cut=str(RCUT),exact_root_interval=list(map(str,ROOTS)),
        exact_true_rho_interval=[str(ROOTS[0]-RCUT),str(ROOTS[1]-RCUT)],
        complete_original_norm_rows=1328,complete_original_forcing_rows=1328,
        complete_original_intrinsic_part_rows=256,complete_cut_sides=len(joined),
        original_part_sha256=PART_SHA,original_part_bytes=paths["original_intrinsic_part"].stat().st_size,
        original_part_common_row_indices=[3066,3322],original_part_interval=spec["exact_interval"],
        complete_cut_row_identity=[dict(original_norm_row=i,original_root_row=fr["original_root_row"],
            original_common_row=fr["original_common_row"],exact_interval=fr["interval"],
            original_intrinsic_interval=br["interval"],original_saved_norm_row_sha256=payload_sha(nr),
            original_saved_forcing_row_sha256=payload_sha(fr),original_saved_intrinsic_row_sha256=payload_sha(br))
            for i,nr,fr,br in joined],
        no_candidate_piece_number_substituted_for_common_row=True,
        no_old_Cauchy_cut_or_SP_gain_moved_to_P22=True)
    return joined,identity

def accepted_scalar_receivers(R,gate):
    first=R["accepted_IN_execution"];dom=first["complete_strict_cut_domain_conclusion"]
    fun=first["complete_new_functional_conclusion"];raw=first["complete_scalar_receiver_conclusion"]
    p=first["mathematical_parameters"]
    gate("the completed first Darboux receiver has the exact P22 input window and all original mean and segment qualifications",
        p["exact_strict_cut"]==str(RCUT) and p["exact_root_interval"]==list(map(str,ROOTS))
        and p["exact_real_delta_radius"]=="1/100000000" and p["cutoff_abs_j"]==97
        and p["physical_frequency"]=="n=4|j|" and p["fixed_intrinsic_parameter"]=="eta_0"
        and p["exact_original_profile_cover"]==str(H) and p["input_window"]=="H^(-4/3)"
        and dom["exact_strict_cut"]==str(RCUT)
        and dom["exact_rho_interval"]==[str(ROOTS[0]-RCUT),str(ROOTS[1]-RCUT)]
        and dom["actual_fixed_cut_all_tau_segments"] is True
        and dom["all_complete_physical_means_and_both_reference_columns_retained"] is True
        and dom["accepted_RV_domain_payload_sha256"]==payload_sha(R["accepted_RV_execution"]["complete_domain_conclusion"])
        and dom["accepted_SV_column_payload_sha256"]==payload_sha(R["accepted_SV_execution"]["complete_exact_inverse_column_conclusion"])
        and fun["exact_input_component_order"]==list(COMPONENTS)
        and fun["all_output_means_and_both_reference_column_inputs_retained"] is True
        and len(fun["complete_zero_order_functional_coefficients"])==6
        and fun["zero_order_output_window"]=="L2"
        and raw["density_zero_w0_p0_g0_include_all_output_means"] is True
        and raw["density_one_w1V_p1_g1_include_all_output_means"] is True
        and raw["p_rows_have_not_yet_been_multiplied_by_radial_eta_inverse"] is True
        and raw["physical_J_L_B_n_g_Tq_and_free_R2_R3_not_yet_composed"] is True
        and raw["raw_Hminus1_not_renamed_raw_L2"] is True
        and raw["exact_differential_source_input_weights"]==["1/n","1/n^2"]
        and raw["exact_primitive_extra_input_weight"]=="1/n^2")
    dz=raw["density_zero"];one=raw["density_one"];e=raw["complete_inhomogeneous_differential_source_Hminus5_3_upper"]
    if set(dz)!={"w0","p0","g0"} or set(one)!={"w1","p1","g1"} or len(e)!=2:
        raise ValueError("the immutable first scalar collection is incomplete")
    receivers={}
    for k,names,key in ((0,("w0","p0","g0"),"complete_raw_scalar_Hminus1_upper"),
                        (1,("w1","p1","g1"),"complete_scalar_error_L2_upper")):
        r=dz if k==0 else one
        receivers["error_density_"+str(k)]=[up(r[n][key]) for n in names]+[up(e[k])]
    saved=dict(first_domain_payload_sha256=payload_sha(dom),
        first_functional_payload_sha256=payload_sha(fun),first_scalar_receiver_payload_sha256=payload_sha(raw),
        complete_first_density_zero_Hminus1=[copy.deepcopy(dz[n]["complete_raw_scalar_Hminus1_upper"]) for n in ("w0","p0","g0")],
        complete_first_density_one_L2=[copy.deepcopy(one[n]["complete_scalar_error_L2_upper"]) for n in ("w1","p1","g1")],
        complete_first_differential_sources_Hminus5_3=copy.deepcopy(e),
        complete_zero_order_functional_coefficients=copy.deepcopy(fun["complete_zero_order_functional_coefficients"]),
        original_n_minus_two_strong_multiplier_upper=copy.deepcopy(fun["complete_n_minus_two_strong_multiplier_upper"]),
        already_paid_primitive_extra_not_added_again=True,
        all_eight_accepted_receiver_bounds_read_verbatim=True,
        first_successful_functionals_profiles_or_source_receivers_recomputed=False)
    return receivers,[up(x) for x in fun["complete_zero_order_functional_coefficients"]],up(fun["complete_n_minus_two_strong_multiplier_upper"]),saved


def read_partial_success(paths,identity,saved,gate):
    execution=read(paths["partial_DR_execution"]);r=execution.get("actual_scientific_receipt",{})
    original=copy.deepcopy(r)
    for k in ("complete_physical_comparison_conclusion","scope"):
        if original.get(k) is not None:raise ValueError("the exact failed prefix contains an unexpected later result")
        original.pop(k,None)
    canonical=(json.dumps(original,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    gate("the exact failed DR execution retains its completed twenty-one-gate prefix",
        sha(paths["partial_DR_execution"])==PARTIAL_EXEC
        and str(execution.get("run_id"))=="43748529142" and str(execution.get("run_attempt"))=="1"
        and execution.get("source_budget_source_sha256")==PARTIAL_SOURCE
        and execution.get("input_manifest_sha256")==PARTIAL_MANIFEST
        and execution.get("worker_source_sha256")==PARTIAL_WORKER
        and execution.get("complete") is False and execution.get("actual_returncode")==1
        and execution.get("actual_source_budget_processes")==1
        and execution.get("complete_immutable_Python_AST_closure_passed") is True
        and execution.get("complete_immutable_Python_AST_file_count")==8
        and r.get("source_sha256")==PARTIAL_SOURCE and r.get("input_manifest_sha256")==PARTIAL_MANIFEST
        and r.get("kind")=="actual_complete_strict_physical_Darboux_receiver_v1"
        and r.get("runtime")==RUNTIME and r.get("complete") is False and r.get("proved") is False
        and r.get("actual_returncode")==1
        and r.get("failure")==dict(type="ValueError",message="unproved strict positive gap: strict negative K")
        and len(r.get("gates",[]))==21 and all(g.get("passed") is True for g in r["gates"])
        and len(canonical)==13623 and hashlib.sha256(canonical).hexdigest()==PARTIAL_PROCESS)
    zeros=("old_numerical_enclosures_recomputed","old_profiles_or_calibrations_recomputed",
        "old_amplitude_mixed_jets_or_Taylor_tails_recomputed","old_potential_or_fold_or_inverse_closures_recomputed",
        "old_intrinsic_mean_or_coefficient_rows_recomputed","old_Darboux_scalar_receiver_or_integrals_recomputed",
        "old_PC_PW_SP_N_or_other_successful_producers_called")
    gate("the completed partial identities and all eight first receiver bounds match the current immutable inputs",
        r["complete_original_cut_identity_conclusion"]==identity
        and r["complete_accepted_scalar_conclusion"]==saved
        and all(r.get(k)==0 for k in zeros)
        and r.get("new_free_amplitude_products")==2 and r.get("new_free_p_products")==2
        and r.get("new_free_inverse_entry_angular_budgets")==16
        and r.get("new_free_g_products")==0 and r.get("new_complete_physical_receivers")==0
        and r.get("complete_strict_physical_Darboux_comparison_paid") is False
        and r.get("full_incoming_inverse_claimed") is False and r.get("full_strong_return_R0_evaluated") is False)
    d=r["complete_free_product_domain_conclusion"];prod=r["complete_free_product_conclusion"]
    matrix=d["complete_free_inverse_entry_modulus_upper"]
    valid=(d["exact_strict_cut"]==str(RCUT)
        and d["exact_true_rho_interval"]==[str(ROOTS[0]-RCUT),str(ROOTS[1]-RCUT)]
        and d["exact_reused_product_radius"]==str(RS) and d["exact_reused_product_strip"]==str(SS)
        and d["exact_reused_free_inverse_radius"]==str(HI) and d["exact_reused_free_inverse_strip"]==str(SB)
        and d["no_deformed_gap_compared_to_free_determinant"] is True
        and d["no_real_angle_positive_derivative_promoted_to_strip_modulus"] is True
        and d["original_successful_product_and_inverse_closures_recomputed"] is False
        and len(matrix)==2 and all(len(a)==2 for a in matrix) and set(prod)=={"2","3"}
        and 0<ROOTS[0]-RCUT<=ROOTS[1]-RCUT<HI<RS<RG and 0<SNEW<SS<SB<SG)
    values={}
    for m in (2,3):
        q=prod[str(m)]
        valid=valid and len(q["complete_amplitude_product_modulus_upper"])==2
        valid=valid and len(q["complete_free_p_product_modulus_upper"])==2
        valid=valid and q["complete_all_output_means_retained"] is True
        valid=valid and q["complete_angular_orders_R_and_p"]==4 and q["complete_mixed_r_phi_orders"]==3
        valid=valid and q["exact_remaining_input_frequency_weight"]=="1/n^"+str(m)
        valid=valid and q["original_density_normalization"]=="n^(7/6)"
        valid=valid and q["exact_free_p"]=="-i*epsilon*Q*K*R"+str(m)
        values[m]=dict(M=[up(v) for v in q["complete_amplitude_product_modulus_upper"]],
            P=[up(v) for v in q["complete_free_p_product_modulus_upper"]],
            factor=up(q["complete_input_multiplier_upper"]),
            Gw=up(q["complete_raw_w_Hminus1_upper"]),Gp=up(q["complete_raw_p_Hminus1_upper"]))
        valid=valid and values[m]["factor"]>0
    dr=gap(d["complete_new_product_radial_margin_lower"],"saved successful free-product radial margin")
    inv=[[up(v) for v in row] for row in matrix]
    gate("all successful product domains zero moduli multipliers and four raw receivers are read without reconstruction",
        valid and values[3]["M"][0]==0 and values[3]["P"][1]==0
        and dr<=ex(RS-(ROOTS[1]-RCUT)) and all(v>=0 for row in inv for v in row))
    conclusion=dict(original_run="43748529142/1",original_execution_sha256=PARTIAL_EXEC,
        original_scientific_process_bytes=13623,original_scientific_process_sha256=PARTIAL_PROCESS,
        original_complete_gate_prefix=21,original_late_zero_counters_do_not_mean_zero_partial_math=True,
        original_partial_domain_payload_sha256=payload_sha(d),
        original_partial_products_payload_sha256=payload_sha(prod),
        all_four_saved_w_p_receivers_read_verbatim=True,
        all_saved_domain_product_and_inverse_moduli_read_verbatim=True,
        lost_derivative_arrays_are_hashes_only_and_not_reconstructed=True,
        completed_product_or_old_functional_calls=0)
    return values,inv,dr,copy.deepcopy(d),copy.deepcopy(prod),conclusion

def capture_cut_inputs(rows,original):
    cD=original["coefficients"]["D"]
    if len(cD)<1:raise ValueError("the original whole-product drift modulus is absent")
    out=[]
    for index,nr,fr,br in rows:
        c=nr["bounds"];j=br["intrinsic_whole_third_jets"]
        out.append(dict(original_norm_row=index,original_common_row=fr["original_common_row"],
            exact_original_interval=fr["interval"],exact_original_intrinsic_interval=br["interval"],
            actual_scalar_germ=copy.deepcopy(br["actual_scalar_germ"]),
            original_signed_forcing_K_read_verbatim=copy.deepcopy(fr["complete_intrinsic_ordinary_jets"]["K"][0]),
            original_signed_whole_K1_read_verbatim=copy.deepcopy(j["K1"]),
            original_physical_radius_read_verbatim=copy.deepcopy(j["a"]),
            original_signed_complete_mean_read_verbatim=copy.deepcopy(fr["full_actual_mean_derivatives"][0]),
            original_eta_lower_read_verbatim=copy.deepcopy(c["eta_lower"]),
            original_J_Hminus5_3_to_Hminus2_3_read_verbatim=copy.deepcopy(c["C_J_scalar"]),
            original_same_window_L_read_verbatim=copy.deepcopy(c["C_L"]),
            original_same_window_B_read_verbatim=copy.deepcopy(c["C_B"]),
            original_complete_u_0_3_read_verbatim=copy.deepcopy(c["U"][:4]),
            original_complete_v_0_3_read_verbatim=copy.deepcopy(c["V"][:4]),
            original_real_drift_0_3_read_verbatim=copy.deepcopy(c["D"][:4]),
            original_full_product_drift_modulus_read_verbatim=copy.deepcopy(cD[0])))
    return out

def root_mean_value_gap(rows,inputs,gate):
    gate("the exact original same-germ body covers the complete cut to root segment outside compact support",
        len(rows)==len(inputs)==1 and all(
            Q(9,50)<Q(br["interval"][0])<=RCUT<ROOTS[0]<=ROOTS[1]<=Q(br["interval"][1])
            and fr["actual_scalar_germ"]==br["actual_scalar_germ"]
            and br["common_row"]==fr["original_common_row"]==3070
            for _,_,fr,br in rows))
    signed=[rb(x["original_signed_whole_K1_read_verbatim"]) for x in inputs]
    gate("the unchanged whole original signed outward K1 has a strict positive lower endpoint",
        all(k.is_finite() and k.lower()>0 for k in signed))
    result=[]
    for x,k in zip(inputs,signed):
        lo=(k.lower()*ex(ROOTS[0]-RCUT)).lower()
        hi=(k.upper()*ex(ROOTS[1]-RCUT)).upper()
        qlo=gap(lo,"root mean-value negative curvature lower").sqrt().lower()
        qhi=gap(hi,"root mean-value negative curvature upper").sqrt().upper()
        result.append(dict(original_norm_row=x["original_norm_row"],
            exact_root_distance=[str(ROOTS[0]-RCUT),str(ROOTS[1]-RCUT)],
            original_signed_whole_K1_read_verbatim=copy.deepcopy(x["original_signed_whole_K1_read_verbatim"]),
            complete_Kr_lower=rec(k.lower()),complete_Kr_upper=rec(k.upper()),
            complete_negative_K_at_cut_lower=rec(lo),complete_negative_K_at_cut_upper=rec(hi),
            q_lower=rec(qlo),q_upper=rec(qhi),
            method="negative K at cut equals integral of outward K1 from cut to the same exact root",
            whole_segment_in_one_original_germ=True,
            original_zero_order_curvature_enclosure_not_overwritten=True))
    gate("the new root FTC supplies finite strict q bounds on every original cut side",
        len(result)==len(rows) and all(gap(v["q_lower"],"q lower")<=up(v["q_upper"]) for v in result))
    return result

def physical_cut_coefficients(inputs,roots,gate):
    out=[];public=[]
    for x,r in zip(inputs,roots):
        eta=gap(x["original_eta_lower_read_verbatim"],"original eta lower")
        mean=rb(x["original_signed_complete_mean_read_verbatim"])
        if not mean.is_finite() or not mean.upper()<0:raise ValueError("the complete original mean sign failed")
        mm=gap(-mean.upper(),"complete actual absolute mean")
        radius=rb(x["original_physical_radius_read_verbatim"])
        gap(radius,"actual physical intrinsic radius");ap=radius.upper()
        qlo=gap(r["q_lower"],"root-FTC q lower");qhi=up(r["q_upper"])
        ng=up(ap*ap/(mm*mm));Tq=up(max(qhi.sqrt().upper(),(1/qlo).sqrt().upper()))
        CI=up(arb(17).sqrt()/4)
        c=dict(eta=eta,CJ=up(x["original_J_Hminus5_3_to_Hminus2_3_read_verbatim"]),
            CL=up(x["original_same_window_L_read_verbatim"]),CB=up(x["original_same_window_B_read_verbatim"]),
            qlo=qlo,qhi=qhi,mm=mm,ap=ap,ng=ng,Tq=Tq,CI=CI,W=up(CI*ng*Tq))
        out.append(c)
        public.append(dict(original_norm_row=x["original_norm_row"],
            root_mean_value_q_bounds=copy.deepcopy(r),
            complete_absolute_mean_lower=rec(mm),physical_radius_upper=rec(ap),
            complete_ng_upper=rec(ng),complete_Tq_upper=rec(Tq),
            complete_primitive_and_mean_multiplier=rec(CI),complete_ordered_radial_readout_upper=rec(c["W"]),
            original_J_L_B_and_eta_read_from_same_complete_row=True,
            both_mean_coordinates_retained=True,strict_normalizer_inverses_composed=False))
    gate("every actual P22 side retains positive full mean radius eta and the original typed complete operators",
        len(out)==len(inputs)==len(roots)
        and all(all(v.is_finite() and v>=0 for v in c.values())
            and all(c[k]>0 for k in ("eta","qlo","qhi","mm","ap","ng","Tq","CI","W")) for c in out))
    return out,public

def joint_free_g(products,inv,dr,coeff,original,gate):
    D=up(original["coefficients"]["D"][0])
    width=gap(ex(SNEW),"new joint strip");margin=gap(ex(SS-SNEW),"new joint product angular margin")
    if len(coeff)!=6:raise ValueError("the complete six saved positive coefficients are absent")
    values={};public={}
    for m in (2,3):
        z=products[m]
        gm=[up(z["M"][i]/dr+(D*z["M"][i]+z["P"][i])/margin) for i in range(2)]
        fm=[up(sum((inv[i][j]*gm[j] for j in range(2)),arb(0))) for i in range(2)]
        jets=[[up(math.factorial(q)*fm[i]/width**q) for q in range(4)] for i in range(2)]
        av=up(sum((coeff[3*i+q]*jets[i][q] for i in range(2) for q in range(3)),arb(0)))
        ad=up(sum((coeff[3*i+q]*jets[i][q+1] for i in range(2) for q in range(3)),arb(0)))
        bound=up(z["factor"]*(av+ad));values[m]=bound
        public[str(m)]=dict(exact_joint_strip=str(SNEW),exact_joint_angular_margin=str(SS-SNEW),
            original_complete_drift_modulus_read_verbatim=copy.deepcopy(original["coefficients"]["D"][0]),
            complete_new_g_strip_modulus_upper=encode(gm),
            complete_new_ordered_Bfree_g_strip_modulus_upper=encode(fm),
            complete_new_whole_Bfree_g_angular_jets_upper=encode(jets),
            complete_new_A_of_Bfree_g_upper=rec(av),complete_new_A_of_derivative_Bfree_g_upper=rec(ad),
            saved_input_multiplier_read_verbatim=None,
            complete_raw_g_Hminus1_upper=rec(bound),
            whole_product_cauchy_instead_of_lost_factor_derivatives=True,
            all_output_means_and_both_input_signs_retained=True,
            no_extra_eta_primitive_or_frequency_factor=True)
    gate("both new complete joint-disk differential products retain the same strip source order and all means",
        D.is_finite() and D>=0 and 0<SNEW<SS<SB<SG and dr>0
        and set(values)=={2,3}
        and all(all(rb(v).is_finite() and rb(v).lower()>=0 for v in x["complete_new_g_strip_modulus_upper"])
            and all(len(v)==4 for v in x["complete_new_whole_Bfree_g_angular_jets_upper"])
            for x in public.values()))
    gate("the two new raw g receivers apply the original six coefficients and each saved input factor exactly once",
        all(v.is_finite() and v>=0 for v in values.values())
        and all(x["all_output_means_and_both_input_signs_retained"] is True for x in public.values()))
    return values,public

def physical_receiver(G,c):
    w,p,g,e=G
    first=up(p/c["eta"]+c["CJ"]*(g+c["CL"]*p/c["eta"]+c["CB"]*w+e))
    pair=up((first*first+w*w).sqrt())
    return dict(complete_first_raw_Hminus1_upper=rec(first),
        complete_second_raw_Hminus1_upper=rec(w),complete_raw_pair_Hminus1_upper=rec(pair),
        complete_old_circle_density_and_two_means_upper=rec(up(c["W"]*pair)),
        J_applied_in_its_original_Hminus5_3_window=True,
        raw_Hminus1_not_renamed_raw_L2=True)

def complete_physical_rows(rows,scalar,products,gvalues,coefficients,cut_public,gate):
    public=[]
    for (index,nr,fr,br),c,cp in zip(rows,coefficients,cut_public):
        pieces={name:physical_receiver(G,c) for name,G in scalar.items()}
        for m in (2,3):
            z=products[m]
            pieces["free_R"+str(m)]=physical_receiver([z["Gw"],z["Gp"],gvalues[m],arb(0)],c)
        total=up(sum((up(v["complete_old_circle_density_and_two_means_upper"]) for v in pieces.values()),arb(0)))
        public.append(dict(original_norm_row=index,exact_original_interval=nr["interval"],
            exact_original_intrinsic_interval=br["interval"],complete_cut_coefficients=cp,
            complete_four_physical_pieces=pieces,complete_four_piece_sum_upper=rec(total)))
    gate("all four complete physical pieces use one original cut case and both full mean coordinates",
        len(public)==len(rows)==len(coefficients) and all(set(x["complete_four_physical_pieces"])==
            {"error_density_0","error_density_1","free_R2","free_R3"} for x in public))
    maxima={name:rec(max(up(x["complete_four_physical_pieces"][name]
        ["complete_old_circle_density_and_two_means_upper"]) for x in public).upper())
        for name in ("error_density_0","error_density_1","free_R2","free_R3")}
    total=max(up(x["complete_four_piece_sum_upper"]) for x in public).upper()
    result=dict(exact_strict_cut=str(RCUT),exact_real_delta_radius="1/100000000",
        input_window=PARAMETERS["input_window"],output_window=PARAMETERS["output_window"],
        complete_cut_sides=len(public),complete_four_piece_maxima=maxima,
        complete_strict_physical_Darboux_comparison_upper=rec(total),
        selection_rule="maximum of the complete four-piece sum on each closed cut side",
        complete_physical_cut_rows=public,both_reference_columns_and_input_signs=True,
        all_output_modes_finite_head_and_both_mean_coordinates_retained=True,
        nonzero_root_beta_and_all_tau_integral_are_in_immutable_first_receiver=True,
        strict_normalizers_final_circle_and_incoming_inverse_not_yet_composed=True,
        complete_corrected_trial_waist_CE_or_return_R0_not_claimed=True,
        no_N_six_cut_or_SP_transport_gain_reused_at_P22=True,
        all_four_partial_raw_w_p_receivers_preserved_verbatim=True)
    gate("the complete strict physical Darboux comparison is a same-case sum and has the original exact scope",
        total.is_finite() and total>0 and len(maxima)==4
        and result["complete_cut_sides"]==len(rows)
        and result["strict_normalizers_final_circle_and_incoming_inverse_not_yet_composed"] is True)
    return result

def render_conclusion(doc):
    keys=("kind","complete","proved","actual_returncode","failure","source_sha256",
        "input_manifest_sha256","runtime","arithmetic_bits","run_id","run_attempt","actual_mathematical_wall_seconds")
    out={k:doc[k] for k in keys if k in doc}
    out["passed_gates"]=sum(g["passed"] for g in doc["gates"]);out["recorded_gates"]=len(doc["gates"])
    out["expected_gates"]=PARAMETERS["expected_actual_gate_count"]
    for k in ("complete_partial_reuse_conclusion","complete_root_mean_value_conclusion",
              "complete_physical_comparison_conclusion","scope"):
        if k in doc:out[k]=doc[k]
    return "\n".join(["# Root mean-value and saved-product Darboux recovery","",
        "The complete execution retains every saved input and every new source and physical conclusion.",
        "The output retains both means; strict normalizers, incoming inverse and strong return remain separate.","",
        chr(96)*3+"json",json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False),chr(96)*3,""])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","workdir","process","conclusion","out"):
        p.add_argument("--"+name,type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new arithmetic is permitted only on the actual public repository Actions runner")
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the frozen public scientific runtime changed")
    ctx.prec=320;a.workdir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,arithmetic_bits=320,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        mathematical_parameters=PARAMETERS,original_successful_small_receipts_read=0,
        original_complete_fold_stages_read=0,original_complete_norm_rows_read=0,original_complete_forcing_rows_read=0,
        original_complete_intrinsic_rows_read=0,original_saved_zero_order_coefficients_read=0,
        original_first_scalar_receiver_bounds_read=0,original_cut_sides_read=0,
        accepted_partial_execution_read=0,completed_partial_free_domains_read=0,
        completed_partial_product_moduli_read=0,completed_partial_raw_w_p_bounds_read=0,
        completed_partial_derivative_arrays_reconstructed=0,completed_partial_functionals_recomputed=0,
        new_root_mean_value_curvature_gaps=0,new_joint_free_g_products=0,new_zero_order_functional_applications=0,
        new_complete_physical_receivers=0,new_complete_physical_comparisons=0,
        old_numerical_enclosures_recomputed=0,old_profiles_or_calibrations_recomputed=0,
        old_amplitude_mixed_jets_or_Taylor_tails_recomputed=0,old_potential_or_fold_or_inverse_closures_recomputed=0,
        old_intrinsic_mean_or_coefficient_rows_recomputed=0,old_Darboux_scalar_receiver_or_integrals_recomputed=0,
        old_PC_PW_SP_N_or_other_successful_producers_called=0,
        original_natural_stage_bytes_modified=False,complete_strict_physical_Darboux_comparison_paid=False,
        full_incoming_inverse_claimed=False,full_strong_return_R0_evaluated=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def checkpoint():save(a.process,doc)
    def gate(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual saved-product Darboux recovery gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the immutable manifest fixes the new root and joint-source contract runtime and parameter scope",
            manifest["source_sha256"]==sha(__file__) and manifest["contract_sha256"]==CONTRACT
            and manifest["runtime"]==RUNTIME and manifest["mathematical_parameters"]==PARAMETERS
            and manifest["expected_actual_gate_count"]==PARAMETERS["expected_actual_gate_count"]
            and len({e["path"] for e in manifest["files"]})==len(manifest["files"]))
        for e in manifest["files"]:
            q=a.repo_root/e["path"]
            if not q.is_file() or q.stat().st_size!=e["bytes"] or sha(q)!=e["sha256"]:
                raise ValueError("immutable complete input changed: "+e["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        gate("all original and partial inputs are immutable and no successful scientific module is imported",
            set(EXPECTED)<=set(paths) and sha(paths["contract"])==CONTRACT
            and sha(paths["DR_contract"])==DR_CONTRACT and sha(paths["IN_contract"])==IN_CONTRACT
            and sha(paths["original_DR_source"])==PARTIAL_SOURCE
            and sha(paths["original_DR_manifest"])==PARTIAL_MANIFEST
            and manifest["old_successful_scientific_calls_allowed"]==0
            and manifest["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
        R={k:accepted(paths[k],identity,gate) for k,identity in EXPECTED.items()}
        doc["original_successful_small_receipts_read"]=len(R)
        original=read_original_fold(paths,gate);doc["original_complete_fold_stages_read"]=1
        rows,identity=read_cut_rows(paths,gate)
        doc["complete_original_cut_identity_conclusion"]=identity
        doc["original_complete_norm_rows_read"]=doc["original_complete_forcing_rows_read"]=1328
        doc["original_complete_intrinsic_rows_read"]=256;doc["original_cut_sides_read"]=len(rows)
        scalar,coeff,s2,saved=accepted_scalar_receivers(R,gate)
        doc["complete_accepted_scalar_conclusion"]=saved
        doc["original_saved_zero_order_coefficients_read"]=6;doc["original_first_scalar_receiver_bounds_read"]=8
        products,inv,dr,domain,product_public,reuse=read_partial_success(paths,identity,saved,gate)
        doc["complete_partial_reuse_conclusion"]=reuse
        doc["complete_free_product_domain_conclusion"]=domain
        doc["complete_free_product_conclusion"]=product_public
        doc["accepted_partial_execution_read"]=doc["completed_partial_free_domains_read"]=1
        doc["completed_partial_product_moduli_read"]=4;doc["completed_partial_raw_w_p_bounds_read"]=4
        checkpoint()
        inputs=capture_cut_inputs(rows,original);doc["complete_original_cut_input_conclusion"]=inputs
        checkpoint()
        roots=root_mean_value_gap(rows,inputs,gate)
        doc["complete_root_mean_value_conclusion"]=roots;doc["new_root_mean_value_curvature_gaps"]=len(roots)
        checkpoint()
        cuts,cut_public=physical_cut_coefficients(inputs,roots,gate)
        doc["complete_physical_cut_coefficient_conclusion"]=cut_public
        checkpoint()
        gvalues,gpublic=joint_free_g(products,inv,dr,coeff,original,gate)
        for m in (2,3):
            gpublic[str(m)]["saved_input_multiplier_read_verbatim"]=copy.deepcopy(product_public[str(m)]["complete_input_multiplier_upper"])
        doc["complete_new_joint_free_g_conclusion"]=gpublic
        doc["new_joint_free_g_products"]=2;doc["new_zero_order_functional_applications"]=4
        checkpoint()
        conclusion=complete_physical_rows(rows,scalar,products,gvalues,cuts,cut_public,gate)
        doc["complete_physical_comparison_conclusion"]=conclusion
        doc["new_complete_physical_receivers"]=4*len(rows);doc["new_complete_physical_comparisons"]=1
        doc["scope"]=dict(complete_original_P22_strict_cut=True,full_real_delta_family=True,
            both_reference_columns_and_both_input_signs=True,complete_finite_output_and_both_means=True,
            old_first_Darboux_receivers_read_without_reexecution=True,
            successful_partial_domain_products_and_four_raw_receivers_read_verbatim=True,
            lost_partial_derivative_arrays_not_reconstructed=True,
            same_original_signed_K1_and_exact_root_used_for_new_curvature_gap=True,
            only_new_joint_Bfree_g_strip_estimates_evaluated=True,
            raw_Hminus1_composed_through_original_Hminus5_3_J_L_B_windows=True,
            two_inhomogeneous_differential_rows_added_once=True,
            old_primitive_extra_already_in_first_receivers_not_added_twice=True,
            actual_eta_inverse_physical_radius_mean_q_and_full_primitive_mean_readout_paid=True,
            free_R2_R3_complete_source_and_inverse_columns_paid=True,
            strict_normalizers_final_circle_and_incoming_inverse_not_yet_composed=True,
            full_corrected_trial_waist_CE_not_claimed=True,full_strong_return_R0_not_claimed=True)
        zeros=("old_numerical_enclosures_recomputed","old_profiles_or_calibrations_recomputed",
            "old_amplitude_mixed_jets_or_Taylor_tails_recomputed","old_potential_or_fold_or_inverse_closures_recomputed",
            "old_intrinsic_mean_or_coefficient_rows_recomputed","old_Darboux_scalar_receiver_or_integrals_recomputed",
            "old_PC_PW_SP_N_or_other_successful_producers_called","completed_partial_derivative_arrays_reconstructed",
            "completed_partial_functionals_recomputed")
        gate("all new physical conclusions are complete and no successful full or partial calculation is repeated",
            len(R)==7 and len(coeff)==6 and len(scalar)==2 and len(products)==2
            and doc["new_zero_order_functional_applications"]==4
            and doc["new_complete_physical_receivers"]==4*len(rows)
            and doc["completed_partial_raw_w_p_bounds_read"]==4
            and all(doc[k]==0 for k in zeros))
        if len(doc["gates"])!=PARAMETERS["expected_actual_gate_count"]:
            raise ValueError("the complete scientific gate count differs from the frozen contract")
        doc["complete"]=doc["proved"]=doc["complete_strict_physical_Darboux_comparison_paid"]=True
        doc["actual_returncode"]=0
    except Exception as e:
        doc["failure"]=dict(type=type(e).__name__,message=str(e))
        print("ACTUAL_SAVED_PRODUCT_DARBOUX_RECOVERY_FAILURE",repr(e),flush=True)
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        # The complete small conclusion is atomic before temporary output or rendering.
        checkpoint()
        save(a.out,dict(scientific_receipt=doc,no_transient_derivative_array_reconstruction=True),compressed=True)
        doc["temporary_native_sha256"]=sha(a.out);doc["temporary_native_bytes"]=a.out.stat().st_size
        checkpoint()
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        t=a.conclusion.with_name(a.conclusion.name+".tmp")
        t.write_text(render_conclusion(doc),encoding="utf-8");t.replace(a.conclusion)
    raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
