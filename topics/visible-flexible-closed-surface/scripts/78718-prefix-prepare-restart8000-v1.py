#!/usr/bin/env python3
"""Pure preparation of a new same-g M14 restart with max_nodes=8000.

Validates the unchanged run02 ancestor, its explicitly failed saved CP and own
last audited tail, and actual small code-identity checks.  Creates metadata
only. No candidate/restart/RHS/Newton/CSC factory/BVP/DN is executed.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--code-check-report', type=Path, required=True)
    ap.add_argument('--code-check-observed', type=Path, required=True)
    ap.add_argument('--check-current-gate', action='store_true')
    args = ap.parse_args()
    i = module('restart8000_pure_input_definitions', HERE / '78718-prefix-restart8000-inputs-v1.py')
    original, ancestor = i.ancestor_context()
    failed = i.failure_inputs(original, ancestor)
    evidence = i.code_evidence(args.code_check_report, args.code_check_observed)
    if args.check_current_gate:
        print(json.dumps({'status': 'PASS_RESTART8000_INPUTS_ONLY', 'writes': 0,
                          'failed_source_remains_failed': True, 'solver_calls': 0,
                          'warm_residual': failed['warm_check']['residual']}))
        return 0
    out = args.out_prefix.resolve()
    i.require(out.parent == i.NOTES.resolve() and not list(out.parent.glob(out.name + '*')),
              'Use a completely unused current topic notes stem')
    c = module('restart8000_pure_driver_definitions', i.RUNNER)
    cfg_path = Path(str(out) + '-tail-config.json')
    launch_path = Path(str(out) + '-launch.json')
    prep_path = Path(str(out) + '-preparation.json')
    cfg = i.expected_config(original, ancestor, out)
    cfg_data = (json.dumps(cfg, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    cfg_row = {'path': str(cfg_path), 'bytes': len(cfg_data), 'sha256': hashlib.sha256(cfg_data).hexdigest()}
    rows = ancestor['launch']['bindings'] + failed['closed_failure_files'] + evidence['bindings']
    rows += failed['original_runtime_closure']
    rows += [i.identity(path) for path in (i.ANCESTOR, i.FAILURE_OBSERVATION, i.RESIDUAL_REPORT,
             i.RUNNER, i.PREPARER, i.AUDITOR, HERE / '78718-prefix-restart8000-inputs-v1.py',
             i.CODE_CORE, i.CODE_CHECKER)]
    bindings = {row['path']: row for row in rows}
    bindings[str(cfg_path)] = cfg_row
    launch = {key: ancestor['launch'][key] for key in (
        'reference_preparation', 'frozen_physical_fields', 'source_root', 'callbacks',
        'weights', 'newton_lifetime_definitions', 'csc_prerequisites', 'csc_selection_definitions')}
    launch.update(schema=i.LAUNCH_SCHEMA, status='PREPARED_NOT_STARTED', scope=i.SCOPE,
        settings=i.SETTINGS, ancestor_launch=i.identity(i.ANCESTOR),
        source_checkpoint=i.identity(i.FAILED_CP), own_actual_tail_warm=i.identity(i.LAST_TAIL),
        ancestor_source_checkpoint=ancestor['launch']['source_checkpoint'],
        ancestor_tail_warm=ancestor['launch']['own_actual_tail_warm'],
        failed_source_root_observation=failed['root_observation'],
        restart_budget_diagnostic=failed['next_initial_guess_diagnostic'],
        typed_code_prerequisite=evidence, launch_path=str(launch_path), out_prefix=str(out),
        tail_config=cfg_row, command=[sys.executable, str(i.RUNNER), '--launch', str(launch_path)],
        cwd=str(i.REPO), delegated_parser_argv=i.expected_argv(ancestor, cfg_path, out),
        stdout_log=str(out)+'-run.log', reproduction_file=str(out)+'-reproduction.json',
        original_summary_file=str(out)+'-summary.json', checkpoint_output=str(out)+'.json.gz',
        first_request_binding=str(out)+'-first-request-binding.json',
        coefficient_output_pattern=str(out)+'_coeff_*.npy.gz',
        bindings=sorted(bindings.values(), key=lambda row: row['path']),
        original_equations_and_callback_identity_unchanged=True,
        changed_numeric_policy={'max_nodes': {'ancestor': 6500, 'new': 8000}},
        restart_scope='Failed run02 CP and own audited last packet are initial guesses only.',
        original_ancestor_success=False,
        runtime_code_gate='Retain every original raw identity/closure gate; separately capture live typed code and check against pinned compilation before/after each real BVP and after restoration.',
        final_gate='Actual successful outer/CP/tail and root natural exit0 remain mandatory.')
    c.validate_inputs(launch, planned_config=cfg)
    c.write_json(cfg_path, cfg, exclusive=True)
    c.write_json(launch_path, launch, exclusive=True)
    report = {'schema': '78718-restart8000-pure-preparation-v1',
        'status': 'PREPARED_ONLY_NO_NEW_CANDIDATE_NO_SOLVER',
        'scope': __doc__, 'launch': i.identity(launch_path), 'tail_config': i.identity(cfg_path),
        'ancestor_launch': i.identity(i.ANCESTOR), 'ancestor_success': False,
        'failed_CP': i.identity(i.FAILED_CP), 'own_last_warm_packet': i.identity(i.LAST_TAIL),
        'failed_CP_polynomial_check': failed['polynomial_check'],
        'own_last_warm_check': failed['warm_check'],
        'settings': i.SETTINGS, 'bindings': len(bindings),
        'callback_definitions': len(launch['callbacks']),
        'typed_code_evidence': evidence,
        'operations': {'candidate_objects': 0, 'restart_calls': 0, 'RHS_calls': 0,
            'Newton_install_calls': 0, 'CSC_factory_calls': 0, 'matrix_calls': 0,
            'BVP_calls': 0, 'DN_calls': 0},
        'future_actual_exit': 'NOT_STARTED; only root can supply actual observation'}
    c.write_json(prep_path, report, exclusive=True)
    print(json.dumps({'status': report['status'], 'bindings': len(bindings),
        'launch': i.identity(launch_path), 'preparation': i.identity(prep_path),
        'source_CP_remains_failed': True, 'solver_calls': 0}, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
