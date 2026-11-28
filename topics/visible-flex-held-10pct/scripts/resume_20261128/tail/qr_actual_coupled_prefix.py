#!/usr/bin/env python3
"""Load a genuine complete-prefix-QR lambda-one native4/chord3/outer8 return.

The coupled source retains its actual-tail flags, command, original finite
gates and all execution sidecars. Its final physical-endpoint tail height is
bound separately from the raw collocation candidate. The exact-core lift,
source angular count/GL6 mean construction and shared-Hermite map definition
are the unchanged ActualR53CartesianPrefix construction. No BVP/tail solve or
continuous geometric certificate is produced by this read-only adapter.
"""
import gzip
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
TAIL = HERE.parent/'tail'
sys.path.insert(0, str(TAIL))
from actual_cartesian_prefix import ActualR53CartesianPrefix, SCRIPTS, module, sha
CHORD_ENTRY = HERE/'continue_original_actual_dn_qr.py'
CHORD_SHA = 'd716cbf3d6c82c1bbe83675218efc7016a6f42c3ec67adb63e03187cefa5fafa'
REVIEWED_READER = HERE.parent/'analytic/chord_actual_coupled_prefix.py'
REVIEWED_READER_SHA256 = '5c1e816af142b8d2f5cc8cba43d840c5bc352a032a9be212e9581f753efd625a'
import prefix_actual_dn_qr_driver as qr_execution
from verified_tail_response_memo import PACKET_SOURCE_NAMES, checked, ref


def load(path):
    return json.loads(Path(path).read_text())


def finite_nonnegative(value, limit):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and 0 <= value <= limit)


def accepted_coupled(source_run, coupling_summary):
    """Check one complete actual outer return and its literal endpoint packet."""
    source_run, coupling_summary = map(lambda p: Path(p).resolve(),
                                      (source_run, coupling_summary))
    summary, record = load(coupling_summary), load(source_run)
    if (sha(REVIEWED_READER) != REVIEWED_READER_SHA256
            or summary.get('schema') != 'original-lambda-one-native4-chord3-outer8-prefix-qr-v1'
            or summary.get('execution_backend') != 'complete_original_prefix_CSR_QR_V5_checkpoints'
            or summary.get('native_full_J_replaced_by_prefix_QR') is not False
            or summary.get('original_record_relabelled') is not False):
        raise ValueError('Require the separately bound actual complete-prefix-QR source contract')
    if (summary.get('status') != 'original_finite_true_dn_gates_passed'
            or summary.get('result', {}).get('accepted') is not True
            or summary['result'].get('original_actual_gate_passed') is not True
            or summary['result'].get('actual_process_returned') is not True
            or summary['result'].get('process_returncode') != 0
            or summary['result'].get('run_sha256') != sha(source_run)
            or Path(summary['result'].get('run', '')).resolve() != source_run
            or summary.get('actual_tail_requested') is not True
            or summary.get('fixed_metric_refinement') is not False
            or summary.get('original_outer_budget') != 8
            or summary.get('native_workers') != 4):
        raise ValueError('Require a genuine complete lambda-one complete-prefix-QR outer return')
    if (sha(CHORD_ENTRY) != CHORD_SHA
            or summary.get('source_hashes', {}).get(str(CHORD_ENTRY)) != CHORD_SHA):
        raise ValueError('Unknown or changed QR coordination source requires explicit review')
    for group in (summary.get('source_hashes'), record.get('source_hashes'), record.get('inputs')):
        if not isinstance(group, dict) or not group:
            raise ValueError('A complete actual chord source/input binding is required')
        for filename, expected in group.items():
            if sha(filename) != expected:
                raise ValueError('Changed actual chord source/input: '+filename)
    original = module('_reviewed_actual_chord_coordination_reader', CHORD_ENTRY)
    execution_ref = summary['result']['prefix_execution']
    execution = load(checked(execution_ref))
    if (execution.get('original_portable_argv') != record['command']
            or execution.get('original_portable_argv') != summary['original_portable_command']
            or execution.get('actual_argv') != summary['actual_command']
            or execution.get('original_portable_command_fabricated') is not False
            or execution.get('execution_backend') != 'complete_original_prefix_CSR_QR_V5_checkpoints'
            or execution.get('original_streamed_SuperLU_execution_claimed') is not False):
        raise ValueError('The actual complete-prefix-QR execution does not bind the literal portable command')
    portable = (SCRIPTS/'resume_m3/portable_prefix_continue.py').resolve()
    if execution.get('wrapper_invoked') is True:
        wrapper = (HERE/'prefix_actual_dn_qr_driver.py').resolve()
        block = execution.get('streamed_rhs_block')
        if type(block) is not int or block < 1:
            raise ValueError('The actual original radial block is invalid')
        expected = [record['command'][0], str(wrapper), '--rhs-block', str(block),
                    *record['command'][2:]]
        if (execution['actual_argv'] != expected
                or execution.get('wrapper') != str(wrapper)
                or execution.get('wrapper_sha256') != sha(wrapper)):
            raise ValueError('The actual original streamed wrapper identity differs')
        provenance = execution['provenance']
        qr_execution.check_execution(provenance['path'], expected, wrapper, portable,
                                           block, provenance['sha256'])
    else:
        raise ValueError('This independent source contract requires the complete prefix QR wrapper')
    native_ref = summary['native']['manifest']
    native = load(checked(native_ref))
    original.verify_references(native)
    if (native['execution_provider']['workers'] != 4
            or native['fixed_scope'] != summary['native']['fixed_scope']
            or native['native_files']['executable'] != summary['native']['executable']):
        raise ValueError('The true native4 manifest differs from the original execution')
    baseline_ref = summary['tail_configuration']['baseline']
    runtime_ref = summary['tail_configuration']['runtime']
    baseline, runtime = load(checked(baseline_ref)), load(checked(runtime_ref))
    if ({key:value for key,value in runtime.items() if key not in original.RUNTIME_KEYS} != baseline
            or runtime.get('chordMaxCorrections') != 3):
        raise ValueError('The actual runtime changed its original baseline beyond declared execution keys')
    sys.path.insert(0, str(SCRIPTS/'resume_20261126'))
    sys.path.insert(0, str(SCRIPTS/'resume_m3'))
    from material_design_continue import original_finite_checks, complete_initializer
    from continue_material_true_tail import actual_gate
    checks = original_finite_checks(record)
    if (record.get('model_kind') is not None or record.get('fixed_metric')
            or record.get('fixed_metric_refinement')
            or record.get('actual_tail_requested') is not True
            or not actual_gate(record) or not checks['solver_and_boundary_pass']
            or not complete_initializer(source_run, record)
            or not finite_nonnegative(record['prefix_audit'].get('metric_l1'), 1e-6)
            or not finite_nonnegative(record['actual_outer_checks'][-1].get('actual_bc'),
                                      record['gates']['bc_tol'])
            or not finite_nonnegative(record['tail_seam'].get('tail_shooting_residual'), 2e-9)):
        raise ValueError('The actual chord source did not pass every original finite gate')
    if (not 1 <= len(record['actual_outer_checks']) <= 8
            or summary['result']['original_finite_checks'] != checks
            or summary['result']['raw'] != ref(source_run.parent/record['raw_return']['file'])
            or summary['result']['physical'] != ref(source_run.parent/'physical.npz')):
        raise ValueError('The actual original finite return/artifact identity differs')
    argv = record['command']
    def option(flag):
        if argv.count(flag) != 1:
            raise ValueError('Require exactly one actual command option '+flag)
        return argv[argv.index(flag)+1]
    portable = (SCRIPTS/'resume_m3/portable_prefix_continue.py').resolve()
    provider = (SCRIPTS/'resume_m3/material_support_factory.py').resolve()
    if (Path(argv[1]).resolve() != portable
            or record['source_hashes'].get(str(portable)) != sha(portable)
            or Path(option('--core-module')).resolve() != provider
            or record['inputs'].get(str(provider)) != sha(provider)
            or any(flag in argv for flag in ('--skip-audit', '--probe-only'))):
        raise ValueError('The actual coupled source is not the declared original R53 portable provider')
    settings = load(option('--core-config'))
    lam = settings.get('homotopy')
    if (settings != record['core_settings'] or not isinstance(lam, (int, float))
            or isinstance(lam, bool) or not math.isfinite(lam) or lam != 1
            or settings.get('curvature_blend') != 1):
        raise ValueError('A true lambda-one original R53 core with curvature_blend=1 is required')
    M = int(record['modes']); N = record['prefix_audit']['samples_psi']
    if (M < 1 or type(N) is not int or N < 16*(3*M+1)
            or int(option('--modes')) != M):
        raise ValueError('Complete actual Fourier state and source mean quadrature are required')
    tail_config = load(option('--tail-config'))
    if (tail_config != runtime or tail_config['modes'] != M or not 1 <= M <= 64
            or native['fixed_scope']['M'] != M
            or native['fixed_scope']['spacing'] != tail_config['spacing']
            or native['fixed_scope']['quadrature'] != tail_config['quadrature']
            or native['fixed_scope']['steps'] != tail_config['steps']
            or N != max(int(option('--audit-angular')),16*(3*M+1))
            or N != summary['input']['source_mean_nodes']):
        raise ValueError('The actual full mode/native scope or literal finite mean differs')
    port = load(option('--port'))
    if (sha(option('--port')) != summary['input']['port']['sha256']
            or port['source']['config_sha256'] != baseline_ref['sha256']
            or port['parameters'] != record['physical_tail_parameters']
            or port['modes'] != [3*j for j in range(1,M+1)]):
        raise ValueError('The complete actual original port/baseline identity differs')
    design_ref = summary['input']['source_run']
    design_path = Path(design_ref['path']).resolve()
    if sha(design_path) != design_ref['sha256']:
        raise ValueError('The actual lambda-one design input changed')
    from material_design_secant_predictor import accepted_original
    design, design_arrays = accepted_original(design_path, SCRIPTS.parents[2])
    del design_arrays
    for key in ('physical_profile','physical_tail_parameters','physical_tail_cut','angular_chart',
                'gauge_q','warp_reference','modes','angular','core_settings','parameter_scales','gates'):
        if design.get(key) != record.get(key):
            raise ValueError('The source-to-actual declaration changed: '+key)
    if summary['input']['source_family'] != 'original-R53-material-support':
        raise ValueError('This gate does not relabel a phase-family return as original R53')
    raw_path = source_run.parent/record['raw_return']['file']
    with np.load(raw_path, allow_pickle=False) as raw:
        x, y, p, scale = (raw[k].copy() for k in ('x', 'y', 'p', 'pscale'))
        if (x.ndim != 1 or len(x) < 2 or y.shape != (3*M+1, len(x))
                or p.shape != (M,) or scale.shape != (M-1,)
                or raw['cubic_c'].shape != (4, len(x)-1, 3*M+1)
                or raw['rms'].shape != (len(x)-1,)
                or not np.array_equal(raw['cubic_x'], x)
                or not all(np.all(np.isfinite(raw[k])) for k in
                           ('x', 'y', 'p', 'pscale', 'cubic_x', 'cubic_c', 'rms'))
                or not np.all(np.diff(x) > 0) or x[0] != 0. or x[-1] != 1.
                or not np.all(scale > 0)
                or not np.array_equal(scale, record['parameter_scales'])
                or not np.array_equal(p, record['raw_return']['parameters'])
                or record['raw_return']['nodes'] != len(x)
                or float(np.max(raw['rms'])) != record['raw_return']['rms']
                or float(np.min(raw['rms'])) < 0):
            raise ValueError('The actual complete raw PPoly/state/scales disagree')
    with np.load(source_run.parent/'physical.npz', allow_pickle=False) as data:
        if (data['x'].shape != x.shape or data['c'].shape != (6, len(x)-1, 3*M+1)
                or not np.array_equal(data['p'], p)
                or not all(np.all(np.isfinite(data[k])) for k in ('x', 'c', 'p'))
                or not np.all(np.diff(data['x']) > 0)):
            raise ValueError('The actual saved physical C2 field is incomplete')
        physical = SimpleNamespace(x=data['x'].copy(), p=data['p'].copy(),
            sol=PPoly.construct_fast(data['c'].copy(), data['x'].copy(),
                                     extrapolate=False, axis=1))
    binding_path = checked(summary['result']['full_height_binding'])
    binding = load(binding_path)
    if (binding['original_run'] != ref(source_run)
            or binding['physical'] != ref(source_run.parent/'physical.npz')
            or binding['packet'] != summary['result']['full_height_packet']
            or binding['raw_candidate_H'] != record['raw_return']['candidate_H']
            or binding['source_mean_nodes'] != N
            or binding['original_seam_mean_nodes'] != record['tail_seam']['angular_samples']):
        raise ValueError('The final physical-endpoint height binding differs from the actual run')
    packet_path = checked(binding['packet'])
    if packet_path != source_run.parent/record['tail_seam']['tail_record']:
        raise ValueError('The complete physical-endpoint packet is not the actual final seam record')
    if (binding['native_manifest'] != native_ref
            or binding['baseline_tail_config'] != baseline_ref
            or binding['runtime_tail_config'] != runtime_ref
            or binding['source_design_run'] != design_ref
            or binding['source_family'] != 'original-R53-material-support'
            or binding['height_reference_kind'] != 'original_seam_audit_physical_endpoint'):
        raise ValueError('The actual physical-endpoint binding lost its native/config/source identity')
    with gzip.open(packet_path, 'rt') as stream:
        packet = json.load(stream)
    request, response = packet['request'], packet['response']
    H = np.asarray(request['height'], dtype='<f8')
    boundH = np.asarray(binding['candidate_H'], dtype='<f8')
    cp = response['checkpoint']; states = np.asarray(cp['states'], float)
    J = np.asarray(response.get('heightJetJacobian'), float)
    if (H.shape != (M,) or not np.all(np.isfinite(H)) or H.tobytes() != boundH.tobytes()
            or request['jacobian'] is not True or request['audit'] is not True
            or response.get('converged') is not True or response.get('failed')
            or not finite_nonnegative(response.get('residual'), tail_config['solveTolerance'])
            or not isinstance(response.get('audit'), dict)
            or cp['parameters']['modes'] != M or cp['parameters']['spacing'] != tail_config['spacing']
            or cp['cutHeight'] != request['height']
            or states.shape != (cp['parameters']['depth']+1, 2*M)
            or not np.all(np.isfinite(states)) or J.shape != ((3*M+2)*M,)
            or not np.all(np.isfinite(J))):
        raise ValueError('The bound endpoint lacks an accepted complete physical height/state/J/audit')
    if packet['config'] != runtime:
        raise ValueError('The final actual tail packet uses another complete runtime configuration')
    if set(packet['source_sha256']) != PACKET_SOURCE_NAMES:
        raise ValueError('The final packet omits original worker/client sources')
    source = Path(option('--source-topic'))
    for name, expected in packet['source_sha256'].items():
        if sha(source/'scripts'/name) != expected:
            raise ValueError('The actual final worker/client source changed: '+name)
    provenance = dict(adapter=ref(__file__), source_kind='actual_lambda_one_qr_chord_final_physical_height',
        coupling_summary=ref(coupling_summary), original_chord_entry=ref(CHORD_ENTRY),
        prefix_execution=execution_ref, native_manifest=native_ref,
        original_summary_not_relabelled_as_memo=True,
        old_7a_or_streamed_execution_claimed=False,
        original_7a_coordination=summary['original_coordination_source'],
        reviewed_original_reader=ref(REVIEWED_READER),
        actual_complete_QR_execution=execution['provenance'],
        source_run=ref(source_run), endpoint_binding=ref(binding_path), packet=ref(packet_path),
        final_physical_height_is_definition=True,
        raw_height_bitwise_equal=(H.tobytes()==np.asarray(binding['raw_candidate_H'],dtype='<f8').tobytes()),
        original_actual_tail_flags_unchanged=True, original_finite_checks=checks,
        source_mean_nodes=N, source_mean_gauss_order=6,
        continuous_Cartesian_seam_certified=False, complete_surface=False)
    return record, physical, binding, provenance


def load_coupled_prefix(source_run, coupling_summary, *, side_modes=None, center_width=.04):
    record, physical, binding, provenance = accepted_coupled(source_run, coupling_summary)
    loader = module('_actual_coupled_c2_model', SCRIPTS/'resume_m3/actual_m3_metric_model.py')
    obj = loader.load_model({'source_run': str(Path(source_run).resolve())})
    obj.initial(physical.p)
    flow = obj.flow(physical.p[0])
    prefix = ActualR53CartesianPrefix(obj, flow, physical,
        record['prefix_audit']['samples_psi'], side_modes, center_width)
    prefix.actual_coupling_provenance = provenance
    return record, prefix, binding
