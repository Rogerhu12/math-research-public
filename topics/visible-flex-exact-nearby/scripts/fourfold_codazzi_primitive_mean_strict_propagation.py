#!/usr/bin/env python3
"""Complete primitive/mean strict propagation from accepted old cells.

New mathematics is only the SP scalar 2x2 comparison, the compact real-delta
curvature correction, and its exact endpoint/readout factors. No original
target, Fourier sum, intrinsic jet, repair, H1 flow, grouped curvature
integral, Cauchy estimate, normalizer or genuine source consumer is called.
All row arrays and the native audit are temporary in public Actions.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,sys,time,traceback
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_primitive_mean_strict_propagation.py"
KIND="actual_complete_primitive_mean_strict_propagation_v1"
CONTRACT="ae01c213b63ae618e4657b5966604e7fbec4acb4763ea4b8aae848e1a40a40b4"
STRICT_NATIVE="23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a"
STRICT_SOURCE="c6baae3e8448b4ceec95eeed50a38e8761207b1ca622173c1a8bccce3245b526"
BODY_MANIFEST="c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784"
BODY_SOURCE="1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07"
RESPONSE_SUMMARY="7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
N_SOURCE="179cc14abfeff1d8281a8971d5e6192439106839213f461e5be8bd1b9150e63c"
N_MANIFEST="7c07d303931747ef2d64779a0681a0a0bb5e452e15e2af330952028e2992f4fe"
RJ_SOURCE="c1ed2857915498a4f301f3ad3bd6caaeea99232b97e0b1e7f87d08e89beb23a8"
RJ_MANIFEST="e0a36c82ed4f2a7aa0ea9bbbcccee8ab3aee06ccbc78ed113a08e9f353eb93d8"
ZERO=Fraction(0)
RA=Fraction(1191939371497,5000000000000)
CUT=Fraction(2333968743003,10000000000000)
CONTROL=(Fraction(1,20),Fraction(9,50))
PARAMETERS=dict(arithmetic_bits=320,exact_real_delta_radius="1/100000000",
    exact_strict_interval=["0",str(CUT)],exact_original_strict_interval=["0",str(RA)],
    exact_compact_support=list(map(str,CONTROL)),exact_root_Cauchy_radius="1/200",
    exact_root_interval=["1191984371497/5000000000000","2383968743003/10000000000000"],
    fixed_intrinsic_parameter="eta_0",original_parameter_half_width="1/1000000000",
    original_strict_complete_rows=3071,original_body_prefix_rows=3066,
    original_body_prefix_natural_parts=17,original_strict_container_parts=5,
    exact_centre_repair_A0="0.000000000000000003861",
    exact_centre_repair_angle_A0="0.00000000000000001970",
    canonical_response_pair_A0="19",canonical_response_pair_angle_A0="83",
    canonical_response_repair_A_1over64="0.0000000000000002292",
    compact_weight_upper="1",compact_weight_first_upper="2400/13",
    compact_weight_second_upper="5280000/169",old_grouped_reverse_log_upper="4.386425547",
    comparison_coordinates=["sqrt(q)*norm(I*T(q)*h)","sqrt(q)*abs(mean(T(q)*h))"],
    complete_mean_coordinates=2,physical_frequency_factor=4,
    exponential_series_degree=18,exponential_scaled_row_norm_upper="1/4",
    original_H1_comparison_flow_reused=False,original_grouped_integral_recomputed=False,
    full_negative_BVP_or_high_inverse_claimed=False)
NATIVE_NAME="temporary-complete-primitive-mean-strict-propagation.json.gz"
EXPECTED_GATES=20

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def canonical(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)

def save_small(p,v):
    raw=canonical(v)
    if len(raw)>60000:raise ValueError("the complete small process exceeds60000 UTF8 bytes")
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(raw);tmp.replace(p)

def q(v):
    f=Fraction(v)
    return arb(f.numerator)/f.denominator

def interval(v):
    if isinstance(v,dict):
        if "lower" in v and "upper" in v:
            x=arb(v["lower"]).lower().union(arb(v["upper"]).upper())
        elif isinstance(v.get("ball"),str):x=arb(v["ball"])
        else:raise ValueError("an old complete scalar has no recorded ball or endpoints")
    elif isinstance(v,Fraction):x=q(v)
    else:x=arb(v)
    if not x.is_finite():raise ValueError("a complete scalar is nonfinite")
    return x

def up(v):
    return interval(v).upper()

def lo(v):
    return interval(v).lower()

def au(v):
    return abs(interval(v)).upper()

def rec(v):
    return {"ball":interval(v).str(64)}

def records(v):
    if isinstance(v,dict):return {k:records(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [records(x) for x in v]
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Fraction):return str(v)
    return v

def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("SP gate failed: "+name)

def check(p,size,digest):
    p=Path(p)
    if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:
        raise ValueError("a complete immutable input differs: "+str(p))

def relpath(p):
    p=Path(p)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(REL):
        raise ValueError("an SP input left the topic")
    return p

def accepted_execution(path,source,manifest,run,gates):
    v=read(path);s=v.get("actual_scientific_receipt",{})
    if not (v.get("complete") is True and v.get("actual_returncode")==0
        and v.get("source_budget_source_sha256")==source
        and v.get("input_manifest_sha256")==manifest
        and str(v.get("run_id"))+"/"+str(v.get("run_attempt"))==run
        and s.get("complete") is True and s.get("proved") is True
        and s.get("actual_returncode")==0 and s.get("failure") is None
        and s.get("source_sha256")==source and s.get("input_manifest_sha256")==manifest
        and len(s.get("gates",[]))==gates and all(x.get("passed") is True for x in s["gates"])
        and s.get("old_numerical_enclosures_recomputed")==0):
        raise ValueError("an accepted complete old execution lost its exact identity")
    return s

def inputs(a,doc):
    m=read(a.manifest)
    entries=m["files"]
    expected={e["path"]:e for e in entries}
    ok=(len(expected)==len(entries) and m.get("public_repository")==PUBLIC
        and m.get("scientific_source_path")==PRODUCER and m.get("scientific_source_sha256")==sha(__file__)
        and sha(a.manifest)==a.manifest_sha and m.get("mathematical_parameters")==PARAMETERS
        and m.get("expected_actual_gate_count")==EXPECTED_GATES)
    for e in entries:check(a.repo/relpath(e["path"]),e["bytes"],e["sha256"])
    p={k:a.repo/relpath(v) for k,v in m["input_paths"].items()}
    gate(doc,"the new source, SP contract, exact parameters and all pinned inputs are unchanged",
        ok and sha(p["contract"])==CONTRACT and sha(p["original_body_manifest"])==BODY_MANIFEST
        and sha(p["response_summary"])==RESPONSE_SUMMARY
        and sha(p["original_strict_source"])==STRICT_SOURCE)
    n=accepted_execution(p["cut_execution"],N_SOURCE,N_MANIFEST,"43716450174/1",17)
    gate(doc,"the accepted full-real-delta cut execution is the complete original seventeen-gate result",True)
    rj=accepted_execution(p["source_execution"],RJ_SOURCE,RJ_MANIFEST,"43728317408/1",27)
    gate(doc,"the accepted current genuine source is the complete original twenty-seven-gate result",True)
    ns=n["mathematical_parameters"];rp=rj["mathematical_parameters"];ledger=rj["complete_source_conclusion"]
    gate(doc,"the same eta0, full real delta, true root interval and complete two source windows agree",
        ns["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"]
        and rp["complete_complex_delta_square_halfwidth"]==PARAMETERS["exact_real_delta_radius"]
        and ns["fixed_intrinsic_parameter"]==rp["fixed_intrinsic_parameter"]=="eta_0"
        and ns["exact_root_interval"]==rp["exact_root_interval"]==PARAMETERS["exact_root_interval"]
        and ns["ordinary_first_window"]=="L2_r H^(-2/3)"
        and ns["ordinary_second_window"]=="L2_r constants"
        and ledger.get("actual_dr_measure") is True
        and ledger.get("one_sided_uncertain_root_band_retained") is True
        and len(ledger["complete_first_source_term_L2_upper"])==21
        and len(ledger["complete_independent_mean_term_L2_upper"])==10
        and ledger["exact_negative_physical_cover"]==n["accepted_genuine_source"]["exact_negative_physical_cover"])
    bm=read(p["original_body_manifest"]);ident=bm["row_identity"]
    gate(doc,"the original whole-cell physical identity, full response and both genuine means are retained",
        bm["residual_kind"]=="actual_full_regular_joint_radial_polynomial_residual_rows_v1"
        and bm["total_common_cells"]==7721 and ident["source_sha256"]==BODY_SOURCE
        and ident["candidate_sha256"]==CANDIDATE
        and ident["original_parameter_half_width"]==PARAMETERS["original_parameter_half_width"]
        and ident["full_trials"]["response"]["metadata"]["modes"]==96
        and ident["full_trials"]["response"]["metadata"]["physical_frequency_factor"]==4
        and ident["full_trials"]["response"]["metadata"]["finite_head_mean_was_not_removed_from_the_solve"] is True
        and ident["full_trials"]["response"]["metadata"]["original_fourth_Robin_row_retained"] is True)
    response=read(p["response_summary"]);bounds=response["whole_original_known_state_bounds"]
    repair=response["exact_centre_repair_bounds"]
    zr=q(PARAMETERS["canonical_response_repair_A_1over64"])
    gate(doc,"the continuous centre and canonical full response fit the already proved repair and 19/83 constants",
        response.get("complete") is True and response.get("failure") is None
        and all(g.get("passed") is True for g in response["gates"])
        and response["complete_common_rows"]==7721 and response["actual_completed_common_rows"]==7680
        and response["input_sha256"]["original-manifest"]==BODY_MANIFEST
        and response["derived_continuous_centre_definition_sha256"]==CENTRE
        and response["original_candidate_sha256"]==CANDIDATE
        and response["true_complete_mean_correction_retained"] is True
        and up(repair["A0"])<q(PARAMETERS["exact_centre_repair_A0"])
        and up(repair["angular_A0"])<q(PARAMETERS["exact_centre_repair_angle_A0"])
        and up(bounds["response_star_A0"])+zr<q(19)
        and up(bounds["response_angle_A0"])+384*zr<q(83)
        and len(response["original_parts"])==40)
    doc["accepted_small_input_conclusions"]={
        "cut":dict(run="43716450174/1",source_sha256=N_SOURCE,input_manifest_sha256=N_MANIFEST,
            execution_sha256=sha(p["cut_execution"])),
        "source":dict(run="43728317408/1",source_sha256=RJ_SOURCE,input_manifest_sha256=RJ_MANIFEST,
            execution_sha256=sha(p["source_execution"]),complete_source_conclusion_sha256=
            hashlib.sha256(canonical(ledger)).hexdigest(),
            combined_L2_upper=ledger["combined_L2_upper"],first_L2_upper=ledger["first_L2_upper"],
            mean_L2_upper=ledger["mean_L2_upper"],first_term_count=21,independent_mean_term_count=10,
            exact_negative_physical_cover=ledger["exact_negative_physical_cover"]),
        "response":dict(sha256=RESPONSE_SUMMARY,centre_definition_sha256=CENTRE,
            direction_definition_sha256=DIRECTION,complete_common_rows=7721,
            legacy_periodic_progress=7680,all_mean_corrections_retained=True)}
    return m,p,bm,response,n,rj

def restore_strict(a,m,p,doc):
    parts=read(p["strict_parts_manifest"])
    if not (parts["kind"]=="complete_native_lossless_container_binary_parts_v2"
        and parts["original_bytes"]==8499033 and parts["original_sha256"]==STRICT_NATIVE
        and parts["original_source_sha256"]==STRICT_SOURCE and parts["complete_native_rows"]==3071
        and parts["native_complete"] is True and parts["native_failure"] is None
        and len(parts["parts"])==5):
        raise ValueError("the old lossless strict container manifest changed")
    payload=[];offset=0;receipts=[]
    for i,e in enumerate(parts["parts"]):
        path=p["strict_parts_manifest"].parent/e["file"]
        check(path,e["compressed_bytes"],e["compressed_sha256"])
        b=gzip.decompress(path.read_bytes())
        if e["index"]!=i or e["offset"]!=offset or len(b)!=e["bytes"] or hashlib.sha256(b).hexdigest()!=e["sha256"]:
            raise ValueError("an original strict container part is not the exact original byte slice")
        payload.append(b);offset+=len(b)
        receipts.append(dict(index=i,offset=e["offset"],bytes=len(b),sha256=e["sha256"],
            compressed_bytes=e["compressed_bytes"],compressed_sha256=e["compressed_sha256"]))
    original=b"".join(payload)
    gate(doc,"all five old byte slices restore the original complete 8499033-byte strict certificate",
        len(original)==8499033 and hashlib.sha256(original).hexdigest()==STRICT_NATIVE)
    s=json.loads(gzip.decompress(original))
    rows=s.get("rows",[])
    edge=ZERO;valid=True
    for i,row in enumerate(rows):
        left,right=map(Fraction,row["interval"])
        gl,gr=map(Fraction,row["actual_scalar_germ"])
        valid=valid and row["common_row"]==i and left==edge and left<right and gl<=left<right<=gr
        edge=right
    gate(doc,"all 3071 complete original strict rows and true closed scalar germs retain their identity",
        s.get("kind")==parts["native_kind"] and s.get("complete") is True and s.get("failure") is None
        and s.get("source_sha256")==STRICT_SOURCE and s["exact_requested_interval"]==["0",str(RA)]
        and s["total_closed_radial_cells"]==3071 and len(rows)==3071 and edge==RA and valid
        and s["original_parameter_half_width"]==PARAMETERS["original_parameter_half_width"]
        and s.get("whole_affine_parameter_interval") is True
        and s.get("complete_original_intrinsic_tail") is True
        and s.get("all_Fourier_variations_and_mean_retained") is True)
    doc.update(original_complete_strict_rows_verified=3071,original_strict_container_parts_read=5,
        original_strict_native_bytes=8499033,original_strict_native_sha256=STRICT_NATIVE,
        original_strict_part_receipts=receipts)
    return s

def original_body_prefix(a,m,p,bm,response,doc):
    expected={tuple(e["indices"]):e["sha256"] for e in response["original_parts"] if e["indices"][1]<=3066}
    selected=m["original_body_prefix_parts"]
    if len(expected)!=17 or {tuple(e["indices"]):e["sha256"] for e in selected}!=expected:
        raise ValueError("the seventeen original natural prefix parts differ from the accepted response table")
    rows=[];receipts=[];edge=ZERO
    for e in sorted(selected,key=lambda x:x["indices"]):
        path=a.repo/relpath(e["temporary_path"]);raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=e["sha256"]:raise ValueError("an original natural prefix part changed bytes")
        v=json.loads(gzip.decompress(raw));start,stop=e["indices"]
        if not (v["kind"]==bm["residual_kind"] and v["identity"]==bm["row_identity"]
            and v["source_sha256"]==BODY_SOURCE and v["selected_indices"]==[start,stop]
            and v["selected_cells_complete"] is True and v["failure"] is None
            and len(v["rows"])==stop-start and start==len(rows)):
            raise ValueError("an original prefix native is not the complete same-identity natural shard")
        for j,row in enumerate(v["rows"],start):
            left,right=map(Fraction,row["interval"]);gl,gr=map(Fraction,row["actual_scalar_germ"])
            if row["common_row"]!=j or left!=edge or not gl<=left<right<=gr:
                raise ValueError("the complete original prefix has a gap, overlap or changed scalar germ")
            edge=right;rows.append(row)
        receipts.append(dict(indices=[start,stop],bytes=len(raw),sha256=e["sha256"]))
    gate(doc,"all seventeen original natural parts form the exact 3066-row whole-intrinsic prefix",
        len(rows)==3066 and edge>CUT and len(receipts)==17)
    doc.update(original_complete_body_prefix_rows_verified=3066,
        original_complete_body_prefix_parts_read=17,
        original_body_prefix_actual_interval=["0",str(edge)],
        original_body_prefix_part_receipts=receipts)
    return rows

def original_joint_identity(strict,bm,doc):
    ident=bm["row_identity"];meta=strict["candidate_metadata"]
    nu=Fraction(ident["exact_nu"]);d=Fraction(PARAMETERS["exact_real_delta_radius"])
    gate(doc,"the strict and whole-jet rows are the same candidate, object, eta family and exact nu within the true type interval",
        strict["object_sha256"]==ident["object_sha256"]==meta["object_sha256"]
        and CANDIDATE in strict["inputs"].values()
        and strict["exact_nu"]==ident["exact_nu"]==meta["exact_float_nu"]
        and strict["exact_amplitude"]==ident["exact_alpha"]==meta["exact_float_amplitude"]
        and strict["original_parameter_half_width"]==ident["original_parameter_half_width"]
        and meta["modes"]==32 and Fraction(-1,25)<=nu-d<=nu+d<=Fraction(-1,40))
    doc["exact_family_identity"]=dict(original_candidate_sha256=CANDIDATE,
        original_object_sha256=ident["object_sha256"],exact_alpha=ident["exact_alpha"],
        exact_nu_centre=str(nu),exact_selected_nu_interval=[str(nu-d),str(nu+d)],
        original_eta_half_width=ident["original_parameter_half_width"],
        fixed_current_eta="eta_0",continuous_centre_definition_sha256=CENTRE,
        continuous_response_definition_sha256=DIRECTION,
        complete_original_eta_enclosures_restricted_without_recomputation=True)

def refine(strict_rows,body_rows,doc):
    cuts={ZERO,CUT,*CONTROL}
    for row in strict_rows+body_rows:
        cuts.update(x for x in map(Fraction,row["interval"]) if ZERO<x<CUT)
    cuts=sorted(cuts);i=j=0;segments=[]
    for left,right in zip(cuts,cuts[1:]):
        while Fraction(strict_rows[i]["interval"][1])<=left:i+=1
        while Fraction(body_rows[j]["interval"][1])<=left:j+=1
        s,b=strict_rows[i],body_rows[j]
        sl,sr=map(Fraction,s["interval"]);bl,br=map(Fraction,b["interval"])
        if not (sl<=left<right<=sr and bl<=left<right<=br):
            raise ValueError("a new common intersection is not inside both entire original cells")
        segments.append((left,right,s,b))
    gate(doc,"the new exact common cover includes both compact seams, the whole strict interval and every one-sided germ",
        cuts[0]==ZERO and cuts[-1]==CUT and all(x in cuts for x in CONTROL)
        and sum((r-l for l,r,_,_ in segments),ZERO)==CUT)
    identity=[dict(interval=[str(l),str(r)],strict_row=s["common_row"],
                   body_row=b["common_row"],strict_germ=s["actual_scalar_germ"],
                   whole_jet_germ=b["actual_scalar_germ"]) for l,r,s,b in segments]
    doc["new_common_intersection_count"]=len(segments)
    doc["new_common_cover_sha256"]=hashlib.sha256(canonical(identity)).hexdigest()
    return segments,identity

def selected_cell(s,b,left,right):
    """SP20--28: only new full-delta scalar assembly, using old complete balls."""
    base=s["base"];st=s["strong"];old=s["actual_target"];jets=b["intrinsic_whole_third_jets"]
    beta=au(old["beta"]);gamma=interval(old["gamma"]);K0=interval(old["K"])
    qold=interval(base["q"]);qlo=qold.lower();qhi=qold.upper()
    if not qlo>0 or not gamma.lower()>0 or not K0.upper()<0:
        raise ValueError("an original entire strict cell lost its negative curvature or positive gamma")
    active=left<CONTROL[1] and right>CONTROL[0]
    if active and not CONTROL[0]<=left<right<=CONTROL[1]:
        raise ValueError("the new scalar intersection crosses a compact seam")
    d=q(PARAMETERS["exact_real_delta_radius"])
    eps0=q(PARAMETERS["exact_centre_repair_A0"])+19*d
    eps1=q(PARAMETERS["exact_centre_repair_angle_A0"])+83*d
    tp=t1=h0=h1=eq=arb(0);Hmargin=arb(1)
    if active:
        aa=interval(jets["a"]);gg=interval(jets["gamma"]);bb=au(jets["beta"])
        if not aa.lower()>0 or not gg.lower()>0:
            raise ValueError("an entire original intrinsic cell has no positive a/gamma denominator")
        W1=q(PARAMETERS["compact_weight_first_upper"]);W2=q(PARAMETERS["compact_weight_second_upper"])
        tp=up(bb/(2*gg.lower()**2*aa.lower()**2))
        t1=up(au(jets["beta1"])/(2*gg.lower()**2*aa.lower()**2)
            +bb*au(jets["gamma1"])/(gg.lower()**3*aa.lower()**2)
            +bb**2/(gg.lower()**2*aa.lower()**2))
        full=(d).exp()
        kd=up((full-1)*au(K0)+d*full*tp*W1)
        # A whole upper on |Kdelta-K0| gives this entire negative interval.
        Kdelta=K0.union(K0-kd).union(K0+kd)
        if not Kdelta.upper()<0:raise ValueError("the full selected delta curvature is not strictly negative")
        qdlo=(-Kdelta.upper()).sqrt().lower()
        qdhi=(-Kdelta.lower()).sqrt().upper()
        kmin=lo(qlo*qlo)
        h0=up(tp*W1/kmin)
        h1=up((t1*W1+tp*W2)/kmin+tp*W1*au(old["K1"])/(kmin*kmin))
        Hmargin=lo(1-d*h0)
        if not Hmargin>0:raise ValueError("the entire selected compact delta H denominator is unresolved")
        eq=up(d*W1/2+d*h1/(2*Hmargin))
        gp=up(gamma.upper()*(d/2).exp())
        qdiff=up(kd/(qlo+qdlo))
    else:
        kd=arb(0);Kdelta=K0;qdlo=qlo;qdhi=qhi;gp=gamma.upper();qdiff=arb(0)
    R0=up(base["actual_R_upper"]);L0=up(base["actual_L_upper"])
    V0=up(base["v_abs_upper"]);V1=up(base["full_v_phi_absolute"])
    R=up(R0+max(arb(1),qdhi)*eps0+qdiff*V0)
    L=up(L0+max(arb(1),qdhi)*eps1+qdiff*V1)
    DU=up(2*R0*eps0+eps0**2)
    DKV=up(au(Kdelta)*(2*V0*eps0+eps0**2)+kd*V0**2)
    DS=up(DU+DKV);D=up(au(base["actual_d_phi"])+2*beta*DS)
    F0=max(up(base["forward_diagonal_1"]),up(st["forward_Y2_rate"]))
    B0=max(up(-interval(base["forward_diagonal_1"])),up(st["backward_Y2_rate"]))
    F=up(F0+4*beta*DS);Brev=up(B0+4*beta*DS)
    B1=up(4*beta*R*L);A1=up(6*beta*R*L)
    Ny=up(2*beta*L*(R+L/4));Nz=up(beta*L*R/2);Ngamma=up(gp*L)
    def matrix(rate):
        return [[max(arb(0),up(rate+D+(A1+Ny)/4)),
                 up(D/2+B1/16+(Nz+Ngamma)/4)],
                [up(A1+Ny),max(arb(0),up(rate+Nz))]]
    ap=matrix(F);am=matrix(Brev)
    vals=dict(q_lower=qdlo,q_upper=qdhi,beta_absolute=beta,gamma_upper=gp,
        complete_R=R,complete_L=L,complete_D=D,forward_diagonal=F,reverse_diagonal=Brev,
        Bphi_upper=B1,A_upper=A1,N_y_upper=Ny,N_z_upper=Nz,N_gamma_upper=Ngamma,
        metric_K_difference_upper=kd,new_log_curvature_difference_upper=eq,
        delta_H_margin_lower=Hmargin,T_upper=tp,T_derivative_upper=t1,
        H0_upper=h0,H1_upper=h1,compact_metric_active=active)
    if any(not x.is_finite() for mat in (ap,am) for row in mat for x in row):
        raise ValueError("a complete new scalar comparison entry is nonfinite")
    return ap,am,vals

def identity2():
    return [[arb(1),arb(0)],[arb(0),arb(1)]]

def mm(a,b):
    return [[up(a[i][0]*b[0][j]+a[i][1]*b[1][j]) for j in range(2)] for i in range(2)]

def positive_exp(a,length):
    """Entrywise upper e^(length*a), with a rigorous positive scalar-series tail."""
    z=[[up(q(length)*a[i][j]) for j in range(2)] for i in range(2)]
    r=max(up(sum(row,arb(0))) for row in z);squarings=0
    while r>q(PARAMETERS["exponential_scaled_row_norm_upper"]):
        z=[[up(x/2) for x in row] for row in z];r=up(r/2);squarings+=1
        if squarings>64:raise ValueError("the new scalar exponential requires an excessive exact scaling")
    degree=PARAMETERS["exponential_series_degree"];power=identity2();total=identity2()
    for k in range(1,degree+1):
        power=mm(power,z)
        for i in range(2):
            for j in range(2):total[i][j]=up(total[i][j]+power[i][j]/math.factorial(k))
    margin=lo(1-r/(degree+2))
    if not margin>0:raise ValueError("the positive exponential remainder ratio is unresolved")
    tail=up(r**(degree+1)/math.factorial(degree+1)/margin)
    total=[[up(x+tail) for x in row] for row in total]
    for _ in range(squarings):total=mm(total,total)
    if not all(total[i][j]>=int(i==j) for i in range(2) for j in range(2)):
        raise ValueError("a positive exponential factor is not entrywise at least identity")
    return total,squarings,tail

def frobenius(a):
    return up(sum((x*x for row in a for x in row),arb(0)).sqrt())

def propagate(segments,strict,doc):
    plus=identity2();minus=identity2();jq=arb(0);compact_length=ZERO;audits=[]
    margin=arb(1);qminimum=None;qmaximum=arb(0);squaremax=0;exp_count=0;newactive=0
    maxima={};witness={}
    for index,(left,right,s,b) in enumerate(segments):
        doc["active_phase"]="new_scalar_comparison";doc["active_common_intersection"]=index
        ap,am,v=selected_cell(s,b,left,right);h=right-left
        ep,sp,tp=positive_exp(ap,h);em,sm,tm=positive_exp(am,h)
        # Ascending r: forward factors multiply on the left; reversed flow on the right.
        plus=mm(ep,plus);minus=mm(minus,em);exp_count+=2;squaremax=max(squaremax,sp,sm)
        if v["compact_metric_active"]:
            compact_length+=h;jq=up(jq+q(h)*v["new_log_curvature_difference_upper"]);newactive+=1
        margin=min(margin,v["delta_H_margin_lower"])
        qminimum=v["q_lower"] if qminimum is None else min(qminimum,v["q_lower"])
        qmaximum=max(qmaximum,v["q_upper"])
        for name in ("complete_R","complete_L","complete_D","Bphi_upper","A_upper","N_y_upper",
                     "N_z_upper","N_gamma_upper","metric_K_difference_upper"):
            value=v[name]
            if name not in maxima or value>maxima[name]:maxima[name]=value;witness[name]=index
        audits.append(dict(interval=[str(left),str(right)],strict_row=s["common_row"],
            body_row=b["common_row"],new_selected_scalar_bounds=records(v),
            complete_forward_matrix=records(ap),complete_reverse_matrix=records(am),
            forward_positive_exponential=records(ep),reverse_positive_exponential=records(em),
            scalar_series_tail_upper=[rec(tp),rec(tm)]))
    gate(doc,"every new complete delta/metric denominator is positive on the true full compact support",
        compact_length==CONTROL[1]-CONTROL[0] and newactive>0 and margin>0 and qminimum>0)
    gate(doc,"both new chronological positive two-state products retain every common intersection",
        exp_count==2*len(segments) and all(x.is_finite() and x>=0 for mat in (plus,minus) for row in mat for x in row))
    oldc=q(PARAMETERS["old_grouped_reverse_log_upper"])
    qleft=interval(strict["rows"][0]["base"]["q"])
    qright=interval(strict["rows"][-1]["base"]["q"])
    if not qleft.lower()>0 or not qright.lower()>0:raise ValueError("the original grouped-curvature endpoints have no gap")
    cminus=up(oldc+jq)
    cplus=up(oldc+jq+(qright.upper()/qleft.lower()).log())
    gate(doc,"the original grouped log cost is read and only the new compact delta fee is integrated",
        cminus>=0 and cplus>=0 and cminus.is_finite() and cplus.is_finite())
    upmat=[[up(cplus.exp()*x) for x in row] for row in plus]
    ummat=[[up(cminus.exp()*x) for x in row] for row in minus]
    pn= frobenius(upmat);mn=frobenius(ummat)
    doc["complete_strict_propagation_conclusion"]=dict(
        exact_interval=["0",str(CUT)],complete_mean_coordinates=2,
        coordinates=PARAMETERS["comparison_coordinates"],
        forward_nonradial_product=records(plus),reverse_nonradial_product=records(minus),
        forward_complete_matrix=records(upmat),reverse_complete_matrix=records(ummat),
        forward_complete_operator_upper=rec(pn),reverse_complete_operator_upper=rec(mn),
        old_grouped_reverse_log_upper=PARAMETERS["old_grouped_reverse_log_upper"],
        new_compact_log_variation_fee_upper=rec(jq),new_complete_reverse_log_upper=rec(cminus),
        new_complete_forward_log_upper=rec(cplus),
        original_grouped_q_at_zero=qleft.str(64),original_grouped_q_at_ra=qright.str(64),
        new_delta_H_margin_lower=rec(margin),new_entire_q_lower=rec(qminimum),new_entire_q_upper=rec(qmaximum),
        complete_selected_scalar_maxima=records(maxima),maximum_witness_common_intersections=witness,
        all_shorter_ordered_products_and_source_insertions_included=True,
        affine_jumps_are_independent_without_radial_length_factor=True,
        both_one_sided_original_scalar_germs_retained=True,
        old_H1_flow_not_used_for_L2_primitive=True)
    doc.update(new_positive_two_state_exponentials=exp_count,
        new_forward_and_reverse_ordered_products=2,new_common_comparison_rows=len(segments),
        new_compact_metric_intersections=newactive,
        new_compact_log_variation_integrals=1,
        positive_exponential_max_scaling_squarings=squaremax,
        positive_exponential_series_degree=PARAMETERS["exponential_series_degree"])
    return upmat,ummat,audits

def endpoint(row):
    aa=interval(row["scalar_mean"]["actual_a"]);m=interval(row["scalar_mean"]["actual_m"])
    qb=interval(row["base"]["q"])
    error=q(PARAMETERS["exact_centre_repair_A0"])+19*q(PARAMETERS["exact_real_delta_radius"])
    mgap=lo(-m.upper()-error);mup=up(au(m)+error)
    if not aa.lower()>0 or not mgap>0 or not qb.lower()>0:
        raise ValueError("a true endpoint a/mean/q denominator is unresolved")
    # Both endpoints lie outside the exact compact metric support; a,q are unchanged.
    nglo=lo(aa.lower()**2/(mup*mup))
    nghi=up(aa.upper()**2/(mgap*mgap))
    return dict(physical_radius_lower=aa.lower(),physical_radius_upper=aa.upper(),
        complete_absolute_mean_lower=mgap,complete_absolute_mean_upper=mup,
        q_lower=qb.lower(),q_upper=qb.upper(),density_radial_factor_lower=nglo,
        density_radial_factor_upper=nghi,mean_state_repair_and_full_response_fee=error)

def endpoint_readouts(strict,segments,n,rj,upmat,ummat,doc):
    atzero=endpoint(strict["rows"][0])
    touching=[s for s in strict["rows"]
              if Fraction(s["interval"][0])<=CUT<=Fraction(s["interval"][1])]
    if not touching:raise ValueError("no complete old one-sided row contains the cut")
    sides=[endpoint(s) for s in touching]
    cut={}
    for key in sides[0]:
        cut[key]=(min(v[key] for v in sides) if key.endswith("_lower") else max(v[key] for v in sides))
    gate(doc,"the true waist and all one-sided cut a/m/q and n_g denominators are paid explicitly",
        all(v["density_radial_factor_lower"]>0 and v["complete_absolute_mean_lower"]>0 for v in [atzero,cut])
        and (CUT<=CONTROL[0] or CUT>=CONTROL[1]))
    cases=[x for x in n["cut_conclusions"] if x["exact_radius"]=="1/200"]
    if len(cases)!=1:raise ValueError("the original R=.005 cut conclusion is not unique")
    case=cases[0];tau1=up(case["first_normalizer_tau"]);tau2=up(case["second_normalizer_tau"])
    gate(doc,"the exact original R=.005 Cauchy/normalizer result retains both ordered factors and both mean coordinates",
        case["exact_fixed_cut"]==str(CUT) and case["exact_radius"]==PARAMETERS["exact_root_Cauchy_radius"]
        and case["cutoff97_two_ordered_normalizers_proved"] is True
        and case["finite_head_and_all_mean_coordinates_retained"] is True
        and case["exact_original_support_zero_extended_outside_its_actual_interval"] is True
        and tau1<1 and tau2<1)
    P=up(case["saved_primitive_root_and_jump_gain"])
    Q=up(case["saved_primitive_ordinary_source_gain"])
    kinv=up(case["ordered_normalizer_inverse_gain"])
    kp=up((1+tau1)*(1+tau2))
    um=frobenius(ummat);uf=frobenius(upmat)
    out0=up(atzero["density_radial_factor_upper"]/atzero["q_lower"].sqrt())
    in0=up(atzero["q_upper"].sqrt()/atzero["density_radial_factor_lower"])
    cutraw= max(arb(1),cut["q_upper"])
    source=up(out0*um*cutraw*Q);rootjump=up(out0*um*cutraw*P)
    normtoc0=up(out0*um*cut["q_upper"].sqrt()/cut["density_radial_factor_lower"]*kp)
    waisttocut=up(cut["density_radial_factor_upper"]/cut["q_lower"].sqrt()*kinv*uf*in0)
    ledger=rj["complete_source_conclusion"];combined=up(ledger["combined_L2_upper"])
    current=up(source*combined)
    # SP33: a separate complete insertion on the strict segment, with true dr.
    qmax=up(doc["complete_strict_propagation_conclusion"]["new_entire_q_upper"])
    injection=up(q(17).sqrt()/4*max(arb(1),qmax))
    strictback=up(out0*um*injection)
    strictforward=up(cut["density_radial_factor_upper"]/cut["q_lower"].sqrt()*kinv*uf*injection)
    doc["complete_endpoint_readout_conclusion"]=dict(
        waist_complete_radial_factors=records(atzero),cut_complete_radial_factors=records(cut),
        exact_cut=str(CUT),one_sided_cut_rows=[s["common_row"] for s in touching],
        saved_Cauchy_case_sha256=case["saved_Cauchy_case_sha256"],
        saved_primitive_root_and_jump_gain=case["saved_primitive_root_and_jump_gain"],
        saved_primitive_ordinary_source_gain=case["saved_primitive_ordinary_source_gain"],
        saved_normalizer_inverse_gain=case["ordered_normalizer_inverse_gain"],
        saved_first_normalizer_tau=case["first_normalizer_tau"],
        saved_second_normalizer_tau=case["second_normalizer_tau"],
        complete_forward_normalizer_gain=rec(kp),
        root_or_affine_jump_to_waist_density_gain=rec(rootjump),
        ordinary_root_window_source_to_waist_density_gain=rec(source),
        normalized_cut_to_waist_density_gain=rec(normtoc0),
        waist_density_to_normalized_cut_gain=rec(waisttocut),
        complete_strict_Hminus1_source_injection_upper=rec(injection),
        strict_L1_Hminus1_source_to_waist_density_gain=rec(strictback),
        strict_L2_Hminus1_source_to_waist_density_gain=rec(up(q(CUT).sqrt()*strictback)),
        strict_L1_Hminus1_source_to_normalized_cut_gain=rec(strictforward),
        strict_L2_Hminus1_source_to_normalized_cut_gain=rec(up(q(CUT).sqrt()*strictforward)),
        waist_output="L2 old-circle density pair plus both full mean coordinates",
        current_genuine_input="both genuine columns and both signs |j|>=97 in H^(-4/3)",
        current_genuine_source_pair_L2_upper=ledger["combined_L2_upper"],
        current_genuine_strong_source_to_waist_contribution_upper=rec(current),
        current_source_support=ledger["exact_negative_physical_cover"],
        all_root_and_affine_jump_inputs_still_separate=True,
        all_positive_graph_inputs_still_separate=True,
        physical_angle_or_KAM_density_changes_still_separate=True,
        no_complete_return_remainder_or_high_BVP_asserted=True)
    gate(doc,"all explicit root/source/normalizer and forward/reverse endpoint gains are complete finite upper bounds",
        all(v.is_finite() and v>=0 for v in (P,Q,kinv,kp,source,rootjump,normtoc0,waisttocut,current,injection,strictback,strictforward)))
    return case

def markdown(doc):
    lines=["# Complete primitive and mean strict propagation: actual public result","",
        "- Public repository: "+PUBLIC,
        "- Run: "+str(doc["run_id"])+"/"+str(doc["run_attempt"]),
        "- Script: "+PRODUCER,
        "- Source SHA256: "+doc["source_sha256"],
        "- Manifest SHA256: "+doc["input_manifest_sha256"],
        "- Actual scientific return code: "+str(doc["actual_returncode"]),
        "- Complete / proved: "+str(doc["complete"])+" / "+str(doc["proved"]),
        "- Exact full real delta range: "+PARAMETERS["exact_real_delta_radius"],
        "- Strict interval: [0, "+str(CUT)+"], actual moving angle and both complete means.",
        "- Old numerical enclosures recomputed: 0.",""]
    if doc.get("failure"):lines.extend(["## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False),""])
    lines.extend(["## Actual gates","","| Gate | Passed |","|---|---|"])
    lines.extend("| "+g["name"].replace("|","\\|")+" | "+str(g["passed"])+" |" for g in doc["gates"])
    def show(title,values):
        lines.extend(["","## "+title,"","| Quantity | Complete bound / identity |","|---|---|"])
        for key,value in values.items():
            if isinstance(value,dict) and "ball" in value:out=value["ball"]
            else:out=json.dumps(value,ensure_ascii=False,separators=(",",":"))
            lines.append("| "+key+" | "+out.replace("|","\\|").replace("\n"," ")+" |")
    for key,title in (("complete_strict_propagation_conclusion","Both chronological scalar propagators"),
                      ("complete_endpoint_readout_conclusion","True endpoint and complete source readouts")):
        if key in doc:show(title,doc[key])
    lines.extend(["","## Scope","",
        "The new positive 2 by 2 scalar products control the complete primitive and both independent means. "
        "They retain every one-sided old cell and the full selected real parameter interval. "
        "The original strict H1 propagator and original grouped curvature integral were not recomputed "
        "or reinterpreted as this L2 primitive evolution.",
        "",
        "The current successful 21 plus 10 genuine source terms are read without a new source integration. "
        "The displayed strong source-to-waist number is their complete contribution in the stated density coordinates. "
        "Root and affine-jump inputs have their own gain. The positive graph, actual root/jump matrices, "
        "true ray/KAM density conversion, physical-angle bridge, finite border and full high BVP remain separate.",
        "",
        "All original certificates, the new row audit and ordered factors are temporary only. "
        "This report and execution metadata are the only new persisted results.",""])
    out="\n".join(lines)
    if len(out.encode())>60000:raise ValueError("the complete readable conclusion exceeds60000 UTF8 bytes")
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args();a.repo=a.repo.resolve();a.out_dir=a.out_dir.resolve()
    a.out_dir.mkdir(parents=True,exist_ok=True)
    if (a.out_dir/"process.json").exists():raise FileExistsError("preserve the original complete or failed SP outcome")
    ctx.prec=320
    started=time.monotonic()
    doc=dict(kind=KIND,public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        complete=False,proved=False,failure=None,actual_returncode=1,gates=[],
        runtime=dict(python=platform.python_version(),python_flint=flint.__version__),
        arithmetic_bits=320,mathematical_parameters=PARAMETERS,
        old_numerical_enclosures_recomputed=0,old_target_FFT_intrinsic_or_repair_recomputed=0,
        old_strict_H1_flow_recomputed_or_reused=0,old_grouped_curvature_integral_recomputed=0,
        old_root_Cauchy_normalizer_or_source_enclosures_recomputed=0,
        old_original_source_rows_or_radial_source_integrals_recomputed=0,
        original_natural_part_bytes_modified=0,
        full_high_inverse_claimed=False,full_return_remainder_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    native=None
    try:
        gate(doc,"the unique new scalar child runs only in public Actions with Python3.12.14/flint0.9.0 and320 bits",
            os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
            and platform.python_version()=="3.12.14" and flint.__version__=="0.9.0" and ctx.prec==320)
        m,paths,bm,response,n,rj=inputs(a,doc)
        ledger_hash=hashlib.sha256(canonical(rj["complete_source_conclusion"])).hexdigest()
        strict=restore_strict(a,m,paths,doc)
        body=original_body_prefix(a,m,paths,bm,response,doc)
        original_joint_identity(strict,bm,doc)
        segments,cover=refine(strict["rows"],body,doc)
        um,ur,audits=propagate(segments,strict,doc)
        endpoint_readouts(strict,segments,n,rj,um,ur,doc)
        gate(doc,"all old successful mathematics and all31 source terms remain byte-identical and read-only",
            ledger_hash==hashlib.sha256(canonical(rj["complete_source_conclusion"])).hexdigest()
            and all(doc[k]==0 for k in ("old_numerical_enclosures_recomputed",
                "old_target_FFT_intrinsic_or_repair_recomputed","old_strict_H1_flow_recomputed_or_reused",
                "old_grouped_curvature_integral_recomputed","old_root_Cauchy_normalizer_or_source_enclosures_recomputed",
                "old_original_source_rows_or_radial_source_integrals_recomputed","original_natural_part_bytes_modified")))
        doc["scope"]=dict(same_full_real_delta_family=True,
            new_two_state_primitive_and_mean_evolution=True,
            all_Fourier_variations_and_two_means_retained=True,
            both_chronological_Cauchy_directions_retained=True,
            full_ordinary_sources_and_affine_impulses_retained=True,
            actual_radial_measure_used=True,original_curvature_scalar_integral_read_only=True,
            new_delta_curvature_correction_only=True,complete_current_RJ_ledger_read_verbatim=True,
            raw_Hminus1_state_not_called_raw_L2=True,
            physical_angle_and_KAM_density_change_not_assumed=True,
            original_positive_graph_and_root_mixed_ports_retained=True,
            full_high_BVP_or_return_inverse_not_claimed=True,new_row_arrays_published=False)
        gate(doc,"the final small conclusion has all complete scope statements and the exact gate count",
            len(doc["gates"])+1==EXPECTED_GATES
            and doc["new_positive_two_state_exponentials"]==2*doc["new_common_intersection_count"])
        native=dict(kind=KIND+"_temporary_native",source_sha256=doc["source_sha256"],
            input_manifest_sha256=a.manifest_sha,complete=True,exact_common_cover=cover,
            new_scalar_rows=audits,original_strict_native_sha256=STRICT_NATIVE,
            no_original_scientific_result_recomputed=True)
        doc["complete"]=doc["proved"]=True;doc["actual_returncode"]=0
    except Exception as exc:
        doc["failure"]=dict(type=type(exc).__name__,message=str(exc),
            phase=doc.get("active_phase"),common_intersection=doc.get("active_common_intersection"))
        traceback.print_exc()
    finally:
        doc.pop("active_phase",None);doc.pop("active_common_intersection",None)
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        if native is not None:
            raw=gzip.compress(canonical(native),mtime=0)
            (a.out_dir/NATIVE_NAME).write_bytes(raw)
            doc["temporary_native_sha256"]=hashlib.sha256(raw).hexdigest()
            doc["temporary_native_bytes"]=len(raw)
        try:
            text=markdown(doc);(a.out_dir/"conclusion.md").write_text(text)
            save_small(a.out_dir/"process.json",doc)
        except Exception as exc:
            scientific_code=doc["actual_returncode"]
            slim={k:v for k,v in doc.items() if k not in ("complete_strict_propagation_conclusion","complete_endpoint_readout_conclusion")}
            slim["actual_scientific_returncode"]=scientific_code
            slim["formatting_failure"]=dict(type=type(exc).__name__,message=str(exc))
            slim["actual_returncode"]=2
            save_small(a.out_dir/"process.json",slim)
            (a.out_dir/"conclusion.md").write_text("# SP formatting failure\n\n"+json.dumps(slim["formatting_failure"])+"\n")
            doc["actual_returncode"]=2
    print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],actual_returncode=doc["actual_returncode"],
        gates=len(doc["gates"]),old_numerical_enclosures_recomputed=0,
        mathematical_seconds=doc["actual_mathematical_wall_seconds"]),sort_keys=True),flush=True)
    raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
