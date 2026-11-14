#!/usr/bin/env python3
"""Fresh ideal meridian guards for the declared monotone initial law.

Author: strong_recovery (GPT-6 Astra Pro, AI assisted), 2026-11-13.
The old exact analytic proof is retained outside explicitly recorded sites.
Nonzero lambda uses the exact binary physical constants in the degree-n
Bernstein formula and a rational enclosure of its positive length root.
Stored floating coefficients, Gauss64 realization, the material chart,
physical quintic, complete mean and surface geometry remain separate.
An initial-only warm inspection never asserts an accepted new solution.
"""
from __future__ import annotations
import argparse
import ast
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import sys
import time

HERE = Path(__file__).resolve().parent
ORIGINAL = HERE/'strong_newg_analytic_profile_bounds.py'
ORIGINAL_SHA = 'cf80d379758054726cc1f77d8065eaf2eab59c3015fb263cb8a8f5918a664af5'
PROVIDERS = {
    'strong_monotone_initial_speed.py':
        '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py':
        '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
}


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def binary(value):
    value = float(value)
    if not math.isfinite(value): raise ValueError('Nonfinite physical constant')
    return Q(*value.as_integer_ratio())
def rec(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                decimal_display=float(value))
def read(path):
    p = Path(path); data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == '.gz' else data)


def sqrt_box(value, bits=88):
    if value <= 0: raise ValueError('Positive rational square root required')
    lo, hi = Q(0), max(Q(1), value)
    for _ in range(bits):
        mid = (lo+hi)/2
        if mid*mid < value: lo = mid
        else: hi = mid
    if not lo*lo <= value <= hi*hi: raise ArithmeticError('sqrt enclosure')
    return lo, hi


def optional_guard(config, accepted, identities, check, source_dir):
    check('explicit_optional_initial_laws', binary(config.get('initial_speed_pulse', 0)) == 0)
    weight = binary(config.get('initial_speed_frontload', 0))
    degree = config.get('initial_speed_frontload_degree', 22)
    check('explicit_frontload_convex_domain', 0 <= weight <= 1 and int(degree) == degree
          and 4 <= degree <= 64)
    for name, expected in PROVIDERS.items():
        path = Path(source_dir)/name
        check('pinned_initial_law_'+name, sha(path) == expected)
        identities[str(path)] = expected
    if weight:
        recorded = accepted.get('design_provenance', {}).get('source_sha256', {})
        for name, expected in PROVIDERS.items():
            found = [v for k, v in recorded.items() if Path(k).name == name]
            check('accepted_nonzero_provider_'+name, bool(found) and all(v == expected for v in found))
    identities[str(ORIGINAL)] = ORIGINAL_SHA
    identities[str(Path(__file__).resolve())] = sha(__file__)


def initial_bounds(config, check):
    """Exact intended polynomial: each velocity control is a+b*S."""
    V, delta, k0 = (binary(config[k]) for k in ('vu', 'delta', 'start_acceleration'))
    weight = binary(config.get('initial_speed_frontload', 0))
    degree = config.get('initial_speed_frontload_degree', 22)
    check('initial_physical_parameters', 0 < V < 1 and delta > 0 and k0 > 0)
    check('initial_law_convex_domain', 0 <= weight <= 1 and int(degree) == degree
          and 4 <= degree <= 64 and binary(config.get('initial_speed_pulse', 0)) == 0)
    n = int(degree)
    A = (1-weight)/2+weight*Q(n-1, n+1)
    B = (1-weight)/12+weight*Q(1, n*(n+1))
    check('initial_length_positive_coefficients', A > 0 and B > 0)
    poly = lambda s: B*k0*s*s+A*V*s-delta
    lo, hi = Q(0), delta/(A*V)
    for _ in range(96):
        mid = (lo+hi)/2
        if poly(mid) < 0: lo = mid
        else: hi = mid
    check('initial_length_unique_positive_root', lo > 0 and poly(lo) <= 0 <= poly(hi),
          dict(equation='B*k0*S^2+A*V*S-delta=0', A=rec(A), B=rec(B),
               lower=rec(lo), upper=rec(hi), derivative_positive=True))
    controls = []
    for j in range(n+1):
        terms = [(k, Q(math.comb(3, k)*math.comb(n-3, j-k), math.comb(n, j)))
                 for k in range(max(0, j-(n-3)), min(3, j)+1)]
        a = V*sum((c for k, c in terms if k >= 2), Q(0))
        b = k0*sum((c/3 for k, c in terms if k == 1), Q(0))
        ea, eb = (Q(0), Q(0)) if j == 0 else ((Q(0), k0/n) if j == 1 else (V, Q(0)))
        controls.append(((1-weight)*a+weight*ea, (1-weight)*b+weight*eb))
    controls[0], controls[1], controls[-2], controls[-1] = (Q(0),Q(0)), (Q(0),k0/n), (V,Q(0)), (V,Q(0))
    bounds = lambda z: (min(z[0]+z[1]*lo, z[0]+z[1]*hi),
                        max(z[0]+z[1]*lo, z[0]+z[1]*hi))
    differences = [(controls[j+1][0]-controls[j][0], controls[j+1][1]-controls[j][1])
                   for j in range(n)]
    dc = [bounds(z) for z in differences]
    check('initial_monotone_Bernstein_controls', min(a for a,b in dc) >= 0,
          dict(degree=n, minimum_difference_lower=rec(min(a for a,b in dc))))
    check('initial_exact_endpoint_velocity_and_acceleration', controls[0] == (0,0)
          and controls[1] == (0,k0/n) and controls[-2] == (V,0) and controls[-1] == (V,0),
          dict(velocity_start='0', velocity_end=rec(V), acceleration_start=rec(k0), acceleration_end='0'))
    summed = (sum((a for a,b in controls), Q(0))/(n+1),
              sum((b for a,b in controls), Q(0))/(n+1))
    check('initial_exact_radius_increment_identity', summed == (A*V, B*k0),
          dict(identity='S*sum(c_j)/(n+1)=A*V*S+B*k0*S^2=delta', delta=rec(delta)))
    accel = n*max(b for a,b in dc)/lo
    check('initial_complete_speed_and_acceleration_hulls', 0 < V < 1 and accel < Q(15,2),
          dict(radius_lower='1', radius_upper=rec(1+delta), speed_lower='0', speed_upper=rec(V),
               acceleration_lower='0', acceleration_upper=rec(accel)))
    derivatives = []
    values = list(controls)
    for order in range(min(4,n)+1):
        hull = [bounds(z) for z in values]
        low, high = min(x for x,y in hull), max(y for x,y in hull)
        derivatives.append(dict(order=order, normalized_u_lower=rec(low), normalized_u_upper=rec(high),
                                physical_s_absolute_upper=rec(max(abs(low),abs(high))/lo**order)))
        if order < min(4,n):
            values = [((n-order)*(values[j+1][0]-values[j][0]),
                       (n-order)*(values[j+1][1]-values[j][1])) for j in range(len(values)-1)]
    check('initial_degree_and_high_derivative_record', len(controls) == n+1,
          dict(degree=n, radial_degree=n+1, velocity_derivative_hulls=derivatives,
               exact_control_affine_in_length=[dict(constant=rec(a), length_coefficient=rec(b)) for a,b in controls],
               intended_analytic_only=True, stored_binary_controls_or_Gauss64_not_certified=True))
    return accel


def sync_lower(vd, vl, Ksync, om, check):
    check('synchronization_positive_domain', 0 < vd < vl < 1 and Ksync > 0 and om > 0)
    _, upper = sqrt_box(1-vd*vd)
    bound = (vl-vd)/(upper*Ksync*om)
    check('synchronization_true_asin_gap_lower', bound > 0,
          dict(proof='asin(vl)-asin(vd)=integral_vd^vl (1-x^2)^(-1/2) dx >= (vl-vd)/sqrt(1-vd^2)',
               sqrt_upper=rec(upper), physical_length_lower=rec(bound)))
    return bound


def asin_box(value, pi):
    """Positive inverse sine via atan, exact rational argument enclosures."""
    if not 0 < value < 1: raise ValueError('Positive asin argument required')
    low, high = sqrt_box(1-value*value)
    if low <= 0: raise ArithmeticError('The asin square root lower bound vanished')
    if value*value > Q(1,2):
        left, right = low/value, high/value
        complement = True
    else:
        left, right = value/high, value/low
        complement = False
    if not 0 < left <= right < 1: raise ArithmeticError('The alternating atan argument domain')
    def atan_bounds(x):
        total = sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(48)), Q(0))
        return total, total+x**97/97
    lo, hi = atan_bounds(left)[0], atan_bounds(right)[1]
    return (pi[0]/2-hi, pi[1]/2-lo) if complement else (lo,hi)


def first_turn_upper(vp, vd, Ks, om, pi, check):
    check('first_turn_positive_domain', 0 < vp < 1 and 0 < vd < 1 and Ks > 0 and om > 0)
    ap, ad = asin_box(vp,pi), asin_box(vd,pi)
    length = (ap[1]+ad[1])/(Ks*om)
    check('first_turn_actual_angle_length_upper', length > 0,
          dict(proof='The actual turn runs from asin(vp) to -asin(vd).',
               inlet_asin_lower=rec(ap[0]),inlet_asin_upper=rec(ap[1]),
               outlet_abs_asin_lower=rec(ad[0]),outlet_abs_asin_upper=rec(ad[1]),
               physical_length_upper=rec(length)))
    return length


def transformed():
    if sha(ORIGINAL) != ORIGINAL_SHA: raise ValueError('The frozen old proof changed')
    text = ORIGINAL.read_text()
    old = """    slo,shi=Q(4,5),Q(9,10)
    def hermite(z):return k0*z*z+6*V*z-12*delta
    check('actual_Hermite_unique_length',hermite(slo)<0<hermite(shi),dict(equation='k0*S0^2+6*V*S0=12*delta',lower=record(slo),upper=record(shi)))
    check('actual_Hermite_monotone_speed',k0*shi<=3*V,dict(acceleration_Bernstein='[k0,3V/S0-k0,0]'))
    accel=max(k0,3*V/slo-k0)
    check('actual_Hermite_acceleration_below_one',accel<1,record(accel))"""
    zero = '\n'.join('    '+line for line in old.splitlines())
    new = ("    optional_guard(config, accepted, identities, check, a.source_dir)\n"
           "    if binary(config.get('initial_speed_frontload',0)) == 0:\n"+zero+
           "\n    else:\n        accel=initial_bounds(config, check)")
    edits = [
        (old,new),
        ('    firstL=pi[1]/(Ks*om);firstLo=1+delta-firstL;firstHi=1+delta+LB+vp*C+firstL',
         '    firstL=first_turn_upper(vp,vd,Ks,om,pi,check);firstLo=1+delta-firstL;firstHi=1+delta+LB+vp*C+firstL'),
        ("    lower_lengths=dict(angle_boost=LB,first_turn=(vp+vd)/(Ks*om),sync=(vl-vd)/(Ksync*om),",
         "    lower_lengths=dict(angle_boost=LB,first_turn=(vp+vd)/(Ks*om),sync=sync_lower(vd,vl,Ksync,om,check),"),
        ("    check('all_nonconstant_phase_lengths',min(lower_lengths.values())>Q(27,10000),{k:record(v) for k,v in lower_lengths.items()})",
         "    minimum_phase_length=Q((min(lower_lengths.values())*2**30).__floor__(),2**30)\n"
         "    check('all_nonconstant_phase_lengths',minimum_phase_length>0,{k:record(v) for k,v in lower_lengths.items()})"),
        ("minimum_nonconstant_segment_length='27/10000',sum_nonconstant_segment_lengths_upper='4',",
         "minimum_nonconstant_segment_length=record(minimum_phase_length),sum_nonconstant_segment_lengths_upper='4',"),
        ("schema='accepted-newg-ideal-analytic-profile-domain-v1'", "schema='accepted-newg-initial-law-ideal-analytic-profile-domain-v1'"),
        ("author='/root/geometry_audit'", "author='/root/strong_recovery'"),
        ("actual_accepted_primary_sha256=sha(a.accepted),frozen_profile=config,actual_original_port=cut,",
         "actual_accepted_primary_sha256=sha(a.accepted),frozen_profile=config,actual_original_port=cut,\n"
         "        initial_law_proof_source=dict(original_sha256=ORIGINAL_SHA,adapter_sha256=sha(__file__),\n"
         "            zero_lambda_original_Hermite_block_unchanged=True,other_original_analytic_guards_retained=True,\n"
         "            tighter_sync_asin_lower=True,tighter_actual_first_turn_angle_upper=True,\n"
         "            dynamic_positive_minimum_phase_length=True),"),
    ]
    changed = text
    for before, after in edits:
        if changed.count(before) != 1: raise ValueError('The old proof anchor is not unique')
        changed = changed.replace(before, after, 1)
    reverse = changed
    for before, after in reversed(edits):
        if reverse.count(after) != 1: raise ValueError('The proof reverse anchor differs')
        reverse = reverse.replace(after, before, 1)
    if reverse != text: raise ValueError('Another old proof site changed')
    ast.parse(changed)
    return changed, [dict(before=a,after=b,count=1) for a,b in edits]


def main():
    ap=argparse.ArgumentParser(add_help=False)
    ap.add_argument('--inspect-initial-profile',type=Path)
    ap.add_argument('--prepare-source-record',type=Path)
    own, remaining=ap.parse_known_args()
    source,edits=transformed()
    if own.prepare_source_record:
        if remaining or own.inspect_initial_profile: raise ValueError('Source preparation is separate')
        out=own.prepare_source_record
        record=dict(schema='initial-law-analytic-source-preparation-v1',source_sha256=sha(__file__),
            original_sha256=ORIGINAL_SHA,transformed_sha256=hashlib.sha256(source.encode()).hexdigest(),
            replacements=edits,exact_reverse_recovers_original=True,new_accepted_values_created=False,
            Node_ODE_or_geometry_calls=0)
    elif own.inspect_initial_profile:
        p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);args=p.parse_args(remaining)
        out=args.out;data=read(own.inspect_initial_profile);config=data.get('frozen_profile',data.get('warm_profile',data.get('profile',data)))
        gates={};evidence={};start=time.monotonic()
        def check(name,yes,details=None):
            if not yes:raise ArithmeticError(name)
            gates[name]=True
            if details is not None:evidence[name]=details
        accel=initial_bounds(config,check)
        record=dict(schema='unsolved-profile-initial-law-ideal-domain-v1',all_gates=all(gates.values()),
            gates=gates,evidence=evidence,input_file=str(own.inspect_initial_profile),input_sha256=sha(own.inspect_initial_profile),
            physical_profile=config,source_sha256=sha(__file__),original_proof_sha256=ORIGINAL_SHA,
            acceleration_upper=rec(accel),whole_profile_certified=False,accepted_new_solution=False,
            actual_Gauss_or_floating_realization_certified=False,Node_ODE_or_geometry_calls=0,
            elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    else:
        namespace=dict(__file__=str(Path(__file__).resolve()),__name__='retained_profile_proof_with_initial_law',
            optional_guard=optional_guard,initial_bounds=initial_bounds,sync_lower=sync_lower,
            first_turn_upper=first_turn_upper,ORIGINAL_SHA=ORIGINAL_SHA)
        exec(compile(source,'<retained-profile-proof-with-explicit-initial-law>','exec'),namespace)
        namespace['__doc__']=__doc__
        old=sys.argv;sys.argv=[old[0],*remaining]
        try:namespace['main']()
        finally:sys.argv=old
        return
    if out.exists():raise FileExistsError(out)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(out),sha256=sha(out),all_gates=record.get('all_gates'),
                         new_accepted_values_created=False)),flush=True)


if __name__=='__main__':main()
