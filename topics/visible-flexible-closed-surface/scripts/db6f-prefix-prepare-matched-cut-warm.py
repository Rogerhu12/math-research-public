#!/usr/bin/env python3
"""Build an UNSOLVED Z-only Hermite warm; never run a BVP or a true tail DN.

Fixed inputs: the reviewed affine M15 checkpoint and the closed successful
continuation03 call001 (63/64).  Only initial data and five output/input paths
change.  A pure original-constructor/restart check is performed with numerical
solvers and process creation blocked inside this preparation process.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
import math
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
REPO = TOPIC.parent.parent
METHOD = NOTES / '2026-11-09-db6f-prefix-matched-cut-hermite-warm-interface.md'
METHOD_SHA = '9c26c977f6bc173b8e8710672c4258dfcaa55ea1a4abbedabb5215204c77ef2f'
SOURCES = NOTES / '2026-11-09-db6f-prefix-matched-cut-hermite-warm-interface-sources.json'
SOURCES_SHA = 'bcdbb73657f477e7db770640ead238ed1365436122817a662933d26a520a7f18'
OLD = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine-input-bindings.json'
AFFINE = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz'
SUCCESS = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-03_tail_0001.json.gz'
SUCCESS_SHA = '3a258afc492f4204f85c0ef4535c00d041983c27d8ebd8c9b907df0961a32a0b'
SUCCESS_AUDIT = NOTES / '2026-11-09-db6f-root-continuation03-call001-closed-audit-v2.json'
RESUME_LAUNCH = NOTES / '2026-11-09-db6f-prefix-amplitude-resume03-launch.json'
DEFAULT_WARM = NOTES / '2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01'
DEFAULT_RUN = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01'
IO_KEYS = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
           'trialDiagnosticFile', 'trialStatePrefix'}
JET_SCALARS = {'radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep',
               'meanSlope', 'meanSecond', 'meanSlopeCorrection', 'meanSecondCorrection',
               'minLeading', 'minD', 'endpointFullD', 'endpointPhi', 'formalCurvature'}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def item(p):
    p = Path(p).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    if p.suffix == '.gz':
        raw = gzip.decompress(raw)
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)


def number(x):
    return type(x) in (float, int) and math.isfinite(x)


def vector(x, count):
    return type(x) is list and len(x) == count and all(number(v) for v in x)


def checked_file(p, expected, files):
    p = Path(p)
    if not p.is_absolute():
        p = REPO / p
    rec = item(p)
    if rec['sha256'] != expected:
        raise ValueError('Changed frozen input: ' + str(p))
    files[str(p.resolve())] = rec


def bind_items(entries, files):
    for x in entries:
        checked_file(x['path'], x['sha256'], files)


def write_new(p, data):
    p = Path(p)
    if len(data) >= 5_000_000:
        raise ValueError('Output exceeds repository file limit: ' + str(p))
    with p.open('xb') as f:
        f.write(data)


def write_json(p, x):
    raw = (json.dumps(x, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    if Path(p).suffix == '.gz':
        raw = gzip.compress(raw, compresslevel=9, mtime=0)
    elif len(raw) >= 1_000_000:
        raise ValueError('Large JSON must be compressed')
    write_new(p, raw)


def q(x):
    return Fraction.from_float(float(x))


def fraction_record(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator),
            'display': float(x)}


def exact_endpoint(coef, mesh, slot):
    h = q(mesh[-1])-q(mesh[-2])
    out = Fraction(0)
    for c in coef[:, -1, slot]:
        out = out*h+q(c)
    return out


def read_coefficients(rec, folder, files):
    arrays = []
    first = 0
    for block in rec['pp_coefficient_chunks']:
        p = folder / block['file']
        if p.parent.resolve() != folder.resolve():
            raise ValueError('Coefficient path escaped its source directory')
        checked_file(p, block['sha256'], files)
        data = np.load(io.BytesIO(gzip.decompress(p.read_bytes())), allow_pickle=False)
        if (data.dtype != np.dtype('float64') or data.ndim != 3
                or data.shape[0] != 6 or data.shape[1] != len(rec['mesh'])-1
                or block['state_first'] != first
                or block['state_last_exclusive'] != first+data.shape[2]):
            raise ValueError('Unexpected frozen coefficient schema')
        first += data.shape[2]
        arrays.append(data)
    coef = np.concatenate(arrays, axis=2)
    if coef.shape != (6, len(rec['mesh'])-1, 46) or not np.all(np.isfinite(coef)):
        raise ValueError('Expected finite M15 quintic coefficients')
    return coef


def hermite_coefficients(coef, mesh, height, multiplier):
    """Round exact rational old coefficient plus exact global quintic once."""
    out = coef.copy()
    L = q(mesh[-1])
    if mesh[0] != 0 or not L > 0:
        raise ValueError('Unexpected physical domain')
    delta = [q(height[j])/q(multiplier)-exact_endpoint(coef, mesh, 31+j)
             for j in range(15)]
    beta = [Fraction(0)]*3+[10/L**3, -15/L**4, 6/L**5]
    max_round = Fraction(0)
    for i, left in enumerate(mesh[:-1]):
        a = q(left)
        local = [sum((beta[k]*math.comb(k, m)*a**(k-m)
                      for k in range(m, 6)), Fraction(0)) for m in range(6)]
        for m, weight in enumerate(local):
            if weight == 0:
                continue
            for j, d in enumerate(delta):
                if d == 0:
                    continue
                value = q(coef[5-m, i, 31+j])+weight*d
                rounded = float(value)
                if not math.isfinite(rounded):
                    raise ValueError('Nonfinite coefficient after Hermite update')
                out[5-m, i, 31+j] = rounded
                max_round = max(max_round, abs(q(rounded)-value))
    return out, delta, max_round


def save_warm(path, rec, coef):
    block = max(1, int(4_400_000/(coef.shape[0]*coef.shape[1]*8)))
    chunks = []
    for index, first in enumerate(range(0, coef.shape[2], block)):
        last = min(first+block, coef.shape[2])
        p = path.with_name(path.name.removesuffix('.json.gz')+f'_coeff_{index:02d}.npy.gz')
        stream = io.BytesIO()
        np.save(stream, coef[:, :, first:last], allow_pickle=False)
        write_new(p, gzip.compress(stream.getvalue(), compresslevel=9, mtime=0))
        chunks.append({'file': p.name, 'state_first': first, 'state_last_exclusive': last,
                       'bytes': p.stat().st_size, 'sha256': sha(p)})
    rec = dict(rec, pp_coefficient_chunks=chunks,
               array_format='Exact stored float64 NumPy arrays; gzip partitioned by state. '
                            'Each changed coefficient is nearest-binary64 rounding of the '
                            'stated exact rational Hermite update; no source-solver claim.')
    write_json(path, rec)
    return rec


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def restart_pair(command, warm_path, source_files):
    """Use original initialization only, with solve/process entry points denied."""
    import scipy.integrate
    denied = {'calls': 0}

    def forbidden(*args, **kwargs):
        denied['calls'] += 1
        raise RuntimeError('Solver/process entry forbidden in a warm preparer')

    scipy.integrate.solve_bvp = forbidden
    scipy.integrate.solve_ivp = forbidden
    subprocess.Popen = forbidden
    subprocess.run = forbidden
    option = lambda name: command[command.index(name)+1]
    runner = load_module('db6f_matched_cut_original', Path(command[1])).runner
    runner.solve_bvp = forbidden
    source_root = Path(option('--source-root')).resolve()
    runner.adaptive.old.install_source(source_root)
    cfg = read(option('--profile'))
    chart = read(option('--chart'))
    port = read(option('--linear-port'))
    port['_sha256'] = sha(option('--linear-port'))
    _, Base = runner.adaptive.build_classes(chart)

    class BVP(runner.TailMixin, Base):
        pass

    helper = load_module('db6f_matched_cut_restart', HERE/'db6f-prefix-preserve-restart.py')
    answers = []
    for checkpoint in [AFFINE, warm_path]:
        obj = BVP(cfg, port, .1, 15, 512, True, .1)
        obj.restart_remesh = 1601
        obj.bcweights = np.full(15, 2e-11/1e-8)
        x, y, par, info = helper.restart(obj, checkpoint, chart)
        physical, ds = obj.chart(x, par[0])
        answers.append({'x': x, 'y': y, 'par': par, 'physical': physical, 'ds': ds,
                        'height': obj.bridge.sigma*obj.q*y[obj.iz:, -1], 'info': info,
                        'support': obj.support_amplitude, 'sigma': obj.bridge.sigma,
                        'q': obj.q, 'warp': obj.warp_q})
    for m in tuple(sys.modules.values()):
        name = getattr(m, '__file__', None)
        if name:
            p = Path(name).resolve()
            if p.suffix == '.py' and (p.is_relative_to(TOPIC) or p.is_relative_to(source_root)):
                source_files[str(p)] = item(p)
    if denied['calls'] != 0:
        raise RuntimeError('A forbidden numerical or process call was attempted')
    return answers, denied


def bits(a, b):
    return np.asarray(a).shape == np.asarray(b).shape and np.asarray(a).tobytes() == np.asarray(b).tobytes()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--warm-prefix', type=Path, default=DEFAULT_WARM)
    ap.add_argument('--coupled-prefix', type=Path, default=DEFAULT_RUN)
    args = ap.parse_args()
    warm_prefix, run_prefix = args.warm_prefix.resolve(), args.coupled_prefix.resolve()
    for prefix in [warm_prefix, run_prefix]:
        if prefix.parent != NOTES or any(prefix.parent.glob(prefix.name+'*')):
            raise FileExistsError('Output must be new and in topic notes: '+str(prefix))
    if warm_prefix == run_prefix:
        raise ValueError('Warm and actual-solver stems must differ')
    started = time.monotonic()
    sources = {}
    checked_file(METHOD, METHOD_SHA, sources)
    checked_file(SOURCES, SOURCES_SHA, sources)
    bind_items(read(SOURCES)['files'], sources)
    bind_items(read(OLD)['bound_files'], sources)
    bind_items(read(RESUME_LAUNCH)['bound_files'], sources)
    success_audit = read(SUCCESS_AUDIT)
    if (success_audit['status'] != 'PASS-closed-converged-finite-DN-provenance-and-request-audit'
            or success_audit['call'] != 1 or success_audit['scale'] != 63/64):
        raise ValueError('Wrong closed success audit')
    bind_items(success_audit['closed_files'], sources)
    for p in [OLD, SUCCESS_AUDIT, RESUME_LAUNCH, Path(__file__).resolve(),
              HERE/'db6f-prefix-run-bound-command.py']:
        sources[str(p.resolve())] = item(p)
    checked_file(SUCCESS, SUCCESS_SHA, sources)
    original = read(OLD)
    command = original['command']
    option = lambda name: command[command.index(name)+1]
    expected = {'--amplitude': '.1', '--warp-reference': '.1', '--modes': '15',
                '--angular': '512', '--audit-angular': '1024', '--nodes': '1601',
                '--max-nodes': '4500', '--tol': '2e-9', '--bc-tol': '1e-8',
                '--physical-bc-tol': '2e-11', '--node-heap': '1536'}
    if any(option(k) != v for k, v in expected.items()):
        raise ValueError('Original numerical command changed')
    if option('--restart') != str(AFFINE) or '--fixed' not in command or '--preserve-restart-mesh' not in command:
        raise ValueError('Original restart/fixed-metric path changed')
    if command[command.index('--warmup-scales')+1] != '--lagged-tail':
        raise ValueError('Original empty warmup/lagged path changed')
    affine = read(AFFINE)
    record = read(SUCCESS)
    response = record['response']
    cfg = read(option('--tail-config'))
    strip = lambda x: {k: v for k, v in x.items() if k not in IO_KEYS}
    if canonical(strip(cfg)) != canonical(strip(record['config'])):
        raise ValueError('Successful tail does not use the original finite equations')
    if cfg.get('correctInitialBoundary', True) is not True or cfg.get('projectionFloor', .05) != .05:
        raise ValueError('Original boundary correction or root guard changed')
    if (response.get('converged') is not True or not number(response.get('residual'))
            or not 0 <= response['residual'] < cfg['solveTolerance']
            or response['residual'] != success_audit['residual']
            or record['request']['jacobian'] is not False or record['request']['audit'] is not False):
        raise ValueError('Not the recorded true successful warm response')
    jets = response['jets']
    if (set(jets) != JET_SCALARS | {'height', 'slope', 'second'}
            or not all(number(jets[k]) for k in JET_SCALARS)
            or not all(vector(jets[k], 15) for k in ['height', 'slope', 'second'])):
        raise ValueError('Bad original jet schema')
    H = record['request']['height']
    cp = response['checkpoint']
    desired = (np.asarray(affine['predicted_cut_height'])*np.float64(63/64)**np.arange(1, 16)).tolist()
    if (not vector(H, 15) or canonical(H) != canonical(desired)
            or canonical(H) != canonical(cp['cutHeight'])
            or len(cp['states']) != 865 or not all(vector(row, 30) for row in cp['states'])
            or len(cp['rawNode']) != 13 or len(cp['rawStates']) != 13
            or not all(type(k) is int and 0 <= k < 865 for k in cp['rawNode'])
            or any(canonical(row) != canonical(cp['states'][k])
                   for row, k in zip(cp['rawStates'], cp['rawNode']))):
        raise ValueError('Successful checkpoint/request state mismatch')
    if affine['config']['actual_nonlinear_tail'] is not False or affine['config']['modes'] != 15:
        raise ValueError('Expected the original UNSOLVED M15 affine prefix')
    mesh = np.asarray(affine['mesh'], float)
    if (len(mesh) != 2633 or not np.all(np.diff(mesh) > 0)
            or mesh[-1] != affine['meridian_length'] or affine['gauge_amplitude'] != .1):
        raise ValueError('Unexpected original physical mesh/gauge')
    coef = read_coefficients(affine, AFFINE.parent, sources)
    multiplier = -.1
    print(json.dumps({'event': 'prepare_exact_Hermite_coefficients', 'intervals': len(mesh)-1,
                      'changed_state_slots': '31..45', 'solver_calls': 0}), flush=True)
    changed, delta, round_error = hermite_coefficients(coef, mesh, H, multiplier)
    if not bits(coef[:, :, :31], changed[:, :, :31]):
        raise ValueError('A non-Z coefficient changed')
    pp0 = PPoly.construct_fast(coef, mesh, extrapolate=True, axis=1)
    pp1 = PPoly.construct_fast(changed, mesh, extrapolate=True, axis=1)
    center = [{'order': k, 'all_46_states_bitwise_equal': bits(pp0(0., k), pp1(0., k)),
               'maximum_absolute_difference': float(abs(pp0(0., k)-pp1(0., k)).max())}
              for k in range(3)]
    if not all(row['all_46_states_bitwise_equal'] for row in center):
        raise ValueError('Central coefficient two-jet changed')
    keep = ('angular_chart', 'chart', 'warp_reference_q', 'frozen_profile', 'gauge_amplitude',
            'physical_port_sha256', 'physical_tail_parameters', 'physical_tail_cut',
            'actual_primary_amplitude', 'meridian_length', 'parameters',
            'central_correction_scales', 'nodes', 'mesh')
    warm = {k: affine[k] for k in keep}
    warm.update(status='UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS',
                scope=__doc__, solver_success=False,
                config={k: v for k, v in affine['config'].items() if k != 'frozen_affine_dn'},
                source_affine_checkpoint=item(AFFINE), source_successful_tail=item(SUCCESS),
                preparation_source=item(Path(__file__).resolve()),
                matched_cut_request=H,
                height_match_scope='Exact real Hermite formula before coefficient rounding. '
                                   'The actual original restart request is recorded separately '
                                   'and must receive a new true DN/J response.',
                invalidated_original_results=['solver_success', 'message',
                    'max_rms_collocation_residual', 'newton_domain_audit', 'summary', 'seconds',
                    'predicted_cut_height', 'predicted_slope_from_surrogate',
                    'restart_mesh_diagnostics', 'frozen_actual_tail',
                    'frozen_actual_tail_sha256'])
    warm['config']['actual_nonlinear_tail'] = False
    warm['config']['initial_guess_construction'] = 'Z-only-global-quintic-Hermite'
    warm_path = warm_prefix.with_suffix('.json.gz')
    stored = save_warm(warm_path, warm, changed)
    print(json.dumps({'event': 'warm_written_checking_original_restart', 'solver_calls': 0}), flush=True)
    answers, denied = restart_pair(command, warm_path, sources)
    old_init, new_init = answers
    required = {'numerical_mesh': bits(old_init['x'], new_init['x']),
                'physical_mesh': bits(mesh, new_init['physical']),
                'all_free_parameters': bits(old_init['par'], new_init['par']),
                'R_T_all_restart_values': bits(old_init['y'][:31], new_init['y'][:31]),
                'all_inlet_values': bits(old_init['y'][:, 0], new_init['y'][:, 0]),
                'support_amplitude': old_init['support'] == new_init['support'] == affine['actual_primary_amplitude'],
                'gauge': old_init['q'] == new_init['q'] == .1,
                'warp_reference': old_init['warp'] == new_init['warp'] == .1,
                'bridge_sigma': old_init['sigma'] == new_init['sigma'] == -1}
    if not all(required.values()):
        raise ValueError('Original restart invariants failed: '+str(required))
    actual_H = new_init['height']
    error = actual_H-np.asarray(H)
    if not np.all(np.isfinite(actual_H)) or float(abs(error).max()) > 1e-18:
        raise ValueError('Unexpected large actual restart-to-known-DN height difference')
    rounding_slots = []
    for j, h in enumerate(H):
        y = h/multiplier
        if multiplier*y == h:
            continue
        low, high = math.nextafter(y, -math.inf), math.nextafter(y, math.inf)
        bracket = (min(multiplier*y, multiplier*low) < h < max(multiplier*y, multiplier*low)
                   or min(multiplier*y, multiplier*high) < h < max(multiplier*y, multiplier*high))
        if not bracket or multiplier*low == h or multiplier*high == h:
            raise ValueError('Unexpected normalization representability change')
        rounding_slots.append({'mode': j+1, 'target_height': h, 'nearest_quotient': y,
                               'rounded_product': multiplier*y,
                               'roundtrip_difference': multiplier*y-h,
                               'strict_adjacent_product_gap': True})
    if [row['mode'] for row in rounding_slots] != [1, 6, 8, 11]:
        raise ValueError('The recorded four nonrepresentable slots changed')
    cfg_path = run_prefix.with_name(run_prefix.name+'-tail-config.json')
    newcfg = dict(cfg)
    newcfg.update(initialCheckpoint=str(SUCCESS),
                  traceFile=str(run_prefix)+'-tail-trace.jsonl',
                  iterationCheckpointFile=str(run_prefix)+'-tail-iteration.json.gz',
                  trialDiagnosticFile=str(run_prefix)+'-tail-trials.jsonl',
                  trialStatePrefix=str(run_prefix)+'-tail-trial-stage')
    if canonical(strip(cfg)) != canonical(strip(newcfg)):
        raise ValueError('A non-I/O tail configuration field changed')
    write_json(cfg_path, newcfg)
    for p in [warm_path, cfg_path]:
        sources[str(p)] = item(p)
    for block in stored['pp_coefficient_chunks']:
        p = warm_path.parent/block['file']
        sources[str(p)] = item(p)
    ratios = actual_H[0]/H[0]
    warm_delta = actual_H/(jets['radius']**4)-ratios*np.asarray(cp['states'][0][:15])
    report_path = warm_prefix.with_name(warm_prefix.name+'-preparation.json')
    report = {'status': 'PREPARED_UNSOLVED_WARM_ORIGINAL_RESTART_CHECKED',
              'scope': __doc__, 'preparer': item(Path(__file__).resolve()),
              'matched_method': item(METHOD), 'known_successful_tail': item(SUCCESS),
              'source_successful_scale': '63/64', 'source_successful_residual': response['residual'],
              'new_warm': item(warm_path), 'new_config': item(cfg_path),
              'central_coefficient_jets': center, 'R_T_coefficients_bitwise_unchanged': True,
              'preserved_metadata': list(keep),
              'exact_delta_Z': [fraction_record(v) for v in delta],
              'maximum_coefficient_rounding_error': fraction_record(round_error),
              'original_PPoly_cut_height': (multiplier*pp0(mesh[-1])[31:]).tolist(),
              'saved_PPoly_cut_height': (multiplier*pp1(mesh[-1])[31:]).tolist(),
              'known_successful_request_height': H,
              'actual_restart_request_height': actual_H.tolist(),
              'actual_restart_request_difference': error.tolist(),
              'actual_restart_request_max_difference': float(abs(error).max()),
              'actual_restart_request_bitwise_equal': bits(actual_H, np.asarray(H)),
              'normalization_nonrepresentable_slots': rounding_slots,
              'cut_nonmean_derivative_change_max': {
                  str(k): float(abs(pp1(mesh[-1], k)[31:]-pp0(mesh[-1], k)[31:]).max())
                  for k in (1, 2)},
              'restart_invariants': required, 'old_restart_info': old_init['info'],
              'new_restart_info': new_init['info'],
              'original_boundary_warm_preview_only': {
                  'ratio': float(ratios), 'maximum_normalized_height_delta': float(abs(warm_delta).max()),
                  'linear_tail_initial_called': False, 'actual_DN_called': False},
              'full_Cartesian_or_mean_two_jet_evaluated': False,
              'central_full_two_jet_basis': 'Only coefficient jets were compared numerically; '
                  'full-mean/Cartesian preservation is the conditional argument in the bound method.',
              'geometry_initialization_only': True, 'denied_entry_attempts': denied['calls'],
              'subprocesses_started': 0, 'solve_bvp_calls': 0, 'solve_ivp_calls': 0,
              'true_tail_DN_calls': 0, 'angular_momentum_root_calls': 0,
              'old_success_and_audits_invalidated': True,
              'original_equations_and_tolerances_unchanged': True,
              'original_empty_warmup_and_free_support_parameters_preserved': True,
              'sources': list(sources.values()), 'preparation_seconds': time.monotonic()-started}
    write_json(report_path, report)
    sources[str(report_path)] = item(report_path)
    newcommand = list(command)
    for flag, value in [('--restart', warm_path), ('--tail-config', cfg_path),
                        ('--out-prefix', run_prefix)]:
        newcommand[newcommand.index(flag)+1] = str(value)
    if sum(a != b for a, b in zip(command, newcommand)) != 3 or len(command) != len(newcommand):
        raise ValueError('Actual coupled argv changed beyond three paths')
    launch_path = run_prefix.with_name(run_prefix.name+'-input-bindings.json')
    launch = {'status': 'PREPARED_ONLY_ORIGINAL_COUPLED_NOT_STARTED',
              'scope': 'Independent matched intermediate-cut initialization, not continuation03 s=1 completion.',
              'cwd': str(REPO), 'out_prefix': str(run_prefix), 'command': newcommand,
              'bound_files': list(sources.values()), 'preparation_report': item(report_path),
              'original_command_binding': item(OLD),
              'command_changes': ['--restart', '--tail-config', '--out-prefix'],
              'changed_configuration_keys': sorted(IO_KEYS), 'warmup_scales': [],
              'source_successful_tail_is_only_warm': True, 'new_prefix_status': 'UNSOLVED',
              'first_request': 'Actual restarted H, jacobian=True, audit=False; no cached response.',
              'final_acceptance': 'Original true-DN outer BC and final seam audit plus all later '
                                  'same-g N512/actual-XYZ/continuous certificates remain required.',
              'original_final_preparer_v3_used_or_modified': False,
              'actual_launch_command': [sys.executable, str(HERE/'db6f-prefix-run-bound-command.py'),
                                       str(launch_path)]}
    write_json(launch_path, launch)
    print(json.dumps({'status': report['status'], 'new_warm': str(warm_path),
                      'warm_sha256': sha(warm_path), 'launch': str(launch_path),
                      'launch_sha256': sha(launch_path), 'sources': len(sources),
                      'central_jets_bitwise_equal': True,
                      'actual_height_max_difference': report['actual_restart_request_max_difference'],
                      'solver_calls': 0, 'seconds': report['preparation_seconds']}), flush=True)


if __name__ == '__main__':
    main()
