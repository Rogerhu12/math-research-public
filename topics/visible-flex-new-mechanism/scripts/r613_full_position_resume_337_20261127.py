#!/usr/bin/env python3
"""Normal continuation from the actual full-S iteration337 checkpoint.

Only the immutable incoming-checkpoint reader and receipt schema are new.
The entire published full-S model, analytic Jacobian, complete-row QR/SVD,
direction/line search, all original meshes and actual terminal readout are
called directly from their hash-bound original driver. No numerical method
is copied, modified, or executed by importing this source locally.

No QR/BFGS/internal linear factor was saved by the preceding scope. This
resume restores the actual accepted1130q, amplitude and next damping only,
then performs the next necessary ordinary solve. Previously paid fine or
direction diagnostics are not run as a new entry gate.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
DRIVER_FILE = 'r613_full_position_height_20261127.py'
DRIVER_SHA = '6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0'
PREVIOUS_INPUT_SHA = 'b21486214dbec1ddd6033a2a90218a91150d6e0b271a12b104aa6ed3203694c4'
RECONSTRUCTION_SHA = '14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee'
SOURCE_Q_SHA = '238d786c6134bcbd356958c5fcf263916feb5bf1004af7e93722a30ed591e1c7'
SCHEMA = 'r613-actual337-normal-full-position-continuation-v1'


def load_original_driver():
    path = HERE / DRIVER_FILE
    if hashlib.sha256(path.read_bytes()).hexdigest() != DRIVER_SHA:
        raise RuntimeError('published complete actual-position driver changed')
    spec = importlib.util.spec_from_file_location('r613_bound_complete_position_resume',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_actual337(args,driver):
    raw = (sys.stdin.buffer.read() if args.source_state_json == '@stdin'
           else args.source_state_json.encode())
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.source_state_sha256:
        raise ValueError('declared normal-resume input identity differs')
    source = json.loads(raw)
    origin = {
        'run_id':45891036836, 'job_id':140153472856,
        'source_commit':'99007dd193fd9fe8301c1f5228d102776e28e58f',
        'source_sha256':DRIVER_SHA,
        'raw_job_log_bytes':2370856,
        'raw_job_log_sha256':'b48665984baac38a0e1ae7c7c43bbe8bf5c5f48ac207ee924e1a55181762f8ec',
        'FINAL_JSON_bytes':98811,
        'FINAL_JSON_sha256':'966595136327c922b905c7000149bfa1d50e09816b0d27ee54a975a391958f37',
        'kind':'actual_accepted_checkpoint_of_completed_full_position_scope'}
    if source['origin'] != origin:
        raise ValueError('actual completed original full-position origin differs')
    qtext = source['actual_1130q_JSON']
    if (len(qtext.encode()) != 22696 or source['actual_q_JSON_bytes'] != 22696
            or source['actual_q_JSON_sha256'] != SOURCE_Q_SHA
            or hashlib.sha256(qtext.encode()).hexdigest() != SOURCE_Q_SHA):
        raise ValueError('actual accepted iteration337 q JSON differs')
    q = driver.np.asarray(json.loads(qtext),dtype=float)
    if q.shape != (1130,) or not driver.np.all(driver.np.isfinite(q)):
        raise ValueError('complete original1130q is required')
    if driver.weak.identity(q) != source['actual_retained_q_identity']:
        raise ValueError('actual accepted q identity changed')
    amplitude = float(source['amplitude'])
    damping = float(source['actual_next_damping'])
    iteration = int(source['global_accepted_iteration'])
    if (amplitude != 1e-5 or damping != 1e-14 or iteration != 337
            or q[0] != .5188903591561069
            or source['input_is_actual_accepted_checkpoint'] is not True
            or source['original_source_status'] != 'declared_complete_position_iteration_limit'
            or source['saved_internal_QR_or_BFGS_restored'] is not False
            or source['previous_fine_or_direction_readout_replayed_as_entry_gate'] is not False):
        raise ValueError('actual continuation state or normal-resume contract changed')
    previous = source['previous_scope_input_JSON']
    if len(previous.encode()) != 67172 or hashlib.sha256(previous.encode()).hexdigest() != PREVIOUS_INPUT_SHA:
        raise ValueError('full original input, including all paid mouths and costs, differs')
    inherited = json.loads(previous)['reconstruction_source_JSON']
    if len(inherited.encode()) != 31425 or hashlib.sha256(inherited.encode()).hexdigest() != RECONSTRUCTION_SHA:
        raise ValueError('same complete canonical field or original mouths changed')
    ledger = source['source_cost_ledger']
    if (ledger['run_id'] != 45891036836 or ledger['job_id'] != 140153472856
            or ledger['elapsed_seconds'] != 2961.020285526
            or ledger['new_complete_position_counts']['accepted_steps'] != 60
            or ledger['new_complete_position_counts']['rejected_steps'] != 166):
        raise ValueError('actual original cost ledger was lost or relabelled')
    return source,json.loads(inherited),q,amplitude,damping,iteration,digest


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('science belongs only to the declared public Actions scope')
    driver = load_original_driver()
    driver.input_state = lambda args: read_actual337(args,driver)
    driver.SCHEMA = SCHEMA
    # The original main prints the current entry source's identity. Its HERE
    # and every imported component were already bound to the same directory.
    driver.__file__ = __file__
    # No model, solver, Jacobian, QR, checkpoint, fine_readout or cost counter
    # is replaced. The original solve takes first_iteration from this reader.
    driver.main()


if __name__ == '__main__':
    main()
