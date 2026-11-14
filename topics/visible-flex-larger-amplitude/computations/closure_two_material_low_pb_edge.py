#!/usr/bin/env python3
"""Retain the actual source position in the independent radial low kernel.

Only the shallow Dirichlet column psi in source cell12 is recomputed.  It
starts at the true outer port with (Q,Xi)=(0,1); no deep-column or radius
quadrature is needed.  The same certified material panels, fixed real
source, 192-bit arithmetic and PB subdivision criterion are retained.
The output is a source integral and an edge bound, not a joint-box proof.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gc
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import ball_record, power2
from closure_real_head_green_enclosure import ball, mv, inverse_unimodular
from closure_real_linear_head_enclosure import PositiveKernels, peano_matrix
from closure_projective_interval_column import ProjectiveColumn
from closure_weighted_panel_flow_v4 import prepare_cell
from closure_split_joint_io import digest, read, iter_array
from tail_r33_middle_ordered_physical import SourceValues
from tail_high_two_material_kernel import Monitor


def only_row(path, key, cell):
    result = None
    for row in iter_array(path, key):
        if row['cell'] == cell:
            if result is not None:
                raise ValueError('A source cell appears more than once')
            result = row
    if result is None:
        raise ValueError('A required certified cell is absent')
    return result


def psi_source_integral(kernels, parents, mode, outer_radius, cap_q, monitor):
    """The exact same projective PB flow, with only the needed Q bound."""
    exponent = mode*mode-4
    column = ProjectiveColumn([arb(0), (outer_radius/kernels.head.rc)**exponent])
    total = arb(0)
    maximum_q = arb(0)
    largest_panel = arb(0)
    witness = None
    for j in range(len(parents)-1, -1, -1):
        parent = parents[j]
        qcap = arb(0)
        for piece in reversed(parent['pieces']):
            A, B = kernels.mode_integrals(piece, mode)
            T, major, _ = peano_matrix(A, B)
            within = mv(major, column.absolute_uppers())
            candidate = (abs((piece['r']/kernels.head.rc)**exponent).upper()*within[0]).upper()
            qcap = max(qcap, min(candidate, cap_q))
            column.advance(inverse_unimodular(T))
        contribution = (qcap*parent['radial_corr']*(-mode*parent['tau'].lower()).exp()).upper()
        total = (total+contribution).upper()
        maximum_q = max(maximum_q, qcap)
        if contribution > largest_panel:
            largest_panel = contribution
            witness = dict(panel=j, segment=parent['segment'], x_left=parent['x_left'],
                           x_right=parent['x_right'], radius=ball_record(parent['radius']),
                           tau=ball_record(parent['tau']))
        if j % 256 == 0:
            monitor.record('mode-panel', mode=mode, remaining_panel=j)
    return total, maximum_q, largest_panel, witness


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('cheap-edge', 'strong-low', 'strong-density', 'strong-reference',
                 'source-panel', 'target-panel', 'material', 'ready', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--only-mode', type=int)
    parser.add_argument('--rss-limit-mib', type=int, default=120)
    args = parser.parse_args()
    ctx.prec = 192
    started = time.monotonic()
    monitor_path = args.out.with_name(args.out.stem+'-monitor.jsonl')
    recovery_path = args.out.with_name(args.out.stem+'-completed-modes.json')
    if any(p.exists() for p in (args.out, monitor_path, recovery_path)):
        raise FileExistsError('Use a fresh PB radial-edge output prefix')
    monitor = Monitor(monitor_path, args.rss_limit_mib)
    hashes = {str(getattr(args, name)): digest(getattr(args, name)) for name in
              ('cheap_edge', 'strong_low', 'strong_density', 'strong_reference',
               'source_panel', 'target_panel', 'material', 'ready')}
    cheap = read(args.cheap_edge)
    for name in ('strong_low', 'strong_density', 'strong_reference', 'source_panel',
                 'target_panel', 'material'):
        path = str(getattr(args, name))
        if cheap['input_hashes'].get(path) != hashes[path]:
            raise ValueError('The independently certified edge input changed')
    n, k = cheap['source_cell'], cheap['target_cell']
    if n != 12 or not 12 < k <= 23:
        raise ValueError('This minimal adapter proves source12 to a deeper shallow cell')
    modes = list(range(2, 93, 2))
    if cheap['modes'] != modes:
        raise ValueError('The complete reference edge is not the low46 problem')
    if args.only_mode is not None:
        if args.only_mode not in modes:
            raise ValueError('The requested mode is outside the paid low window')
        modes = [args.only_mode]
    source, target = read(args.source_panel), read(args.target_panel)
    if source['cell'] != n or target['cell'] != k:
        raise ValueError('The original true column providers differ')
    if source['input_hashes'].get(str(args.ready)) != hashes[str(args.ready)]:
        raise ValueError('The exact source definition changed')
    sn_profile = only_row(args.strong_low, 'source_profiles', n)
    sk_profile = only_row(args.strong_low, 'source_profiles', k)
    density = only_row(args.strong_density, 'rows', n)
    reference = only_row(args.strong_reference, 'cell_rows', n)
    sn, sk = ball(sn_profile['sigma']), ball(sk_profile['sigma'])
    rest = ball(sn_profile['canonical_rest']).upper()
    X = ball(density['canonical_total_envelope']).lower()
    tau_ref = ball(reference['tau']).lower()
    combined = ball(cheap['combined_corr_upper']).upper()
    B = ball(density['B']).lower()
    if not min(X, sn.lower(), sk.lower()) > 0 or not B >= 120:
        raise ValueError('A required positive scale or two-material domain changed')
    material = read(args.material)
    if source['input_hashes'].get(str(args.material)) != hashes[str(args.material)]:
        raise ValueError('The original PB flow used another actual material set')
    if material['cell'] != n or len(material['panels']) != cheap['panels']:
        raise ValueError('The true cell12 material coverage changed')
    mu = ball(material['mu']).lower()
    root = arb(12).sqrt()
    head = SourceValues(read(args.ready))
    kernels = PositiveKernels(head, 225, 92)
    monitor.record('inputs', modes=modes, cell=n, panel_count=len(material['panels']))
    # SourceValues has the identical RealHead source methods but performs no
    # constructor radius integrals. Every physical radius below is already
    # enclosed by the original material panel, refined by its exact positive
    # width formula in the unchanged prepare_cell implementation.
    parents, pieces, product = prepare_cell(kernels, n, material, power2(-20))
    outer_radius = ball(material['panels'][-1]['radius_right'])
    if material['panels'][-1]['segment'] != 8 or material['panels'][-1]['x_right'] != [1, 1]:
        raise ValueError('The actual shallow port is not the complete cell endpoint')
    wmax = arb(0)
    for parent, raw in zip(parents, material['panels']):
        V = (sn.upper()*ball(raw['V']).upper()).upper()
        tau = parent['tau']
        if not tau_ref >= tau.upper():
            raise ValueError('The strong wide centre no longer contains the common strip')
        eps = (rest/X*(-2*(tau_ref-tau.upper())).exp()).upper()
        J1 = (parent['radius'].upper()**4*V**2/(root*mu)*
              ball(raw['radial_log_increment']).upper()).upper()
        parent['radial_corr'] = (J1*eps).upper()
        wmax = max(wmax, parent['w'].upper())
    if not wmax <= arb(1)/2:
        raise ValueError('The full two-material w domain is unpaid')
    del material
    gc.collect()
    monitor.record('prepared', cell=n, PB_pieces=pieces, maximum_AB=str(product))
    source_rows = {r['mode']: r for r in source['rows']}
    target_rows = {r['mode']: r for r in target['rows']}
    source_names = [Path(__file__).name, 'closure_weighted_panel_flow_v4.py',
        'closure_weighted_panel_low_green_v3.py', 'closure_real_head_source_enclosure.py',
        'closure_real_linear_head_enclosure.py', 'closure_real_head_green_enclosure.py',
        'closure_projective_interval_column.py', 'closure_split_joint_io.py',
        'tail_r33_middle_ordered_physical.py', 'tail_high_two_material_kernel.py']
    source_hashes = {name: digest(Path(__file__).with_name(name)) for name in source_names}
    rows = []
    maximum = arb(0)
    witness = None
    for m in modes:
        sr, tr = source_rows[m], target_rows[m]
        integral, qcap, panelmax, panelwitness = psi_source_integral(
            kernels, parents, m, outer_radius, ball(sr['psi_Q_sup']).upper(), monitor)
        output_norm = ((ball(tr['phi_physical_p_sup']).upper()+
                        ball(tr['phi_physical_kappa_sup']).upper())/sk.lower()).upper()
        value = (ball(sr['mu_ratio']).upper()*output_norm*integral).upper()
        if value > maximum:
            maximum, witness = value, m
        row = dict(mode=m, radial_psi_Q_source_integral=ball_record(integral),
            psi_Q_sup=ball_record(qcap), source_mu_ratio=sr['mu_ratio'],
            target_physical_norm=ball_record(output_norm),
            independent_radial_corr_edge=ball_record(value),
            largest_source_panel_integral=ball_record(panelmax),
            largest_source_panel=panelwitness)
        rows.append(row)
        recovery_path.write_text(json.dumps(dict(
            status='Recovery-only completed modal source integrals; uncompleted modes have no new bound',
            source_cell=n, target_cell=k, modes_completed=[r['mode'] for r in rows],
            rows=rows, input_hashes=hashes, source_hashes=source_hashes), indent=2)+'\n')
        event = monitor.record('mode-complete', mode=m,
            edge_log2=str(value.log()/arb(2).log()), seconds_total=time.monotonic()-started)
        print(json.dumps(event), flush=True)
    complete = modes == list(range(2, 93, 2))
    chosen = min(combined, maximum)
    near = (arb(5)/2*chosen+arb(2)/285*combined).upper()
    low = (arb(5)/2*chosen+arb(2)/9*combined).upper()
    result = dict(status='Certified actual-position independent radial corr edge for exactly the listed modes',
        source_cell=n, target_cell=k, modes=modes, full_low46_window_covered=complete,
        source_panels=len(parents), PB_pieces=pieces, maximum_AB=ball_record(product),
        true_outer_radius=ball_record(outer_radius), exact_psi_boundary='Q=0, Xi=1 at the true cell12 outer port',
        mode_maximum_radial_corr_edge=ball_record(maximum), worst_mode=witness,
        combined_full46_corr_upper=ball_record(combined),
        chosen_radial_corr_upper_for_listed_modes=ball_record(chosen),
        DQ_corr_low_from_near_for_listed_modes=ball_record(near),
        DQ_corr_low_from_low_for_listed_modes=ball_record(low),
        ratio_new_near_to_old_for_listed_modes=ball_record(near/(3*combined)),
        coefficient_scope='d1 carries5/2; the old positive combined corr kernel separately bounds d_lambda and carries2/285 for near input or2/9 for low input. No coefficient is applied to a combined source fraction.',
        normalization='Strong V and auxiliary-centre epsilon on the original q continuous tau; canonical d1 integral r^4 V^2 epsilon/(sqrt12 mu) dr/r, with actual psi_Q and exp(-m tau) retained per source panel.',
        complete_mean_and_inverse_unchanged=True, full213_joint_gate_paid=False,
        scalar_flow_kernel_integrations=kernels.integral_count,
        new_background_radius_integrations=0, rows=rows,
        B_lower=ball_record(B), w_upper=ball_record(wmax),
        input_hashes=hashes, source_hashes=source_hashes,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    monitor.record('done', output=str(args.out))
    print(json.dumps(dict(event='done', output=str(args.out), modes=modes,
        full_low46_window_covered=complete, radial_log2=str(maximum.log()/arb(2).log()),
        new_near_over_old=str(near/(3*combined)), seconds=result['elapsed_seconds'],
        RSS_KiB=result['peak_RSS_KiB'])), flush=True)


if __name__ == '__main__':
    main()
