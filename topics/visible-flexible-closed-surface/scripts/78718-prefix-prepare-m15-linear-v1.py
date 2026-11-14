#!/usr/bin/env python3
"""Prepare the new M15/N512/W15 coupled route without running any solver."""
import argparse
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
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--code-check-report', type=Path, required=True)
    p.add_argument('--code-check-observed', type=Path, required=True)
    p.add_argument('--check-current-gate', action='store_true')
    a = p.parse_args()
    i = module('m15_linear_pure_input_gate', HERE/'78718-prefix-m15-linear-inputs-v1.py')
    original, ancestor = i.ancestor_context()
    seed = i.seed_inputs(original, ancestor)
    evidence = i.code_evidence(a.code_check_report, a.code_check_observed)
    if a.check_current_gate:
        print(json.dumps({'status': 'PASS_M15_UNSOLVED_WARM_AND_ORIGINAL_INPUTS_ONLY',
                          'old_prefix_remains_unsolved': True, 'new_DN_required_at_N512': True,
                          'writes': 0, 'solver_calls': 0}))
        return 0
    out = a.out_prefix.resolve()
    i.require(out.parent == i.NOTES.resolve() and out.name.startswith('2026-11-10-78718-numerical-m15-') and
              not list(out.parent.glob(out.name+'*')), 'Use a completely new M15 output stem')
    c = module('m15_linear_pure_driver_definitions', i.RUNNER)
    cfg_path, policy_path, launch_path, prep_path = [Path(str(out)+suffix) for suffix in
        ('-tail-config.json','_tail-continuation-policy.json','-launch.json','-preparation.json')]
    cfg = i.expected_config(original, ancestor, out)
    cfg_row = i.planned_identity(cfg_path, cfg)
    bindings = i.common_bindings(ancestor, seed, evidence)
    bindings[str(cfg_path)] = cfg_row
    policy = i.expected_policy(out, cfg_row, ancestor['launch']['source_root'], seed['prior'], bindings)
    policy_row = i.planned_identity(policy_path, policy)
    bindings[str(policy_path)] = policy_row
    launch = {key: ancestor['launch'][key] for key in
        ('reference_preparation','frozen_physical_fields','source_root',
         'newton_lifetime_definitions','csc_selection_definitions','csc_prerequisites')}
    launch.update(schema=i.LAUNCH_SCHEMA, status='PREPARED_NOT_STARTED', scope=i.SCOPE,
        settings=i.SETTINGS, ancestor_launch=i.identity(i.ANCESTOR), executor='/root',
        observation_recorder=i.identity(i.TOOL_OBSERVER),
        source_checkpoint=i.identity(i.SOURCE_CP), own_actual_tail_warm=i.identity(i.LAST_TAIL),
        seed_input_check=seed['record'], old_prefix_success_claimed=False,
        old_full_run_success_claimed=False, weights=i.weights(), callbacks=i.callbacks(original, ancestor),
        control_callbacks=i.control_callbacks(original), typed_code_prerequisite=evidence,
        launch_path=str(launch_path), out_prefix=str(out), tail_config=cfg_row,
        continuation_policy=policy_row,
        continuation_policy_fields={k:v for k,v in policy.items() if k != 'bindings'},
        command=[sys.executable, str(i.RUNNER), '--launch', str(launch_path)],
        cwd=str(i.REPO), delegated_parser_argv=i.expected_argv(ancestor, cfg_path, out),
        stdout_log=str(out)+'-run.log', reproduction_file=str(out)+'-reproduction.json',
        original_summary_file=str(out)+'-summary.json', checkpoint_output=str(out)+'.json.gz',
        first_request_binding=str(out)+'-first-request-binding.json',
        coefficient_output_pattern=str(out)+'_coeff_*.npy.gz',
        bindings=sorted(bindings.values(), key=lambda row:row['path']),
        numerical_changes={'prefix_M': {'previous':14,'new':15},
                           'diagonal_coordinates': 'original power2_weights(15), W15',
                           'tail_warm_angular_quadrature': {'old':256,'new':512},
                           'maximum_nodes': 8000,
                           'physical_height_path_control': policy['control']},
        unchanged_mathematical_scope='Same frozen g, physical RHS/BC/outer/seam, root/flow/Newton equations and original tolerances.',
        final_gate='Complete original finite gates, actual nine-source packets, control replay and root natural exit0; all continuous closed-graph gates remain separate.')
    i.validate(launch, planned_config=cfg, planned_policy=policy)
    c.write_json(cfg_path, cfg, exclusive=True)
    c.write_json(policy_path, policy, exclusive=True)
    c.write_json(launch_path, launch, exclusive=True)
    report = {'schema': '78718-m15-linear-pure-preparation-v1',
              'status': 'PREPARED_ONLY_NO_NEW_CANDIDATE_NO_SOLVER', 'scope': __doc__,
              'launch': i.identity(launch_path), 'tail_config': i.identity(cfg_path),
              'continuation_policy': i.identity(policy_path), 'seed_inputs': seed['record'],
              'settings': i.SETTINGS, 'launch_bindings': len(bindings),
              'policy_bindings': len(policy['bindings']), 'actual_tail_source_count': 9,
              'control_callback_definitions': len(launch['control_callbacks']),
              'original_physical_callback_definitions': len(launch['callbacks']),
              'typed_code_evidence': evidence, 'old_prefix_remains_unsolved': True,
              'operations': {'candidate_objects':0, 'restart_calls':0, 'RHS_calls':0,
                  'Newton_install_calls':0, 'CSC_factory_calls':0, 'matrix_calls':0,
                  'BVP_calls':0, 'DN_calls':0},
              'future_actual_exit': 'NOT_STARTED; a true root tool observation is required'}
    c.write_json(prep_path, report, exclusive=True)
    print(json.dumps({'status': report['status'], 'launch': i.identity(launch_path),
                      'preparation': i.identity(prep_path), 'launch_bindings':len(bindings),
                      'policy_bindings':len(policy['bindings']), 'solver_calls':0}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
