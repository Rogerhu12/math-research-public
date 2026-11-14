#!/usr/bin/env python3
"""Complete actual parameter density on a true closed leaf, including caps.

Supports central signed sources and an entire explicitly paid real parameter
box. The same g0 first integral and time-row norms are reused; the complete
2*J(g1,g1) polynomial is retained, with only the tiny g0 mixtures paid by norm.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import time
import traceback

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_parameter_time_circle import ParameterTimeCircleField
from fourfold_phase_uniform_parameter_time_circle import UniformParameterTimeCircleField
from fourfold_phase_parameter_cap_uniform import complete_parameter_caps
from fourfold_parameter_local_integrals import parameter_local_from_g0_norms
from fourfold_joint_dft_l2_noise import joint_circle_midpoint_l2, joint_retained_rectangle_error
from fourfold_parameter_spatial_norms import parameter_spatial_rows
from fourfold_phase_unified_scalar_time_circle import exact_time
from fourfold_forward_density_pipeline_Q1024_v3 import (
    choose_fourier, adaptive_layout, full_coefficients, coefficient_digest,
    preserve_rows, compress_rectangle, coefficient_norms, records,
    save, encode_ball, decode_ball, upper, lower,
)
from fourfold_phase_actual_field_fourier_package import decode_complex
from fourfold_phase_time_circle_field_package import combined_budget
from fourfold_actual_reference_density import density_budget, finite_field_modulus
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_exact_fourier_multipoint import time_coefficients
from fourfold_fourier_local_taylor import finite_taylor_evaluate
from fourfold_parameter_ordered_defect import first_and_local_parameter_bounds
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import sha
from fourfold_saved_circle_field_multidomain_budget import read


def joint_circle(sampler, N, Nt, m, rho, callback):
    if Nt < 2 or Nt % 2 or not 0 < m <= Nt:
        raise ValueError("invalid time DFT dimensions")
    values = np.empty((Nt, N, 2), object)
    for j in range(Nt//2+1):
        u = acb(rho) if j == 0 else (acb(-rho) if j == Nt//2
             else rho*acb(0, 2*arb.pi()*j/Nt).exp())
        sampled, timing = sampler(u, N)
        if sampled.shape != (N, 2) or any(not z.is_finite() for z in sampled.flat):
            raise ValueError("invalid complete parameter sample array")
        values[j] = sampled
        if 0 < j < Nt//2:
            for k in range(N):
                for order in range(2):
                    values[Nt-j, k, order] = sampled[k, order].conjugate()
        callback(dict(time_node=j, **timing))
    result = np.empty((2, m, N), object)
    for order in range(2):
        for j in range(N):
            transformed = acb.dft(list(values[:, j, order]))
            for i in range(m):
                result[order, i, j] = transformed[i]/(Nt*rho**i)
    return result


def load_positive_rectangle(path):
    path = Path(path); doc = read(path)
    if not (doc.get("complete") and doc.get("exactly_reloaded")
            and doc["kind"] == "exact_positive_real_time_Fourier_rectangle"
            and doc["frequency_scale"] == 1):
        raise ValueError("complete exact normalized-label rectangle required")
    rows = []; offset = 0
    for item in doc["shards"]:
        file = path.parent/item["path"]
        if sha(file) != item["sha256"] or file.stat().st_size != item["bytes"]:
            raise ValueError("complete g0 density shard identity changed")
        part = read(file)
        if part["identity"] != doc["identity"] or part["time_start"] != offset:
            raise ValueError("g0 density time partition or identity changed")
        rows.extend([[decode_complex(v) for v in row] for row in part["coefficients"]])
        offset = part["time_stop"]
    if (offset != doc["time_terms"] or any(len(row) != doc["Fourier_degree"]+1 for row in rows)
        or coefficient_digest(rows, 1) != doc["coefficient_sha256"]):
        raise ValueError("incomplete exact g0 rectangle")
    return doc, rows


def run(args):
    ctx.prec, ctx.cap = args.bits, 7
    started, cpu = time.monotonic(), time.process_time()
    old = read(args.reference_certificate)
    frozen_pipeline = args.reference_source
    if not (old.get("complete") and old.get("complete_continuous_true_density_proved")
            and old["source_sha256"] == sha(frozen_pipeline)):
        raise ValueError("the reused reference gates need the completed frozen g0 pipeline")
    doc=read(args.domain)
    uniform=bool(args.uniform_half_width)
    models=[]
    for j in range(len(doc["germs"])):
        options=dict(nodes=args.primitive_nodes,root_nodes=args.root_nodes,
                     outer=args.outer,germ=j,radial_degree=args.radial_degree)
        if uniform:
            model=UniformParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
                args.wide_root_jets,half_width=args.uniform_half_width,**options)
        else:
            model=ParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,**options)
        models.append(model)
    source=models[0]
    sl, sr = map(Fraction, doc["normalized_subspan"])
    ref = CompleteReferenceSegment(RetargetReference(args.descriptor), doc["leg"], doc["segment"], sl, sr)
    if ref.identity != old["identity"]["reference"]:
        raise ValueError("reused complete reference gates belong to another exact reference")
    if source.base.time_endpoints != tuple(map(exact_time, old["identity"]["exact_time_endpoints"])):
        raise ValueError("physical source and reference times differ")
    S, sigma = Fraction(args.label_strip), Fraction(args.inner_strip)
    if Fraction(old["label_strip"]) != S or Fraction(old["inner_strip"]) != sigma:
        raise ValueError("parameter and zero-order densities need the same working/inner strips")
    s, inner, rho = exact_arb(S), exact_arb(sigma), exact_arb(args.circle_radius)
    target = arb(args.target)
    real = old["real_reference_gate"]
    image_gate, q_gate = real["image"], real["q"]
    if (not image_gate["complete_real_time_image_proved"]
        or not q_gate["q_nonzero_on_complete_real_time_label_strip_proved"]
        ) :
        raise ValueError("complete same-reference real-time gates required")
    caps=complete_parameter_caps(models,ref,image_gate,q_gate)
    source=models[caps["main_germ_index"]]
    image, qreal = upper(image_gate["physical_theta_image_strip"]), lower(q_gate["full_real_time_q_real_lower"])
    ps_fraction = Fraction(real["physical_approximation_strip"]); ps = exact_arb(ps_fraction)
    if not 0 < qreal or not image < ps < source.strip:
        raise ValueError("real-time reference image does not fit actual parameter field domain")
    accepted = [g for g in old["reference_outer_gates"]
                if g["q_nonzero_on_complete_bidisk_proved"]
                and Fraction(g["time_radius"]) > max(Fraction(1), args.circle_radius)
                and Fraction(g["initial_label_strip"]) > S]
    if not accepted:
        raise ValueError("no complete finite-reference proxy bidisk")
    identity = dict(reference=ref.identity, actual_parameter_source=source.identity(),
                    center_parameter_only=not uniform,whole_real_parameter_tube=uniform,
                    exact_parameter_interval=list(map(str,source.target.parameter_interval)),
                    fixed_reference_independent_of_parameter=True)
    report = dict(kind="actual_parameter_density_on_one_closed_covered_leaf",
        complete=False, source_sha256=sha(__file__), identity=identity,
        reference_certificate_path=str(args.reference_certificate),
        reference_certificate_sha256=sha(args.reference_certificate),
        domain_path=str(args.domain), domain_sha256=sha(args.domain),
        label_strip=str(S), inner_strip=str(sigma), bits=args.bits,
        target_uniform_density_error=args.target,spatial_derivative_strip=str(args.spatial_strip),
        full_error_contract="integral real-time SUP error on the complete source label strip; no same-width A error is claimed for true source composition",
        joint_nodal_error_method="exact dyadic nodes + normalized 2D Parseval + full retained-rectangle weighted Cauchy-Schwarz",
        parameter_orders=[1, 2], actual_parameter_factorials_removed=True,
        source_definition=["g1=h*fp(u,Y)/Yx", "g2=h*fpp(u,Y)/Yx"],
        real_reference_gate=real, accepted_reference_proxy_gates=accepted,
        parameter_cap_ledger=caps,reference_source_path=str(frozen_pipeline),
        reference_source_sha256=sha(frozen_pipeline),
        samples=dict(field=[], density=[]), field=[], density=[],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_parameter_time_circle.py", "fourfold_forward_density_pipeline_Q1024_v3.py",
            "fourfold_phase_time_circle_field_package.py", "fourfold_actual_reference_density.py",
            "fourfold_fourier_local_taylor.py", "fourfold_parameter_ordered_defect.py",
            "fourfold_phase_uniform_parameter_time_circle.py","fourfold_phase_parameter_cap_uniform.py",
            "fourfold_parameter_local_integrals.py","fourfold_joint_dft_l2_noise.py",
            "fourfold_parameter_spatial_norms.py")})
    def checkpoint():
        save(args.out, report)
    def progress(stage, **kw):
        print(json.dumps(dict(stage=stage, segment=doc["segment"], **kw)), flush=True)
    checkpoint()
    try:
        field_target = (target*qreal/(8*abs(source.h))).lower()
        moduli = [upper(source.moduli[name]) for name in ("fp", "fpp")]
        field_rms=[arb(0),arb(0)]
        def fbudget(order, N, K, Nt, m, errors):
            result=combined_budget(N, K, source.strip, ps, 1, errors,
                [(source.outer, moduli[order])], args.circle_radius, Nt, 0)
            charge=joint_retained_rectangle_error(field_rms[order],m,K,rho,ps,frequency_scale=4)
            result["joint_nodal_RMS_error"]=charge
            result["total"]=(result["total"]+charge).upper()
            return result
        max_order = max(range(2), key=lambda j:moduli[j])
        layout, attempts = adaptive_layout(
            lambda N,K,Nt,m,errors:fbudget(max_order,N,K,Nt,m,errors),
            N=max(512,args.primitive_nodes), K=64, Nt=16, m=12,
            target=field_target, max_degree=args.max_degree, max_terms=args.max_terms)
        N,K,Nt,m = layout
        report["field_layout"] = dict(nodes=N, degree=K, time_nodes=Nt, terms=m,
                                      adaptation=attempts, target=ball_record(field_target))
        checkpoint(); progress("parameter_field_sampling", N=N, K=K, Nt=Nt, m=m)
        def field_sample(u, count):
            values, timing = source.sample(u, count)
            return values[:, 1:3], timing
        def callback(timing):
            report["samples"]["field"].append(timing); checkpoint()
            if timing["time_node"] % 8 == 0: progress("field_node", node=timing["time_node"])
        nodes,field_rms=joint_circle_midpoint_l2(field_sample,N,Nt,m,rho,callback,bits=args.coefficient_bits)
        report["field_joint_nodal_RMS"]=list(map(ball_record,field_rms))
        checkpoint()
        fields=[]; field_fees=[]
        for order in range(2):
            rows, errors, fees = choose_fourier(nodes[order], K, args.coefficient_bits)
            actual = fbudget(order,N,K,Nt,m,errors)
            if not actual["total"] <= field_target:
                report["failed_actual_field_budget"]=dict(parameter_order=order+1,
                    budget=records(actual),target=ball_record(field_target),
                    joint_nodal_RMS=list(map(ball_record,field_rms)))
                checkpoint()
                raise ValueError("actual parameter source node fees exceed selected target")
            allowance=min(field_target/4,(field_target-actual["total"]).lower()/2)
            rows, charge, compression=compress_rectangle(rows,ps,4,allowance)
            actual["finite_rectangle_compression"]=charge
            actual["total"]=(actual["total"]+charge).upper()
            item=dict(parameter_order=order+1,error_budget=records(actual),coefficient_fees=fees,
                compression=compression,coefficient_sha256=coefficient_digest(rows,4))
            item["exact_rectangle"]=preserve_rows(args.directory/("field_p"+str(order+1)),rows,
                dict(identity=identity,parameter_order=order+1),4)
            fields.append(full_coefficients(rows))
            field_fees.append((abs(ref.h)*actual["total"]/qreal).upper())
            report["field"].append(item); checkpoint()
        del nodes
        proxy_domains=[[],[]]
        for order,field in enumerate(fields):
            for gate in accepted:
                R,T=map(Fraction,(gate["time_radius"],gate["initial_label_strip"]))
                MP=finite_field_modulus(field,exact_arb(R),upper(gate["physical_theta_image_strip"]))
                Mg=(abs(ref.h)*MP/lower(gate["full_complex_time_and_label_q_real_lower"])).upper()
                proxy_domains[order].append((exact_arb(R),exact_arb(T),Mg))
        common_domains=[(a[0],a[1],max(a[2],b[2]).upper())
                        for a,b in zip(*proxy_domains)]
        density_rms=[arb(0),arb(0)]
        def dbudget(order,N,K,Nt,m,errors):
            result=density_budget(proxy_domains[order],errors,N,K,rho,Nt,s)
            charge=joint_retained_rectangle_error(density_rms[order],m,K,rho,s,frequency_scale=1)
            result["joint_nodal_RMS_error"]=ball_record(charge)
            result["total"]=ball_record((upper(result["total"])+charge).upper())
            return result
        layout, attempts=adaptive_layout(
            lambda N,K,Nt,m,errors:density_budget(common_domains,errors,N,K,rho,Nt,s),
            N=512,K=128,Nt=16,m=12,target=target/2,
            max_degree=args.max_degree,max_terms=args.max_terms)
        N,K,Nt,m=layout
        report["density_layout"]=dict(nodes=N,degree=K,time_nodes=Nt,terms=m,adaptation=attempts)
        report["finite_proxy_domains"]=[
            [dict(time_radius=ball_record(R),label_strip=ball_record(T),modulus=ball_record(M))
             for R,T,M in dom] for dom in proxy_domains]
        checkpoint();progress("parameter_density_sampling",N=N,K=K,Nt=Nt,m=m)
        def density_sample(u,count):
            wall,cpu=time.monotonic(),time.process_time()
            Y,_,q=ref.grid(u,count,Fraction(0));values=np.empty((count,2),object);details=[]
            for order,field in enumerate(fields):
                P,info=finite_taylor_evaluate(time_coefficients(field,u),Y,
                    anchors=args.anchors,radius=Fraction(1,64),tail_target=args.evaluation_tail)
                values[:,order]=[ref.h*v/denom for v,denom in zip(P,q)]
                details.append(info)
            return values,dict(finite_parameter_P_evaluation=details,
                elapsed_seconds=time.monotonic()-wall,cpu_seconds=time.process_time()-cpu)
        def callback(timing):
            report["samples"]["density"].append(timing);checkpoint()
            if timing["time_node"]%8==0:progress("density_node",node=timing["time_node"])
        nodes,density_rms=joint_circle_midpoint_l2(density_sample,N,Nt,m,rho,callback,bits=args.coefficient_bits)
        report["density_joint_nodal_RMS"]=list(map(ball_record,density_rms))
        checkpoint()
        density_rows=[]
        for order in range(2):
            rows,errors,fees=choose_fourier(nodes[order],K,args.coefficient_bits)
            actual=dbudget(order,N,K,Nt,m,errors);error=upper(actual["total"])
            if not error<=target/2:
                raise ValueError("actual finite parameter density error exceeds selected target")
            allowance=min(target/8,(target/2-error).lower()/2)
            rows,charge,compression=compress_rectangle(rows,s,1,allowance)
            error=(error+charge).upper()
            actual=dict(actual,finite_rectangle_compression=ball_record(charge),total=ball_record(error))
            total=(field_fees[order]+error).upper()
            cap=caps["orders"][order]
            integrated_total=(2*total+upper(cap["integrated_density_cap_error_upper"])).upper()
            uniform_total=(total+upper(cap["uniform_density_cap_error_upper"])).upper()
            norms,_=coefficient_norms(rows,s)
            finite_A=sum((2*v/(i+1) for i,v in enumerate(norms)),arb(0)).upper()
            item=dict(parameter_order=order+1,error_budget=actual,coefficient_fees=fees,
                compression=compression,coefficient_sha256=coefficient_digest(rows,1),
                true_field_transfer_error=ball_record(field_fees[order]),
                true_uniform_error=ball_record(uniform_total),true_integrated_error=ball_record(integrated_total),
                finite_integrated_modulus=ball_record(finite_A),
                true_integrated_modulus=ball_record(finite_A+integrated_total),
                true_uniform_modulus=ball_record(sum(norms,arb(0))+uniform_total),
                whole_real_parameter_tube=uniform,
                actual_cap_integrated_error=cap["integrated_density_cap_error_upper"],
                actual_cap_uniform_error=cap["uniform_density_cap_error_upper"])
            item["exact_rectangle"]=preserve_rows(args.directory/("density_p"+str(order+1)),rows,
                dict(identity=identity,parameter_order=order+1),1)
            item["complete_spatial_jet_inputs"]=parameter_spatial_rows(rows,integrated_total,S,args.spatial_strip)
            report["density"].append(item);density_rows.append(rows);checkpoint()
        del nodes,fields
        first,local,local_fees,local_proof=parameter_local_from_g0_norms(old,density_rows,sigma)
        report["R82_local_inputs"]=dict(
            same_g0_certificate_sha256=sha(args.reference_certificate),
            first_coefficients=[[encode_ball(z) for z in row] for row in first],
            retained_local_second_coefficients=[[encode_ball(z) for z in row] for row in local],
            remaining_local_J0_J1_J2_fees=list(map(ball_record,local_fees)),
            local_integral_proof=local_proof,
            true_parameter_density_integrated_errors=[x["true_integrated_error"] for x in report["density"]],
            true_parameter_integrated_moduli=[x["true_integrated_modulus"] for x in report["density"]],
            whole_real_parameter_tube=uniform,
            signed_first_parameter_zero_mode=encode_ball(first[1][0]),
            signed_second_parameter_zero_mode=encode_ball(first[2][0]),
            no_extra_factor_four=True,all_cross_segment_terms_still_required=True)
        if uniform:
            fee=(exact_arb(args.uniform_half_width)*upper(report["density"][0]["true_integrated_modulus"])).upper()
            report["R82_local_inputs"].update(
                g0_uniform_parameter_transfer_integrated_error=ball_record(fee),
                g0_uniform_common_A=ball_record(upper(old["R72_inputs"]["common_integrated_majorant_A"])+fee),
                g0_uniform_E0=ball_record(upper(old["R72_inputs"]["integrated_approximation_error_E"])+fee),
                g0_remains_the_same_central_finite_approximation=True)
        report.update(complete=True,complete_continuous_parameter_densities_proved=True,
            complete_continuous_signed_parameter_densities_proved=not uniform,
            complete_continuous_uniform_parameter_densities_proved=uniform,
            wall_seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu,
            limitations=["This closed actual leaf is not the complete forward leg or its squared return.",
                "The exact declared parameter scope is binding; central and uniform sources remain distinct.",
                "Only the complete finite 2J(g1,g1) is retained locally; every omitted mixture has an explicit fee.",
                "All cross-segment terms and the final endpoint/return parameter conversion remain required."])
        checkpoint();progress("complete",
            first_parameter_zero_mode=str(first[1][0]),
            second_parameter_zero_mode=str(first[2][0]),
            errors=[x["true_integrated_error"]["upper"] for x in report["density"]],
            cpu=report["cpu_seconds"],wall=report["wall_seconds"])
    except Exception as exc:
        report["failure"]=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        report["wall_seconds"]=time.monotonic()-started
        checkpoint()
        raise


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path("data/phase_ring_continuation")
    p.add_argument("--descriptor",type=Path,default=base/"step5_retargeted_reference/descriptor.json")
    p.add_argument("--domain",type=Path,default=base/"step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz")
    p.add_argument("--reference-certificate",type=Path,default=base/"step5_forward_density_pipeline_pilot419_Q1024/forward_0419_ef134f2a18.json.gz")
    p.add_argument("--local-root-jets",type=Path,default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json")
    p.add_argument("--wide-root-jets",type=Path,default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    p.add_argument("--uniform-half-width",type=Fraction,default=Fraction(0))
    p.add_argument("--reference-source",type=Path,default=Path(__file__).with_name("fourfold_forward_density_pipeline_Q1024_v3.py"))
    p.add_argument("--label-strip",default="1/256");p.add_argument("--inner-strip",default="3/1024")
    p.add_argument("--spatial-strip",type=Fraction,default=Fraction(7,2048))
    p.add_argument("--primitive-nodes",type=int,default=512);p.add_argument("--root-nodes",type=int,default=1024)
    p.add_argument("--radial-degree",type=int,default=40);p.add_argument("--outer",type=Fraction,default=Fraction(3))
    p.add_argument("--circle-radius",type=Fraction,default=Fraction(1));p.add_argument("--target",default="1e-11")
    p.add_argument("--coefficient-bits",type=int,default=160);p.add_argument("--bits",type=int,default=256)
    p.add_argument("--max-degree",type=int,default=4095);p.add_argument("--max-terms",type=int,default=128)
    p.add_argument("--anchors",type=int,default=512);p.add_argument("--evaluation-tail",default="1e-38")
    p.add_argument("--directory",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
    run(p.parse_args())


if __name__=="__main__":
    main()
