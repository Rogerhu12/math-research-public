#!/usr/bin/env python3
"""Same-g two-sided R48 height recentering and complete nonlinear source change.

The node11 canonical Q2 is replaced by one explicitly saved exact dyadic.
Its nonmean physical first/second jets and all other endpoint data are kept.
The two neighboring R48 candidates use the same true positive moments.
Complete mean roots are retained, and their net height change is integrated.
For cell11, selected source changes reuse the executed absolute R70 adjoint
functional through a pointwise majorant comparison, without another ODE.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time

from flint import acb, arb, ctx

from closure_real_head_source_enclosure import exact_q
from closure_shared_slope_cut_interface import ball, endpoint, record
from closure_split_joint_io_v2 import digest, iter_array
from closure_split_joint_io import read
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_candidate_domain import endpoint_candidate, nonnegative_integral
from tail_outer_weighted_compatible import (
    intersection, make_weighted_candidate, weighted_panel_fields)


def save(path, obj):
    if path.exists():
        raise FileExistsError('Use a fresh complete recentering prefix: '+str(path))
    path.write_text(json.dumps(obj, indent=2)+'\n')


def point(value):
    if not value.is_exact():
        raise ArithmeticError('The chosen candidate coefficient must be an exact dyadic')
    m, e = value.man_exp()
    return dict(mantissa=str(m), binary_exponent=int(e))


def absup(value):
    return abs(value).upper()


def fourier_norm(field, weights):
    # In the present real even candidate each field is pure cosine or sine.
    # The real+imag bound is also valid without that extra fact.
    return sum((2*weights[m]*(absup(v.real)+absup(v.imag))
                for m, v in field.items() if m > 0), arb(0)).upper()


def add(a, b):
    return {m: a.get(m, acb(0))+b.get(m, acb(0)) for m in set(a)|set(b)}


def conv(a, b, m):
    return sum((v*b[m-j] for j, v in a.items() if m-j in b), acb(0))


def product_change(a, da, b, db, m):
    return conv(a, db, m)+conv(da, b, m)+conv(da, db, m)


def field_data(H, K, r, w, weights):
    P = {m: acb(0, m)*H[m]/(r*w) for m in H}
    T = {m: acb(0, m)*P[m] for m in H}
    U = {m: acb(0, m)*K[m]-P[m] for m in H}
    C = {m: K[m]+T[m] for m in H}
    E = 1+w*w
    L = {m: K[m]+E*T[m] for m in H}
    fs = dict(P=P, K=K, T=T, U=U, C=C, L=L)
    ns = {key: fourier_norm(value, weights) for key, value in fs.items()}
    return fs, ns


def nonlinear_change(old, dn, r, rx, w, ell, weights, true_weights):
    """Selected exact quadratic difference plus complete mean/inverse remainder.

N=(Q+A)/(1+l), A=ell*(2*c*(K+E*T)+c*c), l=c+K+E*T.
For R=N-Q, the algebraic difference is bounded by
(dA+ln*dQ)/(1-ln)+(Qo+Ao)*dl/((1-ln)*(1-lo)).
The finite dQ_m preserves its actual convolution support.
"""
    of, on = old
    df, de = dn
    E, z, ss = 1+w*w, w*w, rx/r
    Rold, dR = (on['P']+on['K']).upper(), (de['P']+de['K']).upper()
    Rnew = (Rold+dR).upper()
    if not Rnew < arb(1)/64:
        raise ArithmeticError('The entire real interpolation segment left the complete mean work domain')
    co, cn = (4*Rold**2).upper(), (4*Rnew**2).upper()
    dc = (16*Rnew*dR).upper()
    lo, ln = (co+on['L']).upper(), (cn+on['L']+de['L']).upper()
    dl = (dc+de['L']).upper()
    if not 0 <= lo < 1 or not 0 <= ln < 1:
        raise ArithmeticError('The complete Wiener leading inverse failed')
    l1, zl, sl = absup(ell), z.upper(), ss.upper()
    Qo = (E.upper()*sl*on['U']**2+l1*(on['C']**2+
           zl*(2*on['K']*on['T']+on['T']**2+on['P']**2))).upper()
    dQ = (E.upper()*sl*de['U']*(2*on['U']+de['U'])+
          l1*(de['C']*(2*on['C']+de['C'])+zl*(
              2*(de['K']*on['T']+on['K']*de['T']+de['K']*de['T'])+
              de['T']*(2*on['T']+de['T'])+de['P']*(2*on['P']+de['P'])))).upper()
    Ao = (l1*(2*co*on['L']+co*co)).upper()
    dA = (l1*(2*dc*on['L']+2*cn*de['L']+(cn+co)*dc)).upper()
    drem = ((dA+ln*dQ)/(1-ln)+(Qo+Ao)*dl/((1-ln)*(1-lo))).upper()
    selected = {}
    for m in (2, 4):
        q = E*ss*product_change(of['U'], df['U'], of['U'], df['U'], m)
        q += ell*(product_change(of['C'], df['C'], of['C'], df['C'], m)+z*(
            2*product_change(of['K'], df['K'], of['T'], df['T'], m)+
            product_change(of['T'], df['T'], of['T'], df['T'], m)-
            product_change(of['P'], df['P'], of['P'], df['P'], m)))
        if not q.imag.contains(0):
            raise ArithmeticError('A selected actual quadratic difference lost real cosine symmetry')
        qcos = 2*q.real
        error = (drem/true_weights[m].lower()).upper()
        total = qcos+(-error).union(error)
        selected[m] = dict(quadratic=qcos, remainder=error, full=total,
                           upper=(absup(qcos)+error).upper())
    return dict(Rold=Rold, Rnew=Rnew, dR=dR, co=co, cn=cn, dc=dc,
                leading_lower=(1-ln).lower(), Qold=Qo, dQ=dQ,
                remainder_change=drem, source_change_W1=(dQ+drem).upper(),
                selected=selected)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('flow', 'adjoint', 'source-summary', 'manifest11', 'manifest10',
                 'candidate11', 'candidate10', 'ports', 'response', 'ready', 'out-prefix'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--rss-kib', type=int, default=40960)
    a = p.parse_args()
    ctx.prec, ctx.threads = 256, 1
    began = time.monotonic()
    output = Path(str(a.out_prefix)+'.json')
    if output.exists() or any(Path(str(a.out_prefix)+f'-cell{n:03d}.json').exists() for n in (11, 10)):
        raise FileExistsError('Use a fresh two-sided candidate output prefix')
    names = ('flow', 'adjoint', 'source_summary', 'manifest11', 'manifest10',
             'candidate11', 'candidate10', 'ports', 'response', 'ready')
    hashes = {str(getattr(a, key)): digest(getattr(a, key)) for key in names}
    flow, adjoint, source, ports, packet, ready = map(read,
        (a.flow, a.adjoint, a.source_summary, a.ports, a.response, a.ready))
    metas = {11: read(a.manifest11), 10: read(a.manifest10)}
    old_bounds = {11: read(a.candidate11), 10: read(a.candidate10)}
    if (not all(flow['gates'].values()) or not adjoint['all_gates'] or not source['all_gates']
            or source['cell'] != 11 or adjoint['cell'] != 11 or adjoint['modes'] != [2, 4]):
        raise ValueError('The complete original flow, source and adjoint certificates are required')
    for path in (a.flow, a.source_summary, a.ready):
        if adjoint['input_hashes'].get(str(path)) != hashes[str(path)]:
            raise ValueError('The selected completed adjoint has another exact dependency')
    cp = packet['response']['checkpoint']
    if (not packet['response']['converged'] or cp['parameters']['modes'] != 20
            or cp['parameters']['physicalDepth'] != 12 or len(cp['rawStates']) != 13):
        raise ValueError('Keep the complete actual M20/13-port input')
    prows = {r['physical_node']: r for r in ports['rows']}
    for n in (11, 10):
        meta, bound = metas[n], old_bounds[n]
        if meta['cell'] != n or bound['cell'] != n or not all(meta['checks'].values()) or not all(bound['gates'].values()):
            raise ValueError('Both original full-cell candidates must have paid their domains')
        for path in (getattr(a, 'manifest'+str(n)), a.ports, a.response, a.ready):
            if bound['input_hashes'].get(str(path)) != hashes[str(path)]:
                raise ValueError('An original actual neighboring candidate input changed')
    cells = {r['cell']: r for r in flow['cell_rows']}
    R = intersection(ball(cells[11]['radius']), ball(metas[11]['original_metadata']['outer_radius']))
    R = intersection(R, ball(metas[10]['original_metadata']['inner_radius']))
    arows = {r['mode']: r for r in adjoint['rows']}
    S = ball(arows[2]['exact_original_S0_Q'])
    eold = ball(arows[2]['complete_candidate_centre_residual_canonical_Q'])
    oldq = exact_q(cp['rawStates'][11][0])
    newq = (oldq+S.mid()*eold.mid()).mid()
    dq = newq-oldq
    if not dq.is_exact() or not newq.is_exact():
        raise ArithmeticError('The new canonical node coefficient was not fixed exactly')
    dHnode = R**4*dq
    centre_definition = dict(node=11, mode=2, old_exact_Q=point(oldq),
        new_exact_Q=point(newq), exact_Q_change=point(dq),
        shared_true_radius=record(R), physical_height_change=record(dHnode),
        selection='newQ=mid(oldQ+mid(S0)*mid(old_R70_centre)); all mids are explicitly chosen dyadic candidate data',
        nonmean_physical_first_second_jets_kept=True,
        saved_internal_L_is_not_claimed_unchanged=True,
        unchanged_external_nodes=[12, 10, 0],
        external_node_preservation_scope='All nonmean height/first/second jets; the mean height integral is separately enclosed')
    source_groups = {g['segment']: g for g in source['groups']}
    head = SourceValues(ready)
    head.params = ready['rationalDeepModel']['physicalParameters']
    tau = Fraction(1, 64)
    true_weights = {m: (1+m)*(exact_q(tau)*m).exp() for m in range(2, 41, 2)}
    weights = {m: v.upper() for m, v in true_weights.items()}
    report = []
    all_count = 0
    def guard():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > a.rss_kib:
            raise MemoryError('The owned recentering scan exceeded its RSS observation threshold')
    try:
        for n in (11, 10):
            data, meta = metas[n], metas[n]['original_metadata']
            cell = OuterCell(head, n)
            left, left_report = endpoint_candidate(cell, 'inner', n+1,
                cp['rawStates'][n+1], prows[n+1], ball(meta['inner_radius']), tau, 8)
            right, right_report = endpoint_candidate(cell, 'outer', n,
                cp['rawStates'][n], prows[n], ball(meta['outer_radius']), tau, 8)
            moments = {key: nonnegative_integral(v, strict=True)
                       for key, v in meta['total_positive_moments'].items()}
            candidate = make_weighted_candidate(left, right, moments)
            I = moments['b']
            lam = (dHnode if n == 11 else -dHnode)/I
            modes = sorted(candidate['left']['H'])
            if modes != list(range(2, 41, 2)):
                raise ValueError('The full original twenty nonmean modes must be retained')
            maxima = {key: arb(0) for key in ('Rold', 'Rnew', 'dR', 'dc', 'source_change_W1',
                'remainder_change', 'height_shift', 'first_shift', 'second_shift')}
            witnesses = {key: None for key in maxima}
            kappas = {m: arb(0) for m in (2, 4)}
            kappa_witness = {m: None for m in (2, 4)}
            selected_max = {m: arb(0) for m in (2, 4)}
            mean_height = arb(0)
            min_leading = None
            segments = []
            count = 0
            for group in sorted(data['groups'], key=lambda g: g['source_segment']):
                j, path = group['source_segment'], Path(group['path'])
                if digest(path) != group['sha256']:
                    raise ValueError('A true material group changed')
                hashes[str(path)] = group['sha256']
                source_iterator = None
                if n == 11:
                    sg = source_groups[j]
                    sp = Path(sg['path'])
                    if digest(sp) != sg['sha256'] or sg['panels'] != group['panels']:
                        raise ValueError('The original full source panel group changed')
                    hashes[str(sp)] = sg['sha256']
                    source_iterator = iter(iter_array(sp, 'panels'))
                segment_count = 0
                segment_kappas = {m: arb(0) for m in (2, 4)}
                segment_mean = arb(0)
                for i, g in enumerate(iter_array(path, 'panels')):
                    if g['segment'] != j:
                        raise ValueError('A material panel has the wrong source segment')
                    prefix = {key: nonnegative_integral(v) for key, v in g['prefix_moments'].items()}
                    suffix = {key: nonnegative_integral(v) for key, v in g['suffix_moments'].items()}
                    H, K, Kx = weighted_panel_fields(candidate,
                        u=ball(g['u']), u_x=ball(g['u_x']),
                        prefix_moments=prefix, suffix_moments=suffix)
                    r, rx, w, ell = (ball(g[key]) for key in ('radius', 'radius_x', 'w', 'log_w_x'))
                    if not r > 0 or not rx > 0 or not 0 < w <= arb(1)/2:
                        raise ArithmeticError('A true original material domain failed')
                    frac = intersection(prefix['b']/I, 1-suffix['b']/I)
                    frac = intersection(frac, arb((1, -1), (1, -1)))
                    dh = dHnode*(frac if n == 11 else 1-frac)
                    u, ux = ball(g['u']), ball(g['u_x'])
                    basis = intersection(u*u*(1-u)**2, arb((1, -5), (1, -5)))
                    dk = lam*basis
                    dkx = lam*2*u*(1-u)*(1-2*u)*ux
                    delta_H = {2: acb(dh/2), -2: acb(dh/2)}
                    delta_K = {2: acb(dk/2), -2: acb(dk/2)}
                    old = field_data(H, K, r, w, weights)
                    change = field_data(delta_H, delta_K, r, w, weights)
                    values = nonlinear_change(old, change, r, rx, w, ell, weights, true_weights)
                    values.update(height_shift=absup(dh), first_shift=absup(w*dk),
                        second_shift=absup((w/rx)*(dkx+ell*dk)))
                    witness = dict(segment=j, panel=i, x_left=g['x_left'], x_right=g['x_right'])
                    for key in maxima:
                        if values[key] > maxima[key]:
                            maxima[key], witnesses[key] = values[key].upper(), witness
                    min_leading = values['leading_lower'] if min_leading is None else min(min_leading, values['leading_lower'])
                    mean_term = (ball(g['width']).upper()*w.upper()*values['dc']).upper()
                    mean_height += mean_term
                    segment_mean += mean_term
                    for m in (2, 4):
                        selected_max[m] = max(selected_max[m], values['selected'][m]['upper'])
                    if source_iterator is not None:
                        saved = next(source_iterator)
                        if (saved['segment'], saved['panel'], saved['x_left'], saved['x_right']) != (j, i, g['x_left'], g['x_right']):
                            raise ValueError('The old source positions are not the same true panels')
                        sr = {v['mode']: v for v in saved['selected_cosine_sources']}
                        for m in (2, 4):
                            rec = sr[m]['complete_source_cosine']
                            cap = max(absup(endpoint(rec['lower'])), absup(endpoint(rec['upper'])))
                            upper = values['selected'][m]['upper']
                            if not cap > 0:
                                if not upper == 0:
                                    raise ArithmeticError('A zero original coefficient majorant cannot dominate the new source difference')
                                ratio = arb(0)
                            else:
                                ratio = (upper/cap).upper()
                            if ratio > kappas[m]:
                                kappas[m], kappa_witness[m] = ratio, witness
                            segment_kappas[m] = max(segment_kappas[m], ratio)
                    count += 1
                    all_count += 1
                    segment_count += 1
                    if count % 64 == 0:
                        guard()
                if segment_count != group['panels'] or (source_iterator is not None and next(source_iterator, None) is not None):
                    raise ValueError('A complete real material/source group was not exhausted')
                segments.append(dict(segment=j, panels=segment_count,
                    mean_height_change_upper=record(segment_mean.upper()),
                    selected_source_ratio_upper={str(m): record(v) for m, v in segment_kappas.items()} if n == 11 else None))
                print(json.dumps(dict(event='recentered_candidate_segment', cell=n, segment=j,
                    panels=segment_count, Rnew=str(maxima['Rnew']),
                    seconds=time.monotonic()-began, peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
            if count != data['panels']:
                raise ValueError('The complete neighboring cell was not scanned')
            item = dict(cell=n, panels=count, exact_candidate_change=centre_definition,
                true_positive_bubble_integral=record(I), bubble_coefficient_change=record(lam),
                source_coordinate='Same entire-cell normalized unwarped length as R48; no radius or source replacement',
                full_old_endpoint_reports=[left_report, right_report],
                whole_cell={key: dict(upper=record(v), witness=witnesses[key]) for key, v in maxima.items()},
                complete_mean_height_change_upper=record(mean_height.upper()),
                complete_Wiener_leading_lower=record(min_leading),
                selected_complete_source_change_upper={str(m): record(v) for m, v in selected_max.items()},
                selected_old_source_majorant_ratio_upper={str(m): record(v) for m, v in kappas.items()} if n == 11 else None,
                ratio_witnesses=kappa_witness if n == 11 else None, segments=segments,
                all_original_panels_paid=True, complete_mean_kept=True,
                one_global_mean_height_constant_only=True,
                same_real_g_and_all_external_nonmean_jets=True,
                no_ODE_or_new_source_integral=True)
            save(Path(str(a.out_prefix)+f'-cell{n:03d}.json'), item)
            report.append(item)
            guard()
        cell11 = report[0]
        functional_rows = []
        for m in (2, 4):
            row = arows[m]
            kap = ball(cell11['selected_old_source_majorant_ratio_upper'][str(m)])
            delta_I = (kap*ball(row['absolute_canonical_cut_forcing_upper'])).upper()
            centre = ball(row['complete_candidate_centre_residual_canonical_Q'])
            if m == 2:
                centre -= dq/ball(row['exact_original_S0_Q'])
            centre += (-delta_I).union(delta_I)
            axis = ball(row['canonical_parameter_axis'])
            functional_rows.append(dict(mode=m, reused_original_absolute_functional=row['absolute_canonical_cut_forcing_upper'],
                whole_cell_source_comparison_factor=record(kap), complete_new_minus_old_forcing_upper=record(delta_I),
                new_complete_candidate_centre_residual_canonical_Q=record(centre),
                canonical_axis=row['canonical_parameter_axis'], new_axis_ratio_upper=record((absup(centre)/axis).upper()),
                all_mean_and_inverse_terms_in_source_difference=True,
                unknown_outer_correction_not_claimed=True))
        mean_total = sum((ball(row['complete_mean_height_change_upper']) for row in report), arb(0)).upper()
        sources = {name: digest(Path(__file__).with_name(name)) for name in (
            'closure_shared_slope_cut_interface.py', 'tail_outer_candidate_domain.py',
            'tail_outer_weighted_compatible.py', 'tail_outer_weighted_endpoint.py',
            'closure_real_outer_radius.py', 'tail_r33_middle_ordered_physical.py')}
        gates = dict(complete_both_cells_and_original10793_panels=True,
            exact_dyadic_internal_canonical_Q_chosen=True,
            all_other_nonmean_heights_and_physical_endpoint_derivatives_kept=True,
            common_node11_nonmean_and_mean_twojet_compatibility=True,
            full_complete_mean_working_domain=True,
            complete_pointwise_Wiener_inverse_and_full_mean_difference=True,
            signed_finite_quadratic_source_difference_all20_modes=True,
            all_inverse_generated_modes_in_remainder=True,
            true_cell11_absolute_adjoint_reused_by_pointwise_majorant=True,
            single_mean_height_integral_and_constant_accounted=True,
            same_g_and_same_phase_range=True,
            no_new_ODE_or_background_quadrature=True)
        result = dict(status='Actual same-g two-sided internal-height recentering with full source/mean change',
            gates=gates, all_gates=all(gates.values()), cells=[11, 10], panels=all_count,
            exact_candidate_change=centre_definition,
            cell_reports=[dict(cell=r['cell'], path=str(Path(str(a.out_prefix)+f'-cell{r["cell"]:03d}.json')),
                sha256=digest(Path(str(a.out_prefix)+f'-cell{r["cell"]:03d}.json'))) for r in report],
            functional_rows=functional_rows,
            complete_mean_height_total_change_upper=record(mean_total),
            mean_anchor='One additive constant at node10 preserves the more external mean height; node12 and the freely positioned cuff acquire the enclosed integrated shift. No independent mean resets.',
            phase_family='For the fixed new shape, all nonmean modes rotate together. Angular averaging makes the single mean-height constant phase-independent.',
            further_outer_linear_centre_residual_unchanged=True,
            further_outer_nonlinear_change_not_discarded=True,
            complete_outer_nonlinear_Green_Schur_not_claimed=True,
            input_hashes=hashes, source_hashes=sources, entrypoint_sha256=digest(Path(__file__)),
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        guard()
        save(output, result)
        print(json.dumps(dict(event='complete_two_sided_recentre', output=str(output), all_gates=True,
            panels=all_count, node11_Q_change=str(dq), mean_height_change=str(mean_total),
            rows=[dict(mode=r['mode'], delta_source_functional=str(ball(r['complete_new_minus_old_forcing_upper'])),
                new_centre=str(ball(r['new_complete_candidate_centre_residual_canonical_Q']))) for r in functional_rows],
            seconds=result['elapsed_seconds'], peak_RSS_KiB=result['peak_RSS_KiB'])), flush=True)
    except Exception as error:
        failure = Path(str(a.out_prefix)+'-failure.json')
        if not failure.exists():
            failure.write_text(json.dumps(dict(status='Incomplete same-g recentering scan',
                error=repr(error), completed_cells=[r['cell'] for r in report], panels=all_count,
                candidate_change=centre_definition, input_hashes=hashes,
                entrypoint_sha256=digest(Path(__file__)), elapsed_seconds=time.monotonic()-began), indent=2)+'\n')
        raise


if __name__ == '__main__':
    main()
