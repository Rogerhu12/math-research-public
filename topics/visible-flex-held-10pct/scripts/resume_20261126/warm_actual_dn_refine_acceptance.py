#!/usr/bin/env python3
"""Read-only acceptance gate for a same-problem actual nonlinear-DN refinement.

This validates one saved complete finite return and its original full-H
packet. It invokes no model, BVP, DN, metric audit or geometry certificate.
Passing it does not certify a Cartesian seam or an infinite closed surface.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import numpy as np

KIND = 'warm-supported-material-phase-fixed-metric-actual-dn-refinement-v1'
SHORT_BRIDGE_SHA = '7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4'
TAIL_SOURCES = {
    '950f-tail-client-v3.py', '950f-tail-stage-port-v3.mjs',
    '950f-tail-stage-core.mjs', '950f-tail-stage-split.mjs',
    '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
    'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs',
}


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            result.update(block)
    return result.hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def finite_gate(value, upper):
    return isinstance(value, (int, float)) and math.isfinite(value) and 0 <= value <= upper


def same_path(left, right):
    return Path(left).resolve() == Path(right).resolve()


def check_hash(path, expected, label):
    if sha(path) != expected:
        raise ValueError(label+' changed: '+str(path))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def accepted_actual_input(path, *, repo=None):
    """Return the unchanged run dict after complete finite/provenance checks."""
    path = Path(path).resolve()
    record = load(path)
    if record.get('model_kind') != KIND:
        raise ValueError('Require an actual warm nonlinear-DN run, not a linear or warmup record')
    repository = Path(repo if repo is not None else record['repository']).resolve()
    current = repository/'topics/visible-flex-held-10pct/scripts/resume_20261126'
    solver_path = current/'warm_actual_dn_refine_step.py'
    geometry = module('_actual_refinement_geometry_contract', current/'warm_actual_dn_refine_model.py')
    parent_path = Path(record['actual_source_run']).resolve()
    if same_path(parent_path, path):
        raise ValueError('An actual refinement cannot use itself as its accepted input')
    check_hash(parent_path, record['actual_source_run_sha256'], 'The accepted actual predecessor')
    parent = geometry.accepted_input(parent_path, repo=repository)
    geometry.validate_refinement_definition(repository, record, parent)
    check_hash(parent['result']['full_height_record'], record['actual_source_full_height_sha256'],
               'The complete accepted actual shooting initializer')
    if (record.get('status') != 'audited_finite_actual_dn_candidate'
            or record.get('error') or record.get('fixed_metric') is not True
            or record.get('finite_actual_dn_candidate_pass') is not True
            or record.get('solver_success') is not True
            or record.get('solver_invoked') is not True
            or record.get('acceptance_kind') != 'actual_nonlinear_dn_refinement_return'
            or record.get('terminal_kind') != 'original_actual_nonlinear_dn'
            or record.get('actual_tail_requested') is not True
            or record.get('original_actual_nonlinear_tail') is not True
            or record.get('parameter_zero_meaning') != 'log(q_aux/gauge_q)'
            or record.get('mean_nodes') != 1168 or record.get('bc_normalization') != .02):
        raise ValueError('Require this actual accepted warm nonlinear-DN return')
    raw = record.get('raw_return', {})
    if raw.get('success') is not True or raw.get('status') != 0:
        raise ValueError('The actual inner BVP has no successful raw return')
    gates = record['gates']
    for key, upper in (('tol', 1e-6), ('bc_tol', 1e-7), ('physical_bc_tol', 2e-9)):
        if not finite_gate(gates.get(key), upper) or gates[key] == 0:
            raise ValueError('An original finite gate was changed: '+key)
    if gates.get('tail_solve_tolerance') != 2e-9 or gates.get('original_outer_budget') != 8:
        raise ValueError('The original nonlinear-tail or outer-iteration gate changed')
    for value, upper in ((raw.get('rms'), gates['tol']),
                         (record.get('actual_scaled_bc_max'), gates['bc_tol']),
                         (record.get('actual_physical_bc_max'), gates['physical_bc_tol'])):
        if not finite_gate(value, upper):
            raise ValueError('An actual original RMS or boundary gate failed')
    modes = int(record['modes'])
    rows = record.get('metric_diagnostics', [])
    if (not rows or any(row['angular'] < 16*(3*modes+1)
                       or not finite_gate(row['legacy_max_component_fft_l1'], 1e-6)
                       or not finite_gate(row['sample_operator_max'], 1e-6) for row in rows)
            or sorted(row['angular'] for row in rows) != sorted(record['actual_audit_angular'])):
        raise ValueError('The complete actual metric audit failed or changed grids')
    for source, digest in record['source_hashes'].items():
        check_hash(source, digest, 'An actual bound numerical source')
    if record['source_hashes'].get(str(solver_path)) != sha(solver_path):
        raise ValueError('The actual solver implementation is not bound to this return')
    implementation = module('_actual_dn_bound_source_gate', current/'warm_true_dn_solve.py')
    linear_path = Path(record['linear_source_run'])
    check_hash(linear_path, record['linear_source_run_sha256'], 'The accepted linear anchor')
    source = implementation.validate_warm_source(repository, linear_path)
    for key in ('frozen_profile', 'warm_definition', 'angular_chart', 'gauge_q',
                'warp_reference', 'mean_nodes', 'bc_normalization',
                'physical_tail_parameters', 'physical_tail_cut',
                'origin_design_run', 'origin_design_sha256',
                'frozen_source_signature', 'warm_provider_sha256'):
        if record[key] != source[key]:
            raise ValueError('Frozen warm geometry changed: '+key)
    for key in ('frozen_radial_chart', 'warm_geometry_base_sha256',
                'basis_anchor_v2_run', 'basis_anchor_v2_sha256'):
        if record.get(key) != source.get(key):
            raise ValueError('Frozen versioned geometry changed: '+key)
    if hasattr(implementation, 'model_bindings'):
        for key, expected in implementation.model_bindings(repository, source).items():
            if record.get(key) != expected:
                raise ValueError('An explicit actual finite-family provider binding changed: '+key)
    if (record['linear_source_model_kind'] != source['model_kind']
            or record['linear_source_acceptance_kind'] != source.get('acceptance_kind', 'actual_warm_bvp_return')
            or record['linear_source_solver_invoked'] != source.get('solver_invoked', True)
            or record['source_raw_sha256'] != source['raw_return']['sha256']
            or record['source_physical_sha256'] != source['physical_sha256']):
        raise ValueError('The accepted linear representation provenance changed')
    raw_path, physical_path = path.parent/raw['file'], path.parent/'physical.npz'
    check_hash(raw_path, raw['sha256'], 'The actual raw field')
    check_hash(physical_path, record['physical_sha256'], 'The actual physical quintic')
    with np.load(raw_path, allow_pickle=False) as values, np.load(physical_path, allow_pickle=False) as field:
        if (values['y'].shape != (3*modes+1, len(values['x']))
                or values['p'].shape != (modes,)
                or field['c'].shape != (6, len(field['x'])-1, 3*modes+1)
                or len(field['x']) != len(values['x'])
                or not np.array_equal(values['p'], field['p'])
                or not np.array_equal(values['p'], raw['parameters'])):
            raise ValueError('The actual raw/physical dimensions or parameters disagree')
        if (not all(np.all(np.isfinite(values[key])) for key in
                    ('x', 'y', 'p', 'rms', 'cubic_x', 'cubic_c', 'pscale'))
                or not all(np.all(np.isfinite(field[key])) for key in ('x', 'c', 'p'))
                or not np.all(np.diff(values['x']) > 0) or not np.all(np.diff(field['x']) > 0)
                or np.any(values['rms'] < 0) or float(np.max(values['rms'])) != raw['rms']
                or not np.array_equal(values['pscale'],
                    np.maximum(record['gauge_q']**np.arange(2, modes+1), 1e-9))):
            raise ValueError('The actual numerical field, RMS, mesh or phase scale is invalid')
        # This source-bound ShortBridge is the upper branch with sigma=-1.
        if (record['frozen_profile']['prefix_bridge']['kind'] != 'turn_plateau_v1'
                or SHORT_BRIDGE_SHA not in record['frozen_source_signature'].values()):
            raise ValueError('The actual upper-bridge height convention is not bound')
        height = -record['gauge_q']*values['y'][2*modes+1:, -1]
    metric_path, seam_path = path.parent/'relative-metric.json', path.parent/'frozen-mean-seam.json'
    check_hash(metric_path, record['relative_metric_sha256'], 'The full metric artifact')
    check_hash(seam_path, record['frozen_mean_seam_sha256'], 'The frozen-mean cut artifact')
    if load(metric_path)['rows'] != rows or load(seam_path) != record['tail_seam']:
        raise ValueError('The recorded metric or mean audit differs from its actual artifact')
    final, seam = record['result'], record['tail_seam']
    if (final.get('original_nonlinear_DN_accepted') is not True
            or final['raw_sha256'] != raw['sha256']
            or final['physical_sha256'] != record['physical_sha256']
            or final['actual_bc_max'] != record['actual_scaled_bc_max']
            or final['physical_bc_max'] != record['actual_physical_bc_max']
            or record.get('seam_reuses_same_accepted_full_H_packet') is not True
            or seam['mean_nodes'] != 1168 or seam.get('tail_converged') is not True):
        raise ValueError('The final field/BC/mean identity changed')
    checks = record.get('actual_outer_checks', [])
    if not 1 <= len(checks) <= 8:
        raise ValueError('No complete original actual outer boundary check')
    last = checks[-1]
    packet_path, target_path = Path(final['full_height_record']), Path(final['height_reference'])
    if (not same_path(packet_path, seam['tail_packet'])
            or not same_path(packet_path, last['packet'])
            or not same_path(target_path, last['height_reference'])
            or last['raw_sha256'] != raw['sha256']
            or last['physical_sha256'] != record['physical_sha256']
            or last['actual_bc'] != record['actual_scaled_bc_max']
            or last['physical_bc'] != record['actual_physical_bc_max']):
        raise ValueError('The last real outer return is not the declared final field')
    check_hash(packet_path, seam['tail_packet_sha256'], 'The final original full-H packet')
    check_hash(packet_path, last['packet_sha256'], 'The last actual outer packet')
    check_hash(target_path, last['height_reference_sha256'], 'The actual full-H target')
    stage = next((row for row in reversed(record['stages'])
                  if same_path(row['packet'], packet_path)), None)
    if (stage is None or stage.get('full_height') is not True or stage.get('factor') != 1.
            or stage.get('requested_jacobian') is not True or stage.get('converged') is not True
            or stage['packet_sha256'] != seam['tail_packet_sha256']
            or not same_path(stage['height_reference'], target_path)
            or stage['height_reference_sha256'] != last['height_reference_sha256']
            or stage['height_reference_key'] != 'candidate_H' or stage['height_arithmetic'] != 'numpy'):
        raise ValueError('The last tail stage is not an accepted original complete-H/J request')
    target = load(target_path)
    if (target['physical_sha256'] != record['physical_sha256']
            or target['raw_sha256'] != raw['sha256']
            or target['gauge_q'] != record['gauge_q'] or target['mean_nodes'] != 1168
            or target['modes'] != modes or target['candidate_H'] != record['candidate_H']
            or target['candidate_H'] != raw['candidate_H']
            or not np.array_equal(np.asarray(target['candidate_H']), height)
            or not same_path(target['linear_source_run'], linear_path)
            or target['linear_source_run_sha256'] != record['linear_source_run_sha256']
            or not same_path(target['actual_source_run'], parent_path)
            or target['actual_source_run_sha256'] != record['actual_source_run_sha256']):
        raise ValueError('The complete Dirichlet target is not the final saved prefix field')
    check_hash(target['raw'], raw['sha256'], 'The height target raw artifact')
    check_hash(target['physical'], record['physical_sha256'], 'The height target physical artifact')
    with gzip.open(packet_path, 'rt') as stream:
        packet = json.load(stream)
    request, response, cfg = packet['request'], packet['response'], packet['config']
    if (request.get('height') != target['candidate_H'] or request.get('jacobian') is not True
            or request.get('audit') is not True or response.get('converged') is not True
            or response.get('failed') or not isinstance(response.get('audit'), dict)
            or cfg.get('solveTolerance') != 2e-9
            or not finite_gate(response.get('residual'), 2e-9)
            or any(value != response['residual'] for value in
                   (final['tail_residual'], seam['tail_shooting_residual'], last['actual_tail'], stage['residual']))):
        raise ValueError('The final original nonlinear response failed or changed its actual residual')
    checkpoint, jets = response['checkpoint'], response['jets']
    parameters, states = checkpoint['parameters'], checkpoint['states']
    raw_nodes, raw_states = checkpoint['rawNode'], checkpoint['rawStates']
    physical_depth = parameters.get('physicalDepth', parameters['depth'])
    if (cfg['modes'] != modes or cfg['spacing'] != 3
            or parameters['modes'] != modes or parameters['spacing'] != 3
            or checkpoint['cutHeight'] != target['candidate_H']
            or len(states) != parameters['depth']+1
            or physical_depth != cfg['depth']
            or parameters['shootingParts'] != cfg.get('shootingParts', 1)
            or len(raw_nodes) != physical_depth+1 or raw_nodes[0] != 0
            or raw_nodes[-1] != parameters['depth']
            or any(not isinstance(node, int) for node in raw_nodes)
            or any(right <= left for left, right in zip(raw_nodes[:-1], raw_nodes[1:]))
            or len(raw_states) != len(raw_nodes)
            or any(row != states[node] for node, row in zip(raw_nodes, raw_states))
            or any(len(row) != 2*modes or not all(math.isfinite(value) for value in row) for row in states)):
        raise ValueError('The final original checkpoint is not the complete finite shooting state')
    for key in ('height', 'slope', 'second'):
        if np.asarray(jets[key]).shape != (modes,) or not np.all(np.isfinite(jets[key])):
            raise ValueError('Incomplete final original physical cut coefficients: '+key)
    jacobian = np.asarray(response['heightJetJacobian'])
    if jacobian.shape != ((3*modes+2)*modes,) or not np.all(np.isfinite(jacobian)):
        raise ValueError('The final original full height-jet Jacobian is incomplete')
    for key in ('radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep'):
        if jets[key] != record['physical_tail_cut'][key]:
            raise ValueError('The final original physical cut changed: '+key)
    for key in ('meanSlope', 'meanSecond', 'meanSlopeCorrection', 'meanSecondCorrection'):
        if not math.isfinite(jets[key]):
            raise ValueError('The original cut mean component is nonfinite: '+key)
    check_hash(record['tail_settings'], record['tail_settings_sha256'], 'The actual tail settings')
    if load(record['tail_settings']) != cfg:
        raise ValueError('The actual saved packet configuration changed')
    manifest_path = Path(record['native_manifest'])
    check_hash(manifest_path, record['native_manifest_sha256'], 'The original native manifest')
    manifest = load(manifest_path)
    for item in [*manifest['owned_sources'], *manifest['native_files'].values()]:
        check_hash(item['path'], item['sha256'], 'An original native source or binary')
    if set(packet['source_sha256']) != TAIL_SOURCES:
        raise ValueError('The original complete client/worker source identity is missing')
    for name, digest in packet['source_sha256'].items():
        check_hash(manifest_path.parent/'scripts'/name, digest, 'An original full-H packet source')
    ready_path = path.parent/'tail-ready.json'
    check_hash(ready_path, record['tail_ready_sha256'], 'The original worker ready packet')
    ready = load(ready_path)
    for key, expected in record['physical_tail_parameters'].items():
        if ready['parameters'].get(key) != expected or parameters.get(key) != expected:
            raise ValueError('A complete original factory physical parameter changed: '+key)
    return record
