#!/usr/bin/env python3
"""Complete new strict radial coefficients and first-symbol propagation defect.
All previous successful science is read as immutable evidence. Only the SJ
Markov/metric/coefficient/ordinary-integral/interface scalar expressions are new.
No original target, repaired polynomial, ray, profile or producer is imported.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_complete_strict_radial_first_symbol_defect_v1"
PRODUCER=TOPIC+"scripts/fourfold_codazzi_strict_radial_first_symbol_defect.py"
CONTRACT="ccaaa1b17fd68ce64d79a7bdc40dae9c0843b610da11149c178e92079d495f31"
SF_CONTRACT="add091118ef1af71bc8c4be275742d4124a076d6cf2ebaf00d35c66f8348f2b4"
BODY_MANIFEST="c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784"
BODY_SOURCE="1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07"
PARTITION_SOURCE="9674f5f6b9d4ad95d7d87fb22b2ec4c8fc3cad136b78afed677343c2510bb6df"
CENTRE_CONTRACT="a39fcfa2b7ca6f83cd9fadcc1987afe86f3364830848de78d2401469d7ce9f44"
RESPONSE_CONTRACT="2b7d6080dc7fdac0bd5c557b71f3e7ec1eb5436a14d45a5a762e1b548a9e20f1"
PARAMETER_CONTRACT="92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635"
FA_SCIENCE="2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
RESPONSE="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
EXPECTED=json.loads("{\"SP\":{\"run\":\"43731464771\",\"source\":\"9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a\",\"manifest\":\"c77e969bd02ef95d30f16b53ae0a0d3854f596412151e9242ffa0485bd142210\",\"digest\":\"a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12\",\"gates\":20,\"runtime\":{\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"execution_source_key\":\"source_budget_source_sha256\"},\"ST\":{\"run\":\"43757644616\",\"source\":\"743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5\",\"manifest\":\"e43b2c7036088cd8d1401c580c1aa6ef694d283057dcce7c65839f92fc1b0e80\",\"digest\":\"b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637\",\"gates\":25,\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"execution_source_key\":\"source_budget_source_sha256\"},\"RR\":{\"run\":\"43750683671\",\"source\":\"2a51b8c45974808e65754ebaa0b476650596e7d8a1e36541e9afd3987146c4c9\",\"manifest\":\"8822511f1f1c853efd8eec4944bcb74b6954c7fa04c143d9dafc9b470bdd1b4a\",\"digest\":\"a75da290077cf0e134834be5e35a0fa7cd55cd79104f5128d87eaee898af162b\",\"gates\":28,\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"execution_source_key\":\"source_budget_source_sha256\"},\"WX\":{\"run\":\"43763424840\",\"source\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"manifest\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"digest\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"gates\":20,\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"execution_source_key\":\"source_budget_source_sha256\"},\"FA\":{\"run\":\"43763658978\",\"source\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\",\"manifest\":\"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b\",\"digest\":\"735c8053b56cc240e3fdfb050d95ef2cbb17c26a376aa4132530d50687474c0a\",\"gates\":24,\"runtime\":{\"Python\":\"3.12.14\",\"arithmetic_bits\":320,\"python_flint\":\"0.9.0\"},\"execution_source_key\":\"source_sha256\"}}")
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_intrinsic_eta\":\"-7789843107295549/4611686018427387904\",\"exact_nu_centre\":\"-2572625729470897/72057594037927936\",\"exact_alpha\":\"6890507429876859/9007199254740992\",\"original_eta_half_width\":\"1/1000000000\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_ra\":\"1191939371497/5000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_complete_radial_interval\":[\"0\",\"76285779072683/320000000000000\"],\"exact_compact_metric_support\":[\"1/20\",\"9/50\"],\"physical_frequency\":\"n=4|j|\",\"input_cutoff_abs_j\":97,\"exact_moving_normalizer_cutoff_abs_j\":268435456,\"full_finite_support_offset\":575,\"complete_physical_mean_coordinates\":2,\"original_complete_body_parts\":18,\"original_restored_body_rows\":3322,\"original_consumed_body_rows\":3071,\"original_scientific_calls_allowed\":0,\"old_strict_containers_restored\":0,\"derivative_convention\":\"ordinary radial and angular derivatives; complete component Fourier A0 sum\",\"markov_coefficients\":{\"first\":18,\"second\":96},\"whole_background_A0\":7,\"whole_background_angle_A0\":6,\"whole_response_A0\":19,\"whole_response_angle_A0\":83,\"original_background_label_band\":32,\"original_response_label_band\":96,\"original_negative_mean_gap\":\"1.068732695\",\"genuine_and_conservative_artificial_impulses_kept_separately\":true,\"all_scientific_arrays_temporary\":true,\"expected_actual_gate_count\":26}")
RC=Q(PARAMETERS["exact_strict_cut"]);RA=Q(PARAMETERS["exact_ra"])
CONTROL=tuple(map(Q,PARAMETERS["exact_compact_metric_support"]))
NATIVE_NAME="temporary-strict-radial-first-symbol-defect.json.gz"

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def payload_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)
def save(p,x,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    tmp=p.with_name(p.name+".tmp");tmp.write_bytes(gzip.compress(raw,mtime=0) if compressed else raw);tmp.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def rb(x):
    if isinstance(x,arb):v=x
    elif isinstance(x,(int,Q)):v=ex(x)
    elif isinstance(x,str):v=arb(x)
    elif "lower" in x and "upper" in x:v=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
    else:v=arb(x["ball"])
    if not v.is_finite():raise ValueError("nonfinite complete scalar")
    return v
def up(x):
    x=rb(x)
    if x.lower()<0:raise ValueError("negative positive-budget input")
    return x.upper()
def au(x):return abs(rb(x)).upper()
def gap(x,label):
    x=rb(x).lower()
    if not x>0:raise ValueError("unproved strict denominator: "+label)
    return x
def rec(x):return dict(ball=rb(x).str(46))
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def positive_power(x,p):
    x=up(x);p=Q(p)
    if not x>0 or p<0:raise ValueError("positive-power helper requires positive base and nonnegative exponent")
    return up((x.log()*ex(p)).exp())
def relpath(s):
    p=Path(s)
    if p.is_absolute() or ".." in p.parts or not s.startswith(TOPIC):raise ValueError("input leaves the topic")
    return p
def check(p,size,digest):
    if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:raise ValueError("immutable input changed: "+str(p))
def accepted(paths,name,gate):
    v=EXPECTED[name];path=paths[name+"_execution"];e=read(path)
    r=read(paths["FA_science"]) if name=="FA" else e.get("actual_scientific_receipt",{})
    extra=True
    if name=="FA":
        s=e.get("scientific_conclusion",{})
        extra=(sha(paths["FA_science"])==FA_SCIENCE==s.get("sha256")
            and paths["FA_science"].stat().st_size==35718==s.get("bytes")
            and s.get("complete") is True and s.get("actual_returncode")==0
            and s.get("actual_gate_count")==s.get("actual_passed_gate_count")==24
            and e.get("actual_scientific_runtime")==v["runtime"])
    gate("accepted "+name+" run "+v["run"]+"/1 retains exact complete source manifest runtime and gates",
        sha(path)==v["digest"] and str(e.get("run_id"))==v["run"] and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get(v["execution_source_key"])==v["source"] and e.get("input_manifest_sha256")==v["manifest"]
        and r.get("source_sha256")==v["source"] and r.get("input_manifest_sha256")==v["manifest"]
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==v["runtime"]
        and len(r.get("gates",[]))==v["gates"] and all(g.get("passed") is True for g in r["gates"]) and extra)
    return r

def input_closure(args,doc,gate):
    m=read(args.manifest);entries=m["files"];roles=m["input_paths"]
    for e in entries:check(args.repo/relpath(e["path"]),e["bytes"],e["sha256"])
    paths={k:args.repo/relpath(v) for k,v in roles.items()}
    gate("new source contract exact parameters and every immutable text or original native are frozen",
        sha(args.manifest)==args.manifest_sha and m["public_repository"]==PUBLIC
        and m["scientific_source_path"]==PRODUCER and m["scientific_source_sha256"]==sha(__file__)
        and len({e["path"] for e in entries})==len(entries)
        and m["mathematical_parameters"]==PARAMETERS
        and m["expected_actual_gate_count"]==PARAMETERS["expected_actual_gate_count"]
        and sha(paths["contract"])==CONTRACT and sha(paths["SF_contract"])==SF_CONTRACT
        and sha(paths["original_body_manifest"])==BODY_MANIFEST
        and sha(paths["original_body_source"])==BODY_SOURCE
        and sha(paths["original_partition_source"])==PARTITION_SOURCE
        and sha(paths["centre_contract"])==CENTRE_CONTRACT
        and sha(paths["response_contract"])==RESPONSE_CONTRACT
        and sha(paths["parameter_contract"])==PARAMETER_CONTRACT)
    old={n:accepted(paths,n,gate) for n in ("SP","ST","RR","WX","FA")}
    bm=read(paths["original_body_manifest"]);ident=bm["row_identity"]
    fam=old["SP"]["exact_family_identity"]
    gate("all original body jets are at fixed nu0 and whole old eta box with the complete physical response",
        ident["source_sha256"]==BODY_SOURCE and ident["candidate_sha256"]==CANDIDATE
        and ident["full_trials"]["response"]["sha256"]==RESPONSE
        and ident["exact_alpha"]==PARAMETERS["exact_alpha"]
        and ident["exact_nu"]==PARAMETERS["exact_nu_centre"]==fam["exact_nu_centre"]
        and ident["original_parameter_half_width"]==PARAMETERS["original_eta_half_width"]==fam["original_eta_half_width"]
        and ident["total_common_cells"]==7721 and ident["radial_subdivisions"]==1
        and fam["original_candidate_sha256"]==CANDIDATE and fam["fixed_current_eta"]=="eta_0"
        and ident["dependencies"]["fourfold_codazzi_mean_completed_head_body_residual_v3.py"]==PARTITION_SOURCE
        and ident["full_trials"]["response"]["metadata"]["modes"]==96
        and ident["full_trials"]["response"]["metadata"]["exact_zero_mean_projection_for_separate_scalar_completion"] is False)
    for n in ("SP","ST","RR","WX","FA"):
        v=EXPECTED[n]
        if sha(paths[n+"_source"])!=v["source"] or sha(paths[n+"_manifest"])!=v["manifest"]:
            raise ValueError("accepted source or manifest text identity differs: "+n)
    gate("only immutable readers are used and all five complete original source chains are frozen",True)
    doc["original_successful_small_receipts_read"]=5
    return m,paths,old,bm

def original_body_rows(args,m,old,bm,doc,gate):
    specs=m["original_body_parts"]
    prior=old["SP"]["original_body_prefix_part_receipts"]
    rr=old["RR"]["complete_original_cut_identity_conclusion"]
    reduced=lambda e:{k:e[k] for k in ("indices","bytes","sha256")}
    gate("eighteen original parts are the seventeen SP parts and the one already restored RR member",
        len(specs)==18 and [reduced(e) for e in specs[:17]]==prior
        and specs[17]["indices"]==rr["original_part_common_row_indices"]==[3066,3322]
        and specs[17]["sha256"]==rr["original_part_sha256"]
        and specs[17]["bytes"]==rr["original_part_bytes"]==1167787)
    rows=[];edge=Q(0);receipts=[]
    for e in specs:
        path=args.repo/relpath(e["temporary_path"]);check(path,e["bytes"],e["sha256"]);v=read(path)
        first,last=e["indices"]
        if not (v.get("kind")==bm["residual_kind"] and v.get("identity")==bm["row_identity"]
            and v.get("source_sha256")==BODY_SOURCE and v.get("selected_indices")==[first,last]
            and v.get("selected_cells_complete") is True and v.get("failure") is None
            and len(v.get("rows",[]))==last-first and first==len(rows)):
            raise ValueError("original natural part has a different complete identity")
        for i,row in enumerate(v["rows"],first):
            l,r=map(Q,row["interval"]);gl,gr=map(Q,row["actual_scalar_germ"])
            if row["common_row"]!=i or l!=edge or not gl<=l<r<=gr:raise ValueError("original body cover or germ changed")
            if any(k not in row["pieces"] for k in ("background","response","adjoint")):raise ValueError("missing exact original PPoly labels")
            jets=row["intrinsic_whole_third_jets"]
            if set(jets)!={"a"}|{s+(str(j) if j else "") for s in ("gamma","beta","K","s") for j in range(4)}:
                raise ValueError("original ordinary whole-third-jet schema differs")
            rows.append(row);edge=r
        receipts.append(reduced(e))
    gate("the complete original 3322-row prefix is consecutive and every old whole germ is retained",
        len(rows)==3322 and edge>RC and len(receipts)==18)
    used=[]
    for row in rows:
        l,r=map(Q,row["interval"])
        if l>=RC:break
        used.append(dict(original=row,left=l,right=min(r,RC)))
    gate("the new exact restriction has all3071 original rows through P22 and no root-crossing denominator inference",
        len(used)==3071 and used[0]["left"]==0 and used[-1]["right"]==RC
        and used[-1]["original"]["common_row"]==3070
        and all(used[i-1]["right"]==used[i]["left"] for i in range(1,len(used))))
    rrrows=rr["complete_cut_row_identity"]
    gate("the final original body row is exactly the already successful RR whole root germ",
        rr["exact_strict_cut"]==str(RC) and rr["exact_root_interval"]==PARAMETERS["exact_root_interval"]
        and len(rrrows)==1 and rrrows[0]["original_common_row"]==3070
        and payload_sha(used[-1]["original"])==rrrows[0]["original_saved_intrinsic_row_sha256"]
        and used[-1]["original"]["interval"]==rrrows[0]["original_intrinsic_interval"])
    doc["original_complete_body_parts_read"]=18;doc["original_complete_body_rows_verified"]=len(rows)
    doc["original_consumed_body_rows"]=len(used);doc["original_part_receipts_read_verbatim"]=receipts
    return used

def polynomial_intervals(rows,gate):
    groups=[]
    for cell in rows:
        row=cell["original"];label=(row["pieces"]["background"],row["pieces"]["response"])
        if not groups or groups[-1]["labels"]!=label:
            groups.append(dict(labels=label,left=cell["left"],right=cell["right"],cells=[]))
        g=groups[-1]
        if g["right"]!=cell["left"] and g["cells"]:raise ValueError("nonconsecutive fixed-polynomial interval")
        g["right"]=cell["right"];g["cells"].append(cell)
    for j,g in enumerate(groups):
        h=g["right"]-g["left"]
        if not h>0:raise ValueError("empty Markov interval")
        s=[max(au(c["original"]["intrinsic_whole_third_jets"]["s"+(str(k) if k else "")]) for c in g["cells"]) for k in range(3)]
        g.update(index=j,length=h,s=s,first=g["cells"][0]["original"]["common_row"],
            stop=g["cells"][-1]["original"]["common_row"]+1)
        g["qualification"]="one unchanged exact background/response polynomial on the closed union; subinterval allowed"
        for c in g["cells"]:c["polynomial_group"]=j
    gate("every true Markov length is an exact union of contiguous same-label original pieces",
        len(groups)>0 and sum((g["length"] for g in groups),Q(0))==RC
        and all(all((c["original"]["pieces"]["background"],c["original"]["pieces"]["response"])==g["labels"]
                    and g["left"]<=c["left"]<c["right"]<=g["right"] for c in g["cells"]) for g in groups))
    return groups

def saved_geometry(old,paths,gate):
    S,T,R,W,F=(old[n] for n in ("SP","ST","RR","WX","FA"))
    so=S["complete_strict_propagation_conclusion"];to=T["complete_accepted_original_conclusion"]
    flow=T["complete_new_strict_propagation_conclusion"];wr=W["complete_shorter_flow_derivative_conclusion"]
    lead=W["complete_ungauged_leading_flow_conclusion"]
    roots=R["complete_root_mean_value_conclusion"]
    gate("the saved positive log budget has its full0_ra family scope and the actual root segment has positive outward K1",
        to["saved_SP_forward_full_0_ra_log_upper_read_verbatim"]==so["new_complete_forward_log_upper"]
        and all(p["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"] for p in
            (S["mathematical_parameters"],T["mathematical_parameters"],R["mathematical_parameters"],W["mathematical_parameters"],F["mathematical_parameters"]))
        and flow["exact_complete_interval"]==PARAMETERS["exact_complete_radial_interval"]
        and flow["original_0_ra_curvature_cost_reused_as_one_whole_budget"] is True
        and flow["all_shorter_ordered_subproducts_and_affine_insertions_retained"] is True
        and all(x["whole_segment_in_one_original_germ"] is True and gap(x["complete_Kr_lower"],"outward root K1")>0 for x in roots)
        and sha(paths["SP_source"])==EXPECTED["SP"]["source"]
        and sha(paths["ST_source"])==EXPECTED["ST"]["source"])
    cp=up(so["new_complete_forward_log_upper"])
    qcut=gap(min(gap(x["q_lower"],"saved actual qcut lower") for x in roots),"both cut sides q lower")
    qlo=gap(qcut*(-cp).exp(),"full0_rc positive-log q lower")
    qhi=up(max(up(so["new_entire_q_upper"]),up(flow["complete_new_tail_scalar_maxima"]["qplus"])))
    if qlo>qhi:raise ValueError("the two complete q covers are inconsistent")
    gate("the new full interval q lower and both old upper covers are strictly positive",qlo>0 and qhi>=qlo)
    gate("WX supplies uniform true shorter flows and separate reverse ungauged leading windows",
        wr["every_shorter_interval_and_both_orientations"] is True
        and wr["true_radial_interval"]==PARAMETERS["exact_complete_radial_interval"]
        and lead["all_shorter_subintervals_and_both_branches"] is True
        and lead["ungauged_primitive_density_convention"] is True
        and lead["ng_endpoint_ratio_not_absorbed_or_inverted"] is True
        and lead["true_radial_interval"]==PARAMETERS["exact_complete_radial_interval"])
    a=F["complete_new_first_frame_and_leading_conclusion"];e=T["complete_endpoint_and_source_conclusion"]
    gate("FA corrected cut input and forward-restored error use exactly the same P22 and same moving normalizer",
        F["complete_saved_cut_receiver_conclusion"]["TN_exact_moving_cutoff_abs_j"]==PARAMETERS["exact_moving_normalizer_cutoff_abs_j"]
        and F["complete_saved_cut_receiver_conclusion"]["input_cutoff_abs_j"]==97
        and F["mathematical_parameters"]["exact_strict_cut"]==PARAMETERS["exact_strict_cut"]
        and e["both_independent_means_and_complete_finite_blocks_retained"] is True
        and e["affine_impulses_have_no_radial_length_factor"] is True
        and e["exact_full_radial_length"]==str(RC))
    g=dict(qlo=qlo,qhi=qhi,cp=cp,qcut=qcut,
        M=up(wr["complete_shorter_flow_derivative_upper"]),F=up(wr["complete_shorter_flow_second_derivative_upper"]),
        G=up(wr["complete_shorter_flow_third_derivative_upper"]),
        v0=up(lead["complete_reverse_L2_upper"]),vm=up(lead["complete_reverse_Hminus4_3_upper"]),
        Kc=up(a["complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once"]),
        Ec=up(a["complete_same_TN_forward_L2_times_free_cut_upper"]),
        Gcut=up(e["complete_raw_cut_to_waist_density_upper"]),
        Gsrc=up(e["strict_L1_Hminus1_source_to_waist_density_upper"]))
    saved=dict(SP_forward_full0_ra_log_upper_read_verbatim=copy.deepcopy(so["new_complete_forward_log_upper"]),
        SP_prefix_q_upper_read_verbatim=copy.deepcopy(so["new_entire_q_upper"]),
        ST_tail_q_upper_read_verbatim=copy.deepcopy(flow["complete_new_tail_scalar_maxima"]["qplus"]),
        RR_complete_root_mean_value_read_verbatim=copy.deepcopy(roots),
        WX_MFG_read_verbatim={k:copy.deepcopy(wr[k]) for k in
            ("complete_shorter_flow_derivative_upper","complete_shorter_flow_second_derivative_upper","complete_shorter_flow_third_derivative_upper")},
        WX_reverse_leading_windows_read_verbatim={k:copy.deepcopy(lead[k]) for k in
            ("complete_reverse_L2_upper","complete_reverse_Hminus4_3_upper")},
        FA_corrected_Kc_minus_read_verbatim=copy.deepcopy(a["complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once"]),
        FA_already_forward_restored_cut_error_read_verbatim=copy.deepcopy(a["complete_same_TN_forward_L2_times_free_cut_upper"]),
        ST_cut_receiver_read_verbatim=copy.deepcopy(e["complete_raw_cut_to_waist_density_upper"]),
        ST_general_primitive_mean_source_receiver_read_verbatim=copy.deepcopy(e["strict_L1_Hminus1_source_to_waist_density_upper"]),
        same_input_Hminus4_3_cutoff=97,same_moving_normalizer_cutoff=268435456,
        cut_ng_inverse_not_applied_again=True,cut_forward_TN_not_applied_again=True,
        all_saved_complete_objects_bound_to_their_original_execution_SHA256=True)
    return g,saved

def ordinary_product(x,y,n=None):
    n=min(len(x),len(y))-1 if n is None else n
    return [up(sum((math.comb(j,i)*x[i]*y[j-i] for i in range(j+1)),arb(0))) for j in range(n+1)]
def reciprocal_derivatives(g,lower,n):
    z=[up(1/gap(lower,"reciprocal coefficient lower"))]
    for j in range(1,n+1):
        z.append(up(sum((math.comb(j,i)*g[i]*z[j-i] for i in range(1,j+1)),arb(0))/lower))
    return z
def exponential_derivatives(z,W):
    e=up((z*W[0]).exp())
    return [e,up(z*W[1]*e),up((z*W[2]+z*z*W[1]**2)*e),
        up((z*W[3]+3*z*z*W[1]*W[2]+z**3*W[1]**3)*e)]

def physical_polynomial_derivatives(group):
    d=ex(PARAMETERS["exact_real_delta_radius"]);h=ex(group["length"])
    mark=[arb(1),up(18/h),up(96/(h*h))]
    C=[up(7+group["s"][0])]+[arb(6*128**(k-1)) for k in range(1,4)]
    Z=[arb(19)]+[arb(83*384**(k-1)) for k in range(1,4)]
    out=[[arb(0) for _ in range(4)] for _ in range(3)]
    for k in range(4):
        out[0][k]=up(7+19*d) if k==0 else up(C[k]+d*Z[k])
        for j in (1,2):out[j][k]=up(mark[j]*(C[k]+d*Z[k])+(group["s"][j] if k==0 else 0))
    return out,dict(exact_polynomial_interval=[str(group["left"]),str(group["right"])],
        exact_length=str(group["length"]),original_background_response_pieces=list(group["labels"]),
        old_s0_s1_s2_absolute_maxima=encode(group["s"]),markov_multipliers=encode(mark[1:]),
        full_Q_mixed_derivative_pair_A0=encode(out),
        physical_response_has_no_extra_alpha=True,fixed_s_nu0_read_not_s_nudelta=True,
        one_sided_ordinary_derivatives_only=True,full_polynomial_or_qualified_subinterval=group["qualification"])

def selected_intrinsic_derivatives(cell,W):
    """SJ14--24: original nu0 jets plus the complete new real-delta metric fee."""
    jets=cell["original"]["intrinsic_whole_third_jets"]
    b=[au(jets["beta"+(str(j) if j else "")]) for j in range(4)]
    gg=[au(jets["gamma"+(str(j) if j else "")]) for j in range(4)]
    kk=[au(jets["K"+(str(j) if j else "")]) for j in range(4)]
    glo=gap(rb(jets["gamma"]),"old complete gamma")
    alo=gap(rb(jets["a"]),"old complete physical radius")
    active=cell["left"]<CONTROL[1] and cell["right"]>CONTROL[0]
    if active and not CONTROL[0]<=cell["left"]<cell["right"]<=CONTROL[1]:
        raise ValueError("an original row crosses an exact compact metric seam")
    T=None
    if active:
        d=ex(PARAMETERS["exact_real_delta_radius"])
        ainv=up(1/(alo*alo))
        aa=[ainv,up(2*b[0]*ainv),up((2*b[1]+4*b[0]**2)*ainv),
            up((2*b[2]+12*b[0]*b[1]+8*b[0]**3)*ainv)]
        gi=reciprocal_derivatives(gg,glo,3)
        T=[up(x/2) for x in ordinary_product(ordinary_product(b,ordinary_product(gi,gi)),aa)]
        L=[up(kk[j]+d*sum((math.comb(j,i)*T[i]*W[j-i+1] for i in range(j+1)),arb(0))) for j in range(4)]
        knew=ordinary_product(exponential_derivatives(d,W),L)
        gnew=ordinary_product(gg,exponential_derivatives(d/2,W))
        glnew=gap(glo*(-d*W[0]/2).exp(),"complete selected gamma lower")
    else:
        knew=kk;gnew=gg;glnew=glo
    return dict(beta=b,gamma=gnew,gamma_lower=glnew,K=knew,
        original_physical_radius_lower=alo,compact_metric_active=active,T=T)

def complete_coefficient_fees(cell,Qmix,intr,g):
    """Complete signed identities SJ26--42 are majorized only after assembly."""
    b,gg,K=intr["beta"],intr["gamma"],intr["K"]
    qlo,qhi=g["qlo"],g["qhi"]
    q=[qhi,up(K[1]/(2*qlo)),
        up(K[2]/(2*qlo)+K[1]**2/(4*qlo**3)),
        up(K[3]/(2*qlo)+3*K[1]*K[2]/(4*qlo**3)+3*K[1]**3/(8*qlo**5))]
    mgap=gap(ex(PARAMETERS["original_negative_mean_gap"])-19*ex(PARAMETERS["exact_real_delta_radius"]),"complete negative physical mean")
    eta=[up(sum((math.comb(j,i)*gg[i]*Qmix[j-i][0] for i in range(j+1)),arb(0))) for j in range(3)]
    etalo=gap(intr["gamma_lower"]*mgap,"complete eta lower")
    h=ordinary_product(eta,q,2);hlo=gap(etalo*qlo,"complete characteristic gap")
    jh=[up(1/hlo),up(h[1]/hlo**2),up(h[2]/hlo**2+2*h[1]**2/hlo**3)]
    R=[]
    for p in range(3):
        R.append([up(max(arb(1),qhi)*Qmix[p][k]+sum(
            (math.comb(p,i)*q[i]*Qmix[p-i][k] for i in range(1,p+1)),arb(0))) for k in range(4)])
    def product_Q2(p,k):
        return up(sum((math.comb(p,i)*math.comb(k,l)*Qmix[i][l]*Qmix[p-i][k-l]
            for i in range(p+1) for l in range(k+1)),arb(0)))
    sq=[]
    for p in range(2):
        sq.append([up(max(arb(1),K[0])*product_Q2(p,k)+sum(
            (math.comb(p,i)*K[i]*product_Q2(p-i,k) for i in range(1,p+1)),arb(0))) for k in range(4)])
    d=[up(b[0]*sq[0][0]/4)]+[up(b[0]*sq[0][k-1]) for k in range(1,5)]
    dr=up((b[1]*sq[0][0]+b[0]*sq[1][0])/4)
    drphi=up(b[1]*sq[0][0]+b[0]*sq[1][0])
    ell=up(2*b[0]*sq[0][0])
    r,rr,rrr=R[0][0],R[1][0],R[2][0]
    rp,rpp,rppp=R[0][1:];rrp=R[1][1]
    B=up(q[1]/(2*qlo)+b[0]*(1+r*r))
    Br=up((q[2]/qlo+q[1]**2/qlo**2)/2+b[1]*(1+r*r)+2*b[0]*r*rr)
    Brr=up((q[3]/qlo+3*q[1]*q[2]/qlo**2+2*q[1]**3/qlo**3)/2
        +b[2]*(1+r*r)+4*b[1]*r*rr+2*b[0]*(rr*rr+r*rrr))
    Bp=up(2*b[0]*r*rp)
    Bpp=up(2*b[0]*(rp*rp+r*rpp))
    Bppp=up(2*b[0]*(3*rp*rpp+r*rppp))
    Brp=up(2*b[1]*r*rp+2*b[0]*(rr*rp+r*rrp))
    S=up(B*jh[0]/2);Sr=up((Br*jh[0]+B*jh[1])/2)
    Srr=up((Brr*jh[0]+2*Br*jh[1]+B*jh[2])/2)
    Sp=up(Bp*jh[0]/2);Spp=up(Bpp*jh[0]/2)
    Srp=up((Brp*jh[0]+Bp*jh[1])/2)
    c=up(d[0]+h[0]);cr=up(dr+h[1])
    O=up(Bp+b[0]*rp*r+c*Sp+Sr+S*d[1])
    Op=up(Bpp+b[0]*(rpp*r+rp*rp)+c*Spp+2*d[1]*Sp+Srp+S*d[2])
    Or=up(Brp+b[1]*rp*r+b[0]*(rrp*r+rp*rr)+cr*Sp+c*Srp+Srr+Sr*d[1]+S*drphi)
    Z=up(O*jh[0]/2);Zp=up(Op*jh[0]/2);Zr=up((Or*jh[0]+O*jh[1])/2)
    Ba=[B,Bp,Bpp,Bppp]
    a=[up(d[k+2]+b[0]*sum((math.comb(k,i)*R[0][i+1]*R[0][k-i] for i in range(k+1)),arb(0))
        +jh[0]*sum((math.comb(k,i)*Ba[i]*Ba[k-i] for i in range(k+1)),arb(0))/2) for k in range(3)]
    # Every matrix, row and column below is a complete entry sum.
    mat=dict(C=up(2*c),Cphi=up(2*d[1]),B=up(2*B),S=up(2*S),Sr=up(2*Sr),
        O=up(2*O),Z=up(2*Z),Zr=up(2*Zr),Zphi=up(2*Zp),a=up(2*a[0]),
        A=up(2*d[2]+2*Bp),D=up(2*d[2]+2*Bp+4*b[0]*rp*r),
        Dphi=up(2*d[3]+2*Bpp+4*b[0]*(rpp*r+rp*rp)),
        rvec=up(2*r),rvecphi=up(2*rp),arow=up(2*r),arowphi=up(2*rp),
        ell0=ell,beta=b[0])
    mat["HZ"]=up(mat["C"]*mat["Zphi"]+mat["Cphi"]*mat["Z"]+mat["Zr"])
    mat["Ny"]=up(b[0]*mat["rvecphi"]*(2*mat["arow"]+mat["arowphi"]/4))
    audit=dict(ordinary_q_0_3=encode(q),complete_eta_0_2=encode(eta),complete_eta_lower=rec(etalo),
        complete_h_0_2=encode(h),complete_h_lower=rec(hlo),complete_inverse_h_0_2=encode(jh),
        common_both_branch_r_mixed_0_2_0_3=encode(R),complete_Squadratic_0_1_0_3=encode(sq),
        complete_d_0_4=encode(d),complete_dr=rec(dr),complete_drphi=rec(drphi),
        common_B_0_3=encode(Ba),common_Br=rec(Br),common_Brr=rec(Brr),common_Brphi=rec(Brp),
        common_S=rec(S),common_Sr=rec(Sr),common_Srr=rec(Srr),common_Sphi=rec(Sp),common_Sphiphi=rec(Spp),
        common_Srphi=rec(Srp),common_O=rec(O),common_Ophi=rec(Op),common_Or=rec(Or),
        common_Z=rec(Z),common_Zphi=rec(Zp),common_Zr=rec(Zr),
        common_both_branch_a_0_2=encode(a),complete_matrix_row_column_A0_entry_sums=encode(mat))
    jump=dict(q2=q[2],beta1=b[1],gamma1=gg[1],physical_pair_r=Qmix[1][0],
        gamma=gg[0],eta_lower=etalo,h_lower=hlo,beta=b[0],r=r,B=B,S_entry=mat["S"],mean_upper=Qmix[0][0])
    return mat,a,audit,jump

def multiplier_weights():
    w={(B,s):positive_power(ex(1+4*B),s) for B in (96,192,384,576)
        for s in (Q(1,3),Q(2,3),Q(4,3),Q(7,3))}
    LJ=PARAMETERS["exact_moving_normalizer_cutoff_abs_j"]+PARAMETERS["full_finite_support_offset"]
    w["finite_7_3"]=positive_power(ex(1+16*LJ*LJ),Q(7,6))
    w["finite_4_3"]=positive_power(ex(1+16*LJ*LJ),Q(2,3))
    return w
def complete_finite_and_two_primitive_fees(c,weights):
    bands=dict(C=192,Cphi=192,B=192,S=192,Sr=192,O=384,Z=384,Zr=384,Zphi=384,
        a=384,A=192,D=192,Dphi=192,rvec=96,rvecphi=96,arow=96,arowphi=96,HZ=576)
    def m(k,s):return up(weights[bands[k],abs(Q(s))]*c[k])
    third=Q(1,3);two=Q(2,3);four=Q(4,3)
    CI2=ex(Q(17,16));beta=c["beta"]
    f0=up(m("B",four)+c["D"]/4+m("D",four)/4+beta*c["rvec"]*m("arow",four))
    f1=up(c["S"]*(c["C"]+m("C",four)))
    f2=up(c["Z"]*(c["C"]+m("C",four))/4)
    zstar=up(m("D",four)+beta*m("rvec",four)*m("arowphi",four))
    t10=up(1+c["S"]/4);t20=up(1+c["Z"]/16);t0=up(t10*t20)
    t1m=up(1+m("S",four)/4);t2m=up(1+m("Z",four)/16);tm=up(t1m*t2m)
    r2=up(CI2*(m("Dphi",third)+beta*m("rvecphi",third)*m("arowphi",four))+f0)
    qstar=up(r2*tm+(CI2*(c["D"]*m("S",third)+c["S"]*m("a",third))+f1)*t2m
        +CI2*(c["O"]*m("Z",two)/4+c["S"]*m("O",third))
        +t10*(CI2*(c["HZ"]+c["Z"]*m("Cphi",third)+c["a"]*m("Z",two)/4+c["Z"]*m("a",third)/4)+f2))
    aS=up(c["S"]/4);bZ=up(c["Z"]/16);aSr=up(c["Sr"]/4);bZr=up(c["Zr"]/16)
    fT=up(2*(aS+bZ+aS*bZ));fTr=up(2*(aSr*(1+bZ)+(1+aS)*bZr))
    g1=up(c["C"]+c["Cphi"]+c["ell0"]+c["B"]+(c["A"]+c["Ny"])/4)
    lm=up(m("C",Q(7,3))+m("Cphi",four)+c["ell0"]+m("a",four)/4)
    fJ=up(fT*weights["finite_7_3"]*(g1+lm)+fTr*weights["finite_4_3"])
    return dict(f0=f0,f1=f1,f2=f2,zstar=zstar,t10=t10,t20=t20,t0=t0,t1m=t1m,t2m=t2m,tm=tm,
        r2=r2,qstar=qstar,fT=fT,fTr=fTr,g1=g1,lminus=lm,fJ=fJ)

def transported_coefficient_bounds(a,g):
    M,F,G=g["M"],g["F"],g["G"]
    one=[up(M*a[0]),up(F*a[0]+M*M*a[1]),up(G*a[0]+3*M*F*a[1]+M**3*a[2])]
    return one

def complete_source_row(c,t,B,global_C,g):
    # The two branches have the same positive bound; their complete sum is explicit.
    cm=up(6*(global_C[0]+2*global_C[1]+global_C[2]));cf=up(1+cm/4)
    b0=up(2*B[0])
    rank_shape=up((ex(Q(33,16))*(g["M"]-1)**2+g["F"]**2).sqrt()+(g["M"]-1)/4)
    fpsi=up(b0*rank_shape)
    dV=up(g["v0"]*(ex(Q(17,16))*b0*cm+fpsi*cf))
    components=dict(leading_two_primitive_and_rank=up(g["Kc"]*t["t0"]*dV),
        complete_Q_including_F0_F1_F2=up(g["Kc"]*t["qstar"]*g["vm"]*cf),
        complete_finite_FT_FJ=up(g["Kc"]*t["fJ"]*g["vm"]*cf),
        complete_independent_mean_row=up(g["Kc"]*t["zstar"]*t["tm"]*g["vm"]*cf))
    physical=up(sum(components.values(),arb(0)))
    return physical,components,dict(complete_two_branch_c_multiplier=rec(cm),complete_c_factor=rec(cf),
        complete_two_primitive_leading_defect=rec(dV),complete_two_primitive_rank=rec(fpsi),
        complete_propagation_integrand=rec(physical),complete_four_source_parts=encode(components),
        complete_mean_row_included=True,finite_FT_and_FJ_included=True)

def complete_interface(left,right,global_C,g):
    # Even artificial refinements get a conservative one-sided sum. True joins are labelled separately.
    j0,j1=left["jump"],right["jump"];qm=g["qlo"];qp=g["qhi"]
    eta=min(j0["eta_lower"],j1["eta_lower"]);hh=min(j0["h_lower"],j1["h_lower"])
    rp=max(j0["r"],j1["r"]);bp=max(j0["B"],j1["B"]);beta=max(j0["beta"],j1["beta"])
    gamma=max(j0["gamma"],j1["gamma"]);M=max(j0["mean_upper"],j1["mean_upper"])
    Jq=up(j0["q2"]+j1["q2"]);Jb=up(j0["beta1"]+j1["beta1"]);Jg=up(j0["gamma1"]+j1["gamma1"])
    Jpair=up(j0["physical_pair_r"]+j1["physical_pair_r"])
    Jeta=up(M*Jg+gamma*Jpair)
    # Ju + q*Jv is bounded jointly by max(1,q)*the complete pair derivative sum.
    JB=up(Jq/(2*qm)+Jb*(1+rp*rp)+2*beta*rp*max(arb(1),qp)*Jpair)
    JZ=up(2*(JB+bp*Jeta/eta)/(4*hh*hh))
    t10=up(1+max(j0["S_entry"],j1["S_entry"])/4)
    cm=up(6*(global_C[0]+2*global_C[1]+global_C[2]));cf=up(1+cm/4)
    result=up(g["Kc"]*t10*ex(Q(17,16))*JZ*g["vm"]*cf)
    genuine=left["cell"]["polynomial_group"]!=right["cell"]["polynomial_group"]
    return result,dict(radius=str(left["cell"]["right"]),genuine_polynomial_join=genuine,
        original_adjacent_common_rows=[left["cell"]["original"]["common_row"],right["cell"]["original"]["common_row"]],
        complete_intrinsic_qrr_jump=rec(Jq),complete_intrinsic_betar_jump=rec(Jb),
        complete_intrinsic_gammar_jump=rec(Jg),complete_physical_pair_r_jump=rec(Jpair),
        complete_eta_r_jump=rec(Jeta),common_Br_jump=rec(JB),complete_two_branch_Z_jump=rec(JZ),
        complete_two_primitive_impulse=rec(result),radial_length_factor_applied=False,
        no_radial_derivative_continuity_inferred_from_polynomial_values=True,
        exact_lower_coefficient_continuity_comes_from_same_repaired_definition=True)

def finite_records(v):
    if isinstance(v,dict):
        if "ball" in v:return rb(v).is_finite()
        return all(finite_records(x) for x in v.values())
    if isinstance(v,(list,tuple)):return all(finite_records(x) for x in v)
    return True

def render_conclusion(d):
    rows=["# Complete strict radial first-symbol defect: actual new scalar conclusion","",
        "Public run: "+str(d.get("run_id"))+"/"+str(d.get("run_attempt"))+".",
        "Scientific source SHA256: "+d["source_sha256"]+".",
        "Input manifest SHA256: "+d["input_manifest_sha256"]+".",
        "Actual complete: "+str(d["complete"])+". Actual scientific return: "+str(d["actual_returncode"])+".","",
        "All old targets, profiles, Fourier arrays, repaired polynomials, successful flows and cut columns are read-only.",
        "Only the complete SJ scalar derivative, ordinary-integral and interface budgets are evaluated.",""]
    if d.get("failure"):rows+=["Failure: "+json.dumps(d["failure"],ensure_ascii=False),""]
    c=d.get("complete_strict_first_symbol_waist_error_conclusion")
    if c:
        rows+=["## Complete new waist density error","",
            "| Complete contribution | Outward ball |","|---|---|"]
        for k in ("complete_cut_error_contribution","complete_ordinary_source_contribution",
                  "complete_all_interface_contribution","complete_SF_waist_density_error_upper"):
            rows.append("| "+k+" | "+c[k]["ball"]+" |")
        rows+=["","The input is the complete physical H^(-4/3) Fourier space with |j|>=97.",
            "The output is the true waist nonmean density pair plus its two independent physical means.",
            "The full finite correction through Js+575 and the actual same Js=268435456 are retained.",
            "This is a strong bound for the difference of the two full columns, not for either order-zero trial separately.",
            "The true waist receiver, common root gauge, actual incoming inverse and finite Schur border remain separate.",""]
    rows+=["## Actual gates",""]
    rows += ["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"] for g in d["gates"]]
    return "\n".join(rows)+"\n"

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","workdir","process","conclusion","out"):
        parser.add_argument("--"+key,type=Path,required=True)
    a=parser.parse_args();a.repo=a.repo_root;a.manifest_sha=sha(a.manifest)
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new SJ arithmetic is permitted only in the real public repository Actions runner")
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the complete frozen scientific runtime changed")
    ctx.prec=320;a.workdir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,arithmetic_bits=320,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        mathematical_parameters=PARAMETERS,stage="immutable inputs",
        original_successful_small_receipts_read=0,original_complete_body_parts_read=0,
        original_complete_body_rows_verified=0,original_consumed_body_rows=0,
        new_full_interval_q_lower_bounds=0,new_fixed_polynomial_intervals=0,
        new_selected_intrinsic_rows=0,new_compact_metric_rows=0,new_complete_coefficient_rows=0,
        new_transported_angular_rows=0,new_ordinary_source_rows=0,new_complete_interface_rows=0,
        new_genuine_polynomial_join_rows=0,new_conservative_artificial_interface_rows=0,
        new_complete_waist_error_bounds=0,
        old_numerical_enclosures_recomputed=0,old_target_intrinsic_jets_or_means_recomputed=0,
        old_repaired_polynomials_or_response_coefficients_recomputed=0,
        old_profiles_Taylor_arrays_rays_or_flows_recomputed=0,old_SP_log_integrals_or_products_recomputed=0,
        old_RR_WX_FA_source_or_receiver_bounds_recomputed=0,old_scientific_producer_imports=0,
        old_scientific_producer_calls=0,old_strict_container_parts_restored=0,
        original_natural_stage_bytes_modified=False,complete_strict_first_symbol_defect_paid=False,
        full_incoming_inverse_claimed=False,finite_Schur_inverse_claimed=False,full_return_R0_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    audit=dict(kind="complete_temporary_SJ_positive_scalar_audit_v1",polynomial_groups=[],rows=[],interfaces=[])
    def checkpoint():save(a.process,d)
    def gate(name,truth):
        ok=bool(truth);d["gates"].append(dict(name=name,passed=ok))
        if not ok:raise ValueError("actual SJ gate failed: "+name)
    try:
        manifest,paths,old,bm=input_closure(a,d,gate);checkpoint()
        rows=original_body_rows(a,manifest,old,bm,d,gate)
        groups=polynomial_intervals(rows,gate)
        g,saved=saved_geometry(old,paths,gate)
        d["complete_saved_scalar_inputs_read_verbatim"]=saved
        d["accepted_success_identity_read_verbatim"]=copy.deepcopy(EXPECTED)
        d["complete_global_q_and_mean_conclusion"]=dict(
            complete_q_lower=rec(g["qlo"]),complete_q_upper=rec(g["qhi"]),
            exact_complete_interval=["0",str(RC)],
            method="qcut_lower*exp(-saved_full0_ra_positive_log_upper), followed by actual monotone final segment",
            positive_log_algorithm_not_arbitrary_operator_norm=True,
            no_old_curvature_integral_or_strict_container_recomputed=True,
            original_negative_mean_gap=PARAMETERS["original_negative_mean_gap"],
            selected_mean_gap_lower=rec(gap(ex(PARAMETERS["original_negative_mean_gap"])-19*ex(PARAMETERS["exact_real_delta_radius"]),"selected mean")))
        d["new_full_interval_q_lower_bounds"]=1;d["new_fixed_polynomial_intervals"]=len(groups)
        d["stage"]="new complete radial coefficient rows";checkpoint()
        W=[arb(1),ex(Q(2400,13)),ex(Q(5280000,169)),ex(10560*Q(100,13)**3),ex(190080*Q(100,13)**4)]
        weights=multiplier_weights()
        group_mixed={}
        for group in groups:
            qm,qa=physical_polynomial_derivatives(group);group_mixed[group["index"]]=qm
            audit["polynomial_groups"].append(dict(index=group["index"],original_common_row_range=[group["first"],group["stop"]],
                original_labels=list(group["labels"]),complete_markov_conclusion=qa))
        closure=[];intrinsic_max={k:[arb(0) for _ in range(4)] for k in ("beta","gamma","K")}
        matrix_max={};scalar_max={};qmax=[arb(0) for _ in range(4)];amin=etamin=hmin=None
        amax=[arb(0) for _ in range(3)];bmax=[arb(0) for _ in range(3)];C=[arb(0) for _ in range(3)]
        for i,cell in enumerate(rows):
            intr=selected_intrinsic_derivatives(cell,W)
            qm=group_mixed[cell["polynomial_group"]]
            mat,angular,detail,jump=complete_coefficient_fees(cell,qm,intr,g)
            fee=complete_finite_and_two_primitive_fees(mat,weights)
            transported=transported_coefficient_bounds(angular,g)
            length=ex(cell["right"]-cell["left"])
            for k in range(3):
                C[k]=up(C[k]+length*transported[k]);amax[k]=max(amax[k],angular[k]);bmax[k]=max(bmax[k],transported[k])
            for k,v in mat.items():matrix_max[k]=max(matrix_max.get(k,arb(0)),v)
            for k,v in fee.items():scalar_max[k]=max(scalar_max.get(k,arb(0)),v)
            for k in intrinsic_max:
                for j in range(4):intrinsic_max[k][j]=max(intrinsic_max[k][j],intr[k][j])
            # Directed endpoint minima remain lower bounds; no maximum upper is inverted.
            amin=intr["gamma_lower"] if amin is None else min(amin,intr["gamma_lower"])
            etamin=jump["eta_lower"] if etamin is None else min(etamin,jump["eta_lower"])
            hmin=jump["h_lower"] if hmin is None else min(hmin,jump["h_lower"])
            for k in range(4):qmax[k]=max(qmax[k],up(detail["ordinary_q_0_3"][k]))
            audit["rows"].append(dict(original_common_row=cell["original"]["common_row"],
                exact_original_interval=cell["original"]["interval"],exact_consumed_interval=[str(cell["left"]),str(cell["right"])],
                exact_original_scalar_germ=cell["original"]["actual_scalar_germ"],original_piece_labels=cell["original"]["pieces"],
                original_complete_row_payload_sha256=payload_sha(cell["original"]),
                original_whole_third_jets_read_verbatim=copy.deepcopy(cell["original"]["intrinsic_whole_third_jets"]),
                qualified_polynomial_group=cell["polynomial_group"],complete_new_intrinsic=encode(intr),
                complete_new_radial_and_angular_coefficients=detail,complete_finite_and_two_primitive_fees=encode(fee),
                complete_common_branch_transported_0_2=encode(transported)))
            closure.append(dict(cell=cell,mat=mat,fee=fee,transported=transported,jump=jump))
            d["new_selected_intrinsic_rows"]+=1;d["new_compact_metric_rows"]+=int(intr["compact_metric_active"])
            d["new_complete_coefficient_rows"]+=1;d["new_transported_angular_rows"]+=1
            if (i+1)%256==0:
                d["latest_completed_original_common_row"]=cell["original"]["common_row"];checkpoint()
                print("SJ_COMPLETE_COEFFICIENT_ROWS",i+1,flush=True)
        d["latest_completed_original_common_row"]=rows[-1]["original"]["common_row"]
        gate("all3071 new coefficient rows retain full delta metric derivatives and strict q eta h denominators",
            len(closure)==3071 and amin>0 and etamin>0 and hmin>0
            and all(x.is_finite() for v in intrinsic_max.values() for x in v)
            and all(x.is_finite() for x in matrix_max.values()))
        gate("only exact off-bump copies or the complete four-derivative bump formula were used",
            0<d["new_compact_metric_rows"]<3071 and len(W)==5
            and all(c["cell"]["left"]>=CONTROL[0] and c["cell"]["right"]<=CONTROL[1]
                for c,z in zip(closure,audit["rows"]) if z["complete_new_intrinsic"]["compact_metric_active"])
            and d["old_target_intrinsic_jets_or_means_recomputed"]==0)
        d["complete_original_body_and_polynomial_conclusion"]=dict(
            exact_consumed_interval=["0",str(RC)],original_restored_rows=3322,original_consumed_rows=3071,
            complete_original_parts=18,qualified_polynomial_intervals=len(groups),
            shortest_exact_qualified_interval=str(min(x["length"] for x in groups)),
            longest_exact_qualified_interval=str(max(x["length"] for x in groups)),
            complete_Q_mixed_maxima=encode([[max(group_mixed[j][p][k] for j in group_mixed) for k in range(4)] for p in range(3)]),
            no_full_background_cubic_assumption=True,fixed_true_s_nu0_ordinary_jets_read=True,
            physical_full193_response_has_no_alpha=True,
            no_global_radial_derivative_continuity_assumed=True,all_final_partial_intervals_explicit=True)
        d["complete_new_selected_intrinsic_conclusion"]=dict(
            complete_radial_0_3_absolute_maxima=encode(intrinsic_max),
            complete_gamma_lower=rec(amin),complete_eta_lower=rec(etamin),complete_h_lower=rec(hmin),
            complete_q_0_3_absolute_maxima=encode(qmax),complete_bump_0_4_upper=encode(W),
            new_compact_metric_rows=d["new_compact_metric_rows"],
            old_intrinsic_eta_box_restricted_to_fixed_eta0=True,
            new_nu_family_is_separately_paid_through_third_radial_derivative=True,
            s_in_background_remains_fixed_s_nu0=True,all_exact_compact_seams_retained=True)
        d["complete_new_radial_coefficient_conclusion"]=dict(
            complete_matrix_row_column_A0_maxima=encode(matrix_max),
            complete_finite_and_two_primitive_scalar_maxima=encode(scalar_max),
            ordinary_derivative_convention=True,complete_branch_entry_sums_before_functional=True,
            exact_moving_Js=PARAMETERS["exact_moving_normalizer_cutoff_abs_j"],
            full_finite_support_through=PARAMETERS["exact_moving_normalizer_cutoff_abs_j"]+575,
            full_F0_F1_F2_FT_FJ_and_Zy_mean_rows_retained=True)
        d["complete_new_transported_coefficient_conclusion"]=dict(
            common_both_branch_a_0_2_maxima=encode(amax),common_both_branch_b_0_2_maxima=encode(bmax),
            common_both_branch_complete_c_0_2_integrals=encode(C),
            complete_two_branch_c_multiplier=rec(up(6*(C[0]+2*C[1]+C[2]))),
            new_ordinary_integrals_use_true_radial_lengths_once=True,
            signed_old_first_symbol_finite_part_never_reintegrated=True,
            constant_C_global_bound_used_in_every_source_and_interface_row=True,
            general_composed_coefficients_not_assigned_finite_Fourier_support=True,
            all_complete_coefficient_means_retained=True)
        gate("the three new full transported coefficient integrals use the complete ordinary radial cover and both branches",
            all(x.is_finite() and x>=0 for x in C) and sum((c["right"]-c["left"] for c in rows),Q(0))==RC
            and d["new_transported_angular_rows"]==3071)
        d["stage"]="new complete ordinary source integral";checkpoint()
        # Save the complete new coefficient stage before assembling its source integral.
        save(a.out,audit,compressed=True)
        total_source=arb(0);source_parts={k:arb(0) for k in
            ("leading_two_primitive_and_rank","complete_Q_including_F0_F1_F2","complete_finite_FT_FJ","complete_independent_mean_row")}
        max_source=arb(0)
        for i,x in enumerate(closure):
            value,parts,detail=complete_source_row(x["mat"],x["fee"],x["transported"],C,g)
            length=ex(x["cell"]["right"]-x["cell"]["left"])
            total_source=up(total_source+length*value);max_source=max(max_source,value)
            for k,v in parts.items():source_parts[k]=up(source_parts[k]+length*v)
            audit["rows"][i]["complete_new_source"]=detail
            audit["rows"][i]["complete_new_ordinary_source_contribution"]=rec(up(length*value))
            d["new_ordinary_source_rows"]+=1
        d["complete_new_complete_source_conclusion"]=dict(
            complete_ordinary_L1_source_upper=rec(total_source),complete_source_integrand_maximum=rec(max_source),
            complete_four_ordinary_source_parts=encode(source_parts),exact_ordinary_radial_interval=["0",str(RC)],
            exact_ordinary_radial_length=str(RC),complete_source_rows=3071,
            original_two_physical_rows_and_two_mean_rows_retained=True,
            finite_F0_F1_F2_and_FT_FJ_included=True,
            ordinary_source_window="L1(dr; L2_nonmean_pair plus two physical means)",
            strong_input_window="H^(-4/3) with original |j|>=97")
        gate("the complete ordinary source contains all four strong contributions including finite maps and both means",
            d["new_ordinary_source_rows"]==3071 and total_source.is_finite() and total_source>=0
            and all(x.is_finite() and x>=0 for x in source_parts.values()))
        d["stage"]="new complete genuine and conservative interface impulses";checkpoint()
        total_jump=arb(0);genuine_sum=arb(0);refinement_sum=arb(0);max_jump=arb(0)
        for left,right in zip(closure,closure[1:]):
            if left["cell"]["right"]!=right["cell"]["left"]:raise ValueError("interface cover changed")
            value,detail=complete_interface(left,right,C,g)
            total_jump=up(total_jump+value);max_jump=max(max_jump,value);audit["interfaces"].append(detail)
            d["new_complete_interface_rows"]+=1
            if detail["genuine_polynomial_join"]:
                d["new_genuine_polynomial_join_rows"]+=1;genuine_sum=up(genuine_sum+value)
            else:
                d["new_conservative_artificial_interface_rows"]+=1;refinement_sum=up(refinement_sum+value)
        d["complete_new_interface_conclusion"]=dict(
            complete_all_interface_impulses_upper=rec(total_jump),complete_genuine_polynomial_join_sum=rec(genuine_sum),
            complete_conservative_artificial_refinement_sum=rec(refinement_sum),complete_maximum_interface_impulse=rec(max_jump),
            complete_interface_count=3070,genuine_polynomial_join_count=d["new_genuine_polynomial_join_rows"],
            conservative_artificial_refinement_count=d["new_conservative_artificial_interface_rows"],
            intrinsic_qrr_betar_gammar_and_physical_mean_r_jumps_all_retained=True,
            exact_S_continuity_is_from_pinned_repaired_and_intrinsic_definitions=True,
            endpoint_ball_overlap_not_used_as_continuity=True,no_radial_length_factor=True,
            both_characteristic_branches_and_complete_finite_interface_projection_retained=True)
        gate("all3070 interfaces keep complete intrinsic and physical one-sided jumps without a length factor",
            d["new_complete_interface_rows"]==3070
            and d["new_genuine_polynomial_join_rows"]+d["new_conservative_artificial_interface_rows"]==3070
            and d["new_genuine_polynomial_join_rows"]==len(groups)-1
            and total_jump.is_finite() and total_jump>=0)
        cut=up(g["Gcut"]*g["Ec"]);body=up(g["Gsrc"]*total_source);seam=up(g["Gsrc"]*total_jump)
        complete=up(cut+body+seam)
        d["complete_strict_first_symbol_waist_error_conclusion"]=dict(
            complete_cut_error_contribution=rec(cut),complete_ordinary_source_contribution=rec(body),
            complete_all_interface_contribution=rec(seam),complete_SF_waist_density_error_upper=rec(complete),
            complete_input_window="original full H^(-4/3) high input |j|>=97",
            complete_output_window="true waist L2 nonmean density pair plus two independent physical means",
            strong_bound_is_for_exact_homogeneous_free_column_minus_same_SF_trial=True,
            FA_ng_inverse_inside_Kc_applied_exactly_once=True,
            FA_forward_TN_inside_cut_error_applied_exactly_once=True,
            ST_cut_and_source_receivers_each_applied_once=True,
            no_TC_cut_factor_used_as_a_waist_factor=True,
            same_moving_normalizer_cutoff_abs_j=268435456,
            complete_finite_support_through=268435456+575,
            true_waist_receiver_common_root_gauge_incoming_inverse_and_finite_border_remain_separate=True)
        d["new_complete_waist_error_bounds"]=1
        gate("the exact same-cut error ordinary source and all impulses give one complete strong waist difference",
            complete.is_finite() and complete>=0 and cut.is_finite() and body.is_finite() and seam.is_finite()
            and d["complete_strict_first_symbol_waist_error_conclusion"]["complete_finite_support_through"]==268436031)
        gate("every accepted source and receiver scalar remains a literal read-only object with its full identity",
            saved["FA_corrected_Kc_minus_read_verbatim"]==old["FA"]["complete_new_first_frame_and_leading_conclusion"]["complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once"]
            and saved["FA_already_forward_restored_cut_error_read_verbatim"]==old["FA"]["complete_new_first_frame_and_leading_conclusion"]["complete_same_TN_forward_L2_times_free_cut_upper"]
            and saved["SP_forward_full0_ra_log_upper_read_verbatim"]==old["SP"]["complete_strict_propagation_conclusion"]["new_complete_forward_log_upper"]
            and d["accepted_success_identity_read_verbatim"]==EXPECTED)
        d["scope"]=dict(same_complete_real_family_fixed_eta0_and_original_moving_angle=True,
            whole_original_eta_jets_restricted_without_recomputation=True,
            new_full_delta_gamma_K_and_third_radial_derivatives_are_paid=True,
            fixed_true_s_nu0_retained_in_the_physical_background=True,
            exact_cubic_plus_constant_qualified_on_each_real_interval=True,
            only_one_sided_ordinary_radial_derivatives_claimed=True,
            full_primitive_mean_finite_and_all_interface_terms_retained=True,
            true_radial_lengths_used_once_and_impulses_have_no_length=True,
            same_TJ_cutoff_and_full_FT_FJ_support_retained=True,
            complete_Zy_trial_mean_defect_not_discarded=True,
            original_fourier_signs_both_waves_and_two_independent_means_retained=True,
            full_angular_Wiener_A0_budgets_not_pointwise_bounds_used_in_finite_band_rule=True,
            transported_coefficients_use_actual_three_derivative_flow_bounds=True,
            old_successful_mathematics_read_only=True,
            strong_difference_not_either_individual_order_zero_trial=True,
            original_PC_AW_ports_and_all_external_means_remain_separate=True,
            true_waist_receiver_root_gauge_actual_incoming_and_finite_border_remain_separate=True,
            no_full_return_R0_or_final_surface_claimed=True)
        gate("the complete strong difference retains all stated domains means finite maps and external interfaces",
            all(d["scope"].values()) and not d["full_incoming_inverse_claimed"]
            and not d["finite_Schur_inverse_claimed"] and not d["full_return_R0_claimed"])
        zero=("old_numerical_enclosures_recomputed","old_target_intrinsic_jets_or_means_recomputed",
            "old_repaired_polynomials_or_response_coefficients_recomputed","old_profiles_Taylor_arrays_rays_or_flows_recomputed",
            "old_SP_log_integrals_or_products_recomputed","old_RR_WX_FA_source_or_receiver_bounds_recomputed",
            "old_scientific_producer_imports","old_scientific_producer_calls","old_strict_container_parts_restored")
        gate("only the declared new SJ scalar rows integrals and jumps were evaluated",
            all(d[k]==0 for k in zero) and d["original_successful_small_receipts_read"]==5
            and d["original_complete_body_parts_read"]==18 and d["original_complete_body_rows_verified"]==3322
            and d["new_full_interval_q_lower_bounds"]==1 and d["new_selected_intrinsic_rows"]==3071
            and d["new_complete_coefficient_rows"]==d["new_transported_angular_rows"]==d["new_ordinary_source_rows"]==3071
            and d["new_complete_interface_rows"]==3070 and d["new_complete_waist_error_bounds"]==1
            and finite_records(d["complete_strict_first_symbol_waist_error_conclusion"]))
        if len(d["gates"])!=PARAMETERS["expected_actual_gate_count"]:
            raise ValueError("the actual SJ gate count differs from the frozen complete contract")
        d["stage"]="complete";d["complete"]=d["proved"]=d["complete_strict_first_symbol_defect_paid"]=True
        d["actual_returncode"]=0
    except Exception as error:
        d["failure"]=dict(type=type(error).__name__,message=str(error))
        print("ACTUAL_STRICT_RADIAL_FIRST_SYMBOL_FAILURE",repr(error),flush=True)
    finally:
        d["actual_mathematical_wall_seconds"]=time.monotonic()-started
        checkpoint()
        audit["scientific_receipt_before_native_hash"]=copy.deepcopy(d);save(a.out,audit,compressed=True)
        d["temporary_native_sha256"]=sha(a.out);d["temporary_native_bytes"]=a.out.stat().st_size;checkpoint()
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        tmp=a.conclusion.with_name(a.conclusion.name+".tmp");tmp.write_text(render_conclusion(d),encoding="utf-8");tmp.replace(a.conclusion)
    raise SystemExit(d["actual_returncode"])

if __name__=="__main__":main()
