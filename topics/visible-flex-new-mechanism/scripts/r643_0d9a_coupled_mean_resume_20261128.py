#!/usr/bin/env python3
"""Complete the saved R643 quarter step and continue the same fixed-E full 1566-column system."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import textwrap
import types


HERE = Path(__file__).resolve().parent
PREVIOUS = HERE / 'r643_actual397_coupled_mean_20261128.py'
PREVIOUS_SHA = '94b5eeab0f08a174c9df981de5a12b7e95e16e201188cb8964b94e28fd2ba4f0'
REQUEST = HERE.parent / 'computations/request-r643-actual397-coupled-mean-20261128.json.gz'
REQUEST_SHA = '7945c8d80b487c4789a7f5774eb0879cf0834ffe7c737e7e4d4d52278074d036'
CONTRACT_SHA = 'a91b811ec60787dba772b233e52160e71054c76d6d6730b79753efcc6b84a011'
FINAL_SHA = 'ccae718f0b0dea2f7ee8f81978bd2bab0a7c9df0e1831f0e4107b6436af78943'
Q_SHA = '0d9a753f09f33fadd88b838c4dd3eddccb2830567050d391d0824e2ab54e7e16'
TRIAL_SHA = 'd1f8e7918fedaa696490a5724ba38e9013702dd25c84abda4f98e5add0e5b229'
TARGET = '86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5'
MODEL = '0394f785ff395a38929d5ef82749fe8523cf24e8719ecdc907759ab1664d122b'
INPUT_SHA = 'c718d88754ca1d2114b51d67a43d813831481fa433938775876d0f0f3b5b3475'
SCHEMA = 'r643-0d9a-complete-pending-quarter-step-same-E-v1'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def literal(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def load_inputs(raw):
    if digest(raw) != INPUT_SHA or digest(REQUEST.read_bytes()) != REQUEST_SHA:
        raise ValueError('R643 prior request or actual transported bytes differ')
    request = json.loads(gzip.decompress(REQUEST.read_bytes()))
    contract = request['lanes']['r643-actual397-coupled-mean']['source_state_json'].encode()
    transfer = json.loads(raw)
    incoming = json.loads(contract)
    prior = transfer.pop('original_final_except_bound_centered_receipt_and_duplicate_q')
    if ('preceding_centered_complete_actual_receipt_not_counted_as_new' in prior or 'actual_response' in prior):
        raise ValueError('the two omitted original fields must come from their bound sources')
    prior['preceding_centered_complete_actual_receipt_not_counted_as_new'] = json.loads(
        incoming['preceding_centered_natural_terminal']['literal_FINAL_JSON'])
    prior['actual_response'] = prior['actual_current_checkpoint']['actual_response']
    transfer['original_final'] = prior
    cp, pending = prior['actual_current_checkpoint'], prior['pending_trial_not_accepted']
    if (digest(contract) != CONTRACT_SHA or transfer['schema'] != SCHEMA
            or digest(literal(prior)) != FINAL_SHA or prior['failure']['type'] != 'RuleChange'
            or prior['actual_new_accepted_steps'] != 2 or cp['actual_new_accepted_steps'] != 2
            or cp['actual_response'] != prior['actual_response'] or len(cp['actual_response']) != 1566
            or digest(literal(cp['actual_response'])) != Q_SHA or cp['response_identity']['sha256'] != Q_SHA
            or cp['same_frozen_target_sha256'] != TARGET or cp['joint_model_sha256'] != MODEL
            or cp['hard_tau'] != 1 or cp['actual_next_damping'] != 1.111111111111111e-9
            or cp['actual_next_damping'] != prior['actual_next_damping']
            or pending['cut'] != 2 or pending['iteration'] != 2 or pending['grid'] != 'work'
            or pending['damping_trial'] != 0 or pending['fraction'] != .25
            or pending['predicted_decrease'] != 2.5094163732265944e-8
            or digest(literal(pending['actual_proposed_response'])) != TRIAL_SHA
            or pending['actual_proposed_response_identity']['sha256'] != TRIAL_SHA
            or transfer['accepted_tail_receipt']['actual_response_sha256'] != Q_SHA
            or transfer['accepted_tail_receipt']['joint_model_sha256'] != MODEL
            or transfer['accepted_tail_receipt']['same_target_sha256'] != TARGET
            or transfer['paid_direction']['iteration'] != 2 or transfer['paid_direction']['damping_trial'] != 0
            or transfer['paid_direction']['damping'] != prior['actual_next_damping']
            or prior['complete_final_readout'] is not None or prior['partial_readout'] is not None):
        raise ValueError('the exact R643 accepted work coordinate, pending trial or paid model differs')
    incoming['schema'] = SCHEMA
    return incoming, transfer


def retain_prior(run, transfer):
    previous = transfer['original_final']
    run.transfer = transfer
    run.record = previous['actual_current_checkpoint']
    run.response = driver.np.asarray(run.record['actual_response'], dtype=float)
    run.accepted = previous['actual_new_accepted_steps']
    run.history = list(previous['accepted_history'])
    run.damping = previous['actual_next_damping']
    run.pending = previous['pending_trial_not_accepted']
    run.last_trial = previous['last_actual_trial']
    run.accepted_tail = transfer['accepted_tail_receipt']
    run.current_tail_extension = None
    run.restored = False
    run.work_iteration = 2
    run.previous_cut_resolved = False


def resolve_prior(run, data, state):
    cp = run.record
    obs = cp['last_complete_field_observation']
    run.model._require(run.response, data, state)
    if (driver.sha(run.response.tolist()) != Q_SHA or run.model.model_sha256 != MODEL
            or run.identity.target_sha256 != TARGET or not driver.np.array_equal(data['r'], run.model.original_work_radii)
            or len(data['r']) != obs['radial_points'] or len(data['theta']) != obs['angular_points']
            or len(state['residual']) != obs['all_actual_rows'] or run.model.nq != obs['all_actual_free_columns']
            or run.accepted_tail['old_source_error_accounting'] != run.tail.contract['source_error_accounting']):
        raise ValueError('the same frozen work field, complete response and source-error ledger are required')
    run.restored = True
    driver.emit('RESTORED', {'actual_response_sha256': Q_SHA, 'actual_pending_response_sha256': TRIAL_SHA,
        'same_frozen_target_sha256': TARGET, 'joint_model_sha256': MODEL,
        'old_accepted_work_observation': obs,
        'rebuilt_current_merit': float(state['residual']@state['residual']/2),
        'previous_accepted_steps': run.accepted, 'previous_next_damping': run.damping})
    pending = run.pending
    proposed = driver.np.asarray(pending['actual_proposed_response'], dtype=float)
    try:
        accepted = driver.finish_saved_trial(run, data, state, proposed, pending['predicted_decrease'],
            run.damping, pending['grid'], pending['iteration'], run.transfer['paid_direction']['function_measures'])
    except Exception:
        if run.accepted == cp['actual_new_accepted_steps']:
            run.pending = pending
        raise
    run.previous_cut_resolved = True
    if accepted:
        run.work_iteration = 3


def compare_rebuilt_direction(run, label, iteration, dtrial, limit, direction, measures, factor):
    if (label, iteration, dtrial) != ('work', 2, 0) or not run.previous_cut_resolved:
        return -1
    old = run.transfer['original_final']['pending_trial_not_accepted']
    fraction = limit*2.**(-old['cut'])
    proposed = run.response+fraction*direction
    prediction = factor.predicted_decrease(direction, fraction)
    previous = run.transfer['original_final']
    half = previous['last_actual_trial']
    half_fraction = limit*2.**(-half['cut'])
    half_sha = driver.sha((run.response+half_fraction*direction).tolist())
    same = (fraction == old['fraction'] and driver.sha(proposed.tolist()) == TRIAL_SHA
            and prediction == old['predicted_decrease']
            and half_fraction == half['fraction'] and half_sha == half['actual_proposed_response_identity']['sha256']
            and factor.predicted_decrease(direction,half_fraction) == half['predicted_decrease']
            and measures == run.transfer['paid_direction']['function_measures']
            and run.last_spectrum == previous['last_complete_full_spectrum']
            and run.rebuilt_base_matches_previous)
    driver.emit('REBUILT_DIRECTION', {'same_previous_quarter_trial_and_prediction': same,
        'actual_quarter_response_sha256': driver.sha(proposed.tolist()), 'previous_quarter_response_sha256': TRIAL_SHA,
        'previous_quarter_prediction': old['predicted_decrease'], 'new_quarter_prediction': prediction})
    return 2 if same else -1


def consume_tail(run):
    """Use one actual existing tail and current paid receipt; each derivative consumer runs once."""
    run.check()
    import r650_complete_mean_true_tail_curvature_20261128 as third
    paid = run.accepted_tail
    q = run.response
    if paid['actual_response_sha256'] != driver.sha(q.tolist()):
        raise ValueError('the current full response has no matching paid R643 tail receipt')
    result = {'actual_response_sha256': paid['actual_response_sha256'],
              'source_error_accounting': run.tail.contract['source_error_accounting'],
              'original_R643_tail_receipt_sha256': driver.sha(paid)}
    run.current_tail_extension = result
    curvature = None
    try:
        connection = third.connection.CompleteTrueTailConnection(run.tail)
        result['R648'] = connection.evaluate(q, paid)
        run.check()
        curvature = third.CompleteTrueTailCurvature.__new__(third.CompleteTrueTailCurvature)
        curvature.__init__(connection)
        result['R650'] = curvature.evaluate(q, paid, result['R648'])
    finally:
        result['R648_counts'] = dict(third.connection.COUNTS)
        result['R650_counts'] = dict(getattr(curvature, 'counts', {}))
        result['R649_counts'] = dict(third.curvature.COUNTS)
        result['extension_underlying_source_arithmetic_counts'] = dict(third.paid.COUNTS)
        result['extension_underlying_interval_bounds_counts'] = dict(third.bounds.COUNTS)


def record_extension(run):
    try:
        consume_tail(run)
    except Exception as exc:
        run.failure_history.append({'attempt':'same_existing_tail_R648_R650_derivative_bounds',
            'failure_type':type(exc).__name__, 'message':str(exc), 'all_partial_bounds_and_costs_retained':True})
    driver.emit('SAME_OBJECT_TAIL_EXTENSION',run.current_tail_extension)


def extend_final(final, run):
    prior = run.transfer['original_final']
    inherited_already_present = {'actual_response', 'actual_current_checkpoint', 'pending_trial_not_accepted',
        'preceding_centered_complete_actual_receipt_not_counted_as_new',
        'older_reference_cost_ledger_not_counted_as_new', 'older_prior_cost_ledgers_not_counted_as_new'}
    final['preceding_R643_terminal_except_vectors_and_already_inherited_ancestors'] = {
        k: v for k,v in prior.items() if k not in inherited_already_present}
    final['preceding_R643_origin'] = {k:v for k,v in run.transfer.items()
        if k not in ('original_final','paid_direction','accepted_tail_receipt')}
    final['old_accepted_and_pending_vector_sha256_in_bound_request'] = [Q_SHA,TRIAL_SHA]
    final['previous_R643_accepted_steps'] = prior['actual_new_accepted_steps']
    final['actual_total_accepted_steps'] = run.accepted
    final['actual_new_accepted_steps'] = run.accepted-prior['actual_new_accepted_steps']
    final['prior_quarter_trial_resolved'] = run.previous_cut_resolved
    final['current_accepted_tail_receipt'] = run.accepted_tail
    final['same_object_R648_R650_true_tail_extension'] = run.current_tail_extension


def amend(source):
    # Lift exactly the original nonlinear evaluation and acceptance statements for
    # the one in-flight proposal. Its direction, predicted decrease and q are paid.
    start = "                    COUNTS['actual_coupled_nonlinear_trials_attempted'] += 1"
    end = "                    REJECTIONS[reason] += 1"
    trial = textwrap.dedent(source[source.index(start):source.index(end)+len(end)])
    trial = trial.replace("COUNTS['actual_coupled_nonlinear_trials_attempted'] += 1",
                          "COUNTS['old_inflight_trial_full_joint_evaluation_restarted'] += 1")
    # The former run completed this tail, but did not serialize its receipt.
    # A rejection needs no receipt. An acceptance regenerates it once for the
    # same q, before changing the current accepted coordinate.
    trial = trial.replace('candidate_tail = self.tail.evaluate(proposed)', 'candidate_tail = None')
    trial = trial.replace('if okay:\n', 'if okay:\n    candidate_tail = self.tail.evaluate(proposed)\n    self.accepted_tail = candidate_tail\n')
    trial = trial.replace('    accepted = True\n    break','    return True')
    helper = ('\ndef finish_saved_trial(self, data, state, proposed, predicted, damping, label, iteration, measures):\n'
              "    base_merit = float(state['residual']@state['residual']/2)\n"
              "    self.rebuilt_base_matches_previous = base_merit == self.record['last_complete_field_observation']['complete_joint_merit']\n"
              +textwrap.indent(trial,'    ')+'\n    return False\n')
    initial = source[source.index('        initial_tail = self.tail.evaluate(self.response)'):
                     source.index("        work_status = self.solve_current_grid")]
    changes = (
        ('    incoming = json.loads(raw)','    incoming, transfer = load_inputs(raw)'),
        ('    run = CoupledRun(incoming,args,modules,started)',
         '    run = CoupledRun(incoming,args,modules,started)\n    retain_prior(run, transfer)'),
        ("'complete_actual_input':incoming,", "'complete_actual_input':incoming,'actual_resume_input':json.loads(raw),"),
        ('        self.response = self.model.initial_response()','        # Actual accepted response is already restored from complete FINAL.'),
        (initial, '        state = self.model.evaluate(self.response,data)\n        self.current = (data,state)\n        resolve_prior(self, data, state)\n'),
        ("for iteration in range(int(params['maximum_iterations_per_grid'])):",
         "for iteration in range(self.work_iteration if label=='work' else 0, int(params['maximum_iterations_per_grid'])):"),
        ("                for cut in range(int(params['line_search_cuts'])):",
         "                skip = compare_rebuilt_direction(self,label,iteration,dtrial,limit,direction,measures,factor)\n                for cut in range(skip+1, int(params['line_search_cuts'])):"),
        ('                        self.response,self.current = proposed,(data,candidate)',
         '                        self.accepted_tail = candidate_tail\n                        self.response,self.current = proposed,(data,candidate)'),
        ("'actual_true_tail':self.tail.evaluate(self.response)", "'actual_true_tail':self.accepted_tail"),
        ('    if run.current is not None and not run.rules.failed:',
         '    if run.current is not None and run.restored and not run.rules.failed:\n        record_extension(run)'),
        ('    literal = json.dumps(final,','    extend_final(final,run)\n    literal = json.dumps(final,'),
    )
    for old,new in changes:
        if source.count(old) != 1:
            raise ValueError('the frozen R643 driver lacks its unique continuation seam')
        source = source.replace(old,new)
    return source+helper


def main():
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('scientific continuation requires the public R643 Actions repository')
    raw = PREVIOUS.read_bytes()
    if digest(raw) != PREVIOUS_SHA:
        raise ValueError('original R643 full physical solver differs')
    global driver
    driver = types.ModuleType('r643_0d9a_frozen_driver')
    driver.__file__ = str(PREVIOUS)
    driver.__dict__.update(load_inputs=load_inputs, retain_prior=retain_prior, resolve_prior=resolve_prior,
        compare_rebuilt_direction=compare_rebuilt_direction, record_extension=record_extension, extend_final=extend_final)
    exec(compile(amend(raw.decode()),str(PREVIOUS),'exec'),driver.__dict__)
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
