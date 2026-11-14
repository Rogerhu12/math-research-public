#!/usr/bin/env python3
"""Accumulate central ghat0/ghat1 with uniform ghat2, retaining all crosses.

Actual first-source box bounds follow by real-parameter mean value:
B_j(I)<=B_j(p0)+eta*C_j(I), E1_j(I)<=E1_j(p0)+eta*C_j(I).
The unchanged central ghat0 then pays eta*B_j(I) in both A_j and E0_j.
No third parameter derivative, complex parameter domain, or formal finite
parameter family is assumed.  The output is an exact-time prefix certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
from flint import arb, acb, ctx
from fourfold_parameter_density_accumulate import center_zero_spatial, check_leaf as check_full_leaf, records
from fourfold_parameter_ordered_defect import advance_parameter_integrals, add_rows, row_norms
from fourfold_forward_density_pipeline_Q1024_v3 import decode_ball, encode_ball, save, upper
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_domain_cover_verify import Time
from fourfold_saved_circle_field_multidomain_budget import read


def read_snapshot(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw),hashlib.sha256(raw).hexdigest()


def key(entry):
    return (entry["segment"],*map(Fraction,entry["normalized_subspan"]))


def check_leaf(entry,descriptor_sha,center,eta,S,inner,spatial):
    path,zero_path=Path(entry["path"]),Path(entry["g0_report_path"])
    report=read(path)
    if not eta or report.get("parameter_orders")==[1,2]:
        return check_full_leaf(entry,descriptor_sha,center,eta,S,inner,spatial)
    if sha(path)!=entry["sha256"]or sha(zero_path)!=entry["g0_report_sha256"]:
        raise ValueError("the completed second-source or g0 report changed")
    zero=read(zero_path);identity=report["identity"];ref=identity["reference"]
    if not(report.get("complete")and report.get("complete_continuous_uniform_second_parameter_density_proved")
        and report.get("second_parameter_only")and report["parameter_orders"]==[2]
        and zero.get("complete")and zero.get("complete_continuous_true_density_proved")):
        raise ValueError("no completed continuous uniform second-source certificate")
    if (ref!=zero["identity"]["reference"]or ref["retarget_descriptor_sha256"]!=descriptor_sha
        or ref["leg"]!="forward"or int(ref["segment"])!=int(entry["segment"])
        or list(map(Fraction,ref["normalized_subspan"]))!=list(map(Fraction,entry["normalized_subspan"]))
        or not identity.get("fixed_reference_independent_of_parameter")):
        raise ValueError("second-source reference coordinates differ")
    if (report["reference_certificate_sha256"]!=entry["g0_report_sha256"]
        or not identity["whole_real_parameter_tube"]
        or list(map(Fraction,identity["exact_parameter_interval"]))!=[center-eta,center+eta]):
        raise ValueError("uniform second-source parameter interval differs")
    if (Fraction(report["label_strip"])!=S or Fraction(report["inner_strip"])!=inner
        or Fraction(report["spatial_derivative_strip"])!=spatial
        or Fraction(zero["label_strip"])!=S or Fraction(zero["inner_strip"])!=inner):
        raise ValueError("uniform second-source strip contracts differ")
    if len(report["density"])!=1 or report["density"][0]["parameter_order"]!=2:
        raise ValueError("unexpected partial source list")
    jet=report["density"][0]["complete_spatial_jet_inputs"]
    if (not jet["proved"]or Fraction(jet["source_error_strip"])!=S
        or Fraction(jet["finite_spatial_norm_strip"])!=spatial):
        raise ValueError("uniform second-source spatial derivative inputs differ")
    data=report["R82_local_inputs"]
    if data["first_coefficients"][1]is not None or data["first_coefficients"][2]is None:
        raise ValueError("missing source must be null; actual second first-integral is required")
    return report,zero


from fourfold_monotone_source_prefix import observed_prefix_ready


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--center-index",type=Path,required=True)
    p.add_argument("--uniform-index",type=Path,required=True)
    p.add_argument("--descriptor",type=Path,default=Path("data/phase_ring_continuation/step5_retargeted_reference/descriptor.json"))
    p.add_argument("--directory",type=Path,required=True)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--follow",action="store_true");p.add_argument("--wait-seconds",type=float,default=15)
    p.add_argument("--stop-file",type=Path)
    args=p.parse_args()
    if not 0<args.wait_seconds<=60:raise ValueError("wait interval must lie in (0,60]")
    ctx.prec=args.bits
    descriptor=read(args.descriptor);descriptor_sha=sha(args.descriptor)
    center=Fraction(descriptor["target_exact_delta_fraction"])
    gridmeta=descriptor["old_forward_reference"]
    if sha(gridmeta["path"])!=gridmeta["sha256"]:raise ValueError("reference grid changed")
    grid=read(gridmeta["path"])
    if grid["segment_count"]!=550:raise ValueError("expected exactly 550 base segments")
    args.directory.mkdir(parents=True,exist_ok=True)
    C=[[acb(0)] for _ in range(3)];D=[[acb(0)] for _ in range(3)]
    A=[[arb(0)for _ in range(3)]for _ in range(3)]
    E=[[arb(0)for _ in range(3)]for _ in range(3)]
    finite=[[arb(0)for _ in range(3)]for _ in range(3)]
    central=[[arb(0)for _ in range(3)]for _ in range(2)]
    central_errors=[[arb(0)for _ in range(3)]for _ in range(2)]
    outer_A=[arb(0)for _ in range(3)];outer_E=[arb(0)for _ in range(3)]
    local=[arb(0)for _ in range(3)]
    processed,evidence,prefix_replays=[],[],[];scope=None;completed_segments=0
    last=Time(Fraction(0),Fraction(-1,2));tic,cpu=time.monotonic(),time.process_time()
    dependencies={name:sha(Path(__file__).with_name(name))for name in (
        "fourfold_parameter_density_accumulate.py","fourfold_parameter_ordered_defect.py",
        "fourfold_parameter_spatial_norms.py","fourfold_phase_domain_cover_verify.py",
        "fourfold_monotone_source_prefix.py")}
    while True:
        ci,csha=read_snapshot(args.center_index);ui,usha=read_snapshot(args.uniform_index)
        eta=Fraction(ui["uniform_parameter_half_width"])
        S,inner,spatial=map(Fraction,(ui["label_strip"],ui["inner_strip"],ui["spatial_strip"]))
        proposed=(eta,S,inner,spatial)
        if (eta<=0 or Fraction(ci["uniform_parameter_half_width"])!=0
            or not ui["whole_real_parameter_tube"] or ci["whole_real_parameter_tube"]
            or ci["descriptor_sha256"]!=descriptor_sha or ui["descriptor_sha256"]!=descriptor_sha
            or any(Fraction(ci[name])!=value for name,value in (("label_strip",S),("inner_strip",inner),("spatial_strip",spatial)))
            or not 0<=inner<spatial<S or scope is not None and proposed!=scope):
            raise ValueError("hybrid source parameter or strip scopes differ")
        scope=proposed
        count=min(len(ci["leaves"]),len(ui["leaves"]))
        pairs=list(zip(ci["leaves"][:count],ui["leaves"][:count]))
        if not observed_prefix_ready(pairs,processed,
                complete=bool(ci.get("complete")and ui.get("complete"))):
            witness=dict(center_index_sha256=csha,uniform_index_sha256=usha,
                observed_pairs=len(pairs),retained_pairs=len(processed),
                all_overlapping_entries_identical=True,
                no_new_integral_or_certificate_published=True)
            if not prefix_replays or prefix_replays[-1]!=witness:
                prefix_replays.append(witness)
            if not args.follow or args.stop_file and args.stop_file.exists():return
            time.sleep(args.wait_seconds)
            continue
        added=False
        for centry,uentry in pairs[len(processed):]:
            if key(centry)!=key(uentry)or centry["g0_report_sha256"]!=uentry["g0_report_sha256"]:
                raise ValueError("central and uniform leaves have different partitions or g0 witnesses")
            cr,zero=check_leaf(centry,descriptor_sha,center,Fraction(0),S,inner,spatial)
            ur,uzero=check_leaf(uentry,descriptor_sha,center,eta,S,inner,spatial)
            if cr["identity"]["reference"]!=ur["identity"]["reference"]:
                raise ValueError("hybrid finite references differ")
            cdata,udata=cr["R82_local_inputs"],ur["R82_local_inputs"]
            if cdata["first_coefficients"][0]!=udata["first_coefficients"][0]:
                raise ValueError("the finite central zero-order first integrals differ")
            segment,left,right=key(centry)
            ta,tb=map(Time.parse,grid["exact_time_endpoints"][segment:segment+2])
            begin,end=ta+(tb-ta).scale(left),ta+(tb-ta).scale(right)
            if begin!=last:raise ValueError("hybrid chronology has a gap or overlap")
            first=[[decode_ball(z)for z in row]for row in (
                cdata["first_coefficients"][0],cdata["first_coefficients"][1],udata["first_coefficients"][2])]
            # Only center 2J11 is retained; uniform 2J11 is a different finite
            # polynomial and must not enter this hybrid approximation.
            second=[[decode_ball(z)for z in row]for row in cdata["retained_local_second_coefficients"]]
            if any(len(row)!=1 or row[0]!=acb(0)for row in second[:2]):
                raise ValueError("expected center's sole retained local term to be 2J11")
            C,D=advance_parameter_integrals(C,D,first,second)
            local_fees=[upper(cdata["remaining_local_J0_J1_J2_fees"][0]),
                        upper(cdata["remaining_local_J0_J1_J2_fees"][1]),
                        upper(udata["remaining_local_J0_J1_J2_fees"][2])]
            for j,v in enumerate(local_fees):local[j]+=v
            f0,e0,a0,g0witness=center_zero_spatial(zero,spatial)
            center1=cr["density"][0]["complete_spatial_jet_inputs"]
            uniform_item2=next(item for item in ur["density"]if item["parameter_order"]==2)
            uniform2=uniform_item2["complete_spatial_jet_inputs"]
            b0=list(map(upper,center1["true_integrated_spatial_derivative_SUP_moduli"]))
            eb0=list(map(upper,center1["actual_error_derivative_fees"]))
            cbox=list(map(upper,uniform2["true_integrated_spatial_derivative_SUP_moduli"]))
            ecbox=list(map(upper,uniform2["actual_error_derivative_fees"]))
            eta_ball=exact_arb(eta)
            btransfer=[(eta_ball*v).upper()for v in cbox]
            bbox=[(a+b).upper()for a,b in zip(b0,btransfer)]
            ebbox=[(a+b).upper()for a,b in zip(eb0,btransfer)]
            atransfer=[(eta_ball*v).upper()for v in bbox]
            abox=[(a+b).upper()for a,b in zip(a0,atransfer)]
            eabox=[(a+b).upper()for a,b in zip(e0,atransfer)]
            common=[abox,bbox,cbox];errors=[eabox,ebbox,ecbox]
            fin=[f0,list(map(upper,center1["finite_integrated_spatial_derivative_moduli"])),
                    list(map(upper,uniform2["finite_integrated_spatial_derivative_moduli"]))]
            for order in range(3):
                for j in range(3):
                    A[order][j]+=common[order][j];E[order][j]+=errors[order][j]
                    finite[order][j]+=fin[order][j]
            for order,(av,ev)in enumerate(((a0,e0),(b0,eb0))):
                for j in range(3):central[order][j]+=av[j];central_errors[order][j]+=ev[j]
            cS=upper(uniform_item2["true_integrated_modulus"])
            bS=(upper(cr["density"][0]["true_integrated_modulus"])+eta_ball*cS).upper()
            aS=(upper(zero["R72_inputs"]["common_integrated_majorant_A"])+eta_ball*bS).upper()
            eS=[(upper(zero["R72_inputs"]["integrated_approximation_error_E"])+eta_ball*bS).upper(),
                (upper(cr["density"][0]["true_integrated_error"])+eta_ball*cS).upper(),
                upper(uniform_item2["true_integrated_error"])]
            for j,v in enumerate((aS,bS,cS)):outer_A[j]+=v
            for j,v in enumerate(eS):outer_E[j]+=v
            evidence.append(dict(segment=segment,normalized_subspan=[str(left),str(right)],
                center_parameter_report=dict(path=centry["path"],sha256=centry["sha256"]),
                uniform_parameter_report=dict(path=uentry["path"],sha256=uentry["sha256"]),
                same_g0_sha256=centry["g0_report_sha256"],center_g0_spatial=g0witness,
                first_parameter_MVT_fees=records(btransfer),zero_parameter_MVT_fees=records(atransfer),
                omitted_local_fees=records(local_fees)))
            processed.append((centry,uentry));last=end;completed_segments=segment+int(right==1);added=True
        whole=bool(ci.get("complete")and ui.get("complete")and ci.get("whole_forward_leg")
            and ui.get("whole_forward_leg")and completed_segments==550
            and last==Time(Fraction(0),Fraction(1,2)))
        if added or whole:
            identity=dict(retarget_descriptor_sha256=descriptor_sha,target_exact_delta_fraction=str(center),
                exact_parameter_half_width=str(eta),exact_parameter_interval=list(map(str,(center-eta,center+eta))),
                fixed_reference_independent_of_parameter=True,whole_real_parameter_tube=True,
                approximation_sources=["center ghat0","center ghat1","uniform ghat2"],
                label_strip=str(S),inner_strip=str(inner),spatial_strip=str(spatial),
                exact_begin=dict(rational="0",pi_coefficient="-1/2"),
                exact_end=dict(rational=str(last.q),pi_coefficient=str(last.p)))
            coeffpath=args.directory/"coefficients.json.gz"
            save(coeffpath,dict(kind="hybrid_complete_finite_parameter_chronological_coefficients",identity=identity,
                C=[[encode_ball(z)for z in row]for row in C],D=[[encode_ball(z)for z in row]for row in D],
                all_product_frequencies_retained=True,normalized_label_frequency_k=True,
                no_extra_physical_factor_four=True))
            total=[add_rows(a,b)for a,b in zip(C,D)]
            norms=[[row_norms(row,exact_arb(inner))[0]for row in rows]for rows in(C,D,total)]
            report=dict(kind="actual_hybrid_parameter_chronological_prefix",proved=True,complete=whole,
                whole_forward_leg=whole,source_sha256=sha(__file__),dependency_sha256=dependencies,
                identity=identity,center_index_snapshot=dict(path=str(args.center_index),sha256=csha),
                uniform_index_snapshot=dict(path=str(args.uniform_index),sha256=usha),
                completed_segments=completed_segments,completed_leaves=len(processed),
                coefficients=dict(path=str(coeffpath),sha256=sha(coeffpath),bytes=coeffpath.stat().st_size,
                    C_positive_counts=list(map(len,C)),D_positive_counts=list(map(len,D))),
                signed_zero_modes_C=[encode_ball(row[0])for row in C],
                signed_zero_modes_D=[encode_ball(row[0])for row in D],
                finite_C_D_and_sum_A_inner_norms=[records(row)for row in norms],
                omitted_local_integral_fees_A_inner=records(local),
                outer_integrated_common_source_sup_moduli=records(outer_A),
                outer_integrated_source_approximation_sup_errors=records(outer_E),
                spatial_integrated_common_source_sup_moduli_by_parameter_order=[records(row)for row in A],
                spatial_integrated_source_approximation_sup_errors_by_parameter_order=[records(row)for row in E],
                spatial_integrated_finite_source_sup_majorants_by_parameter_order=[records(row)for row in finite],
                central_g0_g1_integrated_common_spatial_sup_moduli=[records(row)for row in central],
                central_g0_g1_integrated_spatial_error_fees=[records(row)for row in central_errors],
                real_parameter_transfer=dict(proved=True,orders=[0,1,2],
                    first_source_fees=records([(exact_arb(eta)*v).upper()for v in A[2]]),
                    zero_source_fees=records([(exact_arb(eta)*v).upper()for v in A[1]]),
                    first_formula="B_j(I),E1_j(I) <= respective central quantity + eta*C_j(I)",
                    zero_formula="A_j(I),E0_j(I) <= respective central quantity + eta*B_j(I)",
                    only_real_parameter_mean_value_used=True,no_third_parameter_derivative_used=True),
                source_error_contract="integrated SUP on the stated strip; no same-width Wiener error promotion",
                every_center_local_2J11_retained=True,uniform_local_2J11_not_used=True,
                all_cross_segment_g1_g1_and_g0_g2_terms_retained=True,
                compatible_controller_prefix_replays=prefix_replays,
                leaves=evidence,wall_seconds=time.monotonic()-tic,cpu_seconds=time.process_time()-cpu,
                limitations=["The exact prefix is not the whole forward leg until complete=true.",
                    "All listed omitted-local fees and R86 true-flow/source errors remain payable.",
                    "No endpoint composition, twist, or KAM acceptance is asserted."])
            save(args.directory/"report.json.gz",report)
            print(dict(stage="hybrid_parameter_accumulator",complete=whole,segments=completed_segments,
                leaves=len(processed),C1_zero=str(C[1][0]),D2_zero=str(D[2][0]),
                report_sha256=sha(args.directory/"report.json.gz")),flush=True)
        if whole or not args.follow or args.stop_file and args.stop_file.exists():return
        time.sleep(args.wait_seconds)


if __name__=="__main__":main()

