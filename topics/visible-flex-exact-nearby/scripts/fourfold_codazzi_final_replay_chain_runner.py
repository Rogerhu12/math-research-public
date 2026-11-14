#!/usr/bin/env python3
"""Restore the exact six-stage final centre in an isolated runner directory.

No numerical equation or tolerance is changed.  The first two stages stop
only after the unchanged producer prints a complete accepted checkpoint;
all nodal values AND derivatives then enter the original Hermite spline.
An identity failure preserves the new data and stops: it never relabels a
different centre as ac1.  Only small evidence is copied to --out-dir.
"""
from __future__ import annotations
import argparse
import ast
import datetime
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

KIND = 'actual_original_six_stage_final_centre_runner_v1'
FINAL = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
MANIFEST = 'notes/2026-11-13-R133-final-moving-replay-chain.json'
EARLY_MANIFEST = 'notes/2026-11-13-R133-moving-m32-alpha075-accepted000-reconstruction.json'
FINAL_MANIFEST = 'notes/2026-11-13-R133-moving-m32-alpha0765-fullR-v2-tol2e9-reconstruction.json'
EARLY_NAMES = {
    1: 'reciprocal-m256-alpha075-accepted000-candidate.json',
    2: 'moving-m32-alpha075-accepted000-candidate.json',
}
HELPERS = (
    'fourfold_codazzi_final_replay_first_accept.py',
    'fourfold_codazzi_final_replay_stage.py',
    'fourfold_codazzi_preserve_accepted_checkpoint_v2.py',
    'fourfold_codazzi_replay_historical_identity.py',
    'fourfold_codazzi_candidate_shards.py',
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.partial')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def public_copy(path, target):
    """Only small JSON evidence; regenerable arrays stay in runner scratch."""
    path, target = Path(path), Path(target)
    if not path.exists():
        return
    if path.stat().st_size > 1_000_000:
        raise ValueError('an unexpected large intermediate must not enter the result directory')
    if target.exists() and sha(target) != sha(path):
        raise FileExistsError('preserve the earlier distinct evidence: ' + str(target))
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        shutil.copyfile(path, target)


def checked_candidate(path, expected):
    from fourfold_codazzi_candidate_shards import load_candidate
    path = Path(path)
    if sha(path) != expected:
        raise ValueError('new candidate identity differs; no old certificate is transferred: ' + str(path))
    # The loader verifies every compressed byte, exact shared node, shape,
    # finite coefficient and the complete original interval cover.
    arrays = load_candidate(path)
    doc = read(path)
    return dict(path=str(path.resolve()), sha256=expected,
                radial_nodes=len(arrays['radial_nodes']),
                complete_coefficient_shape=list(arrays['piece_coefficients'].shape),
                all_parts=doc['parts'], every_part_verified=True)


def run(command, topic):
    print(json.dumps(dict(actual_command=command)), flush=True)
    result = subprocess.run(command, cwd=topic, env=os.environ.copy())
    if result.returncode:
        raise RuntimeError('actual child command returned ' + str(result.returncode))


def first_complete_checkpoint(attempt, specification):
    process = read(attempt / 'process.json')
    if (not process.get('complete') or not process.get('first_complete_accept_observed')
            or process.get('status') != 'first_complete_accept_then_intentional_stop'
            or process.get('producer_sha256') != specification['producer_sha256']):
        raise ValueError('no observed complete original accepted checkpoint')
    row = ast.literal_eval(process['complete_accept_log_line'])['accepted_complete_checkpoint']
    checkpoint = Path(row['path'])
    expected = specification['historical_accepted_checkpoint_sha256']
    if sha(checkpoint) != row['sha256'] or sha(checkpoint) != expected:
        raise ValueError('accepted scientific bytes differ from the actual historical checkpoint')
    if checkpoint.stat().st_size != row['bytes']:
        raise ValueError('accepted checkpoint byte count changed')
    return checkpoint, process


def preserve_first(topic, attempt, number, specification):
    checkpoint, process = first_complete_checkpoint(attempt, specification)
    candidate = attempt / EARLY_NAMES[number]
    report = attempt / 'Hermite-preservation.json'
    if not candidate.exists():
        command = [sys.executable, str(topic / 'scripts' / HELPERS[2]),
                   '--checkpoint', str(checkpoint),
                   '--original-process', str(attempt / 'process.json'),
                   '--original-log', str(attempt / 'stdout.log'),
                   '--candidate', str(candidate), '--out', str(report),
                   # This legacy field is explicitly a sentinel, not a
                   # claimed local tool-session number or historical exit.
                   '--observed-session', '0',
                   '--observed-exit-message',
                   'Runner invocation; legacy session 0 is a sentinel. The producer printed the complete accepted SHA and this attempt intentionally stopped it.']
        if process.get('actual_returncode') is not None:
            command += ['--observed-exit-code', str(process['actual_returncode'])]
        run(command, topic)
    else:
        preservation = read(report)
        if (preservation.get('checkpoint_sha256') != sha(checkpoint)
                or not preservation.get('every_saved_state_and_derivative_used')
                or preservation.get('candidate_sha256') != sha(candidate)):
            raise ValueError('incomplete or changed full Hermite preservation')
    return candidate


def restore_historical(topic, candidate, manifest, destination):
    if not destination.exists():
        run([sys.executable, str(topic / 'scripts' / HELPERS[3]),
             '--topic', str(topic), '--candidate', str(candidate),
             '--manifest', str(topic / manifest), '--out-dir', str(destination)], topic)
    report = read(destination / 'identity-report.json')
    if (not report.get('complete')
            or report.get('candidate_sha256') != sha(candidate)
            or report.get('manifest_sha256') != sha(topic / manifest)
            or not report.get('original_scientific_arrays_and_container_recovered')):
        raise ValueError('full scientific/container identity failed; keep the distinct new centre')
    return Path(report['restored_candidate'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--work', type=Path, required=True,
                        help='isolated regenerable storage, normally under RUNNER_TEMP')
    parser.add_argument('--out-dir', type=Path, required=True,
                        help='small actual process/identity evidence only')
    parser.add_argument('--candidate-path-file', type=Path, required=True)
    parser.add_argument('--address-space-mib', type=int, default=6144)
    parser.add_argument('--validate-existing', action='store_true',
                        help='check an already completed six-step chain without launching producers')
    args = parser.parse_args()
    topic, work, output = args.topic.resolve(), args.work.resolve(), args.out_dir.resolve()
    if topic == work or topic in work.parents:
        raise ValueError('large replay work must be outside the Git topic tree')
    if work == output or work in output.parents:
        raise ValueError('small published evidence must be outside regenerable work')
    work.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    manifest = read(topic / MANIFEST)
    original_runtime = manifest['runtime_original']
    runtime = dict(python=platform.python_version())
    for key, package in (('numpy','numpy'),('scipy','scipy'),
                         ('python_flint','python-flint'),('sympy','sympy')):
        runtime[key] = importlib.metadata.version(package)
    runtime.update({name:os.environ[name] for name in
                    ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','PYTHONDONTWRITEBYTECODE')})
    summary = dict(kind=KIND, complete=False, executed=True,
                   validate_existing_only=args.validate_existing,
                   producer_sha256=sha(__file__), manifest_sha256=sha(topic / MANIFEST),
                   original_runtime=original_runtime, actual_runtime=runtime,
                   helper_sha256={name:sha(topic/'scripts'/name) for name in HELPERS},
                   stages=[], started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   all_large_reconstructible_inputs_and_work_outside_git=True,
                   mathematical_existence_claimed=False, failure=None)
    start = time.monotonic()
    summary_path = output / 'replay-summary.json'
    if summary_path.exists() and read(summary_path).get('complete'):
        raise FileExistsError('preserve completed replay evidence; choose a new result directory')
    atomic_json(summary_path, summary)
    current_stage = None
    try:
        if runtime != original_runtime:
            raise ValueError('pin the exact original runtime before attempting deterministic replay')
        for specification in manifest['stages']:
            if sha(topic/specification['producer']) != specification['producer_sha256']:
                raise ValueError('an original producer changed: ' + specification['producer'])
        guess = topic / manifest['published_seed_index']
        seed = read(guess)
        if seed['parts'] != manifest['published_seed_parts']:
            raise ValueError('the complete original M128 seed parts changed')
        from fourfold_codazzi_candidate_shards import load_candidate
        load_candidate(guess)
        summary['seed_index_sha256'] = sha(guess)
        for specification in manifest['stages']:
            number = current_stage = specification['stage']
            attempt = work / ('stage%02d' % number)
            if not attempt.exists():
                if args.validate_existing:
                    raise FileNotFoundError('a complete existing stage is missing: ' + str(attempt))
                helper = HELPERS[0 if number <= 2 else 1]
                run([sys.executable, str(topic/'scripts'/helper), '--topic', str(topic),
                     '--attempt', str(attempt), '--stage', str(number),
                     '--guess', str(guess), '--address-space-mib', str(args.address_space_mib)], topic)
            process = read(attempt / 'process.json')
            if (not process.get('complete')
                    or process.get('producer_sha256') != specification['producer_sha256']
                    or process.get('guess_sha256') != sha(guess)):
                raise ValueError('a stage is unfinished or its actual complete input changed')
            if number <= 2:
                candidate = preserve_first(topic, attempt, number, specification)
                if number == 2:
                    candidate = restore_historical(topic, candidate, EARLY_MANIFEST,
                                                   attempt/'restored-original')
            else:
                if process.get('actual_returncode') != 0 or not process.get('finite_BVP_success'):
                    raise ValueError('the unchanged full finite BVP gate did not pass')
                candidate = Path(process['candidate_path'])
            if number == 6:
                # A fresh comparison reconstructs every original gzip from
                # the complete regenerated arrays before restoring metadata.
                candidate = restore_historical(topic, candidate, FINAL_MANIFEST,
                                               attempt/'restored-original')
            entry = checked_candidate(candidate, specification['historical_complete_candidate_sha256'])
            entry.update(stage=number, process_sha256=sha(attempt/'process.json'),
                         accepted_sha256=specification.get('historical_accepted_checkpoint_sha256'),
                         producer_actual_returncode=process.get('actual_returncode'),
                         original_full_equations_tolerances_and_parameters_retained=True)
            summary['stages'].append(entry)
            for name in ('process.json','Hermite-preservation.json'):
                public_copy(attempt/name, output/('stage%02d-'%number+name))
            public_copy(attempt/'restored-original/identity-report.json',
                        output/('stage%02d-scientific-identity.json'%number))
            atomic_json(summary_path, summary)
            guess = candidate
            print(json.dumps(dict(complete_original_stage=number, candidate_sha256=sha(guess))), flush=True)
        if sha(guess) != FINAL:
            raise ValueError('the final exact ac1 identity did not close')
        summary.update(complete=True, final_candidate=str(guess.resolve()),
                       final_candidate_sha256=sha(guess),
                       all_six_complete_original_identities_recovered=True,
                       all_final_scientific_arrays_and_five_original_container_bytes_verified=True)
        args.candidate_path_file.parent.mkdir(parents=True, exist_ok=True)
        args.candidate_path_file.write_text(str(guess.resolve())+'\n')
    except Exception as error:
        summary['failure'] = dict(stage=current_stage, type=type(error).__name__,
                                  message=str(error), original_files_retained=True)
        raise
    finally:
        summary['wall_seconds'] = time.monotonic()-start
        atomic_json(summary_path, summary)
    print(json.dumps(dict(complete=True, final_candidate=str(guess),
                          small_evidence=str(summary_path))), flush=True)


if __name__ == '__main__':
    main()
