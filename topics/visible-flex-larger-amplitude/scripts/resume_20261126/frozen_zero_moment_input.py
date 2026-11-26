#!/usr/bin/env python3
"""Bind eighteen literal fixed moment-Q control words from one actual report.

Only stdlib JSON, source-byte and binary64-word attribution is performed.
No moment, inverse, field, endpoint root, residual, J or Jtranspose is
computed. The matrices become a NEW fixed mathematical control input;
they are never recomputed as current omega/core/H change.
"""
import argparse
import ast
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import struct

SCHEMA = 'frozen-zero-endpoint-moment-Q-input-v1'
DEFINITION_SCHEMA = 'literal-two-bubble-endpoint-Q-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
TRACE_SCHEMA = 'actual-zero-first-eight-endpoint-replay-v1'
TRACE_SOURCE_SHA = '73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54'
ACTUAL_TRACE_REPORT_SHA = '26b094fef8baf6ff2ecdda5d1a0f5a8be7383e5171733320be959a22d83cb47e'
ACTUAL_FAILED_REPORT_SHA = '4341323c805a3e4f38c20c6e5264e9875b8b717082793ece982c029f488ed744'
ACTUAL_OLD_ZERO_MODEL = '29f540c6fc265b977a388813dcd0d3faddfd48fd06d40c7f6c4bcae5c848281b'
ACTUAL_INITIAL_POINT = 'cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3'
PINS = {
    'trace': ('scripts/resume_20261126/trace_zero_initial_endpoint_failure.py', TRACE_SOURCE_SHA),
    'initial_binding': ('scripts/resume_20261126/diagnose_zero_initial_chord.py', '65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0'),
    'original_endpoint': ('scripts/resume_20261126/so3_zero_closure_endpoint_operator.py', '5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46'),
    'original_driver': ('scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py', 'b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b'),
}
DEFINITION_KEYS = {
    'schema', 'Q0_binary64_hex', 'exact_relative_bubble_nodes',
    'fixed_scalar_metric_identity_sha256', 'initial_reference_bundle_sha256',
    'base_model_identity_sha256', 'trace_report_sha256', 'trace_source_sha256',
    'trace_original_model_identity_sha256', 'trace_initial_full_point_sha256',
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def is_digest(value):
    return isinstance(value, str) and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def source_registry(path):
    values = [ast.literal_eval(node.value) for node in ast.parse(Path(path).read_text()).body
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SOURCE_PINS'
            for t in node.targets)]
    if len(values) != 1:
        raise ValueError('The original complete driver has one literal source table')
    return values[0]


def validate_sources(repo):
    topic = Path(repo).resolve()/TOPIC
    result = {}
    for role, (relative, digest) in PINS.items():
        path = topic/relative
        if sha(path) != digest:
            raise ValueError('Changed actual whole moment input source '+role)
        result[role] = dict(repo_relative_path=TOPIC+'/'+relative, sha256=digest,
            bytes=path.stat().st_size)
    original = topic/PINS['original_driver'][0]
    for role, (relative, digest) in source_registry(original).items():
        if sha(topic/relative) != digest:
            raise ValueError('Changed complete original zero-model source '+role)
        result['original_driver_'+role] = dict(repo_relative_path=TOPIC+'/'+relative,
            sha256=digest, bytes=(topic/relative).stat().st_size)
    return result


def validate_definition(definition, expected_identity=None):
    if not isinstance(definition, dict) or set(definition) != DEFINITION_KEYS:
        raise ValueError('Keep the complete declared fixed-Q definition without hidden mutable parameters')
    if definition['schema'] != DEFINITION_SCHEMA:
        raise ValueError('Unknown complete fixed literal-Q mathematical input')
    identity = canonical(definition)
    if expected_identity is not None and (not is_digest(expected_identity) or identity != expected_identity):
        raise ValueError('The fixed-Q definition changed from the explicitly supplied complete identity')
    for key in ('fixed_scalar_metric_identity_sha256', 'initial_reference_bundle_sha256',
            'base_model_identity_sha256', 'trace_report_sha256', 'trace_source_sha256',
            'trace_original_model_identity_sha256', 'trace_initial_full_point_sha256'):
        if not is_digest(definition[key]):
            raise ValueError('Every fixed control origin/target identity must be an actual SHA256')
    if (definition['trace_report_sha256'] != ACTUAL_TRACE_REPORT_SHA
            or definition['trace_source_sha256'] != TRACE_SOURCE_SHA
            or definition['trace_original_model_identity_sha256'] != ACTUAL_OLD_ZERO_MODEL
            or definition['trace_initial_full_point_sha256'] != ACTUAL_INITIAL_POINT):
        raise ValueError('This complete source selects the actual returned stage-15 control candidate only')
    nodes = definition['exact_relative_bubble_nodes']
    if not isinstance(nodes, list) or len(nodes) != 2 or any(not isinstance(row, list) or len(row) != 3 for row in nodes):
        raise ValueError('Retain both complete exact bubble triples')
    normalized = [[str(Fraction(value)) for value in row] for row in nodes]
    if nodes != normalized or normalized != [['1/32','1/4','15/32'],['17/32','3/4','31/32']]:
        raise ValueError('The moment candidate belongs to the actual wide-support exact bubbles')
    words = definition['Q0_binary64_hex']
    if (not isinstance(words, list) or len(words) != 2
            or any(not isinstance(matrix, list) or len(matrix) != 3 for matrix in words)
            or any(not isinstance(row, list) or len(row) != 3 for matrix in words for row in matrix)):
        raise ValueError('Keep all eighteen literal matrix words with shape (2,3,3)')
    for matrix in words:
        for i, row in enumerate(matrix):
            for j, word in enumerate(row):
                if not isinstance(word, str):
                    raise ValueError('Every selected Q parameter is an exact canonical binary64 hex word')
                value = float.fromhex(word)
                if not math.isfinite(value) or value.hex() != word:
                    raise ValueError('Nonfinite or noncanonical literal fixed-Q word')
                # The selected v_i=(v_x,0,v_z) and its exact block covariance
                # force this polar-to-axial reflection pattern. Preserve
                # actual signed-zero words; never silently project inputs.
                if not ((i == 1) != (j == 1)) and value != 0:
                    raise ValueError('The supplied literal control violates the required exact reflection parity')
    return identity


def from_trace(repo, trace_report, *, trace_report_sha256, failed_report=None,
               expected_definition_identity_sha256=None):
    if trace_report_sha256 != ACTUAL_TRACE_REPORT_SHA or sha(trace_report) != trace_report_sha256:
        raise ValueError('Bind the exact actual 26b094 trace bytes, not an unexecuted replacement')
    sources = validate_sources(repo)
    before = sha(trace_report)
    report = json.loads(Path(trace_report).read_text())
    if (report.get('schema') != TRACE_SCHEMA or report.get('source_sha256') != TRACE_SOURCE_SHA
            or report.get('complete') is not True
            or report.get('exact_same_initial_point_sha256') != ACTUAL_INITIAL_POINT
            or report.get('exact_same_model_identity_sha256') != ACTUAL_OLD_ZERO_MODEL
            or report.get('new_input_or_checkpoint_or_field_written') is not False
            or report.get('original_initial_point_and_accurate_target_unchanged') is not True
            or any(report.get(key) != 0 for key in ('full_residual_calls','full_J_calls','full_Jtranspose_calls'))):
        raise ValueError('The actual moment origin must retain the full original initial point and complete executed trace')
    method = report['complete_original_method_derivation']
    if (method.get('original_endpoint_source_sha256') != PINS['original_endpoint'][1]
            or method.get('removing_exactly_observers_recovers_original_entire_method_AST') is not True
            or method.get('q_original_method_replaced') is not False
            or method.get('physical_equation_or_jacobian_replaced') is not False):
        raise ValueError('Do not accept a trace of another physical root method')
    binding = report['actual_initial_input']
    if (binding.get('schema') != 'actual-zero-original-initial-point-not-a-field-v1'
            or binding.get('source_sha256') != PINS['initial_binding'][1]
            or binding.get('actual_initial_point_sha256') != ACTUAL_INITIAL_POINT
            or binding.get('actual_zero_model_identity_sha256') != ACTUAL_OLD_ZERO_MODEL
            or binding.get('complete_original_free_point_reread') is not True
            or binding.get('current_core_exactly_equals_fixed_chart_core') is not True
            or binding.get('complete_new_initial_field_exists') is not False
            or binding.get('actual_failed_driver_source_sha256') != PINS['original_driver'][1]
            or canonical(binding['fixed_scalar_profile_definition']) != binding['fixed_scalar_metric_identity_sha256']
            or report['exact_same_fixed_scalar_identity_sha256'] != binding['fixed_scalar_metric_identity_sha256']):
        raise ValueError('The fixed input origin must bind its whole initial/base/reference/scalar identity')
    recorded_failure = binding['actual_failed_report']
    failure_path = Path(recorded_failure['path']) if failed_report is None else Path(failed_report)
    if recorded_failure['sha256'] != ACTUAL_FAILED_REPORT_SHA or sha(failure_path) != ACTUAL_FAILED_REPORT_SHA:
        raise ValueError('Bind the actual complete 434132 initial failure, not an accepted or altered field')
    failure = json.loads(failure_path.read_text())
    model = failure['representation']
    if (failure.get('schema') != 'complete-independent-axisymmetric-fixed-deep-zero-closure-so3-QP-v1'
            or failure.get('source_sha256') != PINS['original_driver'][1]
            or failure.get('complete') is not False
            or failure.get('stop_reason') != 'actual_initial_zero_closure_field_read_failed'
            or failure.get('initial') is not None or failure.get('restart') is not None
            or failure.get('direct_base_seed') is not None
            or canonical(model) != ACTUAL_OLD_ZERO_MODEL
            or model['source_sha256'] != PINS['original_endpoint'][1]
            or model['base_model_identity_sha256'] != binding['actual_base_model_identity_sha256']
            or canonical(model['base_complete_model']) != binding['actual_base_model_identity_sha256']
            or model['fixed_scalar_metric_identity_sha256'] != binding['fixed_scalar_metric_identity_sha256']
            or model['base_complete_model']['initial_reference_model_identity_sha256'] != binding['actual_reference_model_identity_sha256']
            or failure['bundle_sha256'] != binding['actual_inputs']['reference_bundle']['sha256']):
        raise ValueError('The actual trace origin differs from the complete original model or reference')
    topic = Path(repo).resolve()/TOPIC
    for role, (_, digest) in source_registry(topic/PINS['original_driver'][0]).items():
        if failure['source_sha256_by_role'].get(role) != digest:
            raise ValueError('A complete failed-driver source role changed: '+role)
    nodes = model['exact_relative_bubble_nodes']
    if (failure['working_evaluation']['exact_relative_bubble_nodes'] != nodes
            or report['actual_root_policy'] != failure['working_evaluation']['endpoint_root_policy']):
        raise ValueError('Keep the exact support and true recorded original root policy')
    moments = report['complete_working_bubble_moments']
    if (moments.get('candidate_available') is not True
            or moments.get('candidate_Q_installed') is not False
            or moments.get('actual_original_radial_cells') != 922
            or moments.get('actual_quadrature_order') != 8
            or moments.get('original_total_source_sha256') != PINS['original_endpoint'][1]
            or moments.get('moments_are_working_values_not_true_intervals') is not True
            or moments.get('true_moment_integration_or_FloatingPoint_error_certified') is not False):
        raise ValueError('Only the actual complete-rule uninstalled literal moment candidate may be frozen')
    record = moments['candidate_Q_at_angle_zero']
    values, words = record['values'], record['exact_binary64_hex_words']
    if (record['shape'] != [2,3,3] or record['dtype'] != 'float64'
            or record.get('finite') is not True or len(values) != 18 or len(words) != 18):
        raise ValueError('The actual candidate must retain exactly eighteen complete finite words')
    for value, word in zip(values, words):
        if (isinstance(value, bool) or not isinstance(value, (int,float))
                or not math.isfinite(float(value))
                or struct.pack('<d', float(value)) != struct.pack('<d', float.fromhex(word))):
            raise ValueError('The candidate numeric word and exact hex word do not agree')
    Q0 = [[words[9*i+3*j:9*i+3*j+3] for j in range(3)] for i in range(2)]
    definition = dict(schema=DEFINITION_SCHEMA, Q0_binary64_hex=Q0,
        exact_relative_bubble_nodes=nodes,
        fixed_scalar_metric_identity_sha256=binding['fixed_scalar_metric_identity_sha256'],
        initial_reference_bundle_sha256=binding['actual_inputs']['reference_bundle']['sha256'],
        base_model_identity_sha256=binding['actual_base_model_identity_sha256'],
        trace_report_sha256=before, trace_source_sha256=TRACE_SOURCE_SHA,
        trace_original_model_identity_sha256=ACTUAL_OLD_ZERO_MODEL,
        trace_initial_full_point_sha256=ACTUAL_INITIAL_POINT)
    identity = validate_definition(definition, expected_definition_identity_sha256)
    if sha(trace_report) != before or sha(failure_path) != ACTUAL_FAILED_REPORT_SHA:
        raise ValueError('The actual small input changed while being bound')
    return dict(schema=SCHEMA, definition=definition, definition_identity_sha256=identity,
        provenance=dict(binding_source_sha256=sha(__file__),
            actual_trace_report=dict(sha256=before, bytes=Path(trace_report).stat().st_size,
                source_commit=report['source_commit'], github_run_id=45820592817, run_attempt=1, stage=15),
            actual_failed_report=dict(sha256=ACTUAL_FAILED_REPORT_SHA, bytes=failure_path.stat().st_size),
            complete_source_records=sources,
            literal_selection='exactly the recorded 18 candidate_Q_at_angle_zero binary64 hex words; no new moment or inverse',
            formula_origin='v_i are full 922-cell order-8 working bubble moments with selected exact y=0; Q_i(0)=[v_i]cross*(sum(|v_i|^2 I-v_i v_i^T))^-1',
            fixed_extension='Q_i(phi0)=Rz(theta0(phi0))*Q_i(0)*Rz(theta0(phi0))^T using only the fixed initial chart',
            current_free_variables_never_recompute_Q=True,
            working_matrix_is_exact_true_endpoint_right_inverse_claimed=False,
            original_root_or_field_success_inherited=False,
            true_moment_error_or_uniform_IFT_certified=False,
            new_control_parameters=18, raw_scientific_field_arrays_copied=False,
            field_calls=0, endpoint_root_calls=0, J_calls=0, Jtranspose_calls=0))


def from_parameter_file(path, *, input_sha256, expected_definition_identity_sha256):
    if not is_digest(input_sha256) or sha(path) != input_sha256:
        raise ValueError('Bind the complete published small fixed-Q parameter file by actual bytes')
    if not is_digest(expected_definition_identity_sha256):
        raise ValueError('The small-file route needs the SAME explicit complete Q definition identity')
    before = sha(path)
    value = json.loads(Path(path).read_text())
    if value.get('schema') != SCHEMA:
        raise ValueError('Unknown complete literal fixed moment-Q input file')
    identity = validate_definition(value['definition'], expected_definition_identity_sha256)
    if value.get('definition_identity_sha256') != identity or sha(path) != before:
        raise ValueError('The complete small control input changed')
    provenance = value.get('provenance', {})
    if (provenance.get('actual_trace_report', {}).get('sha256') != ACTUAL_TRACE_REPORT_SHA
            or provenance.get('new_control_parameters') != 18
            or provenance.get('current_free_variables_never_recompute_Q') is not True):
        raise ValueError('Retain the published actual frozen-input provenance')
    return value


def bind_to_base(value, *, base_model, initial_reference_bundle_sha256,
                 fixed_scalar_metric_identity_sha256, bubble_nodes):
    if value.get('schema') != SCHEMA:
        raise ValueError('Use the complete independently bound frozen moment input')
    definition = value['definition']
    identity = validate_definition(definition, value.get('definition_identity_sha256'))
    if (canonical(base_model) != definition['base_model_identity_sha256']
            or initial_reference_bundle_sha256 != definition['initial_reference_bundle_sha256']
            or fixed_scalar_metric_identity_sha256 != definition['fixed_scalar_metric_identity_sha256']
            or [[str(Fraction(v)) for v in row] for row in bubble_nodes]
                != definition['exact_relative_bubble_nodes']):
        raise ValueError('The fixed Q parameters belong to another base, chart, scalar target or bubble support')
    return identity


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    choice = p.add_mutually_exclusive_group(required=True)
    choice.add_argument('--trace-report', type=Path)
    choice.add_argument('--moment-input', type=Path)
    p.add_argument('--trace-report-sha256')
    p.add_argument('--failed-report', type=Path)
    p.add_argument('--moment-input-sha256')
    p.add_argument('--expected-definition-sha256')
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if a.output.exists():
        raise FileExistsError('Do not overwrite a returned frozen parameter file')
    if a.trace_report is not None:
        value = from_trace(a.repo, a.trace_report,
            trace_report_sha256=a.trace_report_sha256, failed_report=a.failed_report,
            expected_definition_identity_sha256=a.expected_definition_sha256)
    else:
        value = from_parameter_file(a.moment_input, input_sha256=a.moment_input_sha256,
            expected_definition_identity_sha256=a.expected_definition_sha256)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(schema=SCHEMA, binding_source_sha256=sha(__file__),
        complete=True, output=file_record(a.output),
        definition=value['definition'], definition_identity_sha256=value['definition_identity_sha256'],
        new_control_parameters=18, field_calls=0, endpoint_root_calls=0,
        J_calls=0, Jtranspose_calls=0), separators=(',', ':'), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
