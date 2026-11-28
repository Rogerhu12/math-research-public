#!/usr/bin/env python3
"""Load a genuinely accepted coupled prefix into the existing Cartesian map.

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

from actual_cartesian_prefix import ActualR53CartesianPrefix, SCRIPTS, module, sha
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
    if (summary.get('status') != 'original_finite_true_dn_gates_passed'
            or summary.get('result', {}).get('accepted') is not True
            or summary['result'].get('original_finite_gate_before_binding') is not True
            or summary.get('execution', {}).get('original_execution_binding_checked') is not True
            or summary['result'].get('run_sha256') != sha(source_run)
            or summary.get('actual_tail_requested') is not True
            or summary.get('fixed_metric_refinement') is not False):
        raise ValueError('Only a genuinely accepted, execution-bound actual coupled return is allowed')
    expected_entry = Path(__file__).with_name('couple_actual_prefix_memoized.py')
    if summary.get('source_hashes', {}).get(str(expected_entry)) != sha(expected_entry):
        raise ValueError('Unknown or changed actual coupling entry requires explicit review')
    for group in (summary.get('source_hashes'), record.get('source_hashes'), record.get('inputs')):
        if not isinstance(group, dict) or not group:
            raise ValueError('A complete actual coupled source/input binding is required')
        for filename, expected in group.items():
            if sha(filename) != expected:
                raise ValueError('Changed actual coupled source/input: '+filename)
    for name in ('radial_provenance', 'fourier_cache_provenance',
                 'memo_provenance', 'memo_wrapper_provenance'):
        checked(summary['execution'][name])
    checked(summary['memoization_preflight'])
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
        raise ValueError('The actual coupled source did not pass every original finite gate')
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
            or isinstance(lam, bool) or not math.isfinite(lam) or not 0 < lam <= 1):
        raise ValueError('A positive original material homotopy is required')
    M = int(record['modes']); N = record['prefix_audit']['samples_psi']
    if (M < 1 or type(N) is not int or N < 16*(3*M+1)
            or int(option('--modes')) != M):
        raise ValueError('Complete actual Fourier state and source mean quadrature are required')
    tail_config = load(option('--tail-config'))
    if tail_config['modes'] != M:
        raise ValueError('The complete prefix and actual tail mode dimensions differ')
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
    if (binding['source_run'] != ref(source_run)
            or binding['physical'] != ref(source_run.parent/'physical.npz')
            or binding['packet'] != summary['result']['full_height_packet']
            or binding['raw_candidate_H'] != record['raw_return']['candidate_H']
            or binding['source_mean_nodes'] != N
            or binding['original_seam_mean_nodes'] != record['tail_seam']['angular_samples']):
        raise ValueError('The final physical-endpoint height binding differs from the actual run')
    packet_path = checked(binding['packet'])
    if packet_path != source_run.parent/record['tail_seam']['tail_record']:
        raise ValueError('The complete physical-endpoint packet is not the actual final seam record')
    checked(binding['native_manifest'])
    checked(binding['response_memoization_provenance'])
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
    if set(packet['source_sha256']) != PACKET_SOURCE_NAMES:
        raise ValueError('The final packet omits original worker/client sources')
    source = Path(option('--source-topic'))
    for name, expected in packet['source_sha256'].items():
        if sha(source/'scripts'/name) != expected:
            raise ValueError('The actual final worker/client source changed: '+name)
    provenance = dict(adapter=ref(__file__), coupling_summary=ref(coupling_summary),
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
