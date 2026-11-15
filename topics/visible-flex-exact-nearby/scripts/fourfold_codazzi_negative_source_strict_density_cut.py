#!/usr/bin/env python3
"""Read accepted rows and pay complete negative source to strict density cut constants.

Only new cut scalar arithmetic is performed. Old norms, jets, Cauchy energies
and complete source integrals are read unchanged. All numerical execution is
restricted to this repository's public Actions.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,sys,time,traceback
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
KIND="complete_negative_source_to_strict_density_cut_readout_v1"
NORM_SHA="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
NORM_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
NORM_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
FORCE_SHA="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47"
FORCE_SOURCE="ba25934f0f6e147f293644edc93b2adf1c33d5935f86596d96355cf063c95fa6"
FORCE_MANIFEST="a7790a87932a22997e29dfa2085982ac7adbbef9fd36512918eec975dd3c5341"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
CAUCHY_SHA="238a85156791fac2516a23c5f9a6ea1253e648c341bedae139d1c2c5c47cbee5"
CAUCHY_SOURCE="9acc1e8187663b91845347878034a384f5ff25b939e7faa0a1ab72f7f8738de9"
SHARED_SHA="517de329d0cee3466523e9eaaa2747a79ab3da2c771d4ec2984b38784a9b33ee"
G_SOURCE="a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7"
G_MANIFEST="bbfbdbc206f4d724288f8ecb5d9613523f5103ae7c1276ff59f2aaa055476665"
G_EXECUTION="5e5f414a53404f122fbe7c5f5ae073a86402305a7485a6afd44cda940ca5902c"
RADII=(Q(1,1000),Q(1,500),Q(1,200),Q(1,100),Q(3,200),Q(1,50))
ROOTS=("1191984371497/5000000000000","2383968743003/10000000000000")
DELTA="1/100000000"
CUTOFF=97
NMIN=388
GATE_COUNT=17

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith(".gz") else b)
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    b=(json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False)+"\n").encode()
    if str(p).endswith(".gz"):b=gzip.compress(b,mtime=0)
    t=p.with_name(p.name+".partial");t.write_bytes(b);t.replace(p)
def small_save(p,v):
    raw=(json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False)+"\n").encode()
    if len(raw)>60000:raise ValueError("the final small scientific conclusion exceeds 60000 bytes")
    p=Path(p);t=p.with_name(p.name+".partial");t.write_bytes(raw);t.replace(p)
def ex(x):
    q=Q(x);return arb(q.numerator)/q.denominator
def box(v):
    if isinstance(v,dict):
        if "lower" in v and "upper" in v:
            return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
        return arb(v["ball"])
    return arb(v)
def up(x):
    v=arb(x)
    if not v.is_finite():raise ValueError("nonfinite complete scalar bound")
    return abs(v).upper()
def lower_positive(x,name):
    a=arb(x).lower()
    if not a.is_finite() or not a>0:raise ValueError("missing positive complete lower bound: "+name)
    return a
def pos(x):
    a=arb(x)
    if not a.is_finite() or a.lower()<0:raise ValueError("a positive scalar budget is nonfinite or negative")
    return a.upper()
def record(x):return {"ball":arb(x).str(64)}
def allpass(g,n):
    return isinstance(g,list) and len(g)==n and all(v.get("passed") is True for v in g)
def check(doc,name,truth):
    passed=bool(truth);doc["gates"].append({"name":name,"passed":passed})
    if not passed:raise ValueError("negative strict-cut gate failed: "+name)
def checked(p,e):
    if not Path(p).is_file() or Path(p).stat().st_size!=e["bytes"] or sha(p)!=e["sha256"]:
        raise ValueError("complete immutable input differs: "+str(p))
def relpath(s):
    p=Path(s)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(TOPIC+"/"):
        raise ValueError("a pinned input left its exact topic path")
    return p

def input_documents(args,doc):
    m=read(args.manifest)
    if sha(args.manifest)!=args.manifest_sha:raise ValueError("the exact input manifest SHA differs")
    receipts={}
    for entry in m["files"]:
        path=args.repo/relpath(entry["path"]);checked(path,entry)
        if entry["path"] in receipts:raise ValueError("duplicate complete manifest file")
        receipts[entry["path"]]=copy.deepcopy(entry)
    paths=m["input_paths"]
    if any(path not in receipts for path in paths.values()):
        raise ValueError("an input role is not pinned as a complete file")
    if (m["scientific_source_sha256"]!=sha(__file__)
        or receipts[paths["scientific_source"]]["sha256"]!=sha(__file__)):
        raise ValueError("the complete new scientific source is not the pinned one")
    check(doc,"complete_immutable_input_bytes_and_source_manifest_identity",True)
    doc["verified_input_files"]=len(receipts)
    doc["complete_input_receipts_sha256"]=digest(receipts)
    def get(role):return read(args.repo/paths[role])
    norm,force,np,fp=get("original_norm_native"),get("original_forcing_native"),get("original_norm_process"),get("original_forcing_process")
    for role,expected in (("original_norm_native",NORM_SHA),("original_forcing_native",FORCE_SHA),
                          ("cauchy_summary",CAUCHY_SHA),("shared_intrinsic_manifest",SHARED_SHA),
                          ("genuine_source_execution",G_EXECUTION)):
        if receipts[paths[role]]["sha256"]!=expected:raise ValueError("a frozen original identity changed: "+role)
    check(doc,"two_complete_original_natives_and_actual_zero_children",
        norm.get("complete") and norm.get("proved") and norm.get("failure") is None
        and force.get("complete") and force.get("proved") and force.get("failure") is None
        and norm.get("source_sha256")==NORM_SOURCE and force.get("source_sha256")==FORCE_SOURCE
        and allpass(norm.get("gates"),7) and allpass(force.get("gates"),14)
        and len(norm.get("coefficient_rows",[]))==1328 and len(force.get("rows",[]))==1328
        and all(p.get("complete") and p.get("failure") is None and p.get("actual_returncode")==0
            and p.get("mathematical_complete") and p.get("mathematical_failure") is None for p in (np,fp))
        and str(np.get("run_id"))=="43629465215" and str(fp.get("run_id"))=="43624260519"
        and np.get("native_sha256")==NORM_SHA and fp.get("native_sha256")==FORCE_SHA
        and np.get("native_bytes")==4837715 and fp.get("native_bytes")==6577892
        and np.get("mathematical_source_sha256")==NORM_SOURCE and fp.get("mathematical_source_sha256")==FORCE_SOURCE
        and np.get("manifest_sha256")==NORM_MANIFEST and fp.get("manifest_sha256")==FORCE_MANIFEST
        and allpass(np.get("mathematical_gates"),7) and allpass(fp.get("mathematical_gates"),14))
    check(doc,"same_full_real_delta_family_root_bracket_and_original_root",
        norm.get("root_native_sha256")==force.get("root_native_sha256")==ROOT_SHA
        and norm.get("first_forcing_native_sha256")==FORCE_SHA
        and norm.get("exact_root_interval")==force.get("exact_root_interval")==list(ROOTS)
        and norm.get("exact_real_delta_radius")==force.get("exact_real_delta_radius")==DELTA
        and norm.get("exact_cover")==force.get("exact_cover")
        and norm.get("old_mean_and_all_Fourier_outputs_retained") is True
        and force.get("full_original_193_direction_and_even_mean_retained") is True)
    edge=Q(force["exact_cover"][0]);selected={}
    for index,(nr,fr) in enumerate(zip(norm["coefficient_rows"],force["rows"])):
        lo,hi=map(Q,fr["interval"])
        if (nr["common_row"]!=index or nr["interval"]!=fr["interval"]
            or nr["original_root_row"]!=fr["original_root_row"] or lo!=edge or not lo<hi):
            raise ValueError("a same-row complete coefficient or exact closed cover identity changed")
        edge=hi
        for R in RADII:
            cut=Q(ROOTS[1])-R
            if lo<=cut<=hi:selected.setdefault(str(R),[]).append((index,nr,fr))
    check(doc,"all1328_saved_norm_rows_and_forcing_rows_match_without_recalculation",
        edge==Q(force["exact_cover"][1]) and len(selected)==6
        and all(1<=len(rows)<=2 for rows in selected.values()))
    cauchy,shared=get("cauchy_summary"),get("shared_intrinsic_manifest")
    check(doc,"all_six_original_Cauchy_radii_and_both_complete_windows_reused",
        cauchy.get("complete") and cauchy.get("failure") is None and allpass(cauchy.get("gates"),8)
        and cauchy.get("source_sha256")==CAUCHY_SOURCE
        and cauchy.get("native_sha256")=="3a214897f5dc47e1a1fed3db327f54fcc0302ad6fd273ea96ecdbfcc0ca4f1e0"
        and cauchy.get("input_sha256",{}).get("root-native")==ROOT_SHA
        and cauchy.get("exact_root_interval")==list(ROOTS)
        and cauchy.get("exact_real_delta_radius")==DELTA
        and cauchy.get("all_frequencies_and_independent_even_mean_retained") is True
        and tuple(Q(c["exact_radius"]) for c in cauchy.get("cases",[]))==RADII
        and all(c.get("passed") for c in cauchy["cases"]))
    check(doc,"the_original_shared_intrinsic_identity_is_not_redefined",
        shared.get("kind")=="fixed_original_intrinsic_third_jet_parts_for_real_root_radius_one_over_fifty_v1"
        and shared.get("repository")==PUBLIC and shared.get("original_body_run")==43583838026
        and shared.get("original_body_attempt")==1 and len(shared.get("parts",[]))==6)
    body={};part_receipts=[]
    for part_number in range(3):
        spec=shared["parts"][part_number];role="original_intrinsic_part_"+str(part_number)
        path=args.repo/paths[role];entry=receipts[paths[role]];part=read(path)
        first,end=spec["common_row_indices"]
        if (entry["sha256"]!=spec["sha256"]
            or part.get("kind")!="actual_full_regular_joint_radial_polynomial_residual_rows_v1"
            or part.get("complete") is not False or part.get("selected_cells_complete") is not True
            or part.get("failure") is not None or part.get("identity")!=shared["original_row_identity"]
            or part.get("selected_indices")!=[first,end] or len(part.get("rows",[]))!=spec["rows"]):
            raise ValueError("an exact original complete intrinsic part identity failed")
        edge=Q(spec["exact_interval"][0])
        for index,row in enumerate(part["rows"],first):
            lo,hi=map(Q,row["interval"])
            if row.get("common_row")!=index or lo!=edge or not lo<hi or index in body:
                raise ValueError("the old natural intrinsic rows lost their exact cover")
            body[index]=(row,spec["sha256"]);edge=hi
        if edge!=Q(spec["exact_interval"][1]) or end-first!=len(part["rows"]):
            raise ValueError("the old complete intrinsic part endpoint differs")
        part_receipts.append(dict(original_artifact=spec["artifact"],inner_path=spec["inner_path"],
            bytes=entry["bytes"],sha256=entry["sha256"],common_row_indices=spec["common_row_indices"]))
    check(doc,"only_three_complete_original_intrinsic_parts_are_restored",
        len(body)==677 and len(part_receipts)==3)
    doc["original_intrinsic_part_receipts"]=part_receipts
    for rows in selected.values():
        for _,_,fr in rows:
            br,_=body[fr["original_common_row"]]
            if (fr["original_intrinsic_interval"]!=br["interval"]
                or fr["actual_scalar_germ"]!=br["actual_scalar_germ"]):
                raise ValueError("a cut used a different original scalar germ or whole intrinsic interval")
    rlo,rhi=map(Q,ROOTS)
    check(doc,"all_fixed_rplus_minus_R_cuts_keep_the_true_rho_window_and_zero_intrinsic_bump",
        all(Q(9,50)<rhi-R<rlo and 0<R-(rhi-rlo)<=R for R in RADII))
    ge=get("genuine_source_execution");gs=ge.get("actual_scientific_receipt",{})
    check(doc,"accepted_factored_genuine_source_child0_and_all25_gates_are_immutable",
        ge.get("complete") and ge.get("actual_returncode")==0 and ge.get("actual_failure") is None
        and str(ge.get("run_id"))=="43714194714" and str(ge.get("run_attempt"))=="1"
        and ge.get("source_budget_source_sha256")==G_SOURCE and ge.get("input_manifest_sha256")==G_MANIFEST
        and gs.get("complete") and gs.get("proved") and gs.get("actual_returncode")==0
        and gs.get("failure") is None and gs.get("source_sha256")==G_SOURCE
        and gs.get("input_manifest_sha256")==G_MANIFEST and allpass(gs.get("gates"),25))
    source=gs["complete_source_conclusion"];par=gs["mathematical_parameters"]
    support=list(map(Q,source["exact_negative_physical_cover"]))
    check(doc,"same_first_source_and_independent_mean_windows_all31_terms_and_full_support",
        source["first_output_window"]=="ordinary L2_r H^(-2/3)"
        and source["independent_even_mean_window"]=="ordinary L2_r of the constant source row"
        and len(source["complete_first_source_term_L2_upper"])==21
        and len(source["complete_independent_mean_term_L2_upper"])==10
        and source["actual_dr_measure"] is True and source["both_density_windows_retained"] is True
        and source["one_sided_uncertain_root_band_retained"] is True
        and par["fixed_intrinsic_parameter"]=="eta_0"
        and par["complete_complex_delta_square_halfwidth"]==DELTA
        and par["exact_root_interval"]==list(ROOTS) and par["cutoff_abs_j"]==97
        and all(rhi-R<=support[0]<support[1]<=rhi for R in RADII))
    doc["accepted_genuine_source"]={
        "run":"43714194714/1","execution_sha256":G_EXECUTION,
        "source_sha256":G_SOURCE,"input_manifest_sha256":G_MANIFEST,
        "complete_source_conclusion_sha256":digest(source),
        "exact_negative_physical_cover":source["exact_negative_physical_cover"],
        "first_L2_upper":copy.deepcopy(source["first_L2_upper"]),
        "mean_L2_upper":copy.deepcopy(source["mean_L2_upper"]),
        "combined_L2_upper":copy.deepcopy(source["combined_L2_upper"]),
        "complete_first_row_term_count":21,"complete_independent_mean_term_count":10,
        "original_complete_source_ledger_unchanged":True}
    return m,selected,body,cauchy,source

def cut_row_budget(nr,fr,br):
    """N.14--16 only: read full old jets/norms, pay new cut-normalizer scalars."""
    c=nr["bounds"];j=fr["complete_intrinsic_ordinary_jets"]
    K=box(j["K"][0]);Km=-K
    qlo=lower_positive(Km.lower(),"negative K at the actual cut").sqrt().lower()
    qhi=Km.upper().sqrt().upper()
    kr,krr=up(box(j["K"][1])),up(box(j["K"][2]))
    qr=pos(kr/(2*qlo))
    qrr=pos(krr/(2*qlo)+kr*kr/(4*qlo*qlo*qlo))
    b,brad=up(box(j["beta"][0])),up(box(j["beta"][1]))
    em=lower_positive(box(c["eta_lower"]),"original actual eta")
    ep=pos(box(c["eta_upper"]))
    er=up(box(fr["full_actual_eta_derivatives"][1]))
    mean=box(fr["full_actual_mean_derivatives"][0])
    if not mean.upper()<0:raise ValueError("the actual complete moving mean lost its original sign")
    mm=lower_positive(-mean.upper(),"absolute complete moving mean")
    arad=box(br["intrinsic_whole_third_jets"]["a"])
    lower_positive(arad,"actual physical intrinsic radius")
    ap=arad.upper()
    U=[pos(box(x)) for x in c["U"][:2]]
    V=[pos(box(x)) for x in c["V"][:2]]
    Ur=pos(box(c["Ur"][0]));Vr=pos(box(c["Vr"][0]))
    D=[pos(box(x)) for x in c["D"][:2]]
    rv=pos(U[0]+qhi*V[0]);rp=pos(U[1]+qhi*V[1])
    rr=pos(Ur+qhi*Vr+qr*V[0])
    amin=lower_positive(em*qlo,"eta q");amax=pos(ep*qhi)
    ar=pos(er*qhi+ep*qr)
    B=pos(qr/(2*qlo)+b*(1+rv*rv))
    Bp=pos(2*b*rv*rp)
    Br=pos(qrr/(2*qlo)+qr*qr/(2*qlo*qlo)+brad*(1+rv*rv)+2*b*rv*rr)
    S=pos(B/(2*amin));Sp=pos(Bp/(2*amin))
    Sr=pos(Br/(2*amin)+B*ar/(2*amin*amin))
    E=pos(Bp+b*rp*rv+(D[0]+amax)*Sp+Sr+S*D[1])
    S2=pos(E/(2*amin))
    ng=pos(ap*ap/(mm*mm))
    T=pos(max(qhi.sqrt().upper(),(1/qlo).sqrt().upper()))
    W=pos(ng*T)
    public=dict(q_lower=qlo,q_upper=qhi,eta_lower=em,absolute_mean_lower=mm,
        physical_radius_upper=ap,quadratic_density_radial_factor_upper=ng,
        complete_wave_matrix_upper=T,complete_radial_density_map_upper=W,
        first_normalizer_coefficient_upper=S,second_normalizer_coefficient_upper=S2)
    temporary=dict(public,abs_q_r_upper=qr,abs_q_rr_upper=qrr,
        wave_value_upper=rv,wave_phi_upper=rp,wave_radial_upper=rr,
        characteristic_gap_half_lower=amin,characteristic_speed_radial_upper=ar,
        B_upper=B,B_phi_upper=Bp,B_radial_upper=Br,
        S_phi_upper=Sp,S_radial_upper=Sr,second_offdiagonal_upper=E)
    return public,temporary

def cut_conclusion(radius,rows,body,cauchy,source):
    raw=[];ids=[]
    for serial,nr,fr in rows:
        br,partsha=body[fr["original_common_row"]]
        pub,tmp=cut_row_budget(nr,fr,br)
        raw.append((pub,tmp))
        ids.append(dict(original_norm_row=serial,original_root_row=fr["original_root_row"],
            original_common_row=fr["original_common_row"],exact_interval=fr["interval"],
            original_intrinsic_interval=fr["original_intrinsic_interval"],
            original_intrinsic_part_sha256=partsha,
            original_saved_norm_row_sha256=digest(nr),
            original_saved_forcing_row_sha256=digest(fr),
            original_saved_intrinsic_row_sha256=digest(br)))
    minima={"q_lower","eta_lower","absolute_mean_lower"}
    numbers={key:(min(p[key] for p,_ in raw).lower() if key in minima
                 else max(p[key] for p,_ in raw).upper()) for key in raw[0][0]}
    S,S2=numbers["first_normalizer_coefficient_upper"],numbers["second_normalizer_coefficient_upper"]
    tau1=pos(S/NMIN);tau2=pos(S2/(NMIN*NMIN))
    d1=(1-tau1).lower();d2=(1-tau2).lower()
    inverse_pass=bool(d1>0 and d2>0)
    old=next(c for c in cauchy["cases"] if Q(c["exact_radius"])==radius)
    paid=old["bounds"]["primitive_after_Hminus1"]
    rootgain=pos(box(paid["full_root_bracket_to_L2"]))
    sourcegain=pos(box(paid["ordinary_L2_radial_source_to_L2"]))
    W=numbers["complete_radial_density_map_upper"]
    unroot=pos(W*rootgain);unsource=pos(W*sourcegain)
    source_pair=pos(box(source["combined_L2_upper"]))
    out=dict(exact_radius=str(radius),exact_fixed_cut=str(Q(ROOTS[1])-radius),
        exact_true_rho_interval=[str(radius-(Q(ROOTS[1])-Q(ROOTS[0]))),str(radius)],
        complete_cut_sides=len(rows),complete_original_cut_row_identity=ids,
        saved_Cauchy_case_sha256=digest(old),
        saved_primitive_root_and_jump_gain=copy.deepcopy(paid["full_root_bracket_to_L2"]),
        saved_primitive_ordinary_source_gain=copy.deepcopy(paid["ordinary_L2_radial_source_to_L2"]),
        complete_cut_coefficients={k:record(v) for k,v in numbers.items()},
        first_normalizer_tau=record(tau1),second_normalizer_tau=record(tau2),
        first_normalizer_margin_lower=record(d1),second_normalizer_margin_lower=record(d2),
        cutoff97_two_ordered_normalizers_proved=inverse_pass,
        unnormalized_density_root_and_jump_gain=record(unroot),
        unnormalized_density_ordinary_source_gain=record(unsource),
        unnormalized_density_genuine_source_contribution=record(pos(unsource*source_pair)),
        genuine_input_window="H^(-4/3), two columns and both signs |j|>=97",
        ordinary_input_window="L2_r H^(-2/3) first plus independent constant second row",
        output_window="L2 old-circle density pair plus both mean coordinates",
        finite_head_and_all_mean_coordinates_retained=True,
        actual_root_and_affine_jump_columns_evaluated=False,
        exact_original_support_zero_extended_outside_its_actual_interval=True,
        complete_source_ledger_recomputed=False)
    if inverse_pass:
        inv=pos(1/(d1*d2))
        out["ordered_normalizer_inverse_gain"]=record(inv)
        out["normalized_density_root_and_jump_gain"]=record(pos(inv*unroot))
        out["normalized_density_ordinary_source_gain"]=record(pos(inv*unsource))
        out["normalized_density_genuine_source_contribution"]=record(pos(inv*unsource*source_pair))
    else:
        out["normalized_density_conclusion_omitted_reason"]="at least one sufficient cutoff97 contraction test did not pass"
    temp=[{k:record(v) for k,v in t.items()} for _,t in raw]
    return out,temp

def report(doc):
    lines=["# Actual complete negative source to strict density cut readout","",
        "This is a new scalar consumer of completed original rows. It does not recompute old jets, angular norms, Cauchy energies or source integrals.","",
        "- Repository: "+PUBLIC,
        "- Public run: "+doc["run_id"]+"/"+doc["run_attempt"],
        "- Scientific source SHA256: "+doc["source_sha256"],
        "- Manifest SHA256: "+doc["input_manifest_sha256"],
        "- Actual child return code: "+str(doc["actual_returncode"]),
        "- Passed identity and scalar-completeness gates: "+str(sum(g["passed"] for g in doc["gates"]))+"/"+str(len(doc["gates"])),
        "- New completed cut scalar budgets: "+str(doc["new_cut_scalar_budgets"]),
        "- Cuts passing both cutoff97 normalizers: "+str(doc["proved_normalized_cut_readouts"])+"/6",
        "- Old successful mathematical enclosures recomputed: 0","",
        "Every fixed cut is r_plus - R. The true rho interval includes the entire original root bracket. All frequencies, both wave rows, the complete finite head and the independent physical mean remain.","",
        "## Actual cut conclusions","",
        "| R | Exact fixed cut | tau1 | tau2 | Both inverse tests | Ordinary source to normalized density | Accepted genuine-source contribution |",
        "|---|---|---|---|---|---|---|"]
    def b(v):return v["ball"].replace("|","\\|")
    for c in doc["cut_conclusions"]:
        lines.append("| "+ " | ".join([c["exact_radius"],c["exact_fixed_cut"],b(c["first_normalizer_tau"]),
            b(c["second_normalizer_tau"]),"passed" if c["cutoff97_two_ordered_normalizers_proved"] else "not proved",
            b(c["normalized_density_ordinary_source_gain"]) if c["cutoff97_two_ordered_normalizers_proved"] else "omitted",
            b(c["normalized_density_genuine_source_contribution"]) if c["cutoff97_two_ordered_normalizers_proved"] else "omitted"])+" |")
    for c in doc["cut_conclusions"]:
        lines.extend(["","### R = "+c["exact_radius"],"",
            "- True rho interval: ["+", ".join(c["exact_true_rho_interval"])+"]",
            "- Complete one-sided rows read: "+str(c["complete_cut_sides"]),
            "- Raw density root and affine-jump bracket gain: "+b(c["unnormalized_density_root_and_jump_gain"]),
            "- Raw density ordinary source gain: "+b(c["unnormalized_density_ordinary_source_gain"]),
            "- Raw density genuine-source contribution: "+b(c["unnormalized_density_genuine_source_contribution"])])
        if c["cutoff97_two_ordered_normalizers_proved"]:
            lines.extend(["- Ordered inverse norm: "+b(c["ordered_normalizer_inverse_gain"]),
                "- Normalized root and affine-jump bracket gain: "+b(c["normalized_density_root_and_jump_gain"])])
    lines.extend(["","## Scope and reuse","",
        "The source is the complete accepted run43714194714/1 operator, with all 21 first-row terms and ten independent-mean terms. Its ledger is unchanged. No new radial integration is used.",
        "",
        "The new output is the complete old-circle density after the two specified strict normalizers, together with the retained means. Root input and actual affine jumps have separate displayed gains and have not been evaluated or deleted. A failed sufficient normalizer test leaves the displayed raw density bound valid and does not assert singularity.",
        "",
        "Ray-density changes, strict propagation, positive regular graph, root mixed data, physical-angle bridge, full strong return and finite-border inversion are not supplied here. This is not the core GH or an infinite BVP inverse.",
        "",
        "Only this small conclusion and execution metadata are published. Full supporting cut scalars remain temporary; no arrays, native certificates, Releases or new data artifacts are stored."])
    if doc.get("failure"):lines.extend(["","## Actual failure","",doc["failure"]])
    return "\n".join(lines)+"\n"

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new numerical work is confined to the authorized public Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise ValueError("the frozen runtime changed")
    ctx.prec=320;a.out_dir.mkdir(parents=True,exist_ok=True)
    process=a.out_dir/"process.json";native=a.out_dir/"temporary-negative-cut-readout.json.gz"
    conclusion=a.out_dir/"conclusion.md";started=time.monotonic()
    if process.exists():
        previous=read(process)
        if (previous.get("complete") and previous.get("actual_returncode")==0
            and previous.get("source_sha256")==sha(__file__)
            and previous.get("input_manifest_sha256")==a.manifest_sha
            and previous.get("runtime")==runtime and allpass(previous.get("gates"),GATE_COUNT)
            and conclusion.is_file() and sha(conclusion)==previous.get("conclusion_sha256")):
            print(json.dumps(dict(reused_complete_same_identity_conclusion=True,new_cut_scalar_budgets=0)),flush=True)
            return
        raise FileExistsError("preserve the prior temporary outcome; no silent replay")
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ["GITHUB_RUN_ID"],
        run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],source_sha256=sha(__file__),
        input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        cut_conclusions=[],new_cut_scalar_budgets=0,new_one_sided_cut_scalar_budgets=0,
        proved_normalized_cut_readouts=0,old_numerical_enclosures_recomputed=0,
        mathematical_parameters=dict(exact_real_delta_radius=DELTA,fixed_intrinsic_parameter="eta_0",
            exact_root_interval=list(ROOTS),exact_cut_rule="r_plus-R",exact_radii=list(map(str,RADII)),
            cutoff_abs_j=CUTOFF,minimum_physical_frequency=NMIN,
            ordinary_first_window="L2_r H^(-2/3)",ordinary_second_window="L2_r constants",
            output_window="L2 old-circle density pair plus both independent means",
            normalizer_order="T2_inverse after T1_inverse",arithmetic_bits=320),
        scope=dict(original_complete_source_ledger_unchanged=True,
            accepted_old_norms_jets_Cauchy_forcing_and_sources_only_read=True,
            exact_old_quadratic_density_and_primitive_used=True,
            same_fixed_metric_eta0_and_full_real_delta_family=True,
            all_frequencies_and_finite_head_retained=True,
            all_physical_even_mean_and_wave_means_retained=True,
            actual_root_and_affine_jumps_have_separate_gain=True,
            original_negative_Cauchy_energy_recomputed=False,
            old_radial_integrals_recomputed=False,full_GH_inverse_proved=False,
            numerical_strong_return_remainder_proved=False,
            positive_regular_graph_new_window_proved=False,
            raw_physical_L2_from_Hminus1_claimed=False,
            new_reproducible_native_persisted=False))
    temporary=[]
    try:
        m,selected,body,cauchy,source=input_documents(a,doc)
        check(doc,"all_required_same_germ_cut_rows_and_physical_radius_are_saved_not_rebuilt",
            all(fr["original_common_row"] in body for rows in selected.values() for _,_,fr in rows))
        for R in RADII:
            c,t=cut_conclusion(R,selected[str(R)],body,cauchy,source)
            doc["cut_conclusions"].append(c);temporary.append(dict(exact_radius=str(R),supporting_one_sided_scalars=t))
            doc["new_cut_scalar_budgets"]+=1
            doc["new_one_sided_cut_scalar_budgets"]+=len(t)
            doc["proved_normalized_cut_readouts"]+=int(c["cutoff97_two_ordered_normalizers_proved"])
        check(doc,"all_six_complete_cut_budgets_and_both_sides_of_any_exact_join_are_evaluated",
            len(doc["cut_conclusions"])==6 and doc["new_cut_scalar_budgets"]==6)
        check(doc,"each_normalized_conclusion_exists_exactly_when_both_strict_tests_pass",
            all(("ordered_normalizer_inverse_gain" in c)==c["cutoff97_two_ordered_normalizers_proved"]
                and ("normalized_density_genuine_source_contribution" in c)==c["cutoff97_two_ordered_normalizers_proved"]
                for c in doc["cut_conclusions"]))
        check(doc,"same_accepted_source_bound_is_consumed_without_reintegration_or_ledger_changes",
            digest(source)==doc["accepted_genuine_source"]["complete_source_conclusion_sha256"]
            and doc["old_numerical_enclosures_recomputed"]==0)
        check(doc,"root_inputs_affine_jumps_finite_head_and_all_means_remain_separate",
            all(c["finite_head_and_all_mean_coordinates_retained"]
                and c["actual_root_and_affine_jump_columns_evaluated"] is False
                and c["complete_source_ledger_recomputed"] is False for c in doc["cut_conclusions"]))
        check(doc,"new_arithmetic_is_only_cut_scalars_and_accepted_complete_source_multiplication",
            doc["new_one_sided_cut_scalar_budgets"]==sum(len(x) for x in selected.values())
            and not doc["scope"]["original_negative_Cauchy_energy_recomputed"])
        check(doc,"new_small_conclusion_has_no_raw_L2_GH_positive_graph_or_strong_return_upgrade",
            not doc["scope"]["full_GH_inverse_proved"]
            and not doc["scope"]["raw_physical_L2_from_Hminus1_claimed"]
            and not doc["scope"]["numerical_strong_return_remainder_proved"]
            and not doc["scope"]["positive_regular_graph_new_window_proved"])
        if len(doc["gates"])!=GATE_COUNT:raise ValueError("the exact scientific gate inventory changed")
        doc["complete"]=True;doc["proved"]=True;doc["actual_returncode"]=0
    except Exception as error:
        doc["failure"]=type(error).__name__+": "+str(error)
        doc["traceback"]=traceback.format_exc()[-9000:]
    finally:
        doc["actual_seconds"]=time.monotonic()-started
        save(native,dict(scientific_conclusion=doc,supporting_cut_scalars=temporary))
        doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_sha256"]=sha(native)
        text=report(doc)
        if len(text.encode())>60000:raise ValueError("the small genuine conclusion exceeds 60000 bytes")
        conclusion.write_text(text)
        doc["conclusion_bytes"]=conclusion.stat().st_size
        doc["conclusion_sha256"]=sha(conclusion)
        small_save(process,doc)
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=doc["actual_returncode"],
            failure=doc["failure"],gates=len(doc["gates"]),
            new_cut_scalar_budgets=doc["new_cut_scalar_budgets"],
            proved_normalized_cut_readouts=doc["proved_normalized_cut_readouts"],
            seconds=doc["actual_seconds"],process_sha256=sha(process),
            conclusion_sha256=doc["conclusion_sha256"])),flush=True)
    if not doc["complete"]:raise SystemExit(1)
if __name__=="__main__":main()
