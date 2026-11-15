#!/usr/bin/env python3
"""Complete two-window strict-cut normalizers and strong remainders.

Only new strict-cut coefficient and band estimates are evaluated. The original
P.22 root gap and every complete physical comparison column are read unchanged.
All finite/high blocks and both independent physical means are retained.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_strict_cut_two_window_normalizers_and_strong_remainders_v1"
CONTRACT="0ffa3261e3bb3fdea2cd05afd489b2e71b5587a2bba9432410c492e2ee64f2aa"
S_CONTRACT="2010d9a15ff5604dcdfd7d1db8f782a5f247806b4b007565073b02c8d4008fac"
N_CONTRACT="4d44bbe7082d4ee967ebf9d02284b3510624624ab98adb087b8d0499eb030376"
IN_CONTRACT="d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75"
RR_SOURCE="2a51b8c45974808e65754ebaa0b476650596e7d8a1e36541e9afd3987146c4c9"
RR_MANIFEST="8822511f1f1c853efd8eec4944bcb74b6954c7fa04c143d9dafc9b470bdd1b4a"
RR_EXECUTION="a75da290077cf0e134834be5e35a0fa7cd55cd79104f5128d87eaee898af162b"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
RCUT=Q(76285779072683,320000000000000)
OLD_NATIVE="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
OLD_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
OLD_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
FORCE_SHA="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47"
FORCE_SOURCE="ba25934f0f6e147f293644edc93b2adf1c33d5935f86596d96355cf063c95fa6"
FORCE_MANIFEST="a7790a87932a22997e29dfa2085982ac7adbbef9fd36512918eec975dd3c5341"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
EXPECTED={"accepted_RR_execution":["43750683671",RR_SOURCE,RR_MANIFEST,RR_EXECUTION,28]}
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"original_complete_norm_rows\":1328,\"original_complete_forcing_rows\":1328,\"original_physical_comparison_run\":\"43750683671/1\",\"physical_frequency\":\"n=4|j|\",\"initial_cutoff_abs_j\":97,\"first_normalizer_bandwidth\":192,\"second_normalizer_bandwidth\":384,\"dyadic_search_first\":512,\"inverse_windows\":[\"L2\",\"H^(-4/3)\"],\"complete_strong_input_window\":\"H^(-4/3), original moving density circle\",\"complete_strong_output_window\":\"L2 density and two independent means\",\"physical_column_input_window\":\"H^(-4/3), both reference columns and both signs |j|>=97\",\"full_true_phase_coordinate_fee_not_yet_composed\":true,\"finite_Schur_inverse_not_claimed\":true,\"full_incoming_inverse_or_return_R0_not_claimed\":true,\"old_successful_scientific_calls_allowed\":0,\"expected_actual_gate_count\":16}")

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
    return selected

def same_cut_inputs(rows,R,gate):
    saved=R["complete_original_cut_identity_conclusion"]
    identities=saved["complete_cut_row_identity"]
    roots=R["complete_root_mean_value_conclusion"]
    physical=R["complete_physical_comparison_conclusion"]
    gate("the accepted physical root and four-column comparison keep the complete P22 family and mean scope",
        saved["exact_strict_cut"]==str(RCUT) and saved["exact_root_interval"]==list(map(str,ROOTS))
        and saved["complete_original_norm_rows"]==saved["complete_original_forcing_rows"]==1328
        and physical["exact_strict_cut"]==str(RCUT)
        and physical["exact_real_delta_radius"]=="1/100000000"
        and physical["input_window"]==PARAMETERS["physical_column_input_window"]
        and physical["output_window"]=="old-circle L2 density pair plus both mean coordinates"
        and physical["all_output_modes_finite_head_and_both_mean_coordinates_retained"] is True
        and physical["both_reference_columns_and_input_signs"] is True
        and physical["nonzero_root_beta_and_all_tau_integral_are_in_immutable_first_receiver"] is True
        and R["complete_strict_physical_Darboux_comparison_paid"] is True
        and R["new_root_mean_value_curvature_gaps"]==saved["complete_cut_sides"]==len(rows)
        and R["new_joint_free_g_products"]==2 and R["new_complete_physical_receivers"]==4*len(rows))
    byid={x["original_norm_row"]:x for x in identities}
    byroot={x["original_norm_row"]:x for x in roots}
    byphys={x["original_norm_row"]:x for x in physical["complete_physical_cut_rows"]}
    newinputs=[];joined=[]
    for index,nr,fr in rows:
        v=byid[index];root=byroot[index];p=byphys[index];c=nr["bounds"]
        if (v["original_saved_norm_row_sha256"]!=payload_sha(nr)
            or v["original_saved_forcing_row_sha256"]!=payload_sha(fr)
            or v["exact_interval"]!=fr["interval"]
            or v["original_root_row"]!=fr["original_root_row"]
            or v["original_common_row"]!=fr["original_common_row"]
            or v["original_intrinsic_interval"]!=fr["original_intrinsic_interval"]
            or root!=p["complete_cut_coefficients"]["root_mean_value_q_bounds"]
            or set(p["complete_four_physical_pieces"])!={"error_density_0","error_density_1","free_R2","free_R3"}):
            raise ValueError("the saved P22 root and physical columns use a different complete original row")
        gap(root["q_lower"],"accepted q lower");up(root["q_upper"])
        if root["exact_root_distance"]!=[str(ROOTS[0]-RCUT),str(ROOTS[1]-RCUT)]:
            raise ValueError("the root inference is not at this strict cut")
        newinputs.append(dict(original_norm_row=index,original_root_row=fr["original_root_row"],
            original_common_row=fr["original_common_row"],exact_interval=fr["interval"],
            original_saved_norm_row_sha256=payload_sha(nr),original_saved_forcing_row_sha256=payload_sha(fr),
            complete_q_bounds_read_verbatim=copy.deepcopy(root),
            original_complete_intrinsic_ordinary_jets_read_verbatim={
                "K":copy.deepcopy(fr["complete_intrinsic_ordinary_jets"]["K"][:3]),
                "beta":copy.deepcopy(fr["complete_intrinsic_ordinary_jets"]["beta"][:2])},
            original_full_actual_eta_derivatives_read_verbatim=copy.deepcopy(fr["full_actual_eta_derivatives"][:2]),
            original_complete_norm_inputs_read_verbatim={
                k:copy.deepcopy(c[k][:2] if k in ("U","V","D") else c[k][:1] if k in ("Ur","Vr") else c[k])
                for k in ("U","V","D","Ur","Vr","eta_lower","eta_upper")}))
        joined.append((index,nr,fr,root))
    gate("each selected original norm and forcing row is identical to the accepted root and all four physical columns",
        len(byid)==len(byroot)==len(byphys)==len(rows)==len(joined)
        and set(byid)==set(byroot)==set(byphys)=={x[0] for x in rows})
    return joined,newinputs,copy.deepcopy(physical),copy.deepcopy(saved)

def absolute(v):
    a=rb(v)
    if not a.is_finite():raise ValueError("a saved complete coefficient is nonfinite")
    return abs(a).upper()

def complete_normalizer_coefficients(nr,fr,root):
    """TN.7--8 at the exact P.22 cut; the accepted root gap is only read."""
    c=nr["bounds"];old=fr["complete_intrinsic_ordinary_jets"]
    qlo=gap(root["q_lower"],"accepted exact P22 q lower")
    qhi=up(root["q_upper"])
    kr,krr=absolute(old["K"][1]),absolute(old["K"][2])
    b,br=absolute(old["beta"][0]),absolute(old["beta"][1])
    em=gap(c["eta_lower"],"saved full eta lower");ep=up(c["eta_upper"])
    er=absolute(fr["full_actual_eta_derivatives"][1])
    u0,u1=(up(c["U"][k]) for k in range(2))
    v0,v1=(up(c["V"][k]) for k in range(2))
    ur,vr=up(c["Ur"][0]),up(c["Vr"][0])
    d0,d1=(up(c["D"][k]) for k in range(2))
    q1=up(kr/(2*qlo))
    q2=up(krr/(2*qlo)+kr*kr/(4*qlo*qlo*qlo))
    W0=up(u0+qhi*v0);Wp=up(u1+qhi*v1)
    Wr=up(ur+qhi*vr+q1*v0)
    amin=gap(em*qlo,"complete characteristic half-gap")
    amax=up(ep*qhi);ar=up(er*qhi+ep*q1)
    B=up(q1/(2*qlo)+b*(1+W0*W0))
    Bp=up(2*b*W0*Wp)
    Br=up(q2/(2*qlo)+q1*q1/(2*qlo*qlo)+br*(1+W0*W0)+2*b*W0*Wr)
    S=up(B/(2*amin));Sp=up(Bp/(2*amin))
    Sr=up(Br/(2*amin)+B*ar/(2*amin*amin))
    E=up(Bp+b*Wp*W0+(d0+amax)*Sp+Sr+S*d1)
    S2=up(E/(2*amin))
    out=dict(q_r_absolute_upper=q1,q_rr_absolute_upper=q2,
        full_wave_value_upper=W0,full_wave_phi_upper=Wp,full_wave_radial_upper=Wr,
        characteristic_half_gap_lower=amin,characteristic_speed_upper=amax,
        characteristic_speed_radial_upper=ar,complete_B_upper=B,
        complete_B_phi_upper=Bp,complete_B_radial_upper=Br,
        complete_S_upper=S,complete_S_phi_upper=Sp,complete_S_radial_upper=Sr,
        complete_E_upper=E,complete_S2_upper=S2)
    return out

def compressed_multiplier(bound,band,t,J):
    """The input and output projections are in the same moving angle."""
    bound=up(bound);t=Q(t)
    if t==0:return bound
    return up((1+ex(Q(band,J)))**ex(abs(t))*arb(2*band+1).sqrt()*bound)

def two_window_tests(S,S2,J):
    values={}
    for label,t in (("L2",Q(0)),("Hminus4_3",Q(-4,3))):
        m1=compressed_multiplier(S,192,t,J)
        m2=compressed_multiplier(S2,384,t,J)
        tau1=up(m1/(4*J));tau2=up(m2/((4*J)**2))
        margin1=(1-tau1).lower();margin2=(1-tau2).lower()
        passed=bool(margin1>0 and margin2>0)
        entry=dict(first_multiplier_upper=rec(m1),second_multiplier_upper=rec(m2),
            first_tau=rec(tau1),second_tau=rec(tau2),
            first_margin_lower=rec(margin1),second_margin_lower=rec(margin2),
            both_strict_tests_passed=passed)
        if passed:
            entry.update(first_inverse_upper=rec(up(1/margin1)),
                second_inverse_upper=rec(up(1/margin2)),
                ordered_inverse_upper=rec(up(1/(margin2*margin1))),
                complete_forward_upper=rec(up((1+tau1)*(1+tau2))))
        values[label]=entry
    return values

def choose_complete_normalizer(S,S2):
    """Choose one exact cutoff for both windows, retaining the cutoff97 verdict."""
    S=up(S);S2=up(S2)
    initial=two_window_tests(S,S2,97)
    passed=all(x["both_strict_tests_passed"] for x in initial.values())
    construction=None
    if passed:J=97;windows=copy.deepcopy(initial)
    else:
        A1=up(arb(385).sqrt()*S);A2=up(arb(769).sqrt()*S2)
        need1=up(4*A1);need2=up(4*A2);J=512
        while not (arb(J)>=need1 and arb(J*J)>=need2):J*=2
        windows=two_window_tests(S,S2,J)
        construction=dict(first_dyadic_at_least_384=512,
            complete_A1_upper=rec(A1),complete_A2_upper=rec(A2),
            verified_J_ge_4A1=bool(arb(J)>=need1),
            verified_J_squared_ge_4A2=bool(arb(J*J)>=need2))
    if not all(x["both_strict_tests_passed"] for x in windows.values()):
        raise ValueError("the selected common-cutoff normalizer failed a required strict window")
    return J,initial,windows,construction

def complete_strong_normalizer(S,S2,J,windows):
    """TN.17--23: the inverse order and every intermediate Sobolev space."""
    lam=up((1+arb(16)*J*J).sqrt());gamma=up(lam/(4*J))
    mSneg=compressed_multiplier(S,192,Q(-1,3),J)
    mSpos=compressed_multiplier(S,192,Q(2,3),J)
    m2pos=compressed_multiplier(S2,384,Q(2,3),J)
    two_gain=up(lam**ex(Q(4,3))/((4*J)**2))
    # gamma_J^2 Lambda_J^(-2/3) = Lambda_J^(4/3)/(4J)^2;
    # this positive-power form keeps an upper Lambda endpoint directed upward.
    A2strong=up(two_gain*mSneg*mSpos)
    Bstrong=up(two_gain*m2pos)
    leftB=up(windows["L2"]["second_inverse_upper"])
    rightA=up(windows["Hminus4_3"]["first_inverse_upper"])
    inverse_remainder=up((A2strong+leftB*Bstrong)*rightA)
    forward_remainder=up((1+up(windows["L2"]["first_tau"]))*Bstrong)
    finite_lambda=up((1+arb(16)*(J+191)*(J+191)).sqrt())
    CI=up(arb(17).sqrt()/4)
    finite=up(2*CI*up(S)*finite_lambda**ex(Q(1,3)))
    out=dict(complete_high_primitive_gain_upper=rec(gamma),
        complete_S_Hminus1_3_multiplier_upper=rec(mSneg),
        complete_S_H2_3_multiplier_upper=rec(mSpos),
        complete_S2_H2_3_multiplier_upper=rec(m2pos),
        complete_two_gain_and_high_embedding_upper=rec(two_gain),
        complete_A_squared_Hminus4_3_to_L2_upper=rec(A2strong),
        complete_B_Hminus4_3_to_L2_upper=rec(Bstrong),
        complete_ordered_inverse_strong_remainder_upper=rec(inverse_remainder),
        complete_forward_strong_remainder_upper=rec(forward_remainder),
        complete_uncompressed_first_symbol_finite_difference_upper=rec(finite),
        exact_finite_input_and_output_max_abs_j=J+191,
        inverse_remainder_has_high_input_and_high_output=True,
        finite_difference_output_mean_retained=True,
        all_two_original_physical_mean_coordinates_retained=True,
        first_symbol_sign_in_inverse="minus S I",
        ordered_inverse_identity="(I+B)^(-1)(I+A)^(-1)",
        strong_input_window="H^(-4/3) in the original moving density circle",
        strong_output_window="L2 density; both independent means retained",
        no_phase_projection_identification=True,no_finite_schur_inverse_claimed=True)
    return out

def normalized_physical_columns(saved,J,windows):
    """Read a complete RR same-side sum; apply the new L2 inverse only once."""
    gain=up(windows["L2"]["ordered_inverse_upper"])
    rows=[]
    for old in saved["complete_physical_cut_rows"]:
        pieces={name:rec(up(gain*up(v["complete_old_circle_density_and_two_means_upper"])))
            for name,v in old["complete_four_physical_pieces"].items()}
        rows.append(dict(original_norm_row=old["original_norm_row"],
            saved_complete_same_case_sum_read_verbatim=copy.deepcopy(old["complete_four_piece_sum_upper"]),
            complete_normalized_four_pieces_upper=pieces,
            complete_normalized_same_case_sum_upper=rec(up(gain*up(old["complete_four_piece_sum_upper"])))))
    total=max(up(r["complete_normalized_same_case_sum_upper"]) for r in rows).upper()
    return dict(exact_cutoff_abs_j=J,complete_cut_sides=len(rows),
        saved_complete_physical_conclusion_read_verbatim=copy.deepcopy(saved),
        complete_ordered_L2_inverse_upper=rec(gain),
        complete_normalized_cut_rows=rows,
        complete_normalized_physical_Darboux_comparison_upper=rec(total),
        selection_rule="maximum of complete same-side four-piece sums",
        phase_circle_and_full_incoming_not_yet_composed=True,
        finite_ports_97_through_J_minus_1_retained=True)

def render_conclusion(doc):
    out={k:doc[k] for k in ("kind","complete","proved","actual_returncode","failure",
        "source_sha256","input_manifest_sha256","runtime","arithmetic_bits","run_id","run_attempt",
        "actual_mathematical_wall_seconds") if k in doc}
    out["passed_gates"]=sum(g["passed"] for g in doc["gates"])
    out["recorded_gates"]=len(doc["gates"]);out["expected_gates"]=16
    for k in ("complete_selected_normalizer_conclusion","complete_strong_remainder_conclusion","scope"):
        if k in doc:out[k]=doc[k]
    if "complete_normalized_physical_conclusion" in doc:
        p=doc["complete_normalized_physical_conclusion"]
        out["complete_normalized_physical_comparison_upper"]=p["complete_normalized_physical_Darboux_comparison_upper"]
        out["complete_normalized_four_piece_rows"]=[
            {k:r[k] for k in ("original_norm_row","complete_normalized_four_pieces_upper","complete_normalized_same_case_sum_upper")}
            for r in p["complete_normalized_cut_rows"]]
    return "\n".join(["# Complete strict-cut two-window normalizers","",
        "All constants refer to the same original P22 moving-angle cut.",
        "The finite complement and both means remain; the true phase and complete incoming inverse are separate.","",
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
        original_complete_norm_rows_read=0,original_complete_forcing_rows_read=0,
        original_cut_sides_read=0,saved_complete_root_gap_rows_read=0,saved_complete_physical_columns_read=0,
        new_complete_normalizer_coefficient_rows=0,new_initial_cutoff_window_tests=0,
        new_selected_cutoff_window_tests=0,new_complete_strong_remainder_conclusions=0,
        new_complete_normalized_physical_columns=0,new_complete_normalized_physical_sums=0,
        old_numerical_enclosures_recomputed=0,old_root_gap_or_physical_receivers_recomputed=0,
        old_profiles_or_amplitudes_or_sources_recomputed=0,old_intrinsic_or_mean_fields_recomputed=0,
        old_scientific_producer_calls=0,original_natural_stage_bytes_modified=False,
        complete_same_cut_two_window_normalizers_paid=False,full_incoming_inverse_claimed=False,
        true_phase_coordinate_fee_composed=False,finite_Schur_inverse_claimed=False,
        full_return_R0_claimed=False,temporary_native_is_not_published=True,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    def checkpoint():save(a.process,doc)
    def gate(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual two-window normalizer gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the immutable manifest fixes the same cut contract runtime and both complete inverse windows",
            manifest["source_sha256"]==sha(__file__) and manifest["contract_sha256"]==CONTRACT
            and manifest["runtime"]==RUNTIME and manifest["mathematical_parameters"]==PARAMETERS
            and manifest["expected_actual_gate_count"]==16
            and len({e["path"] for e in manifest["files"]})==len(manifest["files"]))
        for e in manifest["files"]:
            q=a.repo_root/e["path"]
            if not q.is_file() or q.stat().st_size!=e["bytes"] or sha(q)!=e["sha256"]:
                raise ValueError("immutable complete input changed: "+e["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        gate("all original definitions and complete scalar receipts are immutable and no old module is imported",
            set(EXPECTED)<=set(paths) and sha(paths["contract"])==CONTRACT
            and sha(paths["S_contract"])==S_CONTRACT and sha(paths["N_contract"])==N_CONTRACT
            and sha(paths["IN_contract"])==IN_CONTRACT and sha(paths["accepted_RR_source"])==RR_SOURCE
            and sha(paths["accepted_RR_manifest"])==RR_MANIFEST
            and manifest["old_successful_scientific_calls_allowed"]==0
            and manifest["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
        R=accepted(paths["accepted_RR_execution"],EXPECTED["accepted_RR_execution"],gate)
        doc["original_successful_small_receipts_read"]=1
        rows=read_cut_rows(paths,gate)
        doc["original_complete_norm_rows_read"]=doc["original_complete_forcing_rows_read"]=1328
        joined,inputs,physical,identity=same_cut_inputs(rows,R,gate)
        doc["complete_original_cut_identity_read_verbatim"]=identity
        doc["complete_original_cut_input_conclusion"]=inputs
        doc["saved_complete_root_gap_rows_read"]=doc["original_cut_sides_read"]=len(rows)
        doc["saved_complete_physical_columns_read"]=4*len(rows)
        checkpoint()
        coeff=[];public=[]
        for index,nr,fr,root in joined:
            c=complete_normalizer_coefficients(nr,fr,root);coeff.append(c)
            public.append(dict(original_norm_row=index,complete_coefficients=encode(c)))
        doc["complete_normalizer_coefficient_conclusion"]=public
        doc["new_complete_normalizer_coefficient_rows"]=len(rows)
        checkpoint()
        gate("all new strict-cut coefficient bounds keep full radial derivatives and both physical mean qualifications",
            len(coeff)==len(rows) and all(all(v.is_finite() and v>=0 for v in c.values())
                and c["characteristic_half_gap_lower"]>0 for c in coeff))
        S=max(c["complete_S_upper"] for c in coeff).upper()
        S2=max(c["complete_S2_upper"] for c in coeff).upper()
        J,initial,windows,construction=choose_complete_normalizer(S,S2)
        doc["new_initial_cutoff_window_tests"]=doc["new_selected_cutoff_window_tests"]=2
        gate("the cutoff97 verdict is complete in both windows and no failed sufficient test is called singular",
            set(initial)=={"L2","Hminus4_3"}
            and all(type(v["both_strict_tests_passed"]) is bool for v in initial.values()))
        gate("one exact moving-angle cutoff satisfies both ordered inverse tests in both Sobolev windows",
            type(J) is int and J>=97 and set(windows)=={"L2","Hminus4_3"}
            and all(v["both_strict_tests_passed"] is True
                and gap(v["first_margin_lower"],"first selected margin")>0
                and gap(v["second_margin_lower"],"second selected margin")>0 for v in windows.values()))
        gate("a changed cutoff uses the complete dyadic threshold and retains its enlarged finite complement",
            (J==97 and construction is None and all(v["both_strict_tests_passed"] for v in initial.values()))
            or (J>=512 and J&(J-1)==0 and construction is not None
                and construction["verified_J_ge_4A1"] is True
                and construction["verified_J_squared_ge_4A2"] is True))
        selected=dict(exact_cutoff_abs_j=J,exact_physical_minimum_high_frequency=4*J,
            complete_S_upper=rec(S),complete_S2_upper=rec(S2),
            complete_initial_cutoff97_window_verdicts=initial,
            complete_selected_cutoff_window_verdicts=windows,
            complete_dyadic_construction=construction,
            same_inverse_on_common_trigonometric_domain=True,
            selected_cutoff_in_original_moving_circle=True,
            first_bandwidth=192,second_bandwidth=384,
            finite_modes_97_through_J_minus_1_retained=True,
            all_HL_LH_blocks_and_both_independent_means_retained=True,
            no_failed_test_interpreted_as_operator_noninvertibility=True)
        doc["complete_selected_normalizer_conclusion"]=selected;checkpoint()
        strong=complete_strong_normalizer(S,S2,J,windows)
        doc["complete_strong_remainder_conclusion"]=strong
        doc["new_complete_strong_remainder_conclusions"]=1
        checkpoint()
        strongkeys=("complete_A_squared_Hminus4_3_to_L2_upper",
            "complete_B_Hminus4_3_to_L2_upper","complete_ordered_inverse_strong_remainder_upper",
            "complete_forward_strong_remainder_upper")
        gate("the ordered inverse and forward strong remainders pay every intermediate Sobolev window",
            all(up(strong[k]).is_finite() for k in strongkeys)
            and strong["ordered_inverse_identity"]=="(I+B)^(-1)(I+A)^(-1)"
            and strong["inverse_remainder_has_high_input_and_high_output"] is True)
        gate("the complete finite first-symbol difference keeps its input and output support including the mean",
            strong["exact_finite_input_and_output_max_abs_j"]==J+191
            and up(strong["complete_uncompressed_first_symbol_finite_difference_upper"]).is_finite()
            and strong["finite_difference_output_mean_retained"] is True
            and strong["all_two_original_physical_mean_coordinates_retained"] is True)
        normalized=normalized_physical_columns(physical,J,windows)
        doc["complete_normalized_physical_conclusion"]=normalized
        doc["new_complete_normalized_physical_columns"]=4*len(rows)
        doc["new_complete_normalized_physical_sums"]=len(rows)
        checkpoint()
        gate("all four accepted physical columns and each original same-side sum are retained before one L2 inverse multiplication",
            normalized["saved_complete_physical_conclusion_read_verbatim"]==R["complete_physical_comparison_conclusion"]
            and normalized["complete_cut_sides"]==len(rows)
            and all(set(v["complete_normalized_four_pieces_upper"])=={"error_density_0","error_density_1","free_R2","free_R3"}
                and all(up(x).is_finite() for x in v["complete_normalized_four_pieces_upper"].values())
                and up(v["complete_normalized_same_case_sum_upper"]).is_finite()
                for v in normalized["complete_normalized_cut_rows"]))
        doc["scope"]=dict(same_exact_P22_cut=True,full_real_delta_family=True,
            original_moving_angle_projection_not_renamed_phase_projection=True,
            complete_radial_derivatives_retained=True,all_two_physical_means_retained=True,
            all_finite_high_and_high_finite_blocks_retained=True,
            old_full_q_and_four_physical_columns_read_verbatim=True,
            complete_same_inverse_on_L2_and_Hminus4_3=True,
            first_symbol_minus_SI_plus_complete_finite_difference=True,
            complete_strong_remainder_in_moving_density_coordinates=True,
            normalized_physical_error_not_identified_with_whole_incoming_error=True,
            true_phase_coordinate_and_finite_dual_row_fees_still_separate=True,
            strict_interval_flow_not_inferred_from_one_cut=True,
            actual_full_incoming_or_stable_or_finite_Schur_inverse_not_claimed=True,
            complete_return_R0_not_claimed=True)
        zeros=("old_numerical_enclosures_recomputed","old_root_gap_or_physical_receivers_recomputed",
            "old_profiles_or_amplitudes_or_sources_recomputed","old_intrinsic_or_mean_fields_recomputed",
            "old_scientific_producer_calls")
        gate("the new cut normalizers and complete physical columns are paid without repeating any successful producer",
            doc["original_successful_small_receipts_read"]==1
            and doc["saved_complete_root_gap_rows_read"]==len(rows)
            and doc["saved_complete_physical_columns_read"]==4*len(rows)
            and doc["new_complete_normalizer_coefficient_rows"]==len(rows)
            and doc["new_complete_normalized_physical_columns"]==4*len(rows)
            and all(doc[k]==0 for k in zeros))
        if len(doc["gates"])!=PARAMETERS["expected_actual_gate_count"]:
            raise ValueError("the complete scientific gate count differs from the frozen contract")
        doc["complete"]=doc["proved"]=doc["complete_same_cut_two_window_normalizers_paid"]=True
        doc["actual_returncode"]=0
    except Exception as e:
        doc["failure"]=dict(type=type(e).__name__,message=str(e))
        print("ACTUAL_TWO_WINDOW_NORMALIZER_FAILURE",repr(e),flush=True)
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        checkpoint()
        save(a.out,dict(scientific_receipt=doc,no_old_scientific_reexecution=True),compressed=True)
        doc["temporary_native_sha256"]=sha(a.out);doc["temporary_native_bytes"]=a.out.stat().st_size
        checkpoint()
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        t=a.conclusion.with_name(a.conclusion.name+".tmp")
        t.write_text(render_conclusion(doc),encoding="utf-8");t.replace(a.conclusion)
    raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
