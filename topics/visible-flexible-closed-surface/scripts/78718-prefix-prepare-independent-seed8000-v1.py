#!/usr/bin/env python3
"""Pure preparation for the independent published-M14 seed route at max8000.

Validates original 97/141/152 source inputs, the original true M14 seed
and own tail_0002, plus existing common typed-code source evidence.
Creates metadata only; no candidate/restart/RHS/Newton/factory/BVP/DN.
This preparation is not an independent numerical execution.
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
    i = module('independent_seed8000_pure_input_definitions', HERE / '78718-prefix-independent-seed8000-inputs-v1.py')
    original, ancestor = i.ancestor_context()
    seed_inputs = i.published_seed_inputs(original, ancestor)
    evidence = i.code_evidence(args.code_check_report, args.code_check_observed)
    if args.check_current_gate:
        print(json.dumps({'status': 'PASS_PUBLISHED_SEED8000_INPUTS_ONLY', 'writes': 0,
                          'failed_CP_warm_input_used': False, 'solver_calls': 0,
                          'warm_residual': seed_inputs['record']['own_last_packet_check']['residual']}))
        return 0
    out = args.out_prefix.resolve()
    i.require(out.parent == i.NOTES.resolve() and out.name.startswith('2026-11-10-78718-independent-')
              and not list(out.parent.glob(out.name + '*')), 'Use a completely unused independent notes stem')
    c = module('independent_seed8000_pure_driver_definitions', i.RUNNER)
    cfg_path = Path(str(out) + '-tail-config.json')
    launch_path = Path(str(out) + '-launch.json')
    prep_path = Path(str(out) + '-preparation.json')
    cfg = i.expected_config(original, ancestor, out)
    cfg_data = (json.dumps(cfg, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    cfg_row = {'path': str(cfg_path), 'bytes': len(cfg_data), 'sha256': hashlib.sha256(cfg_data).hexdigest()}
    rows = ancestor['launch']['bindings'] + seed_inputs['original_runtime_closure'] + evidence['bindings']
    rows += [i.identity(path) for path in (i.ANCESTOR, i.RUNTIME_SOURCE_GUARD,
             i.RUNNER, i.PREPARER, i.AUDITOR, HERE / '78718-prefix-independent-seed8000-inputs-v1.py',
             i.CODE_CORE, i.CODE_CHECKER, i.RUNTIME_CHECKER, i.GUARD_PREPARER, i.TOOL_OBSERVER)]
    bindings = {row['path']: row for row in rows}
    bindings[str(cfg_path)] = cfg_row
    launch = {key: ancestor['launch'][key] for key in (
        'reference_preparation', 'frozen_physical_fields', 'source_root', 'callbacks',
        'weights', 'newton_lifetime_definitions', 'csc_prerequisites', 'csc_selection_definitions')}
    launch.update(schema=i.LAUNCH_SCHEMA, status='PREPARED_NOT_STARTED', scope=i.SCOPE,
        settings=i.SETTINGS, ancestor_launch=i.identity(i.ANCESTOR),
        source_checkpoint=i.identity(i.PUBLISHED_CP), own_actual_tail_warm=i.identity(i.LAST_TAIL),
        published_seed_input_check=seed_inputs['record'], executor=i.EXECUTOR,
        observation_recorder=i.identity(i.TOOL_OBSERVER),
        typed_code_prerequisite=evidence, launch_path=str(launch_path), out_prefix=str(out),
        tail_config=cfg_row, command=[sys.executable, str(i.RUNNER), '--launch', str(launch_path)],
        cwd=str(i.REPO), delegated_parser_argv=i.expected_argv(ancestor, cfg_path, out),
        stdout_log=str(out)+'-run.log', reproduction_file=str(out)+'-reproduction.json',
        original_summary_file=str(out)+'-summary.json', checkpoint_output=str(out)+'.json.gz',
        first_request_binding=str(out)+'-first-request-binding.json',
        coefficient_output_pattern=str(out)+'_coeff_*.npy.gz',
        bindings=sorted(bindings.values(), key=lambda row: row['path']),
        original_equations_and_callback_identity_unchanged=True,
        changed_numeric_policy={'max_nodes': {'source_ancestor': 6500, 'new': 8000}},
        restart_scope='Published true M14 seed and its own published audited tail_0002; no current root failed-CP warm input.',
        failed_CP_warm_input_used=False, exact_replay_of_failed_CP_restart_route=False,
        runtime_code_gate='Retain every original raw identity/closure gate and all ten live typed-code source identities before/after each real BVP and restoration.',
        final_gate='Actual successful outer/CP/tail and genuine /root/independent_audit natural tool exit0 remain mandatory.')
    c.validate_inputs(launch, planned_config=cfg)
    c.write_json(cfg_path, cfg, exclusive=True)
    c.write_json(launch_path, launch, exclusive=True)
    report = {'schema': '78718-independent-seed8000-pure-preparation-v1',
        'status': 'PREPARED_ONLY_NO_NEW_CANDIDATE_NO_SOLVER', 'scope': __doc__,
        'launch': i.identity(launch_path), 'tail_config': i.identity(cfg_path),
        'source_ancestor_launch': i.identity(i.ANCESTOR),
        'original_seed_input_check': seed_inputs['record'], 'executor': i.EXECUTOR,
        'settings': i.SETTINGS, 'bindings': len(bindings),
        'callback_definitions': len(launch['callbacks']), 'typed_code_evidence': evidence,
        'operations': {'candidate_objects': 0, 'restart_calls': 0, 'RHS_calls': 0,
            'Newton_install_calls': 0, 'CSC_factory_calls': 0, 'matrix_calls': 0,
            'BVP_calls': 0, 'DN_calls': 0},
        'failed_CP_warm_input_used': False, 'independent_numerical_replay_performed': False,
        'future_actual_exit': 'NOT_STARTED; only /root/independent_audit can supply its actual tool observation'}
    c.write_json(prep_path, report, exclusive=True)
    print(json.dumps({'status': report['status'], 'bindings': len(bindings),
        'launch': i.identity(launch_path), 'preparation': i.identity(prep_path),
        'failed_CP_warm_input_used': False, 'solver_calls': 0}, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
