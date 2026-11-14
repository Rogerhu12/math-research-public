#!/usr/bin/env python3
"""Practical same-g continuous backend for an actual successful prefix/tail.

Plan the existing mathematical producers, run an explicitly selected stage, or
summarize an actual whole-map certificate at the original 2e-9 target. Prefix
and tail Fourier orders are separate. No frozen-launch, observer, independent
replay or old 80 MB comparison package is a prerequisite. Plans are not bounds.
"""
import argparse
import copy
from datetime import datetime, timezone
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC/'notes'
REPO = TOPIC.parents[1]
PYTHON = '/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python'
OLD_TOPIC = '/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface'
SOURCE_ROOT = TOPIC/'repro/source-root'
TARGET = Q(1, 500_000_000)
L12 = Q(370012576184137, 18889465931478580854784)
PROFILE = NOTES/'2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14-frozen-profile.json'
CHART = NOTES/'2026-11-09-950f-prefix-adaptive-chart.json'
PORT = NOTES/'2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'
TEMPLATES = {
    'storage': NOTES/'2026-11-10-78718-numerical-m14-restart8000-02-storage-production-plan-01.json',
    'single': NOTES/'2026-11-10-78718-numerical-m14-restart8000-02-production-plan-01.json',
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def identity(path):
    path = Path(path).resolve()
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            digest.update(chunk)
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': digest.hexdigest()}


def write(path, value):
    raw = (json.dumps(value, indent=2, allow_nan=False)+'\n').encode()
    require(len(raw) < 1_000_000, 'Unexpectedly large metadata output')
    with Path(path).open('xb') as stream:
        stream.write(raw)


def finite(value, lower=0, upper=math.inf):
    return (type(value) in (int, float) and math.isfinite(value)
            and lower <= value <= upper)


def resolve(name, parent):
    p = Path(name)
    choices = (p, Path(parent)/p, Path(parent)/p.name, NOTES/p.name)
    for candidate in choices:
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(name)


def finite_candidate(path):
    """Read actual finite math results; do not reload PP arrays or rerun a solver."""
    path = Path(path).resolve()
    cp = read(path)
    require(cp.get('solver_success') is True, 'Checkpoint is not an actual successful prefix solve')
    cfg = cp['config']
    M = cfg['modes']
    require(type(M) is int and M > 0 and cfg.get('actual_nonlinear_tail') is True
            and cfg.get('fixed_metric') is True and cfg['tol'] == 2e-9
            and cfg['bc_tol'] == 1e-8 and cfg['physical_bc_tol'] == 2e-11,
            'Different finite equation/tolerance policy')
    require(finite(cp['max_rms_collocation_residual'], upper=2e-9)
            and finite(cp['summary']['physical_bc_max'], upper=2e-11),
            'Actual original physical residuals do not pass')
    outer = cp['actual_outer_checks']
    require(outer and outer[-1]['inner_success'] is True
            and finite(outer[-1]['actual_boundary_residual'], upper=1e-8)
            and finite(outer[-1]['actual_tail_residual'])
            and outer[-1]['actual_tail_residual'] < 2e-9,
            'Actual nonlinear outer boundary condition does not pass')
    port = read(PORT)
    require(cp['frozen_profile'] == read(PROFILE) and cp['chart'] == read(CHART)
            and cp['gauge_amplitude'] == .1 and cp['warp_reference_q'] == .1
            and cp['physical_tail_parameters'] == port['parameters']
            and cp['physical_tail_cut'] == port['cut'], 'Different fixed physical geometry')
    tail_path = resolve(cp['tail_seam']['tail_record'], path.parent)
    stem = path.name[:-8] if path.name.endswith('.json.gz') else path.stem
    require(tail_path.parent == path.parent
            and tail_path.name == stem+f"_tail_{cp['tail_calls']:04d}.json.gz",
            'Checkpoint does not identify its own final actual tail')
    packet = read(tail_path)
    response, request = packet['response'], packet['request']
    parameters = response['checkpoint']['parameters']
    W = parameters['modes']
    require(type(W) is int and W >= M, 'Tail order must cover the prefix boundary modes')
    require(response.get('converged') is True and finite(response['residual'])
            and response['residual'] < 2e-9 and request['jacobian'] is True
            and request['audit'] is True and response['audit'] is not None,
            'Own final true DN lacks the original residual, derivative or audit')
    require(len(request['height']) == W
            and request['height'] == response['checkpoint']['cutHeight']
            and len(response['heightJetJacobian']) == (3*W+2)*W,
            'Own tail target or complete Jacobian has inconsistent dimensions')
    for key, value in port['parameters'].items():
        require(packet['config'].get(key) == value,
                'Tail changes fixed physical parameter: '+key)
    # Mixed M/W routes may save the explicitly projected response in tail_jets;
    # the producer always receives this complete original W packet.
    saved = cp['tail_seam'].get('full_tail_jets', cp['tail_seam']['tail_jets'])
    for key, value in saved.items():
        actual = response['jets'][key]
        if isinstance(value, list):
            require(len(value) in (M, W) and value == actual[:len(value)],
                    'Saved prefix seam is not the declared projection of its own tail')
        else:
            require(value == actual, 'Saved seam scalar differs from its own tail')
    return cp, packet, {
        'checkpoint': identity(path), 'own_final_tail': identity(tail_path),
        'prefix_modes': M, 'tail_modes': W,
        'prefix_angular': cfg['angular'], 'tail_angular': parameters['quadrature'],
        'physical_rms': cp['max_rms_collocation_residual'],
        'physical_bc': cp['summary']['physical_bc_max'],
        'actual_tail_residual': response['residual'],
        'finite_success_only': True, 'closed_surface_success': False,
    }


def flag(argv, name, value):
    argv[argv.index(name)+1] = str(value)


def plan(args):
    cp, packet, candidate = finite_candidate(args.checkpoint)
    source = TEMPLATES[args.container]
    old = read(source)
    run = args.run_directory.resolve()
    require(not run.exists() or (run.is_dir() and not any(run.iterdir())),
            'Choose an unused production directory')
    require(run.parent.is_dir(), 'Production parent does not exist')
    substitutions = [
        (old['production_directory'], str(run)),
        (old['own_successful_checkpoint']['path'], candidate['checkpoint']['path']),
        (old['own_final_audited_tail']['path'], candidate['own_final_tail']['path']),
        (OLD_TOPIC, str(TOPIC)),
    ]
    def move(value):
        if isinstance(value, str):
            for before, after in substitutions:
                value = value.replace(before, after)
            return value
        if isinstance(value, list):
            return [move(v) for v in value]
        if isinstance(value, dict):
            return {k: move(v) for k, v in value.items()}
        return value
    commands = []
    M, W = candidate['prefix_modes'], candidate['tail_modes']
    base_modes = max(M, 24) if args.cartesian_modes is None else args.cartesian_modes
    require(base_modes >= M, 'Cartesian prefix representation cannot drop prefix modes')
    tail_angular = max(512, candidate['tail_angular'])
    for original in old['commands']:
        item = move({k: original[k] for k in
                     ('id', 'argv', 'cwd', 'depends_on', 'condition', 'expected_output_paths')})
        if item['id'].startswith('terminal-'):
            route = item['id'][len('terminal-'):]
            item.update(id='summary-'+route,
                argv=[PYTHON, str(Path(__file__).resolve()), 'summarize',
                      '--checkpoint', candidate['checkpoint']['path'],
                      '--whole', str(run/('whole-'+route+'.json')),
                      '--out', str(run/('summary-'+route+'.json'))],
                expected_output_paths=[str(run/('summary-'+route+'.json'))])
        item['depends_on'] = [d.replace('terminal-', 'summary-') for d in item['depends_on']]
        if item['id'] == 'prefix-base':
            flag(item['argv'], '--modes', base_modes)
            flag(item['argv'], '--angular', max(768, candidate['prefix_angular']))
        if item['id'] == 'tail-export':
            flag(item['argv'], '--angular-nodes', tail_angular)
        item['cwd'] = str(REPO)
        commands.append(item)
    commands.insert(6, {
        'id': 'prefix-inlet-lower',
        'argv': [PYTHON, str(HERE/'78718-prefix-inlet-angular-lower-v1.py'),
                 '--geometry', str(run/'prefix-base.json'), '--target', str(run/'prefix-target.json'),
                 '--out', str(run/'prefix-inlet-lower.json')],
        'cwd': str(REPO), 'depends_on': ['prefix-target'],
        'condition': 'Optional early necessary-condition diagnostic; a lower bound above 2e-9 rejects this retained-prefix graph.',
        'expected_output_paths': [str(run/'prefix-inlet-lower.json')],
    })
    ids = {c['id'] for c in commands}
    require(len(ids) == len(commands) and all(set(c['depends_on']) <= ids for c in commands),
            'Invalid producer dependency graph')
    required_sources = sorted({a for c in commands for a in c['argv']
                               if a.startswith(str(HERE)+'/') and Path(a).is_file()})
    # Only source files actually named in these commands; no recursive archival
    # inventory and no old large M12 candidate dependency.
    roles = move(old['fixed_input_roles'])
    used_roles = {k: v for k, v in roles.items() if any(v in c['argv'] for c in commands)}
    missing = sorted(v for v in used_roles.values() if not Path(v).is_file())
    optional_mesh_checks = [move(c) for c in old.get('manifest_or_independent_input_templates', [])
                            if '-PL-' in c['id']]
    result = {
        'scope': __doc__, 'status': 'ACTUAL_FINITE_INPUTS_PLANNED_NO_PRODUCTION',
        'script': identity(__file__), 'argv': sys.argv[:],
        'candidate': candidate, 'production_directory': str(run),
        'container': args.container,
        'container_note': 'Lossless logical NPZ byte shards; no geometry or float change.'
                          if args.container == 'storage' else 'Original physical single container; file cap applies.',
        'command_template': identity(source), 'fixed_input_roles': used_roles,
        'missing_named_fixed_inputs': missing,
        'environment': move(old['environment']), 'commands': commands,
        'command_sources': [identity(p) for p in required_sources],
        'optional_mesh_checks': optional_mesh_checks,
        'branch_policy': {
            'prefix': 'Use complete baseline if its exact-target bound passes; otherwise diagnose and use complete angular refinement.',
            'tail': 'Use full alone if sufficient; metric-only needs its complete coverage and identical background.',
            'stop': 'A valid strict point lower above the target rejects that graph; do not repeat whole-domain work on it.',
        },
        'mathematical_target': str(TARGET),
        'accepted_comparison': {'M12_point_lower_exact': str(L12),
            'reference': 'notes/2026-11-09-db6f-root-tail-m12-point-lower-proof.md; R21/R25',
            'M14_strict_lower_reference': 'R81; R83',
            'old_reference_arrays_required': False},
        'prefix_and_tail_orders_may_differ': True,
        'old_launch_or_observer_required': False,
        'mandatory_independent_replay': False,
        'actual_production_calls': 0, 'README_complete': False,
    }
    write(args.out, result)
    print(json.dumps({'status': result['status'], 'report': identity(args.out),
        'prefix_modes': M, 'tail_modes': W, 'commands': len(commands),
        'missing_named_fixed_inputs': len(missing), 'actual_production_calls': 0}), flush=True)
    return 0


def stamp():
    return datetime.now(timezone.utc).isoformat()


def run_stage(args):
    package = read(args.plan)
    selected = [c for c in package['commands'] if c['id'] == args.stage]
    require(len(selected) == 1, 'Unknown or ambiguous stage')
    stage = selected[0]
    run = Path(package['production_directory'])
    run.mkdir(exist_ok=True)
    observation = run/(args.stage+'-run.json')
    log = run/(args.stage+'-run.log')
    require(not observation.exists() and not log.exists(), 'Stage has already been attempted')
    for path in stage['expected_output_paths']:
        require(not Path(path).exists(), 'Stage output already exists: '+path)
    by_id = {c['id']: c for c in package['commands']}
    for name in stage['depends_on']:
        for path in by_id[name]['expected_output_paths']:
            require(Path(path).is_file(), 'Missing mathematical stage input: '+path)
    before = {str(p): (p.stat().st_size, p.stat().st_mtime_ns)
              for p in run.rglob('*') if p.is_file()}
    environment = dict(os.environ, **package['environment'])
    def limits():
        resource.setrlimit(resource.RLIMIT_FSIZE, (4_999_999, 4_999_999))
    start, when = time.monotonic(), stamp()
    print(json.dumps({'event': 'starting_producer', 'stage': args.stage,
                      'log': str(log), 'condition': stage['condition']}), flush=True)
    with log.open('xb') as stream:
        child = subprocess.run(stage['argv'], cwd=stage['cwd'], env=environment,
                               stdout=stream, stderr=subprocess.STDOUT, preexec_fn=limits)
    files = []
    for p in run.rglob('*'):
        if p.is_file() and before.get(str(p)) != (p.stat().st_size, p.stat().st_mtime_ns):
            files.append(identity(p))
    missing = [p for p in stage['expected_output_paths'] if not Path(p).is_file()]
    require(all(f['bytes'] < 5_000_000 for f in files), 'Producer exceeded physical file limit')
    record = {
        'stage': args.stage, 'argv': stage['argv'], 'cwd': stage['cwd'],
        'environment_overrides': package['environment'], 'plan': identity(args.plan),
        'started_utc': when, 'completed_utc': stamp(), 'seconds': time.monotonic()-start,
        'actual_subprocess_returncode': child.returncode,
        'expected_outputs_missing': missing, 'changed_or_new_files': files,
        'scope': 'Actual subprocess outcome, not a separate whole-surface success claim.',
    }
    write(observation, record)
    print(json.dumps({'event': 'producer_completed', 'stage': args.stage,
        'actual_exit_code': child.returncode, 'expected_outputs_missing': len(missing),
        'report': identity(observation)}), flush=True)
    if child.returncode == 0 and missing:
        return 2
    return child.returncode if child.returncode >= 0 else 128-child.returncode


def rational_record(value):
    value = Q(value)
    mid = float(value)
    lo = math.nextafter(mid, -math.inf) if Q(mid) > value else mid
    hi = math.nextafter(mid, math.inf) if Q(mid) < value else mid
    return {'exact': str(value), 'binary64_lower': lo, 'binary64_upper': hi}


def summarize(args):
    cp, packet, candidate = finite_candidate(args.checkpoint)
    whole = read(args.whole)
    budget_path = resolve(whole['closed_budget'], args.whole.parent)
    require(identity(budget_path)['sha256'] == whole['closed_budget_sha256'],
            'Whole bound has changed closed-budget input')
    budget = read(budget_path)
    map_row = budget['inputs']['geometry']
    map_path = resolve(map_row['file'], budget_path.parent)
    require(identity(map_path)['sha256'] == map_row['sha256'] == whole['geometry_sha256'],
            'Whole bound is not for this common map')
    geometry = read(map_path)
    require(geometry['checkpoint_sha256'] == candidate['checkpoint']['sha256']
            and geometry['frozen_profile'] == cp['frozen_profile']
            and geometry['chart'] == cp['chart'] and geometry['warp_reference_q'] == .1,
            'Whole map changed the actual prefix or fixed physical target')
    require(geometry['mirror_inlet_C2_exact'] is True
            and geometry['exact_common_cut_C2_by_definition'] is True,
            'The actual mirror/common-cut C2 assembly is not present')
    manifest_path = resolve(geometry['tail_manifest'], map_path.parent)
    manifest = read(manifest_path)
    require(identity(manifest_path)['sha256'] == geometry['tail_manifest_sha256']
            == whole['tail_manifest_sha256']
            and manifest['inputSHA256'] == candidate['own_final_tail']['sha256']
            and manifest['finished'] is True,
            'Whole map is not made from this own completed tail')
    metric = Q(whole['whole_metric_operator_upper']['exact'])
    prefix = Q(whole['prefix_metric_upper']['exact'])
    tail = Q(whole['tail_metric_upper']['exact'])
    diameter = Q(whole['diameter_upper']['exact'])
    curvature = Q(whole['whole_principal_curvature_upper']['exact'])
    support = Q(whole['whole_support_lower']['exact'])
    reach = Q(whole['whole_reach_lower_by_R10']['exact'])
    reach_ratio = Q(whole['whole_reach_over_diameter_lower']['exact'])
    held = Q(whole['held_region_diameter_over_diameter_lower']['exact'])
    displacement = Q(whole['hold_over_diameter_lower']['exact'])
    require(metric == max(prefix, tail, Q(0)) and diameter > 0 and curvature > 0
            and support > 0 and reach == min(support, 1/curvature)
            and reach_ratio == reach/diameter, 'Inconsistent exact whole-map scalars')
    nontrivial = (Q(budget['unmarked_volume_moment_real_lower']['exact']) > 0
                 and Q(budget['centered_third_tensor_norm_squared_change_lower']['exact']) > 0)
    all_time = whole['all_phases_by_R17_rotation_and_material_action'] is True
    geometry_pass = (all_time and nontrivial and reach_ratio >= Q(3,100)
                     and held >= Q(1,5) and displacement >= Q(1,20))
    passed = geometry_pass and 0 <= metric <= TARGET
    decrease = L12 > Q(195883, 20000)*metric  # exact 9.79415
    result = {
        'status': 'ACTUAL_CONTINUOUS_BOUNDS_AT_ORIGINAL_TOLERANCE' if passed
                  else 'ACTUAL_WHOLE_BOUNDS_DO_NOT_PAY_ORIGINAL_TARGET',
        'script': identity(__file__), 'argv': sys.argv[:],
        'candidate': candidate, 'whole_certificate': identity(args.whole),
        'closed_budget': identity(budget_path), 'common_map': identity(map_path),
        'tail_manifest': identity(manifest_path), 'original_metric_target_exact': str(TARGET),
        'whole_metric_upper': rational_record(metric),
        'whole_reach_over_diameter_lower': rational_record(reach_ratio),
        'held_region_diameter_ratio_lower': rational_record(held),
        'held_displacement_ratio_lower': rational_record(displacement),
        'strict_Euclidean_noncongruence_including_reflections': nontrivial,
        'all_phases_by_R17_rotation_and_material_action': all_time,
        'continuous_geometry_thresholds_pass': geometry_pass,
        'original_2e_minus_9_metric_target_pass': 0 <= metric <= TARGET,
        'accepted_M12_lower_exact': str(L12),
        'strict_M12_error_greater_than_9_79415_times_this_upper': decrease,
        'comparison_reference': 'Existing complete M12 point-lower proof; R21/R25. R81 is an additional same-g refinement comparison.',
        'mesh_delivery_and_remaining_README_reasoning_are_separate': True,
        'README_complete': False,
    }
    write(args.out, result)
    print(json.dumps({'status': result['status'], 'report': identity(args.out),
                      'whole_metric_upper': result['whole_metric_upper'],
                      'geometry_pass': geometry_pass, 'strict_comparison': decrease}), flush=True)
    return 0 if passed else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('plan')
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--run-directory', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--container', choices=('storage', 'single'), default='storage')
    p.add_argument('--cartesian-modes', type=int)
    p.set_defaults(function=plan)
    p = sub.add_parser('run-stage')
    p.add_argument('--plan', type=Path, required=True)
    p.add_argument('--stage', required=True)
    p.set_defaults(function=run_stage)
    p = sub.add_parser('summarize')
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--whole', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.set_defaults(function=summarize)
    args = parser.parse_args()
    try:
        return args.function(args)
    except Exception as error:
        print(json.dumps({'status': 'NOT_COMPLETED', 'error': repr(error),
                          'command': args.command}), flush=True)
        return 2


if __name__ == '__main__':
    sys.exit(main())
