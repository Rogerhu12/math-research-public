#!/usr/bin/env python3
"""Evaluate only exact-fold-cancelled h/gd/qv source envelopes on six old windows.

All original profiles, amplitude tensors, moment/matrix rows, radial weights,
positive split fees, seams and complete means are retained. New math runs only
in the public repository's Actions and every accepted prefix is preserved.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_analytic_Airy_old_circle_sources as old

PUBLIC=old.PUBLIC
ROOT_SHA=old.ROOT_SHA;SEAM_SHA=old.SEAM_SHA;OLD_SHA=old.OLD_SHA
RADIAL_SHA="fec8740c26064b973c61828a960c3e5c7e864b83542222c155b9e56474c39853"
RADIAL_SOURCE="10e961471e790286fc439ce56b5e0fff9e9b00e1a444d61396f4187fabe35414"
RADIAL_MANIFEST="831bbaa726f36b1bb9e0b69fec67e55031b54ef341dfa77b6a7d5cf549f9bae2"
DELTA=old.DELTA;CUTOFF=old.CUTOFF;SIGMA=old.SIGMA
ex,box,up,ipow,powq=old.ex,old.box,old.up,old.ipow,old.powq
read,save,sha=old.read,old.save,old.sha
rec,compact,encode,decode=old.rec,old.compact,old.encode,old.decode
tensor_encode,tensor_decode=old.tensor_encode,old.tensor_decode
mv,mvjets,svjets,vjscale=old.mv,old.mvjets,old.svjets,old.vjscale
TENSOR_KEYS=old.NUMERIC_AMPLITUDE_KEYS
CHANGED=("complete_SQ","complete_RQ_J_gd","complete_RQ_JL_h",
         "complete_primitive_error","old_mean_rQ","old_mean_vphi")
UNCHANGED=("complete_SV","old_mean_raw_D","old_mean_V0")

def scalar_product(*jets):
    """Nonnegative ordinary angular jets of order one, with exact Leibniz factors."""
    value=[arb(1),arb(0)]
    for a in jets:
        if len(a)!=2:raise ValueError("a scalar product lacks its first angular jet")
        value=[(value[0]*a[0]).upper(),(value[1]*a[0]+value[0]*a[1]).upper()]
    return value

def exact_scalar_jet_case(case,refined,amplitude):
    af=refined["actual_forcing"]
    if af["leading_strip"]!="3/64" or af["coefficient_strip"]!="1/16":
        raise ValueError("the previously paid old-angle analytic strips changed")
    bounds={k:box(v) for k,v in case["bounds"].items()}
    mixed=af["A_mixed_derivative_bounds"]
    A10,A11,A01,A02=[up(box(mixed[str(v)])) for v in ((1,0),(1,1),(0,1),(0,2))]
    Am=bounds["A_lower"].lower();Ap=bounds["A_upper"].upper()
    km=bounds["k_lower"].lower();ap=bounds["a_upper"].upper()
    G=bounds["leading_G"].upper();R=amplitude["R"]
    k1=up(box(af["divided_curvature_derivatives"]["first"]))
    LE=up(box(refined["complete_coefficient_bounds"]["log_EG_r"]))
    if not (Am>0 and km>0 and R>0):
        raise ValueError("an original complete root or divided-curvature gap was lost")
    Lr=(A10/(6*Am)+k1/(4*km)+LE).upper()
    Lp=(A01/(6*Am)).upper()
    Lrp=((A11/Am+A10*A01/ipow(Am,2))/6).upper()
    Lpp=((A02/Am+ipow(A01/Am,2))/6).upper()
    Gr=(G*Lr).upper();Gp=(G*Lp).upper()
    Grp=(G*(Lrp+Lr*Lp)).upper();Gpp=(G*(Lpp+Lp*Lp)).upper()
    Q0=(ap*powq(Am,Q(-1,3))).upper()
    Q1=(Q0*A01/(3*Am)).upper()
    Q2=(Q0*(A02/(3*Am)+ex(Q(4,9))*ipow(A01/Am,2))).upper()
    T0=(R*powq(Ap,Q(2,3))).upper()
    T1=(ex(Q(2,3))*R*powq(Am,Q(-1,3))*A01).upper()
    T2=(ex(Q(2,3))*R*(powq(Am,Q(-1,3))*A02+
        powq(Am,Q(-4,3))*A01*A01/3)).upper()
    x0=up(box(af["flow_variational_C"]["1"]))
    x1=(R*up(box(af["flow_variational_C"]["2"]))).upper()
    y0,y1=T1,T2
    B0=(x0*x0+T0*y0*y0).upper()
    B1=(2*x0*x1+T1*y0*y0+2*T0*y0*y1).upper()
    L0=(A01/Am).upper();L1=(A02/Am+ipow(A01/Am,2)).upper()
    P=[[[arb(0),Q0*T0],[Q0,arb(0)]],
       [[arb(0),Q1*T0+Q0*T1],[Q1,arb(0)]],
       [[arb(0),Q2*T0+2*Q1*T1+Q0*T2],[Q2,arb(0)]]]
    result=dict(G=[G,Gp],Gphi=[Gp,Gpp],Gr=Gr,Grphi=Grp,
        Q=[Q0,Q1],P=P,T=[T0,T1],x=[x0,x1],y=[y0,y1],
        B=[B0,B1],logAphi=[L0,L1],
        original_R=R,original_A_lower=Am,original_k_lower=km,
        original_A_mixed=[A10,A11,A01,A02],original_k_first=k1,
        original_full_mean_log_EG_r=LE)
    def finite(v):
        if isinstance(v,dict):return all(finite(x) for x in v.values())
        if isinstance(v,list):return all(finite(x) for x in v)
        return v.is_finite() and v.lower()>=0
    if not finite(result):raise ValueError("a complete new scalar jet is invalid")
    return result

def cancelled_source_constants(c,a,j,old_row,side):
    hi,w=a["hi"],a["w"]
    def A(v):
        if len(v)!=2:raise ValueError("the two true Airy components were merged")
        def profile(name):
            return sum((x*y for x,y in zip(a["profiles"][name],v)),arb(0)).upper()
        center=profile("central")
        core=((center*center+4*ipow(profile("negative"),2)).sqrt().upper()
              if side=="negative" else max(center,profile("positive")).upper())
        return (a["composition"]*a["fourier"]*core).upper()
    def Dfrak(v,last):return mvjets(hi,v,last+1)[1:]
    def B(v):return (A(mv(hi[0],v[0]))+A(Dfrak(v,0)[0])).upper()
    def M0(v):return A(Dfrak(v,0)[0])
    D=c["D"];G,Gp=j["G"];Gpp=j["Gphi"][1]
    Z=[(j["Gr"]+D[0]*Gp+2*G*D[1]).upper(),
       (j["Grphi"]+D[1]*Gp+D[0]*Gpp+2*G*D[2]).upper()]
    # N.7 is used as an exact identity before any absolute value is taken.
    a1=scalar_product(Z,j["B"])
    a2=scalar_product(j["Q"],j["T"],j["Gphi"],j["x"],j["y"])
    b1=scalar_product(Z,j["x"],j["y"])
    b2=scalar_product(j["Q"],j["G"],j["logAphi"],j["B"])
    b3=scalar_product(j["Q"],j["G"],j["y"],j["y"],j["y"])
    gd=[[(a1[p]+2*a2[p]).upper(),(2*b1[p]+b2[p]/2+b3[p]).upper()]
        for p in range(2)]
    Pw=mvjets(j["P"],w,2)
    if not c["eta_lower"]>0:raise ValueError("the actual row eta gap is not positive")
    h=vjscale(Pw,1/c["eta_lower"])
    y=svjets(c["V"],Pw,2)
    qv=old.vjadd(svjets(c["V"],gd,1),svjets(c["V"][1:],Pw,1))
    Bh,Bgd=B(h),B(gd)
    changed=dict(complete_SQ=c["C_SQ_directed"]*Bh,
        complete_RQ_J_gd=c["C_RQJ_directed"]*Bgd,
        complete_RQ_JL_h=c["C_RQJL_directed"]*Bh,
        complete_primitive_error=c["C_primitive_directed"]*B(qv),
        old_mean_rQ=c["m0_rQ"]*M0(h),
        old_mean_vphi=c["cB"]*c["V"][1]*M0(y))
    saved=old_row["complete_scalar_nonlocal_terms"]
    if set(saved)!=set(CHANGED+UNCHANGED):raise ValueError("an original complete source term was lost")
    terms={key:up(box(saved[key])) for key in UNCHANGED}
    choices={}
    for key in CHANGED:
        old_bound=up(box(saved[key]));new_bound=changed[key].upper()
        terms[key]=min(old_bound,new_bound).upper()
        choices[key]="new_exact_cancellation" if new_bound<old_bound else "original_complete_bound"
    # This is the original full even-mean equation; only its last term uses v_nonmean.
    Bw=B(w)
    vn=list(c["V"]);vn[0]=min(vn[0],vn[1]/4).upper()
    new_mean=(c["exact_nonlocal_even_mean_row_factor"]*
        (M0(svjets(c["U"],h,1))+c["C_uJ_directed"]*Bgd+
         c["C_uJL_directed"]*Bh+c["C_uJB_directed"]*Bw+
         c["K"]*M0(svjets(vn,w,1)))).upper()
    mean=min(new_mean,up(box(old_row["full_even_mean_singular_envelope"]))).upper()
    first=min((c["C_J_scalar"]*sum(terms.values(),arb(0))).upper(),
              up(box(old_row["first_row_singular_envelope"]))).upper()
    if not all(z.is_finite() and z.lower()>=0 for z in (first,mean,*terms.values())):
        raise ValueError("a complete cancelled source bound is invalid")
    return first,mean,terms,choices

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","root-native","radial-native","seam-native","old-native","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematics runs only in public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):
        raise ValueError("the successful numerical runtime changed")
    if a.out.exists():raise FileExistsError("preserve every actual native and accepted prefix")
    ctx.prec=256;started=time.monotonic()
    result=dict(kind="actual_exact_fold_cancelled_old_circle_sources_v1",
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),runtime=runtime,complete=False,proved=False,failure=None,gates=[],cases=[],
        root_native_sha256=ROOT_SHA,first_seam_native_sha256=SEAM_SHA,
        original_completed_norm_native_sha256=OLD_SHA,original_radial_reference_native_sha256=RADIAL_SHA,
        old_completed_moment_rows_recomputed=0,old_completed_directed_rows_recomputed=0,
        old_completed_analytic_amplitude_cases_recomputed=0,old_completed_Airy_profiles_recomputed=0,
        original_target_coefficient_ray_and_amplitude_solves_recomputed=0,
        original_radial_weights_or_split_integrals_recomputed=0,
        actual_new_scalar_jet_cases=0,scalar_jet_cases_reused=0,
        actual_new_source_integral_rows=0,source_integral_rows_reused=0,
        input_cutoff=CUTOFF,physical_frequency="4|j|",density_input_normalization="n^(7/6)",
        exact_real_delta_radius=str(DELTA),analytic_leading_strip=str(SIGMA),
        source_window="H^-4/3 -> ordinary radial L2(H^-2/3 x H^-2/3)",
        old_mean_and_all_Fourier_outputs_retained=True,original_raw_D_source_retained=True,
        original_global_seam_equations_and_fees_retained=True,
        auxiliary_complex_domain_not_used=True,local_L0_w1_paid=False,
        positive_source_to_root_conversion_claimed=False,complete_strong_return_norm_evaluated=False,
        numerical_cutoff97_inverse_claimed=False,actual_PDE_branch_claimed=False)
    def check(name,truth):
        passed=bool(truth);result["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual exact-fold source gate failed: "+name)
    def checkpoint():
        result["seconds"]=time.monotonic()-started;save(a.out,result)
    try:
        manifest=read(a.manifest);result["input_manifest_sha256"]=sha(a.manifest)
        for entry in manifest["files"]:
            path=a.repo_root/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("an exact complete input changed: "+entry["path"])
        for path,expected,size in ((a.root_native,ROOT_SHA,5923431),
                (a.radial_native,RADIAL_SHA,3434233),(a.seam_native,SEAM_SHA,904977),
                (a.old_native,OLD_SHA,4837715)):
            if not path.is_file() or sha(path)!=expected or path.stat().st_size!=size:
                raise ValueError("a completed original native changed its exact bytes")
        root,radial,seam,original=[read(path) for path in
            (a.root_native,a.radial_native,a.seam_native,a.old_native)]
        receipt=read(a.repo_root/manifest["input_paths"]["radial_reference_process"])
        check("the actual complete radial_reference_native_has_all_nine_gates_and_a_zero_return_receipt",
            radial["complete"] and radial["proved"] and radial["failure"] is None
            and radial["source_sha256"]==RADIAL_SOURCE and radial["input_manifest_sha256"]==RADIAL_MANIFEST
            and len(radial["gates"])==9 and all(g["passed"] for g in radial["gates"])
            and receipt["actual_returncode"]==0 and receipt["complete"] and receipt["mathematical_complete"]
            and receipt["mathematical_failure"] is None and str(receipt["run_id"])=="43635999157"
            and receipt["native_sha256"]==RADIAL_SHA and receipt["native_bytes"]==3434233
            and receipt["mathematical_source_sha256"]==RADIAL_SOURCE
            and receipt["manifest_sha256"]==RADIAL_MANIFEST
            and len(receipt["mathematical_gates"])==9 and all(g["passed"] for g in receipt["mathematical_gates"]))
        check("the_original_root_seam_and_moment_natives_retain_complete_whole_parameter_identities",
            all(d["complete"] and d["proved"] and d["failure"] is None
                and all(g["passed"] for g in d["gates"]) for d in (root,seam,original))
            and len(root["rows"])==1300 and len(seam["seams"])==1079
            and len(original["coefficient_rows"])==1328
            and original["source_sha256"]==old.OLD_SOURCE and original["input_manifest_sha256"]==old.OLD_MANIFEST
            and seam["root_native_sha256"]==ROOT_SHA and seam["first_forcing_native_sha256"]==old.FORCE_SHA
            and len(seam["refined_forcing_radius_cases"])==6
            and radial["root_native_sha256"]==ROOT_SHA and radial["first_seam_native_sha256"]==SEAM_SHA
            and radial["original_completed_norm_native_sha256"]==OLD_SHA
            and radial["exact_real_delta_radius"]==str(DELTA)
            and radial["exact_cover"]==root["exact_cover"]
            and radial["exact_root_interval"]==root["exact_root_interval"]
            and radial["source_window"]==result["source_window"])
        check("all_six_profiles_and_amplitude_tensors_and_all1328_directed_rows_are_complete_saved_inputs",
            len(radial["coefficient_rows"])==1328 and len(radial["cases"])==6
            and all(c["complete"] and c["complete_radial_reference_profile"]
                and set(c["original_complete_analytic_amplitude_numeric"])==set(TENSOR_KEYS)
                and len(c["rows"])==c["complete_original_rows"] for c in radial["cases"])
            and radial["actual_new_source_integral_rows"]==4377
            and radial["old_completed_moment_rows_recomputed"]==0
            and radial["old_completed_directed_rows_recomputed"]==0
            and radial["old_completed_analytic_amplitude_cases_recomputed"]==0)
        rows=radial["coefficient_rows"]
        for i,row in enumerate(rows):
            previous=original["coefficient_rows"][i]
            if (row["common_row"]!=i or previous["common_row"]!=i
                or row["interval"]!=previous["interval"]
                or row["original_root_row"]!=previous["original_root_row"]):
                raise ValueError("an original moment or directed row changed identity")
        check("the_complete_original1328_closed_row_cover_is_retained_without_new_coefficients",
            all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:])))
        result["original_completed_norm_rows_reused"]=1328
        result["original_completed_directed_rows_reused"]=1328
        result["original_completed_analytic_amplitude_cases_reused"]=6
        result["original_completed_Airy_profile_cases_reused"]=6
        result["original_directed_table_sha256"]=hashlib.sha256(
            json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
        roots=list(map(Q,root["exact_root_interval"]))
        body_cut=Q(radial["fixed_positive_body_cut"])
        check("the_same_uncertain_root_and_exact_positive_body_cut_are_preserved",
            body_cut==Q(1192029371497,5000000000000) and body_cut>roots[1])
        for key in ("fixed_positive_body_cut","positive_cut_receipt_sha256",
                "actual_negative_Cauchy_native_sha256","exact_root_interval","exact_cover"):
            result[key]=radial[key]
        if a.resume:
            previous=read(a.resume)
            check("every_accepted_new_scalar_and_integral_prefix_has_identical_source_runtime_and_inputs",
                previous["source_sha256"]==sha(__file__) and previous["input_manifest_sha256"]==sha(a.manifest)
                and previous["runtime"]==runtime and previous["root_native_sha256"]==ROOT_SHA
                and previous["first_seam_native_sha256"]==SEAM_SHA
                and previous["original_completed_norm_native_sha256"]==OLD_SHA
                and previous["original_radial_reference_native_sha256"]==RADIAL_SHA)
            result["cases"]=list(previous["cases"])
        checkpoint()
        for ci,(case,accepted,refined) in enumerate(zip(root["cases"],radial["cases"],
                                                        seam["refined_forcing_radius_cases"])):
            if (not case["passed"] or not refined["passed"] or not all(g["passed"] for g in refined["gates"])
                or case["exact_radius"]!=accepted["exact_radius"] or case["exact_radius"]!=refined["exact_radius"]
                or case["exact_radial_cover"]!=accepted["exact_cover"]
                or case["exact_radial_cover"]!=refined["exact_cover"]):
                raise ValueError("an accepted whole radius or original seam domain changed")
            selected=accepted["rows"];cl,cr=map(Q,case["exact_radial_cover"])
            if (not selected or selected[0]["interval"][0]!=str(cl)
                or selected[-1]["interval"][1]!=str(cr)
                or len(selected)!=accepted["complete_original_rows"]):
                raise ValueError("an original source radius lost its complete closed cover")
            if ci<len(result["cases"]):
                out=result["cases"][ci]
                if out["exact_radius"]!=case["exact_radius"] or out["exact_cover"]!=case["exact_radial_cover"]:
                    raise ValueError("a saved new scalar or integral prefix changed domain")
                result["scalar_jet_cases_reused"]+=int(out.get("complete_new_scalar_jets",False))
                result["source_integral_rows_reused"]+=len(out["rows"])
                if out.get("complete"):continue
            else:
                out=dict(exact_radius=case["exact_radius"],exact_cover=case["exact_radial_cover"],
                    complete=False,complete_original_rows=len(selected),rows=[],
                    original_complete_analytic_amplitude_numeric=accepted["original_complete_analytic_amplitude_numeric"],
                    original_radial_reference_profiles_numeric=accepted["new_profiles_numeric"])
                result["cases"].append(out)
            if (out["original_complete_analytic_amplitude_numeric"]!=accepted["original_complete_analytic_amplitude_numeric"]
                or out["original_radial_reference_profiles_numeric"]!=accepted["new_profiles_numeric"]):
                raise ValueError("an accepted old tensor or radial-reference profile changed")
            amplitude=tensor_decode(out["original_complete_analytic_amplitude_numeric"])
            amplitude["profiles"]=tensor_decode(out["original_radial_reference_profiles_numeric"])
            if out.get("complete_new_scalar_jets"):
                jets=tensor_decode(out["new_scalar_jet_numeric"])
            else:
                jets=exact_scalar_jet_case(case,refined,amplitude)
                out["new_scalar_jet_numeric"]=tensor_encode(jets)
                out["complete_new_scalar_jets"]=True
                result["actual_new_scalar_jet_cases"]+=1;checkpoint()
            prefix=len(out["rows"])
            neg=arb(0);pos=arb(0);pc=arb(0);pb=arb(0)
            for si,saved in enumerate(selected):
                idx=saved["common_row"];coefficient=rows[idx]
                if coefficient["interval"]!=saved["interval"]:
                    raise ValueError("an original source row lost its complete coefficient interval")
                if si<prefix:
                    item=out["rows"][si]
                    if item["common_row"]!=idx or item["interval"]!=saved["interval"]:
                        raise ValueError("an accepted new integral prefix changed its exact row")
                else:
                    c=decode(original["coefficient_rows"][idx]["bounds"])
                    c.update(decode(coefficient["bounds"]))
                    item=dict(common_row=idx,interval=saved["interval"])
                    result["last_attempted_source_row"]=dict(radius=case["exact_radius"],common_row=idx)
                    for side in ("negative","positive"):
                        oside=saved[side]
                        if oside.get("exact_zero_radial_part"):
                            item[side]=dict(squared_source_integral=compact(arb(0)),exact_zero_radial_part=True)
                            continue
                        weight=up(box(oside["radial_weight_integral"]))
                        if not weight>0:raise ValueError("an original nonzero radial weight lost positivity")
                        first,mean,terms,choices=cancelled_source_constants(c,amplitude,jets,oside,side)
                        norm2=(first*first+mean*mean).upper()
                        item[side]=dict(radial_weight_integral=oside["radial_weight_integral"],
                            first_row_singular_envelope=compact(first),
                            full_even_mean_singular_envelope=compact(mean),
                            complete_scalar_nonlocal_terms=encode(terms),
                            first_row_operator_term_envelopes=encode({k:c["C_J_scalar"]*v for k,v in terms.items()}),
                            exact_cancellation_term_choices=choices,
                            squared_source_integral=compact((weight*norm2).upper()),
                            original_radial_weight_copied_without_recalculation=True)
                        if side=="positive":
                            f0=max(arb(0),box(oside["first_row_singular_envelope"]).lower())
                            m0=max(arb(0),box(oside["full_even_mean_singular_envelope"]).lower())
                            denominator=(f0*f0+m0*m0).lower()
                            if not denominator>0:
                                raise ValueError("the saved numerical upper-envelope squared denominator lost its strict lower gap")
                            item[side]["original_upper_envelope_squared_lower"]=compact(denominator)
                            for name in ("collar_squared_source_integral","body_squared_source_integral"):
                                fee=up(box(oside[name]))
                                item[side][name]=compact((fee*norm2/denominator).upper())
                    out["rows"].append(item)
                    result["actual_new_source_integral_rows"]+=1
                    result.pop("last_attempted_source_row",None)
                neg+=box(item["negative"]["squared_source_integral"])
                pos+=box(item["positive"]["squared_source_integral"])
                if not item["positive"].get("exact_zero_radial_part"):
                    pc+=box(item["positive"]["collar_squared_source_integral"])
                    pb+=box(item["positive"]["body_squared_source_integral"])
                if si%128==0:checkpoint()
            out["separate_first_row_term_L2_source_bounds"]={}
            for side in ("negative","positive"):
                sums={}
                for item in out["rows"]:
                    row=item[side]
                    if row.get("exact_zero_radial_part"):continue
                    weight=up(box(row["radial_weight_integral"]))
                    for key,value in row["first_row_operator_term_envelopes"].items():
                        term=up(box(value));sums[key]=sums.get(key,arb(0))+weight*term*term
                out["separate_first_row_term_L2_source_bounds"][side]={
                    key:compact(value.sqrt().upper()) for key,value in sums.items()}
            out["negative_complete_ordinary_L2_source"]=rec(neg.sqrt().upper())
            out["positive_complete_ordinary_L2_source"]=rec(pos.sqrt().upper())
            out["positive_collar_complete_ordinary_L2_source"]=rec(pc.sqrt().upper())
            out["positive_body_complete_ordinary_L2_source"]=rec(pb.sqrt().upper())
            out["actual_negative_source_to_primitive_L2_gain"]=accepted["actual_negative_source_to_primitive_L2_gain"]
            gain=up(box(out["actual_negative_source_to_primitive_L2_gain"]))
            out["negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2"]=rec((gain*neg.sqrt()).upper())
            out["original_radial_reference_source_bounds"]={key:accepted[key] for key in (
                "negative_complete_ordinary_L2_source","positive_complete_ordinary_L2_source",
                "positive_collar_complete_ordinary_L2_source","positive_body_complete_ordinary_L2_source",
                "negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2")}
            out["original_complete_matrix_widths"]=accepted["complete_original_matrix_widths"]
            out["original_complete_source_bounds_not_overwritten"]=True
            out["positive_split_retains_independent_mean_and_is_not_a_full_low_high_inverse"]=True
            out["positive_source_to_root_conversion_claimed"]=False
            out["complete"]=True;checkpoint()
        check("all_six_new_scalar_jet_cases_preserve_original_profiles_and_full_two_component_tensors",
            len(result["cases"])==6 and all(c["complete"] and c["complete_new_scalar_jets"]
                and c["original_complete_analytic_amplitude_numeric"]==r["original_complete_analytic_amplitude_numeric"]
                and c["original_radial_reference_profiles_numeric"]==r["new_profiles_numeric"]
                for c,r in zip(result["cases"],radial["cases"])))
        check("every4377_original_source_row_and_both_sides_and_positive_split_fees_are_complete",
            all(len(c["rows"])==c["complete_original_rows"] for c in result["cases"])
            and sum(len(c["rows"]) for c in result["cases"])==4377)
        check("no_original_target_amplitude_matrix_profile_or_radial_weight_science_was_repeated",
            all(result[key]==0 for key in ("old_completed_moment_rows_recomputed",
                "old_completed_directed_rows_recomputed","old_completed_analytic_amplitude_cases_recomputed",
                "old_completed_Airy_profiles_recomputed","original_target_coefficient_ray_and_amplitude_solves_recomputed",
                "original_radial_weights_or_split_integrals_recomputed")))
        result.update(complete=True,proved=True)
    except BaseException as error:
        result["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=result["complete"],proved=result["proved"],failure=result["failure"],
            complete_cases=sum(bool(c.get("complete")) for c in result["cases"]),
            actual_new_scalar_jet_cases=result["actual_new_scalar_jet_cases"],
            actual_new_source_integral_rows=result["actual_new_source_integral_rows"],
            seconds=result["seconds"])),flush=True)
if __name__=="__main__":main()
