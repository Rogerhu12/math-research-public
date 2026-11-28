#!/usr/bin/env python3
"""Continue the actual d76 state and its distinct unfinished ada2 assessment."""
import hashlib
import json
import os
from pathlib import Path
import sys

if (os.environ.get('GITHUB_ACTIONS')!='true' or
        os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
    raise SystemExit('Scientific execution belongs to the public repository Actions')

HERE=Path(__file__).resolve().parent
PARENT_SOURCE=HERE/'r582_6236_material416_resume_20261128.py'
PARENT_REQUEST=HERE.parent/'computations/request-r582-6236-material416-20261128.json'
PARENT_SHA='8cd16f2d637e2dd1ed14ad47b722f8db7d825e6f98a1572f6944a16e64ef099e'
PARENT_REQUEST_SHA='265393de102d5f0bed469c9fda316e515e5de906815cc0e113f0305a98318d4d'
INPUT_SHA='9c4332b170d113d35fbabb84d94a71b585a55de30b1cf18db5c26ae825f16345'
INPUT_BYTES=337716
MATERIAL_SHA='0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'
SCHEMA='r707-actuald76-original419-with-paid-fine-prefix-storage-v1'
INPUT_SCHEMA='r707-actual416-d76-and-separate-unfinished-ada2-v1'
if hashlib.sha256(PARENT_SOURCE.read_bytes()).hexdigest()!=PARENT_SHA:
    raise RuntimeError('The actual completed original416 source differs')
import r582_6236_material416_resume_20261128 as parent
import r582_material_qualified_resume_guard_20261128 as material_guard
from r707_paid_peak_summary import install

driver=parent.driver
original_emit=driver.emit
save_prefix=install(driver)
pending_identity=None


def load_input(raw,digest):
    global pending_identity
    encoded=sys.stdin.buffer.read() if raw=='@stdin' else raw.encode()
    if (len(encoded)!=INPUT_BYTES or hashlib.sha256(encoded).hexdigest()!=digest or
            digest!=INPUT_SHA):
        raise ValueError('The actual original416 terminal input differs')
    incoming=json.loads(encoded)
    if incoming['schema']!=INPUT_SCHEMA:
        raise ValueError('Unexpected actual d76 continuation input')
    previous=PARENT_REQUEST.read_bytes()
    if hashlib.sha256(previous).hexdigest()!=PARENT_REQUEST_SHA:
        raise ValueError('The actual original416 request differs')
    previous=json.loads(previous)['lanes']['actual6236-material416']['source_state_json']
    source,paid,oldfine=parent.load_input(previous,hashlib.sha256(previous.encode()).hexdigest())
    state,origin=incoming['terminal_state'],incoming['origin']
    rec=state['actual_retained_state']
    actual=driver.np.asarray(state['actual_constraint_radial_nodes'],float)
    fine=driver.np.asarray(state['actual_fine_radial_nodes'],float)
    proposed=driver.np.asarray(state['proposed_constraint_radial_nodes'],float)
    if (origin['run_id']!=46145574830 or origin['job_id']!=140980768950 or
            origin['source_commit']!='5ad49e323dc0033f126a65087cfb93b86a7a14fc' or
            origin['source_entry_sha256']!=PARENT_SHA or origin['request_sha256']!=PARENT_REQUEST_SHA or
            origin['FINAL_JSON_sha256']!='661c3a1a269d0c3b197dc63617731cd91e8e262d2a30e1ac7c6a6a204a51425f' or
            state['source_schema']!=parent.SCHEMA or state['stage']!=0 or state['outer']!=0 or
            state['phase']!='metric' or state['stalled_outer_count']!=0 or
            state['termination']!='scientific_clock_checkpoint_not_complete'):
        raise ValueError('The actual original416 origin or unfinished outer differs')
    if (len(actual)!=416 or len(proposed)!=419 or len(fine)!=16337 or
            not set(actual).issubset(set(proposed)) or
            set(proposed)-set(actual)!=set(state['pending_radial_nodes']) or
            len(state['pending_radial_nodes'])!=3 or not set(oldfine).issubset(set(fine)) or
            state['actual_constraint_theta_nodes']!=1536 or state['proposed_constraint_theta_nodes']!=1536 or
            state['actual_fine_theta_nodes']!=3072 or state['pending_angular_upgrade'] or
            state['pending_angular_upgrade_evidence'] or state['actual_backend_trust']!=2. or
            state['planned_current_trust']!=2. or state['proposed_next_trust']!=2. or
            rec['q_identity']!=driver.identity(rec['q']) or
            rec['q_identity']['binary64_sha256']!='d76ee2f0f2f29e1c81fcdae2fd4cc2da42c704398a67f9de2d682220a1b1119f' or
            rec['p']!=.181 or not rec['qualified_on_this_fine_grid'] or not rec['scan']['complete_fine_scan'] or
            rec['scan']['radial_grid_identity']!=driver.identity(fine) or rec['scan']['theta_nodes']!=3072 or
            rec['scan']['working_geometry_violation_max']>1.e-8 or
            rec['fine_qualification_material_knots_and_jets_sha256']!=MATERIAL_SHA):
        raise ValueError('Retained d76, actual old qualification, or proposed419 row library differs')
    raw_trial=incoming['last_raw_backend_callback']
    complete=incoming['last_completed_full_scan_trial']
    partial=incoming['actual_unfinished_separate_assessment']
    if (driver.identity(raw_trial['q'])!=raw_trial['q_identity'] or
            raw_trial['q_identity']['binary64_sha256']!='e8d791e815c373111a774c14001145ab863da8c9ad3b6822171e69d7d2d7fed7' or
            raw_trial['complete_fine_assessment'] or raw_trial['current_complete_backend_feasible'] or
            driver.identity(complete['q'])!=complete['q_identity'] or
            complete['q_identity']['binary64_sha256']!='b0d7f899d3630393a56ed8fca25b7f42f45ddb18cc105aff8f77eab7cd397018' or
            complete['accepted_as']!='not_accepted' or not complete['scan']['complete_fine_scan'] or
            driver.identity(partial['q'])!=raw_trial['separate_assessment_q_identity'] or
            partial['q_identity']!=raw_trial['separate_assessment_q_identity'] or
            partial['q_identity']['binary64_sha256']!='ada2ef6eabd777255db1e8e70bba4a1b1d03c3595f76e0e6ba42d7376162ac1f' or
            partial['completed_prefix_blocks']!=126 or partial['completed_prefix_radial_points']!=16128 or
            partial['actual_arrays_available'] or partial['qualified_or_accepted']):
        raise ValueError('Raw e8, rejected b0d7, and unfinished ada2 were conflated')
    rebuilt=driver.np.asarray(rec['q'])+.5*(driver.np.asarray(raw_trial['q'])-driver.np.asarray(rec['q']))
    if driver.identity(rebuilt)!=partial['q_identity']:
        raise ValueError('The literal original physical half-step no longer reconstructs ada2')
    state.update(actual_constraint_radial_identity=driver.identity(actual),
        actual_fine_radial_identity=driver.identity(fine),
        source_qualified_fine_identity=rec['scan']['radial_grid_identity'],
        paid_97q_directional_check=source['resume97_state']['paid_97q_directional_check'])
    source['resume97_origin'],source['resume97_state']=origin,state
    source['resume97_input_sha256']=digest
    source['prior_cost_ledger']['r707_actual416_terminal']=incoming['new_terminal_cost_ledger']
    source['original416_last_rejected_complete_trial']=complete
    source['original416_actual_unfinished_separate_assessment']=partial
    source['unqualified_warm_backend_trial']=raw_trial
    # This raw callback has an UNFINISHED separate assessment. Unlike the
    # earlier completed6236 half-step, it must be adjudicated on the new rows.
    source['skip_completed_source_warm_trial']=False
    pending_identity=dict(p=.181,q_identity=partial['q_identity'],fine_radial_identity=driver.identity(fine),
                          fine_theta_nodes=3072,material_sha256=MATERIAL_SHA)
    return source,paid,fine


def emit(tag,value):
    if tag=='FINITE_LOCAL_TAIL_DEFINITION':
        value=dict(value)
        for key in ('source_49_backend_callbacks_are_not_replayed','original_source_unadopted_proposal'):
            value.pop(key,None)
        value.update(schema=SCHEMA,original_source_actual_grid=[416,1536],
            first_new_grid=[419,1536],actual_source_fine_grid=[16337,3072],
            new_scope='Retained d76; three paid new rows, distinct unfinished ada2 and exact paid peak storage',
            last_rejected_b0d7_not_promoted=True,last_raw_e8_not_promoted=True,
            old_ada2_126_prefix_blocks_unavailable_not_fabricated=True,
            new_grid_changes_global_tail_primitive_quadrature_partition=True,
            no_old_fine_summary_merged_into_a_different_numeric_primitive=True,
            necessary_new_material_and_tail_and_J_reconstruction_charged=True,
            original_physical_rows_and_solver_and_acceptance_thresholds_unchanged=True,
            compact_peak_summaries_preserve_all_original_peak_decisions=True)
    if tag=='FINITE_LOCAL_TAIL_FINAL':
        value=dict(value,paid_fine_prefix_artifact=save_prefix('r707-paid-fine-prefix.json.gz'),
            original_ada2_pending_identity=pending_identity,
            original_ada2_missing_prefix_debt_not_erased_by_new_partition=True)
    original_emit(tag,value)


def main():
    material_guard.run(driver,load_input,emit,SCHEMA,qualified_source_material_sha256=MATERIAL_SHA)


if __name__=='__main__':
    main()
