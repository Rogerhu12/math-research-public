#!/usr/bin/env python3
"""One explicit lambda27 comparison on the same actual66/twenty-one-query model.

The frozen twenty-one-query producer remains unchanged. This independent source
binds its complete function bodies and the original full-angle engine, changes
only the declared damping value and corresponding current metadata, and reuses
the original complete A/g/B, C formula, QR/condensation and nonlinear trials.
The same actual66 parent used by request68 is mandatory. This is one declared
algorithm experiment, not a damping scan or a claim of monotone improvement.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import inspect
import json
import math
from pathlib import Path
import struct
import sys

import geometry_20261114_twenty_one_query_condensed_warm as frozen_twenty_one

HERE = Path(__file__).resolve().parent
SCHEMA = "exact-constraint-twenty-one-query-lambda27-condensed-complete-H-warm-v1"
PARENT_SCHEMA = frozen_twenty_one.PARENT_SCHEMA
FROZEN_TWENTY_ONE_SHA = "b7956525ce484c4ed17724c2d84c04b6080688e2d0afc8367c5ba46cbf8626f2"
FROZEN_ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
EXPERIMENT_DAMPING = 27.0
ORIGINAL_DAMPING = 270.0
ACTUAL66_WARM_SHA = "80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6"
ACTUAL66_STATUS_SHA = "04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4"

# Public aliases preserve the established independent FD and read-only
# collocation observer APIs. No scientific function runs at import time.
baseline = frozen_twenty_one.baseline
parent = frozen_twenty_one.parent
engine = frozen_twenty_one.engine
observed = frozen_twenty_one.observed
support = frozen_twenty_one.support
original = frozen_twenty_one.original
domain = frozen_twenty_one.domain
square_root = frozen_twenty_one.square_root
condensation = frozen_twenty_one.condensation
local_qp = frozen_twenty_one.local_qp
identities = frozen_twenty_one.identities
archive_source = frozen_twenty_one.archive_source
SOURCE_NAMES = tuple(dict.fromkeys((Path(__file__).name,
    Path(frozen_twenty_one.__file__).name, *frozen_twenty_one.SOURCE_NAMES)))
FROZEN = {
    **frozen_twenty_one.FROZEN,
    Path(frozen_twenty_one.__file__).name: FROZEN_TWENTY_ONE_SHA,
    Path(engine.__file__).name: FROZEN_ENGINE_SHA,
}

FUNCTION_NAMES = ("equal", "guard", "scalar_or_none", "evidence",
    "compact_metadata", "_run_engine", "main")
ENGINE_EDITS = (
    ('parser.add_argument("--damping", type=float, default=270.)',
     'parser.add_argument("--damping", type=float, default=27.)'),
    ('args.damping != 270.', 'args.damping != 27.'),
    ('Use the declared one-model lambda270/full-angle experiment and original trial bounds',
     'Use the declared one-model lambda27/full-angle experiment and original trial bounds'),
    ('Same complete ||A z+b||^2+lambda^2||z||^2, lambda270',
     'Same complete ||A z+b||^2+lambda^2||z||^2, explicit lambda27; prior lambda270 experiment'),
)
TWENTY_ONE_METADATA_EDITS = {
    "_run_engine": (
        ('original_lambda_LSMR_projection_and_seventeen_trials_unchanged=True,',
         'original_LSMR_projection_and_seventeen_trials_unchanged=True,\n'
         '        damping_changed_explicitly=True,\n'
         '        single_damping_experiment=SINGLE_DAMPING_CONTRACT,'),
    ),
    "main": (
        ('original_lambda_and_row_and_chart_weights_unchanged=True,',
         'original_row_and_chart_weights_unchanged=True,\n'
         '        damping_changed_explicitly=True,\n'
         '        single_damping_experiment=SINGLE_DAMPING_CONTRACT,'),
    ),
}


def sha_text(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def require(test, message):
    if not test:
        raise ValueError(message)


def single_damping_contract():
    return dict(
        schema="same-actual66-twenty-one-query-single-damping-contract-v1",
        original_damping=ORIGINAL_DAMPING,
        explicit_current_damping=EXPERIMENT_DAMPING,
        original_damping_float64le_hex=struct.pack('<d', ORIGINAL_DAMPING).hex(),
        current_damping_float64le_hex=struct.pack('<d', EXPERIMENT_DAMPING).hex(),
        same_actual66_parent_as_request68=True,
        actual_parent_warm_sha256=ACTUAL66_WARM_SHA,
        actual_parent_status_sha256=ACTUAL66_STATUS_SHA,
        original_twenty_one_query_entry_source_sha256=FROZEN_TWENTY_ONE_SHA,
        original_full_trial_engine_source_sha256=FROZEN_ENGINE_SHA,
        typed_domain_source_sha256=frozen_twenty_one.TWENTY_ONE_OPERATOR_SHA,
        selected_query_count=21,
        selected_angle_row_count=43008,
        complete_B_local_dimension=7101,
        complete_B_declared_physical_nodes=list(domain.LOCAL_LAYOUT_NODES),
        explicit_zero_B_layout_nodes=list(domain.ZERO_LAYOUT_NODES),
        complete_original_A_b_g_row_weights_chart_and_B_formulas_unchanged=True,
        original_complete_g_equals_A_transpose_b_retained=True,
        actual_reconstructed_model_arrays_must_be_read_from_this_run=True,
        same_input_does_not_claim_future_array_hashes_before_execution=True,
        B_model_metadata_hash_may_change_with_new_producer_identity=True,
        original_C_formula="sqrt(original complete column_norm_squared + damping**2)",
        C_rebuilt_with_explicit_damping=True,
        original_C270_bytes_not_reused_or_claimed_unchanged=True,
        same_actual66_parent_as_both_request68_and_this_experiment=True,
        actual67_updated_warm_not_used_as_parent=True,
        own_schema_resume_supported=False,
        relative_to_request68_queries_and_complete_B_support_unchanged=True,
        common_original_left_RMS466_is_present_in_both_models=True,
        full_QR_and_local_root_rebuilt_with_explicit_damping=True,
        no_old_lambda270_factor_or_root_reused=True,
        baseline_fixed_C_support_dimension=4059,
        baseline_C_all_outside_raw_contributions_retained=True,
        complete_H_direction_not_limited_to_baseline_C_support=True,
        inequality_reserve_theta_unchanged=0.5,
        full_B_constraints_retained=True,
        original_512_working_200_dual_200_LSMR_experiment_preserved=True,
        original_seventeen_trials_and_domain_RMS_BC_and_merit_preserved=True,
        damping_penalty_not_added_to_actual_nonlinear_merit=True,
        original_new_warm_complete_FD_required=True,
        one_explicit_damping_value_no_scan=True,
        lower_damping_monotone_row_or_nonlinear_improvement_claimed=False,
        actual65_center_observation_does_not_certify_unique_damping_cause=True,
        scientific_acceptance_or_new_gate_created=False)


def source_functions(text):
    """Pure source extraction; this function performs no numerical imports."""
    tree = ast.parse(text)
    result = {}
    for item in tree.body:
        if isinstance(item, ast.FunctionDef):
            require(not item.decorator_list, "Frozen top-level implementation has no decorators")
            require(item.name not in result, "Unique frozen function definitions")
            result[item.name] = ast.get_source_segment(text, item)
    return result


def replace_exactly_once(text, edits, label):
    current = text
    for before, after in edits:
        require(current.count(before) == 1, "One declared source location: "+label)
        require(after not in current, "No existing adapted declaration: "+label)
        current = current.replace(before, after, 1)
    restored = current
    for before, after in reversed(edits):
        require(restored.count(after) == 1, "One reversible source location: "+label)
        restored = restored.replace(after, before, 1)
    require(restored == text, "All original source bytes round-trip: "+label)
    ast.parse(current)
    return current


def prepared_source_texts(twenty_one_text, engine_text):
    """Return complete function texts and a nonnumerical transformation receipt."""
    require(sha_text(twenty_one_text) == FROZEN_TWENTY_ONE_SHA,
        "The exact twenty-one-query complete implementation changed")
    require(sha_text(engine_text) == FROZEN_ENGINE_SHA,
        "The exact full residual and original trial engine changed")
    original_functions = source_functions(twenty_one_text)
    require(set(original_functions) == set(FUNCTION_NAMES),
        "Explicitly account for every frozen twenty-one-query implementation function")
    adapted = {}
    rows = []
    for name in FUNCTION_NAMES:
        before = original_functions[name]
        edits = TWENTY_ONE_METADATA_EDITS.get(name, ())
        after = replace_exactly_once(before, edits, "twenty_one."+name) if edits else before
        adapted[name] = after
        rows.append(dict(function=name, original_sha256=sha_text(before),
            adapted_sha256=sha_text(after),
            complete_original_body_preserved_except_listed_current_metadata=bool(edits),
            body_byte_identical=not edits,
            reversible_edits=[dict(before=x, after=y) for x,y in edits]))
    old_main = source_functions(engine_text)['main']
    new_main = replace_exactly_once(old_main, ENGINE_EDITS, 'full-angle.main')
    # Whole-source round-trip above also preserves every finite equation,
    # original threshold, model callback and original nonlinear trial statement.
    proof = dict(schema="same-model-single-damping-source-transform-v1",
        original_twenty_one_source_sha256=FROZEN_TWENTY_ONE_SHA,
        original_engine_source_sha256=FROZEN_ENGINE_SHA,
        twenty_one_functions=rows,
        original_engine_main_sha256=sha_text(old_main),
        adapted_engine_main_sha256=sha_text(new_main),
        engine_edits=[dict(before=x, after=y) for x,y in ENGINE_EDITS],
        original_function_source_recovered_exactly_by_declared_inverse=True,
        old_twenty_one_module_globals_or_source_file_mutated=False,
        temporary_engine_main_assignment_restored_in_finally=True,
        original_main_all_other_statements_byte_identical=True,
        no_complete_matrix_or_direction_computed_by_source_adapter=True)
    return adapted, new_main, proof


def guard():
    square_root.require_actions()
    for name, digest in FROZEN.items():
        require(original.sha(HERE/name) == digest, "Frozen source identity: "+name)
    require(Path(frozen_twenty_one.__file__).resolve().parent == HERE,
        "Read the frozen implementation from this same source directory")
    require(frozen_twenty_one.ORIGINAL_CHOOSE is archive_source.ORIGINAL_CHOOSE,
        "Keep the imported original complete-model selector")
    require(engine.choose_feasible_descent is frozen_twenty_one.ORIGINAL_CHOOSE,
        "Install this independent entry before a numerical selector wrapper")


def fixed_experiment_arguments():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument('--resume', type=Path, required=True)
    p.add_argument('--expected-resume-sha', required=True)
    p.add_argument('--parent-status', type=Path, required=True)
    p.add_argument('--expected-parent-status-sha', required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--damping', type=float, required=True)
    p.add_argument('--iterations', type=int, required=True)
    p.add_argument('--lsmr-iterations', type=int, required=True)
    p.add_argument('--projection-sweeps', type=int, required=True)
    p.add_argument('--line-search-steps', type=int, required=True)
    p.add_argument('--condensed-max-working', type=int, required=True)
    p.add_argument('--condensed-dual-sweeps', type=int, required=True)
    p.add_argument('--condensed-budget-seconds', type=float, required=True)
    p.add_argument('--condensed-trial-reserve-seconds', type=float, required=True)
    p.add_argument('--condensed-recovery-reserve-seconds', type=float, required=True)
    p.add_argument('--budget-seconds', type=float, required=True)
    p.add_argument('--angles', type=int, required=True)
    p.add_argument('--jac-workers', type=int, required=True)
    p.add_argument('--condensed-store-root', action='store_true')
    a, _ = p.parse_known_args()
    require(math.isfinite(a.damping) and a.damping == EXPERIMENT_DAMPING,
        "Run only the explicit lambda27 experiment; no damping scan")
    require(a.expected_resume_sha == ACTUAL66_WARM_SHA
        and a.expected_parent_status_sha == ACTUAL66_STATUS_SHA,
        "Use the same actual66 parent pair as request68, not its new warm")
    require(original.sha(a.resume) == ACTUAL66_WARM_SHA
        and original.sha(a.parent_status) == ACTUAL66_STATUS_SHA,
        "Both actual66 parent files must have their original bytes")
    status = original.read(a.parent_status)
    require(status.get('schema') == PARENT_SCHEMA,
        "This single comparison starts from the original twenty-query parent")
    require(a.iterations == 1 and a.lsmr_iterations == 200
        and a.projection_sweeps == 200 and a.line_search_steps == 17
        and a.condensed_max_working == 512 and a.condensed_dual_sweeps == 200
        and a.condensed_budget_seconds == 600.0
        and a.condensed_trial_reserve_seconds == 90.0
        and a.condensed_recovery_reserve_seconds == 30.0
        and a.budget_seconds == 1200.0 and a.angles == 4096
        and a.jac_workers == 2 and a.condensed_store_root,
        "Keep the declared request68 experiment budgets, complete root and original trial bounds")
    return a


def main():
    guard()
    args = fixed_experiment_arguments()
    twenty_one_text = Path(frozen_twenty_one.__file__).read_text(encoding='utf-8')
    engine_text = Path(engine.__file__).read_text(encoding='utf-8')
    functions, engine_main_text, proof = prepared_source_texts(twenty_one_text, engine_text)
    contract = single_damping_contract()
    proof.update(entry_source_sha256=original.sha(__file__),
        actual_parent_warm_sha256=ACTUAL66_WARM_SHA,
        actual_parent_status_sha256=ACTUAL66_STATUS_SHA,
        current_schema=SCHEMA, single_damping_experiment=contract)

    # Private globals make every cloned function identify this independent
    # producer. The old twenty-one module and all its frozen functions stay intact.
    private = dict(vars(frozen_twenty_one))
    private.update(__name__=__name__, __file__=__file__, __doc__=__doc__,
        HERE=HERE, SCHEMA=SCHEMA, PARENT_SCHEMA=PARENT_SCHEMA,
        SOURCE_NAMES=SOURCE_NAMES, FROZEN=FROZEN,
        SINGLE_DAMPING_CONTRACT=copy.deepcopy(contract))
    for name in FUNCTION_NAMES:
        exec(compile(functions[name], __file__+'::<frozen-twenty-one.'+name+'>', 'exec'),
            private, private)
    # The engine function deliberately uses its original live global mapping:
    # private._run_engine installs the same real B/observer/callbacks there.
    created = {}
    exec(compile(engine_main_text, __file__+'::<single-damping-engine>', 'exec'),
        engine.__dict__, created)
    modified_main = created['main']
    require(modified_main.__globals__ is engine.__dict__,
        "The original engine must observe the installed complete-model callbacks")
    old_main = engine.main
    engine.main = modified_main
    try:
        status = private['main']()
        original.write(args.out/'single-damping-source-binding.json', proof)
        return status
    finally:
        engine.main = old_main


if __name__ == '__main__':
    raise SystemExit(main())
