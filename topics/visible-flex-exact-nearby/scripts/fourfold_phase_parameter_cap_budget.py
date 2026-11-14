#!/usr/bin/env python3
"""Actual fp quadratic and fpp linear germ-cap fees at the central parameter.

The true parameter derivatives are taken at fixed physical tau. Moving
radial knots therefore reduce the threefold zero of f differences to a
twofold zero for fp and a onefold zero for fpp. The reference is substituted
only on real time after the fixed-theta analytic quotient has been bounded.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_phase_parameter_time_circle import ParameterTimeCircleField
from fourfold_phase_real_time_cap_budget import real_time_reference_cap
from fourfold_phase_germ_cap_budget import leaf_budget
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_phase_fixed_tau_parameter_bounds import sha, read, save
from fourfold_phase_beta_interval import ball_record


def lower(row):
    return arb(row["lower"]).lower()


def upper(row):
    return arb(row["upper"]).upper()


def exact_fraction(value):
    if not value.is_exact():
        raise ValueError("exact actual time radius required")
    m,e=value.man_exp()
    return Fraction(int(m))*Fraction(2)**int(e)


def parameter_real_time_caps(models, reference, image_gate, q_gate):
    """models[j] must be the actual parameter source on domain germ j."""
    if not models:
        raise ValueError("all true parameter germs are required")
    doc=models[0].base.domain
    if len(models)!=len(doc["germs"]):
        raise ValueError("an adjacent parameter germ is missing")
    domain_sha=sha(models[0].base.domain_path)
    for j,model in enumerate(models):
        if (sha(model.base.domain_path)!=domain_sha
            or model.cell!=tuple(map(Fraction,doc["germs"][j]["common_span"]))
            or not model.moduli["proved"]):
            raise ValueError("parameter source and actual ordered germ identities differ")
        if model.base.turn and len(models)>1:
            raise ValueError("ordinary matching is never extrapolated across a turning root")
    R=min(model.outer for model in models)
    restricted=dict(doc,time_radius=str(exact_fraction(R)))
    geometry=leaf_budget(restricted,models[0].root)
    main=models[geometry["main_germ_index"]]
    # This verifies object, exact PiTime coordinates, all C4/C5 scalars,
    # and the complete fixed reference q/image gates, without reusing its
    # cubic numerical fee for either of the parameter sources.
    witness=real_time_reference_cap(main.base,reference,image_gate,q_gate)
    q=lower(q_gate["full_real_time_q_real_lower"])
    orders=[]
    for order,name in ((1,"fp"),(2,"fpp")):
        zero_order=3-order
        total,supremum=arb(0),arb(0);pairs=[]
        for pair in geometry["pairs"]:
            ia,ib=pair["first_germ_index"],pair["second_germ_index"]
            length=upper(pair["possible_cap_length_upper"])
            radius=lower(pair["centered_analytic_radius_lower"])
            h=upper(pair["absolute_time_halfwidth_upper"])
            M=(upper(models[ia].moduli[name])+upper(models[ib].moduli[name])).upper()
            if not 0<=length<radius or not q>0:
                raise ValueError("parameter cap does not fit its paid actual domain")
            fee=(h*M*length**(zero_order+1)/((zero_order+1)*radius**zero_order*q)).upper()
            amplitude=(h*M*length**zero_order/(radius**zero_order*q)).upper()
            total=(total+fee).upper();supremum=(supremum+amplitude).upper()
            pairs.append(dict(first_germ_index=ia,second_germ_index=ib,
                exact_shared_radial_knot=pair["exact_shared_radial_knot"],
                actual_crossing_tau=pair["actual_crossing_tau"],actual_crossing_u=pair["actual_crossing_u"],
                possible_cap_length_upper=ball_record(length),
                centered_analytic_radius_lower=ball_record(radius),
                sum_true_parameter_source_moduli=ball_record(M),
                zero_order=zero_order,
                integrated_density_cap_error_upper=ball_record(fee),
                uniform_density_cap_error_upper=ball_record(amplitude)))
        orders.append(dict(actual_parameter_order=order,zero_order=zero_order,
            integrated_density_cap_error_upper=ball_record(total),
            uniform_density_cap_error_upper=ball_record(supremum),pairs=pairs))
    return dict(complete=True,actual_parameter_cap_errors_proved=True,
        source_sha256=sha(__file__),domain_path=str(main.base.domain_path),domain_sha256=domain_sha,
        exact_center_parameter=doc["exact_delta_fraction"],center_parameter_only=True,
        common_time_radius=str(exact_fraction(R)),physical_theta_strip=doc["physical_theta_strip"],
        main_germ_index=geometry["main_germ_index"],
        main_germ_common_span=geometry["main_germ_common_span"],
        exact_time_endpoints=doc["exact_time_endpoints"],
        initial_label_strip=image_gate["initial_label_strip"],
        actual_reference_image_upper=image_gate["physical_theta_image_strip"],
        actual_reference_q_lower=ball_record(q),reference_identity=reference.identity,
        reference_witness=witness["reference_witness"],
        parameter_sources=[model.identity() for model in models],orders=orders,
        h_and_inverse_q_included_once=True,reference_complex_time_image_not_required=True,
        limitations=["These are only the ordinary crossing caps of this actual leaf.",
            "Add each cap allowance both to its Ei and to the corresponding common Mi/Ai.",
            "The main-germ parameter density approximation and all flow errors are separate."])


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path("data/phase_ring_continuation")
    p.add_argument("--descriptor",type=Path,default=base/"step5_retargeted_reference/descriptor.json")
    p.add_argument("--domain",type=Path,required=True)
    p.add_argument("--reference-gates",type=Path,required=True)
    p.add_argument("--local-root-jets",type=Path,default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json")
    p.add_argument("--label-strip",type=Fraction,default=Fraction(1,256))
    p.add_argument("--primitive-nodes",type=int,default=512)
    p.add_argument("--root-nodes",type=int,default=1024)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec,ctx.cap=args.bits,7
    started,cpu=time.monotonic(),time.process_time()
    doc,gates=read(args.domain),read(args.reference_gates)
    if not gates["complete"] or gates["descriptor_sha256"]!=sha(args.descriptor):
        raise ValueError("complete same-descriptor reference gates required")
    image=next(g for g in gates["image_gates"] if Fraction(g["initial_label_strip"])==args.label_strip)
    q=next(g for g in gates["q_gates"] if Fraction(g["initial_label_strip"])==args.label_strip)
    models=[ParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
        nodes=args.primitive_nodes,root_nodes=args.root_nodes,germ=j)
        for j in range(len(doc["germs"]))]
    l,r=map(Fraction,doc["normalized_subspan"])
    reference=CompleteReferenceSegment(RetargetReference(args.descriptor),doc["leg"],doc["segment"],l,r)
    result=parameter_real_time_caps(models,reference,image,q)
    result.update(reference_gates_sha256=sha(args.reference_gates),
        wall_seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu)
    save(args.out,result)
    print(dict(complete=True,orders=[(row["actual_parameter_order"],
        row["integrated_density_cap_error_upper"]["upper"])for row in result["orders"]],
        sha256=sha(args.out)),flush=True)


if __name__=="__main__":
    main()
