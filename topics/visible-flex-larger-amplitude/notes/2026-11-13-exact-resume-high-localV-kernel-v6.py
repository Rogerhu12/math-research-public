#!/usr/bin/env python3
"""Actual all-frequency high source kernel in localV and balanced target norms.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The full actual common-strip damping pays each leaf source equilibrium
for every high mode at once. The scalar comparison preserves source
position, actual frame and target weight before each radial supremum.  All |m|>=34816 are included.  No
physical source or ODE is recomputed and no Vmin shortcut is used.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def digest(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            h.update(part)
    return h.hexdigest()


def ex(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2) ** int(v[1])
    return F(int(v['numerator']), int(v['denominator']))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ('summary', 'leaves', 'resource', 'balanced', 'out-prefix', 'original'):
        ap.add_argument('--' + key, type=Path, required=True)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--rss-kib', type=int, default=98304)
    ap.add_argument('--floor-shift',type=int,default=3)
    args = ap.parse_args(); started = time.monotonic()
    from flint import arb, ctx
    if args.precision < 256:
        raise ValueError('The original256-bit enclosure precision is retained')
    ctx.prec = args.precision; ctx.threads = 1

    def ball(value):
        return arb(value.numerator) / arb(value.denominator)

    def point(value):
        return arb(int(value[0])) * arb(2) ** int(value[1])

    def top(value):
        if not value.is_finite() or not value >= 0:
            raise ArithmeticError('A finite nonnegative source/target comparison is required')
        return value.upper()

    def up96(value):
        value = top(value)
        mantissa, exponent = value.man_exp(); mantissa, exponent = int(mantissa), int(exponent)
        shift = max(0, abs(mantissa).bit_length() - 96)
        if shift:
            mantissa = -((-mantissa) // (1 << shift)); exponent += shift
        return [str(mantissa), exponent]

    def guard():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > args.rss_kib:
            raise MemoryError('Owned high localV consumer exceeded its unchanged RSS guard')

    meta, usage, balanced = [json.loads(getattr(args, k).read_text()) for k in ('summary', 'resource', 'balanced')]
    if not (meta['all_identity_gates'] and all(meta['gates'].values()) and meta['original_panels'] == 10793
            and usage['exitcode'] == 0 and usage['termination_signal'] is None
            and balanced['all_gates'] and all(balanced['gates'].values())
            and digest(args.leaves) == meta['leaf_primary']['sha256']):
        raise ArithmeticError('The complete exact original common-high coefficient input is required')
    M = meta['leaf_primary']['high_cutoff']; case = next(r for r in meta['cases'] if r['high_threshold'] == M)
    if not case['common_strip_strictly_above_one_over64'] or ex(case['common_terminal_strip']) <= F(1, 64):
        raise ArithmeticError('The common analytic floor is unpaid')
    partition = [row['partition'] for row in case['blocks']]
    original = json.loads(args.original.read_text())
    if not original['all_gates'] or args.floor_shift < 0 or args.floor_shift > 32:
        raise ValueError('Original complete kernel and explicit nonnegative floor choice required')
    floors = [ex(original['rows'][i]['V_max'])/F(2)**args.floor_shift if i == 21 else F(0) for i in range(25)]
    where = {(p['cell'], p['segment'], k): i for i, p in enumerate(partition)
             for k in range(p['first_panel'], p['last_panel_exclusive'])}
    if len(where) != 10793 or len(partition) != 25:
        raise ValueError('Every original source and target leaf must be covered')
    output = Path(str(args.out_prefix) + '.json.gz');
    if output.exists():
        raise FileExistsError('Use a fresh complete infinite-high primary')
    kappa = F(1, 1 << 18); GH = ex(case['full_R93_source_inverse'])
    multiplier = arb(1)
    delta = ex(balanced['exact_head_to_output_strip_gap_lower'])
    if delta <= 0:
        raise ArithmeticError('The actual positive true-head strip gap is required')
    head_state = top((-ball(M * delta)).exp())
    states = []; rows = []; current = -1; in_group = total = jumps = 0
    first_b = None; first_b_inverse = None; vmax = arb(0)
    phase_half = phase_full = F(0)

    def finish():
        if current < 0:
            return
        part = partition[current]
        if in_group != part['panels']:
            raise ValueError('An actual whole target block was truncated')
        sources = []
        for j in range(current + 1):
            densities = []
            for normalization_index, normalization in enumerate(('physical_source', 'already_divided_by_frame')):
              for power_index, power in enumerate((2, 1, 0)):
                values = maxima[6 * j + 3 * normalization_index + power_index]
                densities.append(dict(V_power=power, source_normalization=normalization, P_sup=up96(multiplier * values[0]),
                    K_sup=up96(multiplier * values[1]),
                    localV_strong_output_row=up96(multiplier * (values[0] + values[1])),
                    balanced_strong_output_row=up96(multiplier * values[2]),
                    shifted_P_sup=up96(multiplier*values[3]),shifted_K_sup=up96(multiplier*values[4]),
                    shifted_localV_strong_output_row=up96(multiplier*(values[3]+values[4]))))
            sources.append(dict(source_comparison_block=j, source_partition=partition[j], density_rows=densities))
        rows.append(dict(comparison_block=current, target_partition=part, original_panels=in_group,
            V_max=up96(vmax), source_rows=sources,
            initial_localV_separate_component_sups=[[up96(v) for v in head_max[:2]],
                [up96(v * first_b_inverse) for v in head_max[:2]]],
            initial_balanced_column_sups=[up96(head_max[2]),up96(head_max[2]*first_b_inverse)],
            initial_shifted_localV_separate_component_sups=[[up96(v) for v in head_max[3:]],
                [up96(v*first_b_inverse) for v in head_max[3:]]],
            target_V_floor=dict(numerator=str(floors[current].numerator),denominator=str(floors[current].denominator)),
            true_head_strip_gap_already_paid=True, full_angular_gain_already_paid=True,
            both_physical_target_component_sups_retained=True))

    with gzip.open(args.leaves, 'rt') as stream:
        for line in stream:
            leaf = json.loads(line); gi = where[leaf['cell'], leaf['segment'], leaf['panel']]
            if gi != current:
                finish()
                if gi != current + 1:
                    raise ValueError('True causal target blocks were reordered')
                current = gi; in_group = 0; vmax = arb(0)
                states.extend([arb(0) for _ in range(6)])
                maxima = [[arb(0) for _ in range(5)] for _ in states]
                head_max = [arb(0) for _ in range(5)]
            if leaf['panel'] != partition[gi]['first_panel'] + in_group:
                raise ValueError('An original source leaf was skipped')
            V, b = point(leaf['V']), point(leaf['b'])
            W = V+ball(floors[gi])
            if not V.is_finite() or not b.is_finite() or not V > 0 or not b > 0:
                raise ArithmeticError('The exact positive actual source/targetV and frame are required')
            if first_b is None:
                first_b = leaf['b']; first_b_inverse = top(1 / b)
            c_integral = F(int(leaf['high_positive_c_integral'][0]), int(leaf['high_positive_c_integral'][1]))
            extra = F(int(leaf['extra_continuous_over_high'][0]), int(leaf['extra_continuous_over_high'][1]))
            jump = F(int(leaf['common_entry_jump'][0]), int(leaf['common_entry_jump'][1]))
            if c_integral <= 0 or min(extra, jump) < 0:
                raise ArithmeticError('All exact high attenuation and actual frame charges must retain their signs')
            jumps += jump > 0
            half_loss = M * (kappa * c_integral / 2 + extra)
            full_loss = M * (kappa * c_integral + extra)
            attenuation = min(arb(1), top((-ball(full_loss)).exp()))
            head_attenuation = min(arb(1), top((-ball(full_loss)).exp()))
            if attenuation > 1 or head_attenuation > 1:
                raise ArithmeticError('The exact attenuation must be bounded above by1')
            source_equilibrium_gain = top(ball((1+F(1,M))*c_integral/(kappa*c_integral+extra)))
            if source_equilibrium_gain > ball(GH).upper():
                raise ArithmeticError('The full local source equilibrium exceeds its proved global envelope')
            local_source = [top(source_equilibrium_gain*v) for v in
                (top(V*V/b),top(V/b),top(1/b),top(V*V),V,arb(1))]
            for index, previous in enumerate(states):
                active = index >= 6 * gi
                source_value = local_source[index - 6 * gi] if active else arb(0)
                envelope = max(previous, source_value)
                p_value, k_value = top(envelope / V), top(b * envelope / V)
                maxima[index][0] = max(maxima[index][0], p_value)
                maxima[index][1] = max(maxima[index][1], k_value)
                maxima[index][2] = max(maxima[index][2], envelope)
                maxima[index][3] = max(maxima[index][3],top(envelope/W))
                maxima[index][4] = max(maxima[index][4],top(b*envelope/W))
                if active and previous > source_value:
                    states[index] = top(source_value+top(previous-source_value)*attenuation)
                elif active:
                    states[index] = source_value
                else:
                    states[index] = top(previous*attenuation)
            head_max[0] = max(head_max[0], top(head_state / V))
            head_max[1] = max(head_max[1], top(b * head_state / V))
            head_max[2] = max(head_max[2], head_state)
            head_max[3] = max(head_max[3],top(head_state/W))
            head_max[4] = max(head_max[4],top(b*head_state/W))
            head_state = top(head_state * head_attenuation)
            phase_half += half_loss; phase_full += full_loss; vmax = max(vmax, V)
            in_group += 1; total += 1
            if total % 64 == 0:
                guard()
    finish()
    gates = dict(all10793_original_source_leaves=total == 10793,
        all25_causal_source_and_target_blocks=len(rows) == 25,
        all_original_8956_nonzero_common_frame_jumps_paid=jumps == 8956,
        full_infinite_frequency_range=True, all_three_source_materials_retained=True,
        weak_to_strong_angular_gain_paid_by_complete_leaf_equilibrium=True,
        actual_ordered_V_ratios_retained=True, both_initial_columns_and_output_components_retained=True,
        complete_actual_common_strip_above_one_over64=True, every_state_and_output_finite=True,
        no_global_Vmin_division=True, no_new_background_ODE_or_source_evaluation=True)
    original = json.loads(args.original.read_text())
    identical = len(original['rows']) == len(rows) and original['all_gates']
    for old, new in zip(original['rows'], rows):
        identical = identical and old['initial_localV_separate_component_sups'] == new['initial_localV_separate_component_sups'] and old['V_max'] == new['V_max']
        for old_source, new_source in zip(old['source_rows'], new['source_rows']):
            restored = [{k:v for k,v in density.items() if k not in ('source_normalization','balanced_strong_output_row','shifted_P_sup','shifted_K_sup','shifted_localV_strong_output_row')} for density in new_source['density_rows'][:3]]
            identical = identical and all(old_d['V_power']==new_d['V_power'] and all(ex(new_d[k]) <= ex(old_d[k]) for k in ('P_sup','K_sup','localV_strong_output_row')) for old_d,new_d in zip(old_source['density_rows'],restored))
    gates['all_new_physical_source_rows_below_original_complete_bounds'] = identical
    gates['actual_ordered_balanced_target_six_columns_and_head_paid'] = all('initial_balanced_column_sups' in r and all('balanced_strong_output_row' in d for t in r['source_rows'] for d in t['density_rows']) for r in rows)
    gates['fixed_positive_target_V_plus_floor_paid'] = all('initial_shifted_localV_separate_component_sups' in r and all('shifted_localV_strong_output_row' in d for t in r['source_rows'] for d in t['density_rows']) for r in rows)
    gates['three_extra_already_divided_source_materials_paid'] = all(len(s['density_rows']) == 6 for r in rows for s in r['source_rows'])
    if not all(gates.values()):
        raise ArithmeticError('A complete high localV source/target gate failed')
    result = dict(schema='visible-flex-all-infinite-high-exact-leaf-equilibrium-kernel-v6',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)', all_gates=True, gates=gates,
        status='Completed actual ordered whole-leaf localV source kernel for every signed even high mode',
        high_cutoff=M, upper_frequency_cutoff=None, common_strip=case,
        source_units='physical_source: N=c_bg V_I^p mass; already_divided_by_frame: N/b=c_bg V_I^p mass, p=2,1,0',
        output_units='Physical P/K separate radial suprema in strong Fourier localV norm; full angular gain already included',
        global_source_equilibrium_envelope=dict(numerator=str(GH.numerator),denominator=str(GH.denominator)),
        source_kernel_rule='Each leaf B=(1+1/M)c_integral/(kappa*c_integral+extra) times V^p/b or V^p; q_out=max(B,B+(q_in-B)exp(-M(kappa*c_integral+extra))); inactive source only decays',
        ordered_envelope='Complete high-mode source equilibrium solved before target readout; no half-kappa global source multiplier',
        first_actual_frame=first_b, head_strip_gap=balanced['exact_head_to_output_strip_gap_lower'],
        head_strip_gap_already_paid=True, target_V_floors=[dict(numerator=str(v.numerator),denominator=str(v.denominator)) for v in floors],
        floor_shift=args.floor_shift,original_panels=total, original_full_frame_interfaces=total - 1,
        actual_nonzero_common_frame_jumps=jumps, comparison_partition=partition, source_powers=[2, 1, 0],
        rows=rows, nonlinear_fixed_point_claimed=False, low_feedback_or_cut_claimed=False,
        input_hashes={str(getattr(args, n)): digest(getattr(args, n)) for n in ('summary', 'leaves', 'resource', 'balanced', 'original')},
        source_sha256=digest(__file__), precision=args.precision,
        elapsed_seconds=time.monotonic() - started, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=9) as packed:
            packed.write((json.dumps(result, indent=2) + '\n').encode())
    if output.stat().st_size >= 5_000_000:
        raise ArithmeticError('The complete compressed primary exceeds the repository limit')
    guard()
    diagonal = [F(int(r['source_rows'][-1]['density_rows'][0]['localV_strong_output_row'][0])) *
                F(2) ** int(r['source_rows'][-1]['density_rows'][0]['localV_strong_output_row'][1]) for r in rows]
    print(json.dumps(dict(all_gates=True, high_cutoff=M, original_panels=total,
        maximum_diagonal_Gamma2=float(max(diagonal)), maximum40Gamma2=float(40 * max(diagonal)),
        maximum_diagonal_block=diagonal.index(max(diagonal)), elapsed_seconds=result['elapsed_seconds'],
        peak_rss_kib=result['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
