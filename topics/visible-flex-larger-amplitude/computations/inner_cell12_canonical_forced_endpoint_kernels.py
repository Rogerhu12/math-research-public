#!/usr/bin/env python3
"""True cell12 forced endpoint columns from saved cooperative cell matrices.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original comparison generator is entrywise nonnegative, including its
diagonal. Its complete cell matrix therefore bounds every suffix. All
source material is retained. No new ODE, radial quadrature or source field
evaluation is performed. These columns are separate from homogeneous ones.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_split_joint_io_v2 import iter_array, metadata_without_array
from inner_true_cell13_endpoint_window_kernels import (
    sha, read, exact, aq, ab, ball, pack, up, lower_pack, Gates,
    closed_port_w, WINDOWS, MATERIALS)


PINS = {
    'panels': ('2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell012.json.gz',
               'd0dc6791001a1668afa2f9442bbefbe7e6644e73b0b753943df5a9bc12258181'),
    'qdensity': ('2026-11-12-tail-r33-plateau2-density-window.json.gz',
                 '0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9'),
    'density': ('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz',
                'e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
    'positive': ('2026-11-12-closure-positive-highband-38.json.gz',
                 'cf293799252e8beb9ef15ff27dba1ebbe698186cee3258b6f9df34ab8dff5600'),
    'ready': ('2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json',
              '563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6'),
}
SOURCE_PINS = {
    'inner_true_cell13_endpoint_window_kernels.py': 'cff396cf882488df91c5450490a0c345e408d3fe1a6b29f683910e97b7aa4019',
    'closure_split_joint_io_v2.py': '6cbcb8cf69a39d8df5d10be35a29b941b47fd66456364eb90fab7bbb22b386f0',
    'closure_split_joint_io.py': 'cd03e2fc375e19c8b4d291b601e423a37c584a3e4402957c9f377e82b8cce390',
    'closure_positive_linear_band_enclosure.py': '270e475e33f988ca9d48c1f68e249f2d127fa3afafd3e3d20d80cce3407a170f',
    'closure_real_linear_head_enclosure.py': '1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e',
    'closure_real_head_source_enclosure.py': '97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47',
}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--rss-kib', type=int, default=98304)
    a = p.parse_args(); ctx.prec = 256; ctx.threads = 1
    started = time.monotonic(); gates = Gates(); check = gates.check
    out = Path(str(a.out_prefix)+'.json')
    if out.exists(): raise FileExistsError('Use a fresh immutable forced endpoint')
    ids = {}; paths = {}
    for name, (base, wanted) in PINS.items():
        path = a.inputs/base; check('all_original_input_sha256', sha(path) == wanted)
        ids[name] = {'path': str(path), 'sha256': wanted, 'bytes': path.stat().st_size}
        paths[name] = path
    for name, wanted in SOURCE_PINS.items():
        check('original_cooperative_generator_and_helpers_sha256', sha(Path(__file__).parent/name) == wanted)
    density, qdensity, ready = (read(paths[k]) for k in ('density','qdensity','ready'))
    check('all_original_density_gates', all(density['gates'].values()) and all(qdensity['gates'].values()))
    meta = metadata_without_array(paths['panels'], 'panels')
    pm = metadata_without_array(paths['positive'], 'cell_rows')
    r = next(z for z in density['rows'] if z['cell'] == 12)
    qr = next(z for z in qdensity['rows'] if z['cell'] == 12)
    Arows = next(z for z in iter_array(paths['positive'], 'cell_rows') if z['cell'] == 12)['positive_cell_matrices']
    check('same_ready_geometry', PINS['ready'][1] in pm['input_hashes'].values() and PINS['ready'][1] in meta['input_hashes'].values())
    check('same_original_qdensity', PINS['qdensity'][1] in meta['input_hashes'].values() and PINS['qdensity'][1] in density['input_hashes'].values())
    for name in ('closure_positive_linear_band_enclosure.py','closure_real_linear_head_enclosure.py','closure_real_head_source_enclosure.py'):
        check('original_positive_matrix_generator_identity', pm['source_hashes'][name] == SOURCE_PINS[name])
    for key in ('tau_inner','tau_outer','reference_tau','B'):
        check('same_whole_variable_strip_and_frame', qr[key] == r[key])
    for key in ('tau_inner','tau_outer','B'):
        check('same_saved_panel_strip_and_frame', meta[key]['lower'] == qr[key]['lower'] and meta[key]['upper'] == qr[key]['upper'])
    x = exact(r['canonical_total_envelope']); xq = exact(qr['canonical_total_envelope'])
    check('exact_positive_Xbar_scales', x == exact(r['canonical_total_envelope'],'lower') > 0 and xq == exact(qr['canonical_total_envelope'],'lower') > 0)
    sigma = x/xq; S = F(257,256); scale2 = up(aq((S*sigma)**2))
    mu = ball(meta['mu']); mulo = mu.lower(); muhi = mu.upper(); Bhi = ab(r['B'])
    check('same_actual_mu', ab(r['mu_lower'],'lower') <= mulo and muhi <= ab(r['mu_upper']))
    tauout = ab(meta['tau_outer']); check('exact_output_strip', exact(meta['tau_outer']) == exact(meta['tau_outer'],'lower'))
    port = closed_port_w(ready,12); wlo = port['w'].lower(); whi = port['w'].upper()
    check('strict_true_conversion_denominators', mulo > 0 and wlo > 0 and ab(r['B'],'lower') >= 120)
    rc = aq(ready['rationalDeepModel']['physicalParameters']['rCuff']); R = rc*257/256
    rows = []; uncovered = []
    for lo, hi in WINDOWS:
        covers = [j for j,z in enumerate(pm['bands']) if z['first_mode'] <= lo and hi <= z['last_mode']]
        if not covers:
            uncovered.append([lo,hi]); continue
        j = covers[0]; A = [[ab(z) for z in row] for row in Arows[j]]
        check('all_cooperative_matrix_entries_nonnegative', all(z.is_finite() and z >= 0 for row in A for z in row))
        check('complete_cell_matrix_at_least_identity', A[0][0] >= 1 and A[1][1] >= 1)
        rows.append({'window':[lo,hi], 'matrix_index':j, 'A':A,
                     'I':{z:arb(0) for z in MATERIALS}, 'Iweighted':{z:arb(0) for z in MATERIALS}})
    check('exact_original_nine_window_cover', len(pm['bands']) == 9 and len(rows) == 11 and uncovered == [[2050,4096],[4098,8190]])
    count = 0; segment = 0; endpoint = F(0); segment_counts = [0]*9; first = last = None
    for g in iter_array(paths['panels'],'panels'):
        j = g['segment']; left,right = F(*g['x_left']),F(*g['x_right'])
        if j == segment: check('original_panel_exact_order', left == endpoint)
        else:
            check('complete_original_segment_transition', j == segment+1 and endpoint == 1 and left == 0)
            segment = j
        check('strict_original_panel_range', 0 <= left < right <= 1)
        endpoint = right; count += 1; segment_counts[j] += 1
        if first is None: first = g
        last = g
        rr, vv = ball(g['radius']), ball(g['V'])
        radial, variation = ab(g['radial_log_increment']), ab(g['log_w_variation'])
        common = ab(g['canonical_source_integral'])
        check('all_true_positive_panel_materials', rr.lower() > 0 and vv.lower() > 0 and radial > 0 and variation >= 0 and common > 0)
        check('original_global_radius_domain', rr.lower() >= rc and rr.upper() <= R)
        prefactor = up(rr.upper()**4*vv.upper()**2/(arb(12).sqrt()*mulo))
        material = {'d1':up(min(prefactor*radial,common)), 'd_lambda':up(min(prefactor*variation,common))}
        remaining = max(arb(0), (ab(g['tau_range'],'lower')-tauout).lower())
        check('remaining_strip_is_only_actual_panel_to_endpoint', remaining >= 0 and remaining <= ab(meta['tau_inner'])-tauout)
        for row in rows:
            lo = row['window'][0]; decay = up((-lo*remaining).exp())
            check('remaining_angular_weight_in_unit_interval', 0 < decay <= 1)
            for mat in MATERIALS:
                row['I'][mat] = up(row['I'][mat]+material[mat])
                row['Iweighted'][mat] = up(row['Iweighted'][mat]+decay*material[mat])
        if count % 256 == 0:
            check('owned_small_RSS_guard', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss <= a.rss_kib)
            print(json.dumps({'event':'canonical_forced_source_panels','complete':count,'elapsed_seconds':time.monotonic()-started}),flush=True)
    check('complete_1873_panels_and_all_nine_segments', count == 1873 and segment == 8 and endpoint == 1 and all(z > 0 for z in segment_counts))
    rout = ball(last['radius_right']); check('strict_true_cut_radius', rout.lower() > 0)
    result_rows = []
    for row in rows:
        lo,hi = row['window']; j = row['matrix_index']; A = row['A']
        nulo = arb(lo*lo*(lo*lo-1))/12; nuhi = arb(hi*hi*(hi*hi-1))/12
        cout = [(Bhi*hi+hi*hi)*rout.upper()**3,
                arb(12).sqrt()*muhi*nuhi/(rout.lower()**4*wlo)]
        gain = up(2*(1+hi)*scale2/nulo*(cout[0]*A[0][1]+cout[1]*A[1][1]))
        absolute = {mat:up(gain*row['Iweighted'][mat]) for mat in MATERIALS}
        oldabsolute = {mat:up(gain*row['I'][mat]) for mat in MATERIALS}
        relative = {mat:up(absolute[mat]/wlo) for mat in MATERIALS}
        oldrelative = {mat:up(oldabsolute[mat]/wlo) for mat in MATERIALS}
        for mat in MATERIALS:
            check('weighted_source_column_not_larger_than_unweighted', relative[mat] <= oldrelative[mat])
        result_rows.append({'window':[lo,hi], 'original_matrix_window':[pm['bands'][j]['first_mode'],pm['bands'][j]['last_mode']],
            'original_matrix_index':j, 'whole_cell_positive_matrix_upper':[[pack(z) for z in r] for r in A],
            'canonical_whole_cell_material_integral_upper':{m:pack(row['I'][m]) for m in MATERIALS},
            'canonical_remaining_strip_material_integral_upper':{m:pack(row['Iweighted'][m]) for m in MATERIALS},
            'nu_lower':lower_pack(nulo), 'nu_upper':pack(nuhi), 'physical_output_covector_upper':list(map(pack,cout)),
            'absolute_endpoint_source_gain_upper':pack(gain),
            'source_two_material_to_absolute_endpoint':{m:pack(absolute[m]) for m in MATERIALS},
            'source_two_material_to_cut':{m:pack(relative[m]) for m in MATERIALS},
            'unweighted_whole_cell_two_material_to_cut':{m:pack(oldrelative[m]) for m in MATERIALS},
            'source_common_to_cut':pack(relative['d1']+relative['d_lambda'])})
    check('owned_final_RSS_guard', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss <= a.rss_kib)
    result = {'schema':'inner-true-cell12-canonical-forced-endpoint-two-material-v1',
        'author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)','all_gates':True,'gate_count':gates.count,
        'gates':{k:True for k in gates.by_name},'gate_multiplicities':gates.by_name,
        'source_sha256':sha(__file__),'input_identities':ids,'frozen_reference_source_sha256':SOURCE_PINS,
        'cell':12,'panels':count,'segment_panel_counts':segment_counts,
        'same_original_variable_strip':True,'normalization_S':'257/256',
        'exact_strong_to_q_Xbar_ratio':str(sigma),'source_scale_squared_upper':pack(scale2),
        'tau_output':meta['tau_outer'],'true_w_out_lower':lower_pack(wlo),'true_w_out_upper':pack(whi),
        'physical_output_radius':last['radius_right'],'source_mu':meta['mu'],
        'source_units':'Weak paired Fourier coefficient in the original moving tau, multiplying d1=Vprime^2/(r*w) or d_lambda=abs(w_r/w)*Vprime^2/w in the physical kappa source. Vprime=(257/256)*sigma12*Vq; scale squared is included once.',
        'output_units':'source_two_material_to_cut bounds sum(1+m)*exp(m*tauout)*(abs(B12*p_m)+abs(kappa_m))/w_true_out. source_two_material_to_absolute_endpoint omits only the final division by true w.',
        'canonical_source_identity':'Xi source = r^4*w/(sqrt(12)*mu12) times physical kappa source. The source in (Q,Xi/nu) is (0,I_mat/nu).',
        'suffix_proof':'Original comparison M=[[d,nu*a],[b0,d]], d=(m^2-4)*r_x/r>=0 and a,b0>0. Its every prefix is entrywise>=I, so Phi(b,s)<=Phi(b,a)<=the saved full positive cell matrix. This statement is about the nonnegative comparison evolution, not signed original flow.',
        'remaining_strip_proof':'For source at y in a saved panel, exp(m*(tauout-tau(y)))<=exp(-lo*max(0,tau_panel_lower-tauout)). No whole-cell angular decay is attached to generated source.',
        'factor_two_retained':True,'uncovered_windows_keep_original_kernels':uncovered,
        'shared_window_mass_rule':'For a shared source mass use max of the selected window columns once; for two distinct material masses keep their two columns. Entrywise minima with any independently valid same-unit source columns are allowed.',
        'infinite_far_mean_inverse_source_bounds_changed':False,'same_R100_or_restricted_field_only_after_actual_source_consumer':True,
        'new_fixedpoint_or_cut_consistency_claimed':False,'new_ODE_radial_quadrature_source_evaluation_Node_calls':0,
        'rows':result_rows,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    out.parent.mkdir(parents=True,exist_ok=True);data=(json.dumps(result,indent=2)+'\n').encode()
    check('small_output_file',len(data)<1000000);out.write_bytes(data)
    print(json.dumps({'all_gates':True,'path':str(out),'sha256':sha(out),'bytes':len(data),'gate_count':result['gate_count'],
        'first_source_columns':{m:str(ab(result_rows[0]['source_two_material_to_cut'][m])) for m in MATERIALS},
        'elapsed_seconds':result['elapsed_seconds'],'peak_rss_kib':result['peak_rss_kib']}),flush=True)


if __name__ == '__main__': main()
