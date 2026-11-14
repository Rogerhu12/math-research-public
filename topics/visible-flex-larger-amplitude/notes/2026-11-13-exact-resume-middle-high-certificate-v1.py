#!/usr/bin/env python3
"""Independent exact substitution of the complete R122 mixed certificate.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No radius search, matrix inversion, source integral, Arb or ODE is repeated.
Every displayed conclusion is re-established from the saved exact rows.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ex(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2) ** int(v[1])
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2) ** int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def rec(v):
    return dict(numerator=str(v.numerator), denominator=str(v.denominator), display_only=float(v))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('primary', 'resource', 'finite', 'high', 'balanced', 'source', 'head', 'out'):
        ap.add_argument('--' + name, required=True, type=Path)
    a = ap.parse_args(); start = time.monotonic()
    if a.out.exists():
        raise FileExistsError('Fresh independent certificate output required')
    d, usage, finite, high, balanced, source, head = [read(getattr(a, n)) for n in
        ('primary', 'resource', 'finite', 'high', 'balanced', 'source', 'head')]
    rows = d['rows']; n = len(rows); C, B, D = F(10), F(18555), F(257)
    special = {5, 21}; boundary = ex(balanced['balanced_B_lower'])
    hm = [ex(v) for v in head['complete_coarse_trace_rows']['head']['high_bands_value_upper']]
    centre, tail = ex(source['complete_middle_shared_mass']), ex(source['complete_infinite_high_shared_mass'])
    radii = [ex(r['finite_radius']) for r in rows]
    hradii = [ex(r['high_radius']) for r in rows]
    weights = [(ex(r['finite_distance_weight']), ex(r['high_distance_weight'])) for r in rows]
    gates = dict(successful_actual_producer=d['all_gates'] and all(d['gates'].values()),
        formal_success=usage['exitcode'] == 0 and usage['termination_signal'] is None,
        complete25_blocks=n == 25 and high['comparison_partition'] == finite['comparison_partition'] == d['comparison_partition'],
        complete17361_finite_positive_modes=[m for lo, hi in finite['windows'] for m in range(lo, hi+1, 2)] == list(range(94,34816,2)),
        complete_infinite_range=high['high_cutoff'] == 34816 and high['upper_frequency_cutoff'] is None and high['all_gates'],
        original_shared_strip=high['common_strip'] == finite['fixed_common_strip'] == d['fixed_common_strip'],
        same_source_inputs=all(d['input_hashes'][str(getattr(a,k))] == sha(getattr(a,k)) for k in ('finite','balanced','source','head')))
    checked = []; finite_physical = high_physical = F(0); max_domain = F(0)
    distance_gaps = []
    for i, r in enumerate(rows):
        if i != r['index'] or len(r['complete_causal_derivative_blocks']) != i+1:
            raise ValueError('Every causal row must be present')
        V = ex(r['V_max']); max_domain = max(max_domain, (C+radii[i])*V + (B*hradii[i] if i in special else V*hradii[i]))
        finite_physical += radii[i]*V
        high_physical += (B if i in special else V)*hradii[i]
        G = {p:[ex(v) for v in r['all_finite_source_materials'][str(p)]] for p in (2,1,0)}
        A = {p:[ex(v) for v in r['all_high_source_materials']['physical_source'][str(p)]] for p in (2,1,0)}
        Q = {p:[ex(v) for v in r['all_high_source_materials']['already_divided_by_frame'][str(p)]] for p in (2,1,0)}
        inputs_ok = all(G[p] == [ex(v['value']) for v in finite['rows'][i]['all_material_rows'][str(p)]] for p in (2,1,0))
        for j,sr in enumerate(high['rows'][i]['source_rows']):
            for dr in sr['density_rows']:
                value = ex(dr['balanced_strong_output_row']) if i in special else max(ex(dr['localV_strong_output_row']), ex(dr['P_sup'])+ex(dr['K_sup']))
                inputs_ok = inputs_ok and value == (A if dr['source_normalization']=='physical_source' else Q)[dr['V_power']][j]
        hf = sum((mass*ex(finite['rows'][i]['given_band_gains'][band]['gain']) for mass,band in zip(hm,('near','rest','infinite'))),F(0))
        cols = high['rows'][i]['initial_balanced_column_sups'] if i in special else high['rows'][i]['initial_localV_separate_component_sups']
        if i in special:
            hh = hm[2]*max(ex(cols[0])/boundary, ex(cols[1]))
        else:
            hh = hm[2]*max(sum(map(ex,cols[0]),F(0))/boundary,sum(map(ex,cols[1]),F(0)))
        image_f = hf+centre*sum(G[2],F(0))
        image_h = hh+tail*sum(A[2],F(0))
        jf = jh = F(0); derivatives_ok = True
        for j in range(i+1):
            rj,hj = radii[j],hradii[j]
            if j in special:
                image_f += G[2][j]*(40*rj+2*rj*rj)+4*G[1][j]*(C+rj)*B*hj+2*G[0][j]*B*B*hj*hj
                image_h += A[2][j]*(40*rj+2*rj*rj)+4*Q[1][j]*D*(C+rj)*hj+2*Q[0][j]*D*B*hj*hj
                J = (4*((C+rj)*G[2][j]+B*hj*G[1][j]),
                     4*B*((C+rj)*G[1][j]+B*hj*G[0][j]),
                     4*(C+rj)*A[2][j]+16*D*hj*Q[1][j],
                     4*D*((C+rj)*Q[1][j]+B*hj*Q[0][j]))
            else:
                t = rj+hj
                image_f += G[2][j]*(40*t+2*t*t)
                image_h += A[2][j]*(40*t+2*t*t)
                J = (4*(C+t)*G[2][j],4*(C+t)*G[2][j],4*(C+t)*A[2][j],4*(C+t)*A[2][j])
            derivatives_ok = derivatives_ok and J == tuple(map(ex,r['complete_causal_derivative_blocks'][j]))
            jf += J[0]*weights[j][0]+J[1]*weights[j][1]
            jh += J[2]*weights[j][0]+J[3]*weights[j][1]
        df,dh = jf/weights[i][0],jh/weights[i][1]
        distance_gaps.extend([F(1,2)-df,F(1,2)-dh])
        local = dict(all_kernel_columns_same_exact_inputs=inputs_ok,
            all_complete_mean_derivatives_reproduced=derivatives_ok,
            both_full_images_reproduced=image_f == ex(r['complete_finite_image']) and image_h == ex(r['complete_high_image']),
            all_shared_head_and_centre_masses_once_per_output=hf+centre*sum(G[2],F(0)) == ex(r['true_finite_head_and_centre']) and hh+tail*sum(A[2],F(0)) == ex(r['true_high_head_and_complete_centre']),
            two_strict_selfmaps=image_f < radii[i] and image_h < hradii[i],
            both_complete_weighted_rows_reproduced=df == ex(r['finite_complete_weighted_distance_row']) and dh == ex(r['high_complete_weighted_distance_row']),
            both_complete_distances_strictly_below_half=max(df,dh) < F(1,2),
            whole_domain_below_two_minus34=ex(r['actual_complete_mean_domain']) == (C+radii[i])*V+(B*hradii[i] if i in special else V*hradii[i]) < F(2)**-34)
        checked.append(dict(index=i,gates=local))
    gates.update(all25_exact_row_checks=all(all(r['gates'].values()) for r in checked),
        exact_finite_physical_total=finite_physical == ex(d['complete_finite_physical_norm_upper']),
        exact_high_physical_total=high_physical == ex(d['complete_high_physical_norm_upper']),
        exact_whole_domain=max_domain == ex(d['maximum_whole_ball_physical_domain']),
        combined_physical_cap_below_two_minus42=finite_physical+high_physical < F(2)**-42)
    result = dict(schema='visible-flex-r122-independent-exact-substitution-v1',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=all(gates.values()),gates=gates,rows=checked,
        minimum_strict_distance_gap_to_half=rec(min(distance_gaps)),
        complete_finite_physical_norm_upper=rec(finite_physical),complete_high_physical_norm_upper=rec(high_physical),
        combined_physical_norm_upper=rec(finite_physical+high_physical),maximum_physical_domain=rec(max_domain),
        combined_physical_cap_below_two_minus43=finite_physical+high_physical < F(2)**-43,
        no_radius_search=True,no_new_Arb_or_ODE=True,
        input_hashes={str(getattr(a,n)):sha(getattr(a,n)) for n in ('primary','resource','finite','high','balanced','source','head')},
        source_sha256=sha(__file__),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    if not result['all_gates']:
        raise ArithmeticError('A complete exact substitution failed')
    print(json.dumps(dict(all_gates=True,rows=n,minimum_strict_distance_gap=float(min(distance_gaps)),
        combined_physical=float(finite_physical+high_physical))),flush=True)


if __name__ == '__main__':
    main()
