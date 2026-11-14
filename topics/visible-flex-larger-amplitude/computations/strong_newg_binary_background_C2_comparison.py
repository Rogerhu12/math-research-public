#!/usr/bin/env python3
"""Actual binary segment/table replay and explicit continuous C2 comparison.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The accepted profile is reloaded through the frozen provider, without a
Flow/RHS/Newton/Node call. Its actual binary segment constants and Gauss64
table define exact-real piecewise primitives. Their complete one-sided
endpoint jets are enclosed, then a specified quintic corrector matches
successive jets. This is a new comparison radius, not a modification or a
certificate of the accepted target g or its floating implementation.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import resource
import struct
import time
import numpy as np
from flint import arb, ctx

PINS = {
    'alternative-neck-provider.py': '84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
    'alternative-neck-flatturn.py': 'c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd',
    'alternative-neck-excursion.py': 'f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c',
    'strong_angle_boost.py': 'ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be',
    'strong_newg_gauss64_piecewise_C2_bridge.py': 'a830cdd1da8c4dc187b0ca4e27c0c67d4834c92b8539677f6ef32fbb93e60ea6',
}
TABLE_SHA = '0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def binary(x):
    return F.from_float(float(x))


def aq(q):
    q = F(q)
    return arb(q.numerator)/q.denominator


def dyadic(v):
    return F(int(v[0]))*F(2)**int(v[1])


def lower(v):
    m, e = arb(v).lower().man_exp()
    return [str(m), int(e)]


def upper(v):
    m, e = arb(v).upper().man_exp()
    return [str(m), int(e)]


def box(v):
    return [lower(v), upper(v)]


def rational(q):
    q = F(q)
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def interval(lo, hi):
    return aq((lo+hi)/2)+arb(0, aq((hi-lo)/2))


def polyeval(p, x):
    z = arb(0)
    for c in reversed(p):
        z = z*x+aq(c)
    return z


def derivative(p):
    return [i*p[i] for i in range(1, len(p))] or [F(0)]


def affine_poly(p, a, b):
    """Coefficients of p(a+b*t), exactly."""
    return [sum((p[k]*comb(k,j)*a**(k-j)*b**j
                 for k in range(j, len(p))), F(0)) for j in range(len(p))]


def phase_pieces(seg):
    p0, delta = binary(seg['p0']), binary(seg['p1'])-binary(seg['p0'])
    if 'turn_ramp' in seg:
        e = binary(seg['turn_ramp'])
        k = delta/(1-e)
        left = [p0, 0, 0, k/e**2, -k/(2*e**3)]
        middle = [p0-k*e/2, k]
        # I_right=1-e-((1-u)^3/e^2-(1-u)^4/(2e^3)).
        right = [p0+k*(1-e), 0, 0, 0, 0]
        for degree, scale in ((3, -k/e**2), (4, k/(2*e**3))):
            for j in range(degree+1):
                right[j] += scale*comb(degree,j)*(-1)**j
        return [(F(0), e, left), (e, 1-e, middle), (1-e, F(1), right)]
    if seg['kind'] == 'coast':
        if binary(seg['p0']) != binary(seg['p1']):
            raise ValueError('Original constant phase required')
        return [(F(0), F(1), [p0])]
    if seg['kind'] == 'brake':
        return [(F(0), F(1), [p0, F(0), delta])]
    raise ValueError('Unknown original phase segment')


def partial_primitive(piece, width, nodes, weights):
    """Value, first and second u derivatives of w*sum omega*f(a+w*g)."""
    left, right, poly = piece
    d1, d2 = derivative(poly), derivative(derivative(poly))
    totals = [arb(0), arb(0), arb(0)]
    for node, weight in zip(nodes, weights):
        x = aq(left)+width*node
        phase = polyeval(poly, x)
        phase1, phase2 = polyeval(d1, x), polyeval(d2, x)
        sn, cs = phase.sin(), phase.cos()
        f1 = cs*phase1
        f2 = cs*phase2-sn*phase1**2
        totals[0] += weight*width*sn
        totals[1] += weight*(sn+width*node*f1)
        totals[2] += weight*(2*node*f1+width*node**2*f2)
    return totals


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--accepted', type=Path, nargs='+', required=True)
    for key in ('port','source-dir','table','out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--radius-subdivisions', type=int, default=32)
    p.add_argument('--rss-kib', type=int, default=131072)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Fresh exact binary-background comparison required')
    if a.radius_subdivisions < 16:
        raise ValueError('Explicit complete background interval cover required')
    ctx.prec = 256
    ctx.threads = 1
    start = time.monotonic()
    counts = {}
    def check(name, yes):
        if not yes:
            raise ArithmeticError(name)
        counts[name] = counts.get(name,0)+1
    for name, wanted in PINS.items():
        check('all_frozen_background_sources', sha(a.source_dir/name) == wanted)
    check('actual_binary_table_certificate_identity', sha(a.table) == TABLE_SHA)
    table, port = read(a.table), read(a.port)
    check('complete_table_certificate', table['all_gates'] and all(table['gates'].values()) and
          len(table['root_weight_rows']) == 64)
    nodes = [aq(F(int(r['actual_binary_gu']['numerator']), int(r['actual_binary_gu']['denominator'])))
             for r in table['root_weight_rows']]
    weights = [aq(F(int(r['actual_normalized_binary_weight']['numerator']), int(r['actual_normalized_binary_weight']['denominator'])))
               for r in table['root_weight_rows']]
    Ew = dyadic(table['certified_error_bounds']['normalized_total_weight_error'])
    Eu = dyadic(table['certified_error_bounds']['maximum_normalized_node_error'])
    spec = importlib.util.spec_from_file_location('actual_binary_background_provider', a.source_dir/'alternative-neck-provider.py')
    provider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(provider)
    actual_table = b''.join(struct.pack('<ddd', float(x), float(w), float(u))
                           for x,w,u in zip(provider.base.gx,provider.base.gw,provider.base.gu))
    check('actual_loaded_table_all_bits', hashlib.sha256(actual_table).hexdigest() == table['binary_table_float64le_sha256'])
    spec = importlib.util.spec_from_file_location('frozen_gauss_error_formula', a.source_dir/'strong_newg_gauss64_piecewise_C2_bridge.py')
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    remainder = helper.remainder_jet(F(2),F(1<<20))
    profiles = []
    input_ids = {str(a.table):sha(a.table),str(a.port):sha(a.port)}
    for accepted_path in a.accepted:
        saved = read(accepted_path)
        input_ids[str(accepted_path)] = sha(accepted_path)
        cfg = saved['frozen_profile']
        check('actually_accepted_original_profile', saved['solver_success'] and not saved.get('audit_pending',True) and
              saved['config']['actual_nonlinear_tail'] and saved['physical_port_sha256'] == sha(a.port))
        check('original_zero_optional_initial_laws', float(cfg.get('initial_speed_frontload',0)) == 0 and
              float(cfg.get('initial_speed_pulse',0)) == 0 and cfg['boost_law'] == 'angle')
        prefix = provider.NeckPrefix(cfg)
        bridge = provider.NeckTerminalBridge(provider.tagged_port(port,cfg)['cut'])
        check('same_actual_binary_physical_length', prefix.end+bridge.end == saved['meridian_length'])
        segments = []
        for component, obj, shift in [('prefix',prefix,0.),('bridge',bridge,prefix.end)]:
            for j, seg in enumerate(obj.segments):
                g0, g1 = float(shift+seg['s0']), float(shift+seg['s1'])
                segments.append({'component':component,'local_segment':j,'original_binary_segment':seg,
                                 'physical_start_binary':g0,'physical_end_binary':g1})
        check('complete_actual_binary_segment_cover', segments[0]['physical_start_binary'] == 0 and
              segments[-1]['physical_end_binary'] == saved['meridian_length'] and
              all(x['physical_end_binary'] == y['physical_start_binary'] for x,y in zip(segments,segments[1:])))
        pieces = []
        for index, rec in enumerate(segments):
            seg = rec['original_binary_segment']
            L, h = binary(seg['length']), binary(rec['physical_end_binary'])-binary(rec['physical_start_binary'])
            s0, a0 = binary(rec['physical_start_binary']), binary(seg['a0'])
            check('actual_segment_positive_length_and_anchor', L > 0 and h > 0 and a0 > 0)
            rec['exact_physical_length_minus_constructor_length'] = rational(h-L)
            if seg['kind'] == 'hermite':
                b, V = binary(seg['k0'])*L, binary(seg['v1'])
                c, d = 3*V-2*b, b-2*V
                poly = [a0,F(0),L*b/2,L*c/3,L*d/4]
                def hermite(u):
                    return [polyeval(poly,u),polyeval(derivative(poly),u)/aq(h),
                            polyeval(derivative(derivative(poly)),u)/aq(h*h)]
                left, right = hermite(arb(0)), hermite(arb(1))
                check('actual_binary_Hermite_monotonicity', 0 < b < 3*V and V < 1)
                rlo, rhi = left[0].lower(), right[0].upper()
                vcap = (aq(L/h)*aq(V)).upper()
                acap = (aq(L/(h*h))*aq(max(b,3*V-b))).upper()
                pieces.append({'segment':index,'phase_piece':0,'physical_left':s0,'physical_right':s0+h,
                    'left':left,'right':right,'radius_lower':rlo,'radius_upper':rhi,
                    'first_absolute_upper':vcap,'second_absolute_upper':acap,
                    'Gauss_first_second_error':[arb(0),arb(0)],'constructor_rate_discrepancy':arb(0)})
                continue
            pp = phase_pieces(seg)
            previous = arb(0)
            for j, piece in enumerate(pp):
                lo, hi, phi = piece
                span = hi-lo
                # The actual polynomial on this normalized smooth subpiece
                # is fixed before any partial upper endpoint is varied.
                normpoly = affine_poly(phi,lo,span)
                centered = affine_poly(normpoly,F(1,2),F(1))
                complex_cap = sum((abs(c)*2**k for k,c in enumerate(centered)),F(0))
                check('actual_phase_Cauchy_disk_modulus', aq(complex_cap).exp() < 1<<20)
                d1max = F(0)
                d2max = F(0)
                d3max = F(0)
                # Exact power bounds after u=lo+span*t; the coefficients
                # need only bound this one actual smooth subpiece.
                for order in range(1,4):
                    q = normpoly
                    for _ in range(order):q=derivative(q)
                    cap = sum(map(abs,q),F(0))
                    if order==1:d1max=cap
                    elif order==2:d2max=cap
                    else:d3max=cap
                M=[F(1),d1max,d1max*d1max+d2max,
                   d1max**3+3*d1max*d2max+d3max]
                taberr, exacterr, totalerr = helper.primitive_errors(Ew,Eu,M,remainder)
                error1 = aq(L/h)*aq(totalerr[1])
                error2 = aq(L/(h*h*span))*aq(totalerr[2])
                if seg['kind']=='coast':
                    phase_bound=abs(aq(binary(seg['p0'])).sin()).upper()
                    analytic_acc=arb(0)
                else:
                    phase_range=interval(min(binary(seg['p0']),binary(seg['p1'])),max(binary(seg['p0']),binary(seg['p1'])))
                    phase_bound=abs(phase_range.sin()).upper()
                    if 'turn_ramp' in seg:
                        rate=abs(binary(seg['p1'])-binary(seg['p0']))/(1-binary(seg['turn_ramp']))
                    else:
                        rate=2*abs(binary(seg['p1'])-binary(seg['p0']))
                    analytic_acc=aq(L/(h*h))*aq(rate)
                vcap=(aq(L/h)*phase_bound+error1).upper()
                acap=(analytic_acc+error2).upper()
                qleft=partial_primitive(piece,arb(0),nodes,weights)
                qright=partial_primitive(piece,aq(span),nodes,weights)
                def actual_jets(q):
                    return [aq(a0)+aq(L)*(previous+q[0]),aq(L/h)*q[1],aq(L/(h*h))*q[2]]
                left,right=actual_jets(qleft),actual_jets(qright)
                rlo,rhi=None,None
                for sub in range(a.radius_subdivisions):
                    w0,w1=span*F(sub,a.radius_subdivisions),span*F(sub+1,a.radius_subdivisions)
                    q=partial_primitive(piece,interval(w0,w1),nodes,weights)[0]
                    radius=aq(a0)+aq(L)*(previous+q)
                    rlo=radius.lower() if rlo is None else min(rlo,radius.lower())
                    rhi=radius.upper() if rhi is None else max(rhi,radius.upper())
                    check('complete_radius_subinterval_order',0<=w0<w1<=span)
                discrepancy=arb(0)
                if 'turn_ramp' in seg:
                    exact_rate=abs(binary(seg['p1'])-binary(seg['p0']))/(L*(1-binary(seg['turn_ramp'])))
                    discrepancy=abs(aq(exact_rate-binary(seg['K']))).upper()
                pieces.append({'segment':index,'phase_piece':j,'physical_left':s0+h*lo,'physical_right':s0+h*hi,
                    'left':left,'right':right,'radius_lower':rlo,'radius_upper':rhi,
                    'first_absolute_upper':vcap,'second_absolute_upper':acap,
                    'Gauss_first_second_error':[error1,error2],
                    'constructor_rate_discrepancy':discrepancy,
                    'phase_Cauchy_complex_cap':complex_cap,'normalized_phase_power_coefficients':normpoly,
                    'normalized_sin_derivative_bounds':M})
                previous+=qright[0]
            check('actual_profile_small_owned_RSS',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=a.rss_kib)
        check('all_exact_comparison_pieces_cover_domain', pieces[0]['physical_left']==0 and
              pieces[-1]['physical_right']==binary(saved['meridian_length']) and
              all(x['physical_right']==y['physical_left'] for x,y in zip(pieces,pieces[1:])))
        maximum=[arb(0),arb(0),arb(0)]
        gaps_max=[arb(0),arb(0),arb(0)]
        rows=[]
        for j,piece in enumerate(pieces):
            length=piece['physical_right']-piece['physical_left']
            gaps=[pieces[j+1]['left'][k]-piece['right'][k] for k in range(3)] if j+1<len(pieces) else [arb(0)]*3
            E=[abs(z).upper() for z in gaps]
            # Degree-5 Bernstein hulls of the three Hermite endpoint bases:
            # sup|H0,H1,H2| <= (1,2/5,1/10), first <= (5,2,1/2),
            # second <= (20,12,4). v=h*gap1, w=h^2*gap2/2.
            corr=[E[0]+aq(F(2,5)*length)*E[1]+aq(length**2/F(20))*E[2],
                  aq(5/length)*E[0]+2*E[1]+aq(length/4)*E[2],
                  aq(20/length**2)*E[0]+aq(12/length)*E[1]+2*E[2]]
            for k in range(3):
                maximum[k]=max(maximum[k],corr[k].upper())
                gaps_max[k]=max(gaps_max[k],E[k])
            rows.append({'segment':piece['segment'],'phase_piece':piece['phase_piece'],
                'physical_interval':[rational(piece['physical_left']),rational(piece['physical_right'])],
                'left_value_first_second':list(map(box,piece['left'])),
                'right_value_first_second':list(map(box,piece['right'])),
                'next_left_minus_current_right':list(map(box,gaps)),
                'quintic_repair_uniform_C0_C1_C2_upper':list(map(upper,corr)),
                'complete_radius_interval':[lower(piece['radius_lower']),upper(piece['radius_upper'])],
                'continuous_first_absolute_upper':upper(piece['first_absolute_upper']),
                'continuous_second_absolute_upper':upper(piece['second_absolute_upper']),
                'Gauss_derivative_comparison_first_second_upper':list(map(upper,piece['Gauss_first_second_error'])),
                'frozen_K_vs_exact_binary_phase_rate_error_upper':upper(piece['constructor_rate_discrepancy'])})
        radius_lo=min(p['radius_lower'] for p in pieces)-maximum[0]
        radius_hi=max(p['radius_upper'] for p in pieces)+maximum[0]
        first=max(p['first_absolute_upper'] for p in pieces)+maximum[1]
        second=max(p['second_absolute_upper'] for p in pieces)+maximum[2]
        check('repaired_radius_strictly_positive',radius_lo>0)
        check('repaired_speed_strictly_below_one',first<1)
        cut=port['cut'];w=binary(cut['backgroundSlope']);wp=binary(cut['backgroundSecond'])
        target=[aq(binary(cut['radius'])),-1/(1+aq(w)**2).sqrt(),-aq(w*wp)/(1+aq(w)**2)**2]
        terminal_gap=[pieces[-1]['right'][k]-target[k] for k in range(3)]
        definition={'accepted_primary_sha256':sha(accepted_path),'actual_binary_segments':segments,
                    'actual_binary_table_sha256':table['binary_table_float64le_sha256'],
                    'normalization':'Use the exact binary global segment endpoints, with u=(s-start)/(end-start). All other operations and sin/cos are exact real.',
                    'primitive':'Use original split Gauss64 partial primitives with exact binary normalized nodes/weights; Hermite radius is the exact polynomial.',
                    'repair':'On each smooth piece except the last add u0*(10t^3-15t^4+6t^5)+v0*(-4t^3+7t^4-3t^5)+w0*(t^3-2t^4+t^5), where u0=next_left_value-current_right_value, v0=piece_length*first_gap, w0=piece_length^2*second_gap/2. Last piece unchanged.'}
        definition_sha=hashlib.sha256(json.dumps(definition,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
        profiles.append({'accepted_primary':str(accepted_path),'accepted_primary_sha256':sha(accepted_path),
            'original_physical_metric_sha256':hashlib.sha256(json.dumps(cfg,sort_keys=True).encode()).hexdigest(),
            'frozen_profile':cfg,'comparison_definition':definition,'comparison_definition_sha256':definition_sha,
            'segments':len(segments),'complete_smooth_pieces':len(pieces),'piece_rows':rows,
            'unrepaired_join_gap_absolute_upper':list(map(upper,gaps_max)),
            'global_explicit_repair_C0_C1_C2_upper':list(map(upper,maximum)),
            'new_C2_comparison_radius_bounds':[lower(radius_lo),upper(radius_hi)],
            'new_C2_comparison_speed_absolute_upper':upper(first),
            'new_C2_comparison_acceleration_absolute_upper':upper(second),
            'original_first_left_and_last_right_jets_preserved':True,
            'last_jet_minus_exact_original_cut_target':list(map(box,terminal_gap)),
            'all_internal_comparison_joins_C2_by_explicit_endpoint_identity':True,
            'original_floating_candidate_or_target_g_modified':False,
            'actual_libm_dot_affine_node_and_initialization_rounding_certified':False})
        print(json.dumps({'event':'actual_binary_background_comparison_complete','accepted':str(accepted_path),
             'pieces':len(pieces),'repair_displays':[float(x) for x in maximum],
             'radius_lower_display':float(radius_lo),'speed_upper_display':float(first),
             'acceleration_upper_display':float(second)}),flush=True)
    check('final_small_owned_RSS',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=a.rss_kib)
    result={'schema':'actual-binary-background-piecewise-primitive-explicit-C2-comparison-v1',
        'scope':__doc__,'author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        'all_gates':True,'gate_count':sum(counts.values()),'gates':{k:True for k in counts},'gate_multiplicities':counts,
        'source_sha256':sha(__file__),'frozen_source_sha256':PINS,'input_identities':input_ids,
        'actual_binary_table_sha256':table['binary_table_float64le_sha256'],'profiles':profiles,
        'radius_cover_subdivisions_per_smooth_piece':a.radius_subdivisions,
        'coefficient_and_transcendental_intervals':'Arb 256-bit outward enclosures; binary inputs are exact rational values.',
        'sampling_used_as_proof':False,'new_ODE_RHS_Flow_Node_Newton_calls':0,
        'pending':['Floating initialization/asin/atan/sqrt and evaluation error relative to this explicit exact-real expression.',
                   'Target-g error caused by physical endpoint alignment and this comparison repair.',
                   'Complete surface nonmean and mean Cartesian jet transfer and its quadrature bounds.',
                   'Physical tail/cap matching, closed surface, same-g refinement and full-family reach/amplitude.'],
        'full_actual_surface_or_original_target_g_certified':False,
        'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    data=(json.dumps(result,indent=2,allow_nan=False)+'\n').encode()
    if len(data)>=1_000_000:
        raise ValueError('Small complete continuous-background certificate required')
    a.out.write_bytes(data)
    print(json.dumps({'all_gates':True,'gate_count':result['gate_count'],'path':str(a.out),
                      'sha256':sha(a.out),'bytes':len(data),'elapsed':result['elapsed_seconds'],
                      'peak_rss_kib':result['peak_rss_kib']}),flush=True)


if __name__=='__main__':
    main()
