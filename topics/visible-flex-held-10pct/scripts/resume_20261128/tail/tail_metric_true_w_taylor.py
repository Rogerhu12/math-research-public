#!/usr/bin/env python3
"""Certify unchanged actual tail spans with a true-background linear Taylor model.

Only the proof enclosure changes. Saved full Fourier/quintic coefficients,
all original cumulative means and their common two-jets remain unchanged.
The original constant-w Gram formula is retained with its two linear w terms
replaced by polynomial products; all high quadratic products remain bounded.
A C1 w with bounded piecewise w_RR has the integral Taylor remainder used here.
One-sided hulls include original absolute-value cusps and source joins.
"""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import sys
import time

SCRIPTS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SCRIPTS/'resume_20261126'))
sys.path.insert(0, str(SCRIPTS/'resume_n4'))
import seam_certify_tail_geometry_v2 as original
import certify_q060_shared_r_tail_batch as kernel
from q060_true_background_oracle import Q060TrueBackgroundOracle, mpf_fraction

lib, product = kernel.lib, kernel.product
GATE = Q(1, 10**6)
ORIGINAL_KERNEL_SHA = 'c646bd4a918aa467212870d437718f22451903a0141242fa5ebf3166ba376aac'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def write(path, value):
    tmp = path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    tmp.replace(path)


def outward_float(value, upward):
    f = float(value)
    if (Q.from_float(f) < value) if upward else (Q.from_float(f) > value):
        f = math.nextafter(f, math.inf if upward else -math.inf)
    return f


def compose_affine(poly, left, width):
    result = [Q(0)]
    for coefficient in reversed(poly):
        result = lib.add(product(result, [left, width]), [coefficient])
    return result


def restricted_span(parent, left, right, pm, hm):
    if not 0 <= left < right <= 1:
        raise ValueError('Invalid exact proof subinterval')
    deriv = [[compose_affine(p, left, right-left) for p in row] for row in parent['deriv']]
    norm = [[lib.bernstein_abs(p) for p in row] for row in deriv]
    modes, P = pm+hm, len(pm)
    result = dict(parent, r0=parent['r0']+parent['h']*left,
                  r1=parent['r0']+parent['h']*right, h=parent['h']*(right-left),
                  deriv=deriv, norm=norm)
    result.update(v=sum(norm[0], Q(0)), vr=sum(norm[1], Q(0)),
                  vt=sum((abs(m)*v for m,v in zip(modes,norm[0])), Q(0)),
                  hz_r=sum(norm[1][P:], Q(0)),
                  hz_t=sum((m*v for m,v in zip(hm,norm[0][P:])), Q(0)))
    return result


def interval_center(o, value):
    lo, hi = mpf_fraction(o.lo(value)), mpf_fraction(o.hi(value))
    center = Q.from_float(float((lo+hi)/2))
    return center, max(abs(center-lo), abs(hi-center))


def true_w_taylor(o, d, span, left, right, parent_index):
    source_a = Q.from_float(d['rawLeft'])
    source_h = Q.from_float(d['rawRight'])-source_a
    count = len(d['nodes'])-1
    xa = source_a+source_h*(Q(parent_index)+left)/count
    xb = source_a+source_h*(Q(parent_index)+right)/count
    # These source-x endpoints are only guesses. The unchanged original
    # monotone primitive cover proves inclusion of the actual literal R box.
    mini = dict(d, rawLeft=float(xa), rawRight=float(xb),
                nodes=[dict(radiusJS=outward_float(span['r0'], False)),
                       dict(radiusJS=outward_float(span['r1'], True))])
    cover, old_w0, old_dw = kernel.local_background_cover(o, mini)
    xa, xb = Q.from_float(mini['rawLeft']), Q.from_float(mini['rawRight'])
    anchor_x = (xa+xb)/2
    anchor = o.local_jets(d['rawCell'], d['rawSegment'], anchor_x)
    radius = o.primitives(d['rawCell'], d['rawSegment'], anchor_x)['r']
    w0, ew = interval_center(o, anchor['w'])
    slope, es = interval_center(o, anchor['h_RR'])
    Rstar, er = interval_center(o, radius)
    second = Q(0)
    component_bounds = []
    for n,j,aa,bb in cover['source_ranges']:
        aa, bb = Q(aa), Q(bb)
        for k in range(8):
            lo,hi = aa+(bb-aa)*Q(k,8), aa+(bb-aa)*Q(k+1,8)
            jets = o.local_jets(n,j,lo,hi)
            rx, rxx = jets['r_x'], jets['r_xx_one_sided_hull']
            if o.lo(rx) <= 0:
                raise ArithmeticError('Positive source-to-R derivative is required')
            value = (jets['w_xx']*rx-jets['w_x']*rxx)/(rx**3)
            bound = max(abs(mpf_fraction(o.lo(value))),abs(mpf_fraction(o.hi(value))))
            second = max(second,bound)
            component_bounds.append(dict(cell=n,segment=j,source_x=[str(lo),str(hi)],
                                         absolute_w_RR_upper_exact=str(bound)))
    H = max(abs(span['r0']-Rstar),abs(span['r1']-Rstar))+er
    error = ew+es*H+abs(slope)*er+second*H*H/2
    poly = [w0+slope*(span['r0']-Rstar), slope*span['h']]
    proof = dict(original_true_R_cover=cover, anchor_source_x=str(anchor_x),
                 anchor_actual_source_piece=[d['rawCell'],d['rawSegment']],
                 anchor_R_center_exact=str(Rstar), anchor_R_error_exact=str(er),
                 anchor_w_center_exact=str(w0), anchor_w_error_exact=str(ew),
                 anchor_w_R_center_exact=str(slope), anchor_w_R_error_exact=str(es),
                 absolute_w_RR_upper_exact=str(second),
                 absolute_R_minus_true_anchor_upper_exact=str(H),
                 polynomial_in_exact_span_coordinate=list(map(str,poly)),
                 absolute_w_minus_polynomial_upper_exact=str(error),
                 second_derivative_component_bounds=component_bounds,
                 true_background_same_R58_C1_w_and_piecewise_second_derivatives=True)
    return poly, error, proof

def gram_span_variable(s, pm, hm, wpoly, dw, quadratic_cutoff=None):
    r0, h, d = s['r0'], s['h'], s['deriv']
    P, modes = len(pm), pm+hm
    aa, bb, cc = {}, {}, {}
    for i, m in enumerate(pm):
        lib.harmonic_add(aa, m-1, lib.scale(d[1][i], 2))
        lib.harmonic_add(bb, m-1, lib.add(lib.radius_product(d[1][i], r0, h), lib.scale(d[0][i], -m)), sine=True)
        lib.harmonic_add(cc, m-1, lib.scale(lib.radius_product(d[0][i], r0, h), 2*m))
    for j, m in enumerate(hm):
        lib.harmonic_add(aa, m, lib.scale(product(wpoly, d[1][P+j]), 2))
        lib.harmonic_add(bb, m, lib.scale(product(wpoly, d[0][P+j]), -m), sine=True)
    if quadratic_cutoff is None:
        remainder = [s['vr']**2, s['vr']*s['vt'], s['vt']**2]
        method = 'all_linear_Fourier_merged_all_quadratic_norm_bounded'
    else:
        lp = [i for i, m in enumerate(pm) if abs(m) <= quadratic_cutoff]
        lh = [i for i, m in enumerate(hm) if m <= quadratic_cutoff]
        low = set(lp+[P+i for i in lh])
        high = set(range(len(modes)))-low
        for i in lp:
            m = pm[i]
            for j in lp:
                n = pm[j]
                lib.harmonic_add(aa, m-n, product(d[1][i], d[1][j]))
                lib.harmonic_add(bb, m-n, lib.scale(product(d[1][i], d[0][j]), n), sine=True)
                lib.harmonic_add(cc, m-n, lib.scale(product(d[0][i], d[0][j]), m*n))
        for i in lh:
            m = hm[i]
            for j in lh:
                n = hm[j]
                aij = lib.scale(product(d[1][P+i], d[1][P+j]), Q(1, 2))
                bij = lib.scale(product(d[1][P+i], d[0][P+j]), -Q(n, 2))
                cij = lib.scale(product(d[0][P+i], d[0][P+j]), Q(m*n, 2))
                lib.harmonic_add(aa, m-n, aij)
                lib.harmonic_add(aa, m+n, aij)
                lib.harmonic_add(bb, n+m, bij, sine=True)
                lib.harmonic_add(bb, n-m, bij, sine=True)
                lib.harmonic_add(cc, m-n, cij)
                lib.harmonic_add(cc, m+n, lib.scale(cij, -1))
        rl = sum((s['norm'][1][i] for i in low), Q(0))
        rh = sum((s['norm'][1][i] for i in high), Q(0))
        tl = sum((abs(modes[i])*s['norm'][0][i] for i in low), Q(0))
        th = sum((abs(modes[i])*s['norm'][0][i] for i in high), Q(0))
        remainder = [2*rl*rh+rh*rh, rl*th+rh*tl+rh*th, 2*tl*th+th*th]
        method = 'all_linear_and_low_quadratic_Fourier_merged_high_quadratic_bounded'
    merged = [sum((lib.bernstein_abs(v) for v in z.values()), Q(0)) for z in (aa, bb, cc)]
    A = merged[0]+2*dw*s['hz_r']+remainder[0]
    B = (merged[1]+dw*s['hz_t']+remainder[1])/r0
    C = (merged[2]+remainder[2])/r0**2
    return {'method': method, 'metric': max(A, C)+B, 'components': (A, B, C),
            'merged': merged, 'quadratic_remainder': remainder}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('geometry-bundle','constants','normalization-certificate','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--stage',type=int,required=True)
    parser.add_argument('--spans',default='15')
    parser.add_argument('--max-depth',type=int,default=0)
    parser.add_argument('--quadratic-mode-cutoff',type=int,default=12)
    args=parser.parse_args()
    if not 0<=args.max_depth<=12 or args.quadratic_mode_cutoff<0:
        raise ValueError('Use bounded proof refinement and the complete quadratic remainder')
    if ref(kernel.__file__)['sha256']!=ORIGINAL_KERNEL_SHA:
        raise ValueError('The reviewed unchanged original Gram kernel changed')
    bundle,chain,manifest,index,constants=original.validate_inputs(
        args.geometry_bundle,args.constants,args.normalization_certificate)
    out=args.outdir.resolve()
    original.fresh_dir(out)
    entries={v['stage']:v for v in manifest['files']}
    entry=entries[args.stage];data=original.checked(entry)
    if data['boundInput']!=bundle['mean_chain'] or data['sharing']['mapHash']!=entry['mapHash']:
        raise ValueError('The actual finite field changed')
    pm,hm,spans,identities=kernel.prepare(data)
    selected=list(range(len(spans))) if args.spans=='all' else sorted(set(map(int,args.spans.split(','))))
    if not selected or not set(selected)<=set(range(len(spans))):
        raise ValueError('Only actual original finite spans may be selected')
    oracle=Q060TrueBackgroundOracle(args.constants,args.normalization_certificate)
    cover,w0,dw=kernel.local_background_cover(oracle,data)
    baseline=kernel.gram_span(spans[selected[0]],pm,hm,w0,dw,args.quadratic_mode_cutoff)
    constant=gram_span_variable(spans[selected[0]],pm,hm,[w0],dw,args.quadratic_mode_cutoff)
    for name in ('metric','components','merged','quadratic_remainder'):
        if baseline[name]!=constant[name]:
            raise ArithmeticError('Constant-w specialization differs from the original exact Gram formula')
    start=time.monotonic()
    result=dict(schema='actual-full-spectrum-tail-true-w-taylor-span-certificate-v1',status='running',
        source=ref(__file__),original_gram_source=ref(kernel.__file__),
        original_bundle_validator=ref(original.__file__),geometry_bundle=ref(args.geometry_bundle),
        spectrum=bundle['spectrum'],spectrum_contract=bundle['spectrum_contract'],
        accepted_packet=bundle['accepted_packet'],original_entire_mean_chain=bundle['mean_chain'],
        stage=args.stage,actual_stage_data=entry,actual_map_hash=entry['mapHash'],
        selected_original_spans=selected,original_endpoint_scalar_identities_checked=identities,
        original_constant_w_specialization_exactly_equal=True,
        quadratic_mode_cutoff=args.quadratic_mode_cutoff,
        every_linear_mode_retained=True,every_high_quadratic_product_bounded=True,
        finite_map_or_mean_or_spectrum_changed=False,
        field_subdivision_performed=False,proof_interval_subdivision_only=True,
        oracle_provenance=oracle.provenance,target_metric_gate_exact=str(GATE),
        leaves=[],attempt_count=0,whole_tail_metric_claimed=False)
    path=out/'summary.json';write(path,result)
    def visit(parent,left,right,depth):
        span=restricted_span(spans[parent],left,right,pm,hm)
        W,error,background=true_w_taylor(oracle,data,span,left,right,parent)
        bound=gram_span_variable(span,pm,hm,W,error,args.quadratic_mode_cutoff)
        result['attempt_count']+=1
        if bound['metric']>=GATE and depth<args.max_depth:
            mid=(left+right)/2
            visit(parent,left,mid,depth+1);visit(parent,mid,right,depth+1)
            return
        row=dict(original_span=parent,proof_t=[str(left),str(right)],depth=depth,
                 literal_R_interval_exact=[str(span['r0']),str(span['r1'])],
                 true_w_linear_Taylor=background,
                 metric_operator_upper=oracle.bounds(oracle.qi(bound['metric'])),
                 exact_Gram_component_upper=list(map(str,bound['components'])),
                 exact_merged_Fourier_upper=list(map(str,bound['merged'])),
                 exact_complete_quadratic_remainder=list(map(str,bound['quadratic_remainder'])),
                 metric_gate_passed=bound['metric']<GATE)
        leaf=out/('leaf-'+str(len(result['leaves'])).zfill(5)+'.json');write(leaf,row)
        result['leaves'].append(dict(certificate=ref(leaf),original_span=parent,
            proof_t=row['proof_t'],metric_upper=row['metric_operator_upper']['upper'],
            metric_gate_passed=row['metric_gate_passed']))
        result['seconds']=time.monotonic()-start;write(path,result)
        print(json.dumps(dict(event='actual_same_map_Taylor_leaf',stage=args.stage,span=parent,
            depth=depth,metric_upper=row['metric_operator_upper']['upper'],
            passed=row['metric_gate_passed'])),flush=True)
    try:
        for j in selected:visit(j,Q(0),Q(1),0)
        for j in selected:
            intervals=sorted((Q(r['proof_t'][0]),Q(r['proof_t'][1])) for r in result['leaves'] if r['original_span']==j)
            if intervals[0][0]!=0 or intervals[-1][1]!=1 or any(a[1]!=b[0] for a,b in zip(intervals,intervals[1:])):
                raise ArithmeticError('The exact proof leaves do not cover an original span')
        passed=all(r['metric_gate_passed'] for r in result['leaves'])
        result.update(status='same_actual_selected_spans_continuous_metric_certified' if passed else 'same_actual_selected_spans_metric_not_yet_proved',
            all_selected_spans_covered_exactly=True,all_selected_metric_gates_passed=passed,
            whole_actual_stage_metric_certified=passed and selected==list(range(len(spans))),
            maximum_metric_upper=max(r['metric_upper'] for r in result['leaves']),
            seconds=time.monotonic()-start)
    except Exception as exc:
        result.update(status='actual_Taylor_certificate_execution_failed',error=repr(exc),seconds=time.monotonic()-start)
        write(path,result);raise
    write(path,result)
    print(json.dumps(dict(status=result['status'],summary=ref(path),maximum_metric_upper=result['maximum_metric_upper'],seconds=result['seconds'])),flush=True)


if __name__=='__main__':
    main()
