#!/usr/bin/env python3
"""One explicit lambda27 comparison on the same actual64/twenty-query model.

The frozen twenty-query producer remains unchanged. This independent source
binds its complete function bodies and the original full-angle engine, changes
only the declared damping value and corresponding current metadata, and reuses
the original complete A/g/B, C formula, QR/condensation and nonlinear trials.
The same actual64 parent used by request66 is mandatory. This is one declared
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

import geometry_20261114_twenty_query_condensed_warm as frozen_twenty

HERE = Path(__file__).resolve().parent
SCHEMA = "exact-constraint-twenty-query-lambda27-condensed-complete-H-warm-v1"
PARENT_SCHEMA = frozen_twenty.PARENT_SCHEMA
FROZEN_TWENTY_SHA = "9d750fcba45624f23dbae19ca44fded0437f1f5dc15943879cbf046064fe22ee"
FROZEN_ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
EXPERIMENT_DAMPING = 27.0
ORIGINAL_DAMPING = 270.0
ACTUAL64_WARM_SHA = "3b25ea84dfababece99e1dc098d56cdcebd94737e428e509140e818d48e8eb1e"
ACTUAL64_STATUS_SHA = "037fb9eeaeb196f74976188efb9515736396f2c86a44fde4e93251e92ca01466"

# Public aliases preserve the established independent FD and read-only
# collocation observer APIs. No scientific function runs at import time.
baseline = frozen_twenty.baseline
parent = frozen_twenty.parent
engine = frozen_twenty.engine
observed = frozen_twenty.observed
support = frozen_twenty.support
original = frozen_twenty.original
domain = frozen_twenty.domain
square_root = frozen_twenty.square_root
condensation = frozen_twenty.condensation
local_qp = frozen_twenty.local_qp
identities = frozen_twenty.identities
archive_source = frozen_twenty.archive_source
SOURCE_NAMES = tuple(dict.fromkeys((Path(__file__).name,
    Path(frozen_twenty.__file__).name, *frozen_twenty.SOURCE_NAMES)))
FROZEN = {
    **frozen_twenty.FROZEN,
    Path(frozen_twenty.__file__).name: FROZEN_TWENTY_SHA,
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
TWENTY_METADATA_EDITS = {
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
        schema="same-actual64-twenty-query-single-damping-contract-v1",
        original_damping=ORIGINAL_DAMPING,
        explicit_current_damping=EXPERIMENT_DAMPING,
        original_damping_float64le_hex=struct.pack('<d', ORIGINAL_DAMPING).hex(),
        current_damping_float64le_hex=struct.pack('<d', EXPERIMENT_DAMPING).hex(),
        same_actual64_parent_as_request66=True,
        actual_parent_warm_sha256=ACTUAL64_WARM_SHA,
        actual_parent_status_sha256=ACTUAL64_STATUS_SHA,
        original_twenty_query_entry_source_sha256=FROZEN_TWENTY_SHA,
        original_full_trial_engine_source_sha256=FROZEN_ENGINE_SHA,
        typed_domain_source_sha256=frozen_twenty.TWENTY_OPERATOR_SHA,
        selected_query_count=20,
        selected_angle_row_count=40960,
        complete_B_local_dimension=6763,
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


def prepared_source_texts(twenty_text, engine_text):
    """Return complete function texts and a nonnumerical transformation receipt."""
    require(sha_text(twenty_text) == FROZEN_TWENTY_SHA,
        "The exact twenty-query complete implementation changed")
    require(sha_text(engine_text) == FROZEN_ENGINE_SHA,
        "The exact full residual and original trial engine changed")
    original_functions = source_functions(twenty_text)
    require(set(original_functions) == set(FUNCTION_NAMES),
        "Explicitly account for every frozen twenty-query implementation function")
    adapted = {}
    rows = []
    for name in FUNCTION_NAMES:
        before = original_functions[name]
        edits = TWENTY_METADATA_EDITS.get(name, ())
        after = replace_exactly_once(before, edits, "twenty."+name) if edits else before
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
        original_twenty_source_sha256=FROZEN_TWENTY_SHA,
        original_engine_source_sha256=FROZEN_ENGINE_SHA,
        twenty_functions=rows,
        original_engine_main_sha256=sha_text(old_main),
        adapted_engine_main_sha256=sha_text(new_main),
        engine_edits=[dict(before=x, after=y) for x,y in ENGINE_EDITS],
        original_function_source_recovered_exactly_by_declared_inverse=True,
        old_twenty_module_globals_or_source_file_mutated=False,
        temporary_engine_main_assignment_restored_in_finally=True,
        original_main_all_other_statements_byte_identical=True,
        no_complete_matrix_or_direction_computed_by_source_adapter=True)
    return adapted, new_main, proof


def guard():
    square_root.require_actions()
    for name, digest in FROZEN.items():
        require(original.sha(HERE/name) == digest, "Frozen source identity: "+name)
    require(Path(frozen_twenty.__file__).resolve().parent == HERE,
        "Read the frozen implementation from this same source directory")
    require(frozen_twenty.ORIGINAL_CHOOSE is archive_source.ORIGINAL_CHOOSE,
        "Keep the imported original complete-model selector")
    require(engine.choose_feasible_descent is frozen_twenty.ORIGINAL_CHOOSE,
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
    require(a.expected_resume_sha == ACTUAL64_WARM_SHA
        and a.expected_parent_status_sha == ACTUAL64_STATUS_SHA,
        "Use the same actual64 parent pair as request66, not its new warm")
    require(original.sha(a.resume) == ACTUAL64_WARM_SHA
        and original.sha(a.parent_status) == ACTUAL64_STATUS_SHA,
        "Both actual64 parent files must have their original bytes")
    status = original.read(a.parent_status)
    require(status.get('schema') == PARENT_SCHEMA,
        "This single comparison starts from the original nineteen-query parent")
    require(a.iterations == 1 and a.lsmr_iterations == 200
        and a.projection_sweeps == 200 and a.line_search_steps == 17
        and a.condensed_max_working == 512 and a.condensed_dual_sweeps == 200
        and a.condensed_budget_seconds == 600.0
        and a.condensed_trial_reserve_seconds == 90.0
        and a.condensed_recovery_reserve_seconds == 30.0
        and a.budget_seconds == 1200.0 and a.angles == 4096
        and a.jac_workers == 2 and a.condensed_store_root,
        "Keep the declared request66 experiment budgets, complete root and original trial bounds")
    return a


def main():
    guard()
    args = fixed_experiment_arguments()
    twenty_text = Path(frozen_twenty.__file__).read_text(encoding='utf-8')
    engine_text = Path(engine.__file__).read_text(encoding='utf-8')
    functions, engine_main_text, proof = prepared_source_texts(twenty_text, engine_text)
    contract = single_damping_contract()
    proof.update(entry_source_sha256=original.sha(__file__),
        actual_parent_warm_sha256=ACTUAL64_WARM_SHA,
        actual_parent_status_sha256=ACTUAL64_STATUS_SHA,
        current_schema=SCHEMA, single_damping_experiment=contract)
    args.out.mkdir(parents=True, exist_ok=True)
    original.write(args.out/'single-damping-source-binding.json', proof)

    # Private globals make every cloned function identify this independent
    # producer. The old twenty module and all its frozen functions stay intact.
    private = dict(vars(frozen_twenty))
    private.update(__name__=__name__, __file__=__file__, __doc__=__doc__,
        HERE=HERE, SCHEMA=SCHEMA, PARENT_SCHEMA=PARENT_SCHEMA,
        SOURCE_NAMES=SOURCE_NAMES, FROZEN=FROZEN,
        SINGLE_DAMPING_CONTRACT=copy.deepcopy(contract))
    for name in FUNCTION_NAMES:
        exec(compile(functions[name], __file__+'::<frozen-twenty.'+name+'>', 'exec'),
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
        return private['main']()
    finally:
        engine.main = old_main


if __name__ == '__main__':
    raise SystemExit(main())
