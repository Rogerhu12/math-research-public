#!/usr/bin/env python3
"""Pay actual singleton94/96 outer comparison and the original common strip.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
Keep every original leaf, both initial components, three source materials,
25 target/source blocks, and frame jumps. This is an operator refinement.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from r127_window_helpers import ex, up, decay, rec


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p); b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args(); start = time.monotonic(); ids = read(a.inputs); gates = {}

    def gate(k, v):
        if not v: raise ArithmeticError(k)
        gates[k] = True

    def checked(k):
        r = ids[k]; gate('identity_'+k, sha(r['path']) == r['sha256'])
        return read(r['path'])

    meta = checked('new_windows_metadata'); usage = checked('new_windows_resource')
    old = checked('original_185_window_primary'); balanced = checked('balanced_head')
    gate('new_actual_formal0', usage['exitcode'] == 0 and usage['termination_signal'] is None
         and meta['all_enclosure_gates'] and meta['windows'] == [[94, 94], [96, 96]])
    gate('all_original_leaf_and_source_contracts', meta['original_leaf_count_per_window'] == 10793
         and meta['original_source_groups'] == 18 and meta['source_powers'] == [2, 1, 0]
         and meta['comparison_source_blocks'] == 25 and meta['precision'] >= 256)
    gate('same_original_comparison_partition', old['all_gates'] and old['comparison_partition'] == meta['comparison_partition'])
    nr = ids['new_windows']; pr = ids['original_parent_kernel']
    gate('new_stream_identity', sha(nr['path']) == nr['sha256'] == meta['primary']['sha256'])
    gate('original_parent_identity', sha(pr['path']) == pr['sha256'])
    with gzip.open(nr['path'], 'rt') as f: newrows = [json.loads(line) for line in f]
    with gzip.open(pr['path'], 'rt') as f: parent = [json.loads(line) for line in f]
    parent = [r for r in parent if r['window'] == [94, 96]]
    gate('unique_original_parent_window', len(parent) == 1 and parent[0]['common_strip_already_paid']
         and len(parent[0]['rows']) == 25)
    parent = parent[0]
    case = old['common_strip']; delta = ex(balanced['exact_head_to_output_strip_gap_lower'])
    Bcut = ex(balanced['balanced_B_lower'])
    extra = [ex(row['extra_start']) for row in case['blocks']]
    ends = [ex(row['extra_end']) for row in case['blocks']]
    gate('complete_existing_common_strip', len(extra) == 25 and delta > 0 and Bcut > 0
         and case['high_threshold'] == 34816)
    result_rows = []; changes = []
    for win in newrows:
        m = win['window'][0]
        gate('actual_singleton_'+str(m), win['window'] == [m, m] and m in (94, 96)
             and win['actual_mode_count'] == 1 and win['all10793_original_leaves']
             and win['all18_original_source_segments_retained'] and win['all3_source_materials']
             and win['both_initial_columns_retained'] and win['entry_count'] == win['exit_count'] == 1
             and win['frame_jump_count'] == 1804 and len(win['rows']) == 25)
        rows = []; ratios = []
        for i, (row, prior) in enumerate(zip(win['rows'], parent['rows'])):
            gate('actual_target_'+str(m)+'_'+str(i), row['comparison_block'] == prior['target_block'] == i
                 and len(row['source_rows']) == i+1)
            cols = row['initial_localV_separate_component_sups']
            head = up(max(sum(map(ex, cols[0]), F(0))/Bcut, sum(map(ex, cols[1]), F(0)))
                      *decay(m*(delta+extra[i])))
            # Both are complete independent bounds for the singleton.
            head = min(head, ex(prior['head_gain']))
            mats = {str(p): [] for p in (2, 1, 0)}
            for j, sr in enumerate(row['source_rows']):
                gate('actual_source_'+str(m)+'_'+str(i)+'_'+str(j), sr['source_comparison_block'] == j
                     and [d['V_power'] for d in sr['density_rows']] == [2, 1, 0])
                factor = decay(m*max(F(0), extra[i]-ends[j])) if j < i else F(1)
                for d in sr['density_rows']:
                    p = str(d['V_power'])
                    val = up(max(ex(d['localV_strong_output_row']), ex(d['P_sup'])+ex(d['K_sup']))*factor)
                    val = min(val, ex(prior['three_materials'][p][j]))
                    mats[p].append(rec(val))
            rows.append(dict(target_block=i, head_gain=rec(head), three_materials=mats))
            ratios.append(rec(head/ex(prior['head_gain'])))
        result_rows.append(dict(window=[m, m], common_strip_already_paid=True, head_band=0, rows=rows))
        changes.append(dict(mode=m, head_gain_over_original_parent=ratios))
    gate('both_singletons_complete', [r['window'] for r in result_rows] == [[94, 94], [96, 96]])
    ans = dict(schema='R127-actual-singleton94-96-original-common-strip-kernels-v1',
        author='/root (GPT-6 Astra Pro, AI-assisted)', source_sha256=sha(__file__),
        helper_sha256=sha(Path(__file__).with_name('r127_window_helpers.py')),
        all_gates=all(gates.values()), gates=gates, inputs=ids, rows=result_rows,
        comparison_partition=meta['comparison_partition'], common_strip=case, improvements=changes,
        original_parent_window=[94, 96], full185_window_and_shared_mass_bounds_still_simultaneous=True,
        complete_mean_inverse_far_source_not_preinserted=True,
        no_new_ODE_or_original_radial_source_integrals=True,
        full_nonlinear_field_or_cut_claimed=False, elapsed_seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if a.out.exists(): raise FileExistsError(a.out)
    raw = gzip.compress((json.dumps(ans, separators=(',', ':'))+'\n').encode(), mtime=0)
    if len(raw) >= 5_000_000: raise ArithmeticError('Partition output')
    a.out.write_bytes(raw)
    print(json.dumps(dict(all_gates=True, gates=len(gates), sha256=sha(a.out), bytes=len(raw),
        block23_head_ratios=[float(ex(r['head_gain_over_original_parent'][23])) for r in changes],
        elapsed_seconds=ans['elapsed_seconds'], peak_rss_kib=ans['peak_rss_kib'])), flush=True)


if __name__ == '__main__': main()
