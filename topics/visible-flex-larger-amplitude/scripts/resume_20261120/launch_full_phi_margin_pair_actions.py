#!/usr/bin/env python3
"""Run a same-parent .992/.998 complete-Phi comparison in public Actions.

The existing launcher is used only with --print-command.  Its original bytes
are unchanged.  The two child argv lists differ only in numerical safety,
active band, and output directory.  Each child has one BLAS thread, independent
row caches, and the same actual parent, source paths, damping, and positions.

No field code is imported here.  --print-command is preparation only.  Actual
children require GITHUB_ACTIONS=true; all raw results remain in --work.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time


PAIRS = (('margin-0992', '.992', '.025'), ('margin-0998', '.998', '.031'))
DIFFERING_FLAGS = ('--reach-safety-factor', '--active-band', '--outdir')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def json_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


def json_safe(value):
    if isinstance(value, float) and not math.isfinite(value):
        return dict(nonfinite_float=repr(value))
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    return value


def flag_value(argv, flag):
    if argv.count(flag) != 1:
        raise ValueError('Expected exactly one option: ' + flag)
    return argv[argv.index(flag) + 1]


def replace_flag(argv, flag, value):
    flag_value(argv, flag)
    argv[argv.index(flag) + 1] = str(value)


def common_command(argv):
    result = argv.copy()
    for flag in DIFFERING_FLAGS:
        replace_flag(result, flag, '@PAIR_DIFFERENCE')
    return result


def commands(args):
    launcher = args.source_launcher.resolve()
    parent = args.outdir.resolve() if args.outdir else args.work.resolve() / 'full-phi-margin-pair'
    prepare = [sys.executable, str(launcher), '--repo', str(args.repo.resolve()),
        '--work', str(args.work.resolve()), '--bundle', str(args.bundle.resolve()),
        '--carrier', str(args.carrier.resolve()), '--damping', str(args.damping),
        '--maxiter', str(args.maxiter), '--directions', '1',
        '--active-rows', str(args.active_rows), '--qp-rtol', str(args.qp_rtol),
        '--qp-atol', str(args.qp_atol), '--outdir', str(parent / PAIRS[0][0]),
        '--print-command']
    for path in args.manifest:
        prepare.extend(['--manifest', str(path.resolve())])
    if args.coarse_centers is not None:
        prepare.extend(['--coarse-centers', args.coarse_centers])
    prepared = subprocess.run(prepare, text=True, capture_output=True, check=True)
    base = shlex.split(prepared.stdout.strip())
    if not base:
        raise ValueError('The original launcher returned no command')
    result = []
    for name, safety, band in PAIRS:
        argv = base.copy()
        replace_flag(argv, '--reach-safety-factor', safety)
        replace_flag(argv, '--active-band', band)
        replace_flag(argv, '--outdir', parent / name)
        result.append(dict(name=name, safety=safety, active_band=band,
            candidate_cutoff_decimal='.967', output=str(parent / name), command=argv))
    if common_command(result[0]['command']) != common_command(result[1]['command']):
        raise ValueError('The pair differs beyond the three declared options')
    return parent, prepare, result


def compact_statistics(value):
    spectral = value.get('spectral', {})
    result = {key: value[key] for key in (
        'max_relative_gram', 'radial_weighted_frobenius_sse',
        'radial_weighted_mean_sse', 'legacy_raw_frobenius_sse',
        'all_raw_frobenius_sse', 'min_relative_E', 'min_relative_determinant',
        'rho_sample_min') if key in value}
    for key in ('phi_normalized', 'smoothed_spectral_lp', 'phi_zero', 'normalization'):
        if key in spectral:
            result[key] = spectral[key]
    return result


def compact_direction(value):
    qp = value.get('qp', {})
    active = value.get('active_geometry', {})
    row_locations = [[row.get('curvature_point'), row.get('radius_point')]
                     for row in active.get('rows', [])]
    qp_keys = ('status', 'advances', 'seconds', 'initial_gradient_norm',
        'gradient_tolerance', 'final_face_projected_gradient_norm',
        'minimum_multiplier', 'maximum_linear_violation',
        'maximum_complementarity_residual', 'coordinate_norm',
        'maximum_active_face_rank', 'operator_products')
    result = {key: value[key] for key in ('index', 'damping', 'accepted',
        'accepted_alpha', 'new_merit', 'old_merit', 'seconds',
        'quadratic_predicted_actual_objective', 'maximum_selected_linear_product',
        'coordinate_norm', 'height_step', 'projected_endpoint_error',
        'direction_sha256', 'accepted_bundle_sha256') if key in value}
    result.update(qp={key: qp[key] for key in qp_keys if key in qp},
        release_events=sum(event.get('kind', '').startswith('release_negative_multiplier')
                           for event in qp.get('transitions', [])),
        selected_rows=active.get('selected_rows'), eligible_rows=active.get('eligible_rows'),
        protected_inequalities=active.get('protected_inequalities'),
        near_duplicate_primary_rows_deferred=active.get('near_duplicate_primary_rows_deferred'),
        selected_ordered_locations_sha256=json_sha(row_locations),
        row_cache_bytes=active.get('row_cache_bytes'))
    trials = []
    for trial in value.get('trials', []):
        item = {key: trial[key] for key in ('index', 'alpha', 'merit', 'finite',
            'feasible', 'descent', 'curvature_feasible', 'arithmetic_error') if key in trial}
        item['statistics'] = compact_statistics(trial.get('statistics', {}))
        item['point_filter'] = trial.get('curvature_filter')
        item['new_permanent_curvature_locations'] = trial.get('new_permanent_curvature_locations', [])
        item['new_permanent_radius_locations'] = trial.get('new_permanent_radius_locations', [])
        trials.append(item)
    result['trials'] = trials
    return result


def summarize(plan, returncode, seconds, log):
    path = Path(plan['output']) / 'report.json'
    summary = dict(name=plan['name'], safety=plan['safety'], active_band=plan['active_band'],
        returncode=returncode, wall_seconds=seconds, stdout_path=str(log),
        stdout_sha256=sha(log), report_path=str(path), report_available=path.is_file())
    if not path.is_file():
        return summary
    summary['report_sha256'] = sha(path)
    try:
        value = json.loads(path.read_text())
    except (OSError, ValueError) as error:
        summary['report_read_error'] = repr(error)
        return summary
    directions = [compact_direction(item) for item in value.get('directions', [])]
    summary.update(complete=value.get('complete', False),
        initial=compact_statistics(value.get('initial', {})),
        final=compact_statistics(value.get('current', value.get('initial', {}))),
        initial_point_filter=value.get('initial_curvature_filter'),
        final_point_filter=value.get('final_curvature_filter'),
        parent_bundle_sha256=value.get('bundle_sha256'),
        final_bundle=value.get('final_bundle'), final_bundle_sha256=value.get('final_bundle_sha256'),
        observation_carrier_sha256=value.get('observation_carrier_sha256'),
        process_peak_rss_KiB=value.get('process_peak_rss_KiB'),
        sample_target=bool(value.get('sample_target', False)),
        initial_stop_reason=value.get('stopped_before_linear_iteration'),
        directions=directions, actual_directions_computed=len(directions),
        accepted_directions=sum(bool(item.get('accepted')) for item in directions),
        final_curvature_location_count=len(value.get('final_curvature_memory', [])),
        final_radius_location_count=len(value.get('final_radius_memory', [])),
        source_sha256=value.get('source_sha256'),
        source_sha256_by_role=value.get('source_sha256_by_role'),
        continuous_geometry_certified=False,
        scope='Actual child values only. Point products use D lower bounds; no continuous K, marked D, reach or completion certificate is inherited.')
    return summary


def compare(summaries):
    first, second = summaries
    result = dict(declared_comparison='0998 minus 0992, same actual parent and mean-Phi damping',
        both_processes_returned=all(item.get('returncode') is not None for item in summaries),
        both_reports_complete=all(item.get('complete', False) for item in summaries),
        both_actual_directions_computed=all(item.get('actual_directions_computed', 0) == 1 for item in summaries),
        same_initial_statistics=bool(first.get('initial')) and first.get('initial') == second.get('initial'),
        same_actual_parent=first.get('parent_bundle_sha256') is not None and
                          first.get('parent_bundle_sha256') == second.get('parent_bundle_sha256'),
        same_actual_sources=first.get('source_sha256_by_role') is not None and
                            first.get('source_sha256_by_role') == second.get('source_sha256_by_role'))
    for key in ('phi_normalized', 'max_relative_gram', 'radial_weighted_frobenius_sse'):
        a, b = first.get('final', {}).get(key), second.get('final', {}).get(key)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result[key + '_difference'] = b-a
            result[key + '_ratio'] = b/a if a else None
    if all(item.get('directions') for item in summaries):
        result['same_initial_ordered_working_locations'] = (
            first['directions'][0].get('selected_ordered_locations_sha256') ==
            second['directions'][0].get('selected_ordered_locations_sha256'))
    for item in summaries:
        point_filter = item.get('final_point_filter') or {}
        result[item['name'] + '_known_point_product'] = point_filter.get('necessary_reach_product')
        result[item['name'] + '_own_numerical_screen_passed'] = point_filter.get('passed')
    result['no_winner_or_reach_claim'] = True
    result['scope'] = ('The two finite nonlinear runs report their actual metric gains and geometric costs. '
        'A lower Phi or passage of .998 does not establish reach >= .03 D. '
        'Original README standards, all variables, and permanent point checks remain unchanged.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'work', 'bundle', 'carrier'):
        parser.add_argument('--' + key, type=Path, required=True)
    parser.add_argument('--manifest', type=Path, action='append', required=True)
    parser.add_argument('--source-launcher', type=Path,
        default=Path(__file__).resolve().with_name('launch_full_phi_qp_actions.py'))
    parser.add_argument('--outdir', type=Path)
    parser.add_argument('--damping', type=float, required=True)
    parser.add_argument('--maxiter', type=int, default=256)
    parser.add_argument('--active-rows', type=int, default=192)
    parser.add_argument('--qp-rtol', type=float, default=1e-6)
    parser.add_argument('--qp-atol', type=float, default=1e-12)
    parser.add_argument('--coarse-centers')
    parser.add_argument('--concurrency', type=int, choices=(1, 2), default=2)
    parser.add_argument('--print-command', action='store_true')
    args = parser.parse_args()
    if not math.isfinite(args.damping) or args.damping <= 0 or args.maxiter < 1 or args.active_rows < 1:
        raise ValueError('Need an explicit positive common damping and positive inner/row counts')
    parent, prepare, plans = commands(args)
    if args.print_command:
        print(json.dumps(dict(preparation_command=prepare, commands=plans,
            actual_scientific_children_started=False), indent=2))
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise SystemExit('Scientific children run only in public GitHub Actions; --print-command is preparation only.')
    if parent.exists():
        raise FileExistsError('Use an independent new pair directory: ' + str(parent))
    inputs = [args.bundle.resolve(), args.carrier.resolve(), *(path.resolve() for path in args.manifest)]
    for path in inputs:
        if not path.is_file():
            raise FileNotFoundError(path)
    parent.mkdir(parents=True)
    common = dict(schema='public-actions-same-parent-Phi-margin-pair-v1',
        launcher_sha256=sha(__file__), original_launcher_sha256=sha(args.source_launcher),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        github_sha=os.environ.get('GITHUB_SHA'), github_repository=os.environ.get('GITHUB_REPOSITORY'),
        parent_bundle=str(args.bundle.resolve()), parent_bundle_sha256=sha(args.bundle),
        carrier=str(args.carrier.resolve()), carrier_sha256=sha(args.carrier),
        manifests=[dict(path=str(path.resolve()), sha256=sha(path)) for path in args.manifest],
        explicit_common_damping=args.damping, maxiter=args.maxiter, directions_per_child=1,
        concurrency=args.concurrency, BLAS_threads_per_child=1,
        preparation_command=prepare, differing_options=list(DIFFERING_FLAGS),
        common_eligibility_cutoff='.967', candidate_values_inherited_from_old_reports=False,
        compact_results_only_for_publication=True, raw_outputs_location=str(parent),
        final_reach_target_unchanged='.03 D with continuous all-t certification still required')
    for plan in plans:
        write_json(parent / (plan['name'] + '-plan.json'), dict(**common, **plan))
    write_json(parent / 'pair-plan.json', dict(**common, children=plans))
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    pending, running, finished = plans.copy(), {}, {}
    while pending or running:
        while pending and len(running) < args.concurrency:
            plan = pending.pop(0)
            log = parent / (plan['name'] + '.stdout.log')
            handle = log.open('w')
            started = time.monotonic()
            try:
                process = subprocess.Popen(plan['command'], cwd=args.repo.resolve(),
                    env=env, stdout=handle, stderr=subprocess.STDOUT)
            except OSError as error:
                handle.write(repr(error) + '\n')
                handle.close()
                finished[plan['name']] = summarize(plan, None, time.monotonic()-started, log)
                finished[plan['name']]['launch_error'] = repr(error)
                continue
            running[plan['name']] = (process, handle, plan, log, started)
            print(json.dumps(dict(event='margin_pair_child_started', name=plan['name'],
                process_id=process.pid, safety=plan['safety'], active_band=plan['active_band'])), flush=True)
        for name, (process, handle, plan, log, started) in list(running.items()):
            returncode = process.poll()
            if returncode is None:
                continue
            handle.close()
            finished[name] = summarize(plan, returncode, time.monotonic()-started, log)
            write_json(parent / (name + '-summary.json'), json_safe(finished[name]))
            del running[name]
            print(json.dumps(dict(event='margin_pair_child_returned', name=name,
                returncode=returncode, actual_directions=finished[name].get('actual_directions_computed'),
                accepted_directions=finished[name].get('accepted_directions'))), flush=True)
        if running:
            time.sleep(2.)
    summaries = [finished[plan['name']] for plan in plans]
    result = json_safe(dict(**common, children=summaries, comparison=compare(summaries)))
    write_json(parent / 'comparison-report.json', result)
    print(json.dumps(dict(event='margin_pair_complete', report=str(parent / 'comparison-report.json'),
        comparison=result['comparison'])), flush=True)
    if any(item.get('returncode') != 0 or not item.get('complete', False) for item in summaries):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
