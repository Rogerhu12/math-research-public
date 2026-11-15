#!/usr/bin/env python3
"""New strict tail from the P22 true branch cut to the accepted waist flow.
All original scalar rows, successful products, source columns and coordinate
closures are immutable inputs. Only the two declared tail products and their
complete endpoint/source readouts are new mathematical arithmetic.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_complete_strict_tail_true_branch_cut_to_waist_v1"
CONTRACT="b15c1630edba1510dc293dea447d4bfe8144680cf73523c3b3b7a237949d5938"
SP_CONTRACT="ae01c213b63ae618e4657b5966604e7fbec4acb4763ea4b8aae848e1a40a40b4"
TN_CONTRACT="0ffa3261e3bb3fdea2cd05afd489b2e71b5587a2bba9432410c492e2ee64f2aa"
TC_CONTRACT="57ff88f5b022b68e78512e485528fd6b5e61b704dfd56a6003d13d24a37f8a07"
STRICT_NATIVE="23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a"
STRICT_SOURCE="c6baae3e8448b4ceec95eeed50a38e8761207b1ca622173c1a8bccce3245b526"
STRICT_PARTS="3f0c7d011248a71061270de37fb13dcc94356bfd49b42b440028565f66e5ad1a"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
SP_RUNTIME=dict(python="3.12.14",python_flint="0.9.0")
EXPECTED=json.loads("{\"accepted_SP_execution\":[\"43731464771\",\"9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a\",\"c77e969bd02ef95d30f16b53ae0a0d3854f596412151e9242ffa0485bd142210\",\"a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12\",20],\"accepted_RR_execution\":[\"43750683671\",\"2a51b8c45974808e65754ebaa0b476650596e7d8a1e36541e9afd3987146c4c9\",\"8822511f1f1c853efd8eec4944bcb74b6954c7fa04c143d9dafc9b470bdd1b4a\",\"a75da290077cf0e134834be5e35a0fa7cd55cd79104f5128d87eaee898af162b\",28],\"accepted_TN_execution\":[\"43752771157\",\"4dbc776babf0e8be12440bb21ac0765e2676c9cea02912326d46f53cfb627256\",\"9e5688400b91714b189e2ed3865cf5448b54bf26d0ff8fef76ba3af06161646e\",\"7abb04effcb8009dafaeec65cf3474e5d045b92c555bb92118544cd47256ee3d\",16],\"accepted_TC_execution\":[\"43754703603\",\"e05b4a9cbe5d66e03a1fb22b70c75ee48cdc885d1bd83c523d9a0173b92b0d71\",\"0e78cfa73d9d2ce8d53fc8eb1c0bdffef276739360aa66f55f13ea13f5ab3c45\",\"37c2a5ae3b77e7f0895aa0c3130d8707868816f1d26a119a880272f9b92f902e\",18]}")
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_old_strict_cut\":\"2333968743003/10000000000000\",\"exact_original_strict_endpoint\":\"1191939371497/5000000000000\",\"exact_true_branch_cut\":\"76285779072683/320000000000000\",\"exact_compact_support\":[\"1/20\",\"9/50\"],\"exact_centre_repair_A0\":\"0.000000000000000003861\",\"exact_centre_repair_angle_A0\":\"0.00000000000000001970\",\"canonical_response_pair_A0\":\"19\",\"canonical_response_pair_angle_A0\":\"83\",\"original_parameter_half_width\":\"1/1000000000\",\"original_strict_complete_rows\":3071,\"original_strict_container_parts\":5,\"original_old_cut_row\":2803,\"original_final_norm_row\":790,\"original_final_body_row\":3070,\"expected_actual_gate_count\":25,\"exponential_series_degree\":18,\"exponential_scaled_row_norm_upper\":\"1/4\",\"complete_mean_coordinates\":2,\"physical_frequency\":\"n=4|j|\",\"strict_state\":\"sqrt(q)*(L2 norm of I*T(q)*h, Euclidean norm of mean(T(q)*h))\",\"density_state\":\"(I*w,mean(w)), w=(a_phys^2/m^2)*T(q)*h\",\"physical_column_input\":\"H^(-4/3), both reference columns and both signs |j|>=97\",\"physical_column_output\":\"waist old-circle L2 density pair plus two independent means\",\"new_body_norm_forcing_archives_restored\":0,\"old_successful_scientific_calls_allowed\":0,\"full_incoming_or_high_BVP_or_return_R0_claimed\":false}")
ROOTS=tuple(map(Q,PARAMETERS["exact_root_interval"]))
RS=Q(PARAMETERS["exact_old_strict_cut"])
RA=Q(PARAMETERS["exact_original_strict_endpoint"])
RC=Q(PARAMETERS["exact_true_branch_cut"])
NATIVE_NAME="temporary-complete-strict-tail-true-cut-to-waist.json.gz"

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
def payload_sha(x):return hashlib.sha256(canonical(x)[:-1]).hexdigest()
def read(p):return json.loads(Path(p).read_bytes())
def save(p,x,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);raw=canonical(x)
    if not compressed and len(raw)>60000:raise ValueError("complete small scientific receipt exceeds 60000 bytes")
    body=gzip.compress(raw,mtime=0) if compressed else raw
    t=p.with_name(p.name+".partial");t.write_bytes(body);t.replace(p)
def ex(x):
    f=Q(x);return arb(f.numerator)/arb(f.denominator)
def rb(v):
    if isinstance(v,arb):x=v
    elif isinstance(v,(int,Q)):x=ex(v)
    elif isinstance(v,str):x=arb(v)
    elif "lower" in v and "upper" in v:x=arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    else:x=arb(v["ball"])
    if not x.is_finite():raise ValueError("a complete original or new scalar is not finite")
    return x
def up(v):return rb(v).upper()
def au(v):return abs(rb(v)).upper()
def gap(v,label):
    x=rb(v).lower()
    if not x>0:raise ValueError("unproved complete positive gap: "+label)
    return x
def rec(v):return {"ball":rb(v).str(52)}
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return v
def check(p,n,digest):
    p=Path(p)
    if not p.is_file() or p.stat().st_size!=n or sha(p)!=digest:raise ValueError("complete input identity differs: "+str(p))
def relpath(x):
    p=Path(x)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(TOPIC):raise ValueError("input leaves topic")
    return p
def accepted(path,identity,gate):
    run,source,manifest,digest,ngates=identity;e=read(path);r=e.get("actual_scientific_receipt",{})
    # SP's exact historical schema records only these two runtime keys.
    runtime=SP_RUNTIME if (run,source)==tuple(EXPECTED["accepted_SP_execution"][:2]) else RUNTIME
    gate("accepted complete run "+run+"/1 retains its exact success and historical runtime schema",
        sha(path)==digest and str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==runtime
        and len(r.get("gates",[]))==ngates and all(x.get("passed") is True for x in r["gates"]))
    return r
def eye():return [[arb(1),arb(0)],[arb(0),arb(1)]]
def mm(a,b):return [[up(sum((a[i][k]*b[k][j] for k in range(2)),arb(0))) for j in range(2)] for i in range(2)]
def matrix(v):
    if not isinstance(v,list) or len(v)!=2 or any(len(r)!=2 for r in v):raise ValueError("comparison is not a complete two-state matrix")
    a=[[up(x) for x in r] for r in v]
    if not all(x>=0 for r in a for x in r):raise ValueError("comparison matrix has a negative entry")
    return a
def scale(a,c):return [[up(c*x) for x in r] for r in a]
def frob(a):return up(up(sum((x*x for r in a for x in r),arb(0))).sqrt())
def positive_exp(a,length):
    z=scale(a,ex(length));r=max(up(sum(row,arb(0))) for row in z);squarings=0
    while r>ex(PARAMETERS["exponential_scaled_row_norm_upper"]):
        z=scale(z,ex(Q(1,2)));r=up(r/2);squarings+=1
        if squarings>64:raise ValueError("new positive exponential requires excessive scaling")
    degree=PARAMETERS["exponential_series_degree"];power=eye();total=eye()
    for k in range(1,degree+1):
        power=mm(power,z)
        total=[[up(total[i][j]+power[i][j]/math.factorial(k)) for j in range(2)] for i in range(2)]
    den=gap(1-r/(degree+2),"positive scalar exponential series tail")
    tail=up(r**(degree+1)/math.factorial(degree+1)/den)
    total=[[up(x+tail) for x in row] for row in total]
    for _ in range(squarings):total=mm(total,total)
    if not all(total[i][j]>=int(i==j) for i in range(2) for j in range(2)):
        raise ValueError("complete nonnegative exponential does not dominate identity")
    return total,squarings,tail

def same_objects(S,R,T,C,sp_source,gate,doc):
    common=("exact_real_delta_radius","exact_root_interval","fixed_intrinsic_parameter")
    gate("all accepted conclusions use the same exact real family while retaining the three distinct cuts",
        all(x["mathematical_parameters"][k]==PARAMETERS[k] for x in (S,R,T,C) for k in common)
        and S["mathematical_parameters"]["exact_strict_interval"]==["0",str(RS)]
        and all(x["mathematical_parameters"]["exact_strict_cut"]==str(RC) for x in (R,T,C))
        and Q(9,50)<RS<RA<RC<ROOTS[0]<=ROOTS[1]
        and RA==ROOTS[0]-Q(9,10**6) and RC==ROOTS[0]-Q(1,262144)
        and RS==ROOTS[1]-Q(1,200)
        and S["exact_family_identity"]["continuous_centre_definition_sha256"]=="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
        and S["exact_family_identity"]["continuous_response_definition_sha256"]=="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04")
    phys=R["complete_physical_comparison_conclusion"];ident=R["complete_original_cut_identity_conclusion"]
    gate("the complete raw physical columns and cut identity are the literal RR objects in both later successes",
        T["complete_original_cut_identity_read_verbatim"]==ident
        and C["complete_original_cut_identity_read_verbatim"]==ident
        and T["complete_normalized_physical_conclusion"]["saved_complete_physical_conclusion_read_verbatim"]==phys
        and C["accepted_complete_physical_payload_sha256"]==payload_sha(phys)
        and len(R["complete_original_cut_input_conclusion"])==len(T["complete_original_cut_input_conclusion"])==1
        and phys["complete_cut_sides"]==1
        and phys["all_output_modes_finite_head_and_both_mean_coordinates_retained"] is True)
    flow=S["complete_strict_propagation_conclusion"];end=S["complete_endpoint_readout_conclusion"]
    gate("the original source makes the saved curvature cost a whole zero-to-ra budget and not an old-cut-only fee",
        'qright=interval(strict["rows"][-1]["base"]["q"])' in sp_source
        and 'cminus=up(oldc+jq)' in sp_source
        and 'cplus=up(oldc+jq+(qright.upper()/qleft.lower()).log())' in sp_source
        and flow["old_grouped_reverse_log_upper"]=="4.386425547"
        and flow["exact_interval"]==["0",str(RS)]
        and end["exact_cut"]==str(RS) and end["one_sided_cut_rows"]==[2803]
        and flow["all_shorter_ordered_products_and_source_insertions_included"] is True
        and flow["affine_jumps_are_independent_without_radial_length_factor"] is True
        and flow["both_one_sided_original_scalar_germs_retained"] is True
        and up(flow["new_complete_reverse_log_upper"])>=0 and up(flow["new_complete_forward_log_upper"])>=0)
    original=dict(
        saved_SP_forward_complete_matrix_read_verbatim=copy.deepcopy(flow["forward_complete_matrix"]),
        saved_SP_reverse_complete_matrix_read_verbatim=copy.deepcopy(flow["reverse_complete_matrix"]),
        saved_SP_forward_full_0_ra_log_upper_read_verbatim=copy.deepcopy(flow["new_complete_forward_log_upper"]),
        saved_SP_reverse_full_0_ra_log_upper_read_verbatim=copy.deepcopy(flow["new_complete_reverse_log_upper"]),
        saved_SP_complete_boundary_row_maxima_read_verbatim=copy.deepcopy(flow["complete_selected_scalar_maxima"]),
        saved_SP_waist_radial_factors_read_verbatim=copy.deepcopy(end["waist_complete_radial_factors"]),
        saved_SP_original_source_injection_read_verbatim=copy.deepcopy(end["complete_strict_Hminus1_source_injection_upper"]),
        original_RR_complete_physical_payload_sha256=payload_sha(phys),
        original_RR_cut_identity_payload_sha256=payload_sha(ident),
        exact_family_identity_read_verbatim=copy.deepcopy(S["exact_family_identity"]),
        old_normalizer_radius_1over200_not_used_at_P22=True)
    doc["complete_accepted_original_conclusion"]=original
    doc["original_successful_small_receipts_read"]=4
    doc["saved_complete_SP_products_read"]=2
    doc["saved_complete_SP_boundary_row_closures_read"]=1
    doc["saved_complete_physical_columns_read"]=4
    return flow,end,phys

def restore_strict(paths,gate,doc):
    parts=read(paths["strict_parts_manifest"])
    if not (parts["kind"]=="complete_native_lossless_container_binary_parts_v2"
        and parts["original_bytes"]==8499033 and parts["original_sha256"]==STRICT_NATIVE
        and parts["original_source_sha256"]==STRICT_SOURCE and parts["complete_native_rows"]==3071
        and parts["native_complete"] is True and parts["native_failure"] is None and len(parts["parts"])==5):
        raise ValueError("original strict container identity changed")
    payload=[];offset=0;receipts=[]
    for i,e in enumerate(parts["parts"]):
        p=paths["strict_parts_manifest"].parent/e["file"]
        check(p,e["compressed_bytes"],e["compressed_sha256"]);b=gzip.decompress(p.read_bytes())
        if not (e["index"]==i and e["offset"]==offset and len(b)==e["bytes"] and hashlib.sha256(b).hexdigest()==e["sha256"]):
            raise ValueError("original strict container slice is incomplete or changed")
        payload.append(b);offset+=len(b)
        receipts.append(dict(index=i,offset=e["offset"],bytes=len(b),sha256=e["sha256"],
            compressed_bytes=e["compressed_bytes"],compressed_sha256=e["compressed_sha256"]))
    original=b"".join(payload)
    gate("the five immutable containers restore the entire original strict certificate without any producer",
        len(original)==8499033 and hashlib.sha256(original).hexdigest()==STRICT_NATIVE)
    native=json.loads(gzip.decompress(original));rows=native.get("rows",[]);edge=Q(0);valid=True
    for i,row in enumerate(rows):
        left,right=map(Q,row["interval"]);gl,gr=map(Q,row["actual_scalar_germ"])
        valid=valid and row["common_row"]==i and left==edge and gl<=left<right<=gr;edge=right
    gate("all 3071 original rows closed germs original parameter and complete mean identities remain intact",
        native.get("kind")==parts["native_kind"] and native.get("complete") is True
        and native.get("failure") is None and native.get("source_sha256")==STRICT_SOURCE
        and native["exact_requested_interval"]==["0",str(RA)]
        and native["total_closed_radial_cells"]==len(rows)==3071 and edge==RA and valid
        and native["original_parameter_half_width"]==PARAMETERS["original_parameter_half_width"]
        and native.get("whole_affine_parameter_interval") is True
        and native.get("complete_original_intrinsic_tail") is True
        and native.get("all_Fourier_variations_and_mean_retained") is True)
    doc["original_complete_strict_rows_verified"]=3071;doc["original_strict_container_parts_read"]=5
    doc["complete_strict_recovery_conclusion"]=dict(original_native_bytes=len(original),original_native_sha256=STRICT_NATIVE,
        original_part_receipts=receipts,original_full_cover=["0",str(RA)],
        historical_restore_commit="a3d84d905ce72e3a854874bbe98d119623f3f8de",
        complete_original_target_enclosures_read_not_recomputed=True)
    return rows

def first_tail_cover(rows,flow,end,gate,doc):
    segments=[];edge=RS;boundary=[]
    for row in rows:
        sl,sr=map(Q,row["interval"]);left=max(RS,sl);right=min(RA,sr)
        if not left<right:continue
        if left!=edge or not sl<=left<right<=sr:raise ValueError("new first tail has a gap or leaves its original whole row")
        kind="saved_boundary_row" if sl<RS<sr or sl==RS else "new_tail_scalar"
        if kind=="saved_boundary_row":boundary.append(row["common_row"])
        segments.append((left,right,row,kind));edge=right
    gate("the new first tail covers exactly rs-to-ra and the single old-cut whole-row closure is reused",
        edge==RA and segments and segments[0][0]==RS and segments[-1][1]==RA
        and boundary==end["one_sided_cut_rows"]==[2803]
        and sum((r-l for l,r,_,_ in segments),Q(0))==RA-RS
        and all(Q(row["interval"][0])>Q(9,50) for _,_,row,_ in segments)
        and all(k in flow["complete_selected_scalar_maxima"] for k in (
            "complete_R","complete_L","complete_D","A_upper","Bphi_upper","N_y_upper","N_z_upper","N_gamma_upper")))
    cover=[dict(interval=[str(l),str(r)],original_strict_row=row["common_row"],
        original_whole_interval=row["interval"],original_scalar_germ=row["actual_scalar_germ"],closure_kind=kind)
        for l,r,row,kind in segments]
    doc["complete_new_tail_cover_conclusion"]=dict(first_interval=[str(RS),str(RA)],second_interval=[str(RA),str(RC)],
        first_tail_intersections=len(segments),boundary_whole_row_reused=boundary,
        new_first_tail_scalar_rows=len(segments)-len(boundary),first_tail_cover_sha256=payload_sha(cover),
        old_prefix_scalar_rows_recomputed=0,original_seams_and_one_sided_bounds_retained=True)
    return segments,cover

def final_saved_inputs(R,T,gate,doc):
    r=R["complete_original_cut_input_conclusion"][0];t=T["complete_original_cut_input_conclusion"][0]
    p=R["complete_physical_cut_coefficient_conclusion"][0]
    root=R["complete_root_mean_value_conclusion"][0]
    nl,nr=map(Q,t["exact_interval"]);bl,br=map(Q,r["exact_original_intrinsic_interval"])
    gl,gr=map(Q,r["actual_scalar_germ"])
    gate("the complete original norm790 and signed body3070 cover the new ra-to-cut-to-root segment in one germ",
        nl==RA and nr==ROOTS[0] and nl<=RA<RC<=nr
        and Q(9,50)<bl<=RA<RC<ROOTS[0]<=ROOTS[1]<=br and gl<=bl<br<=gr
        and t["original_norm_row"]==r["original_norm_row"]==p["original_norm_row"]==790
        and t["original_common_row"]==r["original_common_row"]==3070
        and t["exact_interval"]==r["exact_original_interval"]
        and t["complete_q_bounds_read_verbatim"]==root==p["root_mean_value_q_bounds"]
        and root["original_signed_whole_K1_read_verbatim"]==r["original_signed_whole_K1_read_verbatim"]
        and root["whole_segment_in_one_original_germ"] is True)
    krlo=gap(root["complete_Kr_lower"],"saved entire Kr lower");krhi=up(root["complete_Kr_upper"])
    qlo=gap(root["q_lower"],"saved entire cut q lower");qhi=up(root["q_upper"])
    mn=gap(p["complete_absolute_mean_lower"],"saved entire actual mean gap")
    gate("the original outward signed curvature and the saved cut gap are read literally without repeating FTC",
        gap(r["original_signed_whole_K1_read_verbatim"],"original whole outward K1")>0
        and krlo>0 and krhi>=krlo and qhi>=qlo and mn>0
        and root["exact_root_distance"]==[str(ROOTS[0]-RC),str(ROOTS[1]-RC)]
        and root["original_zero_order_curvature_enclosure_not_overwritten"] is True)
    old=dict(norm_row=790,body_row=3070,norm_whole_interval=t["exact_interval"],
        body_whole_interval=r["exact_original_intrinsic_interval"],same_scalar_germ=r["actual_scalar_germ"],
        full_selected_norm_inputs_read_verbatim=copy.deepcopy(t["original_complete_norm_inputs_read_verbatim"]),
        whole_beta_read_verbatim=copy.deepcopy(t["original_complete_intrinsic_ordinary_jets_read_verbatim"]["beta"][0]),
        signed_mean_read_verbatim=copy.deepcopy(r["original_signed_complete_mean_read_verbatim"]),
        physical_radius_read_verbatim=copy.deepcopy(r["original_physical_radius_read_verbatim"]),
        root_mean_value_conclusion_read_verbatim=copy.deepcopy(root),
        original_complete_cut_ng_upper_read_verbatim=copy.deepcopy(p["complete_ng_upper"]),
        original_complete_cut_mean_lower_read_verbatim=copy.deepcopy(p["complete_absolute_mean_lower"]),
        original_primitive_mean_multiplier_read_verbatim=copy.deepcopy(p["complete_primitive_and_mean_multiplier"]),
        original_norm_row_sha256=t["original_saved_norm_row_sha256"],
        original_forcing_row_sha256=t["original_saved_forcing_row_sha256"],
        no_old_forcing_norm_or_body_arrays_restored=True)
    doc["complete_final_saved_input_conclusion"]=old;doc["saved_final_norm_rows_read"]=1;doc["saved_signed_K1_rows_read"]=1
    return old,dict(krlo=krlo,krhi=krhi,qlo=qlo,qhi=qhi,mn=mn,ncplus=up(p["complete_ng_upper"]),
        CI=up(p["complete_primitive_and_mean_multiplier"]))

def comparison(v,rate):
    A,Ny,B1,Nz,Ng=v["A"],v["Ny"],v["Bphi"],v["Nz"],v["Ngamma"];D=v["D"]
    return [[max(arb(0),up(rate+D+(A+Ny)/4)),up(D/2+B1/16+(Nz+Ng)/4)],
            [up(A+Ny),max(arb(0),up(rate+Nz))]]
def nonlocal_fees(b,g,R,L,D):
    return dict(beta=b,gamma=g,R=R,L=L,D=D,Bphi=up(4*b*R*L),A=up(6*b*R*L),
        Ny=up(2*b*L*(R+L/4)),Nz=up(b*L*R/2),Ngamma=up(g*L))
def final_cell(old,k,gate,doc):
    n=old["full_selected_norm_inputs_read_verbatim"]
    qa=up(up(k["krhi"]*ex(ROOTS[1]-RA)).sqrt())
    U0,U1=map(up,n["U"]);V0,V1=map(up,n["V"]);D=up(n["D"][1])
    b=au(old["whole_beta_read_verbatim"]);g=up(up(n["eta_upper"])/k["mn"])
    R=up(up(U0*U0+qa*qa*V0*V0).sqrt());L=up(up(U1*U1+qa*qa*V1*V1).sqrt())
    v=nonlocal_fees(b,g,R,L,D);rate=up(b*(1+3*R*R)+D/2);v.update(qplus=qa,forward_rate=rate,reverse_rate=rate)
    ap=comparison(v,rate);am=comparison(v,rate)
    gate("the final full-family scalar row uses saved U_V_D_eta and a new same-Kr endpoint bound with no double repair",
        all(x.is_finite() and x>=0 for x in v.values())
        and qa>=k["qlo"] and gap(n["eta_lower"],"saved full eta lower")>0
        and all(x.is_finite() and x>=0 for m in (ap,am) for row in m for x in row))
    doc["complete_final_tail_scalar_conclusion"]=dict(exact_interval=[str(RA),str(RC)],original_norm_row=790,original_body_row=3070,
        complete_new_scalar_bounds=encode(v),complete_forward_comparison_matrix=encode(ap),
        complete_reverse_comparison_matrix=encode(am),gamma_method="eta_upper / original complete absolute mean lower",
        q_at_ra_method="sqrt(saved Kr upper * (original root upper - ra))",
        full_selected_state_inputs_not_repaired_again=True,all_nonlocal_columns_and_both_means_retained=True)
    doc["new_final_tail_scalar_rows"]=1;doc["new_ra_curvature_endpoint_bounds"]=1
    return ap,am,v

def first_cell(row,kind,maximum):
    base=row["base"];strong=row["strong"];target=row["actual_target"]
    b=au(target["beta"]);qold=rb(base["q"]);qp=qold.upper()
    gap(qold,"old whole strict q");gap(target["gamma"],"old whole strict gamma")
    if not rb(target["K"]).upper()<0:raise ValueError("original entire strict negative type lost")
    if kind=="saved_boundary_row":
        v={key:up(maximum[field]) for key,field in (
            ("R","complete_R"),("L","complete_L"),("D","complete_D"),("A","A_upper"),
            ("Bphi","Bphi_upper"),("Ny","N_y_upper"),("Nz","N_z_upper"),("Ngamma","N_gamma_upper"))}
        rate=up(b*(1+3*v["R"]*v["R"])+v["D"]/2)
        v.update(beta=b,qplus=qp,forward_rate=rate,reverse_rate=rate)
        return comparison(v,rate),comparison(v,rate),v
    e0=ex(PARAMETERS["exact_centre_repair_A0"])+19*ex(PARAMETERS["exact_real_delta_radius"])
    e1=ex(PARAMETERS["exact_centre_repair_angle_A0"])+83*ex(PARAMETERS["exact_real_delta_radius"])
    R0=up(base["actual_R_upper"]);L0=up(base["actual_L_upper"]);V0=up(base["v_abs_upper"])
    R=up(R0+max(arb(1),qp)*e0);L=up(L0+max(arb(1),qp)*e1)
    ds=up(2*R0*e0+e0*e0+au(target["K"])*(2*V0*e0+e0*e0))
    D=up(au(base["actual_d_phi"])+2*b*ds)
    F0=max(up(base["forward_diagonal_1"]),up(strong["forward_Y2_rate"]))
    B0=max(up(-rb(base["forward_diagonal_1"])),up(strong["backward_Y2_rate"]))
    fp=up(F0+4*b*ds);fm=up(B0+4*b*ds)
    v=nonlocal_fees(b,up(target["gamma"]),R,L,D)
    v.update(qplus=qp,forward_rate=fp,reverse_rate=fm,complete_state_square_difference=ds)
    return comparison(v,fp),comparison(v,fm),v

def propagate(segments,flow,last,gate,doc,checkpoint):
    plus=eye();minus=eye();audits=[];maximum={};sqmax=0;count=0;newrows=0;boundary=0
    for left,right,row,kind in segments:
        ap,am,v=first_cell(row,kind,flow["complete_selected_scalar_maxima"])
        ep,sp,tp=positive_exp(ap,right-left);em,sm,tm=positive_exp(am,right-left)
        plus=mm(ep,plus);minus=mm(minus,em);count+=2;sqmax=max(sqmax,sp,sm)
        newrows+=int(kind=="new_tail_scalar");boundary+=int(kind=="saved_boundary_row")
        for name,value in v.items():maximum[name]=value if name not in maximum else max(maximum[name],value)
        audits.append(dict(interval=[str(left),str(right)],original_strict_row=row["common_row"],closure_kind=kind,
            complete_scalar_bounds=encode(v),complete_forward_matrix=encode(ap),complete_reverse_matrix=encode(am),
            positive_forward_exponential=encode(ep),positive_reverse_exponential=encode(em),
            complete_series_tail_upper=encode([tp,tm])))
        if len(audits)%16==0:
            doc["complete_new_tail_progress"]=dict(completed_first_tail_rows=len(audits),last_original_row=row["common_row"],
                exact_completed_interval=[str(RS),str(right)],complete_forward_prefix=encode(plus),
                complete_reverse_prefix=encode(minus),successful_new_exponentials=count,
                completed_new_scalar_rows=newrows,old_cut_row_closures_recomputed=0)
            checkpoint()
    gate("only previously unused first-tail lengths receive new exponentials and the old boundary closure stays read-only",
        boundary==1 and newrows==len(segments)-1 and count==2*len(segments)
        and all(l>=RS and r<=RA for l,r,_,_ in segments))
    first_plus=plus;first_minus=minus;ap,am,v=last
    ep,sp,tp=positive_exp(ap,RC-RA);em,sm,tm=positive_exp(am,RC-RA)
    plus=mm(ep,plus);minus=mm(minus,em);count+=2;sqmax=max(sqmax,sp,sm)
    for name,value in v.items():maximum[name]=value if name not in maximum else max(maximum[name],value)
    audits.append(dict(interval=[str(RA),str(RC)],original_norm_row=790,original_body_row=3070,
        closure_kind="new_final_saved_scalar",complete_scalar_bounds=encode(v),
        complete_forward_matrix=encode(ap),complete_reverse_matrix=encode(am),
        positive_forward_exponential=encode(ep),positive_reverse_exponential=encode(em),
        complete_series_tail_upper=encode([tp,tm])))
    gate("the complete two-tail products retain every true length and both chronological orders",
        count==2*(len(segments)+1) and len(audits)==len(segments)+1
        and all(x.is_finite() and x>=0 for mat in (plus,minus) for row in mat for x in row))
    old=doc["complete_final_saved_input_conclusion"]
    qclo=gap(old["root_mean_value_conclusion_read_verbatim"]["q_lower"],"saved cut q lower")
    c2=up((v["qplus"]/qclo).log())
    gate("only the final positive-Kr reverse log is added and no prior scalar upper is subtracted",
        c2.is_finite() and c2>=0
        and gap(old["root_mean_value_conclusion_read_verbatim"]["complete_Kr_lower"],"entire Kr lower")>0)
    oldplus=matrix(flow["forward_complete_matrix"]);oldminus=matrix(flow["reverse_complete_matrix"])
    fullplus=mm(plus,oldplus);fullminus=scale(mm(oldminus,minus),up(c2.exp()))
    gate("saved SP matrices and both new tail matrices compose in their complete physical orders",
        all(x.is_finite() and x>=0 for mat in (fullplus,fullminus) for row in mat for x in row)
        and all(plus[i][j]>=int(i==j) and minus[i][j]>=int(i==j) for i in range(2) for j in range(2)))
    conclusion=dict(exact_complete_interval=["0",str(RC)],exact_new_tail_interval=[str(RS),str(RC)],
        complete_first_tail_forward_product=encode(first_plus),complete_first_tail_reverse_product=encode(first_minus),
        complete_final_tail_forward_exponential=encode(ep),complete_final_tail_reverse_exponential=encode(em),
        complete_new_tail_forward_product=encode(plus),complete_new_tail_reverse_product=encode(minus),
        complete_new_final_reverse_log_upper=rec(c2),complete_new_final_forward_log_upper=rec(arb(0)),
        complete_forward_matrix=encode(fullplus),complete_reverse_matrix=encode(fullminus),
        complete_forward_operator_upper=rec(frob(fullplus)),complete_reverse_operator_upper=rec(frob(fullminus)),
        complete_new_tail_scalar_maxima=encode(maximum),complete_new_tail_row_count=len(audits),
        complete_new_tail_audit_sha256=payload_sha(audits),
        original_0_ra_curvature_cost_reused_as_one_whole_budget=True,
        original_prefix_matrices_read_verbatim=True,no_old_upper_subtraction_or_division=True,
        all_shorter_ordered_subproducts_and_affine_insertions_retained=True,
        complete_both_mean_and_all_Fourier_coordinates_retained=True)
    doc["complete_new_strict_propagation_conclusion"]=conclusion
    doc["new_first_tail_scalar_rows"]=newrows;doc["saved_boundary_row_closures_used"]=boundary
    doc["new_positive_two_state_exponentials"]=count;doc["new_tail_products"]=2;doc["new_complete_interval_products"]=2
    doc["new_reverse_curvature_log_fees"]=1;doc["positive_exponential_max_scaling_squarings"]=sqmax
    doc.pop("complete_new_tail_progress",None);checkpoint()
    return fullplus,fullminus,maximum,audits

def endpoint_readouts(end,old,k,T,C,upmat,ummat,maximum,gate,doc):
    waist=end["waist_complete_radial_factors"]
    alo=gap(old["physical_radius_read_verbatim"],"saved whole physical radius lower")
    mp=au(old["signed_mean_read_verbatim"])
    if not rb(old["signed_mean_read_verbatim"]).upper()<0:raise ValueError("complete original mean sign changed")
    ncminus=(alo*alo/(mp*mp)).lower();gap(ncminus,"new opposite radial ng denominator")
    o0=up(up(waist["density_radial_factor_upper"])/gap(waist["q_lower"],"waist q lower").sqrt())
    i0=up(up(waist["q_upper"]).sqrt()/gap(waist["density_radial_factor_lower"],"waist ng lower"))
    oc=up(k["ncplus"]/k["qlo"].sqrt());ic=up(k["qhi"].sqrt()/ncminus)
    uf=frob(upmat);ub=frob(ummat);back=up(o0*ub*ic);forward=up(oc*uf*i0)
    gate("both true endpoint radial directions have complete positive a_mean_q_ng denominators",
        ncminus>0 and k["ncplus"]>=ncminus and all(x.is_finite() and x>0 for x in (o0,i0,oc,ic,ub,uf,back,forward)))
    jtail=up(k["CI"]*max(arb(1),maximum["qplus"]))
    inj=max(up(end["complete_strict_Hminus1_source_injection_upper"]),jtail)
    backsrc=up(o0*ub*inj);forwardsrc=up(oc*uf*inj);length=ex(RC).sqrt()
    gate("complete volume sources retain the saved prefix injection true tail length and independent zero-length impulses",
        inj>=1 and backsrc.is_finite() and forwardsrc.is_finite()
        and all(up(x).is_finite() for x in (backsrc*length,forwardsrc*length)))
    sel=T["complete_selected_normalizer_conclusion"];selected=sel["complete_selected_cutoff_window_verdicts"]["L2"]
    coord=C["complete_density_coordinate_conclusion"]
    fN=up(selected["complete_forward_upper"]);kN=up(selected["ordered_inverse_upper"])
    a0=up(coord["complete_density_L2_upper"]);b0=up(coord["complete_inverse_density_L2_upper"])
    phaseback=up(back*fN*a0);phaseforward=up(b0*kN*forward)
    gate("true-phase endpoint maps use the ordered forward inverse normalizers and only the same L2 coordinate window",
        selected["both_strict_tests_passed"] is True and sel["all_HL_LH_blocks_and_both_independent_means_retained"] is True
        and sel["same_inverse_on_common_trigonometric_domain"] is True
        and coord["independent_physical_mean_block_is_identity"] is True
        and all(x.is_finite() and x>=1 for x in (fN,kN,a0,b0))
        and phaseback.is_finite() and phaseforward.is_finite())
    out=dict(complete_new_cut_ng_lower=rec(ncminus),saved_complete_cut_ng_upper_read_verbatim=copy.deepcopy(old["original_complete_cut_ng_upper_read_verbatim"]),
        complete_new_cut_absolute_mean_upper=rec(mp),complete_new_cut_physical_radius_lower=rec(alo),
        waist_output_factor=rec(o0),waist_input_factor=rec(i0),cut_output_factor=rec(oc),cut_input_factor=rec(ic),
        complete_raw_cut_to_waist_density_upper=rec(back),complete_waist_to_raw_cut_density_upper=rec(forward),
        saved_prefix_source_injection_read_verbatim=copy.deepcopy(end["complete_strict_Hminus1_source_injection_upper"]),
        complete_new_tail_source_injection_upper=rec(jtail),complete_source_injection_upper=rec(inj),
        strict_L1_Hminus1_source_to_waist_density_upper=rec(backsrc),
        strict_L2_Hminus1_source_to_waist_density_upper=rec(up(length*backsrc)),
        strict_L1_Hminus1_source_to_raw_cut_density_upper=rec(forwardsrc),
        strict_L2_Hminus1_source_to_raw_cut_density_upper=rec(up(length*forwardsrc)),
        affine_raw_state_jump_to_waist_density_upper=rec(backsrc),
        affine_raw_state_jump_to_raw_cut_density_upper=rec(forwardsrc),
        true_phase_normalized_cut_to_waist_upper=rec(phaseback),
        waist_to_true_phase_normalized_cut_upper=rec(phaseforward),
        strict_L1_Hminus1_source_to_true_phase_normalized_cut_upper=rec(up(b0*kN*forwardsrc)),
        strict_L2_Hminus1_source_to_true_phase_normalized_cut_upper=rec(up(b0*kN*length*forwardsrc)),
        saved_TN_L2_forward_normalizer_read_verbatim=copy.deepcopy(selected["complete_forward_upper"]),
        saved_TN_L2_inverse_normalizer_read_verbatim=copy.deepcopy(selected["ordered_inverse_upper"]),
        saved_TC_L2_density_read_verbatim=copy.deepcopy(coord["complete_density_L2_upper"]),
        saved_TC_L2_inverse_density_read_verbatim=copy.deepcopy(coord["complete_inverse_density_L2_upper"]),
        exact_full_radial_length=str(RC),volume_source_window="L1 or L2 true dr with full H^(-1) moving-circle state",
        affine_impulse_is_a_raw_state_jump_not_a_density_jump=True,
        affine_impulses_have_no_radial_length_factor=True,
        density_impulses_require_their_own_radial_entry_factor=True,
        both_independent_means_and_complete_finite_blocks_retained=True,
        old_N_radius_1over200_not_moved_to_the_true_cut=True)
    doc["complete_endpoint_and_source_conclusion"]=out;doc["new_endpoint_readout_conclusions"]=1
    return back,out

def complete_physical_columns(physical,gain,gate,doc):
    keys=("error_density_0","error_density_1","free_R2","free_R3");rows=[]
    for old in physical["complete_physical_cut_rows"]:
        bound={k:copy.deepcopy(old["complete_four_physical_pieces"][k]["complete_old_circle_density_and_two_means_upper"]) for k in keys}
        new={k:rec(up(gain*up(bound[k]))) for k in keys}
        total=rec(up(gain*up(old["complete_four_piece_sum_upper"])))
        rows.append(dict(original_norm_row=old["original_norm_row"],saved_complete_four_columns_read_verbatim=bound,
            saved_complete_same_case_sum_read_verbatim=copy.deepcopy(old["complete_four_piece_sum_upper"]),
            complete_four_waist_columns_upper=new,complete_same_case_waist_sum_upper=total))
    gate("each complete RR physical column reaches the waist with one new raw state continuation factor",
        len(rows)==physical["complete_cut_sides"]==1
        and all(set(x["complete_four_waist_columns_upper"])==set(keys) for x in rows)
        and physical["all_output_modes_finite_head_and_both_mean_coordinates_retained"] is True)
    worst=max(up(x["complete_same_case_waist_sum_upper"]) for x in rows)
    gate("complete same-side four-piece sums are multiplied before the side maximum and all root input labels remain",
        worst.is_finite() and all(up(v).is_finite() for x in rows for v in x["complete_four_waist_columns_upper"].values())
        and physical["input_window"]==PARAMETERS["physical_column_input"]
        and physical["exact_strict_cut"]==str(RC)
        and physical["both_reference_columns_and_input_signs"] is True)
    doc["complete_waist_physical_comparison_conclusion"]=dict(complete_case_rows=rows,
        complete_four_waist_column_maxima={k:rec(max(up(x["complete_four_waist_columns_upper"][k]) for x in rows)) for k in keys},
        complete_same_case_sum_maximum_upper=rec(worst),
        original_complete_RR_physical_conclusion_sha256=payload_sha(physical),
        input_window=PARAMETERS["physical_column_input"],output_window=PARAMETERS["physical_column_output"],
        both_reference_columns_both_signs_and_both_means_retained=True,
        one_raw_RR_factor_no_second_normalizer_or_root_input_chart=True,
        no_entrywise_mix_of_different_closed_cut_sides=True,
        complete_incoming_error_or_whole_CE_or_return_R0_not_claimed=True)
    doc["new_complete_waist_physical_columns"]=4*len(rows);doc["new_complete_same_case_waist_sums"]=len(rows)

def render_conclusion(d):
    def show(x):
        if isinstance(x,dict) and "ball" in x:return x["ball"]
        return str(x).replace("|","\\|").replace("\n"," ")
    out=["# Actual complete strict tail from the true branch cut to the waist","",
        "Public run "+str(d["run_id"])+"/"+str(d["run_attempt"]),
        "", "Scientific child exit status: "+str(d["actual_returncode"]),
        "Complete: "+str(d["complete"])+". Proved: "+str(d["proved"])+".",
        "", "The accompanying execution.json preserves the complete scientific receipt: every new scalar ball, both ordered matrices, source and endpoint factors, all four physical columns, original input objects and complete gate outcomes. This report avoids repeating that entire object.","",
        "Ordinary sources, affine impulses, finite modes and both means remain. These are complete continuation and Darboux-comparison contributions; the incoming inverse and the whole return remainder are not asserted.","",
        "## Gates",""]
    out.extend("- "+("PASS " if x["passed"] else "FAIL ")+x["name"] for x in d["gates"])
    cover=d.get("complete_new_tail_cover_conclusion")
    if cover:
        out.extend(["","## Exact new cover","",
            "- First tail: "+str(cover["first_interval"]),
            "- Second tail: "+str(cover["second_interval"]),
            "- Original intersections: "+str(cover["first_tail_intersections"]),
            "- Reused complete boundary row: "+str(cover["boundary_whole_row_reused"]),
            "- New scalar rows in the first tail: "+str(cover["new_first_tail_scalar_rows"]),
            "- Complete cover SHA256: "+cover["first_tail_cover_sha256"]])
    last=d.get("complete_final_tail_scalar_conclusion")
    if last:
        out.extend(["","## Complete final-tail scalar row","",
            "| Quantity | Complete outward ball |","|---|---|"])
        for key in ("qplus","gamma","R","L","D","A","Bphi","Ny","Nz","Ngamma"):
            out.append("| "+key+" | "+show(last["complete_new_scalar_bounds"][key])+" |")
    flow=d.get("complete_new_strict_propagation_conclusion")
    if flow:
        out.extend(["","## Complete ordered propagation","",
            "| Quantity | Complete outward ball |","|---|---|"])
        for key in ("complete_new_final_reverse_log_upper","complete_forward_operator_upper","complete_reverse_operator_upper"):
            out.append("| "+key+" | "+show(flow[key])+" |")
        out.extend(["","Both full matrices and both new tail products are retained in the complete scientific receipt. The original zero-to-ra curvature cost is one whole budget; no old upper is subtracted or divided."])
    ends=d.get("complete_endpoint_and_source_conclusion")
    if ends:
        out.extend(["","## Endpoint and ordinary-source readouts","",
            "| Quantity | Complete outward ball |","|---|---|"])
        for key in ("complete_raw_cut_to_waist_density_upper","complete_waist_to_raw_cut_density_upper",
            "strict_L1_Hminus1_source_to_waist_density_upper","strict_L2_Hminus1_source_to_waist_density_upper",
            "strict_L1_Hminus1_source_to_raw_cut_density_upper","strict_L2_Hminus1_source_to_raw_cut_density_upper",
            "true_phase_normalized_cut_to_waist_upper","waist_to_true_phase_normalized_cut_upper"):
            out.append("| "+key+" | "+show(ends[key])+" |")
        out.extend(["","The complete receipt also retains opposite endpoint denominators, both ordered L2 normalizers, both coordinate directions and phase-coordinate source factors. Raw affine jumps use the corresponding L1 factor with no radial length fee. Density jumps require their own radial entry factor."])
    columns=d.get("complete_waist_physical_comparison_conclusion")
    if columns:
        out.extend(["","## Four complete physical columns at the waist","",
            "| Column | Complete outward ball |","|---|---|"])
        for key,value in columns["complete_four_waist_column_maxima"].items():
            out.append("| "+key+" | "+show(value)+" |")
        out.append("| Complete same-case sum | "+show(columns["complete_same_case_sum_maximum_upper"])+" |")
        out.extend(["","Input: "+columns["input_window"]+". Output: "+columns["output_window"]+". Both signs, both reference columns and both independent means are retained."])
    if d.get("failure"):out.extend(["","## Failure","",json.dumps(d["failure"],sort_keys=True)])
    return "\n".join(out)+"\n"

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","workdir","process","conclusion","out"):parser.add_argument("--"+key,type=Path,required=True)
    a=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new strict-tail arithmetic is permitted only in the actual public Actions runner")
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the frozen public scientific runtime changed")
    ctx.prec=320;a.workdir.mkdir(parents=True,exist_ok=True);start=time.monotonic();audits=[];cover=[]
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,arithmetic_bits=320,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        mathematical_parameters=PARAMETERS,original_successful_small_receipts_read=0,
        original_complete_strict_rows_verified=0,original_strict_container_parts_read=0,
        saved_complete_SP_products_read=0,saved_complete_SP_boundary_row_closures_read=0,
        saved_complete_physical_columns_read=0,saved_final_norm_rows_read=0,saved_signed_K1_rows_read=0,
        saved_boundary_row_closures_used=0,new_first_tail_scalar_rows=0,new_final_tail_scalar_rows=0,
        new_ra_curvature_endpoint_bounds=0,new_reverse_curvature_log_fees=0,new_positive_two_state_exponentials=0,
        new_tail_products=0,new_complete_interval_products=0,new_endpoint_readout_conclusions=0,
        new_complete_waist_physical_columns=0,new_complete_same_case_waist_sums=0,
        old_numerical_enclosures_recomputed=0,old_target_intrinsic_mean_or_repair_recomputed=0,
        old_SP_prefix_or_boundary_scalar_closures_recomputed=0,old_SP_grouped_integral_or_exponential_recomputed=0,
        old_RR_TN_TC_or_source_columns_recomputed=0,old_scientific_producer_calls=0,
        old_forcing_norm_body_natives_restored=0,original_natural_stage_bytes_modified=False,
        complete_strict_tail_to_waist_paid=False,full_incoming_inverse_claimed=False,
        finite_Schur_inverse_claimed=False,full_return_R0_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def checkpoint():save(a.process,d)
    def gate(name,truth):
        okay=bool(truth);d["gates"].append(dict(name=name,passed=okay))
        if not okay:raise ValueError("actual strict-tail gate failed: "+name)
    try:
        m=read(a.manifest)
        gate("the immutable manifest fixes the exact tail contract parameters runtime and historical identities",
            m["source_sha256"]==sha(__file__) and m["contract_sha256"]==CONTRACT
            and m["runtime"]==RUNTIME and m["mathematical_parameters"]==PARAMETERS
            and m["expected_actual_gate_count"]==PARAMETERS["expected_actual_gate_count"]
            and len({x["path"] for x in m["files"]})==len(m["files"]))
        for item in m["files"]:check(a.repo_root/relpath(item["path"]),item["bytes"],item["sha256"])
        paths={k:a.repo_root/relpath(v) for k,v in m["input_paths"].items()}
        gate("every proof source and successful receipt is frozen and the old sources are never imported",
            set(EXPECTED)<=set(paths) and sha(paths["contract"])==CONTRACT
            and sha(paths["SP_contract"])==SP_CONTRACT and sha(paths["TN_contract"])==TN_CONTRACT
            and sha(paths["TC_contract"])==TC_CONTRACT
            and sha(paths["strict_parts_manifest"])==STRICT_PARTS
            and sha(paths["original_strict_source"])==STRICT_SOURCE
            and all(sha(paths["accepted_"+tag+"_source"])==EXPECTED["accepted_"+tag+"_execution"][1]
                and sha(paths["accepted_"+tag+"_manifest"])==EXPECTED["accepted_"+tag+"_execution"][2]
                for tag in ("SP","RR","TN","TC"))
            and m["old_scientific_source_files_are_identity_evidence_not_imported"] is True
            and m["old_successful_scientific_calls_allowed"]==0
            and m["old_forcing_norm_body_natives_restored"]==0)
        S=accepted(paths["accepted_SP_execution"],EXPECTED["accepted_SP_execution"],gate)
        R=accepted(paths["accepted_RR_execution"],EXPECTED["accepted_RR_execution"],gate)
        T=accepted(paths["accepted_TN_execution"],EXPECTED["accepted_TN_execution"],gate)
        C=accepted(paths["accepted_TC_execution"],EXPECTED["accepted_TC_execution"],gate)
        flow,end,physical=same_objects(S,R,T,C,paths["accepted_SP_source"].read_text(),gate,d);checkpoint()
        rows=restore_strict(paths,gate,d);checkpoint()
        segments,cover=first_tail_cover(rows,flow,end,gate,d);checkpoint()
        old,k=final_saved_inputs(R,T,gate,d);checkpoint()
        last=final_cell(old,k,gate,d);checkpoint()
        fullplus,fullminus,maximum,audits=propagate(segments,flow,last,gate,d,checkpoint)
        gain,endpoint=endpoint_readouts(end,old,k,T,C,fullplus,fullminus,maximum,gate,d);checkpoint()
        complete_physical_columns(physical,gain,gate,d);checkpoint()
        d["scope"]=dict(exact_same_real_family_and_three_distinct_cuts=True,
            original_full_0_ra_scalar_cost_retained_without_subtracting_uppers=True,
            old_nonradial_prefix_and_boundary_row_closure_not_recomputed=True,
            original_five_strict_containers_read_only=True,
            final_tail_only_uses_saved_TN_norm_and_RR_signed_body_inputs=True,
            original_root_cut_q_gap_not_recomputed=True,
            all_tail_lengths_and_original_one_sided_germs_retained=True,
            both_complete_means_and_all_Fourier_modes_retained=True,
            every_shorter_source_insertion_has_the_complete_ordered_upper=True,
            volume_L2_to_L1_uses_true_length_and_jump_has_no_length_fee=True,
            raw_Hminus1_never_relabelled_raw_L2=True,
            RR_physical_columns_use_one_raw_state_factor_only=True,
            true_phase_coordinate_state_maps_keep_both_ordered_normalizers=True,
            original_N_1over200_conclusion_not_transferred_to_P22=True,
            prescribed_waist_data_not_a_solved_boundary_problem=True,
            whole_CE_incoming_inverse_finite_Schur_and_return_R0_not_claimed=True)
        zeros=("old_numerical_enclosures_recomputed","old_target_intrinsic_mean_or_repair_recomputed",
            "old_SP_prefix_or_boundary_scalar_closures_recomputed","old_SP_grouped_integral_or_exponential_recomputed",
            "old_RR_TN_TC_or_source_columns_recomputed","old_scientific_producer_calls","old_forcing_norm_body_natives_restored")
        gate("only the two new tails endpoint source readouts and four complete same-case contributions are new arithmetic",
            all(d[x]==0 for x in zeros) and d["original_successful_small_receipts_read"]==4
            and d["original_complete_strict_rows_verified"]==3071 and d["original_strict_container_parts_read"]==5
            and d["saved_boundary_row_closures_used"]==1 and d["new_first_tail_scalar_rows"]==len(segments)-1
            and d["new_final_tail_scalar_rows"]==d["new_ra_curvature_endpoint_bounds"]==d["new_reverse_curvature_log_fees"]==1
            and d["new_positive_two_state_exponentials"]==2*(len(segments)+1)
            and d["new_tail_products"]==d["new_complete_interval_products"]==2
            and d["new_complete_waist_physical_columns"]==4 and d["new_complete_same_case_waist_sums"]==1)
        if len(d["gates"])!=PARAMETERS["expected_actual_gate_count"]:raise ValueError("strict-tail gate count differs")
        d["complete"]=d["proved"]=d["complete_strict_tail_to_waist_paid"]=True;d["actual_returncode"]=0
    except Exception as e:
        d["failure"]=dict(type=type(e).__name__,message=str(e));print("ACTUAL_STRICT_TAIL_FAILURE",repr(e),flush=True)
    finally:
        d["actual_mathematical_wall_seconds"]=time.monotonic()-start;checkpoint()
        save(a.out,dict(scientific_receipt=d,new_tail_cover=cover,complete_new_tail_row_audit=audits),compressed=True)
        d["temporary_native_sha256"]=sha(a.out);d["temporary_native_bytes"]=a.out.stat().st_size;checkpoint()
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        t=a.conclusion.with_name(a.conclusion.name+".partial");t.write_text(render_conclusion(d),encoding="utf-8");t.replace(a.conclusion)
    raise SystemExit(d["actual_returncode"])

if __name__=="__main__":main()
