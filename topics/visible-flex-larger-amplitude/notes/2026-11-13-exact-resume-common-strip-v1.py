#!/usr/bin/env python3
"""Exact common strip for the paid hybrid middle and original R93 frames.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This consumes the complete original leaves.  The common loss is the maximum
of the two continuous losses on each leaf, with every R93 frame jump paid.
Both additional losses are nondecreasing, so both causal inverses restrict
legally to the common strip.  This alone does not close either nonlinear
coupling equation or an uncomputed gap of finite modes.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re
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
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2) ** int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def rec(v):
    return dict(numerator=str(v.numerator), denominator=str(v.denominator), display_only=float(v))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for n in ('topic', 'coefficients', 'leaves', 'frame', 'high', 'partition', 'out'):
        ap.add_argument('--' + n, required=True, type=Path)
    ap.add_argument('--cutoffs', default='5760,8192,16384,32768,65536,131072,262144,1048576')
    args = ap.parse_args()
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError('Fresh common-strip exact output required')
    read = lambda p: json.loads(Path(p).read_text())
    coeff, frames, high, partition_meta = [read(getattr(args, n)) for n in ('coefficients', 'frame', 'high', 'partition')]
    helper = args.topic / 'computations/root_outer_frame_continuous_prefix.py'
    if digest(helper) != '828ea557a5f9b702658eed425cc6344128d7e4be4a13a3efefc1d25b6c302fe5':
        raise ValueError('Keep the exact original positive-log algorithm')
    if digest(args.frame) != 'e726b2006b27c84ac61d73e0d899d504da7997fd7c3775c7ca3b35e175261751':
        raise ValueError('Keep the exact original optimal-frame packet')
    if not all(frames['gates'].values()) or not high['all_gates'] or not coeff['all_coefficient_gates']:
        raise ValueError('All original complete input gates are required')
    if digest(args.leaves) != coeff['leaf_file']['sha256']:
        raise ValueError('The complete actual hybrid leaves changed')
    spec = importlib.util.spec_from_file_location('original_frame_logs', helper)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    partition = partition_meta['comparison_partition']
    block = {(p['cell'], p['segment'], k): i for i, p in enumerate(partition)
             for k in range(p['first_panel'], p['last_panel_exclusive'])}
    if len(block) != 10793 or len(partition) != 25:
        raise ValueError('Every actual comparison block and leaf must be kept')
    cutoffs = list(map(int, args.cutoffs.split(',')))
    if len(set(cutoffs)) != len(cutoffs) or any(M < 5760 or M % 2 for M in cutoffs):
        raise ValueError('Distinct positive even high thresholds at or above5760 are required')
    K = F(1, 1 << 18); eps = F(1, 1 << 25); rho = F(33, 32); tau0 = F(18, 125)
    cases = {M: dict(common_loss=F(0), high_loss=F(0), middle_extra=F(0), high_extra=F(0),
                     blocks=[dict(extra_start=None, extra_end=None, gap_min=None, gap_max=None) for _ in partition])
             for M in cutoffs}
    total_phase = total_pf = total_pi = hybrid_loss = F(0)
    count = 0; previous_b = None
    hashes = {str(getattr(args, n)): digest(getattr(args, n)) for n in ('coefficients', 'leaves', 'frame', 'high', 'partition')}
    hashes[str(helper)] = digest(helper)
    packets = [p for p in frames['files'] if p['path'].endswith('-panels.jsonl.gz')]
    with gzip.open(args.leaves, 'rt') as leaves:
        for packet in packets:
            path = args.topic / packet['path']
            if digest(path) != packet['sha256']:
                raise ValueError('An original actual R68 leaf packet changed')
            hashes[str(path)] = packet['sha256']
            m = re.search(r'-cell(\d+)-seg(\d+)-panels', path.name)
            cell, segment = map(int, m.groups())
            n = 0
            with gzip.open(path, 'rt') as stream:
                for line in stream:
                    fr = json.loads(line); leaf = json.loads(next(leaves))
                    if (leaf['cell'], leaf['segment'], leaf['panel']) != (cell, segment, fr['index']):
                        raise ValueError('True source/frame order changed')
                    dx = F(int(leaf['dx'][0]), int(leaf['dx'][1]))
                    if dx != F(fr['x_right']) - F(fr['x_left']) or dx <= 0:
                        raise ValueError('The complete actual leaf width changed')
                    b = ex(fr['chosen_frame'])
                    if b != ex(fr['chosen_frame']['lower']) or b != ex(leaf['b']) or b <= 0:
                        raise ValueError('The same exact positive original frame is required')
                    jf, ji = (F(0), F(0)) if previous_b is None else module.positive_pair(previous_b / b)
                    nf, ni, phase = [ex(fr[key]) for key in ('new_forward_with_jump', 'new_backward_with_jump', 'new_phase')]
                    pf, pi = max(F(0), nf, jf), max(F(0), ni, ji)
                    lower_jump = max(F(0), jf - eps)
                    nonphase = max(F(0), nf - lower_jump)
                    if nonphase + jf > pf + eps or min(phase, pf, pi) < 0:
                        raise ArithmeticError('The exact R93 jump split failed')
                    h_loss = rho * ex(leaf['q_energy'] if (cell, segment) == (10, 3) else leaf['q_Metzler']) * dx
                    i = block[cell, segment, fr['index']]
                    for M, case in cases.items():
                        row = case['blocks'][i]
                        # The old high norm takes both sides of a frame jump.
                        old_gap = case['high_loss'] - hybrid_loss
                        row['gap_min'] = old_gap if row['gap_min'] is None else min(row['gap_min'], old_gap)
                        row['gap_max'] = old_gap if row['gap_max'] is None else max(row['gap_max'], old_gap)
                        if row['extra_start'] is None:
                            row['extra_start'] = case['middle_extra']
                        jump = jf / M
                        high_cont = phase + nonphase / M + K * (pf + pi)
                        common_cont = max(h_loss, high_cont)
                        case['high_loss'] += jump + high_cont
                        case['common_loss'] += jump + common_cont
                        case['middle_extra'] += jump + common_cont - h_loss
                        case['high_extra'] += common_cont - high_cont
                        row['extra_end'] = case['middle_extra']
                        new_gap = case['high_loss'] - (hybrid_loss + h_loss)
                        # Both continuous endpoint gaps and the entering jump
                        # endpoint are needed for the actual profile comparison.
                        entry_gap = old_gap + jump
                        row['gap_min'] = min(row['gap_min'], entry_gap, new_gap)
                        row['gap_max'] = max(row['gap_max'], entry_gap, new_gap)
                    total_phase += phase; total_pf += pf; total_pi += pi; hybrid_loss += h_loss
                    previous_b = b; count += 1; n += 1
            if n != packet['panels']:
                raise ValueError('An original frame packet was truncated')
        if next(leaves, None) is not None:
            raise ValueError('The hybrid stream contains unmatched source leaves')
    gates = dict(all10793_original_leaves=count == 10793, all18_original_segments=len(packets) == 18,
        exact_original_phase_reproduced=total_phase == ex(high['exact_actual_phase_total']),
        exact_positive_forward_reproduced=total_pf == ex(high['exact_positive_forward_total']),
        exact_positive_inverse_reproduced=total_pi == ex(high['exact_positive_inverse_total']),
        exact_hybrid_strip_reproduced=hybrid_loss == ex(next(r for r in coeff['phase_cases'] if r['energy_groups'] == [[10, 3]])['strip_loss']))
    if not all(gates.values()):
        raise ArithmeticError('An original exact ledger identity failed: ' + str(gates))
    results = []
    for M, case in cases.items():
        if case['common_loss'] != hybrid_loss + case['middle_extra'] or case['common_loss'] != case['high_loss'] + case['high_extra']:
            raise ArithmeticError('Both nondecreasing losses must give the identical common strip')
        row = dict(high_threshold=M, common_terminal_strip=rec(tau0 - case['common_loss']),
                   original_high_terminal_strip=rec(tau0 - case['high_loss']),
                   original_hybrid_terminal_strip=rec(tau0 - hybrid_loss),
                   complete_common_loss=rec(case['common_loss']),
                   complete_nondecreasing_middle_extra=rec(case['middle_extra']),
                   complete_nondecreasing_high_extra=rec(case['high_extra']),
                   common_strip_strictly_above_one_over64=tau0 - case['common_loss'] > F(1, 64),
                   all_partial_positions_paid=True, both_additional_losses_nondecreasing=True,
                   full_R93_source_inverse=rec((1 + F(1, M)) / K),
                   extra_positive_middle_modes=max(0, (M - 5760) // 2),
                   finite_mode_gap_already_computed=M == 5760,
                   original_strip_gap_minimum=rec(min(r['gap_min'] for r in case['blocks'])),
                   original_strip_gap_maximum=rec(max(r['gap_max'] for r in case['blocks'])),
                   blocks=[dict(partition=partition[i], **{k: rec(v) for k, v in r.items()})
                           for i, r in enumerate(case['blocks'])])
        results.append(row)
    result = dict(schema='visible-flex-exact-common-middle-high-strip-v1',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        status='Complete exact shared-leaf strip interface; finite gaps and nonlinear coupling are separate obligations',
        all_identity_gates=True, gates=gates, initial_strip='18/125', kappa=rec(K),
        original_panels=count, cases=results, coupled_fixed_point_claimed=False,
        full_outer_or_cut_claimed=False, input_hashes=hashes, source_sha256=digest(__file__),
        elapsed_seconds=time.monotonic() - started, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(all_identity_gates=True, cases=[{k: r[k] for k in
        ('high_threshold', 'common_strip_strictly_above_one_over64', 'extra_positive_middle_modes')} |
        dict(common_terminal_display=r['common_terminal_strip']['display_only'],
             extra_middle_loss_display=r['complete_nondecreasing_middle_extra']['display_only'],
             original_gap_minimum_display=r['original_strip_gap_minimum']['display_only']) for r in results],
        elapsed_seconds=result['elapsed_seconds'], peak_rss_kib=result['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
