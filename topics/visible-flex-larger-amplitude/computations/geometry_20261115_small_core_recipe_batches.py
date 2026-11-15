#!/usr/bin/env python3
"""Actions-only bounded orchestration of the frozen eta=0.01 recipe producer.

Each child keeps the original 8x20 outer and 12x20 inner budgets, equations,
Jacobian, full-three merit/Armijo, unit/full112, FD, scalar Arb and circle
checks. This stdlib parent computes no scientific quantity. It copies three
actual final parameters into a short recipe for a fresh child evaluation.
Only an explicit original outer-budget stop with the original unit flag
false permits continuation, at most 64 batches. Other stops/errors remain
stops; neither a batch nor this runner claims native/BVP completion.

Every actual outer/inner trial and reported flag is printed. Long numeric
arrays alone are omitted from the compact log, with explicit path/length;
their original enclosing file is hashed. Output file hashes and compact
actual summaries precede cleanup of each temporary raw tree. OUT retains
only the last recipe, last compact batch readout and run/parameter/hash summary.
No artifact, Release, Git write, network call or equation import occurs.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import traceback

HERE = Path(__file__).resolve().parent
ENTRY = 'geometry_20261115_small_core_recipe_batches.py'
SCHEMA = 'R278-explicit-recipe-fixed-eta-batch-orchestration-v1'
PRODUCER = 'geometry_20261115_small_core_inexact_p3_eta_0p01_recipe.py'
PRODUCER_SHA = '3169b2d3ea821a244d9f27611cd6c5cb3b239cf0e7f9bbbd7f49ac9d5f1dc9ee'
PRODUCER_SCHEMA = 'R278-original-three-equation-inexact-p3-explicit-recipe-LM-eta0p01-v1'
RECIPE_SCHEMA = 'R278-explicit-three-parameter-continuation-recipe-v1'
STATUS = 'inexact-p3-restoration-status.json'
BUDGET_STOP = 'explicit outer direction budget completed'
INPUTS = {
    'accepted': 'b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff',
    'prepared': '0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714',
    'tail_anchor': 'e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51',
    'tail_config': '01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5',
}
BUDGET = dict(candidate_iteration_budget=8, original_backtrack_budget=20,
    inner_newton_update_budget=12, inner_backtrack_budget=20,
    damping_cli_text='0.01', damping_binary64=0.01,
    candidate_resonance_tolerance=1e-8, scalar_interval_bits=160,
    scalar_interval_maximum_depth=14)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=True, allow_nan=False,
                       sort_keys=True, separators=(',', ':'))+'\n').encode('utf-8')


def save(path, value):
    raw = encode(value)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)
    return dict(file=path.name, bytes=len(raw), sha256=digest(raw))


def emit(kind, value):
    print('R278_BATCH_EVENT '+encode(dict(kind=kind, **value)).decode().rstrip('\n'), flush=True)


def compact(value, path=''):
    """Copy all trial dictionaries, scalar values and booleans; no new math."""
    if isinstance(value, dict):
        return {key: compact(item, path+'/'+key) for key, item in value.items()}
    if isinstance(value, list):
        if len(value) > 3 and all(type(item) in (int, float) for item in value):
            return dict(omitted_numeric_array=True, original_json_path=path, length=len(value),
                        enclosing_original_file_hashed=True)
        return [compact(item, path+'/'+str(index)) for index, item in enumerate(value)]
    return value


def inventory(root):
    rows = []
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Unexpected child-output symlink')
        if path.is_file():
            rows.append(dict(file=path.relative_to(root).as_posix(),
                             bytes=path.stat().st_size, sha256=file_sha(path)))
    return rows


def original_inner(root, receipt):
    name = Path(receipt['file'])
    if name.is_absolute() or '..' in name.parts:
        raise ValueError('An inner receipt must remain inside the child output')
    path = root/name
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('An inner receipt escaped the child output')
    raw = path.read_bytes()
    if len(raw) != receipt['bytes'] or digest(raw) != receipt['sha256']:
        raise ValueError('The actual inner report did not match its descriptor')
    return json.loads(gzip.decompress(raw) if raw.startswith(b'\x1f\x8b') else raw)


def validate(status, recipe):
    if (status.get('schema') != PRODUCER_SCHEMA or status.get('source_sha256') != PRODUCER_SHA
            or status.get('consumed_source_sha256', {}).get(PRODUCER) != PRODUCER_SHA
            or len(status.get('consumed_source_sha256', {})) != 15
            or status.get('input_sha256') != INPUTS
            or status.get('phase') != 'diagnostic-completed'
            or status.get('diagnostic_completed') is not True
            or status.get('success') is not False
            or status.get('native_nonlinear_solver_called') is not False
            or status.get('full_nonlinear_nonzero_lambda_solution_computed') is not False):
        raise ValueError('The original child did not return its genuine completed diagnostic')
    for key, value in BUDGET.items():
        if status.get(key) != value:
            raise ValueError('The child changed its fixed parameter/budget: '+key)
    bound = status.get('parameter_recipe', {})
    if (bound.get('sha256') != recipe['sha256'] or bound.get('bytes') != recipe['bytes']
            or status.get('explicit_recipe_is_not_a_parent_status') is not True
            or status.get('prior_status_or_log_payloads_read') is not False):
        raise ValueError('The child must bind the exact short recipe it received')
    if type(status.get('original_unit_stopping_tolerance_met')) is not bool:
        raise ValueError('The original unit stopping flag is missing')
    parameters = status.get('final', {}).get('parameters')
    if not isinstance(parameters, list) or len(parameters) != 3:
        raise ValueError('The actual final three parameters are missing')
    return parameters


def recipe_from(run, raw_status, log_summary, parameters):
    return dict(schema=RECIPE_SCHEMA, origin=dict(
        repository='Rogerhu12/math-research-public', run_id=run['run_id'],
        source_commit=run['source_commit'], producer_file=PRODUCER,
        producer_sha256=PRODUCER_SHA, producer_schema=PRODUCER_SCHEMA,
        status_bytes=raw_status['bytes'], status_sha256=raw_status['sha256'],
        log_summary_bytes=log_summary['bytes'], log_summary_sha256=log_summary['sha256'],
        parameter_field='final.parameters'),
        literal_parameters=parameters, input_sha256=INPUTS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('accepted', 'prepared', 'tail-anchor', 'tail-config', 'parameter-recipe', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--parameter-recipe-sha256', required=True)
    parser.add_argument('--max-batches', type=int, default=64)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Run only in the original public repository Actions')
    if not 1 <= args.max_batches <= 64:
        raise ValueError('The explicit batch bound is one through 64')
    if Path(__file__).name != ENTRY or file_sha(HERE/PRODUCER) != PRODUCER_SHA:
        raise ValueError('Retain the frozen recipe producer and orchestration basename')
    run = dict(repository='Rogerhu12/math-research-public',
        run_id=os.environ.get('GITHUB_RUN_ID', ''), source_commit=os.environ.get('GITHUB_SHA', ''),
        attempt=os.environ.get('GITHUB_RUN_ATTEMPT', ''))
    if (not run['run_id'] or any(c not in '0123456789' for c in run['run_id'])
            or len(run['source_commit']) != 40
            or any(c not in '0123456789abcdef' for c in run['source_commit'])):
        raise ValueError('Retain the real Actions run/source identity')
    for key, wanted in INPUTS.items():
        if file_sha(getattr(args, key)) != wanted:
            raise ValueError('Retain the complete original model input: '+key)
    initial_raw = args.parameter_recipe.read_bytes()
    if len(initial_raw) > 16384 or digest(initial_raw) != args.parameter_recipe_sha256:
        raise ValueError('Use the actual first short recipe and its declared digest')
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError('Use a fresh orchestration output directory')
    seed_path = args.out/'next-parameter-recipe.json'
    seed_path.write_bytes(initial_raw)
    seed = dict(file=seed_path.name, bytes=len(initial_raw), sha256=digest(initial_raw))
    temporary_parent = Path(os.environ['RUNNER_TEMP']).resolve()
    if not temporary_parent.is_dir():
        raise ValueError('Actions RUNNER_TEMP must exist')
    result = dict(schema=SCHEMA, run=run, source_sha256=file_sha(__file__),
        producer_file=PRODUCER, producer_sha256=PRODUCER_SHA,
        input_sha256=INPUTS, initial_recipe=seed, maximum_batches=args.max_batches,
        original_budget=BUDGET, batches=[], stop_reason=None, success=False,
        native_or_BVP_acceptance_claimed=False, scientific_arithmetic_in_parent=False,
        raw_results_saved_to_git_release_or_artifact=False)
    code = 0
    try:
        for batch in range(args.max_batches):
            result.update(phase='running-batch', current_batch=batch)
            save(args.out/'summary.json', result)
            with tempfile.TemporaryDirectory(prefix='r278-recipe-batch-', dir=temporary_parent) as temp:
                child_out = Path(temp)/'result'
                command = [sys.executable, str(HERE/PRODUCER)]
                for key in INPUTS:
                    command += ['--'+key.replace('_', '-'), str(getattr(args, key).resolve())]
                command += ['--parameter-recipe', str(seed_path.resolve()),
                    '--parameter-recipe-sha256', seed['sha256'],
                    '--damping', '0.01', '--candidate-steps', '8', '--backtracks', '20',
                    '--inner-newton-steps', '12', '--inner-backtracks', '20',
                    '--candidate-resonance-tolerance', '1e-8',
                    '--interval-bits', '160', '--interval-depth', '14', '--out', str(child_out)]
                emit('batch_start', dict(batch=batch, command=command, input_recipe=seed))
                child = subprocess.run(command, check=False)
                files = inventory(child_out) if child_out.is_dir() else []
                emit('all_output_file_hashes', dict(batch=batch, files=files))
                status, status_file = {}, None
                if (child_out/STATUS).is_file():
                    raw = (child_out/STATUS).read_bytes()
                    status_file = dict(file=STATUS, bytes=len(raw), sha256=digest(raw))
                    result['current_status_file'] = status_file
                    status = json.loads(raw)
                small = compact({key: value for key, value in status.items()
                    if key not in ('searches', 'inner_reports')})
                summary = dict(schema='R278-recipe-batch-original-log-summary-v1',
                    batch=batch, run=run, input_recipe=seed, command=command,
                    child_returncode=child.returncode, original_status=status_file,
                    original_fields=small,
                    original_search_count=len(status.get('searches', [])),
                    no_scientific_quantity_recomputed_by_parent=True)
                summary_raw = encode(summary)
                (args.out/'last-batch-log-summary.json').write_bytes(summary_raw)
                summary_file = dict(bytes=len(summary_raw), sha256=digest(summary_raw),
                    encoding='UTF-8 JSON plus LF between R278_BATCH_SUMMARY markers')
                print('R278_BATCH_SUMMARY_BEGIN '+str(batch), flush=True)
                sys.stdout.write(summary_raw.decode('utf-8'))
                sys.stdout.flush()
                print('R278_BATCH_SUMMARY_END '+str(batch), flush=True)
                for search in status.get('searches', []):
                    emit('complete_outer_direction_and_trials',
                         dict(batch=batch, original=compact(search)))
                for receipt in status.get('inner_reports', []):
                    report = original_inner(child_out, receipt)
                    emit('complete_inner_probe_steps_and_trials',
                         dict(batch=batch, receipt=compact(receipt), original=compact(report)))
                item = dict(batch=batch, child_returncode=child.returncode,
                    status=status_file, log_summary=summary_file,
                    initial_merit=status.get('initial_original_three_equation_merit'),
                    final_merit=status.get('final_original_three_equation_merit'),
                    final_parameters=status.get('final', {}).get('parameters'),
                    original_stop_reason=status.get('search_stop_reason'),
                    original_unit_flag=status.get('original_unit_stopping_tolerance_met'),
                    original_full112_flag=status.get('low_mode_candidate_has_small_full_recorded_right_residual'),
                    raw_outputs_deleted=False)
                result['batches'].append(item)
                again = False
                if child.returncode != 0:
                    code = child.returncode if child.returncode > 0 else 1
                    result['stop_reason'] = 'original child process returned nonzero'
                else:
                    parameters = validate(status, seed)
                    seed = save(seed_path, recipe_from(run, status_file, summary_file, parameters))
                    result.update(last_recipe=seed, last_actual_parameters=parameters)
                    if status['original_unit_stopping_tolerance_met']:
                        result['stop_reason'] = 'original unit stopping condition reported; no native completion claimed'
                    elif status['search_stop_reason'] != BUDGET_STOP:
                        result['stop_reason'] = 'original non-budget stop: '+status['search_stop_reason']
                    elif batch+1 == args.max_batches:
                        result['stop_reason'] = 'explicit orchestration batch budget completed'
                    else:
                        again = True
                        result['stop_reason'] = None
            item['raw_outputs_deleted'] = True
            emit('batch_closed', dict(batch=batch, raw_outputs_deleted=True, continue_batch=again,
                                     stop_reason=result['stop_reason']))
            save(args.out/'summary.json', result)
            if not again:
                break
        result.update(phase='orchestration-stopped', orchestration_returncode=code)
        return code
    except Exception as error:
        result.update(phase='orchestration-error', exception=repr(error),
            traceback=traceback.format_exc(), stop_reason='orchestration readout/transport error')
        raise
    finally:
        final = save(args.out/'summary.json', result)
        emit('orchestration_final', dict(summary=final, original_report=result,
            only_last_recipe_and_compact_summaries_retained=True,
            original_native_acceptance_claimed=False))


if __name__ == '__main__':
    raise SystemExit(main())
