#!/usr/bin/env python3
"""R84 local parameter integrals using the same g0 row-norm witness.

Keep 2*J(g1,g1) as a complete finite Fourier polynomial.  Only the small
g0/g2 mixed terms of J2 and all g0/g1 terms of J1 are paid by norm.  No
large g0 rectangle is required or replaced by a different approximation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, acb, ctx

from fourfold_parameter_ordered_defect import (
    row_norms, derivative_product, add_rows, chronological_weight,
)
from fourfold_forward_density_pipeline_Q1024_v3 import (
    encode_ball, decode_ball, upper, save,
)
from fourfold_parameter_density_leaf import load_positive_rectangle
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb


def first_integral(rows):
    if not rows or any(len(row)!=len(rows[0]) for row in rows):
        raise ValueError("nonempty rectangular full positive-frequency rows required")
    return [sum((2*rows[i][k]/(i+1) for i in range(0,len(rows),2)),acb(0))
            for k in range(len(rows[0]))]


def exact_diagonal_local(rows, multiplier=1):
    """All modes of multiplier*integral g_x(u) integral_-1^u g(v)dv du."""
    result=[acb(0)]
    for m,left in enumerate(rows):
        for n,right in enumerate(rows):
            weight=multiplier*chronological_weight(m,n)
            if weight:
                result=add_rows(result,[exact_arb(weight)*z
                                      for z in derivative_product(left,right)])
    return result


def parameter_local_from_g0_norms(g0_report, parameter_rows, inner_width):
    if len(parameter_rows)!=2:
        raise ValueError("both first and second finite parameter densities required")
    if not g0_report.get("complete_continuous_true_density_proved"):
        raise ValueError("a complete original g0 certificate is required")
    S,sigma=Fraction(g0_report["label_strip"]),Fraction(inner_width)
    if not 0<=sigma<S or Fraction(g0_report["inner_strip"])!=sigma:
        raise ValueError("the local inner strip must match the saved g0 witness")
    first_meta=g0_report["first_integral_file"]
    if sha(first_meta["path"])!=first_meta["sha256"]:
        raise ValueError("the complete g0 first-integral file changed")
    first_doc=read(first_meta["path"])
    if first_doc["identity"]!=g0_report["identity"]:
        raise ValueError("g0 first integral has another exact reference/source")
    first0=[decode_ball(z) for z in first_doc["coefficients"]]
    first=[first0]+[first_integral(rows) for rows in parameter_rows]
    n0=[upper(v) for v in g0_report["R72_inputs"]["finite_time_coefficient_A_norms"]]
    if not n0:
        raise ValueError("all time-row A_S norms, including zero, are required")
    derivative_factor=1/(arb(1).exp()*exact_arb(S-sigma))
    norms=[n0]
    derivatives=[[v*derivative_factor for v in n0]]
    for rows in parameter_rows:
        nd=[row_norms(row,exact_arb(sigma)) for row in rows]
        norms.append([v[0] for v in nd]);derivatives.append([v[1] for v in nd])
    count=max(map(len,norms))
    for table in (norms,derivatives):
        for row in table:
            row.extend([arb(0)]*(count-len(row)))
    endpoint=[row_norms(row,exact_arb(sigma)) for row in first]
    def symmetric(i,j):
        value=(endpoint[i][1]*endpoint[j][0]+endpoint[j][1]*endpoint[i][0])/2
        for even in range(0,count,2):
            for odd in range(1,count,2):
                weight=arb(2)/((even+odd+2)*(even+1))
                value+=weight*(derivatives[i][odd]*norms[j][even]
                    +derivatives[j][odd]*norms[i][even]
                    +derivatives[i][even]*norms[j][odd]
                    +derivatives[j][even]*norms[i][odd])
        return value.upper()
    fees=[upper(g0_report["R72_inputs"]["omitted_local_second_integral_bound_on_inner_strip"]),
          symmetric(0,1),symmetric(0,2)]
    diagonal=exact_diagonal_local(parameter_rows[0],2)
    local=[[acb(0)],[acb(0)],diagonal]
    return first,local,fees,dict(
        proved=True,same_complete_g0_first_sha256=first_meta["sha256"],
        g0_row_norm_strip=str(S),inner_strip=str(sigma),
        g0_derivative_Cauchy_factor=ball_record(derivative_factor),
        complete_g0_time_rows=len(n0),complete_parameter_time_rows=list(map(len,parameter_rows)),
        retained_local_second_parameter_definition="2*integral g1_x(u) integral_-1^u g1(v)dv du",
        retained_local_second_parameter_norm=ball_record(row_norms(diagonal,exact_arb(sigma))[0]),
        remaining_local_J0_J1_J2_fees=list(map(ball_record,fees)),
        no_zero_mode_or_product_frequency_omitted=True,
        all_cross_segment_terms_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path("data/phase_ring_continuation")
    p.add_argument("--parameter-report",type=Path,default=base/"type_fixed_step02_d5_step5_parameter_density419.json.gz")
    p.add_argument("--g0-report",type=Path,default=base/"step5_forward_density_pipeline_pilot419_Q1024/forward_0419_ef134f2a18.json.gz")
    p.add_argument("--bits",type=int,default=256);p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    started,cpu=time.monotonic(),time.process_time()
    parameter,g0=read(args.parameter_report),read(args.g0_report)
    if not parameter["complete_continuous_signed_parameter_densities_proved"]:
        raise ValueError("complete continuous input densities required")
    if parameter["reference_certificate_sha256"]!=sha(args.g0_report):
        raise ValueError("parameter densities and g0 witness differ")
    rows=[]
    for item in parameter["density"]:
        meta=item["exact_rectangle"]
        if sha(meta["path"])!=meta["sha256"]:
            raise ValueError("a finite parameter rectangle manifest changed")
        _,values=load_positive_rectangle(meta["path"]);rows.append(values)
    first,local,fees,proof=parameter_local_from_g0_norms(g0,rows,parameter["inner_strip"])
    oldfirst=parameter["R82_local_inputs"]["first_coefficients"]
    for row,saved in zip(first,oldfirst):
        if len(row)!=len(saved) or any(not (a.real.overlaps(b.real) and a.imag.overlaps(b.imag))
                                      for a,b in zip(row,map(decode_ball,saved))):
            raise ValueError("the complete original signed first integrals differ")
    report=dict(kind="same_g0_norms_and_retained_parameter_diagonal_local_integral",
        complete=True,source_sha256=sha(__file__),parameter_report_sha256=sha(args.parameter_report),
        g0_report_sha256=sha(args.g0_report),identity=parameter["identity"],
        first_coefficients=[[encode_ball(z) for z in row] for row in first],
        retained_local_second_coefficients=[[encode_ball(z) for z in row] for row in local],
        remaining_local_J0_J1_J2_fees=list(map(ball_record,fees)),proof=proof,
        original_all_omitted_local_fees=parameter["R82_local_inputs"]["complete_local_J0_J1_J2_fees"],
        wall_seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu)
    save(args.out,report)
    print(dict(complete=True,sha256=sha(args.out),cpu=report["cpu_seconds"],
        wall=report["wall_seconds"],remaining_J2=str(fees[2]),
        retained_J2_norm=proof["retained_local_second_parameter_norm"]["upper"]),flush=True)


if __name__=="__main__":
    main()
