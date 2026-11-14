#!/usr/bin/env python3
"""Independent stored-data review; no author import, BVP, IVP, or tail engine."""
import argparse
import copy
import gzip
import hashlib
import io
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

T = Path(__file__).resolve().parent.parent
N = T / 'notes'
R = T.parent.parent
P = '2026-11-09-db6f-'
AUTHOR_WARM = N / (P + 'prefix-matched-cut-s63of64-warm-01.json.gz')
REPLAY_WARM = N / (P + 'tail-review-matched-cut-warm-replay.json.gz')
AUTHOR_REPORT = N / (P + 'prefix-matched-cut-s63of64-warm-01-preparation.json')
REPLAY_REPORT = N / (P + 'tail-review-matched-cut-warm-replay-preparation.json')
AUTHOR_LAUNCH = N / (P + 'prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01-input-bindings.json')
REPLAY_LAUNCH = N / (P + 'tail-review-matched-cut-run-replay-input-bindings.json')
METHOD = N / (P + 'prefix-matched-cut-hermite-warm-interface.md')
LEDGER = N / (P + 'prefix-matched-cut-hermite-warm-interface-sources.json')
PUBLICATION = N / (P + 'prefix-matched-cut-s63of64-publication.json')
PREPARER = T / 'scripts/db6f-prefix-prepare-matched-cut-warm.py'
PINS = {
    METHOD: '9c26c977f6bc173b8e8710672c4258dfcaa55ea1a4abbedabb5215204c77ef2f',
    LEDGER: 'bcdbb73657f477e7db770640ead238ed1365436122817a662933d26a520a7f18',
    PREPARER: '246e36312e7dc80b7f8c16dc8759423752c6370ad923eeba14a5545e5a3ecf48',
    AUTHOR_WARM: 'cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc',
    AUTHOR_REPORT: '31bc073433407e02edb11ec7ea41478195b46d95de1bb73d04b864e56c40a358',
    AUTHOR_LAUNCH: '5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21',
    PUBLICATION: 'bd8151805eaf1cb5eb26b0c8ccbfeaee26643fbb5554c8caf9812414a4b0f08d',
}
IO = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
      'trialDiagnosticFile', 'trialStatePrefix'}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def record(p):
    p = Path(p).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}


def read(p):
    p = Path(p)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def canon(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_binding(entry):
    p = Path(entry['path'])
    if not p.is_absolute():
        p = R / p
    actual = record(p)
    require(actual['sha256'] == entry['sha256'], 'Changed source ' + str(p))
    if 'bytes' in entry:
        require(actual['bytes'] == entry['bytes'], 'Changed length ' + str(p))
    return actual


def array(cp, cp_path):
    parts = []
    first = 0
    for b in cp['pp_coefficient_chunks']:
        p = cp_path.parent / b['file']
        require(p.parent.resolve() == cp_path.parent.resolve(), 'Chunk escaped topic notes')
        require(sha(p) == b['sha256'] and p.stat().st_size == b['bytes'], 'Chunk identity')
        require(p.stat().st_size < 5_000_000, 'Per-file limit')
        a = np.load(io.BytesIO(gzip.decompress(p.read_bytes())), allow_pickle=False)
        require(a.dtype == np.float64 and a.ndim == 3, 'dtype/rank')
        require(a.shape[:2] == (6, 2632), 'degree/interval axes')
        require(b['state_first'] == first and b['state_last_exclusive'] == first+a.shape[2], 'State partition')
        first += a.shape[2]
        parts.append(a)
    a = np.concatenate(parts, axis=2)
    require(a.shape == (6, 2632, 46) and np.all(np.isfinite(a)), 'Complete finite M15 array')
    return a


def bits(x, y):
    return np.asarray(x).shape == np.asarray(y).shape and np.asarray(x).tobytes() == np.asarray(y).tobytes()


def fq(x):
    return Q.from_float(float(x))


def frac_record(q):
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator), 'display': float(q)}


def shift_by_horner(descending_coefficients, left):
    """Independent polynomial composition p(left+u), ascending output."""
    acc = [descending_coefficients[0]]
    for c in descending_coefficients[1:]:
        nxt = [left*acc[0]+c]
        nxt.extend(acc[j-1]+left*acc[j] for j in range(1, len(acc)))
        nxt.append(acc[-1])
        acc = nxt
    return acc


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    require(not args.out.exists(), 'Refuse overwrite')
    for path, expected in PINS.items():
        require(sha(path) == expected, 'Frozen author pin ' + str(path))
    author_launch, replay_launch = read(AUTHOR_LAUNCH), read(REPLAY_LAUNCH)
    author_report, replay_report = read(AUTHOR_REPORT), read(REPLAY_REPORT)
    ledger, publication = read(LEDGER), read(PUBLICATION)
    require(len(ledger['files']) == 34, 'Static ledger size')
    require(len(author_launch['bound_files']) == len(replay_launch['bound_files']) == 121, 'Launch binding size')
    require(len(publication['files']) == 9, 'Closed author inventory size')
    unique = {}
    for items in [ledger['files'], author_launch['bound_files'], replay_launch['bound_files'], publication['files']]:
        for entry in items:
            bound = check_binding(entry)
            unique[bound['path']] = bound
    require(author_launch['status'] == replay_launch['status'] == 'PREPARED_ONLY_ORIGINAL_COUPLED_NOT_STARTED', 'Launch identity')

    original_launch_path = Path(author_launch['original_command_binding']['path'])
    original = read(original_launch_path)
    command, newcommand = original['command'], author_launch['command']
    changes = []
    require(len(command) == len(newcommand), 'Argv length')
    for index, (old, new) in enumerate(zip(command, newcommand)):
        if old != new:
            require(index > 0, 'Executable changed')
            changes.append(command[index-1])
    require(sorted(changes) == sorted(['--restart', '--tail-config', '--out-prefix']), 'Only three path changes')
    option = lambda cmd, key: cmd[cmd.index(key)+1]
    oldcfg = read(option(command, '--tail-config'))
    newcfg = read(option(newcommand, '--tail-config'))
    changed_keys = {k for k in oldcfg.keys() | newcfg.keys()
                    if (k in oldcfg) != (k in newcfg) or canon(oldcfg.get(k)) != canon(newcfg.get(k))}
    require(changed_keys == IO, 'Exactly five typed I/O fields')
    expected_run = Path(author_launch['out_prefix'])
    for key, suffix in [('traceFile', '-tail-trace.jsonl'), ('iterationCheckpointFile', '-tail-iteration.json.gz'),
                        ('trialDiagnosticFile', '-tail-trials.jsonl'), ('trialStatePrefix', '-tail-trial-stage')]:
        require(newcfg[key] == str(expected_run)+suffix, 'New independent output ' + key)
    require(newcfg.get('correctInitialBoundary', True) is True, 'Original boundary correction')
    require(newcfg.get('projectionFloor', .05) == .05, 'Original floor')
    require(option(newcommand, '--restart') == str(AUTHOR_WARM), 'Actual UNSOLVED restart')
    require(command[command.index('--warmup-scales')+1] == '--lagged-tail', 'Empty warmup')
    for flag in ['--fixed', '--lagged-tail', '--preserve-restart-mesh']:
        require(flag in newcommand, 'Original flag ' + flag)

    warm, replay = read(AUTHOR_WARM), read(REPLAY_WARM)
    old_path = Path(warm['source_affine_checkpoint']['path'])
    old = read(old_path)
    success_path = Path(warm['source_successful_tail']['path'])
    success = read(success_path)
    require(newcfg['initialCheckpoint'] == str(success_path), 'Successful warm source')
    require(success['response']['converged'] is True, 'True source response')
    require(success['request']['jacobian'] is False and success['request']['audit'] is False, 'Unaudited source scope')
    require(0 <= success['response']['residual'] < newcfg['solveTolerance'], 'Original source tolerance')
    for rec in [warm, replay]:
        require(rec['status'] == 'UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS', 'Warm status')
        require(rec['solver_success'] is False and rec['config']['actual_nonlinear_tail'] is False, 'No inherited success')
        for key in rec['invalidated_original_results']:
            if key != 'solver_success':
                require(key not in rec, 'Stale result ' + key)
        for key in author_report['preserved_metadata']:
            require(canon(rec[key]) == canon(old[key]), 'Copied physical/parameter field ' + key)
    warm_copy, replay_copy = copy.deepcopy(warm), copy.deepcopy(replay)
    for rec in [warm_copy, replay_copy]:
        for b in rec['pp_coefficient_chunks']:
            del b['file']
    require(canon(warm_copy) == canon(replay_copy), 'All warm metadata except output chunk names')

    a0, a1, a2 = array(old, old_path), array(warm, AUTHOR_WARM), array(replay, REPLAY_WARM)
    require(bits(a1, a2), 'Full independent replay array')
    compressed_equal = []
    for b1, b2 in zip(warm['pp_coefficient_chunks'], replay['pp_coefficient_chunks']):
        compressed_equal.append(sha(AUTHOR_WARM.parent / b1['file']) == sha(REPLAY_WARM.parent / b2['file']))
    require(all(compressed_equal), 'Compressed chunk bytes')
    require(bits(a0[:, :, :31], a1[:, :, :31]), 'Untouched R/T block')
    mesh = list(map(fq, old['mesh']))
    require(mesh[0] == 0 and all(a < b for a, b in zip(mesh, mesh[1:])), 'Physical mesh')
    length, last_width = mesh[-1], mesh[-1]-mesh[-2]
    height = success['request']['height']
    multiplier = fq(-.1)
    delta = []
    for j in range(15):
        endpoint = sum((fq(a0[k, -1, 31+j])*last_width**(5-k) for k in range(6)), Q(0))
        delta.append(fq(height[j])/multiplier-endpoint)
    require(canon([frac_record(x) for x in delta]) == canon(author_report['exact_delta_Z']), 'Independent exact endpoint/delta')
    global_descending = [6/length**5, -15/length**4, 10/length**3, Q(0), Q(0), Q(0)]
    require(shift_by_horner(global_descending, Q(0))[:3] == [0, 0, 0], 'Zero initial two-jet')
    end_coeff = shift_by_horner(global_descending, length)
    require(end_coeff[:3] == [1, 0, 0], 'Final value/derivatives')
    maximum_rounding = Q(0)
    tested = 0
    for interval, left in enumerate(mesh[:-1]):
        shifted = shift_by_horner(global_descending, left)
        for j, d in enumerate(delta):
            for power, weight in enumerate(shifted):
                oldvalue = a0[5-power, interval, 31+j]
                exact = fq(oldvalue)+weight*d
                expected = oldvalue if weight == 0 or d == 0 else float(exact)
                require(np.float64(expected).tobytes() == a1[5-power, interval, 31+j].tobytes(), 'Independent shifted coefficient')
                maximum_rounding = max(maximum_rounding, abs(fq(expected)-exact))
                tested += 1
    require(canon(frac_record(maximum_rounding)) == canon(author_report['maximum_coefficient_rounding_error']), 'Exact rounding maximum')
    for derivative in range(3):
        require(bits(a0[5-derivative, 0, :], a1[5-derivative, 0, :]), 'All 46 central coefficient jets')

    nonrepresentable = []
    for mode, h in enumerate(height, 1):
        nearest = float(fq(h)/multiplier)
        if -.1*nearest == h:
            continue
        values = [math.nextafter(nearest, -math.inf), nearest, math.nextafter(nearest, math.inf)]
        products = [-.1*v for v in values]
        adjacent_bracket = any(min(a, b) < h < max(a, b) for a, b in zip(products, products[1:]))
        require(adjacent_bracket and all(v != h for v in products), 'Adjacent rounded-product gap')
        nonrepresentable.append(mode)
    require(nonrepresentable == [1, 6, 8, 11], 'Four normalized-product gaps')
    actual = author_report['actual_restart_request_height']
    diff = [a-b for a, b in zip(actual, height)]
    require(canon(diff) == canon(author_report['actual_restart_request_difference']), 'Actual request error')
    changed_modes = [j+1 for j, d in enumerate(diff) if d != 0]
    require(changed_modes == [1, 5, 6, 7, 8, 11, 12, 14, 15], 'Nine actual request differences')

    ignored_top = {'new_warm', 'new_config', 'sources', 'preparation_seconds', 'new_restart_info'}
    left = {k: v for k, v in author_report.items() if k not in ignored_top}
    right = {k: v for k, v in replay_report.items() if k not in ignored_top}
    require(canon(left) == canon(right), 'All deterministic mathematics/report fields')
    left = {k: v for k, v in author_report['new_restart_info'].items() if k not in {'source', 'source_sha256'}}
    right = {k: v for k, v in replay_report['new_restart_info'].items() if k not in {'source', 'source_sha256'}}
    require(canon(left) == canon(right), 'All deterministic restart diagnostics')
    require(all(author_report['restart_invariants'].values()) and all(replay_report['restart_invariants'].values()), 'Original restart invariants')
    for report in [author_report, replay_report]:
        for k in ['denied_entry_attempts', 'subprocesses_started', 'solve_bvp_calls', 'solve_ivp_calls',
                  'true_tail_DN_calls', 'angular_momentum_root_calls']:
            require(type(report[k]) is int and report[k] == 0, 'No solver/process ' + k)
        require(report['full_Cartesian_or_mean_two_jet_evaluated'] is False, 'Scope of numerical comparison')

    out = {
        'status': 'PASS-independent-stored-coefficients-input-identity-and-pure-replay',
        'reviewer': '/root/tail_theory',
        'scope': 'Independent exact coefficient arithmetic and stored-data checks. Original preparer replay is a separate observed process. No BVP/IVP, tail root, RK, DN, or actual-geometry evaluation by this checker.',
        'checker': record(__file__),
        'inputs': [record(p) for p in [METHOD, LEDGER, PREPARER, AUTHOR_WARM, REPLAY_WARM, AUTHOR_REPORT,
                                      REPLAY_REPORT, AUTHOR_LAUNCH, REPLAY_LAUNCH, PUBLICATION]],
        'binding_counts': {'static_ledger': 34, 'author_launch': 121, 'replay_launch': 121,
                           'author_publication': 9, 'distinct_files_rehashed': len(unique)},
        'full_array_shape': list(a1.shape),
        'total_stored_scalars': int(a1.size),
        'independently_recomputed_Z_coefficients': tested,
        'bitwise_preserved_R_T_coefficients': int(a0[:, :, :31].size),
        'coefficient_blocks_byte_equal': compressed_equal,
        'whole_replay_array_byte_equal': True,
        'method': 'Independent exact power-sum endpoint plus Horner polynomial shift, rather than the author binomial formula.',
        'maximum_coefficient_rounding_error': frac_record(maximum_rounding),
        'central_46_slot_two_jet_coefficients_equal': True,
        'original_restart_math_fields_identical': True,
        'actual_request_different_modes': changed_modes,
        'normalization_nonrepresentable_modes': nonrepresentable,
        'actual_height_max_difference': max(map(abs, diff)),
        'source_success_only_unaudited_warm': True,
        'changed_argv_values': sorted(changes),
        'changed_configuration_fields': sorted(changed_keys),
        'output_paths_independent_from_old_active_IO': True,
        'old_success_fields_not_inherited': True,
        'original_initial_boundary_correction_retained': True,
        'future_actual_coupled_launch_executed': False,
    }
    with args.out.open('x') as f:
        json.dump(out, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')
    print(json.dumps({'status': out['status'], 'rehashed_files': len(unique),
                      'exact_Z_checks': tested, 'out_sha256': sha(args.out)}))


if __name__ == '__main__':
    main()
