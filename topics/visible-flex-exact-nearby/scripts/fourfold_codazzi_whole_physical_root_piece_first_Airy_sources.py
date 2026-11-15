#!/usr/bin/env python3
"""Complete first-Airy sources on the original physical root piece.

Only new scalar radius budgets, complete Airy operators and radial integrals
are evaluated. Accepted Fourier norms, signed coefficients, old-circle words,
matrix conversions and exterior source rows are immutable inputs.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,ctx
import fourfold_codazzi_strict_exterior_first_Airy_complete_sources as full
import fourfold_codazzi_correlated_first_Airy_local_numerator as numerator

inner=full.inner
PUBLIC="Rogerhu12/math-research-public"
TAYLOR="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
TPROC="42ab23b97ce922b042b8291af46cfe8c44ffd7e90ba1e2a6049caef263b7224e"
TSOURCE="42048094f7c5e0ba3b83f10e9e6fcbc5cd4c5b3d67057f69241409a5a4be87a1"
TMANIFEST="5700ded5038d500d14f43dfa69994665d2688f220de155128fff1fec6286e3a5"
NRAW="fbe1bce690f33335d2b024fe38a751743e0017e7d275b4d1fb0712be155f177e"
NPROC="6396a554ab8401d709744b47315ab73830dfe2051937a980ecaab0efa8fc82db"
NSOURCE="e9024812c2f87fe18cb43fcdd5661b6063cc7e5cf5ba4380af5b8a5d50e605fe"
NMANIFEST="bc34acdc1738a92bf71d9ce6c8be2dddfced3ae1de0ca884a1025c45419256d1"
BSTAR="2a387a9d1f478eba4c469ceec2d7b01a8f6ed619f458e465f36067fa280876df"
BPROC="a7c42cca5dc3490462749cca4dbe5e1202aed0dd9e39570c0ec98dff7f668b5f"
BSOURCE="314c092b8f7042938e40242105eed5b3b7ab504e0d25f2985f08f16fcdee6c32"
BMANIFEST="bd17d3779659133139003b0a79934c0e7768c4422898ac7163b4705d850c99c6"
AUX=inner.AUX
APROC=inner.APROC
MOMENT=inner.NORM
CONVERSIONS="a2b11b2773ce693f45e6fbbdb50b71236e9feafff520ee396d547efa8c7643ed"
CSOURCE="d4ea7d15874d602a833cf23c3ff48739974e41f2ca922a62da7ca2563ee9f768"
CMANIFEST="6456b7fb5a3313b38f73e6e97116b023804778ee88cce5fec20f6a5f9dc17cba"
ISOURCE="0b0dc7b3b5c747dd8935f77c75554c60f2b08fd40a6cf5dd27c7c81f5c945fbf"
CONTRACT="d6369980d02cb9b998082d5b9e80a055abd54fdfe20eb09f26c4e97b0af57d33"
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
GERM=(Q(8556839292003943,36028797018963968),Q(8636031980136455,36028797018963968))
BODY=Q(1192029371497,5000000000000)
RHO=Q(1,6000)
SIGMA=Q(1,128)
WIDTHS=(Q(0),Q(1,512))
DELTA=Q(1,10**8)
RADII=full.RADII
CUTOFF=97
TERM_NAMES=full.TERM_NAMES
MEAN_NAMES=("direct_u_h","complete_uJ_gd","complete_uJL_h","complete_uJB_w",
            "complete_curvature_v_nonmean_w")
sha=inner.sha
payload_sha=inner.payload_sha
read=inner.read
save=full.save
ex=inner.ex
box=inner.box
up=inner.up
record=inner.record
encode=inner.encode
decode=inner.decode
ipow=inner.ipow
ensure_nonnegative=inner.ensure_nonnegative

def receipt(path,base):
    return dict(file=str(path.relative_to(base)),bytes=path.stat().st_size,sha256=sha(path))

def recover_prefix_receipts(previous,base,original_cases,expected):
    """Reconcile only complete atomic files with a lagging metadata index.

    This is byte and payload validation, not interval arithmetic. Original
    index bytes remain untouched. A partial original-envelope row is not
    admitted through a stale receipt. Complete root rows must equal their
    independently accepted immutable scalar stage exactly.
    """
    base=Path(base)
    def load_file(path):
        raw=Path(path).read_bytes()
        return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)
    def rec(path):
        return dict(file=str(path.relative_to(base)),bytes=path.stat().st_size,sha256=sha(path))
    def digest(v):
        return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
    stages=copy.deepcopy(previous.get("stages",{}));cases=copy.deepcopy(previous.get("case_stages",[]))
    audit=[];payloads={}
    allowed={"profile_stages","radius_budget_stages","complete_source_rows",
             "piece_summary_stages","case_summary_stages"}
    for path in sorted((base/"stages").glob("*.json.gz")):
        value=load_file(path);name=value.get("stage")
        if not (isinstance(name,str) and path.name==name+".json.gz" and value.get("complete") is True
            and value.get("source_sha256")==expected["source_sha256"]
            and value.get("input_manifest_sha256")==expected["input_manifest_sha256"]
            and value.get("runtime")==expected["runtime"] and value.get("stage_kind") in allowed
            and value.get("original_Taylor_native_sha256")==expected["original_Taylor_native_sha256"]
            and value.get("original_Nraw_native_sha256")==expected["original_Nraw_native_sha256"]):
            raise ValueError("an unindexed natural stage changed complete scientific identity")
        current=rec(path)
        if name in stages:
            old=stages[name]
            if any(old[k]!=current[k] for k in ("file","bytes","sha256")):
                raise ValueError("an immutable accepted scalar stage changed bytes")
        else:
            stages[name]=dict(**current,stage_kind=value["stage_kind"])
            audit.append(dict(kind="complete_scalar_file_before_index",stage=name,receipt=current))
        payloads[name]=value["payload"]
    for name,entry in stages.items():
        if name not in payloads:raise ValueError("a previously accepted immutable scalar stage is missing")
    for ci,source in enumerate(original_cases):
        original=source["document"];radius=original["exact_radius"]
        tag=radius.replace("/","-")
        path=base/"cases"/("radius-"+tag+".json.gz")
        if not path.is_file():
            if ci<len(cases):raise ValueError("an accepted complete case file is missing")
            break
        if ci>len(cases):raise ValueError("an unindexed case skipped an earlier complete prefix")
        value=load_file(path);current=rec(path)
        indexed=ci<len(cases)
        stale=not indexed or any(cases[ci][k]!=current[k] for k in ("file","bytes","sha256"))
        if not (value.get("source_sha256")==expected["source_sha256"]
            and value.get("input_manifest_sha256")==expected["input_manifest_sha256"]
            and value.get("runtime")==expected["runtime"]
            and value.get("original_complete_case_sha256")==source["sha256"]
            and value.get("exact_radius")==radius and value.get("exact_cover")==original["exact_cover"]):
            raise ValueError("an advanced case snapshot changed complete scientific identity")
        rows=value.get("rows",[]);roles=value.get("row_roles",[])
        if len(rows)!=len(roles):raise ValueError("an advanced source-row ledger is incomplete")
        if indexed and len(rows)<cases[ci].get("accepted_rows",0):
            raise ValueError("an advanced snapshot shortened an accepted source prefix")
        for row,role in zip(rows,roles):
            if row["interval"]!=role["interval"] or row["side"]!=role["side"]:
                raise ValueError("an advanced row changed its physical interval or side")
            kind=role["kind"]
            if kind in ("copied_original","partial_original"):
                oi=role["original_serial"]
                if not isinstance(oi,int) or not 0<=oi<len(original["rows"]):
                    raise ValueError("an advanced row names no original source row")
                old=original["rows"][oi]
                if role["original_row_payload_sha256"]!=digest(old):
                    raise ValueError("an advanced row changed its original complete source identity")
                if kind=="copied_original":
                    if row!=old:raise ValueError("an advanced unchanged row is not an exact original payload")
                elif stale:
                    raise ValueError("a partial-envelope row cannot inherit an unindexed numerical result")
            elif kind=="new_complete_root_piece":
                name=role["stage"]
                if name not in payloads or stages[name]["stage_kind"]!="complete_source_rows":
                    raise ValueError("an advanced root-piece row lacks its accepted scalar stage")
                if row!=payloads[name] or role["row_payload_sha256"]!=digest(row):
                    raise ValueError("an advanced root-piece row differs from its accepted full source stage")
            else:raise ValueError("an advanced case has an unknown source-row role")
        if value.get("complete"):
            name="complete-recombined-case-summary-"+str(ci)
            if name not in payloads or stages[name]["stage_kind"]!="case_summary_stages":
                raise ValueError("a complete advanced case lacks its accepted independent summary stage")
            if value.get("complete_case_summary")!=payloads[name]:
                raise ValueError("an advanced complete summary changed its accepted interval result")
        new=dict(**current,accepted_rows=len(rows),complete=bool(value.get("complete")))
        if stale:
            audit.append(dict(kind="atomic_case_snapshot_before_index",case=ci,
                original_index_receipt=cases[ci] if indexed else None,reconciled_receipt=new,
                original_case_sha256=source["sha256"],all_complete_row_payloads_verified=True))
        if indexed:cases[ci]=new
        else:cases.append(new)
    return stages,cases,audit

def case_receipt(path,base,value):
    return dict(**receipt(path,base),accepted_rows=len(value["rows"]),complete=bool(value["complete"]))

def checked_file(path,entry):
    path=Path(path)
    if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
        raise ValueError("an immutable whole-piece input or prefix changed: "+str(path))
    return read(path)

def success(native,process,path,source,manifest,native_hash,count):
    return (sha(path)==process["native_sha256"]==native_hash
        and native["source_sha256"]==process["mathematical_source_sha256"]==source
        and native["input_manifest_sha256"]==manifest
        and native["complete"] and native["proved"] and native["failure"] is None
        and process["complete"] and process["actual_returncode"]==0
        and process["mathematical_complete"] and process["mathematical_failure"] is None
        and native["gates"]==process["mathematical_gates"]
        and len(native["gates"])==count and all(g["passed"] for g in native["gates"]))

def width_row(rows,width):
    found=[v for v in rows if Q(v["exact_output_phi_width"])==width]
    if len(found)!=1:raise ValueError("an original complete angular width is missing or duplicated")
    return found[0]

def amplitude_tail(t,p):
    d=1-t
    if not (t>=0 and d>0):raise ValueError("the complete radial amplitude tail lost its positive gap")
    if p==0:return ipow(t,13)/d
    if p==1:return 13*ipow(t,12)/d+ipow(t,13)/ipow(d,2)
    if p==2:return 156*ipow(t,11)/d+26*ipow(t,12)/ipow(d,2)+2*ipow(t,13)/ipow(d,3)
    raise ValueError("an unproved radial amplitude derivative was requested")

def radius_budget(h,tnorm,nnorm,tbudgets,nbudgets,multipliers,amplitudes):
    """The complete original finite norms are only multiplied by new radii."""
    if not Q(0)<h<RHO:raise ValueError("a physical subinterval leaves the original product disk")
    hr=ex(h);R=ex(RHO);t=hr/R;d=1-t;m=11
    radial=dict(t=t,U=(m+1)*(m+2)*ipow(t,m)/d
        +2*(m+2)*ipow(t,m+1)/ipow(d,2)+2*ipow(t,m+2)/ipow(d,3),
        V0=(m+1)*ipow(t,m)/d+ipow(t,m+1)/ipow(d,2))
    radial["V1"]=radial["U"]/2
    result=[]
    for width in WIDTHS:
        tag=str(width);delta=ex(SIGMA-width)
        original_t=width_row(tbudgets,width);original_n=width_row(nbudgets,width)
        sums=decode(original_t["complete_geometric_Fourier_sums"])
        angular=decode(original_n["complete_angular_factors"])
        if not (len(sums)==4 and angular["delta"].contains(delta)):
            raise ValueError("a saved complete angular factor changed its exact loss")
        tables={}
        for name,key in (("a1","a"),("b1","b")):
            sup={};wiener={};parts={}
            for p in range(3):
                for q in range(4):
                    finite=sum((math.factorial(n)//math.factorial(n-p)
                        *up(box(tnorm[tag][n][name][q]))*ipow(hr,n-p)
                        for n in range(p,13)),arb(0)).upper()
                    common=amplitudes[key]*amplitude_tail(t,p)/ipow(R,p)
                    st=(common*math.factorial(q)/ipow(delta,q)).upper()
                    wt=(common*sums[q]).upper()
                    k=str(p)+","+str(q)
                    sup[k]=(finite+st).upper();wiener[k]=(finite+wt).upper()
                    parts[k]=dict(complete_original_finite_norm_sum=finite,
                        complete_strip_sup_tail=st,complete_Wiener_tail=wt)
            tables[name]=dict(strip_sup=sup,Wiener=wiener,parts=parts)
        nvalues={space:{k:{} for k in ("a","b")} for space in ("strip_sup","Wiener")}
        nparts=copy.deepcopy(nvalues)
        for q in range(3):
            finite={k:sum((up(box(nnorm[tag][n]["Nraw_"+k][q]))*ipow(hr,n)
                for n in range(11)),arb(0)).upper() for k in ("a","b")}
            for space in ("strip_sup","Wiener"):
                tails=numerator.complete_remainder(q,space,radial,multipliers,amplitudes,angular)
                for k in ("a","b"):
                    tail=up(tails[k]["complete_tail"])
                    nvalues[space][k][str(q)]=(finite[k]+tail).upper()
                    nparts[space][k][str(q)]=dict(complete_original_correlated_finite_norm_sum=finite[k],
                        complete_full_tail=tail,complete_tail_terms=tails[k])
        if not ensure_nonnegative([tables,nvalues,nparts]):
            raise ValueError("a complete physical-piece radius budget is not finite nonnegative")
        result.append(dict(exact_output_phi_width=str(width),exact_rho_cover=str(h),
            first_amplitude_budgets=encode(tables),complete_Nraw_derivative_budgets=encode(nvalues),
            complete_Nraw_finite_and_tail_parts=encode(nparts),
            original_amplitude_budget_payload_sha256=payload_sha(original_t),
            original_Nraw_budget_payload_sha256=payload_sha(original_n),
            all_saved_finite_norms_and_complete_angular_factors_reused=True,
            old_first_correction_or_numerator_coefficients_recomputed=False))
    return dict(exact_physical_rho_cover=str(h),exact_holomorphic_rho_radius=str(RHO),
        exact_holomorphic_phi_width=str(SIGMA),complete_radial_numerator_tails=encode(radial),
        budgets=result,complete=True)

def source_row(piece,common,conversion,budget,profile):
    real=decode(common["bounds"]);p=decode(profile["numeric"])
    c=p["c"];PQ=p["PQ"]
    rv=dict(U=[real["U"]],V=[real["V"]],D=real["D"],em=real["eta_lower"])
    rbudget=width_row(budget["budgets"],Q(0))
    abudget=width_row(budget["budgets"],Q(1,512))
    rjets=inner.amplitude_jets(rbudget,rv,PQ)
    ajets=inner.amplitude_jets(abudget,c,PQ)
    side=piece["side"]
    operators={k:inner.Airy_bound(rjets[k],ajets[k][0],p,side) for k in rjets}
    rn=decode(rbudget["complete_Nraw_derivative_budgets"])["strip_sup"]
    an=decode(abudget["complete_Nraw_derivative_budgets"])["strip_sup"]
    localjets=[[rn[k][str(q)] for k in ("a","b")] for q in range(3)]
    localvalue=[an[k]["0"] for k in ("a","b")]
    localop=inner.Airy_bound(localjets,localvalue,p,side)
    local=record((real["C_J_scalar"]*up(box(localop["bound"]))).upper())
    z=decode(conversion["matrix_conversion"]["costs"])
    bounds=full.nonlocal_constants(real,z,operators,local)
    a,b=map(Q,piece["interval"]);weight=inner.radial_weight(a,b,ROOTS,side)
    if not weight>0:raise ValueError("a retained physical source interval has no positive radial weight")
    sq=(weight*up(box(bounds["complete_squared_vector_envelope"]))).upper()
    separated={k:record((weight*ipow(up(box(bounds[n])),2)).upper()) for k,n in (
        ("first_nonlocal","first_nonlocal_singular_envelope"),
        ("independent_even_mean","independent_even_mean_singular_envelope"),
        ("original_first_local","original_first_local_singular_envelope"))}
    return dict(common_row=common["common_row"],interval=piece["interval"],
        original_root_row=common["original_root_row"],original_piece=2549,side=side,
        radial_weight_integral=record(weight),complete_amplitude_operator_evidence=operators,
        correlated_local_numerator_operator_evidence=localop,source_bounds=bounds,
        separate_squared_source_integrals=separated,complete_squared_source_integral=record(sq),
        exact_rho_cover=budget["exact_physical_rho_cover"],
        original_moment_row_payload_sha256=payload_sha(common),
        original_same_order_conversion_payload_sha256=payload_sha(conversion),
        complete_radius_budget_payload_sha256=payload_sha(budget),
        complete_whole_piece_profile_payload_sha256=payload_sha(profile),
        uncertain_root_one_sided_charge=piece["uncertain_root_band"],
        actual_local_source_is_JP_S_of_unnormalized_Nraw=True,
        complete_nine_nonlocal_and_five_independent_mean_terms_retained=True,
        new_physical_field_or_artificial_interface_source_introduced=False)

def restrict_original(row,left,right):
    """Restrict a complete old envelope; never subtract an old upper integral."""
    a,b=map(Q,row["interval"])
    if not a<=left<right<=b:raise ValueError("an old source restriction leaves its exact interval")
    weight=inner.radial_weight(left,right,ROOTS,row["side"])
    bounds=row["source_bounds"];result=copy.deepcopy(row)
    result["interval"]=[str(left),str(right)]
    result["radial_weight_integral"]=record(weight)
    result["complete_squared_source_integral"]=record(min(
        (weight*up(box(bounds["complete_squared_vector_envelope"]))).upper(),
        up(box(row["complete_squared_source_integral"]))).upper())
    for k,name in (("first_nonlocal","first_nonlocal_singular_envelope"),
        ("independent_even_mean","independent_even_mean_singular_envelope"),
        ("original_first_local","original_first_local_singular_envelope")):
        new=(weight*ipow(up(box(bounds[name])),2)).upper()
        result["separate_squared_source_integrals"][k]=record(min(
            new,up(box(row["separate_squared_source_integrals"][k]))).upper())
    result["original_unrestricted_row_payload_sha256"]=payload_sha(row)
    result["partial_restriction_uses_same_complete_old_envelope"]=True
    result["no_subtraction_of_an_old_upper_bound"]=True
    return result

def interval_cover(rows,left,right):
    intervals=sorted(tuple(map(Q,r["interval"])) for r in rows)
    return bool(intervals and intervals[0][0]==left and intervals[-1][1]==right
        and all(a<b for a,b in intervals)
        and all(intervals[j][1]==intervals[j+1][0] for j in range(len(intervals)-1)))

def channel_sum(rows):
    sq=sum((up(box(v["complete_squared_source_integral"])) for v in rows),arb(0)).upper()
    components={k:record(sum((up(box(v["separate_squared_source_integrals"][k]))
        for v in rows),arb(0)).upper().sqrt().upper()) for k in
        ("first_nonlocal","independent_even_mean","original_first_local")}
    terms={}
    for name in TERM_NAMES:
        value=sum((up(box(v["radial_weight_integral"]))*ipow(
            up(box(v["source_bounds"]["final_old_J_Hminus5over3_to_Hminus2over3"]))*
            up(box(v["source_bounds"]["complete_nine_nonlocal_terms"][name])),2)
            for v in rows),arb(0)).upper()
        terms[name]=record(value.sqrt().upper())
    means={}
    for name in MEAN_NAMES:
        value=sum((up(box(v["radial_weight_integral"]))*ipow(
            up(box(v["source_bounds"]["independent_even_mean_factor"]))*
            up(box(v["source_bounds"]["complete_five_independent_even_mean_terms"][name])),2)
            for v in rows),arb(0)).upper()
        means[name]=record(value.sqrt().upper())
    return dict(complete_rows=len(rows),complete_first_correction_ordinary_L2_source=record(sq.sqrt().upper()),
        complete_squared_source_integral=record(sq),separate_component_L2_bounds=components,
        individual_first_row_nonlocal_L2_bounds=terms,individual_independent_mean_L2_bounds=means)

def summarize(rows,cover,radius,gain):
    negative=[v for v in rows if v["side"]=="negative"]
    positive=[v for v in rows if v["side"]=="positive"]
    collar=[v for v in positive if Q(v["interval"][1])<=BODY]
    body=[v for v in positive if Q(v["interval"][0])>=BODY]
    if len(collar)+len(body)!=len(positive):raise ValueError("a positive source row crosses the fixed body cut")
    lo,hi=map(Q,cover)
    if not (interval_cover(negative,lo,ROOTS[1]) and interval_cover(positive,ROOTS[0],hi)):
        raise ValueError("the complete recombined physical source cover has a gap or duplicate")
    totals={side:channel_sum(v) for side,v in (("negative",negative),("positive",positive),
        ("positive_collar",collar),("positive_body",body))}
    value=up(box(totals["negative"]["complete_first_correction_ordinary_L2_source"]))
    return dict(exact_radius=str(radius),exact_cover=list(map(str,cover)),complete=True,
        exact_complete_physical_root_piece=list(map(str,PIECE)),complete_rows=len(rows),
        source_summary=totals,original_actual_negative_source_to_primitive_L2_gain=copy.deepcopy(gain),
        negative_first_correction_source_component_Hminus4over3_to_primitive_L2=record((up(box(gain))*value).upper()),
        positive_collar_first_correction_source_L2=totals["positive_collar"]["complete_first_correction_ordinary_L2_source"],
        positive_body_first_correction_source_L2=totals["positive_body"]["complete_first_correction_ordinary_L2_source"],
        uncertain_root_band_charged_separately_on_each_side=True,
        all_complete_means_and_physical_seams_retained=True,
        positive_weighted_port_conversion_claimed=False,complete_corrected_seam_operator_paid=False,
        whole_first_corrected_strong_return_or_cutoff97_inverse_claimed=False)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","prepared","out"):parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new whole-piece interval mathematics runs only in the public Actions repository")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise ValueError("the pinned complete interval environment changed")
    if args.out.exists():raise FileExistsError("preserve every original or new successful or failed prefix")
    if not (sha(inner.__file__)==ISOURCE and sha(full.__file__)==CSOURCE
        and sha(numerator.__file__)==NSOURCE and sha(numerator.L.__file__)==numerator.ALGEBRA):
        raise ValueError("a frozen complete source, Airy or Taylor-tail helper changed")
    ctx.prec=320;start=time.monotonic()
    doc=dict(kind="whole_original_physical_root_piece_complete_first_Airy_sources",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),runtime=runtime,
        complete=False,proved=False,failure=None,gates=[],stages={},case_stages=[],cases=[],
        original_Taylor_native_sha256=TAYLOR,original_Nraw_native_sha256=NRAW,
        original_bstar_complete_native_sha256=BSTAR,original_auxiliary_native_sha256=AUX,
        original_moment_native_sha256=MOMENT,original_complete_conversion_sha256=CONVERSIONS,
        fixed_intrinsic_parameter="eta_0",exact_real_delta_radius=str(DELTA),
        exact_complex_coefficient_delta_radius=str(DELTA),exact_root_interval=list(map(str,ROOTS)),
        exact_original_physical_piece_interval=list(map(str,PIECE)),
        exact_original_scalar_germ=list(map(str,GERM)),fixed_positive_body_cut=str(BODY),
        exact_holomorphic_rho_radius=str(RHO),exact_holomorphic_phi_width=str(SIGMA),
        input_cutoff=CUTOFF,physical_frequency="4 abs(j)",actual_first_correction_density="n^(1/6)",
        source_window="H^-4/3 input -> ordinary radial L2(H^-2/3 pair); second row is the independent even mean",
        original_targets_FFT_intrinsic_cubics_folds_signed_coefficients_and_saved_norms_recomputed=0,
        original_matrix_words_or_same_order_conversions_recomputed=0,
        original_exterior_complete_source_rows_recomputed=0,
        original_Airy_profiles_recomputed=0,original_complete_angular_tail_factors_recomputed=0,
        new_profile_stages=0,reused_profile_stages=0,new_radius_budget_stages=0,reused_radius_budget_stages=0,
        new_complete_source_rows=0,reused_complete_source_rows=0,new_case_summaries=0,
        new_piece_summary_stages=0,reused_piece_summary_stages=0,
        new_case_summary_stages=0,reused_case_summary_stages=0,
        copied_original_complete_rows=0,reused_copied_original_complete_rows=0,
        new_partial_original_rows=0,reused_partial_original_rows=0,
        recovered_unindexed_complete_stages=0,original_complete_physical_seams_retained=1079,
        original_complete_normalized_seam_rows_retained=653,
        all_original_failed_large_radius_gates_and_ledgers_retained=True,
        actual_local_numerator_is_unnormalized=True,all_old_circle_and_independent_mean_terms_retained=True,
        artificial_interface_source_introduced=False,complete_first_corrected_trial_seam_sources_paid=False,
        positive_weighted_port_conversion_claimed=False,full_high_feedback_strong_return_or_PDE_branch_claimed=False)
    def gate(name,value):
        value=bool(value);doc["gates"].append(dict(name=name,passed=value))
        if not value:raise ValueError("whole physical root-piece gate failed: "+name)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(args.out,doc)
    def stage(name,kind,build):
        path=args.out.parent/"stages"/(name+".json.gz")
        if name in doc["stages"] or path.exists():
            if name in doc["stages"]:v=checked_file(path,doc["stages"][name])
            else:v=read(path)
            if not (v["stage"]==name and v["stage_kind"]==kind and v["complete"]
                and v["source_sha256"]==doc["source_sha256"]
                and v["input_manifest_sha256"]==doc["input_manifest_sha256"] and v["runtime"]==runtime
                and v["original_Taylor_native_sha256"]==TAYLOR and v["original_Nraw_native_sha256"]==NRAW):
                raise ValueError("a new accepted scalar stage changed its complete identity")
            if name not in doc["stages"]:
                doc["recovered_unindexed_complete_stages"]+=1
                doc["stages"][name]=dict(**receipt(path,args.out.parent),stage_kind=kind);checkpoint()
            doc["reused_"+kind]+=1
            return v["payload"]
        payload=build()
        v=dict(stage=name,stage_kind=kind,complete=True,source_sha256=doc["source_sha256"],
            input_manifest_sha256=doc["input_manifest_sha256"],runtime=runtime,
            original_Taylor_native_sha256=TAYLOR,original_Nraw_native_sha256=NRAW,payload=payload)
        save(path,v);doc["stages"][name]=dict(**receipt(path,args.out.parent),stage_kind=kind)
        doc["new_"+kind]+=1;checkpoint()
        return payload
    try:
        m=read(args.manifest)
        gate("the public manifest requests the complete same physical root piece and exact full source windows",
            m["public_repository"]==PUBLIC and m["mathematical_parameters"]["input_cutoff"]==CUTOFF
            and m["mathematical_parameters"]["physical_piece"]==2549
            and m["mathematical_parameters"]["Taylor_order"]==12
            and m["mathematical_parameters"]["residual_Taylor_order"]==10)
        pins={}
        for entry in m["files"]:
            path=args.repo_root/entry["path"]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("an exact pinned scientific input changed: "+entry["path"])
            pins[str(path.resolve())]=entry
        paths={k:args.repo_root/v for k,v in m["input_paths"].items()}
        for entry in m.get("external_completed_natives",[]):
            path=args.prepared/entry["prepared_path"]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("a complete immutable original artifact file changed")
            paths[entry["name"]]=path
            pins[str(path.resolve())]=entry
        ext,ep,nraw,np_,aux,ap,bn,bp=[read(paths[k]) for k in
            ("Taylor_native","Taylor_process","Nraw_native","Nraw_process",
             "auxiliary_native","auxiliary_process","bstar_native","bstar_process")]
        gate("Taylor12 Nraw and complete exterior b-star sources are exact actual successful inputs",
            success(ext,ep,paths["Taylor_native"],TSOURCE,TMANIFEST,TAYLOR,19)
            and success(nraw,np_,paths["Nraw_native"],NSOURCE,NMANIFEST,NRAW,10)
            and success(bn,bp,paths["bstar_native"],BSOURCE,BMANIFEST,BSTAR,8)
            and sha(paths["Taylor_process"])==TPROC and sha(paths["Nraw_process"])==NPROC
            and sha(paths["bstar_process"])==BPROC
            and sha(paths["auxiliary_native"])==ap["native_sha256"]==AUX
            and sha(paths["auxiliary_process"])==APROC
            and aux["complete"] and aux["proved"] and aux["failure"] is None
            and ap["actual_returncode"]==0 and ap["mathematical_complete"]
            and aux["gates"]==ap["mathematical_gates"] and all(g["passed"] for g in aux["gates"]))
        gate("the exact repaired background direction fixed eta0 complex disk and true root are identical",
            ext["background_definition_sha256"]==nraw["background_definition_sha256"]==inner.BASE
            and ext["explicit_direction_definition_sha256"]==nraw["explicit_direction_definition_sha256"]==inner.ZDEF
            and ext["actual_intrinsic_parameter"]==nraw["fixed_intrinsic_parameter"]==bn["fixed_intrinsic_parameter"]=="eta_0"
            and Q(ext["exact_fixed_intrinsic_parameter"])==Q(nraw["exact_fixed_intrinsic_parameter"])
                ==Q(-7789843107295549,4611686018427387904)
            and Q(ext["exact_complex_delta_radius"])==Q(nraw["exact_complex_delta_radius"])
                ==Q(bn["exact_real_delta_radius"])==DELTA
            and ext["exact_root_interval"]==nraw["exact_root_interval"]==aux["exact_root_interval"]
                ==bn["exact_root_interval"]==list(map(str,ROOTS))
            and ext["exact_original_physical_piece_interval"]==nraw["exact_original_physical_piece_interval"]
                ==list(map(str,PIECE))
            and aux["exact_original_piece_interval"]==list(map(str,PIECE))
            and aux["exact_original_scalar_germ"]==list(map(str,GERM))
            and ext["old_product_domain"]==nraw["old_product_domain"]
            and ext["complete_branch_identity"]==nraw["original_complete_branch_identity"]
            and bn["fixed_positive_body_cut"]==str(BODY))
        domain=ext["old_product_domain"]
        hstar=max(ROOTS[1]-PIECE[0],PIECE[1]-ROOTS[0])
        gate("both genuine physical seams remain within the original scalar germ and paid old-product domains",
            GERM[0]<=PIECE[0]<ROOTS[0]<ROOTS[1]<BODY<PIECE[1]<=GERM[1]
            and Q(domain["exact_rho_radius"])==RHO and Q(domain["exact_phi_width"])==SIGMA
            and hstar<RHO and hstar<Q(3,40000)
            and Q(domain["exact_physical_interval"][0])>PIECE[0]
            and Q(domain["exact_physical_interval"][1])<PIECE[1]
            and sha(paths["contract"])==CONTRACT)
        doc["exact_whole_piece_rho_cover"]=str(hstar)
        doc["original_complete_holomorphic_product"]=copy.deepcopy(domain)
        doc["original_complete_source_summaries"]=copy.deepcopy(bn["cases"])
        doc["original_exact_inner_interval"]=copy.deepcopy(bn["exact_physical_inner_interval"])
        doc["original_bstar_domain_results"]=copy.deepcopy(bn["original_bstar_domain_results"])
        doc["original_complete_seam_native_sha256"]=bn["original_complete_seam_native_sha256"]
        gate("the original six exterior cases and all true seam ledgers retain their complete recorded identities",
            len(bn["case_stages"])==len(bn["cases"])==6
            and bn["original_complete_physical_seams_retained"]==1079
            and bn["original_complete_normalized_seam_rows_retained"]==653
            and bn["all_fourier_outputs_old_projections_and_independent_mean_retained"]
            and not bn["complete_first_corrected_trial_seam_sources_paid"])
        norm=read(paths["moment_native"]);converted=read(paths["conversions"])
        nr=norm["coefficient_rows"];zr=converted["rows"]
        gate("all1328 moment rows and complete same-order old-circle conversions are reused unchanged",
            sha(paths["moment_native"])==MOMENT and sha(paths["conversions"])==CONVERSIONS
            and norm["complete"] and norm["proved"] and norm["failure"] is None
            and all(g["passed"] for g in norm["gates"])
            and converted["complete"] and converted["source_sha256"]==CSOURCE
            and converted["input_manifest_sha256"]==CMANIFEST
            and len(nr)==len(zr)==1328
            and all(n["common_row"]==z["common_row"]==i and n["interval"]==z["interval"]
                and n["original_root_row"]==z["original_root_row"]
                and z["original_moment_row_payload_sha256"]==payload_sha(n)
                and set(z["matrix_conversion"]["costs"])==set(full.WORD_NAMES)
                for i,(n,z) in enumerate(zip(nr,zr))))
        selected=[]
        def accepted_stage(native,key,base,native_hash):
            old=key in native.get("original_stages",{})
            entry=(native["original_stages"] if old else native["stages"])[key]
            path=base/entry["file"]
            if str(path.resolve()) not in pins:raise ValueError("an original norm or tail stage was not manifest-pinned")
            value=checked_file(path,entry)
            source=numerator.OLD_SOURCE if old else TSOURCE if native_hash==TAYLOR else NSOURCE
            manifest=numerator.OLD_MANIFEST if old else TMANIFEST if native_hash==TAYLOR else NMANIFEST
            if not (value["complete"] and value.get("stage",value.get("name"))==key
                and value["source_sha256"]==source and value["input_manifest_sha256"]==manifest):
                raise ValueError("an original accepted norm stage changed its original source or manifest")
            selected.append(dict(stage=key,native_sha256=native_hash,file=entry["file"],
                bytes=entry["bytes"],sha256=entry["sha256"],
                original_source_sha256=source,original_manifest_sha256=manifest))
            return value["payload"]
        tnorm={};nnorm={}
        for width in WIDTHS:
            tag=str(width.numerator)+"_"+str(width.denominator)
            tnorm[str(width)]=[]
            for degree in range(13):
                key="full-Fourier-norm-"+tag+"-degree-"+str(degree).zfill(3)
                row=accepted_stage(ext,key,paths["Taylor_native"].parent,TAYLOR)
                if not (row["degree"]==degree and Q(row["exact_width"])==width
                    and len(row["a1"])==len(row["b1"])==4):
                    raise ValueError("an original amplitude norm changed degree width or full angular order")
                tnorm[str(width)].append(row)
            nnorm[str(width)]=[]
            for degree in range(11):
                key="full-Nraw-Fourier-norm-"+tag+"-degree-"+str(degree).zfill(3)
                row=accepted_stage(nraw,key,paths["Nraw_native"].parent,NRAW)
                if not (row["degree"]==degree and Q(row["exact_output_phi_width"])==width
                    and len(row["Nraw_a"])==len(row["Nraw_b"])==3):
                    raise ValueError("an original full residual norm changed degree width or angular order")
                nnorm[str(width)].append(row)
        mult=accepted_stage(nraw,"complete-local-numerator-whole-product-multipliers",
            paths["Nraw_native"].parent,NRAW)
        multipliers=decode(mult["complete_multiplier_bounds"])
        amplitudes={k:up(box(domain["full_canonical_"+v+"_sup"])) for k,v in (("a","a1"),("b","b1"))}
        gate("exactly48 complete original norm stages and one whole-product multiplier stage were read without recomputation",
            len(selected)==49 and sum(v["native_sha256"]==TAYLOR for v in selected)==26
            and sum(v["native_sha256"]==NRAW for v in selected)==23
            and Q(mult["exact_common_product_rho_radius"])==RHO
            and Q(mult["exact_common_product_phi_width"])==SIGMA
            and set(multipliers)=={"C11","C01","C02","C10","C00","Cab","Cba"})
        doc["original_selected_complete_stage_receipts"]=selected
        doc["original_complete_matrix_row_count"]=1328
        if args.resume:
            previous=read(args.resume)
            keys=("source_sha256","input_manifest_sha256","runtime","original_Taylor_native_sha256",
                "original_Nraw_native_sha256","original_bstar_complete_native_sha256",
                "original_auxiliary_native_sha256","original_moment_native_sha256",
                "original_complete_conversion_sha256","exact_root_interval",
                "exact_original_physical_piece_interval","original_selected_complete_stage_receipts")
            gate("every new resumed prefix retains the exact source manifest runtime and original scientific objects",
                all(previous.get(k)==doc.get(k) for k in keys))
            originals=[dict(document=read(paths["bstar_case_"+str(i)]),
                sha256=sha(paths["bstar_case_"+str(i)])) for i in range(6)]
            adopted_stages,adopted_cases,recovery=recover_prefix_receipts(previous,args.resume.parent,originals,doc)
            for entry in [*adopted_stages.values(),*adopted_cases]:
                source=args.resume.parent/entry["file"];target=args.out.parent/entry["file"]
                checked_file(source,entry);target.parent.mkdir(parents=True,exist_ok=True)
                if target.exists():raise FileExistsError("resume would overwrite an existing complete source prefix")
                shutil.copyfile(source,target)
            doc["stages"]=adopted_stages
            doc["case_stages"]=adopted_cases
            doc["exact_atomic_prefix_recovery"]=recovery
            doc["cases"]=copy.deepcopy(previous.get("cases",[]))
            doc["preserved_actual_prefix"]=dict(native_sha256=sha(args.resume),complete=previous["complete"],
                proved=previous["proved"],failure=previous["failure"],gates=previous["gates"])
        checkpoint()
        profile=stage("whole-original-root-piece-Airy-profile","profile_stages",
            lambda:inner.inner_profile(aux["cases"][0],ex(hstar)))
        plan=[]
        for idx,n in enumerate(nr):
            left,right=map(Q,n["interval"]);a=max(left,PIECE[0]);b=min(right,PIECE[1])
            if not a<b:continue
            cuts=sorted({a,b,*[x for x in (*ROOTS,BODY) if a<x<b]})
            for a,b in zip(cuts[:-1],cuts[1:]):
                band=ROOTS[0]<=a<b<=ROOTS[1]
                sides=("negative","positive") if band else ("negative",) if b<=ROOTS[0] else ("positive",)
                for side in sides:
                    plan.append(dict(common_row=idx,interval=[str(a),str(b)],side=side,uncertain_root_band=band))
        gate("the entire original physical root piece is covered once on each required side including both root-band charges",
            plan and interval_cover([v for v in plan if v["side"]=="negative"],PIECE[0],ROOTS[1])
            and interval_cover([v for v in plan if v["side"]=="positive"],ROOTS[0],PIECE[1])
            and all(PIECE[0]<=Q(v["interval"][0])<Q(v["interval"][1])<=PIECE[1] for v in plan))
        doc["exact_new_physical_partition"]=copy.deepcopy(plan)
        rootrows=[]
        for i,piece in enumerate(plan):
            a,b=map(Q,piece["interval"]);h=max(ROOTS[1]-a,b-ROOTS[0])
            bname="complete-radius-budget-"+str(h.numerator)+"-"+str(h.denominator)
            budget=stage(bname,"radius_budget_stages",lambda h=h:radius_budget(h,tnorm,nnorm,
                ext["first_correction_derivative_budgets"],nraw["complete_correlated_Nraw_budgets"],
                multipliers,amplitudes))
            idx=piece["common_row"];name="complete-physical-root-row-"+str(i).zfill(4)
            row=stage(name,"complete_source_rows",lambda piece=piece,idx=idx,budget=budget:
                source_row(piece,nr[idx],zr[idx],budget,profile))
            if not (row["interval"]==piece["interval"] and row["side"]==piece["side"]
                and row["common_row"]==idx and row["original_piece"]==2549
                and row["original_moment_row_payload_sha256"]==payload_sha(nr[idx])
                and row["complete_radius_budget_payload_sha256"]==payload_sha(budget)):
                raise ValueError("a new complete physical-piece row changed its original inputs")
            rootrows.append((name,row))
        doc["whole_root_piece_source_summary"]=stage("whole-root-piece-complete-two-sided-source-summary",
            "piece_summary_stages",lambda:{side:channel_sum([r for _,r in rootrows if r["side"]==side])
                for side in ("negative","positive")})
        doc["whole_root_piece_row_count"]=len(rootrows);checkpoint()
        for ci,radius in enumerate(RADII):
            original_path=paths["bstar_case_"+str(ci)]
            original=checked_file(original_path,bn["case_stages"][ci])
            cover=tuple(map(Q,original["exact_cover"]))
            if not (original["complete"] and original["source_sha256"]==BSOURCE
                and original["input_manifest_sha256"]==BMANIFEST and original["exact_radius"]==str(radius)
                and cover==(ROOTS[0]-radius,ROOTS[1]+radius)
                and cover[0]<PIECE[0]<PIECE[1]<cover[1]
                and original["complete_case_summary"]==bn["cases"][ci]):
                raise ValueError("a complete original exterior radius lost its exact physical identity")
            items=[];omitted=[]
            for oi,row in enumerate(original["rows"]):
                a,b=map(Q,row["interval"]);left=max(a,PIECE[0]);right=min(b,PIECE[1])
                if left<right and not (row["original_piece"]==2549 and PIECE[0]<=a<b<=PIECE[1]):
                    raise ValueError("an original source row crosses a physical root-piece seam without subdivision")
                if row["original_piece"]==2549 and not PIECE[0]<=a<b<=PIECE[1]:
                    raise ValueError("the recorded original root-piece label leaves its exact two seams")
                if left<right:omitted.append(dict(original_serial=oi,original_row_payload_sha256=payload_sha(row)))
                for u,v in ((a,min(b,PIECE[0])),(max(a,PIECE[1]),b)):
                    if not u<v:continue
                    kind="copied_original" if (u,v)==(a,b) else "partial_original"
                    items.append(dict(kind=kind,original_serial=oi,interval=[str(u),str(v)],
                        side=row["side"],original_row_payload_sha256=payload_sha(row)))
            for name,row in rootrows:
                items.append(dict(kind="new_complete_root_piece",stage=name,interval=copy.deepcopy(row["interval"]),
                    side=row["side"],row_payload_sha256=payload_sha(row)))
            items.sort(key=lambda v:(0 if v["side"]=="negative" else 1,Q(v["interval"][0]),Q(v["interval"][1])))
            path=args.out.parent/"cases"/("radius-"+str(radius.numerator)+"-"+str(radius.denominator)+".json.gz")
            if ci<len(doc["case_stages"]):case=checked_file(path,doc["case_stages"][ci])
            elif path.exists():
                case=read(path);doc["case_stages"].append(case_receipt(path,args.out.parent,case));checkpoint()
            else:
                case=dict(kind="whole_physical_root_piece_recombined_complete_first_Airy_sources",
                    complete=False,source_sha256=doc["source_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
                    runtime=runtime,exact_radius=str(radius),exact_cover=original["exact_cover"],
                    original_complete_case_sha256=sha(original_path),
                    original_complete_case_summary=copy.deepcopy(original["complete_case_summary"]),
                    original_bstar_profile=copy.deepcopy(original["original_bstar_profile"]),
                    original_normalized_seam_ledger=copy.deepcopy(original["original_normalized_seam_ledger"]),
                    original_complete_outward_states=copy.deepcopy(original["original_complete_outward_states"]),
                    original_root_mean_norm_stage=copy.deepcopy(original["original_root_mean_norm_stage"]),
                    discarded_old_estimator_records_retained_by_original_case_sha256=True,
                    original_rows_wholly_replaced_by_same_solution_estimate=omitted,
                    complete_whole_piece_profile_stage="whole-original-root-piece-Airy-profile",
                    rows=[],row_roles=[])
                save(path,case);doc["case_stages"].append(case_receipt(path,args.out.parent,case));checkpoint()
            if not (case["source_sha256"]==doc["source_sha256"]
                and case["input_manifest_sha256"]==doc["input_manifest_sha256"] and case["runtime"]==runtime
                and case["original_complete_case_sha256"]==sha(original_path)
                and case["exact_radius"]==str(radius) and len(case["rows"])==len(case["row_roles"])
                and len(case["rows"])<=len(items)):
                raise ValueError("an accepted recombination prefix changed its complete scientific identity")
            for j,(row,role) in enumerate(zip(case["rows"],case["row_roles"])):
                if role!=items[j]:raise ValueError("an accepted complete recombination plan changed")
                if role["kind"]=="copied_original":
                    if row!=original["rows"][role["original_serial"]]:
                        raise ValueError("an unchanged exterior source row was not copied verbatim")
                    doc["reused_copied_original_complete_rows"]+=1
                elif role["kind"]=="partial_original":doc["reused_partial_original_rows"]+=1
                elif payload_sha(row)!=role["row_payload_sha256"]:
                    raise ValueError("a previously accepted whole-piece row changed")
            if case["complete"]:
                if len(case["rows"])!=len(items):raise ValueError("a complete recombination is missing source rows")
                summary=case["complete_case_summary"]
                if ci==len(doc["cases"]):doc["cases"].append(copy.deepcopy(summary))
                elif doc["cases"][ci]!=summary:raise ValueError("a complete case summary changed")
                checkpoint();continue
            rootmap=dict(rootrows)
            for j in range(len(case["rows"]),len(items)):
                role=items[j]
                if role["kind"]=="copied_original":
                    row=copy.deepcopy(original["rows"][role["original_serial"]])
                    doc["copied_original_complete_rows"]+=1
                elif role["kind"]=="partial_original":
                    a,b=map(Q,role["interval"])
                    row=restrict_original(original["rows"][role["original_serial"]],a,b)
                    doc["new_partial_original_rows"]+=1
                else:row=copy.deepcopy(rootmap[role["stage"]])
                case["rows"].append(row);case["row_roles"].append(copy.deepcopy(role))
                save(path,case);doc["case_stages"][ci]=case_receipt(path,args.out.parent,case);checkpoint()
            summary=stage("complete-recombined-case-summary-"+str(ci),"case_summary_stages",
                lambda:summarize(case["rows"],cover,radius,original["complete_case_summary"][
                    "original_actual_negative_source_to_primitive_L2_gain"]))
            case.update(complete=True,complete_case_summary=summary,
                complete_original_exterior_rows_copied_verbatim=sum(v["kind"]=="copied_original" for v in items),
                complete_original_partial_rows=sum(v["kind"]=="partial_original" for v in items),
                new_whole_piece_rows_reused=len(rootrows),
                all_original_physical_seam_ledgers_retained=True,no_artificial_interface_source=True,
                complete_first_corrected_trial_seam_sources_paid=False)
            save(path,case);doc["case_stages"][ci]=case_receipt(path,args.out.parent,case);doc["new_case_summaries"]+=1
            if ci==len(doc["cases"]):doc["cases"].append(copy.deepcopy(summary))
            elif doc["cases"][ci]!=summary:raise ValueError("a completed new source summary changed")
            checkpoint()
        gate("all six full radial cases have complete local old-circle and independent-mean integrals with true cuts",
            len(doc["case_stages"])==len(doc["cases"])==6
            and all(v["complete"] and Q(v["exact_radius"])==RADII[i] for i,v in enumerate(doc["cases"])))
        gate("every original finite coefficient norm matrix word and exterior row was reused without successful mathematics repeated",
            all(doc[k]==0 for k in
                ("original_targets_FFT_intrinsic_cubics_folds_signed_coefficients_and_saved_norms_recomputed",
                 "original_matrix_words_or_same_order_conversions_recomputed",
                 "original_exterior_complete_source_rows_recomputed","original_Airy_profiles_recomputed",
                 "original_complete_angular_tail_factors_recomputed"))
            and len(doc["original_selected_complete_stage_receipts"])==49
            and doc["all_old_circle_and_independent_mean_terms_retained"]
            and not doc["artificial_interface_source_introduced"]
            and not doc["complete_first_corrected_trial_seam_sources_paid"]
            and not doc["positive_weighted_port_conversion_claimed"]
            and not doc["full_high_feedback_strong_return_or_PDE_branch_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            accepted_new_stages=len(doc["stages"]),whole_piece_rows=doc.get("whole_root_piece_row_count",0),
            complete_cases=len(doc["cases"]),native_sha256=sha(args.out),seconds=doc["seconds"]),
            allow_nan=False),flush=True)
if __name__=="__main__":main()
