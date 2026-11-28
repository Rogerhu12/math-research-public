#!/usr/bin/env python3
"""Read-only gate for an original-support fixed-g actual nonlinear-DN return.

The true predecessor chain terminates in an explicitly source-bound 7a
lambda-one chord return. Every fixed problem declaration, original residual,
complete raw/physical artifact, full shooting state and complete height
Jacobian is checked. Final physical-endpoint H and outer raw H have distinct
roles. This performs no model construction, BVP, tail or geometric proof.
"""
import gzip
import math
from pathlib import Path
import sys

import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import chord_fixed_support_actual_model as model
from chord_fixed_support_actual_model import sha,load,ref,checked,module

TAIL_SOURCES = {
    '950f-tail-client-v3.py','950f-tail-stage-port-v3.mjs','950f-tail-stage-core.mjs',
    '950f-tail-stage-split.mjs','950f-tail-subdivision.mjs','950f-tail-warm-remesh.mjs',
    'closing_weighted_tail.mjs','closing_recalibrated_tail.mjs',
}


def height_bytes(value,M):
    result = np.asarray(value,dtype='<f8')
    if result.shape != (M,) or not np.all(np.isfinite(result)):
        raise ValueError('An actual complete height vector is invalid')
    return result.tobytes()


def same_path(left,right):
    return Path(left).resolve() == Path(right).resolve()


def packet_gate(path,target,cfg,problem,M,native,*,full_jacobian=True):
    with gzip.open(path,'rt') as stream:
        packet = __import__('json').load(stream)
    request,response = packet['request'],packet['response']
    if (packet['config'] != cfg or request.get('audit') is not True
            or (full_jacobian and request.get('jacobian') is not True)
            or response.get('converged') is not True or response.get('failed')
            or not isinstance(response.get('audit'),dict)
            or not model.finite(response.get('residual'),2e-9)
            or height_bytes(request['height'],M) != height_bytes(target,M)):
        raise ValueError('A bound complete original tail request failed or changed')
    for key in ('fullD','normalizedFullDefect','minLeading','minD','formalCurvature',
                'maxPhysicalPV','actualMetric','holonomy'):
        value = response['audit'].get(key)
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):
            raise ValueError('An original complete audit scalar is missing/nonfinite: '+key)
    checkpoint,jets = response['checkpoint'],response['jets']
    parameters = checkpoint['parameters']
    if (height_bytes(checkpoint['cutHeight'],M) != height_bytes(target,M)
            or parameters['modes'] != M or parameters['spacing'] != 3
            or parameters.get('linearMethod') != 'stable-momentum-cusp-subdivision'):
        raise ValueError('The original full-state cut/basis/linear far construction changed')
    for key,default in (('quadrature',128),('steps',64),('linearFar',48),
                        ('linearSteps',512),('projectionFloor',.05)):
        if parameters.get(key) != cfg.get(key,default):
            raise ValueError('The actual original discretization changed: '+key)
    for key,wanted in problem['physical_tail_parameters'].items():
        if parameters.get(key) != wanted:
            raise ValueError('An actual complete checkpoint physical parameter changed: '+key)
    states = np.asarray(checkpoint['states'],float)
    raw_nodes = checkpoint['rawNode']
    physical_depth = parameters.get('physicalDepth',parameters['depth'])
    if (states.shape != (parameters['depth']+1,2*M) or not np.all(np.isfinite(states))
            or physical_depth != cfg['depth']
            or parameters['shootingParts'] != cfg.get('shootingParts',1)
            or len(raw_nodes) != physical_depth+1 or raw_nodes[0] != 0
            or raw_nodes[-1] != parameters['depth']
            or any(type(node) is not int for node in raw_nodes)
            or any(right <= left for left,right in zip(raw_nodes[:-1],raw_nodes[1:]))
            or not np.array_equal(np.asarray(checkpoint['rawStates'],float),states[raw_nodes])):
        raise ValueError('The original complete finite shooting state/raw-node relation changed')
    for key in ('height','slope','second'):
        height_bytes(jets[key],M)
    if full_jacobian:
        jac = np.asarray(response.get('heightJetJacobian'),float)
        if jac.shape != ((3*M+2)*M,) or not np.all(np.isfinite(jac)):
            raise ValueError('The original complete height/mean Jacobian is missing')
    for key in ('radius','backgroundSlope','backgroundSecond','E','Ep'):
        if jets[key] != problem['physical_tail_cut'][key]:
            raise ValueError('The actual physical cut jet changed: '+key)
    for key in ('meanSlope','meanSecond','meanSlopeCorrection','meanSecondCorrection'):
        if not isinstance(jets[key],(int,float)) or not math.isfinite(jets[key]):
            raise ValueError('A retained actual mean jet is nonfinite: '+key)
    if set(packet['source_sha256']) != TAIL_SOURCES:
        raise ValueError('The original complete worker/client source identity is missing')
    for name,digest in packet['source_sha256'].items():
        if sha(native/'scripts'/name) != digest:
            raise ValueError('An actual original packet source changed: '+name)
    return response


def accepted_actual_input(path,*,repo=None,seen=None):
    path = Path(path).resolve()
    record = load(path)
    if record.get('model_kind') != model.KIND:
        raise ValueError('Require this honest original-support fixed actual-DN model kind')
    repo = Path(repo if repo is not None else record['repository']).resolve()
    seen = {str(path)} if seen is None else set(seen)
    source_path = checked(record['actual_source'])
    if source_path == path:
        raise ValueError('A fixed actual refinement cannot cite itself as predecessor')
    problem = record['fixed_problem']
    parent_provisional = load(source_path)
    parent_is_fixed = parent_provisional.get('model_kind') == model.KIND
    parent = model.accepted_input(source_path,repo=repo,seen=seen,
        origin_repo=None if parent_is_fixed else problem['original_repository'],
        coupling_summary=None if parent_is_fixed else checked(problem['coupling_summary']))
    model.validate_refinement_definition(record,parent)
    if (record.get('status') != 'audited_finite_original_support_actual_dn_candidate'
            or record.get('error') or record.get('solver_invoked') is not True
            or record.get('solver_success') is not True
            or record.get('finite_actual_dn_candidate_pass') is not True
            or record.get('actual_tail_requested') is not True
            or record.get('original_actual_nonlinear_tail') is not True
            or record.get('acceptance_kind') != 'actual_original_support_fixed_dn_refinement_return'
            or record.get('fixed_metric_design_continuation') is not False
            or record.get('same_complete_metric_as_source') is not True
            or record.get('boundary_problem_changed') is not False
            or record.get('raw_and_final_physical_heights_have_separate_bindings') is not True
            or record.get('initializer_is_accepted_solution') is not False):
        raise ValueError('The complete original actual refinement has no genuine accepted return')
    for key,wanted in (('actual_source_role',parent['role']),('actual_source_raw',parent['raw']),
            ('actual_source_physical',parent['physical']),('actual_source_final_physical_packet',parent['final_packet']),
            ('actual_source_final_physical_height_binding',parent['final_height_binding'])):
        if record[key] != wanted:
            raise ValueError('The complete actual predecessor role changed: '+key)
    for key,problem_key in (('frozen_profile','frozen_profile'),('gauge_q','gauge_q'),
            ('warp_reference','warp_reference_q'),('mean_nodes','mean_nodes'),
            ('bc_normalization','bc_normalization'),('physical_tail_parameters','physical_tail_parameters'),
            ('physical_tail_cut','physical_tail_cut'),('angular_chart','angular_chart'),('core_settings','core_settings')):
        if record[key] != problem[problem_key]:
            raise ValueError('A frozen physical/chart/mean definition changed: '+key)
    if (problem['core_settings']['homotopy'] != 1 or problem['core_settings']['curvature_blend'] != 1
            or problem['parameter_zero_meaning'] != model.PARAMETER_ZERO
            or problem['physical_delta_is_solution_unknown'] is not False
            or problem['original_support_family_and_exact_lift_retained'] is not True
            or type(problem['mean_nodes']) is not int or problem['mean_nodes'] < 16):
        raise ValueError('The fixed lambda-one original support/mean semantics changed')
    anchor = load(checked(problem['actual_anchor']))
    for key in ('anchor_raw','anchor_physical','anchor_final_physical_height_binding',
                'anchor_final_physical_packet','anchor_port','original_anchor_gate'):
        checked(problem[key])
    for key in ('angular_chart','core_settings','gauge_q','physical_tail_parameters','physical_tail_cut'):
        if problem[key] != anchor[key]:
            raise ValueError('A frozen original actual anchor quantity changed: '+key)
    if (problem['frozen_profile'] != anchor['frozen_profile']
            or problem['warp_reference_q'] != anchor['warp_reference']
            or problem['mean_nodes'] != anchor['prefix_audit']['samples_psi']
            or problem['bc_normalization'] != anchor['gates']['physical_bc_tol']/anchor['gates']['bc_tol']
            or problem['q_seed'] != anchor['gauge_q']):
        raise ValueError('The full returned metric, finite mean or BC normalization left its actual anchor')
    source_repo = Path(record['repository']).resolve()
    local_scripts = source_repo/'topics/visible-flex-held-10pct/scripts/resume_20261128/analytic'
    required_files = ('chord_fixed_support_actual_step.py','chord_fixed_support_actual_model.py',
                      'chord_fixed_support_actual_acceptance.py','chord_fixed_support_actual_resources.py')
    for filename,digest in record['source_hashes'].items():
        if sha(filename) != digest:
            raise ValueError('An actual numerical source/input changed: '+filename)
    for name in required_files:
        file = local_scripts/name
        if record['source_hashes'].get(str(file)) != sha(file) or sha(file) != sha(HERE/name):
            raise ValueError('The independently frozen original-support actual implementation changed: '+name)
    if (not same_path(record['command'][1],local_scripts/'chord_fixed_support_actual_step.py')
            or '--prepare-only' in record['command']):
        raise ValueError('The actual solver argv is not this complete executed entry')
    interpreter_argv = record['actual_interpreter_argv']
    script = record['command'][1]
    if (interpreter_argv.count(script) != 1
            or interpreter_argv[interpreter_argv.index(script):] != record['command'][1:]
            or record['actual_design_source_relabelled_as_a_fixed_solver_return'] is not False
            or record['first_actual_anchor_unknowns_converted_to_fixed_metric'] is not
               (parent['role']=='accepted_original_support_chord_design_actual_return')):
        raise ValueError('The actual interpreter invocation or first-anchor parameter-role declaration changed')
    M = record['modes'];raw = record['raw_return'];gates = record['gates']
    if (type(M) is not int or not 1 <= M <= 64 or raw.get('success') is not True
            or raw.get('status') != 0 or not model.finite(raw.get('rms'),gates['tol'])
            or not model.finite(record.get('actual_scaled_bc_max'),gates['bc_tol'])
            or not model.finite(record.get('actual_physical_bc_max'),gates['physical_bc_tol'])):
        raise ValueError('An actual original full RMS/boundary gate failed')
    raw_path = path.parent/raw['file'];physical_path = path.parent/'physical.npz'
    if sha(raw_path) != raw['sha256'] or sha(physical_path) != record['physical_sha256']:
        raise ValueError('The actual complete raw/physical field changed')
    with np.load(raw_path,allow_pickle=False) as data,np.load(physical_path,allow_pickle=False) as physical:
        if (data['y'].shape != (3*M+1,len(data['x'])) or data['p'].shape != (M,)
                or data['cubic_c'].shape != (4,len(data['x'])-1,3*M+1)
                or data['rms'].shape != (len(data['x'])-1,)
                or not np.array_equal(data['cubic_x'],data['x'])
                or physical['x'].shape != data['x'].shape
                or physical['c'].shape != (6,len(data['x'])-1,3*M+1)
                or not np.array_equal(physical['p'],data['p'])
                or not np.array_equal(data['p'],raw['parameters'])
                or data['x'][0] != 0 or data['x'][-1] != 1
                or not np.all(np.diff(data['x'])>0) or not np.all(np.diff(physical['x'])>0)
                or not all(np.all(np.isfinite(data[key])) for key in ('x','y','p','cubic_x','cubic_c','rms','pscale'))
                or not all(np.all(np.isfinite(physical[key])) for key in ('x','c','p'))
                or not np.all(data['rms']>=0) or float(np.max(data['rms'])) != raw['rms']
                or raw['nodes'] != len(data['x'])
                or not np.array_equal(data['pscale'],record['parameter_scales'])
                or not np.array_equal(data['pscale'],np.maximum(record['gauge_q']**np.arange(2,M+1),1e-9))):
            raise ValueError('The actual complete raw/physical dimensions, scale, mesh or RMS changed')
        expected_q = problem['q_seed']*math.exp(float(data['p'][0]))
        expected_coefficients = np.r_[expected_q,data['p'][1:]*data['pscale']]
        if (not 1e-7 < expected_q < .2 or record['returned_actual_q'] != expected_q
                or not np.array_equal(expected_coefficients,record['returned_support_coefficients'])):
            raise ValueError('The fixed actual original support parameters changed meaning')
        raw_H = problem['bridge_sigma']*record['gauge_q']*data['y'][2*M+1:,-1]
        pp = PPoly.construct_fast(physical['c'].copy(),physical['x'].copy(),axis=1,extrapolate=False)
        physical_H = problem['bridge_sigma']*record['gauge_q']*pp(np.array([physical['x'][-1]]))[2*M+1:,0]
        if (height_bytes(raw_H,M) != height_bytes(raw['candidate_H'],M)
                or height_bytes(physical_H,M) != height_bytes(record['final_physical_H'],M)):
            raise ValueError('A raw or final physical endpoint height was replaced by the other role')
    checks = record['actual_outer_checks']
    if not 1 <= len(checks) <= 8 or [row['outer'] for row in checks] != list(range(len(checks))):
        raise ValueError('The original eight-outer history is missing or nonsequential')
    last = checks[-1]
    if (last['raw'] != ref(raw_path) or last['physical']['sha256'] != record['physical_sha256']
            or last['actual_bc'] != record['actual_scaled_bc_max']
            or last['physical_bc'] != record['actual_physical_bc_max']):
        raise ValueError('The final raw actual boundary check does not bind this complete field')
    checked(last['physical'])
    raw_binding = load(checked(last['height_reference']))
    if (raw_binding['height_reference_kind'] != 'actual_outer_raw_nodal_height'
            or height_bytes(raw_binding['candidate_H'],M) != height_bytes(raw_H,M)
            or raw_binding['raw'] != ref(raw_path) or raw_binding['physical'] != last['physical']):
        raise ValueError('The raw actual boundary packet has lost its actual nodal-height identity')
    metric_path,seam_path = path.parent/'relative-metric.json',path.parent/'frozen-mean-seam.json'
    if sha(metric_path) != record['relative_metric_sha256'] or sha(seam_path) != record['frozen_mean_seam_sha256']:
        raise ValueError('The saved complete metric or frozen-mean seam audit changed')
    rows,seam = record['metric_diagnostics'],record['tail_seam']
    if (load(metric_path)['rows'] != rows or load(seam_path) != seam
            or not rows or sorted(row['angular'] for row in rows) != record['actual_audit_angular']
            or any(row['angular'] < 16*(3*M+1) or not model.finite(row['legacy_max_component_fft_l1'],1e-6)
                   or not model.finite(row['sample_operator_max'],1e-6) for row in rows)
            or seam['mean_nodes'] != record['mean_nodes'] or seam['cut_chart_error'] != 0
            or seam['tail_converged'] is not True
            or not model.finite(seam['physical_endpoint_bc_max'],gates['physical_bc_tol'])):
        raise ValueError('The complete metric, physical endpoint or unchanged finite-mean gate failed')
    final = record['result']
    final_packet = Path(final['full_height_record']).resolve()
    target_path = Path(final['height_reference']).resolve()
    if (final.get('original_nonlinear_DN_accepted') is not True
            or final['raw'] != ref(raw_path) or final['physical'] != ref(physical_path)
            or final['actual_bc_max'] != record['actual_scaled_bc_max']
            or final['physical_bc_max'] != record['actual_physical_bc_max']
            or final['physical_endpoint_bc_max'] != seam['physical_endpoint_bc_max']
            or final['metric_max'] != max(row['legacy_max_component_fft_l1'] for row in rows)
            or final['full_height_record_sha256'] != sha(final_packet)
            or final['height_reference_sha256'] != sha(target_path)
            or seam['tail_packet'] != ref(final_packet) or seam['height_reference'] != ref(target_path)
            or final['final_height_reference_kind'] != 'actual_saved_physical_quintic_endpoint'):
        raise ValueError('The final physical-endpoint artifacts differ from their actual declaration')
    target = load(target_path)
    if (target['height_reference_kind'] != 'actual_saved_physical_quintic_endpoint'
            or height_bytes(target['candidate_H'],M) != height_bytes(physical_H,M)
            or height_bytes(target['raw_candidate_H'],M) != height_bytes(raw_H,M)
            or target['raw'] != ref(raw_path) or target['physical'] != ref(physical_path)
            or target['actual_source'] != record['actual_source']
            or target['mean_nodes'] != record['mean_nodes'] or target['fixed_problem'] != problem
            or target['parameter_zero_meaning'] != model.PARAMETER_ZERO):
        raise ValueError('The final complete physical height binding changed')
    bitwise_equal = height_bytes(raw_H,M) == height_bytes(physical_H,M)
    if (record['final_physical_H_bitwise_equal_raw_H'] is not bitwise_equal
            or record['final_physical_packet_reuses_identical_original_full_H'] is not bitwise_equal
            or (bitwise_equal and ref(final_packet) != last['packet'])):
        raise ValueError('The exact raw/physical height identity and packet reuse differ')
    cfg = load(record['tail_settings'])
    if (sha(record['tail_settings']) != record['tail_settings_sha256']
            or sha(record['base_tail_settings']) != record['base_tail_settings_sha256']
            or sha(record['linear_port_path']) != record['linear_port_sha256']
            or record['tail_resolution'] != {key:cfg[key] for key in ('modes','quadrature','steps','depth','shootingParts')}
            or record['actual_tail_RK_refined'] is not (cfg['steps']>load(checked(parent['tail_settings']))['steps'])):
        raise ValueError('The actual original numerical tail resolution changed')
    manifest_path = checked(record['native_manifest'])
    manifest = load(manifest_path)
    original = module('_fixed_acceptance_original_native_manifest',Path(problem['original_repository'])/
        'topics/visible-flex-held-10pct/scripts/resume_20261126/continue_original_actual_dn_chord.py')
    original.verify_references(manifest)
    if (manifest['fixed_scope'] != dict(M=M,spacing=3,quadrature=cfg['quadrature'],steps=cfg['steps'],
            projectionFloor=.05,orientation=1,cuspAwareFlow=True)
            or manifest['execution_provider']['workers'] != record['native_workers']
            or record['native_workers'] not in (2,4)):
        raise ValueError('The complete actual native execution scope changed')
    raw_response = packet_gate(checked(last['packet']),raw_H,cfg,problem,M,manifest_path.parent)
    final_response = raw_response if ref(final_packet) == last['packet'] else packet_gate(
        final_packet,physical_H,cfg,problem,M,manifest_path.parent)
    if (raw_response['residual'] != last['actual_tail']
            or final_response['residual'] != final['tail_residual']
            or final_response['residual'] != seam['tail_shooting_residual']):
        raise ValueError('A recorded actual complete tail residual changed')
    for packet,expected in ((last['packet'],raw_H),(ref(final_packet),physical_H)):
        stages = [row for row in record['stages'] if row['packet'] == packet]
        if not stages or not any(row['full_height'] is True and row['factor']==1.
            and row['requested_jacobian'] is True and row['converged'] is True for row in stages):
            raise ValueError('The original complete full-H/J/audit stage is missing')
    ready = load(checked(record['tail_ready']))
    if any(ready['parameters'].get(k) != v for k,v in problem['physical_tail_parameters'].items()):
        raise ValueError('The original actual worker ready parameters changed')
    resource = record['resource_execution']
    if (resource['rhs_block'] != 64 or resource['jacobian_block'] != 32
            or resource['matrix_format'] != 'complete_CSR'
            or resource['storage'] != 'complete_factor_only_mmap'
            or resource['gates_relaxed'] is not False
            or resource['original_complete_QR_arithmetic_unchanged'] is not True
            or resource['mapped_logical_bytes_are_not_RSS_credit'] is not True):
        raise ValueError('The declared complete original linear solve/resource contract changed')
    for filename,digest in resource['source_hashes'].items():
        if sha(filename) != digest:
            raise ValueError('A bound full-matrix resource component changed')
    return record
