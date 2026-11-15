#!/usr/bin/env python3
"""Complete physical strict-cut Darboux receiver; immutable first scalar stage only read.

New mathematics is restricted to the two free amplitude products, their
complete derivative/inverse products, and the true P22 physical readout.
No successful old profile, calibration, intrinsic row, amplitude, potential,
first Darboux receiver, source integral or old solver is imported or called.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_complete_strict_physical_Darboux_receiver_v1"
CONTRACT="0e80f086565a78fc90a8ace9a79da274d76f5fd97e7c8685e870a4977c0d2a19"
IN_CONTRACT="d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
RCUT=Q(76285779072683,320000000000000)
H=Q(893368603925465506687,21990232555520000000000000)
RG=Q(3,8000);SG=Q(3,128);SB=Q(1,64);HI=Q(1,20000)
RS=Q(1,8000);SS=Q(3,512);N=388
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
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"cutoff_abs_j\":97,\"physical_frequency\":\"n=4|j|\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_real_delta_radius\":\"1/100000000\",\"exact_original_profile_cover\":\"893368603925465506687/21990232555520000000000000\",\"exact_original_fold_radius\":\"3/8000\",\"exact_original_fold_strip\":\"3/128\",\"exact_new_product_radius\":\"1/8000\",\"exact_new_product_strip\":\"3/512\",\"exact_original_free_inverse_radius\":\"1/20000\",\"exact_original_inverse_strip\":\"1/64\",\"original_common_row_part\":[3066,3322],\"original_complete_norm_rows\":1328,\"original_complete_forcing_rows\":1328,\"original_complete_intrinsic_part_rows\":256,\"input_window\":\"H^(-4/3), both reference columns and both signs |j|>=97\",\"output_window\":\"old-circle L2 density pair plus both mean coordinates\",\"original_J_window\":\"H^(-5/3) to H^(-2/3)\",\"same_order_L_B_window\":\"H^(-5/3) to H^(-5/3)\",\"old_scientific_producer_calls\":0,\"strict_normalizers_and_final_circle_not_yet_composed\":true,\"full_incoming_inverse_or_strong_return_claimed\":false}")

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
def pw(x,p):return (rb(x).log()*ex(p)).exp()
def rec(x):return dict(ball=rb(x).str(52))
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def add(*v,k=2):
    if not v or min(map(len,v))<=k:raise ValueError("missing complete angular derivative")
    return [up(sum((a[i] for a in v),arb(0))) for i in range(k+1)]
def scale(a,c):return [up(x*rb(c)) for x in a]
def mul(a,b,k=2):
    if min(len(a),len(b))<=k:raise ValueError("missing complete product derivative")
    return [up(sum((math.comb(q,j)*a[j]*b[q-j] for j in range(q+1)),arb(0))) for q in range(k+1)]
def product(*v,k=2):
    z=[arb(1)]+[arb(0)]*k
    for a in v:z=mul(z,a,k)
    return z
def vector(x,k):
    if len(x)!=2 or any(len(a)!=k+1 for a in x):raise ValueError("saved vector derivative order changed")
    return [[up(v) for v in a] for a in x]
def deriv(v):return [a[1:] for a in v]
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



def scalar_abs(v):
    a=rb(v)
    if not a.is_finite():raise ValueError("nonfinite original signed scalar")
    return abs(a).upper()

def cauchy_modulus(M,width,last):
    w=gap(ex(width),"new product angular width")
    return [up(math.factorial(k)*M/w**k) for k in range(last+1)]

def vder(v):return [a[1:] for a in v]
def vadd(*vs,k=3):return [add(*(v[i] for v in vs),k=k) for i in range(2)]
def mapply(M,v,k=3):
    return [add(*(mul(M[i][j],v[j],k=k) for j in range(2)),k=k) for i in range(2)]

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

def free_product_domain(R,original,gate):
    ref=R["refined_first_local_execution"]["complete_domain_conclusion"]
    wd=R["Taylor_execution"]["complete_domain_conclusion"]
    rv=R["accepted_RV_execution"]["complete_domain_conclusion"]
    sv=R["accepted_SV_execution"]["complete_exact_inverse_column_conclusion"]
    hi=R["columns_execution"]["old_circle_inverse"]
    h=Q(rv["exact_negative_rho_cover"]);rho0=ROOTS[0]-RCUT;rho1=ROOTS[1]-RCUT
    gate("the new free products restrict the immutable whole amplitude and leading products without rerunning a jet",
        Q(ref["exact_new_old_rho_radius"])==RS and Q(ref["exact_new_old_phi_strip"])==SS
        and Q(ref["exact_full_physical_cover"])==H and ref["all_sT_paths_in_same_paid_domain"] is True
        and ref["root_normalization_and_all_means_unchanged"] is True
        and ref["original_forcing_and_fold_recomputed"] is False
        and Q(wd["exact_whole_physical_piece_cover_radius"])==H
        and wd["same_complex_delta_and_z_squares"] is True
        and wd["same_reference_T_not_old_r_substituted"] is True
        and Q(sv["exact_negative_rho_cover"])==h
        and Q(sv["exact_original_fold_radius"])==RG and Q(sv["exact_original_fold_strip"])==SG
        and sv["same_full_complex_delta_and_old_angle_domains_retained"] is True
        and 0<rho0<=rho1<h<H<HI<RS<RG and 0<SS<SB<SG
        and len(wd["complete_Fuchsian_integral_T_derivative_modulus_upper"])==3)
    cases=[x for x in R["potential_execution"]["cases"] if x["exact_complex_radial_radius"]=="1/6000"]
    if len(cases)!=1:raise ValueError("the original common potential case is not unique")
    pot=cases[0];image=gap(pot["reference_image"]["complete_image_disk_radius_lower"],"whole original potential image")
    Ts=up(ref["complete_old_product_T_image_upper"])
    Th=up(rv["new_complete_negative_T_image_upper"])
    gate("both new product images stay inside the same accepted Fuchsian and potential parameter disk",
        pot["complete"] and pot["proved"] and pot["failure"] is None
        and pot["both_carrier_signs_retained"] and pot["whole_complex_bilinear_family"]
        and pot["exact_complex_delta_square_halfwidth"]=="1/100000000"
        and pot["exact_complex_z_square_halfwidth"]=="1/9409"
        and pot["fixed_intrinsic_parameter"]=="eta_0"
        and wd["original_potential_execution_sha256"]==EXPECTED["potential_execution"][3]
        and Q(pot["reference_image"]["old_fold_original_radius"])==RG
        and Q(pot["reference_image"]["old_fold_phi_width"])==SG
        and Ts<image and Th<image and Ts>0 and Th>0)
    gfree=gap(hi["complete_free_Bplus_modulus_lower"],"saved whole free Bplus")
    gate("the saved original free gap is consumed on its genuine full old-angle product",
        Q(hi["exact_old_rho_radius"])==HI and Q(hi["exact_inverse_phi_strip"])==SB
        and Q(hi["exact_original_fold_radius"])==RG and Q(hi["exact_original_fold_phi_strip"])==SG
        and Q(hi["exact_full_physical_root_cover"])==H
        and hi["full_physical_root_piece_covered"] is True and hi["full_mean_output_retained"] is True
        and hi["physical_primitive_projection_retained"] is True
        and hi["final_complex_old_circle_inverse_matrix_paid"] is True
        and hi["full_complex_angle_reference_column_norm_paid"] is False
        and hi["full_strong_return_or_high_BVP_inverse_paid"] is False
        and h<HI and Q(sv["exact_accepted_inverse_radius"])==HI
        and Q(sv["exact_accepted_inverse_strip"])==SB)
    f=original["fold"];maj=original["majorants"]
    a1=up(ref["complete_new_amplitude_modulus"]["a1"]);b1=up(ref["complete_new_amplitude_modulus"]["b1"])
    b0=up(maj["b0"][0]);q0=up(f["Q"])
    ell=[up(x) for x in wd["complete_Fuchsian_integral_T_derivative_modulus_upper"][:2]]
    x=up(sv["complete_X_angular_derivative_upper"][0]);y=up(sv["complete_Y_angular_derivative_upper"][0])
    dr=gap(ex(RS-rho1),"new free-product radial Cauchy margin")
    invmod=[[up(x/gfree),up(Th*y/gfree)],[up(y/gfree),up(x/gfree)]]
    invjets=[[cauchy_modulus(v,SB,3) for v in row] for row in invmod]
    gate("the new free inverse entries use saved full-strip zero orders and three new complete angular Cauchy derivatives",
        all(len(v)==4 and all(z.is_finite() and z>=0 for z in v) for row in invjets for v in row)
        and all(v.is_finite() and v>=0 for v in (a1,b1,b0,q0,x,y,*ell))
        and dr>0 and gfree>0)
    data=dict(a1=a1,b1=b1,b0=b0,Q=q0,ell=ell,Ts=Ts,Th=Th,dr=dr,invjets=invjets)
    out=dict(exact_strict_cut=str(RCUT),exact_true_rho_interval=[str(rho0),str(rho1)],
        exact_reused_product_radius=str(RS),exact_reused_product_strip=str(SS),
        exact_reused_free_inverse_radius=str(HI),exact_reused_free_inverse_strip=str(SB),
        complete_new_product_radial_margin_lower=rec(dr),
        complete_product_T_modulus_read_verbatim=copy.deepcopy(ref["complete_old_product_T_image_upper"]),
        complete_inverse_numerator_T_modulus_read_verbatim=copy.deepcopy(rv["new_complete_negative_T_image_upper"]),
        complete_free_Bplus_lower_read_verbatim=copy.deepcopy(hi["complete_free_Bplus_modulus_lower"]),
        complete_Fuchsian_0_1_read_verbatim=copy.deepcopy(wd["complete_Fuchsian_integral_T_derivative_modulus_upper"][:2]),
        complete_amplitude_moduli_read_verbatim=copy.deepcopy(ref["complete_new_amplitude_modulus"]),
        complete_original_leading_b0_modulus_read=copy.deepcopy(maj["b0"][0]),
        complete_original_Q_modulus_read=copy.deepcopy(f["Q"]),
        complete_free_inverse_entry_modulus_upper=encode(invmod),
        complete_new_free_inverse_angular_jets_sha256=payload_sha(encode(invjets)),
        no_deformed_gap_compared_to_free_determinant=True,
        no_real_angle_positive_derivative_promoted_to_strip_modulus=True,
        original_amplitude_jets_and_all_mean_factors_unchanged=True,
        original_successful_product_and_inverse_closures_recomputed=False)
    return data,out

class SavedZeroFunctional:
    def __init__(self,coeff):
        if len(coeff)!=6:raise ValueError("six complete saved zero-order coefficients are required")
        self.coeff=coeff;self.applications=0
    def value(self,v):
        if len(v)!=2 or min(map(len,v))<3:raise ValueError("missing complete free angular triple")
        self.applications+=1;inp=v[0][:3]+v[1][:3]
        return up(sum((a*b for a,b in zip(self.coeff,inp)),arb(0)))
    def plus(self,v):return up(self.value(v)+self.value(vder(v)))

def new_free_products(d,A,s2,gate):
    e0,e1=d["ell"];Ts=d["Ts"]
    mod={2:[up(e0*Ts*d["b1"]),up(e0*d["a1"]+e1*d["b0"])],
         3:[arb(0),up(e1*d["b1"])]}
    out={};saved={}
    for m in (2,3):
        M=mod[m];pm=[up(d["Q"]*Ts*M[1]),up(d["Q"]*M[0])]
        w=[cauchy_modulus(x,SS,4) for x in M]
        wr=[[up(z/d["dr"]) for z in row[:4]] for row in w]
        p=[cauchy_modulus(x,SS,4) for x in pm]
        Bw=mapply(d["invjets"],w);Bp=mapply(d["invjets"],p)
        factor=s2 if m==2 else up(s2/N)
        gw=up(factor*A.plus(Bw));gp=up(factor*A.plus(Bp))
        out[m]=dict(w=w,wr=wr,p=p,factor=factor,Gw=gw,Gp=gp,Bw=Bw,Bp=Bp)
        saved[str(m)]=dict(complete_amplitude_product_modulus_upper=encode(M),
            complete_free_p_product_modulus_upper=encode(pm),complete_input_multiplier_upper=rec(factor),
            complete_raw_w_Hminus1_upper=rec(gw),complete_raw_p_Hminus1_upper=rec(gp),
            exact_free_p="-i*epsilon*Q*K*R"+str(m),
            exact_remaining_input_frequency_weight="1/n^"+str(m),
            original_density_normalization="n^(7/6)",
            complete_angular_orders_R_and_p=4,complete_mixed_r_phi_orders=3,
            complete_new_derivative_arrays_sha256=payload_sha(encode(dict(w=w,wr=wr,p=p,Bw=Bw,Bp=Bp))),
            complete_all_output_means_retained=True)
    gate("both new free products retain the exact R2 R3 entries and every fourth angular derivative",
        set(out)=={2,3} and A.applications==8
        and all(len(v)==2 and all(len(x)==5 for x in v) for z in out.values() for v in (z["w"],z["p"]))
        and all(len(x)==4 for z in out.values() for x in z["wr"])
        and all(z["factor"]>0 and z["Gw"]>=0 and z["Gp"]>=0 for z in out.values())
        and mod[3][0]==0)
    return out,saved

def cut_coefficients(nr,fr,br):
    c=nr["bounds"];km=-rb(fr["complete_intrinsic_ordinary_jets"]["K"][0])
    qlo=gap(km.lower(),"strict negative K").sqrt().lower()
    qhi=gap(km.upper(),"strict negative K upper").sqrt().upper()
    eta=gap(c["eta_lower"],"original eta lower")
    mean=rb(fr["full_actual_mean_derivatives"][0])
    if not mean.is_finite() or not mean.upper()<0:raise ValueError("the complete original mean sign failed")
    mm=gap(-mean.upper(),"complete actual absolute mean")
    radius=rb(br["intrinsic_whole_third_jets"]["a"])
    gap(radius,"actual physical intrinsic radius");ap=radius.upper()
    ng=up(ap*ap/(mm*mm));Tq=up(max(qhi.sqrt().upper(),(1/qlo).sqrt().upper()))
    CI=up(arb(17).sqrt()/4)
    numbers=dict(eta=eta,CJ=up(c["C_J_scalar"]),CL=up(c["C_L"]),CB=up(c["C_B"]),
        qlo=qlo,qhi=qhi,mm=mm,ap=ap,ng=ng,Tq=Tq,CI=CI,W=up(CI*ng*Tq))
    D=[up(x) for x in c["D"][:4]]
    if len(D)!=4:raise ValueError("the old complete drift lacks angular order three")
    public=dict(original_eta_lower_read_verbatim=copy.deepcopy(c["eta_lower"]),
        original_J_Hminus5_3_to_Hminus2_3_read_verbatim=copy.deepcopy(c["C_J_scalar"]),
        original_same_window_L_read_verbatim=copy.deepcopy(c["C_L"]),
        original_same_window_B_read_verbatim=copy.deepcopy(c["C_B"]),
        original_signed_K_read_verbatim=copy.deepcopy(fr["complete_intrinsic_ordinary_jets"]["K"][0]),
        original_signed_complete_mean_read_verbatim=copy.deepcopy(fr["full_actual_mean_derivatives"][0]),
        original_physical_radius_read_verbatim=copy.deepcopy(br["intrinsic_whole_third_jets"]["a"]),
        q_lower=rec(qlo),q_upper=rec(qhi),complete_absolute_mean_lower=rec(mm),
        physical_radius_upper=rec(ap),complete_ng_upper=rec(ng),complete_Tq_upper=rec(Tq),
        complete_primitive_and_mean_multiplier=rec(CI),complete_ordered_radial_readout_upper=rec(numbers["W"]),
        original_drift_0_3_payload_sha256=payload_sha(c["D"][:4]),
        both_mean_coordinates_retained=True,strict_normalizer_inverses_composed=False)
    return numbers,D,public

def physical_receiver(G,c):
    w,p,g,e=G
    first=up(p/c["eta"]+c["CJ"]*(g+c["CL"]*p/c["eta"]+c["CB"]*w+e))
    pair=up((first*first+w*w).sqrt())
    return dict(complete_first_raw_Hminus1_upper=rec(first),
        complete_second_raw_Hminus1_upper=rec(w),complete_raw_pair_Hminus1_upper=rec(pair),
        complete_old_circle_density_and_two_means_upper=rec(up(c["W"]*pair)),
        J_applied_in_its_original_Hminus5_3_window=True,
        raw_Hminus1_not_renamed_raw_L2=True)

def complete_free_g(z,D,d,A):
    # g=R_r-d R_phi-p_phi, with every complete derivative and no sign loss
    # until the positive majorant of this exact ordered identity is formed.
    g=[[up(z["wr"][i][k]+sum((math.comb(k,l)*D[l]*z["w"][i][k-l+1]
        for l in range(k+1)),arb(0))+z["p"][i][k+1]) for k in range(4)] for i in range(2)]
    Bg=mapply(d["invjets"],g)
    bound=up(z["factor"]*A.plus(Bg))
    return bound,dict(complete_free_g_angular_jets=g,complete_free_Bg_angular_jets=Bg)

def complete_physical_rows(rows,Rcv,products,d,A,gate):
    public=[];audit=[];counts=0
    for index,nr,fr,br in rows:
        c,D,cp=cut_coefficients(nr,fr,br)
        pieces={name:physical_receiver(G,c) for name,G in Rcv.items()}
        ng={}
        for m in (2,3):
            gg,extra=complete_free_g(products[m],D,d,A)
            pieces["free_R"+str(m)]=physical_receiver([products[m]["Gw"],products[m]["Gp"],gg,arb(0)],c)
            ng[str(m)]=rec(gg);audit.append(dict(original_norm_row=index,free_order=m,**encode(extra)))
        total=up(sum((up(v["complete_old_circle_density_and_two_means_upper"]) for v in pieces.values()),arb(0)))
        public.append(dict(original_norm_row=index,exact_original_interval=nr["interval"],
            exact_original_intrinsic_interval=br["interval"],complete_cut_coefficients=cp,
            complete_new_free_g_Hminus1_upper=ng,complete_four_physical_pieces=pieces,
            complete_four_piece_sum_upper=rec(total)))
        counts+=4
    gate("every actual P22 side keeps positive physical geometry and the complete original typed J L B mean rows",
        1<=len(public)<=2 and all(set(x["complete_four_physical_pieces"])==
            {"error_density_0","error_density_1","free_R2","free_R3"} for x in public))
    gate("all six free scalar receivers and four physical pieces per side are complete with no extra frequency fee",
        A.applications==8+4*len(rows) and counts==4*len(rows)
        and len(audit)==2*len(rows)
        and all(len(v)==4 for a in audit for v in a["complete_free_g_angular_jets"]))
    maxima={name:rec(max(up(x["complete_four_physical_pieces"][name]
        ["complete_old_circle_density_and_two_means_upper"]) for x in public).upper())
        for name in ("error_density_0","error_density_1","free_R2","free_R3")}
    # The maximum is taken after all four complete same-row pieces are summed.
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
        no_N_six_cut_or_SP_transport_gain_reused_at_P22=True)
    gate("the complete strict old-circle Darboux comparison contains all four same-row contributions and both means",
        total.is_finite() and total>0 and len(maxima)==4
        and result["complete_cut_sides"]==len(rows)
        and result["strict_normalizers_final_circle_and_incoming_inverse_not_yet_composed"] is True)
    return result,audit

def render_conclusion(doc):
    keys=("kind","complete","proved","actual_returncode","failure","source_sha256",
          "input_manifest_sha256","runtime","arithmetic_bits","run_id","run_attempt","actual_mathematical_wall_seconds")
    out={k:doc[k] for k in keys if k in doc}
    out["passed_gates"]=sum(g["passed"] for g in doc["gates"]);out["total_gates"]=len(doc["gates"])
    for k in ("mathematical_parameters","complete_original_cut_identity_conclusion",
            "complete_accepted_scalar_conclusion","complete_free_product_domain_conclusion",
            "complete_free_product_conclusion","complete_physical_comparison_conclusion","scope"):
        if k in doc:out[k]=doc[k]
    return "\n".join(["# Complete strict physical Darboux receiver","",
        "The output is the full old-circle density pair and both mean coordinates at the original P22 cut.",
        "The strict normalizers, circle change, incoming inverse and complete return remain separate.","",
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
        new_free_amplitude_products=0,new_free_p_products=0,new_free_inverse_entry_angular_budgets=0,
        new_free_scalar_receiver_bounds=0,new_free_g_products=0,new_zero_order_functional_applications=0,
        new_complete_physical_receivers=0,new_complete_physical_comparisons=0,
        old_numerical_enclosures_recomputed=0,old_profiles_or_calibrations_recomputed=0,
        old_amplitude_mixed_jets_or_Taylor_tails_recomputed=0,old_potential_or_fold_or_inverse_closures_recomputed=0,
        old_intrinsic_mean_or_coefficient_rows_recomputed=0,old_Darboux_scalar_receiver_or_integrals_recomputed=0,
        old_PC_PW_SP_N_or_other_successful_producers_called=0,
        original_natural_stage_bytes_modified=False,complete_strict_physical_Darboux_comparison_paid=False,
        full_incoming_inverse_claimed=False,full_strong_return_R0_evaluated=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    temporary={}
    def gate(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual complete physical Darboux receiver gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the immutable manifest fixes the new scalar source contract runtime and complete physical parameter scope",
            manifest["source_sha256"]==sha(__file__) and manifest["contract_sha256"]==CONTRACT
            and manifest["runtime"]==RUNTIME and manifest["mathematical_parameters"]==PARAMETERS
            and len({e["path"] for e in manifest["files"]})==len(manifest["files"]))
        for e in manifest["files"]:
            q=a.repo_root/e["path"]
            if not q.is_file() or sha(q)!=e["sha256"]:
                raise ValueError("immutable complete input changed: "+e["path"])
            if e["bytes"] is not None:
                if q.stat().st_size!=e["bytes"]:raise ValueError("immutable input byte count changed")
            elif (e["path"]!=manifest["input_paths"]["original_intrinsic_part"]
                or e["sha256"]!=PART_SHA or e.get("maximum_bytes")!=20000000
                or e.get("prior_receipt_did_not_store_member_bytes") is not True
                or not 0<q.stat().st_size<=e["maximum_bytes"]):
                raise ValueError("only the exact original SHA-pinned intrinsic member lacks a prior byte count")
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        gate("all original current history and archive inputs are immutable and no old scientific module is imported",
            set(EXPECTED)<=set(paths) and sha(paths["contract"])==CONTRACT
            and sha(paths["IN_contract"])==IN_CONTRACT
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
        d,domain=free_product_domain(R,original,gate);doc["complete_free_product_domain_conclusion"]=domain
        A=SavedZeroFunctional(coeff);products,pub=new_free_products(d,A,s2,gate)
        doc["complete_free_product_conclusion"]=pub
        doc["new_free_amplitude_products"]=2;doc["new_free_p_products"]=2
        doc["new_free_inverse_entry_angular_budgets"]=16
        conclusion,audit=complete_physical_rows(rows,scalar,products,d,A,gate)
        doc["complete_physical_comparison_conclusion"]=conclusion
        doc["new_free_scalar_receiver_bounds"]=4+2*len(rows)
        doc["new_free_g_products"]=2*len(rows);doc["new_zero_order_functional_applications"]=A.applications
        doc["new_complete_physical_receivers"]=4*len(rows);doc["new_complete_physical_comparisons"]=1
        doc["scope"]=dict(complete_original_P22_strict_cut=True,full_real_delta_family=True,
            both_reference_columns_and_both_input_signs=True,complete_finite_output_and_both_means=True,
            old_first_Darboux_receivers_read_without_reexecution=True,
            old_free_Bplus_lower_read_without_new_gap_calculation=True,
            only_new_R2_R3_product_derivatives_evaluated=True,
            raw_Hminus1_composed_through_original_Hminus5_3_J_L_B_windows=True,
            two_inhomogeneous_differential_rows_added_once=True,
            old_primitive_extra_already_in_first_receivers_not_added_twice=True,
            actual_eta_inverse_physical_radius_mean_q_and_full_primitive_mean_readout_paid=True,
            free_R2_R3_complete_source_and_inverse_columns_paid=True,
            strict_normalizers_final_circle_and_incoming_inverse_not_yet_composed=True,
            full_corrected_trial_waist_CE_not_claimed=True,full_strong_return_R0_not_claimed=True)
        gate("all new physical conclusions are complete and every old successful producer remains unused",
            len(R)==7 and len(coeff)==6 and len(scalar)==2 and len(products)==2
            and doc["new_zero_order_functional_applications"]==8+4*len(rows)
            and doc["new_complete_physical_receivers"]==4*len(rows)
            and doc["new_free_scalar_receiver_bounds"]==4+2*len(rows)
            and all(doc[k]==0 for k in ("old_numerical_enclosures_recomputed","old_profiles_or_calibrations_recomputed",
                "old_amplitude_mixed_jets_or_Taylor_tails_recomputed","old_potential_or_fold_or_inverse_closures_recomputed",
                "old_intrinsic_mean_or_coefficient_rows_recomputed","old_Darboux_scalar_receiver_or_integrals_recomputed",
                "old_PC_PW_SP_N_or_other_successful_producers_called")))
        temporary=dict(new_domain=encode(d),new_free_products=encode(products),complete_cut_free_g_audit=audit)
        doc["complete"]=doc["proved"]=doc["complete_strict_physical_Darboux_comparison_paid"]=True
        doc["actual_returncode"]=0
    except Exception as e:
        doc["failure"]=dict(type=type(e).__name__,message=str(e))
        print("ACTUAL_COMPLETE_PHYSICAL_DARBOUX_FAILURE",repr(e),flush=True)
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        save(a.out,dict(scientific_receipt=doc,temporary_new_derivative_audit=temporary),compressed=True)
        doc["temporary_native_sha256"]=sha(a.out);doc["temporary_native_bytes"]=a.out.stat().st_size
        # The complete small science exists before any rendering or publication.
        save(a.process,doc)
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        t=a.conclusion.with_name(a.conclusion.name+".tmp")
        t.write_text(render_conclusion(doc),encoding="utf-8");t.replace(a.conclusion)
    raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
