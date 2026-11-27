"""Explicit PHI continuation after the actual zero-prefix q-jet power failure."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
ADAPTER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_resume_worker.py'
ADAPTER_SHA = '490c152c03c7b0d43cbf08880cf5272cbe6097c3f97823574bad5b01ed62edd0'
FAILED = TOPIC+'/notes/strict_nu_phase_ci/run-45914123725-1/execution.json'
FAILED_SHA = '5975debd2466c29236dd54a3d4eb5bd598e70d186809d7712a8de5f5318a77c4'
ACTUAL = TOPIC+'/notes/strict_nu_phase_ci/run-45914123725-1/actual-strict-nu-phase.json'
ACTUAL_SHA = 'cd4487056ad752ffdeda4fbf5ae70046e24cd6d2a4724ba97f6088b90411b407'
OLD_MANIFEST = TOPIC+'/notes/2026-11-27-strict-nu-phase-after-45913335399-inputs.json'
OLD_MANIFEST_SHA = 'ba28dbb6d08e7a358e77ebf3e81ea044f0159ce08377e1db26b698371ef63ceb'


def require(ok,message):
    if not ok:raise ValueError(message)


def admitted_failure(root):
    raws = [(root/path).read_bytes() for path in (FAILED,ACTUAL,OLD_MANIFEST)]
    require([len(raw) for raw in raws] == [32942,10102,85210]
        and [hashlib.sha256(raw).hexdigest() for raw in raws] == [FAILED_SHA,ACTUAL_SHA,OLD_MANIFEST_SHA],
        'whole actual failed execution, full scientific prefix and exact second manifest')
    old,actual,manifest = map(json.loads,raws)
    require(old['run_id'] == actual['identity']['run_id'] == '45914123725'
        and old['run_attempt'] == actual['identity']['run_attempt'] == '1'
        and old['manifest_sha256'] == actual['identity']['manifest_sha256'] == OLD_MANIFEST_SHA
        and actual['identity']['source_sha256'] == next(x['sha256'] for x in manifest['files'] if x['role'] == 'science')
        and actual['identity']['kind'] == manifest['scientific_kind']
        and actual['parameters'] == manifest['parameters']
        and old['actual_child_returncode'] == actual['actual_returncode'] == 1
        and old['child_timeout'] is False and old['scientific_children'] == 1
        and old['complete'] is actual['complete'] is actual['proved'] is False
        and old['completed_new_scalar_targets'] == actual['saved_record_count'] == 0
        and actual['completed_targets'] == [] and actual['new_records'] == {}
        and actual['candidate_record'] is actual['current_target'] is actual['phase_integral_prefix'] is None
        and actual['necessary_original_phase_receipts'] is None
        and old['original_scientific_failure'] == actual['failure']
        and actual['failure']['type'] == 'ValueError'
        and actual['failure']['message'] == 'finite explicit scalar polynomial coefficient'
        and old['current_input_receipts'] == manifest['files']
        and old['scientific_files'] == [{'path':ACTUAL,'bytes':10102,'sha256':ACTUAL_SHA}]
        and actual['old_scientific_target_calls'] == old['old_completed_targets_recomputed']
            == old['old_numerical_producers_called'] == 0,
        'the actual zero-target and zero-accepted-germ failure, without replacing its status')
    receipt = actual['necessary_original_trial_receipts']
    require(receipt['all_four_complete_arrays_read_back'] is True
        and receipt['complete_original_trial_definition_sha256']
            == '83da6322dbb4702fe6ae308acbcfb7bb1ed9410d17e0cded65bc1215dec233db'
        and len(receipt['complete_original_array_receipts']) == 4
        and all(x['bytes'] == 1142560 and x['shape'] == [740,193]
            for x in receipt['complete_original_array_receipts'])
        and receipt['old_residual_cells_evaluated'] == receipt['old_scientific_norm_targets_evaluated']
            == receipt['old_signed_pairings_evaluated'] == 0 and receipt['new_trial_selected'] is False,
        'the complete original NP carrier restoration succeeded and is retained as such')
    return old,actual,manifest


def build_adapter(root):
    raw = (root/ADAPTER).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == ADAPTER_SHA,'the entire idempotent original-input adapter')
    spec = importlib.util.spec_from_file_location('_PHI_idempotent_original_adapter',root/ADAPTER)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.admitted_failure(root)
    return module.build_adapter(root)


def main():
    parser = argparse.ArgumentParser(add_help=False);parser.add_argument('--repo',required=True)
    args,_ = parser.parse_known_args();root = Path(args.repo).resolve();admitted_failure(root)
    namespace = {'__name__':'_PHI_explicit_integer_cube_continuation','__file__':__file__}
    exec(compile(build_adapter(root),str(Path(__file__).resolve()),'exec'),namespace)
    namespace['main']()


if __name__ == '__main__':main()
