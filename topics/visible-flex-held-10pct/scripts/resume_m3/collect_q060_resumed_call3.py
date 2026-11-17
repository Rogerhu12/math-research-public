#!/usr/bin/env python3
"""Collect the already completed q060 retry and its existing residual locator.

No solver or locator is executed.  Full failed states, stage rankings and
coefficient arrays stay in scratch.  Only parameters, source hashes, actual
terminal metadata and three explanatory residual locations are collected.
"""
import argparse
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_bytes()
    return json.loads(data)


def parameter_options(command):
    result = {}
    i = 2
    while i < len(command):
        if i+1 < len(command) and not command[i+1].startswith('--'):
            result[command[i]] = command[i+1]
            i += 2
        else:
            result[command[i]] = True
            i += 1
    return result


def selected_location(row):
    return {key:row[key] for key in (
        'stage','rawCell','rawSegment','rawLeft','rawRight','component',
        'physicalMode','componentKind','normalizedResidual','signedResidual',
        'normalizationScale','componentUlp','residualInComponentUlps','minA','minD')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--original-run', type=Path, required=True)
    parser.add_argument('--source-aliases', type=Path,
                        help='JSON mapping of unavailable recorded paths to byte-identical current paths')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    run, oldrun = args.run.resolve(), args.original_run.resolve()
    resume = read(run/'resume-command.json')
    original_command = read(oldrun/'continuation-command.json')
    terminal = read(run/'resource.json')
    summary = read(run/'seed-summary.json')
    locate = read(run/'call3-locate.json')
    locate_terminal = read(run/'call3-locate-resource.json')
    cfg, oldcfg = read(run/'config.json'), read(oldrun/'config.json')
    newopt, oldopt = parameter_options(resume['command']), parameter_options(original_command['command'])
    option_changes = {key:dict(before=oldopt.get(key),after=newopt.get(key))
        for key in set(newopt)|set(oldopt) if newopt.get(key)!=oldopt.get(key)}
    config_changes = {key:dict(before=oldcfg.get(key),after=cfg.get(key))
        for key in set(cfg)|set(oldcfg) if cfg.get(key)!=oldcfg.get(key)}
    aliases = read(args.source_aliases) if args.source_aliases else {}
    input_verification = {}
    for path, expected in {**resume['inputs'], **resume['source_sha256']}.items():
        actual_path = path if Path(path).is_file() else aliases.get(path)
        if actual_path is None or sha(actual_path) != expected:
            raise ValueError('A recorded input/source changed: '+path)
        input_verification[path] = dict(expected_sha256=expected,
            verified_path=str(actual_path), storage_path_migrated=str(actual_path)!=path)
    checks = dict(
        original_command_sha_matches=sha(oldrun/'continuation-command.json')==resume['original_command_sha256'],
        original_config_sha_matches=sha(oldrun/'config.json')==resume['original_configuration_sha256'],
        profile_bytes_unchanged=(run/'profile.json').read_bytes()==(oldrun/'profile.json').read_bytes(),
        port_bytes_unchanged=(run/'port.json').read_bytes()==(oldrun/'port.json').read_bytes(),
        only_output_argument_paths_changed=set(option_changes)=={'--profile','--linear-port','--tail-config','--out-prefix'},
        only_tail_initializer_and_trace_changed=set(config_changes)=={'designInitialCheckpoint','initialCheckpoint','traceFile'},
        original_solver_gate=cfg['solveTolerance']==2e-9,
        observed_process_terminal=terminal['status']=='observed_terminal' and terminal['child_returncode']==0,
        observed_locator_terminal=locate_terminal['status']=='observed_terminal' and locate_terminal['child_returncode']==0,
        summary_is_failed=summary['solver_success'] is False,
        no_final_prefix_file=not (run/'seed.json.gz').exists(),
        no_saved_prefix_coefficients=not list(run.glob('seed_coeff_*.npy.gz')),
        no_saved_inner_debug=not list(run.glob('seed-inner-*-debug.json.gz')))
    if not all(checks.values()):
        raise ValueError(checks)
    source = Path(newopt['--source-topic'])
    coupler_path = source/'scripts/db6f-prefix-coupled.py'
    coupler_text = coupler_path.read_text()
    node = next(z for z in ast.parse(coupler_text).body
                if isinstance(z, ast.FunctionDef) and z.name=='solve_with_actual_tail')
    loop = next(z for z in node.body if isinstance(z, ast.For))
    guard = next(i for i,z in enumerate(loop.body) if isinstance(z,ast.If) and
        ast.unparse(z.test)=='not sol.success' and any(isinstance(q,ast.Return) for q in z.body))
    actual = next(i for i,z in enumerate(loop.body) if isinstance(z,ast.Assign) and
        any(isinstance(q,ast.Name) and q.id=='actual' for q in z.targets))
    if not actual > guard:
        raise ValueError('The source does not establish inner success before candidate tail query')
    calls = []
    records = []
    for number in (1,2,3):
        path = run/f'seed_tail_{number:04d}.json.gz'
        item = read(path); records.append(item)
        if item['config'] != cfg:
            raise ValueError('The actual tail config differs at call '+str(number))
        for name, expected in item['source_sha256'].items():
            if sha(source/'scripts'/name) != expected:
                raise ValueError('An actual tail source changed: '+name)
        response = item['response']; jac = response.get('heightJetJacobian')
        calls.append(dict(call=number,file=str(path),sha256=sha(path),
            request=item['request'],converged=response.get('converged',False),
            residual=response.get('residual'),failure=response.get('failed'),
            last_iteration=response.get('lastIteration'),
            history_scalar=response.get('history'),
            returned_height_jacobian_entries=len(jac) if jac is not None else None,
            returned_height_jacobian_finite=all(math.isfinite(x) for x in jac) if jac is not None else None,
            audit=response.get('audit')))
    if not (calls[0]['converged'] and calls[1]['converged'] and not calls[2]['converged']):
        raise ValueError('Unexpected actual tail acceptance sequence')
    if not all(isinstance(row['residual'], (int,float)) and
               math.isfinite(row['residual']) and row['residual'] < cfg['solveTolerance']
               for row in calls[:2]):
        raise ValueError('An accepted initial tail failed the original finite residual gate')
    if not calls[1]['returned_height_jacobian_finite'] or calls[1]['returned_height_jacobian_entries'] != 208:
        raise ValueError('The accepted call2 tangent is not complete')
    if (records[0]['request']['height'] != records[1]['request']['height'] or
            records[1]['request']['height'] == records[2]['request']['height']):
        raise ValueError('Unexpected initial/candidate height identity')
    if locate['input_sha256'] != calls[2]['sha256']:
        raise ValueError('The locator does not belong to the actual failed candidate tail')
    if locate['replayNormalizedResidual'] != calls[2]['last_iteration']['norm']:
        raise ValueError('The locator did not reproduce the last original residual')
    for path,expected in locate['source_sha256'].items():
        if sha(path)!=expected:
            raise ValueError('The locator source changed: '+path)
    dominant, second, lowest = locate['largestResidual'][0], locate['largestResidual'][1], locate['lowestA'][0]
    if (dominant['stage'],dominant['physicalMode'],second['stage'],second['physicalMode'],lowest['stage']) != (45,12,43,15,40):
        raise ValueError('The explanatory locations do not match this recorded state')
    inputs = dict(resume['inputs'])
    restart = Path(newopt['--restart'])
    inputs.update({str(z):sha(z) for z in sorted(restart.parent.glob(restart.name.split('.')[0]+'_coeff_*.npy.gz'))})
    artifacts = {str(run/name):sha(run/name) for name in (
        'resume-command.json','resource.json','seed-summary.json','seed-design-initializer.json',
        'config.json','profile.json','port.json','run.log','worker-trace.jsonl',
        'call3-locate.json','call3-locate-resource.json')}
    output = dict(scope=__doc__,command=sys.argv,run=str(run),original_run=str(oldrun),
        recorded_design=dict(q=.06,base_mode=3,modes=8,angular=256,audit_angular=512,
            fixed_metric=False,initial_prefix_nodes=815,tail_quadrature=locate['quadrature'],
            tail_parts=locate['shootingParts'],tail_stages=locate['stages'],
            tail_gate=locate['originalGate'],profile=read(run/'profile.json'),tail_config=cfg),
        execution=dict(actual_command=resume['command'],
            resumed_utc=resume['started_utc'],
            terminal={key:terminal[key] for key in ('status','child_returncode','observed_utc','seconds')},
            summary=summary,
            tool_session_reported_by_parent=36748,locator_tool_session_reported_by_parent=91612,
            locator_command=locate_terminal['command'],
            locator_terminal={key:locate_terminal[key] for key in ('status','child_returncode','observed_utc','seconds')}),
        identity_checks=checks,option_changes=option_changes,config_changes=config_changes,
        recorded_input_verification=input_verification,
        inputs_sha256=inputs,artifacts_sha256=artifacts,
        actual_tail_source_sha256=records[2]['source_sha256'],
        additional_source_sha256={**resume['source_sha256'],str(coupler_path):sha(coupler_path),str(Path(__file__).resolve()):sha(__file__)},
        tail_calls=calls,
        candidate_height_change_max=max(abs(a-b) for a,b in zip(records[1]['request']['height'],records[2]['request']['height'])),
        inner_prefix_status=dict(
            source_control_flow='The original failed-inner guard returns before candidate=... and the call3 actual tail query. Reaching this new request therefore implies sol.success for the temporary affine inner problem.',
            original_function_source_sha256=hashlib.sha256(ast.get_source_segment(coupler_text,node).encode()).hexdigest(),
            accepted_actual_prefix=False,saved_raw_inner_state=False,
            final_prefix_checkpoint=False,final_prefix_metric=None,
            limitation='No raw p/sol checkpoint was written before call3 in this original coupler. The new H alone does not recover the inner field, its parameters, RMS or a final actual boundary/metric audit.'),
        locator=dict(input_accepted=False,replay_residual=locate['replayNormalizedResidual'],
            exact_replay_of_recorded_norm=True,minA=locate['minA'],minD=locate['minD'],
            end_residual_max=locate['endResidualMax'],
            dominant_matching_location=selected_location(dominant),
            second_independent_matching_location=selected_location(second),
            minimum_A_location=selected_location(lowest),
            source_sha256=locate['source_sha256'],
            scope='Only these three explanatory locations are collected. The complete failed state and stage/ranking tables remain in the hashed scratch artifacts.'),
        interpretation='The resumed old-H actual tail passed, but its new prefix-generated H failed the unchanged original tail gate. This is a new q060 physical design relative to the accepted q040 prefix, not fixed-g refinement. Exit0 reflects the wrapper catching the error, not a successful coupled state. No finite threshold, mathematical amplitude barrier, or complete prefix metric is inferred.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),checks=checks,
        call3_residual=locate['replayNormalizedResidual'],prefix_saved=False),indent=2))


if __name__=='__main__':
    main()
