#!/usr/bin/env python3
"""New exact radial cancellation of two complete negative local source vectors.

The original free Nraw/free correction tables, signed Taylor totals, complete
scalar products, column coefficients and latest31-term source ledger are read.
Only new negative-cover scalar bounds and two whole-term comparisons are
evaluated. No accepted mathematical producer is called.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_exact_radial_cancellation_negative_local_sources_v1"
CONTRACT="8e91d7a28a4d2cdda467abba0703d615d9b5cd194a8808a65df2c5fc29a43b71"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
H=Q(893368603925465506687,21990232555520000000000000)
RG=Q(3,8000);SG=Q(3,128);SP=Q(1,256);CW=Q(1,32)
R0=Q(1,6000);RA=Q(3,40000);SIGMA0=Q(1,128)
RF=Q(3,20000);SF=Q(1,64);RS=Q(1,8000);SS=Q(3,512)
RC=Q(27,32000);SC=Q(1,64);N=388
BRANCHES=("central","positive_characteristic","negative_characteristic")
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
WHOLE_SOURCE="66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81"
WHOLE_MANIFEST="d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac"
WHOLE_NATIVE="6668c9b2c8f1632e3bd8af392a803335f076c64e1d7fb74dfc9e1605f0e1ee2d"
WHOLE_PROCESS="242d82b6f1ead216bf8e90679a9952a2aaad0e9d7ba29293739911e70ab4d145"
WHOLE_PUBLICATION="fc3a190d8b701ef84188f2a37ee846c4f3669b5ac409faa5a6b72850162d1099"
WHOLE_TAYLOR="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
WHOLE_NRAW="fbe1bce690f33335d2b024fe38a751743e0017e7d275b4d1fb0712be155f177e"
RECEIPTS={
 "scalar_execution":("43698106023","564759dceb4b38dd37fdd275d0fa3e22cdf2efa271cd9ef1049c6cfa4ff121f6","a6fbb28de8a85bd6f71054df0056a869285f131cc4c4702c66e5434deb7061cf","3896925b758840c4bbf2ce910141ca8a93d725d56bf22b5002e9c0b2486004af",26),
 "Taylor_execution":("43694458725","a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be","11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65","777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1",None),
 "refined_local_execution":("43711480764","e0541949f521e0852bb4a8b204b51281f7d83e0ed2a7a1afbb259ca73362e92a","5e2618c446288cd8d84fcbf4bb7955f56f7a1041f823e05213d043d20b5aeaaf","20422f41645c2a4544bb8a0d79eddf771b45ff0386cc81b3ee97a32849586ef2",19),
 "positive_execution":("43702688640","b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0","8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9","bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3",17),
 "directed_execution":("43703879926","1aa46093bba5150d636cc7c6ef4f5b080447fc2c75d7438b2e52ae5fa6b5d0af","5ce9aceb3be46e795696c09028f39091fdc9a4f969dba0e0b317408974083e9b","2c5cba2e7351267e090d0ca6c06cfecbb21309c039a7844937ee64026254f1d0",12),
 "columns_execution":("43688459733","9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c","1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99","fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57",16),
 "potential_execution":("43685624307","042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7","44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437","d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9",None),
 "baseline_execution":("43718112378","32c45b335639a48b0d32541d03924246023e5e3f19deec1bcd8cf0549e955f03","871240a7a97011d837025aad7f9ca1707d69c17b6dec3c1f510f6415c278b74d","58462f96a486dede07873c4fc6aade100539f9f28ef49b49567a4acf7c2e8706",29)
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):return abs(rb(v)).upper()
def bound(v,label="complete upper"):
    v=rb(v)
    if not v.is_finite() or v.lower()<0:raise ValueError("invalid "+label)
    return v.upper()
def lower(v,label="positive budget number"):
    v=rb(v).lower()
    if not v.is_finite() or v<0:raise ValueError("invalid nonnegative lower "+label)
    return v
def gap(v,label):
    v=lower(v,label)
    if not v>0:raise ValueError("missing positive gap "+label)
    return v
def rec(v):return dict(ball=rb(v).str(64))
def unpack(v):
    if isinstance(v,dict):
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:unpack(z) for k,z in v.items()}
    if isinstance(v,list):return [unpack(z) for z in v]
    return v
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def save(p,v,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    temp=p.with_name(p.name+".partial")
    temp.write_bytes(gzip.compress(raw,mtime=0) if compressed else raw);temp.replace(p)
def add(*args,k=2):
    return [up(sum((a[q] for a in args),arb(0))) for q in range(k+1)]
def scale(a,s,k=2):return [up(ex(s)*a[q]) for q in range(k+1)]
def mul(a,b,k=2):
    return [up(sum((math.comb(q,j)*a[j]*b[q-j] for j in range(q+1)),arb(0))) for q in range(k+1)]
def product(*args,k=2):
    out=[arb(1)]+[arb(0)]*k
    for a in args:out=mul(out,a,k)
    return out
def cauchy(m,width,k):
    if not Q(width)>0:raise ValueError("nonpositive complete angular width")
    return [up(bound(m)*math.factorial(q)/ex(Q(width)**q)) for q in range(k+1)]
def recurrence(initial,zeta,factor,k):
    values=[bound(initial)]
    for q in range(k):
        values.append(up(ex(factor)*sum((math.comb(q,j)*values[j]*zeta[q-j]
            for j in range(q+1)),arb(0))))
    return values
def compose2(values,y):
    if len(values)<3:raise ValueError("complete scalar T derivatives missing")
    return [bound(values[0]),up(values[1]*y[0]),up(values[2]*y[0]*y[0]+values[1]*y[1])]
def choose_complete(old,new):
    if bound(new)<bound(old):return rec(bound(new)),bool(bound(new)<rb(old).lower())
    return old,False

def parameters():
    return dict(arithmetic_bits=320,physical_piece=2549,cutoff_abs_j=97,physical_frequency="4j",
        exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],exact_root_interval=list(map(str,ROOTS)),
        exact_full_original_cover=str(H),new_negative_cover_radius_definition="r_plus_minus_piece_left",
        original_fold_radius=str(RG),original_fold_strip=str(SG),
        original_Taylor_radius=str(R0),original_added_Taylor_radius=str(RA),original_Taylor_strip=str(SIGMA0),
        accepted_forcing_radius=str(RF),accepted_forcing_strip=str(SF),
        accepted_amplitude_radius=str(RS),accepted_amplitude_strip=str(SS),
        original_leading_canonical_radius=str(RC),original_leading_canonical_strip=str(SC),
        actual_old_phi_strip=str(SP),complex_delta_square_halfwidth="1/100000000",
        complex_z_square_halfwidth="1/9409",fixed_intrinsic_parameter="eta_0",
        first_omitted_Taylor_degree=13,full_mean_and_both_input_signs=True,
        complete_free_Nraw_is_not_divided_by_mu=True,
        new_local_input_weights=["1","1/388"],new_changed_terms=["local_raw_1","local_raw_2"],
        accepted_baseline_run="43718112378/1",original_whole_piece_run="43669106351/1",
        common_column_envelope="abs(rho)^(-1/4)",original_source_rows_and_radial_weights_recomputed=0)

def accepted(path,identity,gate):
    run,source,manifest,digest,ngates=identity
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 retains source manifest all gates and actual child zero",
        sha(path)==digest and str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==RUNTIME
        and r.get("gates") and all(g.get("passed") is True for g in r["gates"])
        and (ngates is None or len(r["gates"])==ngates))
    return r

def read_original_fold(paths,gate):
    ms=read(paths["old_fold_majorants_stage"]);p=read(paths["adjacent_process"]);u=read(paths["adjacent_publication"])
    entries=[e for e in u["files"] if e["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
    gate("the original4501-byte fold and coefficient payload are read without rerunning their producers",
        sha(paths["old_fold_majorants_stage"])==MAJORANTS and sha(paths["adjacent_process"])==APROC
        and sha(paths["adjacent_publication"])==APUB and len(entries)==1
        and entries[0]["bytes"]==4501 and entries[0]["sha256"]==MAJORANTS
        and ms["complete"] and ms["stage"]==ms["name"]=="complete-original-reference-holomorphic-majorants"
        and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
        and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==RUNTIME
        and p["actual_returncode"]==0 and p["mathematical_complete"] and p["mathematical_proved"]
        and p["mathematical_failure"] is None and u["complete"]
        and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi")))
    return unpack(ms["payload"])

def read_original_free_budgets(paths,pins,h,gate):
    native=read(paths["whole_native"]);process=read(paths["whole_process"]);publication=read(paths["whole_publication"])
    gate("the original whole-piece mathematics succeeded before its separately preserved formatter failure",
        sha(paths["whole_native"])==WHOLE_NATIVE and sha(paths["whole_process"])==WHOLE_PROCESS
        and sha(paths["whole_publication"])==WHOLE_PUBLICATION
        and process["actual_returncode"]==0 and process["mathematical_complete"] and process["mathematical_proved"]
        and process["mathematical_failure"] is None and process["mathematical_source_sha256"]==WHOLE_SOURCE
        and process["manifest_sha256"]==WHOLE_MANIFEST and process["native_sha256"]==WHOLE_NATIVE
        and process["failure"]=={"type":"TypeError","message":"dict() got multiple values for keyword argument 'complete'"}
        and native["complete"] and native["proved"] and native["failure"] is None
        and native["source_sha256"]==WHOLE_SOURCE and native["input_manifest_sha256"]==WHOLE_MANIFEST
        and native["runtime"]==RUNTIME and native["gates"]==process["mathematical_gates"]
        and len(native["gates"])==10 and all(g["passed"] for g in native["gates"])
        and native["actual_local_numerator_is_unnormalized"] and publication["complete"])
    gate("the free numerator and free correction are on the same repaired piece parameter square and physical root",
        native["fixed_intrinsic_parameter"]=="eta_0"
        and Q(native["exact_complex_coefficient_delta_radius"])==Q(1,10**8)
        and native["exact_root_interval"]==list(map(str,ROOTS))
        and native["exact_original_physical_piece_interval"]==list(map(str,PIECE))
        and Q(native["exact_holomorphic_rho_radius"])==R0
        and Q(native["exact_holomorphic_phi_width"])==SIGMA0
        and native["original_Taylor_native_sha256"]==WHOLE_TAYLOR
        and native["original_Nraw_native_sha256"]==WHOLE_NRAW
        and native["original_targets_FFT_intrinsic_cubics_folds_signed_coefficients_and_saved_norms_recomputed"]==0)
    published={e["file"]:e for e in publication["files"]}
    base=paths["whole_native"].parent
    cache={};stage_audit=[]
    def oldstage(name,kind):
        if name in cache:return cache[name]
        e=native["stages"][name];path=base/e["file"];full=path.as_posix()
        pub=published.get("consumers/"+e["file"])
        if pub is None:raise ValueError("original natural stage has no published receipt")
        pin=next((v for v in pins.values() if path==v["absolute"]),None)
        if pin is None:raise ValueError("original stage was not in the immutable new input list")
        if not (path.stat().st_size==e["bytes"]==pub["bytes"]==pin["bytes"]
            and sha(path)==e["sha256"]==pub["sha256"]==pin["sha256"]):
            raise ValueError("an original complete stage byte changed")
        v=read(path)
        if not (v["stage"]==name and v["stage_kind"]==kind and v["complete"]
            and v["source_sha256"]==WHOLE_SOURCE and v["input_manifest_sha256"]==WHOLE_MANIFEST
            and v["runtime"]==RUNTIME and v["original_Taylor_native_sha256"]==WHOLE_TAYLOR
            and v["original_Nraw_native_sha256"]==WHOLE_NRAW):
            raise ValueError("original stage identity changed")
        cache[name]=v["payload"];stage_audit.append(dict(name=name,file=e["file"],bytes=e["bytes"],sha256=e["sha256"]))
        return v["payload"]
    names=sorted(k for k in native["stages"] if k.startswith("complete-physical-root-row-"))
    if names!=["complete-physical-root-row-"+str(i).zfill(4) for i in range(9)]:
        raise ValueError("the original9 complete physical rows changed")
    rows=[oldstage(name,"complete_source_rows") for name in names]
    negative=sorted((v for v in rows if v["side"]=="negative"),key=lambda v:Q(v["interval"][0]))
    edge=PIECE[0];budgets=[];row_audit=[]
    for row in negative:
        a,b=map(Q,row["interval"])
        if a!=edge or not a<b:raise ValueError("the original negative cover has a gap or overlap")
        edge=b;r=Q(row["exact_rho_cover"])
        if not 0<r<=h:raise ValueError("an original negative radius leaves the new cover")
        name="complete-radius-budget-"+str(r.numerator)+"-"+str(r.denominator)
        budget=oldstage(name,"radius_budget_stages")
        if not (Q(budget["exact_physical_rho_cover"])==r and budget["complete"]
            and Q(budget["exact_holomorphic_rho_radius"])==R0
            and Q(budget["exact_holomorphic_phi_width"])==SIGMA0
            and payload_sha(budget)==row["complete_radius_budget_payload_sha256"]
            and row["actual_local_source_is_JP_S_of_unnormalized_Nraw"]
            and row["original_piece"]==2549):
            raise ValueError("the original complete numerator budget is not linked to its true row")
        real=[v for v in budget["budgets"] if Q(v["exact_output_phi_width"])==0]
        if len(real)!=1:raise ValueError("the complete real-angle numerator budget is not unique")
        v=real[0]
        if not (v["all_saved_finite_norms_and_complete_angular_factors_reused"]
            and v["old_first_correction_or_numerator_coefficients_recomputed"] is False):
            raise ValueError("the original completed finite and infinite budget is incomplete")
        budgets.append(v)
        row_audit.append(dict(common_row=row["common_row"],interval=row["interval"],
            uncertain_root_one_sided_charge=row["uncertain_root_one_sided_charge"],
            original_radius_budget_payload_sha256=row["complete_radius_budget_payload_sha256"],
            original_row_payload_sha256=payload_sha(row)))
    gate("exactly six old complete negative rows retain the true cover and its one-sided uncertain-root charge",
        len(negative)==6 and edge==ROOTS[1] and any(v["uncertain_root_one_sided_charge"] for v in negative)
        and 0<h<H<R0 and len(budgets)==6)
    raw=[];free=[]
    for field,key in (("a","a1"),("b","b1")):
        raw.append([max(bound(v["complete_Nraw_derivative_budgets"]["strip_sup"][field][str(q)],
            "complete old correlated numerator") for v in budgets).upper() for q in range(3)])
        free.append([max(bound(v["first_amplitude_budgets"][key]["strip_sup"]["0,"+str(q)],
            "complete old free correction") for v in budgets).upper() for q in range(3)])
    conclusion=dict(original_run="43669106351/1",original_native_sha256=WHOLE_NATIVE,
        original_process_sha256=WHOLE_PROCESS,original_publication_sha256=WHOLE_PUBLICATION,
        original_scientific_source_sha256=WHOLE_SOURCE,original_scientific_manifest_sha256=WHOLE_MANIFEST,
        original_mathematical_returncode=0,original_mathematical_gate_count=10,
        original_formatter_failure_preserved=process["failure"],
        original_full_source_rows_read=9,original_negative_rows_consumed=6,
        original_radius_budget_stages_read=len(cache)-9,
        original_natural_stage_receipts_sha256=payload_sha(stage_audit),
        original_six_row_identity_sha256=payload_sha(row_audit),exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],
        actual_negative_rho_cover=str(h),full_free_Nraw_and_w1_not_regenerated=True,
        original_raw_numerator_not_divided_by_mu=True,
        old_matrix_words_profile_or_radial_weights_recomputed=False)
    return raw,free,conclusion,dict(stage_receipts=stage_audit,row_receipts=row_audit,
        complete_original_free_Nraw=encode(raw),complete_original_free_w1=encode(free))

def radial_tail_number(M,R,h,p):
    if p not in (0,1) or not 0<h<R:raise ValueError("the new complete tail leaves its exact product")
    t=ex(h/R);d=1-t;gap(d,"complete radial tail")
    kernel=t**13/d if p==0 else t**12*(13/d+t/(d*d))
    return rb(M)*ex(R**(-p))*kernel

def fourier_tail_number(width,q):
    if not Q(width)>0 or q not in (0,1,2,3):raise ValueError("complete angular tail order")
    v=(-4*ex(width)).exp();d=1-v;gap(d,"complete angular tail")
    if q==0:return (1+v)/d
    if q==1:return 8*v/d**2
    if q==2:return 32*v*(1+v)/d**3
    return 128*v*(1+4*v+v*v)/d**4

def read_Taylor_rows(W,gate):
    cases=[v for v in W["cases"] if Q(v["exact_output_old_phi_width"])==0]
    if len(cases)!=1:raise ValueError("the real whole-Taylor case is not unique")
    case=cases[0];fields={v["field"]:v for v in case["fields"]}
    gate("the accepted signed Taylor totals retain their finite-before-modulus full two-tail identities",
        case["complete"] and case["proved"] and Q(case["exact_whole_piece_cover_radius"])==H
        and all(fields[k]["finite_signed_addition_precedes_modulus_and_sum"]
            and fields[k]["joint_sum_of_radial_coefficient_suprema"] and fields[k]["full_output_zero_mode_retained"]
            and fields[k]["amplitude_mean_is_not_independent_physical_even_mean"]
            and Q(fields[k]["old_tail_radius"])==R0 and Q(fields[k]["added_term_tail_radius"])==RA
            and Q(fields[k]["common_outer_angle_strip"])==SIGMA0 for k in ("fa","fb","b1")))
    out={}
    for name in ("fa","fb","b1"):
        out[name]={}
        for row in fields[name]["complete_mixed_derivative_rows"]:
            if row["radial_derivative_order"] not in (0,1):continue
            if row["angular_derivative_orders"]!=[0,1,2,3]:raise ValueError("old physical angular derivative order changed")
            out[name][row["radial_derivative_order"]]=row["complete_joint_Wiener_upper"]
    return out

def negative_Taylor_budget(W,S,B,h,gate):
    old=read_Taylor_rows(W,gate);tails=W["complete_tail_conclusion"]
    sf=S["complete_forcing_conclusion"];bd=B["complete_domain_conclusion"]
    gate("the already completed forcing and amplitude products cover the smaller negative evaluation radius",
        0<h<H<RS<RF<RG and Q(sf["exact_new_old_rho_radius"])==RF
        and Q(sf["exact_new_old_angle_strip"])==SF and Q(bd["exact_new_old_rho_radius"])==RS
        and Q(bd["exact_new_old_phi_strip"])==SS and Q(bd["exact_full_physical_cover"])==H
        and bd["all_sT_paths_in_same_paid_domain"] and bd["root_normalization_and_all_means_unchanged"]
        and sf["old_potential_bounds_consumed_without_recomputation"] and sf["actual_common_T_segment_consumed"]
        and tails["first_omitted_Taylor_degree"]==13 and Q(tails["old_radius"])==R0
        and Q(tails["new_added_term_radius"])==RA and Q(tails["outer_old_phi_strip"])==SIGMA0
        and tails["angular_tails_from_joint_double_Cauchy"]
        and tails["no_uncomputed_finite_coefficient_was_set_to_zero"])
    requests=[("fa",0,q) for q in range(3)]+[("fb",0,q) for q in range(3)]
    requests += [("b1",0,q) for q in range(4)]+[("b1",1,q) for q in range(3)]
    moduli={"fa":(sf["fa"],RF,SF),"fb":(sf["fb"],RF,SF),
        "b1":(bd["complete_new_amplitude_modulus"]["b1"],RS,SS)}
    result={name:{p:[] for p in ((0,1) if name=="b1" else (0,))} for name in ("fa","fb","b1")}
    details=[]
    for name,p,q in requests:
        mo=lower(tails["unchanged_original_full_product_modulus"][name],"old complete positive modulus")
        ma=lower(tails["complete_added_term_full_product_modulus"][name],"old added positive modulus")
        same=(radial_tail_number(mo,R0,H,p)+radial_tail_number(ma,RA,H,p))*fourier_tail_number(SIGMA0,q)
        lo=lower(same,"same old numerical tail addend")
        total=bound(old[name][p][q],"saved complete Taylor derivative")
        finite=(total-lo).upper()
        if not finite.is_finite() or finite.lower()<0:
            raise ValueError("same positive-tail recovery inconsistent; no clipping")
        M,R,width=moduli[name]
        tail=up(radial_tail_number(bound(M),R,h,p)*fourier_tail_number(width,q))
        candidate=up(finite+tail);chosen=min(candidate,total).upper()
        result[name][p].append(chosen)
        details.append(dict(field=name,p=p,q=q,old_total=old[name][p][q],
            same_old_positive_tail_lower=rec(lo),complete_old_finite_sum_upper=rec(finite),
            new_complete_negative_tail_upper=rec(tail),new_complete_derivative_upper=rec(chosen)))
    gate("all thirteen new derivatives keep every old finite coefficient and the entire n13 Fourier and radial tail",
        len(details)==13 and all(v.is_finite() and v.lower()>=0
            for field in result.values() for values in field.values() for v in values))
    conclusion=dict(exact_new_negative_rho_cover=str(h),old_complete_whole_piece_radius=str(H),
        complete_derivatives_compared=13,full_zero_mode_retained=True,
        complete_original_finite_budget_not_rescaled=True,
        subtracted_lower_is_same_algorithm_tail_not_function_lower=True,
        original_coefficients_Fourier_norms_transport_and_products_recomputed=False,
        retained_complete_forcing_derivative_upper=encode({"fa":result["fa"][0],"fb":result["fb"][0]}),
        retained_complete_b1_value_derivative_upper=encode(result["b1"][0]),
        retained_complete_b1_radial_derivative_upper=encode(result["b1"][1]))
    return result,conclusion,details

def negative_geometry(f,c,AJ,W,P,Hv,h,gate):
    accepted=AJ["complete_domain_conclusion"];aj=AJ["complete_AJ_angular_derivative_conclusion"]
    gate("the completed AJ whole-domain connection derivatives and physical image are read without rerunning AJ",
        Q(accepted["exact_full_physical_cover"])==H and Q(accepted["exact_original_fold_radius"])==RG
        and Q(accepted["exact_original_fold_strip"])==SG and Q(accepted["exact_physical_phi_strip"])==SP
        and accepted["all_sT_segments_in_accepted_product"]
        and accepted["physical_T_image_definition_read_from_frozen_producer"]
        and aj["accepted_order_zero_domain_read_verbatim"]==accepted
        and aj["exact_mu_identity"]=="Q^2*(x^2+T*y^2)"
        and aj["old_fold_coefficient_or_original_pipeline_recomputed"] is False)
    tau=ex(h/RG);Am=gap(f["Am"],"original complete A modulus")
    xsmall=up(tau*bound(f["j"]));yy=up(tau*tau*bound(f["BT"]))
    zz=up(ex(Q(2,3))*tau*bound(f["BA"])/Am)
    X=cauchy(xsmall,SG,3);X[0]=up(1+xsmall)
    Y=cauchy(yy,SG,3);Z=cauchy(zz,SG,2)
    Th=up(ex(h/H)*bound(accepted["accepted_complete_physical_T_image"]))
    T=[Th]+Y[:3]
    QQ=recurrence(f["Q"],Z,Q(1,2),2);GG=recurrence(f["G"],Z,Q(1,4),2)
    Bplus=add(mul(X,X),product(T,Y,Y))
    aa=product(GG,Bplus);bb=scale(product(GG,X,Y),2)
    mu=product(QQ,QQ,Bplus)
    Xi=[bound(v) for v in aj["complete_Xi_angular_derivative_upper"][:3]]
    ct=[bound(v) for v in aj["complete_cT_angular_derivative_upper"][:3]]
    M=bound(f["M"]);B2=bound(f["B2"])
    if M<1:raise ValueError("the rooted leading value1 is not in its complete modulus")
    XH=bound(accepted["accepted_complete_physical_X_image"])
    marginT=gap(ex(RC)-Th,"original leading canonical T margin")
    marginX=gap(ex(SC)-XH,"original leading canonical X margin")
    ax=up(2*(M-1)*Th/(marginT*marginX));bx=up(B2*Th*Th/marginX)
    wX=[cauchy(ax,SP,2),cauchy(bx,SP,2)]
    cases=[v for v in P["cases"] if Q(v["exact_complex_radial_radius"])==R0]
    if len(cases)!=1:raise ValueError("original common potential case is not unique")
    pc=cases[0];image=gap(pc["reference_image"]["complete_image_disk_radius_lower"],"same complete common T image")
    dt=gap(image-Th,"same potential positive image margin")
    gate("the negative physical T image remains in the same common potential and leading inverse products",
        pc["complete"] and pc["proved"] and pc["failure"] is None
        and pc["both_carrier_signs_retained"] and pc["whole_complex_bilinear_family"]
        and Q(pc["exact_complex_z_square_halfwidth"])==Q(1,9409)
        and Q(pc["exact_complex_delta_square_halfwidth"])==Q(1,10**8)
        and pc["fixed_intrinsic_parameter"]=="eta_0" and image>Th and marginT>0 and marginX>0
        and 0<h<H<RS and Q(W["complete_domain_conclusion"]["exact_whole_physical_piece_cover_radius"])==H
        and W["complete_domain_conclusion"]["same_reference_T_not_old_r_substituted"])
    vp=[bound(pc["complete_modulus_upper"][k]) for k in ("V","V_T","V_TT")]
    ell=[bound(v) for v in W["complete_domain_conclusion"]["complete_Fuchsian_integral_T_derivative_modulus_upper"]]
    if len(ell)!=3:raise ValueError("accepted complete Fuchsian derivative list changed")
    ell.extend([up(vp[2]/(7*dt)),up(2*vp[2]/(9*dt*dt))])
    V=compose2(vp,Y);VT=compose2([vp[1],vp[2],up(vp[2]/dt)],Y)
    B0=compose2(ell[:3],Y);B1=compose2(ell[1:4],Y);B22=compose2(ell[2:5],Y)
    inv=Hv["old_circle_inverse"]
    determinant=gap(inv["complete_deformed_determinant_modulus_lower"],"complete genuine deformed determinant")
    gate("the genuine determinant and physical drift retain their same full original product and complex input square",
        inv["full_physical_root_piece_covered"] and inv["full_mean_output_retained"]
        and Q(inv["exact_full_physical_root_cover"])==H
        and Q(inv["exact_old_rho_radius"])>H and len(c["D"])>=3
        and determinant>0 and len(Xi)==len(ct)==3)
    deltajet=add(mul(X,X),product(add(T,scale(V,Q(2,N*N))),Y,Y))
    invdelta=[up(1/determinant)]
    for q in (1,2):
        invdelta.append(up(sum((math.comb(q,j)*deltajet[j]*invdelta[q-j]
            for j in range(1,q+1)),arb(0))/determinant))
    theta=cauchy(c["vartheta"],CW,2)
    pref=product(theta,QQ,V,GG,Bplus,invdelta)
    rank=[product(pref,X,Y),product(pref,Y,Y)]
    out=dict(x=X,y=Y,T=T,Q=QQ,G=GG,a0=aa,b0=bb,mu=mu,
        Xi=Xi,cT=ct,w0X=wX,V=V,VT=VT,B=B0,BT=B1,BTT=B22,
        D=[bound(v) for v in c["D"][:3]],rank=rank)
    conclusion=dict(exact_negative_rho_cover=str(h),exact_original_whole_cover=str(H),
        new_complete_negative_T_image_upper=rec(Th),
        original_complete_potential_T_image_lower=rec(image),new_complete_potential_T_margin_lower=rec(dt),
        complete_leading_T_margin_lower=rec(marginT),complete_leading_X_margin_lower=rec(marginX),
        accepted_AJ_connection_angular_jets_read_without_recomputation=True,
        accepted_complete_deformed_determinant_lower=rec(determinant),
        complete_additional_Fuchsian_derivatives_3_4=encode(ell[3:]),
        complete_leading_X_derivative_moduli=encode([ax,bx]),
        original_full_mean_gauge_retained=True,original_potential_and_fold_producers_called=False,
        exact_L1_has_no_cT_or_leading_T_derivative=True)
    return out,conclusion

def correlated_local_vectors(oldN,oldw,jets,g):
    """R11--12 and R25--26, with complete ordered products before majorants."""
    T=g["T"];aa=g["a0"];bb=g["b0"];V=g["V"];mu=g["mu"]
    fa=jets["fa"][0];fb=jets["fb"][0]
    KMf=[mul(T,add(mul(bb,fb),mul(aa,fa))),add(mul(aa,fb),product(T,bb,fa))]
    kw=[mul(T,bb),aa]
    tangent=[add(scale(g["w0X"][i],2),mul(g["Xi"],[aa,bb][i])) for i in range(2)]
    Nterm=oldN
    Vterm=[product(mu,V,oldw[i]) for i in range(2)]
    Fterm=[product(mu,g["B"],KMf[i]) for i in range(2)]
    remainder=[mul(mu,add(mul(g["BTT"],kw[i]),product(T,g["BT"],tangent[i]))) for i in range(2)]
    L1=[add(Nterm[i],Vterm[i],Fterm[i],remainder[i]) for i in range(2)]
    b=jets["b1"][0];br=jets["b1"][1];bphi=b[1:4]
    drift=add(product(g["Q"],T,g["y"]),mul(g["x"],g["D"]))
    derivative=add(mul(g["x"],br),mul(drift,bphi))
    l2a=add(scale(product(g["Q"],V,derivative),2),
        product(mu,add(g["VT"],mul(g["cT"],V)),b),g["rank"][0])
    L2=[l2a,g["rank"][1]]
    return L1,L2,dict(first_original_correlated_numerator=Nterm,
        first_complete_V_free_correction=Vterm,first_complete_normalized_forcing=Fterm,
        first_complete_connection_free_remainder=remainder,
        second_complete_rank=g["rank"],new_complete_L1=L1,new_complete_L2=L2)

def read_positive_coefficients(C,gate):
    rows=C["complete_positive_linear_operator_conclusion"]
    gate("the same eighteen complete genuine-column coefficients include all three branches two signs and output means",
        len(rows)==3 and [r["branch"] for r in rows]==list(BRANCHES)
        and all(r["exact_input_component_order"]==["a","a_phi","a_phiphi","b","b_phi","b_phiphi"]
            and len(r["complete_positive_linear_coefficients"])==6
            and len(r["selected_inputs"])==6
            and all(v["denominator_is_lower_for_bound_number_only"] for v in r["selected_inputs"]) for r in rows)
        and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
        and C["scope"]["all_input_abs_j_at_least97"])
    return [[bound(v) for v in r["complete_positive_linear_coefficients"]] for r in rows]

def positive_operator(coeff,vector):
    values=vector[0][:3]+vector[1][:3]
    return up(sum((sum((c*v for c,v in zip(row,values)),arb(0)) for row in coeff),arb(0)))

def compare_and_combine(C,D,B,AJ,values,gate):
    local=C["complete_local_vector_conclusion"]
    if D["accepted_complete_local_vector_conclusion"]!=local:raise ValueError("old local raw coefficient identity changed")
    original=D["complete_source_conclusion"];base=AJ["complete_source_conclusion"]
    terms0=original["complete_first_source_term_L2_upper"];terms=dict(base["complete_first_source_term_L2_upper"])
    bterms=B["complete_source_conclusion"]["complete_first_source_term_L2_upper"]
    gate("the latest29-gate AJ ledger retains B local1 and the same original local2 local3 six-row measure",
        len(terms)==21 and len(base["complete_independent_mean_term_L2_upper"])==10
        and terms["local_raw_1"]==bterms["local_raw_1"]
        and terms["local_raw_2"]==terms0["local_raw_2"] and terms["local_raw_3"]==terms0["local_raw_3"]
        and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
        and all(base[k]==original[k] for k in ("actual_dr_measure","exact_negative_physical_cover",
            "one_sided_uncertain_root_band_retained","both_density_windows_retained","outer_J_window",
            "input_window","first_output_window","independent_even_mean_window",
            "total_squared_envelope_radial_weight_upper","original_temporary_row_payload_sha256"))
        and local["raw_numerator_not_divided_by_mu"]
        and local["exact_input_weights"]==["1","1/388","1/150544"])
    comparisons=[]
    for i,value in enumerate(values,1):
        key="local_raw_"+str(i);beta=gap(local["raw_complete_operator_coefficients"][i-1],"same original raw local numerical coefficient")
        ratio=min(arb(1),up(value/beta)).upper()
        candidate=up(ratio*bound(terms0[key]))
        retained,improved=choose_complete(terms[key],candidate);terms[key]=retained
        comparisons.append(dict(source_term=key,new_complete_raw_operator_upper=rec(value),
            same_original_positive_budget_lower=rec(beta),complete_uniform_comparison_factor=rec(ratio),
            complete_original_term_L2_upper=terms0[key],latest_complete_term_L2_upper=base["complete_first_source_term_L2_upper"][key],
            retained_complete_term_L2_upper=retained,strict_complete_term_improvement=improved,
            comparison_denominator_is_not_function_lower=True))
    result=dict(base);result["complete_first_source_term_L2_upper"]=terms
    local_sum=up(sum((bound(terms["local_raw_"+str(j)]) for j in (1,2,3)),arb(0)))
    result["local_L2_upper"],a=choose_complete(base["local_L2_upper"],local_sum)
    first=up(bound(result["local_L2_upper"])+bound(base["nonlocal_total_L2_upper"]))
    result["first_L2_upper"],b=choose_complete(base["first_L2_upper"],first)
    pair=up((bound(result["first_L2_upper"])**2+bound(base["mean_L2_upper"])**2).sqrt())
    result["combined_L2_upper"],c=choose_complete(base["combined_L2_upper"],pair)
    result["strictly_smaller_complete_aggregates"]=dict(local=a,first=b,combined=c)
    result["only_two_complete_local_vectors_replaced"]=True
    result["all_other_twenty_nine_term_balls_read_verbatim"]=True
    result["old_source_row_or_radial_integral_recomputed"]=False
    # Remove inherited scope flags that describe earlier local recipes.
    result.pop("complete_local_budget_read_unchanged",None)
    return result,comparisons

def render(doc):
    lines=["# Actual exact radial-cancellation local-source consumption","",
        "This result keeps the latest complete negative source ledger and replaces only whole proved local bounds.",
        "The new arithmetic consumes accepted complete free numerators, full means and original positive Taylor budgets.",
        "", "## Actual status","",
        "| Item | Actual result |","|---|---|",
        "| Run | "+str(doc.get("run_id"))+"/"+str(doc.get("run_attempt"))+" |",
        "| Scientific source SHA256 | "+doc["source_sha256"]+" |",
        "| Input manifest SHA256 | "+doc["input_manifest_sha256"]+" |",
        "| Actual scientific return code | "+str(doc["actual_returncode"])+" |",
        "| Passed gates | "+str(sum(bool(g["passed"]) for g in doc["gates"]))+"/"+str(len(doc["gates"]))+" |",
        "| New scalar mathematical seconds | "+str(doc.get("actual_mathematical_wall_seconds"))+" |",
        "| Original numerical enclosures recomputed | 0 |","",
        "## Scientific gates",""]
    for g in doc["gates"]:lines.append("- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"]+".")
    if doc.get("failure"):lines+=["","Failure: "+json.dumps(doc["failure"],ensure_ascii=False)]
    if "complete_domain_conclusion" in doc:
        d=doc["complete_domain_conclusion"]
        lines+=["","## New negative evaluation domain","",
            "The complete negative radius is "+d["exact_negative_rho_cover"]+
            "; the old full-piece radius remains "+d["exact_original_whole_cover"]+".",
            "Every original root-band, physical seam, parameter square and common reference gauge is retained.",
            "", "| Complete scalar conclusion | Directed ball |","|---|---|"]
        for k in ("new_complete_negative_T_image_upper","original_complete_potential_T_image_lower",
            "new_complete_potential_T_margin_lower","complete_leading_T_margin_lower",
            "complete_leading_X_margin_lower","accepted_complete_deformed_determinant_lower"):
            lines.append("| "+k+" | "+d[k]["ball"]+" |")
    if "complete_local_operator_conclusion" in doc:
        d=doc["complete_local_operator_conclusion"]
        lines+=["","## Complete local operator coefficients","",
            "These coefficients multiply the same pointwise abs(rho)^(-1/4) genuine-column envelope.",
            "They include both genuine columns, both input signs and all output means.",
            "", "| Vector | New raw whole-operator upper | Exact external input weight |",
            "|---|---|---|"]
        for i,v in enumerate(d["new_complete_raw_local_operator_upper"],1):
            lines.append("| local_raw_"+str(i)+" | "+v["ball"]+" | "+(["1","1/388"][i-1])+" |")
        lines+=["","The first vector was formed as Nold - mu V w1 - mu B KM fV plus the exact connection-free remainder.",
            "Its free numerator and free correction were read from the successful whole-piece stages.",
            "Its complete summand diagnostics are upper bounds, not measured residuals or lower bounds.","",
            "| Complete first-vector summand | Operator upper |","|---|---|"]
        for k,v in d["first_vector_complete_summand_operator_upper"].items():
            lines.append("| "+k+" | "+v["ball"]+" |")
    if "complete_comparison_conclusions" in doc:
        lines+=["","## Same-term comparisons","",
            "| Whole source term | Uniform ratio to original positive budget | Latest complete L2 upper | Retained complete L2 upper | Strict improvement |",
            "|---|---|---|---|---|"]
        for c in doc["complete_comparison_conclusions"]:
            lines.append("| "+c["source_term"]+" | "+c["complete_uniform_comparison_factor"]["ball"]+" | "+
                c["latest_complete_term_L2_upper"]["ball"]+" | "+c["retained_complete_term_L2_upper"]["ball"]+" | "+
                str(c["strict_complete_term_improvement"])+" |")
        lines+=["","Each denominator bounds an old numerical budget parameter from below; it is not a lower bound for an amplitude.",
            "The original six outer-J rows, physical dr, uncertain-root one-sided charge and all input weights are unchanged."]
    if "complete_source_conclusion" in doc:
        d=doc["complete_source_conclusion"]
        lines+=["","## Complete retained source","",
            "| Complete source | Directed L2 upper |","|---|---|"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+k+" | "+d[k]["ball"]+" |")
        lines+=["","### All21 first-row terms","","| Term | Complete L2 upper |","|---|---|"]
        for k,v in d["complete_first_source_term_L2_upper"].items():lines.append("| "+k+" | "+v["ball"]+" |")
        lines+=["","### All10 independent even-mean terms","","| Term | Complete L2 upper |","|---|---|"]
        for k,v in d["complete_independent_mean_term_L2_upper"].items():lines.append("| "+k+" | "+v["ball"]+" |")
    lines+=["","## Reproduction and scope","",
        "Producer: scripts/fourfold_codazzi_correlated_radial_local_sources.py.",
        "Arguments: --repo REPO --manifest MANIFEST --manifest-sha SHA256 --out-dir TEMP_OUT.",
        "Only the new scalar negative-cover bounds, complete product combinations and whole-term comparisons are evaluated.",
        "No accepted target, Fourier transform, intrinsic solve, repair, fold, signed Taylor coefficient, numerator norm, transport, potential, profile, inverse, matrix word or source radial integral is regenerated.",
        "The complete restored inputs and new intermediate arrays remain temporary; only this small conclusion and execution identity are published.",
        "The independent physical mean, all old-circle terms and actual seams are retained. Root and affine-jump sources, positive two-end selection, physical-to-wave conversion and the complete coupled strong return remain separate obligations.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematical arithmetic is restricted to this public Actions repository")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the immutable numerical runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    source=sha(__file__);h=ROOTS[1]-PIECE[0]
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_complete_fold_stages_read=0,original_complete_whole_native_read=0,
        original_complete_source_rows_read=0,original_complete_negative_source_rows_consumed=0,
        original_complete_radius_budget_stages_read=0,original_successful_small_receipts_read=0,
        original_positive_linear_coefficients_read=0,original_complete_source_terms_read=0,
        new_same_positive_tail_lower_recoveries=0,new_complete_negative_Taylor_derivative_bounds=0,
        new_complete_negative_coefficient_closures=0,new_complete_raw_local_vectors=0,
        new_complete_local_operator_bounds=0,new_complete_first_vector_summand_diagnostics=0,
        new_complete_uniform_term_comparisons=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,old_free_Nraw_or_free_correction_recomputed=0,
        old_target_FFT_intrinsic_repair_fold_or_Taylor_recomputed=0,
        old_scalar_potential_forcing_transport_or_product_recomputed=0,
        old_genuine_profile_inverse_AJ_closure_or_calibration_recomputed=0,
        old_source_row_or_radial_integral_recomputed=0,new_radial_integrals_computed=0,
        original_natural_stage_bytes_modified=0,full_physical_negative_volume_source_paid=False,
        full_high_inverse_claimed=False,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    temporary={}
    def gate(name,ok):
        doc["gates"].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    try:
        m=read(a.manifest);doc["mathematical_parameters"]=parameters()
        gate("the exact new-only radial-cancellation manifest and smaller physical evaluation domain are fixed",
            sha(a.manifest)==a.manifest_sha and m["public_repository"]==PUBLIC
            and m["scientific_source_sha256"]==source and m["mathematical_parameters"]==parameters()
            and 0<h<H<RS<RF<RG)
        pins={}
        for e in m["files"]:
            rel=Path(e["path"]);path=a.repo/rel
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):
                raise ValueError("an immutable input leaves this topic")
            if e["path"] in pins:raise ValueError("duplicate immutable path")
            if not path.is_file() or path.stat().st_size!=e["bytes"] or sha(path)!=e["sha256"]:
                raise ValueError("immutable input changed: "+e["path"])
            pins[e["path"]]=dict(e,absolute=path)
        if any(v not in pins for v in m["input_paths"].values()):raise ValueError("an input role lacks its exact pin")
        paths={k:a.repo/v for k,v in m["input_paths"].items()}
        gate("the exact contract and accepted original sources bind the mathematical identities",
            sha(paths["contract"])==CONTRACT and sha(paths["original_whole_algorithm"])==WHOLE_SOURCE
            and sha(paths["original_whole_manifest"])==WHOLE_MANIFEST
            and sha(paths["original_Taylor_algorithm"])==RECEIPTS["Taylor_execution"][1]
            and sha(paths["original_scalar_algorithm"])==RECEIPTS["scalar_execution"][1]
            and sha(paths["original_positive_algorithm"])==RECEIPTS["positive_execution"][1]
            and sha(paths["original_fold_algorithm"])=="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783"
            and sha(paths["original_first_local_algorithm"])=="c479aaec9438a80340e425223b2eac0ed9b5707583c6a8125553e59ccd189048")
        receipts={k:accepted(paths[k],identity,gate) for k,identity in RECEIPTS.items()}
        doc["original_successful_small_receipts_read"]=len(receipts)
        S=receipts["scalar_execution"];W=receipts["Taylor_execution"];B=receipts["refined_local_execution"]
        C=receipts["positive_execution"];D=receipts["directed_execution"];AJ=receipts["baseline_execution"]
        P=receipts["potential_execution"];Hv=receipts["columns_execution"]
        old=read_original_fold(paths,gate);f=old["fold"];c=old["coefficients"]
        doc["original_complete_fold_stages_read"]=1
        gate("all retained source and correction products keep both signs the full parameter squares and independent physical mean",
            S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and S["complete_amplitude_conclusion"]["exact_regular_root_normalization_retained"]
            and S["complete_amplitude_conclusion"]["full_raw_forcing_used"]
            and C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["output_mean_and_complete_original_primitive_retained"]
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and AJ["full_physical_negative_volume_source_paid"] and not AJ["full_high_inverse_claimed"]
            and AJ["old_numerical_enclosures_recomputed"]==0)
        ws=paths["original_Taylor_algorithm"].read_text()
        fs=paths["original_fold_algorithm"].read_text()
        ps=paths["original_first_local_algorithm"].read_text()
        ss=paths["original_scalar_algorithm"].read_text()
        gate("the old Taylor positive addends and whole-fold leading inverse products have their frozen exact definitions",
            "fulltail=oldtail+newtail" in ws and "tail=fulltail*angular_sum(SIGMA-width,q)" in ws
            and "vals.append(rec(up(finite+tail)))" in ws
            and "exact_canonical_radius=str(LAM*R/2),exact_canonical_width=str(SF)" in fs
            and "LAM=Q(9,2)" in fs and "SG=Q(3,128);SF=Q(1,64)" in fs
            and 'imageT=up(ex(H)*powr(Ap,Q(2,3)))' in ps
            and "fb=up(ai*raw_fb+ti*raw_fa);fa=up(bi*raw_fb+ai*raw_fa)" in ss)
        oldN,oldw,original,original_temp=read_original_free_budgets(paths,pins,h,gate)
        doc.update(original_complete_whole_native_read=1,original_complete_source_rows_read=9,
            original_complete_negative_source_rows_consumed=6,
            original_complete_radius_budget_stages_read=original["original_radius_budget_stages_read"],
            complete_original_free_budget_conclusion=original)
        jets,taylor,taylor_temp=negative_Taylor_budget(W,S,B,h,gate)
        doc.update(new_same_positive_tail_lower_recoveries=13,new_complete_negative_Taylor_derivative_bounds=13,
            complete_negative_Taylor_conclusion=taylor)
        geometry,domain=negative_geometry(f,c,AJ,W,P,Hv,h,gate)
        doc.update(new_complete_negative_coefficient_closures=1,complete_domain_conclusion=domain)
        l1,l2,local_temp=correlated_local_vectors(oldN,oldw,jets,geometry)
        coeff=read_positive_coefficients(C,gate)
        values=[positive_operator(coeff,l1),positive_operator(coeff,l2)]
        diagnostic={name:rec(positive_operator(coeff,local_temp[name])) for name in
            ("first_original_correlated_numerator","first_complete_V_free_correction",
             "first_complete_normalized_forcing","first_complete_connection_free_remainder")}
        gate("both complete new local raw vectors are finite and keep the original numerator mu and input weights",
            all(v.is_finite() and v.lower()>=0 for vec in (l1,l2) for component in vec for v in component)
            and all(v.is_finite() and v.lower()>=0 for v in values))
        doc.update(original_positive_linear_coefficients_read=18,
            new_complete_raw_local_vectors=2,new_complete_local_operator_bounds=2,
            new_complete_first_vector_summand_diagnostics=4)
        doc["complete_local_operator_conclusion"]=dict(
            new_complete_raw_local_operator_upper=encode(values),
            complete_new_raw_local_angular_derivative_upper=encode({"L1":l1,"L2":l2}),
            first_vector_complete_summand_operator_upper=diagnostic,
            first_identity="Nold-mu*V*w1-mu*B*K*M*fV+mu*(BTT*K*Jplus*w0+i*epsilon*T*BT*Jplus*(2*w0X+Xi*w0))",
            second_identity="minus full left-E12 correction of w1V plus complete rank(w0)",
            exact_Jplus="diag(1,-1)",exact_original_P_Jminus="diag(-1,1)",
            first_vector_complete_cT_cancels_before_norm=True,first_vector_no_w1rr_or_leading_T_derivative=True,
            second_vector_only_b1_r_b1_phi_and_full_rank=True,original_Nold_and_free_w1_read_without_recomputation=True,
            exact_input_weights=["1","1/388"],common_pointwise_radial_envelope="abs(rho)^(-1/4)",
            full_zero_modes_and_two_genuine_branches_retained=True)
        result,comparisons=compare_and_combine(C,D,B,AJ,values,gate)
        doc.update(original_complete_source_terms_read=31,new_complete_uniform_term_comparisons=2,
            new_complete_scalar_recombinations=3,complete_comparison_conclusions=comparisons,
            complete_source_conclusion=result,strictly_smaller_complete_local_terms=sum(
                int(v["strict_complete_term_improvement"]) for v in comparisons))
        base=AJ["complete_source_conclusion"]
        gate("only two declared local terms may change while all twenty-nine other terms and the actual measure remain verbatim",
            all(v==result["complete_first_source_term_L2_upper"][k]
                for k,v in base["complete_first_source_term_L2_upper"].items() if k not in ("local_raw_1","local_raw_2"))
            and result["complete_independent_mean_term_L2_upper"]==base["complete_independent_mean_term_L2_upper"]
            and result["mean_L2_upper"]==base["mean_L2_upper"]
            and result["nonlocal_total_L2_upper"]==base["nonlocal_total_L2_upper"]
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete negative source remains finite with all ordinary and independent-mean output windows",
            all(bound(result[k]).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(original_fixed_intrinsic_parameter="eta_0",original_physical_piece_2549_only=True,
            same_repaired_family_and_complete_complex_squares=True,both_genuine_columns_and_signed_inputs=True,
            original_complete_parameter_dependent_potential_retained=True,full_old_and_physical_even_means_retained=True,
            new_negative_evaluation_radius_only=True,new_complete_Taylor_derivative_bounds_not_old_amplitude_unchanged_flag=True,
            old_Nraw_Taylor_transport_and_profiles_only_read=True,
            old_circle_windows_and_source_to_cut_inputs_unchanged=True,
            physical_reference_seams_root_and_affine_jumps_remain_separate=True,
            positive_growing_graph_and_strong_return_not_claimed=True)
        temporary.update(original_restored_free_budget_audit=original_temp,
            new_negative_Taylor_positive_addend_details=taylor_temp,
            new_complete_scalar_geometry=encode(geometry),new_complete_local_vector_details=encode(local_temp))
        doc.update(complete=True,proved=True,actual_returncode=0,full_physical_negative_volume_source_paid=True)
    except Exception as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        native=a.out_dir/"temporary-correlated-radial-local-sources.json.gz"
        save(native,dict(summary=doc,intermediate=temporary),True)
        doc.update(temporary_native_sha256=sha(native),temporary_native_bytes=native.stat().st_size,
            temporary_native_is_not_published=True)
        # Small scientific conclusions only: no original rows, coefficient
        # arrays, recovered finite/tail detail or new intermediate table.
        encoded=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
        if len(encoded)>60000:raise ValueError("the complete scientific conclusion exceeds its small-text budget")
        save(a.out_dir/"process.json",doc)
        report=render(doc).encode()
        if len(report)>60000:raise ValueError("the scientific readable conclusion exceeds its small-text budget")
        (a.out_dir/"conclusion.md").write_bytes(report)
    print(json.dumps(dict(complete=doc["complete"],actual_returncode=doc["actual_returncode"],
        failure=doc["failure"],gates=len(doc["gates"]),process_sha256=sha(a.out_dir/"process.json"),
        conclusion_sha256=sha(a.out_dir/"conclusion.md")),sort_keys=True),flush=True)
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())
