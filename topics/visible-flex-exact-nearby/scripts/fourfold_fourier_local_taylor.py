#!/usr/bin/env python3
"""Full finite Fourier evaluation using scalar FFT angular Taylor tables.

The finite polynomial may be evaluated outside the analytic domain of the
true field it approximates. Only the *finite* polynomial norm pays its local
Taylor tail; a true field approximation error is a separate input.
All finite modes are folded exactly into the uniform anchor DFT. No angular
alias or truncation is introduced by using fewer anchors than Fourier modes.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import arb, acb, acb_poly, ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_actual_field_fourier_package import load_polynomial
from fourfold_exact_fourier_multipoint import middle, time_coefficients, exact_H_nodes


def finite_taylor_evaluate(coefficients, thetas, *, anchors=1024,
                           radius=Fraction(1, 64), tail_target='1e-32',
                           maximum_terms=512):
    """Return enclosures of the full finite sum at all original angle balls.

    Coefficients are ordered -K,...,K and have physical frequency scale 4.
    Float arithmetic chooses an anchor only; a directed bound on the actual
    distance to that exact pi-grid anchor must pass before any evaluation.
    """
    tick, cpu = time.monotonic(), time.process_time()
    K = (len(coefficients)-1)//2
    if len(coefficients) != 2*K+1 or not thetas or anchors < 1:
        raise ValueError('nonempty points and symmetric Fourier array required')
    A = exact_arb(radius)
    target = arb(tail_target)
    if not A > 0 or not target > 0 or maximum_terms < 1:
        raise ValueError('positive Taylor radius, target and term limit required')
    selected = list(map(middle, coefficients))
    centers = list(map(middle, thetas))
    if not all(v.is_finite() for v in selected+centers):
        raise ValueError('all finite coefficients and input points must be finite')
    theta_error = max(abs(v-c).upper() for v,c in zip(thetas, centers))
    S = max(abs(c.imag).upper() for c in centers)
    coefficient_fee = arb(0)
    angle_fee = arb(0)
    norm_A = arb(0)
    for index, (a,b) in enumerate(zip(coefficients,selected)):
        n = 4*abs(index-K)
        coefficient_fee += abs(a-b)*(n*(S+theta_error)).exp()
        angle_fee += abs(b)*(n*S).exp()*((n*theta_error).exp()-1)
        norm_A += abs(b)*(n*A).exp()
    coefficient_fee, angle_fee, norm_A = [v.upper() for v in
                                          (coefficient_fee,angle_fee,norm_A)]
    pi = arb.pi()
    indices, offsets = [], []
    for value in centers:
        # An imperfect floating anchor selection remains valid: no closeness
        # is assumed until the exact directed radius test below succeeds.
        index = round(float(2*anchors*value.real/pi))
        anchor = index*pi/(2*anchors)
        indices.append(index % anchors)
        offsets.append((value-anchor)/A)
    ratio = max(abs(z).upper() for z in offsets)
    if not ratio < 1:
        raise ValueError('chosen exact angular anchors leave the Taylor disk')
    terms = 1
    tail = (norm_A*ratio/(1-ratio)).upper()
    while not tail <= target:
        terms += 1
        if terms > maximum_terms:
            raise ValueError('angular Taylor term limit insufficient for proved tail')
        tail = (norm_A*ratio**terms/(1-ratio)).upper()
    prep_seconds, prep_cpu = time.monotonic()-tick, time.process_time()-cpu
    tick, cpu = time.monotonic(), time.process_time()
    scale = [acb(0, 4*(k-K))*A for k in range(2*K+1)]
    current = selected
    tables = []
    for j in range(terms):
        folded = [acb(0) for _ in range(anchors)]
        for k,value in enumerate(current):
            folded[(k-K) % anchors] += value
        tables.append([anchors*v for v in acb.dft(folded, inverse=True)])
        if j+1 < terms:
            current = [value*s/(j+1) for value,s in zip(current,scale)]
    table_seconds, table_cpu = time.monotonic()-tick, time.process_time()-cpu
    tick, cpu = time.monotonic(), time.process_time()
    polynomials = {i:acb_poly([row[i] for row in tables]) for i in set(indices)}
    raw = [polynomials[i](z) for i,z in zip(indices,offsets)]
    arithmetic = max(abs(value-middle(value)).upper() for value in raw)
    fee = (coefficient_fee+angle_fee+tail).upper()
    result = [complex_pad(value,fee) for value in raw]
    evaluation_seconds, evaluation_cpu = time.monotonic()-tick, time.process_time()-cpu
    return result, dict(
        Fourier_degree=K, physical_frequency_scale=4, anchors=anchors, terms=terms,
        no_finite_modes_discarded=True, exact_DFT_folding=True,
        Taylor_radius=str(radius), Taylor_tail_target=str(tail_target),
        maximum_normalized_anchor_distance=ball_record(ratio),
        center_physical_theta_strip=ball_record(S),
        theta_input_error=ball_record(theta_error),
        coefficient_input_fee=ball_record(coefficient_fee),
        theta_input_fee=ball_record(angle_fee),
        finite_polynomial_norm_on_Taylor_radius=ball_record(norm_A),
        complete_angular_Taylor_tail=ball_record(tail),
        maximum_arithmetic_radius=ball_record(arithmetic),
        complete_finite_evaluation_error=ball_record((fee+arithmetic).upper()),
        preparation_seconds=prep_seconds, preparation_cpu_seconds=prep_cpu,
        table_seconds=table_seconds, table_cpu_seconds=table_cpu,
        evaluation_seconds=evaluation_seconds, evaluation_cpu_seconds=evaluation_cpu,
        total_seconds=prep_seconds+table_seconds+evaluation_seconds,
        total_cpu_seconds=prep_cpu+table_cpu+evaluation_cpu)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--polynomial',type=Path,default=Path('data/phase_ring_continuation/step5_reference419_main_field_polynomial/manifest.json'))
    p.add_argument('--H',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_dyadic_H.json'))
    p.add_argument('--nodes',type=int,default=8192)
    p.add_argument('--anchors',type=int,default=512)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--label-width',default='1/512')
    p.add_argument('--time-real',default='1/2');p.add_argument('--time-imag',default='1/8')
    p.add_argument('--angular-Taylor-radius',default='1/64')
    p.add_argument('--tail-target',default='1e-32')
    p.add_argument('--out',type=Path,required=True)
    args = p.parse_args();ctx.prec=args.bits
    tick,cpu = time.monotonic(),time.process_time()
    manifest,coefficients = load_polynomial(args.polynomial)
    u = acb(exact_arb(Fraction(args.time_real)),exact_arb(Fraction(args.time_imag)))
    row = time_coefficients(coefficients,u)
    thetas = exact_H_nodes(args.H,args.nodes,Fraction(args.label_width))
    preparation = dict(seconds=time.monotonic()-tick,cpu_seconds=time.process_time()-cpu)
    values,info = finite_taylor_evaluate(row,thetas,anchors=args.anchors,
        radius=Fraction(args.angular_Taylor_radius),tail_target=args.tail_target)
    K = (len(row)-1)//2
    checks = []
    for j in sorted({0,args.nodes//7,args.nodes//3,args.nodes-1}):
        direct = sum((a*(acb(0,4*(k-K))*thetas[j]).exp()
                      for k,a in enumerate(row)),acb(0))
        if not (values[j].real.overlaps(direct.real) and values[j].imag.overlaps(direct.imag)):
            raise ValueError('angular Taylor enclosure fails independent full Laurent sum')
        checks.append(dict(node=j,independent_full_finite_sum_overlaps=True,
                           direct_sum=repr(direct),Taylor_value=repr(values[j])))
    report = dict(kind='exact_saved_field_native_FFT_local_angular_Taylor_evaluation',
        complete=True,source_sha256=sha(__file__),bits=args.bits,
        polynomial_manifest_sha256=sha(args.polynomial),field_identity=manifest['identity'],
        H_sha256=sha(args.H),input_map='saved exact delta5 H(x)/4',nodes=args.nodes,
        label_imaginary=args.label_width,time_real=args.time_real,time_imaginary=args.time_imag,
        preparation=preparation,evaluation=info,independent_checks=checks,
        complete_error_below_1e_minus_28=arb(info['complete_finite_evaluation_error']['upper'])<arb('1e-28'),
        limitations=['Full finite P is enclosed, including all retained saved modes.',
                     'The actual field error f-P must be paid separately on its proved domain.',
                     'Input H/4 is not the trajectory Y at segment419; no residual or full flow is asserted.',
                     'This benchmark is finite-node only, not a full initial-label continuum certificate.'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(complete=True,nodes=args.nodes,**info)),flush=True)


if __name__=='__main__':main()
