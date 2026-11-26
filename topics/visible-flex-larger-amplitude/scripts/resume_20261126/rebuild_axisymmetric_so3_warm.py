#!/usr/bin/env python3
"""Reproduce only the genuine warm inputs for the direct R690/SO3 branch.

The one scientific command is the unchanged published reproduce_and_solve.py
WITHOUT --implementation. Its genuine five accepted-prefix continuations,
pulse/common-jet assembly and complete Hold/mode-damped warm generators remain
unchanged. This entry never starts the af89/e8/a04/continue optimization chain,
an old Gauss carrier, a geometry certificate or a new SO3 solve.

The status/record shape is compatible with the existing public controller.
--print-only is stdlib source/argv inspection and starts no scientific process.
Actual execution is restricted to this repository's public GitHub Actions.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time


REPOSITORY = 'Rogerhu12/math-research-public'
TOPIC = 'topics/visible-flex-larger-amplitude'
RECIPE_PATH = TOPIC + '/scripts/resume_20261126/rebuild_axisymmetric_so3_warm.py'
OLD_COMMIT = '60321451c058c6a51da58c37ae5ec6f2d1145f74'
OLD_PATH = TOPIC + '/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz'
OLD_SHA = 'b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff'
HISTORICAL_MODE_WARM_SHA = '79c161cc11a0743209ca3947e2b0f51f7ab7046e14ebfadf519f5d6e7259edba'

# These are the actual complete recovery sources and their imported project
# dependencies. They are read and hashed here, never imported by this recipe.
# The unused --implementation branch of reproduce_and_solve is not invoked.
SOURCES = {
    'reproduce': ('scripts/resume_20261120/reproduce_and_solve.py',
        '067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d'),
    'prefix_rebuild': ('scripts/resume_20261120/rebuild_fullclosed.py',
        '4e9ddeaeef2a0ab8b1b38b1412eb066b53578dd649d8f9b4d1a077c7256dee6b'),
    'warm_rebuild': ('scripts/resume_20261120/rebuild_closed_warm.py',
        '63950b72e75e8b6497ad2119ca16076c2c8749f9615166beb6d52adcab86708e'),
    'prefix_continue': ('scripts/parallel_20261117_continue.py',
        '8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae'),
    'prefix_qr': ('computations/geometry_20261114_separated_qr_bvp.py',
        'c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39'),
    'frenet': ('scripts/parallel_20261117_frenet_symbol.py',
        '7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831'),
    'profile': ('scripts/parallel_20261117_profile.py',
        '08b1894ca407a0c49b0de80427c669cafe702ab5878b1abf7b346994138d79b3'),
    'inward_profile': ('scripts/parallel_20261117_inward_profile.py',
        '1816ba9f5c9d1c207ba5e502ed5fa37a2f28807c54067cde766ae313df40e3e0'),
    'pulse_shared_jets': ('notes/2026-11-17-parallel-pulse-common-jet-field.py',
        '7525fe7713078ec09f1b2096f96c5df2920cb32c3fcfda80a0038a4f866bce4e'),
    'pulse_field': ('notes/2026-11-17-parallel-geometry-short-ivp-field.py',
        'ed0de0d513f28e1d227ba4f49a2ac2b2379107ca200c50f0d43f933e0edfd924'),
    'pulse_refine': ('notes/2026-11-17-parallel-geometry-short-ivp-refine.py',
        '13f363bef6133f30795842055d4bea6367748a1e954f29bafb42e1653b4e979c'),
    'pulse_probe': ('notes/2026-11-17-parallel-geometry-terminal-target-probe.py',
        'b6fea795cc807add91b7c78418b211982733ceb76f09f89e08f34c8a67b2b93d'),
    'pulse_schur_helpers': ('notes/2026-11-17-parallel-geometry-frenet-schur.py',
        '426635e625e3f80b2b7eea238df1a7f9ac9285fafa5f87a79fd0e2c3d645cd6b'),
    'pulse_profile': ('notes/2026-11-17-parallel-inward-curvature-pulse.py',
        '148dd6305df67c881ceb180249f4eaf34e3a996a6568c7378be467d41a92d157'),
    'assembly': ('scripts/parallel_20261117_pulse_arclength_readout.py',
        '31782ba06d5414a7851284ce330a89d208b8d56c4f1d99421a804e2a78271266'),
    'hold_oracle': ('notes/2026-11-17-parallel-model-full-hold-oracle.py',
        'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'),
    'integral_oracle': ('notes/2026-11-17-parallel-inward-integral-enclosure.py',
        'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'),
    'integer_trigonometry': ('notes/2026-11-17-parallel-geometry-inward-chord-cover.py',
        'e480a2ca7ebd5911768cad04ef7b98319ff2cff1840cf71531eaf2b574b4211a'),
    'hold_profile': ('scripts/parallel_20261117_negative_hold_profile_ivp.py',
        'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'),
    'hold_warm': ('notes/2026-11-17-parallel-model-fullclosed-hold-warm.py',
        'bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3'),
    'mode_warm': ('notes/2026-11-17-parallel-model-fullclosed-mode-damped-warm.py',
        '632d6cfc5f3113bc6f64c340fe9d066a1614c5b0bd649a357bdea2d0d94af6e8'),
}
PREFIX_NAMES = ('continue0991', 'continue0992', 'refine0992m112',
                'continue0993m112', 'continue0995m112')
WARM_NAMES = ('pulse_shared_jets', 'assemble_common_prefix',
              'fullclosed_hold_warm', 'fullclosed_mode_damped_warm')
REQUIRED_OUTPUTS = (
    'rebuild-prefix-manifest.json', 'rebuild-closed-warm-manifest.json',
    'data/accepted099.json.gz',
    *(f'data/{name}.json.gz' for name in PREFIX_NAMES),
    'data/inward-scalar-parameter-carrier.json.gz',
    'data/pulse-a5-fullfield-n4096-c2.json.gz',
    'data/pulse-a5-complete-base.json.gz',
    'data/fullclosed-hold-warm.json', 'data/fullclosed-hold-warm.npz',
    'data/fullclosed-mode-damped-warm.json', 'data/fullclosed-mode-damped-warm.npz',
)


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def checked_sources(repo):
    result = {}
    for role, (relative, expected) in SOURCES.items():
        path = repo / TOPIC / relative
        if not path.is_file():
            raise FileNotFoundError('Complete recovery source required: ' + str(path))
        actual = sha(path)
        if actual != expected:
            raise ValueError('Changed recovery source: ' + role + ' actual=' + actual)
        result[role] = dict(path=str(path), repository_path=TOPIC + '/' + relative,
                            sha256=actual)
    return result


def require_digest(path, expected):
    path = Path(path)
    if not path.is_file() or sha(path) != expected:
        raise ValueError('Current-run output or input identity changed: ' + str(path))


def make_plan(repo, work, status_path):
    sources = checked_sources(repo)
    full = work / 'fullclosed_solver'
    command = [sys.executable, '-u', sources['reproduce']['path'],
               '--repo', str(repo), '--work', str(full)]
    stage = dict(name='warm', argv=command, parent=None,
        bundle=str(full / 'data/fullclosed-mode-damped-warm.npz'),
        report=str(full / 'rebuild-closed-warm-manifest.json'),
        extra_outputs=[str(full / name) for name in REQUIRED_OUTPUTS
                       if name not in ('data/fullclosed-mode-damped-warm.npz',
                                       'rebuild-closed-warm-manifest.json')],
        action=None, parameters={}, historical_bundle_sha256=HISTORICAL_MODE_WARM_SHA,
        scope='Genuine accepted five-prefix, pulse and complete warm input reconstruction only; '
              'no registered optimization directions or scientific certificates are repeated.')
    return dict(schema='public-actions-direct-SO3-warm-command-chain-v1',
        repository=REPOSITORY, source_sha256=sha(__file__),
        repo=str(repo), work=str(work), status=str(status_path), stop_after='warm',
        sources=sources, stages=[stage],
        numerical_environment=dict(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1'),
        exact_delegation='published reproduce_and_solve.py --repo REPO --work WORK/fullclosed_solver',
        implementation_option_supplied=False,
        direct_consumer_inputs={
            'warm_bundle': str(full / 'data/fullclosed-hold-warm.npz'),
            'warm_report': str(full / 'data/fullclosed-hold-warm.json'),
            'scalar_input': str(full / 'data/pulse-a5-complete-base.json.gz')},
        old_optimization_directions_started=0,
        old_observation_carrier_required=False,
        new_SO3_field_or_solver_started=False,
        historical_names_are_labels_only=True, old_certificates_inherited=False)


def verify_actual_recovery(full, sources):
    """Verify producer journals and file hashes only; do not load any arrays."""
    prefix_path = full / 'rebuild-prefix-manifest.json'
    warm_path = full / 'rebuild-closed-warm-manifest.json'
    prefix = json.loads(prefix_path.read_text())
    warm = json.loads(warm_path.read_text())
    if (prefix.get('schema') != 'fullclosed-prefix-recovery-20261120-v1'
            or prefix.get('driver_sha256') != sources['prefix_rebuild']['sha256']
            or prefix.get('continue_source_sha256') != sources['prefix_continue']['sha256']
            or prefix.get('historical_blob') != dict(commit=OLD_COMMIT, path=OLD_PATH, sha256=OLD_SHA)
            or prefix.get('complete') is not True
            or [r.get('name') for r in prefix.get('stages', [])] != list(PREFIX_NAMES)):
        raise ValueError('The original complete five-prefix journal is not this actual recovery')
    files = {str((full / name).resolve()) for name in REQUIRED_OUTPUTS}
    previous = full / 'data/accepted099.json.gz'
    require_digest(previous, OLD_SHA)
    for record, name in zip(prefix['stages'], PREFIX_NAMES):
        if record.get('returncode') != 0 or record.get('success') is not True:
            raise ValueError('A genuine prefix stage did not accept: ' + name)
        require_digest(previous, record['input_sha256'])
        previous = full / 'data' / (name + '.json.gz')
        require_digest(previous, record['output_sha256'])
    last = prefix['stages'][-1]
    if (last.get('M') != 112 or last.get('N') != 2048 or last.get('endpoint') != .995
            or Path(prefix['final_prefix']).resolve() != previous.resolve()):
        raise ValueError('The warm chain did not use its actual accepted .995 M112/N2048 prefix')
    if (warm.get('schema') != 'fullclosed-warm-recovery-20261120-v1'
            or warm.get('driver_sha256') != sources['warm_rebuild']['sha256']
            or warm.get('complete') is not True
            or Path(warm['prefix']).resolve() != previous.resolve()
            or warm.get('prefix_sha256') != sha(previous)
            or [r.get('name') for r in warm.get('stages', [])] != list(WARM_NAMES)):
        raise ValueError('The original complete pulse/Hold warm journal does not match')
    roles = dict(zip(WARM_NAMES, ('pulse_shared_jets', 'assembly', 'hold_warm', 'mode_warm')))
    for record in warm['stages']:
        if (record.get('complete') is not True
                or record.get('source_sha256') != sources[roles[record['name']]]['sha256']):
            raise ValueError('Incomplete or changed actual warm producer: ' + record['name'])
        for name, expected in record['outputs'].items():
            path = Path(name).resolve()
            if full not in path.parents:
                raise ValueError('Producer journal output escaped the declared raw work directory')
            require_digest(path, expected)
            files.add(str(path))
    hold_report_path = full / 'data/fullclosed-hold-warm.json'
    hold_bundle = full / 'data/fullclosed-hold-warm.npz'
    mode_report_path = full / 'data/fullclosed-mode-damped-warm.json'
    mode_bundle = full / 'data/fullclosed-mode-damped-warm.npz'
    scalar = full / 'data/pulse-a5-complete-base.json.gz'
    hold = json.loads(hold_report_path.read_text())
    mode = json.loads(mode_report_path.read_text())
    if (hold.get('schema') != 'fullclosed-hold-real-pulse-warm-v1'
            or hold.get('source_sha256') != sources['hold_warm']['sha256']
            or hold.get('input_sha256') != sha(scalar)
            or hold.get('J') != 923 or hold.get('M') != 160 or hold.get('cells') != 922):
        raise ValueError('Incorrect actual Hold warm source, scalar or full mesh')
    require_digest(hold_bundle, hold['bundle_sha256'])
    if (mode.get('schema') != 'fullclosed-hold-single-mode-damped-warm-v1'
            or mode.get('source_sha256') != sources['mode_warm']['sha256']
            or mode.get('parent_bundle_sha256') != sha(hold_bundle)
            or mode.get('parent_report_sha256') != sha(hold_report_path)
            or mode.get('raw_pulse_sha256') != sha(scalar)
            or mode.get('scalar_source_sha256') != sources['hold_oracle']['sha256']
            or mode.get('J') != 923 or mode.get('M') != 160
            or mode.get('prefix_819_triples_bitwise_identical') is not True
            or mode.get('core_and_first3_unchanged') is not True
            or Path(warm['final_bundle']).resolve() != mode_bundle.resolve()):
        raise ValueError('Incorrect actual mode-warm source, parents or unchanged core contract')
    require_digest(mode_bundle, mode['bundle_sha256'])
    outputs = []
    for name in sorted(files):
        path = Path(name)
        if not path.is_file():
            raise FileNotFoundError('Missing complete warm output: ' + name)
        outputs.append(dict(path=name, sha256=sha(path), bytes=path.stat().st_size))
    metrics = dict(prefix_stages=5, accepted_prefix_sha256=sha(previous),
        historical_accepted099_sha256=OLD_SHA, prefix_M=112, prefix_N=2048,
        prefix_endpoint=last['endpoint'], warm_stages=4,
        hold_bundle_sha256=sha(hold_bundle), hold_report_sha256=sha(hold_report_path),
        scalar_input_sha256=sha(scalar), mode_bundle_sha256=sha(mode_bundle),
        M=160, J=923, cells=922, mode_prefix_819_unchanged=True,
        mode_core_and_first3_unchanged=True, old_optimization_directions_started=0,
        direct_SO3_preparation_executed=False, continuous_certificates_inherited=False,
        topic_completion_claimed=False)
    return outputs, metrics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--status', type=Path)
    parser.add_argument('--stop-after', choices=('warm',), default='warm')
    parser.add_argument('--print-only', action='store_true')
    args = parser.parse_args()
    repo, work = args.repo.resolve(), args.work.resolve()
    status_path = args.status or Path('status.json')
    status_path = (status_path if status_path.is_absolute() else work / status_path).resolve()
    if work == repo or repo in work.parents:
        raise ValueError('All raw work must remain outside the Git repository')
    if work not in status_path.parents:
        raise ValueError('The status file must be inside this exact raw work directory')
    plan = make_plan(repo, work, status_path)
    stage = plan['stages'][0]
    if args.print_only:
        print(json.dumps(dict(stage='warm', scope=stage['scope'],
            command=shlex.join(stage['argv']), bundle=stage['bundle'], report=stage['report'],
            direct_consumer_inputs=plan['direct_consumer_inputs'], status=str(status_path),
            pinned_sources=len(plan['sources']), stop_after='warm')), flush=True)
        print(json.dumps(dict(event='plan_only_complete', stages=1,
            source_sha256=plan['source_sha256'], scientific_subprocesses_started=0)), flush=True)
        return
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY', '').lower() != REPOSITORY.lower()):
        raise RuntimeError('Scientific recovery is restricted to this public repository Actions; use --print-only locally')
    if Path(__file__).resolve() != (repo / RECIPE_PATH).resolve():
        raise ValueError('Execute the complete published recipe from the declared source checkout')
    source_commit = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    published_files = [(RECIPE_PATH, plan['source_sha256'])]
    published_files += [(s['repository_path'], s['sha256']) for s in plan['sources'].values()]
    for relative, expected in published_files:
        raw = subprocess.check_output(['git', '-C', str(repo), 'show', 'HEAD:' + relative])
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError('Executed source differs from the declared published commit: ' + relative)
    subprocess.run(['git', '-C', str(repo), 'cat-file', '-e', OLD_COMMIT + ':' + OLD_PATH], check=True)
    work.mkdir(parents=True, exist_ok=True)
    full = work / 'fullclosed_solver'
    identity = dict(source_sha256=plan['source_sha256'], stop_after='warm',
        sources_sha256={k: v['sha256'] for k, v in plan['sources'].items()},
        work=str(work), status=str(status_path), historical_input_sha256=OLD_SHA)
    if status_path.exists():
        status = json.loads(status_path.read_text())
        if (status.get('schema') != 'public-actions-direct-SO3-warm-status-v1'
                or status.get('identity') != identity):
            raise ValueError('Cannot reuse a work directory under different warm source/input identities')
        warm_records = [r for r in status.get('completed', []) if r.get('name') == 'warm']
        if len(warm_records) > 1 or (status.get('completed') and status['completed'][0].get('name') != 'warm'):
            raise ValueError('The warm journal must contain at most one initial actual warm record')
    else:
        if any((full / name).exists() for name in REQUIRED_OUTPUTS):
            raise FileExistsError('Unjournaled warm products require inspection; they are not adopted as this run')
        status = dict(schema='public-actions-direct-SO3-warm-status-v1', identity=identity,
            stage='initializing', state='running', completed=[],
            run_url='https://github.com/' + REPOSITORY + '/actions/runs/' + os.environ.get('GITHUB_RUN_ID', ''),
            scientific_scope=stage['scope'])
    plan['source_commit'] = source_commit
    write_json(work / 'recipe-manifest.json', plan)
    logs = work / 'recipe-logs'
    logs.mkdir(exist_ok=True)
    log_path = logs / 'warm.log'
    record = None
    try:
        if status['completed']:
            old = status['completed'][0]
            for item in old['outputs']:
                require_digest(item['path'], item['sha256'])
            verify_actual_recovery(full, plan['sources'])
            status.update(stage='warm', state='completed', recipe_finished=True, updated_utc=utc())
            write_json(status_path, status)
            print(json.dumps(dict(stage='warm', state='completed', reused_same_run=True,
                output_bundle_sha256=old['output_bundle_sha256'])), flush=True)
        else:
            status.update(stage='warm', state='running', current_command=stage['argv'],
                current_scope=stage['scope'], parent_sha256=None, updated_utc=utc())
            status.pop('failed', None)
            status.pop('error', None)
            write_json(status_path, status)
            print(json.dumps(dict(stage='warm', state='running', command=stage['argv'])), flush=True)
            env = os.environ.copy()
            env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
            started = time.monotonic()
            with log_path.open('w') as log:
                returned = subprocess.run(stage['argv'], cwd=repo, env=env,
                    stdout=log, stderr=subprocess.STDOUT)
            elapsed = time.monotonic() - started
            record = dict(name='warm', state='completed' if returned.returncode == 0 else 'failed',
                returncode=returned.returncode, seconds=elapsed, scope=stage['scope'],
                parent=None, parent_sha256=None, source_commit=source_commit,
                source_sha256=plan['sources']['reproduce']['sha256'], command=stage['argv'],
                output_bundle=stage['bundle'], report=stage['report'],
                output_report=stage['report'], log=str(log_path), outputs=[],
                input_files=[dict(role='recipe', path=RECIPE_PATH, commit=source_commit,
                                  sha256=plan['source_sha256'])] +
                    [dict(role=role, path=value['repository_path'], commit=source_commit,
                          sha256=value['sha256']) for role, value in plan['sources'].items()] +
                    [dict(role='genuine_accepted099_blob', path=OLD_PATH,
                          commit=OLD_COMMIT, sha256=OLD_SHA)])
            if returned.returncode:
                raise RuntimeError('Original complete warm recovery failed; see ' + str(log_path))
            outputs, metrics = verify_actual_recovery(full, plan['sources'])
            if checked_sources(repo) != plan['sources'] or sha(__file__) != plan['source_sha256']:
                raise ValueError('A recovery source changed during the actual stage')
            record.update(outputs=outputs, metrics=metrics,
                output_bundle_sha256=sha(stage['bundle']), report_sha256=sha(stage['report']),
                historical_bundle_sha256=HISTORICAL_MODE_WARM_SHA,
                historical_bytes_match=sha(stage['bundle']) == HISTORICAL_MODE_WARM_SHA)
            status['completed'].append(record)
            status.update(stage='warm', state='completed', recipe_finished=True, updated_utc=utc())
            write_json(status_path, status)
            print(json.dumps({k: v for k, v in record.items() if k not in ('outputs', 'input_files', 'log')},
                             allow_nan=False), flush=True)
        print(json.dumps(dict(event='recipe_finished', stage='warm', status=str(status_path),
            historical_names_are_labels_only=True, inherited_scientific_certificates=False,
            old_optimization_directions_started=0, direct_SO3_preparation_executed=False)), flush=True)
    except BaseException as error:
        status.update(stage='warm', state='failed', error=repr(error), updated_utc=utc())
        if record is None:
            record = dict(name='warm', log=str(log_path), scope=stage['scope'])
        status['failed'] = dict(record, state='failed', setup_error=repr(error))
        write_json(status_path, status)
        raise


if __name__ == '__main__':
    main()
