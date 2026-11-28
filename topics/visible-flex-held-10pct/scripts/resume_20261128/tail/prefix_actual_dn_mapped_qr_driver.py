#!/usr/bin/env python3
"""Run original actual DN with full CSR-before-QR and factor mapped storage.

The unchanged portable driver owns every full-height native call, the original
eight outer iterations, complete residuals, domain rules and final finite gates.
Only prefix storage changes to the already accepted design prefactor-mapped
CSR/QR/V5/checkpoint stack. The original full CSR entries and QR algorithms
remain. Native full Jacobians are not mapped by this prefix adapter. Both
application argv lists, the intervening original QR argv, every mapped factor
and every resource sidecar are bound. This is a new execution schema, not an
old anonymous-CSR or streamed/SuperLU execution label.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SCRIPTS = ROOT.parent
DESIGN = ROOT/'design'
PORTABLE = SCRIPTS/'resume_m3/portable_prefix_continue.py'
QR = DESIGN/'prefix_csr_prefactor_qr_driver.py'
INNER_QR = ROOT/'prefix_block_qr_driver_v3.py'
BASE = DESIGN/'prefix_mapped_chord_checkpoint_driver.py'
V5 = DESIGN/'prefix_resource_driver_v5.py'
SCHEMA = 'original-actual-dn-complete-prefix-mapped-qr-execution-v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def load(path):
    return json.loads(Path(path).read_text())


def checked(value):
    path = Path(value['path']).resolve()
    if sha(path) != value['sha256']:
        raise ValueError('Changed complete QR execution evidence: '+str(path))
    return path


def source_files():
    """The complete selected stack, including the analytical delta derivative."""
    design = ('prefix_mapped_chord_checkpoint_driver.py', 'accepted_newton_nodal_checkpoint.py',
        'prefix_csr_prefactor_budget_driver.py', 'complete_prefactor_memory_budget.py',
        'complete_mapped_memory_budget.py', 'complete_csr_memory_budget_v2.py',
        'complete_csr_memory_budget.py',
        'complete_csr_prefactor_mmap.py', 'complete_factor_mmap.py',
        'literal_design_nodal_restart.py',
        'exception_safe_radial_batches.py', 'prefix_csr_assembly_driver.py',
        'direct_csr_collocation.py', 'prefix_resource_driver_v5.py',
        'analytic_delta_jac_adapter.py', 'nodal_jac_checkpoint.py',
        'prefix_resource_driver_v4.py', 'material_core_evaluate_cache.py',
        'prefix_resource_driver_v2.py', 'cached_fourier_tables.py',
        'prefix_resource_driver.py')
    return [Path(__file__).resolve(), QR, INNER_QR, ROOT/'block_qr_v2.py', PORTABLE,
        SCRIPTS/'resume_20261126/streamed_release_prefix_driver.py',
        SCRIPTS/'resume_m3/round_raw_lib/analytic_adaptive_core_jac.py',
        ROOT/'analytic/material_delta_column.py',
        *[DESIGN/name for name in design]]


def delegated_argv(original_arguments, block):
    return [str(QR), '--mmap-disk-margin-mib', '512',
            '--base-driver', str(BASE), '--rhs-block', str(block),
            '--memory-external-margin-mib', '512', '--storage-disk-margin-mib', '512',
            *map(str, original_arguments)]


def inner_qr_argv(original_arguments, block):
    return [str(INNER_QR), *delegated_argv(original_arguments, block)[3:]]


def resource_argv(original_arguments, block):
    return [str(V5), '--rhs-block', str(block), *map(str, original_arguments)]


def evidence_paths(out):
    out = Path(out)
    internal = ('radial-batching.json', 'fourier-table-cache.json',
        'material-core-evaluate-cache.json', 'analytical-delta-and-nodal-checkpoints.json',
        'complete-csr-assembly.json', 'prefactor-storage-and-flow-lifecycle.json',
        'latest-complete-prefactor-storage-budget.json',
        'accepted-newton-checkpoint-execution.json')
    result = {name:out/name for name in internal}
    for suffix in ('block-qr.jsonl', 'direct-csr.jsonl', 'flow-lifecycle.jsonl',
                   'prefactor-nodal-budget.jsonl', 'csr-prefactor-mapped.jsonl'):
        result[suffix] = out.with_name(out.name+'-'+suffix)
    return result


def check_mapped_trace(path, expected_command, expected_factors):
    """Check actual full mapped factor/solve returns without reopening scratch arrays.

    The trace is scientific execution metadata, not an accepted field. The
    complete original nonlinear/native/outer gates still decide acceptance.
    A caller can also use this helper on a genuine already returned design
    trace; that does not fabricate an execution of this new outer wrapper.
    """
    requests, ended = [], []
    starts, returned, allowed, solves = {}, {}, set(), []
    for line in Path(path).read_text().splitlines():
        row = json.loads(line)
        event = row.get('event')
        if event == 'complete_CSR_before_QR_mapping_requested':
            requests.append(row)
        elif event == 'complete_CSR_prefactor_constructor_start':
            ordinal = row['ordinal']
            if ordinal in starts or row['disk_free_bytes'] < row['disk_required_bytes']:
                raise ValueError('A complete mapped factor has a duplicate or unpaid disk start')
            starts[ordinal] = row
        elif event == 'actual_mapped_CSR_released_before_recursive_QR_gate':
            if row['ordinal'] not in starts or row.get('logical_mapped_bytes_credited_as_RSS') is not False:
                raise ValueError('The actual prefactor RAM gate lost its own source or RSS accounting')
            if row.get('allowed') is True:
                allowed.add(row['ordinal'])
        elif event == 'complete_CSR_and_QR_mapped_return':
            ordinal = row['ordinal']
            if ordinal in returned or ordinal not in starts or ordinal not in allowed:
                raise ValueError('A complete mapped factor returned without its current storage gate')
            if (row.get('composite_CSR_is_mapped_not_anonymous') is not True
                    or row.get('frozen_factor_only_component_CSR_location_field_not_applicable') is not True
                    or row['CSR_storage'].get('last_solve_page_release', {}).get(
                        'clean_mapped_pages_advised_DONTNEED') is not True):
                raise ValueError('The real complete prefactor CSR mapping/release contract differs')
            returned[ordinal] = row
        elif event == 'complete_mapped_solve_return_or_exception':
            if row['ordinal'] not in returned or row.get('composite_CSR_is_mapped_not_anonymous') is not True:
                raise ValueError('The complete mapped solve has no returned full factor')
            for name in ('CSR_storage', 'factor_component_storage'):
                if row[name].get('last_solve_page_release', {}).get('clean_mapped_pages_advised_DONTNEED') is not True:
                    raise ValueError('The complete mapped state was not released for original nonlinear work')
            solves.append(row)
        elif event == 'complete_mapped_entry_return_or_exception':
            ended.append(row)
    if (len(requests) != 1 or len(ended) != 1
            or requests[0].get('command') != list(map(str, expected_command))
            or requests[0].get('all_original_equations_and_gates_retained') is not True
            or requests[0].get('complete_original_CSR_object_and_entries_retained') is not True
            or requests[0].get('complete_warm_matrix_and_factor_residency_budgeted') is not True
            or set(starts) != set(expected_factors) or set(returned) != set(expected_factors)
            or ended[0].get('complete_factors_requested') != len(expected_factors)
            or ended[0].get('original_math_and_acceptance_changed') is not False
            or (expected_factors and not solves)):
        raise ValueError('The genuine complete mapped execution trace is incomplete')
    for source, digest in requests[0]['source_hashes'].items():
        if sha(source) != digest:
            raise ValueError('The bound actual mapped execution source changed: '+source)
    return dict(complete_factors=len(returned), recorded_mapped_solve_returns=len(solves),
        complete_CSR_before_QR_and_all_factors_mapped=True,
        source_trace=ref(path), original_math_or_gates_changed=False)


def check_prefactor_trace(out, expected_base, expected_factors):
    """Check genuine pre-J storage receipts and the original lifecycle identity."""
    paths = evidence_paths(out)
    life = load(paths['prefactor-storage-and-flow-lifecycle.json'])
    if (life.get('actual_command') != list(map(str, expected_base))
            or life.get('map_scope') != 'complete_CSR_before_QR_and_all_factors_after_QR'
            or life.get('original_math_and_gates_changed') is not False):
        raise ValueError('The original mapped lifecycle/base-driver identity changed')
    for source, digest in life['source_hashes'].items():
        if sha(source) != digest:
            raise ValueError('The actual prefactor source changed: '+source)
    if expected_factors:
        permitted = set()
        for line in paths['prefactor-nodal-budget.jsonl'].read_text().splitlines():
            row = json.loads(line)
            if (row.get('event') != 'complete_nodal_CSR_prefactor_storage_gate'
                    or row.get('actual_command') != list(map(str, expected_base))
                    or row.get('mapped_logical_bytes_credited_as_RSS') is not False
                    or row.get('original_CSR_assembly_and_complete_warm_solve_residency_retained') is not True
                    or row.get('original_nonlinear_or_acceptance_gates_changed') is not False):
                raise ValueError('The complete mapped nodal resource gate changed')
            estimate = row['estimate']
            if (estimate.get('storage_scope') != 'complete_CSR_before_QR_and_all_factors_after_QR'
                    or estimate.get('complete_original_CSR_remains_anonymous') is not False
                    or estimate.get('anonymous_RSS_is_the_only_MemAvailable_credit') is not True
                    or estimate.get('mapped_logical_bytes_are_never_RSS_credit') is not True
                    or estimate.get('all_CSR_and_factor_pages_counted_in_complete_warm_solve') is not True
                    or estimate['external_margin_bytes'] < 512*2**20
                    or row['full_factor_backing_plus_disk_margin_bytes'] < (
                        estimate['disk_backing']['total_backing_and_manifest_upper_bytes']+512*2**20)):
                raise ValueError('The full original RAM/disk budget lost a required resource phase')
            if row.get('allowed') is True:
                if row.get('RAM_allowed') is not True or row.get('disk_allowed') is not True:
                    raise ValueError('An actual admitted mapped stage did not pass both resource gates')
                permitted.add(row['ordinal'])
        if permitted != set(expected_factors):
            raise ValueError('The accepted complete factors lack their individual pre-J storage gates')
        latest = load(paths['latest-complete-prefactor-storage-budget.json'])
        if latest.get('allowed') is not True or latest.get('ordinal') != max(expected_factors):
            raise ValueError('The latest full prefactor storage gate is not the final original factor')
    return dict(lifecycle=ref(paths['prefactor-storage-and-flow-lifecycle.json']),
        accepted_pre_J_storage_gates=len(expected_factors),
        complete_CSR_before_QR_and_all_factors_mapped=True,
        original_math_or_gates_changed=False)


def check_execution(path, actual_argv, wrapper, portable, block, expected_sha=None):
    """Verify honest QR provenance without assigning a mathematical acceptance."""
    path, wrapper, portable = map(lambda p:Path(p).resolve(), (path, wrapper, portable))
    if expected_sha is not None and sha(path) != expected_sha:
        raise ValueError('The saved actual-DN QR execution record changed')
    actual_argv = list(map(str, actual_argv))
    if (wrapper != Path(__file__).resolve() or portable != PORTABLE
            or type(block) is not int or block < 1
            or actual_argv[1:4] != [str(wrapper), '--rhs-block', str(block)]):
        raise ValueError('The actual prefix QR wrapper/argument identity differs')
    arguments = actual_argv[4:]
    portable_argv = [actual_argv[0], str(PORTABLE), *arguments]
    delegated = delegated_argv(arguments, block)
    record = load(path)
    if (record.get('schema') != SCHEMA or record.get('wrapper_returned_normally') is not True
            or record.get('command') != actual_argv[1:]
            or record.get('original_portable_argv') != portable_argv
            or record.get('delegated_in_process_application_argv') != delegated
            or record.get('radial_rhs_jacobian_block') != block
            or record.get('original_equations_changed') is not False
            or record.get('original_outer_native_or_acceptance_gates_changed') is not False
            or record.get('full_native_J_replaced_by_prefix_QR') is not False
            or record.get('numerical_prefix_linear_arithmetic_changed') is not True
            or record.get('original_additive_delta_column_analytical') is not True
            or record.get('complete_CSR_before_QR_and_all_factors_mapped') is not True
            or record.get('old_anonymous_QR_execution_claimed') is not False
            or record.get('original_inner_QR_application_argv') != inner_qr_argv(arguments, block)
            or record.get('external_RAM_margin_mib') != 512
            or record.get('external_disk_margin_mib') != 512
            or record.get('bound_sources_unchanged_at_return') is not True):
        raise ValueError('The actual complete QR execution contract differs')
    sources = {str(p):sha(p) for p in source_files()}
    if record.get('source_hashes') != sources:
        raise ValueError('The complete QR resource source binding differs')
    start_path = checked(record['start_record'])
    if start_path != path.parent.with_name(path.parent.name+'-actual-dn-mapped-qr-start.json'):
        raise ValueError('The complete QR execution has another immutable start record')
    start = load(start_path)
    if (start.get('wrapper_returned_normally') is not False
            or any(start.get(key) != record.get(key) for key in (
                'schema', 'command', 'source_hashes', 'original_portable_argv',
                'delegated_in_process_application_argv', 'original_inner_QR_application_argv',
                'radial_rhs_jacobian_block', 'complete_CSR_before_QR_and_all_factors_mapped',
                'old_anonymous_QR_execution_claimed', 'external_RAM_margin_mib', 'external_disk_margin_mib'))):
        raise ValueError('The final QR execution does not continue its real start record')
    paths = evidence_paths(path.parent)
    bound = record.get('evidence', {})
    required = set(paths)-{'accepted-newton-checkpoint-execution.json',
                          'prefactor-nodal-budget.jsonl', 'direct-csr.jsonl',
                          'latest-complete-prefactor-storage-budget.json'}
    if not required <= set(bound) or set(bound)-set(paths):
        raise ValueError('The complete actual QR resource sidecars are missing')
    for name, value in bound.items():
        if checked(value) != paths[name].resolve():
            raise ValueError('A QR resource sidecar points outside its true output')
    radial = load(paths['radial-batching.json'])
    if (radial.get('command') != resource_argv(arguments, block)
            or radial.get('wrapper_sha256') != sha(DESIGN/'prefix_resource_driver.py')
            or radial.get('original_driver_sha256') != sha(PORTABLE)
            or radial.get('radial_rhs_jacobian_block') != block
            or radial.get('initial_domain_rhs_batched') is not True
            or radial.get('original_all_nodes_and_components_evaluated') is not True
            or radial.get('mathematical_parameters_changed') is not False
            or radial.get('original_gates_relaxed') is not False):
        raise ValueError('The bounded original entry/RHS/J execution differs')
    assembly = load(paths['complete-csr-assembly.json'])
    if (assembly.get('all_original_entries_retained') is not True
            or assembly.get('numerical_block_arithmetic_changed') is not False
            or assembly.get('original_gates_changed') is not False):
        raise ValueError('The complete original CSR assembly contract differs')
    factors, returned, solves, begin, end = set(), set(), 0, None, None
    with paths['block-qr.jsonl'].open() as stream:
        for line in stream:
            row = json.loads(line)
            kind = row.get('event')
            if kind == 'replacement_requested':
                if begin is not None:
                    raise ValueError('More than one complete QR execution was joined')
                begin = row
            elif kind == 'factor_start':
                if row['factor'] in factors:
                    raise ValueError('Repeated complete QR factor identity')
                factors.add(row['factor'])
            elif kind == 'factor_return':
                if row['factor'] not in factors or row['factor'] in returned:
                    raise ValueError('A complete QR factor return has no unique start')
                returned.add(row['factor'])
            elif kind == 'solve_return':
                if row['factor'] not in returned:
                    raise ValueError('A QR solve has no complete returned factor')
                solves += 1
            elif kind == 'driver_return_or_exception':
                end = row
    if (begin is None or end is None or begin.get('command') != inner_qr_argv(arguments, block)
            or begin.get('equations_changed') is not False
            or begin.get('original_nonlinear_gates_changed') is not False
            or factors != returned or end.get('factor_count') != len(factors)):
        raise ValueError('The complete actual prefix QR factor trace is incomplete')
    # An already converged initial collocation field can legitimately need no
    # factor. Original nonlinear/RMS/metric/actual-boundary gates decide that.
    if factors and (not solves or 'accepted-newton-checkpoint-execution.json' not in bound
                    or 'prefactor-nodal-budget.jsonl' not in bound
                    or 'direct-csr.jsonl' not in bound
                    or 'latest-complete-prefactor-storage-budget.json' not in bound):
        raise ValueError('Actual QR factors lack their full nodal/resource execution')
    mapped = check_mapped_trace(paths['csr-prefactor-mapped.jsonl'], delegated, factors)
    if mapped['recorded_mapped_solve_returns'] != solves:
        raise ValueError('The original full solves and complete mapped solve receipts differ')
    expected_base = [str(BASE), *inner_qr_argv(arguments, block)[3:]]
    check_prefactor_trace(path.parent, expected_base, factors)
    return ref(path)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--rhs-block', type=int, default=8)
    options, arguments = parser.parse_known_args()
    if type(options.rhs_block) is not int or options.rhs_block < 1:
        raise ValueError('The complete original radial block must be positive')
    command = list(sys.argv)
    delegated = delegated_argv(arguments, options.rhs_block)
    sys.path[:0] = [str(ROOT), str(DESIGN)]
    spec = importlib.util.spec_from_file_location('_actual_dn_complete_qr_driver', QR)
    qr = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = qr
    spec.loader.exec_module(qr)
    if '--help' in arguments or '-h' in arguments:
        sys.argv = delegated
        return qr.main()
    for flag in ('--outdir', '--raw-restart', '--tail-config', '--modes', '--core-module'):
        if arguments.count(flag) != 1:
            raise ValueError('An original actual-DN command needs exactly one '+flag)
    if any(flag in arguments for flag in ('--skip-audit', '--probe-only', '--base-driver')):
        raise ValueError('No alternate solver or unpaid original gate may enter this adapter')
    out = Path(arguments[arguments.index('--outdir')+1]).resolve()
    if out.exists():
        raise FileExistsError(out)
    sources = {str(p):sha(p) for p in source_files()}
    start = out.with_name(out.name+'-actual-dn-mapped-qr-start.json')
    record = dict(schema=SCHEMA, scope=__doc__, command=command,
        original_portable_argv=[sys.executable, str(PORTABLE), *arguments],
        delegated_in_process_application_argv=delegated,
        original_inner_QR_application_argv=inner_qr_argv(arguments, options.rhs_block),
        delegated_is_in_process_not_a_fabricated_OS_child=True,
        radial_rhs_jacobian_block=options.rhs_block, source_hashes=sources,
        wrapper_returned_normally=False, original_equations_changed=False,
        original_outer_native_or_acceptance_gates_changed=False,
        full_native_J_replaced_by_prefix_QR=False,
        numerical_prefix_linear_arithmetic_changed=True,
        original_additive_delta_column_analytical=True,
        original_complete_state_and_all_support_columns_retained=True,
        complete_CSR_before_QR_and_all_factors_mapped=True,
        old_anonymous_QR_execution_claimed=False,
        external_RAM_margin_mib=512, external_disk_margin_mib=512,
        floating_point_bit_identity_claimed=False, complete_surface=False)
    with start.open('x') as stream:
        stream.write(json.dumps(record, indent=2, allow_nan=False)+'\n')
    begin = time.monotonic()
    sys.argv = delegated
    try:
        value = qr.main()
        record['wrapper_returned_normally'] = True
        return value
    except BaseException as error:
        record['exception'] = type(error).__name__+': '+str(error)
        raise
    finally:
        sys.argv = command
        record['seconds_this_wrapper'] = time.monotonic()-begin
        record['start_record'] = ref(start)
        record['evidence'] = {name:ref(path) for name,path in evidence_paths(out).items()
                              if path.is_file()}
        record['bound_sources_unchanged_at_return'] = (
            sources == {str(p):sha(p) for p in source_files()})
        if out.is_dir():
            destination = out/'actual-dn-mapped-qr-execution.json'
            with destination.open('x') as stream:
                stream.write(json.dumps(record, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
