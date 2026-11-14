#!/usr/bin/env python3
"""Refine six completed Airy profiles with the true radial reference and entire tails.

Reuse every accepted analytic amplitude tensor, complete moment row and directed
matrix row. Only six scalar profile bounds and their source integrals are new.
"""
from __future__ import annotations
import argparse,json,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_analytic_Airy_old_circle_sources as old

PUBLIC=old.PUBLIC
ROOT_SHA=old.ROOT_SHA;FORCE_SHA=old.FORCE_SHA;SEAM_SHA=old.SEAM_SHA
OLD_SHA=old.OLD_SHA;DIRECTED_SHA=old.DIRECTED_SHA
ANALYTIC_SHA="e54f05c3eea0e2ed9a8f7511004059b730b448adb26c9e035cc1803325080db8"
ANALYTIC_SOURCE="439a29e2f1a3273bf9901d6a6ddfae075fb88a308d9a9e2a665cf839fc3e0dc7"
ANALYTIC_MANIFEST="ee066de1b0328b6ede8b2a928680548065f6a8d1ad7d678f3ca515febf834e37"
DELTA=old.DELTA;CUTOFF=old.CUTOFF;SIGMA=old.SIGMA
ex,box,up,ipow,powq=old.ex,old.box,old.up,old.ipow,old.powq
read,save,sha=old.read,old.save,old.sha
rec,compact,encode,decode=old.rec,old.compact,old.encode,old.decode
tensor_encode,tensor_decode=old.tensor_encode,old.tensor_decode
radial_weight,source_constants=old.radial_weight,old.source_constants
TENSOR_KEYS=old.NUMERIC_AMPLITUDE_KEYS

def entire_profiles(Z,K=16):
    """R9--12: positive entire series, with both complete geometric tails."""
    if not Z>0 or K<1:raise ValueError("the entire central disk or tail index is invalid")
    evidence=[];values=[];derivatives=[]
    Z3=ipow(Z,3)
    for r in (0,1):
        c=arb(1);value=arb(0);derivative=arb(0)
        for k in range(K):
            m=3*k+r
            value+=c*ipow(Z,m)
            if m:derivative+=m*c*ipow(Z,m-1)
            c/=((m+3)*(m+2))
        m=3*K+r
        qF=(Z3/((m+3)*(m+2))).upper()
        qD=(Z3/(m*(m+2))).upper()
        if not (qF<1 and qD<1):
            raise ValueError("a full entire-profile tail does not contract")
        firstF=(c*ipow(Z,m)).upper()
        firstD=(m*c*ipow(Z,m-1)).upper()
        tailF=(firstF/(1-qF)).upper()
        tailD=(firstD/(1-qD)).upper()
        totalF=(value+tailF).upper();totalD=(derivative+tailD).upper()
        values.append(totalF);derivatives.append(totalD)
        evidence.append(dict(initial_index=r,first_omitted_index=m,
            complete_value=compact(totalF),complete_derivative=compact(totalD),
            value_tail_ratio=compact(qF),derivative_tail_ratio=compact(qD),
            entire_value_tail=compact(tailF),entire_derivative_tail=compact(tailD)))
    CA=max(values).upper();CD=max(derivatives).upper()
    return CA,CD,evidence

def profile_case(root_case,completed_case,amplitude):
    vals={k:box(v) for k,v in root_case["bounds"].items()}
    amin=vals["a_lower"].lower();ap=vals["a_upper"].upper()
    Am=vals["A_lower"].lower();Ap=vals["A_upper"].upper()
    saved=completed_case["analytic_amplitude_summary"]
    if saved["leading_strip"]!="3/64" or not saved["no_angular_Cauchy_loss"]:
        raise ValueError("the actual complete old-angle analytic domain changed")
    m=box(saved["real_inverse_phase_derivative_lower"]).lower()
    j=(1-m).upper();epsilon=(ap*j/amin).upper()
    if not (amin>0 and Am>0 and m>0 and j>=0 and epsilon<1):
        raise ValueError("the true radial-reference relative angular gap was lost")
    g=(1-epsilon).lower()
    Z=powq(ex(Q(3,2))*(1+epsilon),Q(2,3)).upper()
    CA,CD,evidence=entire_profiles(Z)
    cm=(ex(Q(5,36))/g).exp()/(2*arb.pi().sqrt())
    cp=(ex(Q(5,72))/g).exp()/(2*arb.pi().sqrt())
    derivative=(1+ex(Q(11,36))/g).upper()
    R=amplitude["R"]
    profiles=dict(
        central=[(CA*powq(3/(2*amin),Q(1,6))).upper(),
                 (CD*powq(R,Q(1,4))*powq(ex(4*CUTOFF),Q(-1,6))).upper()],
        negative=[(cm*powq(Am,Q(-1,6))).upper(),
                  (derivative*cm*powq(R,Q(1,2))*powq(Ap,Q(1,6))).upper()],
        positive=[(cp*powq(Am,Q(-1,6))).upper(),
                  (derivative*cp*powq(R,Q(1,2))*powq(Ap,Q(1,6))).upper()])
    if not all(x.is_finite() and x.lower()>=0 for row in profiles.values() for x in row):
        raise ValueError("a new complete Airy profile is invalid")
    summary=dict(a_minus=compact(amin),a_plus=compact(ap),
        actual_A_minus=compact(Am),actual_A_plus=compact(Ap),
        actual_jacobian_deviation=compact(j),relative_angular_error=compact(epsilon),
        high_halfplane_gap=compact(g),central_argument_disk=compact(Z),
        complete_central_Ai=compact(CA),complete_central_Ai_prime=compact(CD),
        high_derivative_factor=compact(derivative),
        profiles=tensor_encode(profiles),
        leading_strip=str(SIGMA),parameter_domain="real |delta|<=1/100000000",
        true_radial_reference_retained=True,radial_trial_cutoff_or_seam_inserted=False,
        high_prefactors_use_actual_A_bounds=True,entire_tail_terms=16,
        no_original_matrix_or_amplitude_tensor_recomputed=True)
    return profiles,summary,evidence

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","root-native","analytic-native","old-native","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all numerical mathematics requires the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):
        raise ValueError("the pinned successful numerical runtime changed")
    if a.out.exists():raise FileExistsError("preserve every actual native and accepted prefix")
    ctx.prec=256;started=time.monotonic()
    result=dict(kind="actual_radial_reference_Airy_profiles_and_old_circle_sources_v1",
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),runtime=runtime,complete=False,proved=False,failure=None,
        root_native_sha256=ROOT_SHA,first_forcing_native_sha256=FORCE_SHA,
        first_seam_native_sha256=SEAM_SHA,original_completed_norm_native_sha256=OLD_SHA,
        original_completed_directed_native_sha256=DIRECTED_SHA,
        original_completed_analytic_native_sha256=ANALYTIC_SHA,
        old_completed_moment_rows_recomputed=0,old_completed_directed_rows_recomputed=0,
        old_completed_analytic_amplitude_cases_recomputed=0,new_coefficient_norm_rows=0,
        original_target_coefficient_ray_and_amplitude_solves_recomputed=0,
        actual_new_profile_cases=0,profile_cases_reused=0,actual_new_source_integral_rows=0,
        input_cutoff=CUTOFF,physical_frequency="4|j|",density_input_normalization="n^(7/6)",
        source_window="H^-4/3 -> ordinary radial L2(H^-2/3 x H^-2/3)",
        exact_real_delta_radius=str(DELTA),analytic_leading_strip=str(SIGMA),
        old_mean_and_all_Fourier_outputs_retained=True,
        local_L0_w1_paid=False,positive_source_to_root_conversion_claimed=False,
        complete_strong_return_norm_evaluated=False,numerical_cutoff97_inverse_claimed=False,
        actual_PDE_branch_claimed=False,gates=[],coefficient_rows=[],cases=[])
    def check(name,truth):
        passed=bool(truth);result["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual radial-reference Airy gate failed: "+name)
    def checkpoint():
        result["seconds"]=time.monotonic()-started;save(a.out,result)
    try:
        manifest=read(a.manifest);result["input_manifest_sha256"]=sha(a.manifest)
        for entry in manifest["files"]:
            path=a.repo_root/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("an exact complete input changed: "+entry["path"])
        for path,expected,size in ((a.root_native,ROOT_SHA,5923431),
                (a.analytic_native,ANALYTIC_SHA,3445399),(a.old_native,OLD_SHA,4837715)):
            if not path.is_file() or sha(path)!=expected or path.stat().st_size!=size:
                raise ValueError("a completed original native changed its exact bytes")
        root=read(a.root_native);analytic=read(a.analytic_native);original_norm=read(a.old_native)
        process=read(a.repo_root/manifest["input_paths"]["analytic_process"])
        check("the actual complete analytic Airy native and all ten public gates have a zero-return receipt",
            analytic["complete"] and analytic["proved"] and analytic["failure"] is None
            and analytic["source_sha256"]==ANALYTIC_SOURCE
            and analytic["input_manifest_sha256"]==ANALYTIC_MANIFEST
            and len(analytic["gates"])==10 and all(g["passed"] for g in analytic["gates"])
            and process["actual_returncode"]==0 and process["complete"] and process["mathematical_complete"]
            and process["mathematical_failure"] is None and str(process["run_id"])=="43634456797"
            and process["native_sha256"]==ANALYTIC_SHA and process["native_bytes"]==3445399
            and process["mathematical_source_sha256"]==ANALYTIC_SOURCE
            and process["manifest_sha256"]==ANALYTIC_MANIFEST
            and len(process["mathematical_gates"])==10
            and all(g["passed"] for g in process["mathematical_gates"]))
        check("all original root and moment records retain their proved identities and whole real parameter family",
            all(d["complete"] and d["proved"] and d["failure"] is None
                and all(g["passed"] for g in d["gates"]) for d in (root,original_norm))
            and len(root["rows"])==1300 and len(original_norm["coefficient_rows"])==1328
            and original_norm["source_sha256"]==old.OLD_SOURCE
            and original_norm["input_manifest_sha256"]==old.OLD_MANIFEST
            and analytic["root_native_sha256"]==ROOT_SHA
            and analytic["first_forcing_native_sha256"]==FORCE_SHA
            and analytic["first_seam_native_sha256"]==SEAM_SHA
            and analytic["original_completed_norm_native_sha256"]==OLD_SHA
            and analytic["original_completed_directed_native_sha256"]==DIRECTED_SHA
            and analytic["exact_real_delta_radius"]==str(DELTA)
            and analytic["exact_cover"]==root["exact_cover"]
            and analytic["exact_root_interval"]==root["exact_root_interval"])
        check("all six complete amplitude tensors and all1328 directed rows were saved by the actual successful run",
            len(analytic["coefficient_rows"])==1328 and len(analytic["cases"])==6
            and all(c["complete"] and c["complete_analytic_amplitude"]
                and set(c["complete_analytic_amplitude_numeric"])==set(TENSOR_KEYS)
                and len(c["rows"])==c["complete_original_rows"] for c in analytic["cases"])
            and analytic["actual_new_analytic_amplitude_cases"]==6
            and analytic["actual_new_source_integral_rows"]==4377
            and analytic["old_completed_moment_rows_recomputed"]==0
            and analytic["old_completed_directed_rows_recomputed"]==0)
        roots=list(map(Q,root["exact_root_interval"]))
        body_cut=Q(analytic["fixed_positive_body_cut"])
        check("the same exact positive body cut and complete root interval are retained",
            body_cut==Q(1192029371497,5000000000000) and body_cut>roots[1]
            and analytic["source_window"]==result["source_window"])
        result["fixed_positive_body_cut"]=str(body_cut)
        result["positive_cut_receipt_sha256"]=analytic["positive_cut_receipt_sha256"]
        result["actual_negative_Cauchy_native_sha256"]=analytic["actual_negative_Cauchy_native_sha256"]
        if a.resume:
            resumed=read(a.resume)
            check("every accepted profile and integral prefix has the identical source and complete input identities",
                resumed["source_sha256"]==sha(__file__)
                and resumed["input_manifest_sha256"]==sha(a.manifest)
                and resumed["runtime"]==runtime
                and resumed["root_native_sha256"]==ROOT_SHA
                and resumed["original_completed_norm_native_sha256"]==OLD_SHA
                and resumed["original_completed_analytic_native_sha256"]==ANALYTIC_SHA)
            result["cases"]=list(resumed["cases"])
        result["coefficient_rows"]=list(analytic["coefficient_rows"])
        for i,row in enumerate(result["coefficient_rows"]):
            oldrow=original_norm["coefficient_rows"][i]
            if (row["common_row"]!=i or oldrow["common_row"]!=i
                or row["interval"]!=oldrow["interval"]
                or row["original_root_row"]!=oldrow["original_root_row"]):
                raise ValueError("an accepted complete moment/directed row changed identity")
        check("all1328 moment and directed coefficient rows are copied with no new matrix calculation",
            len(result["coefficient_rows"])==1328
            and all(x["interval"][1]==y["interval"][0]
                for x,y in zip(result["coefficient_rows"],result["coefficient_rows"][1:])))
        result["original_completed_norm_rows_reused"]=1328
        result["original_completed_directed_rows_reused"]=1328
        result["original_completed_analytic_amplitude_cases_reused"]=6
        result["profile_cases_reused"]=sum(bool(c.get("complete_radial_reference_profile"))
            for c in result["cases"])
        checkpoint()
        for ci,(case,accepted) in enumerate(zip(root["cases"],analytic["cases"])):
            if (case["exact_radius"]!=accepted["exact_radius"]
                or case["exact_radial_cover"]!=accepted["exact_cover"] or not case["passed"]):
                raise ValueError("an accepted radius or whole radial domain changed")
            cl,cr=map(Q,case["exact_radial_cover"])
            selected=[r for r in result["coefficient_rows"]
                if cl<=Q(r["interval"][0]) and Q(r["interval"][1])<=cr]
            if (not selected or selected[0]["interval"][0]!=str(cl)
                or selected[-1]["interval"][1]!=str(cr)
                or len(selected)!=accepted["complete_original_rows"]):
                raise ValueError("a complete source radius lost its exact common cover")
            if ci<len(result["cases"]):
                out=result["cases"][ci]
                if out["exact_radius"]!=case["exact_radius"] or out["exact_cover"]!=case["exact_radial_cover"]:
                    raise ValueError("a completed radius prefix changed domain")
                if out.get("complete"):continue
            else:
                out=dict(exact_radius=case["exact_radius"],exact_cover=case["exact_radial_cover"],
                    complete=False,complete_original_rows=len(selected),rows=[],
                    original_complete_analytic_amplitude_numeric=accepted["complete_analytic_amplitude_numeric"])
                result["cases"].append(out)
            if out["original_complete_analytic_amplitude_numeric"]!=accepted["complete_analytic_amplitude_numeric"]:
                raise ValueError("an original accepted amplitude tensor was modified")
            amplitude=tensor_decode(accepted["complete_analytic_amplitude_numeric"])
            if out.get("complete_radial_reference_profile"):
                profiles=tensor_decode(out["new_profiles_numeric"])
            else:
                profiles,summary,evidence=profile_case(case,accepted,amplitude)
                out.update(new_profiles_numeric=tensor_encode(profiles),
                    radial_reference_profile_summary=summary,
                    entire_central_profile_complete_tail_evidence=evidence,
                    complete_radial_reference_profile=True)
                result["actual_new_profile_cases"]+=1;checkpoint()
            amplitude["profiles"]=profiles
            prefix=len(out["rows"]);neg=arb(0);pos=arb(0);pos_collar=arb(0);pos_body=arb(0)
            for si,saved in enumerate(selected):
                left,right=map(Q,saved["interval"])
                if si<prefix:
                    item=out["rows"][si]
                    if item["common_row"]!=saved["common_row"] or item["interval"]!=saved["interval"]:
                        raise ValueError("an accepted integral prefix changed identity")
                else:
                    c=decode(original_norm["coefficient_rows"][saved["common_row"]]["bounds"])
                    c.update(decode(saved["bounds"]))
                    item=dict(common_row=saved["common_row"],interval=saved["interval"])
                    result["last_attempted_source_row"]=dict(radius=case["exact_radius"],common_row=saved["common_row"])
                    for side in ("negative","positive"):
                        weight=radial_weight(left,right,roots,side)
                        if not weight>0:
                            item[side]=dict(squared_source_integral=compact(arb(0)),exact_zero_radial_part=True)
                            continue
                        first,mean,terms=source_constants(c,amplitude,side)
                        value=(weight*(first*first+mean*mean)).upper()
                        item[side]=dict(radial_weight_integral=compact(weight),
                            first_row_singular_envelope=compact(first),full_even_mean_singular_envelope=compact(mean),
                            complete_scalar_nonlocal_terms=encode(terms),
                            first_row_operator_term_envelopes=encode({k:c["C_J_scalar"]*z for k,z in terms.items()}),
                            squared_source_integral=compact(value))
                        if side=="positive":
                            wc=(radial_weight(left,min(right,body_cut),roots,side)
                                if left<min(right,body_cut) else arb(0))
                            wb=(radial_weight(max(left,body_cut),right,roots,side)
                                if max(left,body_cut)<right else arb(0))
                            item[side]["collar_squared_source_integral"]=compact((wc*(first*first+mean*mean)).upper())
                            item[side]["body_squared_source_integral"]=compact((wb*(first*first+mean*mean)).upper())
                    out["rows"].append(item);result["actual_new_source_integral_rows"]+=1
                    result.pop("last_attempted_source_row",None)
                neg+=box(item["negative"]["squared_source_integral"])
                pos+=box(item["positive"]["squared_source_integral"])
                if not item["positive"].get("exact_zero_radial_part"):
                    pos_collar+=box(item["positive"]["collar_squared_source_integral"])
                    pos_body+=box(item["positive"]["body_squared_source_integral"])
                if si%128==0:checkpoint()
            gain=box(accepted["actual_negative_source_to_primitive_L2_gain"])
            out["complete_case_operator_cost_maxima"]=accepted["complete_case_operator_cost_maxima"]
            out["separate_first_row_term_L2_source_bounds"]={}
            for side in ("negative","positive"):
                sums={}
                for item in out["rows"]:
                    row=item[side]
                    if row.get("exact_zero_radial_part"):continue
                    weight=box(row["radial_weight_integral"])
                    for key,value in row["first_row_operator_term_envelopes"].items():
                        term=box(value);sums[key]=sums.get(key,arb(0))+weight*term*term
                out["separate_first_row_term_L2_source_bounds"][side]={
                    key:compact(value.sqrt().upper()) for key,value in sums.items()}
            out["negative_complete_ordinary_L2_source"]=rec(neg.sqrt().upper())
            out["positive_complete_ordinary_L2_source"]=rec(pos.sqrt().upper())
            out["positive_collar_complete_ordinary_L2_source"]=rec(pos_collar.sqrt().upper())
            out["positive_body_complete_ordinary_L2_source"]=rec(pos_body.sqrt().upper())
            out["positive_split_retains_independent_mean_and_is_not_a_full_low_high_inverse"]=True
            out["actual_negative_source_to_primitive_L2_gain"]=accepted["actual_negative_source_to_primitive_L2_gain"]
            out["negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2"]=rec((gain*neg.sqrt()).upper())
            out["positive_source_to_root_conversion_claimed"]=False
            out["original_norm_rows_reused"]=len(selected);out["original_directed_rows_reused"]=len(selected)
            out["complete_original_matrix_widths"]=accepted["complete_original_matrix_widths"]
            out["original_complete_source_bounds_not_overwritten"]=True
            out["original_complete_analytic_source_bounds"]={k:accepted[k] for k in (
                "negative_complete_ordinary_L2_source","positive_complete_ordinary_L2_source",
                "positive_collar_complete_ordinary_L2_source","positive_body_complete_ordinary_L2_source")}
            out["complete"]=True;checkpoint()
        check("all six true radial-reference profile cases retain the full original numeric tensors",
            len(result["cases"])==6 and all(c["complete_radial_reference_profile"]
                and c["original_complete_analytic_amplitude_numeric"]==accepted["complete_analytic_amplitude_numeric"]
                for c,accepted in zip(result["cases"],analytic["cases"])))
        check("both entire central series and their derivative tails contract in every complete case",
            all(box(e["value_tail_ratio"]).upper()<1 and box(e["derivative_tail_ratio"]).upper()<1
                for c in result["cases"] for e in c["entire_central_profile_complete_tail_evidence"]))
        check("all six complete source integrals retain both sides of the root and the independent mean",
            len(result["cases"])==6 and all(c["complete"] and len(c["rows"])==c["complete_original_rows"]
                for c in result["cases"])
            and sum(len(c["rows"]) for c in result["cases"])==4377)
        check("no original target coefficient ray amplitude matrix or Fourier-tail calculation was repeated",
            result["old_completed_moment_rows_recomputed"]==0
            and result["old_completed_directed_rows_recomputed"]==0
            and result["old_completed_analytic_amplitude_cases_recomputed"]==0
            and result["new_coefficient_norm_rows"]==0
            and result["original_target_coefficient_ray_and_amplitude_solves_recomputed"]==0)
        result["exact_root_interval"]=root["exact_root_interval"];result["exact_cover"]=root["exact_cover"]
        result.update(complete=True,proved=True)
    except BaseException as error:
        result["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=result["complete"],failure=result["failure"],
            complete_cases=sum(bool(c.get("complete")) for c in result["cases"]),
            actual_new_profile_cases=result["actual_new_profile_cases"],
            actual_new_source_integral_rows=result["actual_new_source_integral_rows"],
            seconds=result["seconds"])),flush=True)
if __name__=="__main__":main()
