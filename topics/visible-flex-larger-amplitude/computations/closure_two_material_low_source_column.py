#!/usr/bin/env python3
"""Reuse an actual-position source12 radial integral for all deeper targets.

All46 independent psi source integrals are already certified. This tool
reads the unchanged true phi columns and complete panel output caps, and
forms the independent d1 column of the strong low Green operator. There
is no new source evaluation, radial quadrature, or fundamental flow.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gc
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import ball_record, power2
from closure_real_head_green_enclosure import ball, endpoint
from closure_split_joint_io_v2 import digest, read, read_field, iter_array, metadata_without_array
from tail_high_two_material_kernel import Monitor


def compact(x):
    return arb(int(x[0]))*power2(int(x[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-integrals', 'low', 'columns', 'ordered', 'density', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--rss-limit-mib', type=int, default=120)
    args = parser.parse_args()
    ctx.prec = 192
    start = time.monotonic()
    monitor_path = args.out.with_name(args.out.stem+'-monitor.jsonl')
    if args.out.exists() or monitor_path.exists():
        raise FileExistsError('Use a fresh complete source-column prefix')
    monitor = Monitor(monitor_path, args.rss_limit_mib)
    hashes = {str(getattr(args,name)):digest(getattr(args,name)) for name in
              ('source_integrals','low','columns','ordered','density')}
    source = read(args.source_integrals)
    columns = read(args.columns)
    ordered = read(args.ordered)
    density = read(args.density)
    modes = list(range(2,93,2))
    cells = list(range(12,225))
    if source['source_cell'] != 12 or not source['full_low46_window_covered'] or source['modes'] != modes:
        raise ValueError('The complete true source12 psi integral window is required')
    for p in (args.low,args.density):
        if source['input_hashes'].get(str(p)) != hashes[str(p)]:
            raise ValueError('The certified source integral belongs to another source/norm')
    low_hashes = read_field(args.low,'input_hashes')
    for p in (args.columns,args.ordered,args.density):
        if hashes[str(p)] not in low_hashes.values():
            raise ValueError('The true low columns or strong physical norm differ')
    if columns['modes'] != modes or not all(density['gates'].values()):
        raise ValueError('All46 columns and the actual common-strip domain are required')
    if [r['cell'] for r in density['rows']] != cells:
        raise ValueError('The full213 physical norm is absent')
    Bsource = ball(density['rows'][0]['B']).lower()
    if not Bsource >= 120 or not ball(source['w_upper']).upper() <= arb(1)/2:
        raise ValueError('The independently paid material coefficient domain changed')
    den = {r['cell']:r for r in density['rows']}
    sigma = {r['cell']:ball(r['sigma']) for r in iter_array(args.low,'source_profiles')}
    if sorted(sigma) != cells:
        raise ValueError('The complete strong rescaling is unavailable')
    combined = []
    for row in iter_array(args.low,'corr'):
        if len(row) != len(cells):
            raise ValueError('A complete low corr row is absent')
        combined.append(compact(row[0]))
    if len(combined) != len(cells):
        raise ValueError('The complete corr source column is absent')
    refined = {(r['mode'],c['cell']):c for r in ordered['mode_rows'] for c in r['refined_cells']}
    panel_hashes = read_field(args.low,'panel_hashes')
    panel_caps = {}
    for name, expected in panel_hashes.items():
        path = Path(name)
        if digest(path) != expected:
            raise ValueError('An actual completed output panel provider changed')
        doc = read(path)
        if doc['modes'] != modes:
            raise ValueError('An output cap omits modes')
        for row in doc['rows']:
            panel_caps[(doc['cell'],row['mode'])] = (
                ball(row['phi_physical_p_sup']).upper(),
                ball(row['phi_physical_kappa_sup']).upper())
    source_rows = {r['mode']:r for r in source['rows']}
    maxima = {n:arb(0) for n in cells[1:]}
    witnesses = {n:None for n in cells[1:]}
    group_hashes = {}
    seen_modes = []
    monitor.record('inputs',target_cells=len(maxima),source_modes=len(source_rows))
    del ordered,doc,columns['endpoint_rows']
    gc.collect()
    for group in columns['column_groups']:
        path = Path(group['path'])
        gh = digest(path)
        if gh != group['sha256']:
            raise ValueError('An exact signed true-column group changed')
        group_hashes[str(path)] = gh
        meta = metadata_without_array(path,'cell_rows')
        gains = []
        for j,m in enumerate(meta['modes']):
            if m in seen_modes or m not in modes:
                raise ValueError('A column frequency is repeated or outside the real window')
            seen_modes.append(m)
            record = meta['endpoint_rows'][j]['Q_gain']
            lo,hi = endpoint(record['lower']),endpoint(record['upper'])
            if not (lo>0 or hi<0):
                raise ValueError('A true shallow height chart contains zero')
            gains.append(lo if lo>0 else -hi)
        count = 0
        for index, row in enumerate(iter_array(path,'cell_rows')):
            n = row['cell']
            if n != cells[index]:
                raise ValueError('An entire true radial cell is missing or reordered')
            count += 1
            if n == 12:
                continue
            d = den[n]
            X = ball(d['canonical_total_envelope']).lower()
            B = ball(d['B']).upper()
            a = ball(d['Q_coefficient']).lower()
            tau = ball(d['tau_inner']).upper()
            if not min(X,a,sigma[n].lower()) > 0:
                raise ValueError('An actual physical output normalization is nonpositive')
            for j,m in enumerate(meta['modes']):
                lin = row['linear_rows'][j]
                q = (ball(lin['column_Q_sup']).upper()/gains[j]).upper()
                xi = (ball(lin['column_Xi_sup']).upper()/gains[j]).upper()
                old = refined.get((m,n))
                if old is not None:
                    q = min(q,ball(old['refined_phi_Q_sup']).upper())
                    xi = min(xi,ball(old['refined_phi_Xi_sup']).upper())
                angle = (m*tau).exp().upper()
                pp = ((1+m)*B*m*q/(X*a)*angle).upper()
                kk = ((1+m)*(m*m*q/a+xi)/X*angle).upper()
                cap = panel_caps.get((n,m))
                if cap is not None:
                    pp = min(pp,(cap[0]/sigma[n].lower()).upper())
                    kk = min(kk,(cap[1]/sigma[n].lower()).upper())
                sr = source_rows[m]
                value = (ball(sr['source_mu_ratio']).upper()*(pp+kk)*
                         ball(sr['radial_psi_Q_source_integral']).upper()).upper()
                if value > maxima[n]:
                    maxima[n],witnesses[n] = value,m
        if count != len(cells):
            raise ValueError('The true radial column coverage is incomplete')
        monitor.record('column-group',modes=meta['modes'])
    if sorted(seen_modes) != modes:
        raise ValueError('The union of true modal columns is incomplete')
    rows = []
    for k,n in enumerate(cells[1:],1):
        radial = min(combined[k],maxima[n])
        near = (arb(5)/2*radial+arb(2)/285*combined[k]).upper()
        low = (arb(5)/2*radial+arb(2)/9*combined[k]).upper()
        rows.append(dict(output_cell=n,source_cell=12,complete_modes=modes,
            independent_radial_corr=ball_record(maxima[n]),radial_worst_mode=witnesses[n],
            chosen_radial_corr=ball_record(radial),combined_corr=ball_record(combined[k]),
            DQ_corr_from_low=ball_record(low),DQ_corr_from_near=ball_record(near),
            near_ratio_to_original=ball_record(near/(3*combined[k]))))
    result = dict(status='Complete actual-position radial corr source12 column to every deeper true target',
        source_cell=12,target_cells=cells[1:],modes=modes,full46_and_all_deeper_targets=True,
        excluded='Same source/output cell12 requires an ordered diagonal. All other source columns and all far-z rows remain their previous paid values.',
        low_and_near_coefficients='Independent d1 carries5/2; the previous positive combined corr kernel bounds d_lambda and carries2/9 or2/285 respectively. Main, quadratic variation and216 remainder remain separate.',
        source_epsilon_and_material_unchanged=True,continuous_strip_unchanged=True,
        new_source_values=0,new_radial_quadratures=0,new_fundamental_flows=0,
        rows=rows,input_hashes=hashes,group_hashes=group_hashes,panel_hashes=panel_hashes,
        source_sha256=digest(Path(__file__)),helper_hashes={name:digest(Path(__file__).with_name(name)) for name in
            ('closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py',
             'closure_split_joint_io.py','closure_split_joint_io_v2.py','tail_high_two_material_kernel.py')},
        full_joint_gate_paid=False,elapsed_seconds=time.monotonic()-start,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload = (json.dumps(result,separators=(',',':'))+'\n').encode()
    if args.out.suffix == '.gz':
        payload = gzip.compress(payload,mtime=0)
    if len(payload) >= 5_000_000:
        raise ArithmeticError('Repository individual-file cap exceeded')
    args.out.write_bytes(payload)
    event = monitor.record('done',output=str(args.out),target_count=len(rows))
    print(json.dumps(dict(**event,source_cell=12,
        sample_near_ratios={str(r['output_cell']):r['near_ratio_to_original']['display'] for r in rows[:4]})),flush=True)


if __name__ == '__main__':
    main()
