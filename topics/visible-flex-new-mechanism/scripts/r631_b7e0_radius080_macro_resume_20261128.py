#!/usr/bin/env python3
"""Continue the R631 R=.8 connection from the actual accepted work-grid b7e0 state."""
import hashlib
import json
import os
from pathlib import Path
import types


HERE = Path(__file__).resolve().parent
PREVIOUS = HERE / 'r631_radius080_macro_core_design_20261128.py'
PREVIOUS_SHA = '119f32035445345514f8ebc3fd33cc8fe5ab8c24cadcb587b82c631f5f8c23e2'
REQUEST = HERE.parent / 'computations/request-r631-radius080-macro-core-design-20261128.json'
REQUEST_SHA = '48763230c66da5265768ed8983ddaf3aadc7a57b17c7b95532eabce8bc7fe041'
CONTRACT_SHA = '9aafec2a3438dccad64be320e292facdacfc6d9de7aa099f52b9db59a103ec9f'
INPUT_SHA = '90e94c4e43ccfec7566354c5c8b5ba46bc3f152bd22be566fa57c9d882570c48'
FINAL_SHA = 'd0d227e9dadff13b71f9e85e4ac102af018e34fcbde4f61e794c24fbde0f3ab2'
Q_SHA = 'b7e0720ebe30818a0a57d5e07c231f885ef7b01688fa92987b301e44df3a7839'
SCHEMA = 'R631-R080-b7e0-real-51-accept-resume-v1'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def literal(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def load_inputs(raw):
    if digest(raw) != INPUT_SHA or digest(REQUEST.read_bytes()) != REQUEST_SHA:
        raise ValueError('R631 continuation or its original complete request differs')
    transport = json.loads(raw)
    previous = transport['original_final']
    contract_raw = json.loads(REQUEST.read_bytes())['lanes']['r631-radius080-macro-core-design']['source_state_json'].encode()
    if (digest(contract_raw) != CONTRACT_SHA or digest(literal(previous)) != FINAL_SHA
            or transport['schema'] != SCHEMA):
        raise ValueError('R631 original contract, complete terminal receipt or resume schema differs')
    checkpoint = previous['actual_current_checkpoint']
    core = checkpoint['actual_core_input']
    if (previous['failure']['type'] != 'RuleChange' or previous['actual_accepted_Newton_steps'] != 51
            or checkpoint['accepted_Newton_steps'] != 51 or checkpoint['actual_q_sha256'] != Q_SHA
            or digest(literal(checkpoint['actual_complete_q'])) != Q_SHA
            or len(checkpoint['actual_complete_q']) != 1451 or checkpoint['mu_literal'] != '0'
            or checkpoint['maximum_independent_mode'] != 48 or checkpoint['fine_grid_active']
            or checkpoint['actual_next_damping'] != previous['actual_next_damping']
            or previous['actual_next_damping'] != 1e-14 or previous['completed_finite_stages']
            or previous['last_completed_finite_stage_checkpoint'] is not None
            or previous['pending_actual_trial_not_accepted'] is not None
            or previous['complete_or_partial_final_readout'] is not None
            or core['P0_coefficients'] != checkpoint['actual_prescribed_total_P0']
            or len(core['P0_path_derivative_coefficients']) != 24):
        raise ValueError('R631 actual terminal state does not match this continuation')
    contract = json.loads(contract_raw)
    contract['schema'] = SCHEMA
    contract['resume_source'] = {k: v for k, v in transport.items() if k != 'original_final'}
    return contract, previous


class PaidCorePath:
    """The saved finite P and derivative serve this work stage; construct dense path only on advancement."""
    def __init__(self, module, seed, settings, expected):
        self.module, self.seed, self.settings, self.expected = module, seed, settings, expected
        self.path = None

    def input(self, mu_literal, *, maximum_mode, angular_points):
        if self.path is None:
            candidate = self.module.Radius080ConvexCoreInputPath(self.seed, **self.settings)
            if candidate.definition_sha256 != self.expected:
                raise ValueError('regenerated continuous R631 path differs from paid b7e0 source')
            self.path = candidate
        return self.path.input(mu_literal, maximum_mode=maximum_mode, angular_points=angular_points)


def retain_prior(run, previous):
    run.previous_terminal = previous
    run.current_record = previous['actual_current_checkpoint']
    run.accepted_steps = previous['actual_accepted_Newton_steps']
    run.damping = previous['actual_next_damping']
    run.last_trial = previous['last_actual_trial']
    run.restoring = True


def restore(run, path_module):
    source = run.input['resume_source']
    record = run.current_record
    core = record['actual_core_input']
    if (run.factory.grid_receipt != source['grid_receipt']
            or run.seed_model.guard()['design_model_sha256'] != source['seed_model_sha256']):
        raise ValueError('R631 reconstructed grid or seed definition differs')
    run.path = PaidCorePath(path_module, run.seed_model, run.input['path_settings'],
                            core['continuous_function_definition_sha256'])
    run.make_current(driver.Fraction(record['mu_literal']), core, run.seed_model,
                     driver.np.asarray(record['actual_complete_q'], dtype=float))


def restored_checkpoint(run):
    record = run.current_record
    model, q, data, state, core, mu, fine = run.current
    obs = record['observation']
    if (driver.sha(q.tolist()) != Q_SHA or not driver.np.array_equal(state['q'], q)
            or model.design_model_sha256 != obs['design_model_sha256']
            or state['design_model_sha256'] != model.design_model_sha256
            or driver.sha(data['r'].tolist()) != run.input['resume_source']['grid_receipt']['work_sha256']
            or len(data['theta']) != obs['theta_points'] or len(state['residual']) != obs['actual_all_position_rows']
            or core is not record['actual_core_input'] or model.prescribed_pc.tolist() != record['actual_prescribed_total_P0']
            or str(mu) != record['mu_literal'] or fine or model.J != 48):
        raise ValueError('R631 rebuilt full-row work state does not identify the actual previous coordinate')
    run.restoring = False
    driver.emit('RESTORED', {'accepted_steps_brought_forward': run.accepted_steps,
        'actual_q_sha256': Q_SHA, 'actual_next_damping': run.damping,
        'actual_core_input_sha256': driver.sha(core), 'work_grid': run.factory.grid_receipt,
        'work_state_evaluated_and_ball_checked_in_this_scope': True,
        'current_eta_on_rebuilt_state': float(driver.np.max(state['g']['eta'])),
        'last_paid_observation_retained_as_prior': obs,
        'old_52nd_full_J_matrix_or_factor_available': False})


def extend_final(final, run):
    prior = run.previous_terminal
    final['resume_source'] = run.input['resume_source']
    final['previous_terminal_except_full_checkpoint'] = {k: v for k, v in prior.items()
                                                        if k != 'actual_current_checkpoint'}
    final['previous_checkpoint_identity'] = {'actual_q_sha256': Q_SHA,
        'complete_checkpoint_sha256': driver.sha(prior['actual_current_checkpoint']),
        'complete_predecessor_final_sha256': FINAL_SHA, 'checkpoint_is_in_bound_request': True}
    final['previous_accepted_Newton_steps'] = prior['actual_accepted_Newton_steps']
    final['new_accepted_Newton_steps'] = run.accepted_steps-prior['actual_accepted_Newton_steps']
    final['restored_state_evaluated_in_this_scope'] = not run.restoring
    final['previous_counts_are_retained_separately_and_not_new'] = True


def amended_entry(source):
    """Bound substitutions affect receipt/startup glue; the entire nonlinear loop is reused verbatim."""
    start = "        self.path = p.Radius080ConvexCoreInputPath(self.seed_model, **self.input['path_settings'])"
    end = "        self.make_current(Fraction(0), core_input, self.seed_model, self.seed_model.initial_response())"
    bootstrap = source[source.index(start):source.index(end)+len(end)]
    changes = (
        (bootstrap, '        restore(self, p)'),
        ("        self.checkpoint('actual_new_input_domain_valid_before_connection_solve')",
         "        if self.restoring:\n            restored_checkpoint(self)\n        else:\n            self.checkpoint('actual_new_input_domain_valid_before_connection_solve')"),
        ('    incoming = json.loads(raw)', '    incoming, previous = load_inputs(raw)'),
        ('    run = DesignRun(incoming, args, modules, started)',
         '    run = DesignRun(incoming, args, modules, started)\n    retain_prior(run, previous)'),
        ("'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),",
         "'source_sha256': entry_sha, 'full_original_solver_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"),
        ("'complete_scientific_input': incoming,", "'complete_scientific_input': incoming, 'actual_transport_including_original_terminal': json.loads(raw),"),
        ("'actual_initial_accepted_steps': 0", "'actual_initial_accepted_steps': run.accepted_steps"),
        ('if run.current is not None and (failure', 'if run.current is not None and not run.restoring and (failure'),
        ('    literal = json.dumps(final,', '    extend_final(final, run)\n    literal = json.dumps(final,'),
    )
    for old, new in changes:
        if source.count(old) != 1:
            raise ValueError('bound R631 source does not have its unique continuation hook')
        source = source.replace(old, new)
    return source


def main():
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('all R631 scientific work requires the declared public Actions repository')
    raw = PREVIOUS.read_bytes()
    if digest(raw) != PREVIOUS_SHA:
        raise ValueError('original R631 all-row solver differs')
    global driver
    driver = types.ModuleType('r631_b7e0_frozen_driver')
    driver.__file__ = str(PREVIOUS)
    driver.__dict__.update(entry_sha=digest(Path(__file__).read_bytes()), restore=restore, restored_checkpoint=restored_checkpoint,
        load_inputs=load_inputs, retain_prior=retain_prior, extend_final=extend_final)
    exec(compile(amended_entry(raw.decode()), str(PREVIOUS), 'exec'), driver.__dict__)
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
