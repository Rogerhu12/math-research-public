#!/usr/bin/env python3
"""Same full-S solver from actual457 with its one paid fine peak added.

The immutable checkpoint reader and explicit work-radius exchange are new.
The entire published full-S model, analytic Jacobian, complete-row QR/SVD,
direction/line search, all original meshes and actual terminal readout are
called directly from their hash-bound original driver. No numerical method
is copied, modified, or executed by importing this source locally.

No QR/BFGS/internal linear factor was saved by the preceding scope. This
resume restores the actual accepted1130q, amplitude and next damping only,
then performs the next necessary ordinary solve. Previously paid fine or
direction diagnostics are not run as a new entry gate.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
DRIVER_FILE = 'r613_full_position_height_20261127.py'
DRIVER_SHA = '6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0'
PREVIOUS_INPUT_SHA = '79e6d6ce708687decd47fb8eb7a9668f8ca2ebf2351b2f3109fd571c6d692f9c'
RECONSTRUCTION_SHA = '14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee'
SOURCE_Q_SHA = 'a05c4374fe966df1982ae2f3fc5a92129aba03da562670fc848d4a666600b539'
SCHEMA = 'r613-actual457-paid-fine-peak-full-position-exchange-v1'


def load_original_driver():
    path = HERE / DRIVER_FILE
    if hashlib.sha256(path.read_bytes()).hexdigest() != DRIVER_SHA:
        raise RuntimeError('published complete actual-position driver changed')
    spec = importlib.util.spec_from_file_location('r613_bound_complete_position_resume',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_actual457(args,driver):
    raw = (sys.stdin.buffer.read() if args.source_state_json == '@stdin'
           else args.source_state_json.encode())
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.source_state_sha256:
        raise ValueError('declared normal-resume input identity differs')
    source = json.loads(raw)
    origin = {
        'run_id':45909455678, 'job_id':140214007842,
        'source_commit':'12e47b06d7003b2df0a3c77be6d481b30cf226e9',
        'source_sha256':'bc4cf1bce2f62a67eac633deedf12a3fa9ba75b1758042b32c9354c87d802ff3',
        'raw_job_log_bytes':2465022,
        'raw_job_log_sha256':'6bfe702c7eabfed835ac19125364ad1c2328f8009770f37e97551fbbe08842ae',
        'FINAL_JSON_bytes':106832,
        'FINAL_JSON_sha256':'da0c9caaea414b6cfd392e2bed4d0665a3837b5d54c922fa5faacc05c14fefad',
        'kind':'actual_accepted_checkpoint_of_completed_full_position_scope'}
    if source['origin'] != origin:
        raise ValueError('actual completed original full-position origin differs')
    qtext = source['actual_1130q_JSON']
    if (len(qtext.encode()) != 22777 or source['actual_q_JSON_bytes'] != 22777
            or source['actual_q_JSON_sha256'] != SOURCE_Q_SHA
            or hashlib.sha256(qtext.encode()).hexdigest() != SOURCE_Q_SHA):
        raise ValueError('actual accepted iteration457 q JSON differs')
    q = driver.np.asarray(json.loads(qtext),dtype=float)
    if q.shape != (1130,) or not driver.np.all(driver.np.isfinite(q)):
        raise ValueError('complete original1130q is required')
    if driver.weak.identity(q) != source['actual_retained_q_identity']:
        raise ValueError('actual accepted q identity changed')
    amplitude = float(source['amplitude'])
    damping = float(source['actual_next_damping'])
    iteration = int(source['global_accepted_iteration'])
    if (amplitude != 1e-5 or damping != 1e-14 or iteration != 457
            or q[0] != .5188904014900897
            or source['input_is_actual_accepted_checkpoint'] is not True
            or source['original_source_status'] != 'declared_complete_position_iteration_limit'
            or source['saved_internal_QR_or_BFGS_restored'] is not False
            or source['previous_fine_or_direction_readout_replayed_as_entry_gate'] is not False):
        raise ValueError('actual continuation state or normal-resume contract changed')
    previous = source['previous_scope_input_JSON']
    if len(previous.encode()) != 157609 or hashlib.sha256(previous.encode()).hexdigest() != PREVIOUS_INPUT_SHA:
        raise ValueError('full original input, including all paid mouths and costs, differs')
    owner = json.loads(previous)
    while 'reconstruction_source_JSON' not in owner:
        owner = json.loads(owner['previous_scope_input_JSON'])
    inherited = owner['reconstruction_source_JSON']
    if len(inherited.encode()) != 31425 or hashlib.sha256(inherited.encode()).hexdigest() != RECONSTRUCTION_SHA:
        raise ValueError('same complete canonical field or original mouths changed')
    ledger = source['source_cost_ledger']
    if (ledger['run_id'] != 45909455678 or ledger['job_id'] != 140214007842
            or ledger['elapsed_seconds'] != 4768.702256165
            or ledger['new_complete_position_counts']['accepted_steps'] != 60
            or ledger['new_complete_position_counts']['rejected_steps'] != 42):
        raise ValueError('actual original cost ledger was lost or relabelled')
    exchange = source['paid_fine_peak_exchange']
    if (exchange['radii'] != [.32708333333333334]
            or exchange['source_fine_eta'] != 2.2449537902118403e-7
            or exchange['source_fine_eta_attainer'] != [.32708333333333334,4.135612204139688]
            or exchange['source_direct_h_eta_attainer'][0] != exchange['radii'][0]
            or exchange['source_direct_half_eta_attainer'][0] != exchange['radii'][0]
            or exchange['only_the_one_paid_fine_maximum_radius_is_added'] is not True
            or exchange['original_prepare_radial_dr_weights_recomputed_on_union'] is not True
            or exchange['original1728_fine_grid_unchanged'] is not True
            or exchange['old_fine_or_restriction_gate_replayed'] is not False):
        raise ValueError('the actual already-paid fine-maximum exchange differs')
    return source,json.loads(inherited),q,amplitude,damping,iteration,digest


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-state-json',required=True)
    parser.add_argument('--source-state-sha256',required=True)
    parser.add_argument('--maximum-seconds',type=float,default=5400.)
    parser.add_argument('--M',type=int,choices=[25],default=25)
    parser.add_argument('--rtol',type=float,default=2e-11)
    parser.add_argument('--atol',type=float,default=2e-13)
    parser.add_argument('--iterations',type=int,choices=[60],default=60)
    parser.add_argument('--theta-nodes',type=int,choices=[256],default=256)
    parser.add_argument('--target-eta',type=float,default=2e-9)
    parser.add_argument('--height-saturation',type=float,choices=[.15],default=.15)
    args=parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('science only in this declared public Actions scope')
    if not 600<=args.maximum_seconds<=5400 or args.rtol!=2e-11 or args.atol!=2e-13:
        raise ValueError('original declared tolerance or clock changed')
    driver=load_original_driver()
    source,reconstruction,q,amplitude,damping,first_iteration,input_sha=read_actual457(args,driver)
    started=time.monotonic();deadline=started+args.maximum_seconds
    solver_deadline=deadline-240.
    model=summary=readout=None
    attempts=[];exchange_receipt={'phase':'before_original_model_reconstruction'}
    status='actual457_before_necessary_reconstruction_and_paid_fine_peak_exchange'
    driver.emit('FULL_POSITION_DEFINITION',{
        'schema':SCHEMA,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_state_sha256':input_sha,'source_state':source,
        'arguments':{key:value for key,value in vars(args).items() if key!='source_state_json'},
        'actual_initial_q_identity':driver.weak.identity(q),
        'source_global_accepted_iteration':first_iteration,'actual_initial_damping':damping,
        'full_parameters':1130,'actual_accepted457_q_unchanged_on_input':True,
        'complete_working_odd_position_modes':driver.POSITION_ODD_MODES.tolist(),
        'full_output_rows_per_radius':2*len(driver.POSITION_ODD_MODES),
        'original_At_M_positive_readout_preserved':True,
        'all_original950_radial_points_and_every_span_retained':True,
        'only_additional_radius_is_actual_paid_fine_maximum':source['paid_fine_peak_exchange']['radii'],
        'original_prepare_radial_weights_recomputed_on_complete_union':True,
        'new_work_merit_not_mislabelled_as_original950_merit':True,
        'original_full_model_Jacobian_solve_QR_acceptance_and_fine_called_without_change':True,
        'original_canonical512_tanh_force_paid_mouths_and_full_core_preserved':True,
        'original_fine1728_and_shared_R606_R615_pass_unchanged':True,
        'no_old_fine_or_direction_or_inner_Riccati_gate':True,
        'source_and_prior_costs_preserved_not_counted_as_new':True,
        'separate_R618_actual397_fixed_target_not_changed':True,
        'fixed_g_or_README_completion_claim':False})
    try:
        model=driver.restore_model(reconstruction,args,deadline,attempts)
        model.actual_checkpoint={'q':q.copy(),'amplitude':amplitude,'iteration':first_iteration,
            'damping':damping,'status':'actual457_checkpoint_before_new_work_union_evaluation'}
        original_r=driver.compact.radial_grid(model,1)
        additional=np.asarray(source['paid_fine_peak_exchange']['radii'],dtype=float)
        exchange_receipt.update(phase='original_radial_mesh_formed',
            original_radius_count=int(len(original_r)),requested_paid_radii=additional.tolist())
        if (len(original_r)!=950 or additional.shape!=(1,)
                or np.any(additional<model.minimum*(1+1e-10))
                or np.any(additional>model.par.R-1e-7)):
            raise ValueError('same original950 domain or exact paid peak differs')
        r=np.unique(np.r_[original_r,additional])
        retained=np.isin(original_r,r)
        new_r=r[~np.isin(r,original_r)]
        exchange_receipt.update(phase='complete_union_formed',
            union_radius_count=int(len(r)),actual_new_radii=new_r.tolist(),
            all_original_radii_retained=bool(np.all(retained)),
            actual_all_original_rows_retained=int(128*len(original_r)),
            actual_full_position_rows=int(128*len(r)),
            actual_analytic_J_shape=[int(128*len(r)),1130],
            actual_raw_J_bytes_from_shape=int(128*len(r)*1130*8),
            exact_duplicate_radii_shared_without_dropping_any_old_row=True,
            original_prepare_dr_rule_used_on_union=True,
            actual_previous_fine_peak_not_reprobed_as_a_gate=True,
            previous950_merit_is_a_different_radial_quadrature_scalar=True)
        if not np.all(retained) or len(r)!=951 or new_r.tolist()!=additional.tolist():
            raise ValueError('the declared one-radius union did not retain every original row')
        data=model.prepare(r,args.theta_nodes)
        exchange_receipt.update(phase='actual_new_work_data_prepared',
            working_angle_count=int(len(data['theta'])),
            original_odd_modes=driver.POSITION_ODD_MODES.tolist())
        driver.emit('FULL_POSITION_PAID_FINE_PEAK_EXCHANGE',exchange_receipt)
        q,state,damping,summary=driver.solve(model,q,amplitude,damping,first_iteration,
            data,args,solver_deadline)
        status=summary['status']
        readout=driver.fine_readout(model,q,amplitude,args)
        driver.emit('FULL_POSITION_STAGE',{'summary':summary,'readout':readout,
            'actual_q_identity':driver.weak.identity(q),'actual_next_damping':damping,
            'paid_fine_peak_exchange':exchange_receipt})
    except (driver.weak.ScientificBudget,driver.paid.ScientificBudget,driver.high.HighModeBudget) as exc:
        status='declared_scientific_budget_actual_exchange_checkpoint'
        driver.emit('FULL_POSITION_CLOCK',{'message':str(exc),'actual_retained_state_preserved':True})
    except (driver.base.DomainError,ArithmeticError,ValueError,FloatingPointError,np.linalg.LinAlgError) as exc:
        status='declared_exchange_model_or_numerical_failure'
        driver.emit('FULL_POSITION_FAILURE',{'type':type(exc).__name__,'message':str(exc)})
    actual=pending=None
    if model is not None and model.actual_checkpoint is not None:
        keep=model.actual_checkpoint
        q=keep['q'].copy();amplitude=keep['amplitude'];damping=keep['damping']
        actual={key:value for key,value in keep.items() if key!='q'}
        if model.pending_trial is not None:
            pending={key:(value.tolist() if isinstance(value,np.ndarray) else value)
                for key,value in model.pending_trial.items()}
    final={'schema':SCHEMA,'status':status,'elapsed_seconds':time.monotonic()-started,
        'actual_retained_amplitude':amplitude,'actual_retained_q':q.tolist(),
        'actual_retained_q_identity':driver.weak.identity(q),'actual_next_damping':damping,
        'actual_complete_checkpoint':actual,'pending_trial_not_accepted':pending,
        'last_trial':None if model is None else model.last_trial,
        'model_constructed':model is not None,'summary':summary,'readout':readout,
        'paid_fine_peak_exchange':exchange_receipt,
        'paid_high_reconstruction_attempts':driver.full.attempt_receipts(attempts),
        'canonical_paid_tanh_mean_observations':None if model is None else model.canonical_mean_observations,
        'source_cost_not_counted_as_this_run':source['source_cost_ledger'],
        'earlier_cost_ledgers_not_counted_as_this_run':source['prior_cost_ledgers'],
        'new_complete_position_counts':dict(driver.NEW),
        'complete_row_QR_SVD_counts':dict(driver.factorization.COUNTS),
        'same_field_position_evaluation_counts':dict(driver.operator.NEW),
        'same_field_position_linearization_counts':dict(driver.position.COUNTS),
        'compact_basis_counts':dict(driver.compact.NEW),'parent_full_counts':dict(driver.full.NEW),
        'inherited_completed_height_counts':dict(driver.complete.COUNTS),
        'factored_evaluator_counts':dict(driver.high.COUNTS),
        'coefficient_majorant_counts':dict(driver.majorant.COUNTS),
        'base_counts':driver.base.COUNTS,'forced_counts':driver.paid.NEW_COUNTS,
        'function_counts':driver.parent.EXTRA,'gain_counts':driver.base.gain.COUNTS,
        'paid_mouth_and_position_counts':driver.resume.NEW,'old_weak_helper_counts':driver.weak.COUNTS,
        'rejections':driver.REJECTIONS,'overlapping_counters_not_disjoint_work':True,
        'new_DtN_inner_RHS':0,'old_direction_or_restriction_gate_replayed':False,
        'all_original950_work_points_and_all_original_fine1728_retained':True,
        'new_union_merit_not_compared_as_same_original950_quadrature':True,
        'separate_R618_actual397_fixed_target_not_changed':True,
        'continuous_metric_curvature_reach_or_README_completion_claim':False,
        'raw_arrays_artifacts_releases_or_git_writes':False}
    raw=json.dumps(final,sort_keys=True,separators=(',',':'),allow_nan=False)
    print('FULL_POSITION_FINAL '+raw,flush=True)
    driver.emit('FULL_POSITION_FINAL_IDENTITY',{'JSON_bytes':len(raw.encode()),
        'sha256':hashlib.sha256(raw.encode()).hexdigest()})


if __name__=='__main__':
    main()
