#!/usr/bin/env python3
"""Resume the unchanged complete target-H solve from a real accepted inner trial.

The input is still an unaccepted nonlinear recovery point.  It is not renamed
an initial-seed packet or a converged solution.  Its complete original raw
shooting state, parameter set, node grid and H are checked, then loaded by the
unchanged exact-raw worker.  Original residuals, full Jacobians, Newton steps,
positivity, line search and final audit still decide acceptance.  Previously
completed identical-input stages may be restored by the existing exact cache.
"""
from __future__ import annotations
import argparse
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import sys

HERE = Path(__file__).resolve().parent
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
EXPECTED = {
    'strong_cached_target_tail_audit.py':
        '061809242a2eb12aec99ca71272f86c0096da77cbb4d7d6006d7119ee1081702',
    'strong_tail_young_space_guard.py':
        '867244ef03a99ea50f7629d437873c073e9a07ee8a88b48568c79817be7b7eba',
    'strong_tail_constructor_guard.py':
        '6f51a896e44aff8aa8a2f66a71320b68f15d279ec2a8e2ee0e3093cedf0696a3',
}
IO = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def packed(values):
    flat = [float(v) for v in values]
    if not all(math.isfinite(v) for v in flat):
        raise ValueError('Nonfinite full recovery value')
    return struct.pack('<'+'d'*len(flat), *flat)


def validate_iteration(path, binding, original_checkpoint):
    path = Path(path)
    data = path.read_bytes()
    record = json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)
    iteration = record.get('iteration', {})
    if (record.get('status') != 'iteration-recovery-only'
            or iteration.get('phase') != 'accepted-trial-recovery-only'
            or not isinstance(iteration.get('acceptedFromIteration'), int)
            or not isinstance(iteration.get('acceptedTrial'), int)
            or not 0 < float(iteration.get('acceptedStep', 0)) <= 1
            or not math.isfinite(float(iteration.get('norm', math.inf)))):
        raise ValueError('An actual accepted-trial recovery record is required')
    checkpoint = record['checkpoint']
    if checkpoint.get('exactInitialSeed'):
        raise ValueError('Do not relabel an initial seed as an accepted trial')
    current, original = checkpoint['parameters'], original_checkpoint['parameters']
    if ({k: v for k, v in current.items() if k not in IO} !=
            {k: v for k, v in original.items() if k not in IO}):
        raise ValueError('Accepted trial differs from the complete original tail parameters')
    M = int(binding['modes'])
    if int(current['modes']) != M:
        raise ValueError('The complete tail mode count differs')
    H = packed(checkpoint['cutHeight'])
    if len(checkpoint['cutHeight']) != M or H != packed(binding['complete_warm_H']):
        raise ValueError('Accepted trial belongs to another complete H')
    states = checkpoint['states']
    count = int(current['depth'])+1
    if len(states) != count or any(len(row) != 2*M for row in states):
        raise ValueError('The complete accepted raw state is missing')
    state_bytes = packed(value for row in states for value in row)
    raw_node = checkpoint['rawNode']
    if (packed(raw_node) != packed(original_checkpoint['rawNode'])
            or len(checkpoint['rawStates']) != len(raw_node)):
        raise ValueError('The original shooting raw-node grid differs')
    for node, row in zip(raw_node, checkpoint['rawStates']):
        if (not isinstance(node, (int, float)) or node != int(node)
                or not 0 <= int(node) < count
                or len(row) != 2*M or packed(row) != packed(states[int(node)])):
            raise ValueError('Raw shooting boundaries differ from the complete stored state')
    return dict(scope=__doc__, source=str(path), source_sha256=hashlib.sha256(data).hexdigest(),
        original_status=record['status'], original_iteration=iteration,
        original_call=record.get('call'), complete_H_float64LE_sha256=hashlib.sha256(H).hexdigest(),
        full_state_from_saved_JSON_float64LE_sha256=hashlib.sha256(state_bytes).hexdigest(),
        node_count=count, shape_dimension=2*M, all_values_finite=True,
        all_non_IO_parameters_match_accepted_baseline=True,
        complete_original_raw_node_grid_and_states_consistent=True,
        source_file_and_checkpoint_values_unmodified=True,
        original_norm_not_used_for_acceptance=True,
        original_full_residual_Jacobian_Newton_and_audit_required=True,
        numerical_solution_accepted=False)


def build_source(old_heap, semi_space):
    for name, expected in EXPECTED.items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest() != expected:
            raise ValueError('Retained iteration resource source changed: '+name)
    import strong_cached_target_tail_audit as prior
    source, original = prior.build_source()
    guard_before = (
        "    seed_input=None\n"
        "    if args.initial_seed:\n"
        "        seed_input=read(args.initial_seed)\n"
        "        checkpoint=seed_input.get('checkpoint',seed_input)\n"
        "        if not checkpoint.get('exactInitialSeed'):\n"
        "            raise ValueError('The explicit initial seed has no exact binary marker')\n"
        "        if checkpoint['cutHeight'] != binding['complete_warm_H']:\n"
        "            raise ValueError('The explicit seed belongs to another complete H')\n"
        "        if seed_input.get('status') != 'initial-warm-only':\n"
        "            raise ValueError('An initial seed cannot be relabelled as an accepted trial')")
    edits = [
        ("    parser.add_argument('--initial-seed', type=Path)",
         "    parser.add_argument('--iteration-checkpoint', type=Path, required=True)"),
        ("    cfg['initialCheckpoint'] = str((args.initial_seed or args.accepted_tail).resolve())",
         "    cfg['initialCheckpoint'] = str(args.iteration_checkpoint.resolve())"),
        (guard_before,
         "    iteration_recovery = ITERATION_VALIDATOR(args.iteration_checkpoint, binding,\n"
         "        old_tail['response']['checkpoint'])"),
        ("    if args.initial_seed: hashes[str(args.initial_seed)]=sha(args.initial_seed)",
         "    hashes[str(args.iteration_checkpoint)]=sha(args.iteration_checkpoint)\n"
         "    hashes.update(ITERATION_SOURCE_HASHES)"),
        ("        initial_seed=None if args.initial_seed is None else str(args.initial_seed),",
         "        iteration_recovery=iteration_recovery,\n"
         "        iteration_resource_wrapper=ITERATION_RESOURCE_RECORD,"),
        ("        exact_same_H_raw_shortcut_will_not_apply=(args.initial_seed is None),",
         "        exact_same_H_raw_shortcut_will_not_apply=False,"),
        ("        warm_guess_kind='old accepted full shooting state at a different H; original predictor/Newton remain required',",
         "        warm_guess_kind='actual accepted inner trial, still unaccepted recovery; original raw loader and complete residual/Jacobian/Newton/audit required',"),
    ]
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError('Iteration recovery source anchor is not unique: '+repr(before))
        source = source.replace(before, after, 1)
    if 'args.initial_seed' in source:
        raise ValueError('An initial-seed argument survived the explicit iteration recovery transform')
    ast.parse(source, filename='<accepted-inner-trial-tail-recovery>')
    record = dict(original)
    record['accepted_iteration_recovery_adapter'] = dict(scope=__doc__,
        entry_sha256=SELF_SHA, original_transformed_source_sha256=original['transformed_source_sha256'],
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=a, after=b, count=1) for a, b in edits],
        mathematical_MJS_and_all_acceptance_unchanged=True,
        stage_cache_identity_unchanged=True, old_heap_MiB=old_heap,
        young_semi_space_MiB=semi_space)
    return source, record, prior


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--node-young-semi-space', type=int,
        choices=(1, 2, 4, 8, 16), required=True)
    own, remaining = parser.parse_known_args()
    for name in ('--node-heap', '--iteration-checkpoint', '--out-prefix'):
        if remaining.count(name) != 1:
            raise ValueError('Explicit unique recovery argument required: '+name)
    if '--initial-seed' in remaining or '--diagnostic-complete-evaluate' in remaining:
        raise ValueError('This entry performs original full nonlinear acceptance from an inner trial')
    old_heap = int(remaining[remaining.index('--node-heap')+1])
    if old_heap <= 0:
        raise ValueError('The explicit old-heap limit must be positive')
    source, record, prior = build_source(old_heap, own.node_young_semi_space)
    resource_record = dict(old_heap_MiB=old_heap,
        young_semi_space_MiB=own.node_young_semi_space,
        resource_source_sha256=EXPECTED['strong_tail_young_space_guard.py'],
        constructor_guard_sha256=EXPECTED['strong_tail_constructor_guard.py'],
        no_claim_about_prior_signal9_cause=True)
    hashes = {str(HERE/name): value for name, value in EXPECTED.items()}
    hashes[str(Path(__file__).resolve())] = SELF_SHA
    namespace = dict(__file__=str(prior.TEMPLATE), __name__='strong_cached_iteration_tail_source',
        STAGE_SOURCE_TRANSFORM=record, ITERATION_VALIDATOR=validate_iteration,
        ITERATION_SOURCE_HASHES=hashes, ITERATION_RESOURCE_RECORD=resource_record)
    from strong_tail_young_space_guard import resource_port_class
    import strong_exact_stage_tail_client as client
    old_class, old_argv = client.WeightedTailPort, sys.argv
    client.WeightedTailPort = resource_port_class(old_class, old_heap, own.node_young_semi_space)
    sys.argv = [old_argv[0], *remaining]
    try:
        exec(compile(source, '<accepted-inner-trial-tail-recovery>', 'exec'), namespace)
        namespace['main']()
    finally:
        client.WeightedTailPort = old_class
        sys.argv = old_argv


if __name__ == '__main__':
    main()
