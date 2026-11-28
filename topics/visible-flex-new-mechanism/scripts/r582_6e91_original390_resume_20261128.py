#!/usr/bin/env python3
"""Continue actual6e91 on the original proposed390 complete row library.

The original physical solver and every acceptance rule are reused verbatim.
The already rejected raw/half-step are retained as source evidence; the new
optimizer initializes from the accepted physical q, whose new fine grid must
receive its own qualification. No old rejected scan is replayed as a test.
"""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT_SHA256 = '863ef47bb48ebf6ac02ccb9de808c90d30c89c7b69adf10d4ee64b07cef6bfbe'
PARENT_REQUEST_SHA256 = '79a17e7a7aab2673d31c23252f60d447c802e47175398895115d2ba0d379de1a'
INPUT_SHA256 = 'a21bc8e922a79c0831fc9f5f06adae95bc489c739a349993aec9193a2f8f4045'
FINAL_SHA256 = '360c099eb99cb74b6671c9319b5d2fdd47a77cc95c4ec51f671956a4835424f3'
if hashlib.sha256((HERE/'r582_e781_original383_resume_20261128.py').read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('the published original383 source differs')
import r582_e781_original383_resume_20261128 as parent

driver = parent.driver
SCHEMA = 'r582-actual6e91-original390-continuation-v1'
INPUT_SCHEMA = 'r582-6e91-required-terminal-input-v1'
original_emit = driver.emit


def load_input(raw, digest):
    encoded = sys.stdin.buffer.read() if raw == '@stdin' else raw.encode()
    if hashlib.sha256(encoded).hexdigest() != digest or digest != INPUT_SHA256:
        raise ValueError('the required actual6e91 terminal input differs')
    incoming = json.loads(encoded)
    if incoming['schema'] != INPUT_SCHEMA:
        raise ValueError('wrong actual6e91 terminal input schema')
    previous_path = HERE.parent/'computations/request-r582-e781-original383-20261128.json'
    previous_bytes = previous_path.read_bytes()
    if hashlib.sha256(previous_bytes).hexdigest() != PARENT_REQUEST_SHA256:
        raise ValueError('the published original383 request differs')
    previous = json.loads(previous_bytes)['lanes']['actuale781-original383']['source_state_json']
    source, paid, oldfine = parent.load_input(previous, hashlib.sha256(previous.encode()).hexdigest())
    state, origin = incoming['terminal_state'], incoming['origin']
    if (origin['run_id'] != 46121523891 or origin['job_id'] != 140906911350
            or origin['source_commit'] != '60cdf0c3f928294bd0adc2db3df6cdd8165785e8'
            or origin['source_entry_sha256'] != PARENT_SHA256
            or origin['FINAL_JSON_sha256'] != FINAL_SHA256
            or state['source_schema'] != parent.SCHEMA
            or state['stage'] != 0 or state['phase'] != 'metric'
            or state['termination'] != 'scientific_clock_checkpoint_not_complete'
            or state['stalled_outer_count'] != 0):
        raise ValueError('source terminal provenance or actual phase differs')
    actual = driver.np.asarray(state['actual_constraint_radial_nodes'], dtype=float)
    fine = driver.np.asarray(state['actual_fine_radial_nodes'], dtype=float)
    proposed = driver.np.asarray(state['proposed_constraint_radial_nodes'], dtype=float)
    pending = driver.np.asarray(state['pending_radial_nodes'], dtype=float)
    retained = state['actual_retained_state']
    if (len(actual) != 385 or len(fine) != 16290 or len(proposed) != 390
            or not set(actual).issubset(set(proposed))
            or set(proposed)-set(actual) != set(pending)
            or not set(oldfine).issubset(set(fine))
            or not set(actual).issubset(set(fine))
            or state['actual_constraint_theta_nodes'] != 1536
            or state['actual_fine_theta_nodes'] != 3072
            or state['proposed_constraint_theta_nodes'] != 1536
            or state['pending_angular_upgrade'] or state['pending_angular_upgrade_evidence']
            or state['actual_backend_trust'] != 2. or state['proposed_next_trust'] != 2.
            or retained['q_identity'] != driver.identity(retained['q'])
            or retained['q_identity']['binary64_sha256'] !=
                '6e91b58d61b2535ea4e262950d2177310a53ceb7fc50e87869d38e639949a334'
            or not retained['qualified_on_this_fine_grid'] or retained['p'] != .181
            or retained['scan']['radial_grid_identity'] != driver.identity(fine)
            or not retained['scan']['complete_fine_scan']
            or retained['scan']['eta_max'] != 3.3050334486861566e-5
            or retained['scan']['geometry_violation_max'] != 0.
            or retained['scan']['working_geometry_violation_max'] != 1.1922296396654763e-10
            or state['source_actual_material_mesh_sha256'] !=
                '0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'):
        raise ValueError('actual accepted point or complete original library differs')
    raw_trial, rejected = incoming['last_raw_backend_callback'], incoming['last_rejected_complete_trial']
    if (raw_trial['q_identity'] != driver.identity(raw_trial['q'])
            or raw_trial['q_identity']['binary64_sha256'] !=
                '5cf6911a6a3fc3b80b4ddccfc6239b93052d9c49703e3cdfb230f8b2f2dafc0d'
            or raw_trial['current_complete_backend_feasible']
            or rejected['q_identity'] != driver.identity(rejected['q'])
            or rejected['q_identity']['binary64_sha256'] !=
                'a9384a54438cba0462e5b2de32c22a5ac2b73867f0925c56cd3caa4cbd3910e1'
            or rejected['accepted_as'] != 'not_accepted'
            or not rejected['scan']['complete_fine_scan']
            or rejected['scan']['working_geometry_violation_max'] != 8.946709917348125e-7):
        raise ValueError('the actual previously rejected raw and physical half-step differ')
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        source_qualified_fine_identity=dict(retained['scan']['radial_grid_identity']),
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    ledger = incoming['new_terminal_cost_ledger']
    if (ledger['new_scientific_seconds'] != 2515.759658948
            or ledger['counts']['accepted_metric'] != 4
            or ledger['counts']['accepted_geometry_restoration'] != 1
            or ledger['counts']['completed_backend_Jacobians'] != 3
            or ledger['current_backend_cost_not_yet_folded_into_completed_outers']['complete_Jacobians'] != 8
            or ledger['counts']['complete_fine_scans'] != 14):
        raise ValueError('complete and unclosed original383 costs differ')
    source['resume97_origin'], source['resume97_state'] = origin, state
    source['resume97_input_sha256'] = digest
    source['prior_cost_ledger']['physical_original383_terminal'] = ledger
    source['previous_known_rejected_raw_and_half_step'] = {
        'raw':raw_trial, 'rejected_complete_trial':rejected,
        'not_used_as_new_optimizer_initializer_or_independent_diagnostic':True}
    # This is the original driver's initializer slot, not a claim that this
    # new initializer was the preceding backend's raw point. The actual q is
    # unchanged; the original complete new baseline and row tests still run.
    source['unqualified_warm_backend_trial'] = {
        'p':retained['p'], 'q':retained['q'], 'q_identity':retained['q_identity'],
        'backend_extra':retained['scan']['eta_max']+1.e-9,
        'scientific_source_kind':'accepted_physical6e91_with_original_fine_metric_epigraph',
        'is_previous_raw_backend_point':False,
        'original_source_fine_qualification_retained':True,
        'new390_rows_and16296_fine_still_require_actual_original_tests':True}
    return source, paid, fine


def emit(tag, value):
    if tag == 'FINITE_LOCAL_TAIL_DEFINITION':
        value = dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed',
                    'source_warm_trial_has_no_fine_or_geometry_qualification',
                    'original_source_unadopted_proposal'):
            value.pop(key, None)
        value.update(schema=SCHEMA, original_source_actual_grid=[385,1536],
            first_new_grid=[390,1536], all_source16290_fine_radial_locations_preserved=True,
            new_scope='accepted6e91 initialization and full original390 solve; no replay of rejected raw/half-step',
            source_initializer_is_real_accepted6e91_not_the_previous_raw_callback=True,
            source11_complete_Jacobians143_direction_blocks60_values_retained=True,
            source14_full_fine_scans_not_replayed_as_new_results=True,
            new_six_midpoints_require_new_original_complete_fine_qualification=True,
            source_actual2515_759658948_seconds_including_budget_overshoot_retained=True,
            actual_new_material_identity_recorded_without_relabelling=True,
            original_physical_solver_and_stage_acceptance_unchanged=True)
    original_emit(tag, value)


def main():
    driver.load_input = load_input
    driver.emit = emit
    driver.SCHEMA = SCHEMA
    driver.main()


if __name__ == '__main__':
    main()
