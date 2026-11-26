#!/usr/bin/env python3
"""Complete fixed-common-normal-plane six-control SO3 optimization.

All original core/rotation/H variables, the actual fixed g, every positive
Gram row and the old complete 192-plus-amplitude physical constraints remain.
Every angle and candidate uses the SAME exact normal-stage partition.
Every preceding frame and zero-control target edge stays in the complete
6m/9m angular-jet J/J*. No stationary KKT root is selected, and an isolated
successful numerical endpoint root is not a continuous-branch certificate.
The complete actual scalar/geometry/memory/restoration loop is retained.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import mmap
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.sparse.linalg import LinearOperator


SCHEMA = 'complete-independent-fixed-deep-fixed-normal-plane-SO3-QP-v1'
SOURCE_PINS = {'reference': ('scripts/resume_20261126/so3_axisymmetric_reference.py',
               '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),
 'warm_producer': ('notes/2026-11-17-parallel-model-fullclosed-hold-warm.py',
                   'bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3'),
 'observed': ('scripts/resume_20261120/gauss_observed_closed_gram.py',
              '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d'),
 'deep_scalar': ('scripts/resume_20261126/deep_valley_tail_input.py',
                 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'),
 'scalar': ('notes/2026-11-17-parallel-model-full-hold-oracle.py',
            'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'),
 'integer': ('notes/2026-11-17-parallel-inward-integral-enclosure.py',
             'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'),
 'hold': ('scripts/parallel_20261117_negative_hold_profile_ivp.py',
          'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'),
 'meridian': ('scripts/resume_20261126/so3_axisymmetric_meridian_operator.py',
              '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'),
 'geometry': ('scripts/resume_20261126/so3_zero_normal_lift_geometry.py',
              '255760e188d13f22ffef86c029f35f5d1629384411d2e32f03f75df60f4ab71c'),
 'qp': ('scripts/resume_20261120/fullspace_feasible_active_cg_v3.py',
        'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'),
 'spectral': ('scripts/resume_20261120/positive_spectral_gram_weights.py',
              'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'),
 'hessian': ('scripts/resume_20261120/positive_spectral_gram_hessian.py',
             '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4'),
 'centered': ('scripts/resume_20261126/centered_spectral_statistics.py',
              '5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'),
 'history': ('scripts/resume_20261120/launch_refinement_from_full_report.py',
             '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'),
 'pure_geometry': ('scripts/resume_20261120_curvature_qp.py',
                   'a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854'),
 'geometry_selector': ('scripts/resume_20261120/fullclosed_point_inequalities_v2.py',
                       'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'),
 'endpoint': ('scripts/resume_20261126/so3_zero_normal_lift_operator.py',
              '42ea8ec5920e3815b99c83c41448efb38ee37860f4d9362ddea6bce2418d39fe'),
 'axisymmetric_seed_driver': ('scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py',
                              '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'),
 'frozen_moment_input': ('scripts/resume_20261126/frozen_zero_moment_input.py',
                         '4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611'),
 'moment_trace_source': ('scripts/resume_20261126/trace_zero_initial_endpoint_failure.py',
                         '73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54'),
 'moment_initial_binding': ('scripts/resume_20261126/diagnose_zero_initial_chord.py',
                            '65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0'),
 'moment_original_endpoint': ('scripts/resume_20261126/so3_zero_closure_endpoint_operator.py',
                              '5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46'),
 'moment_original_driver': ('scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py',
                            'b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b'),
 'new_moment_input': ('scripts/resume_20261126/new_reference_literal_zero_moment_input.py',
                      'ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39')}

ROOT_SNAPSHOT_SCHEMA = 'actual-fixed-normal-plane-current-point-snapshot-v1'
ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256',
 'endpoint_root_policy',
 'normal_stage_count',
 'exact_normal_step_nodes',
 'actual_normal_step_carriers_binary64_hex',
 'common_partition_for_all_angles_and_free_points',
 'per_angle_adaptive_normal_partition',
 'current_cached_angle_roots',
 'current_all_grid_angle_roots_available',
 'current_all_grid_second_angular_jets_available',
 'current_maximum_endpoint_residual',
 'current_maximum_dimensionless_control_norm',
 'current_maximum_physical_z_norm',
 'current_maximum_gamma_axis_norm',
 'current_maximum_first_angular_endpoint_residual',
 'current_maximum_second_angular_endpoint_residual',
 'endpoint_counts',
 'actual_normal_counts',
 'last_root_failure',
 'normal_lift_last_summary',
 'numerical_Newton_iterations_differentiated',
 'complete_uniform_IFT_conditions_verified',
 'complete_continuous_root_branch_certified',
 'endpoint_root_error_enclosed',
 'stationary_KKT_selection_used',
 'continuous_horizontal_ODE_solution_claimed',
 'final_implicit_J_uses_all_normal_stage_equations',
 'previous_normal_frame_full_parameter_chain_retained',
 'original_zero_control_target_full_parameter_chain_retained',
 'implicit_control_dimension',
 'normal_increment_dimension',
 'implicit_dimension_per_stage',
 'complete_first_angular_implicit_dimension',
 'complete_second_angular_implicit_dimension')

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def file_record(path, repo=None):
    path = Path(path).resolve()
    result = dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
    if repo is not None:
        try:
            result['repo_relative_path'] = str(path.relative_to(repo))
        except ValueError:
            pass
    return result


def load(name, path, expected=None):
    if expected is not None and sha(path) != expected:
        raise ValueError('Changed complete source '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def event(**values):
    print(json.dumps(values, separators=(',', ':'), allow_nan=False), flush=True)


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def actual_reference(args, paths):
    report = json.loads(args.preparation_report.read_text())
    if (report.get('schema') != 'R690-independent-axisymmetric-SO3-preparation-v1'
            or report.get('source_sha256') != SOURCE_PINS['reference'][1]
            or report.get('complete') is not True):
        raise ValueError('Bind the actual independent full-scalar input preparation')
    for role,path in dict(reference_bundle=args.reference_bundle,carrier=args.carrier,
            node_report=args.node_report,scalar_input=args.scalar_input).items():
        if report['input_for_solver'][role]['sha256'] != sha(path):
            raise ValueError('Changed actual complete independent input: '+role)
    for role,digest in report['source_sha256_by_role'].items():
        if role not in SOURCE_PINS or SOURCE_PINS[role][1] != digest:
            raise ValueError('Changed actual independent preparation source: '+role)
    model = report['reference_definition']
    profile = report['fixed_scalar_metric_identity_sha256']
    if (canonical(model) != report['reference_model_identity_sha256']
            or canonical(model['fixed_scalar_profile_definition']) != profile
            or model['fixed_scalar_metric_identity_sha256'] != profile
            or report['N'] != args.angles or report['J'] != 923 or report['M'] != 160 or report['P'] != 7377
            or report.get('historical_nonlinear_directions_replayed') is not False
            or report.get('optimized_old_q_field_read_as_T0') is not False):
        raise ValueError('Retain the actual independent mathematical reference and full positive observation domain')
    supplied = {sha(path) for path in args.manifest}
    if report['new_locations']['sha256'] not in supplied:
        raise ValueError('The complete prepared historical union must be one explicit solver manifest')
    return report,dict(preparation_report=file_record(args.preparation_report),
        actual_source=file_record(paths['reference'],args.repo),
        reference_model_identity_sha256=report['reference_model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=profile,original_scalar_parameters_identity_sha256=
            report['original_scalar_parameters_identity_sha256'],
        actual_input_records=report['input_for_solver'],new_locations=report['new_locations'],
        complete_supplied_location_provenance=report['complete_supplied_location_provenance'],
        all_supplied_history_retained=True,old_optimized_parent_required=False)

def all_locations(args, preparation, q, history, restart=None, source_report_path=None):
    def indexed_grid(value):
        if isinstance(value, dict):
            if 'stage' in value and 'angle' in value and 'phi' not in value:
                return True
            return any(indexed_grid(item) for item in value.values())
        if isinstance(value, list):
            if value and isinstance(value[0], str) and value[0] in ('grid', 'grid_radius'):
                return True
            return any(indexed_grid(item) for item in value)
        return False

    if int(preparation['N']) != q.full_N or (restart is not None and int(restart['N']) != q.full_N):
        raise ValueError('Never reinterpret a tagged parent grid index under another full angle count')
    points = history.Locations(q.J, q.P, q.full_N)
    sources = [file_record(args.preparation_report)]
    if restart is not None:
        points.walk(restart, path=('complete_actual_SO3_restart_report',))
        if source_report_path is None:
            raise ValueError('The actual complete address-parent report path is required')
        sources.append(file_record(source_report_path))
    carrier_sha = sha(args.carrier)
    for path in args.manifest:
        payload = json.loads(path.read_text())
        declared = payload.get('carrier_sha256', payload.get('observation_carrier_sha256'))
        if declared != carrier_sha:
            raise ValueError('Every supplied historical location source must bind the actual same carrier')
        if payload.get('schema') == 'deep-valley-same-symbolic-location-transfer-v1':
            payload = {key: payload[key] for key in
                ('curvature_points', 'radius_points', 'protected_curvature_points')}
        if indexed_grid(payload):
            recorded_N = payload.get('N', payload.get('full_angles', payload.get('full_N')))
            if recorded_N is None or int(recorded_N) != q.full_N:
                raise ValueError('An indexed historical grid must explicitly bind this same full angular count; pure literal phi addresses need no reinterpretation')
        points.walk(payload, path=('explicit_complete_history', path.name))
        sources.append(file_record(path))
    before = points.summary()
    resolved = points.resolve_grid(args.carrier)
    arrays = points.arrays()
    protected = {tuple(value) for value in arrays['protected_curvature_points']}
    witnesses = [dict(cell=int(c), u=float(u), phi=float(phi),
        protected=(c, u, phi) in protected) for c, u, phi in arrays['curvature_points']]
    radii = [dict(cell=int(c), u=float(u), phi=float(phi)) for c, u, phi in arrays['radius_points']]
    if not witnesses or not radii:
        raise ValueError('Retain every complete inherited curvature and radius address set')
    return witnesses, radii, dict(sources=sources, before=before,
        resolved_grid_positions=resolved, after=points.summary(),
        legacy_angle_reinterpretation='literal old normal-angle value used as new frozen-chart phi0; not same physical point',
        new_locations_use='fixed initial-reference material chart phi0, never the moving internal phi_c',
        exact_binary_identity=True, old_values_or_certificates_inherited=False)


def add_location(value, values, q):
    if value is None:
        return False
    if 'cell' in value:
        cell, u, phi = int(value['cell']), float(value['u']), float(value['phi'])
    elif 'stage' in value:
        stage = int(value['stage'])
        cell, u = int(q.observation_cells[stage]), float(q.observation_u[stage])
        phi = float(value['phi']) if 'phi' in value else float(q.phi[int(value['angle'])])
    else:
        raise ValueError('Every remembered point must have an actual physical address')
    if not (0 <= cell < q.J-1 and 0 <= u <= 1 and math.isfinite(phi)):
        raise ValueError('Invalid actual same-mesh permanent address')
    key = (cell, u.hex(), phi.hex())
    for old in values:
        if (int(old['cell']), float(old['u']).hex(), float(old['phi']).hex()) == key:
            if value.get('protected', False):
                old['protected'] = True
            return False
    values.append(dict(cell=cell, u=u, phi=phi, protected=bool(value.get('protected', False))))
    return True


class CommonSlackRows:
    """Every original row plus one scalar slack, without copying a multi-GB C.

    Original row C_i z <= -g_i/n_i becomes
    C_i z - delta_tau/n_i <= -g_i/n_i + tau0/n_i.
    Positive row renormalization is applied to BOTH sides; the extra row
    imposes tau0+delta_tau>=0. The physical g_i semantics are unchanged.
    """
    def __init__(self, matrix, bounds, metadata):
        self.matrix = matrix
        self.m, self.n = matrix.shape
        if len(metadata['rows']) != self.m:
            raise ValueError('Every complete row needs its real physical g and gradient norm')
        norms = np.array([row['gradient_coordinate_norm'] for row in metadata['rows']], dtype=float)
        scales = np.array([row['row_normalization_scale'] for row in metadata['rows']], dtype=float)
        gs = np.array([row['physical_g'] for row in metadata['rows']], dtype=float)
        if (not np.isfinite(norms).all() or np.any(norms < 0)
                or not np.isfinite(scales).all() or np.any(scales <= 0)
                or not np.isfinite(gs).all()):
            raise ValueError('Every restored row must have its finite actual gradient norm and positive row scale')
        discrepancy = np.max(np.abs(np.asarray(bounds)+gs/scales), initial=0.)
        tolerance = 32*np.finfo(float).eps*(1+np.max(np.abs(bounds), initial=0.))
        if discrepancy > tolerance:
            raise ValueError('The complete typed row physical margin changed before Phase I')
        # The tiny positive padding is a declared SLACK initialization,
        # not an acceptance tolerance or an extra geometric margin.
        self.tau0 = max(0., float(gs.max(initial=0.)))+8*np.finfo(float).eps*(1+float(np.max(np.abs(gs), initial=0.)))
        denominator = np.hypot(norms, 1.)
        self.factors = scales/denominator
        self.slack_column = -1/denominator
        self.bounds = np.r_[(self.tau0-gs)/denominator, self.tau0]
        self.shape = (self.m+1, self.n+1)
        self.record = dict(schema='complete-all-typed-C-common-slack-phase-I-v1',
            original_rows=self.m, augmented_rows=self.m+1,
            all_original_rows_retained=True, tau_initial=self.tau0,
            current_physical_g_max=float(gs.max(initial=0.)),
            maximum_margin_formula_discrepancy=float(discrepancy),
            zero_physical_gradient_rows_retained=int(np.count_nonzero(norms == 0)),
            objective='.5*(tau0+delta_tau)^2+.5*mu_restore^2*(|z|^2+delta_tau^2)',
            constraints='g_i+dg_i[Tz] <= tau0+delta_tau for EVERY selected typed row; tau0+delta_tau>=0',
            positive_row_rescaling_changes_feasible_set=False,
            physical_feasibility_inferred_from_slack=False,
            operator_only_virtual_rows=True, full_duplicate_row_cache_bytes=0)

    def _discard(self):
        if isinstance(self.matrix, np.memmap) and hasattr(self.matrix._mmap, 'madvise') and hasattr(mmap, 'MADV_DONTNEED'):
            self.matrix._mmap.madvise(mmap.MADV_DONTNEED)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            rows, columns = index
            if rows != slice(None):
                raise IndexError('The frozen QPv3 uses full-row streamed column slices')
            if not isinstance(columns, slice):
                raise IndexError('Use an actual contiguous column slice')
            start, stop, step = columns.indices(self.n+1)
            if step != 1:
                raise IndexError('Only contiguous original QPv3 blocks are used')
            result = np.zeros((self.m+1, max(0, stop-start)))
            original_stop = min(stop, self.n)
            if start < original_stop:
                result[:self.m, :original_stop-start] = np.asarray(
                    self.matrix[:, start:original_stop])*self.factors[:, None]
            if start <= self.n < stop:
                result[:self.m, self.n-start] = self.slack_column
                result[self.m, self.n-start] = -1.
            self._discard()
            return result
        row = int(index)
        if row == self.m:
            result = np.zeros(self.n+1)
            result[-1] = -1.
            return result
        if not 0 <= row < self.m:
            raise IndexError(row)
        result = np.r_[np.asarray(self.matrix[row])*self.factors[row], self.slack_column[row]]
        self._discard()
        return result



def endpoint_readout(q):
    """A complete explicit current-point snapshot; no replacement from another point."""
    value = q.metadata()
    result = {name: value[name] for name in ROOT_SNAPSHOT_KEYS}
    result.update(schema=ROOT_SNAPSHOT_SCHEMA,
        operator_schema=value['schema'], operator_source_sha256=value['source_sha256'],
        model_identity_sha256=value['model_identity_sha256'],
        snapshot_scope='actual current point and its own fixed normal-chain/root cache at this call; absent numerical values remain null')
    return result


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'reference-bundle', 'preparation-report', 'carrier', 'node-report', 'scalar-input', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--manifest', type=Path, action='append', required=True)
    p.add_argument('--restart-checkpoint', type=Path)
    p.add_argument('--restart-report', type=Path)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--angle-block', type=int, default=8)
    p.add_argument('--integration-order', type=int, default=8)
    p.add_argument('--inverse-root-iterations', type=int, default=18)
    p.add_argument('--inverse-root-tolerance', type=float, default=2.e-12)
    p.add_argument('--norm-kind', choices=('jet-sum', 'integral'), default='jet-sum')
    p.add_argument('--radial-norm-length', type=float, default=.05)
    p.add_argument('--angular-transition', type=float, default=24.)
    p.add_argument('--torch-threads', type=int, default=4)
    p.add_argument('--damping', type=float, required=True)
    p.add_argument('--directions', type=int, default=2)
    p.add_argument('--maxiter', type=int, default=64)
    p.add_argument('--restoration-directions', type=int, default=4)
    p.add_argument('--restoration-damping', type=float, default=.01)
    p.add_argument('--restoration-maxiter', type=int, default=64)
    p.add_argument('--line-trials', type=int, default=15)
    p.add_argument('--qp-atol', type=float, default=0.)
    p.add_argument('--qp-rtol', type=float, default=1.e-6)
    p.add_argument('--qp-feasibility-tolerance', type=float, default=2.e-11)
    p.add_argument('--qp-rank-tolerance', type=float, default=2.e-12)
    p.add_argument('--active-rows', type=int, default=192)
    p.add_argument('--active-block-columns', type=int, default=32768)
    p.add_argument('--active-band', type=float, default=.025)
    p.add_argument('--reach-ratio', type=float, default=.03)
    p.add_argument('--reach-safety-factor', type=float, default=.992)
    p.add_argument('--marked-diameter-budget', type=float, default=4.2)
    p.add_argument('--witness-lower-budget', type=float, default=.9)
    p.add_argument('--amplitude-height-floor', type=float, default=1.01)
    p.add_argument('--amplitude-top-radius', type=int, default=2)
    p.add_argument('--amplitude-top-distance', type=int, default=4)
    p.add_argument('--spectral-p', type=int, default=4)
    p.add_argument('--spectral-epsilon', type=float, default=.001)
    p.add_argument('--spectral-scale', type=float, default=.05)
    p.add_argument('--legacy-fraction', type=float, default=.5)
    p.add_argument('--target', type=float, required=True)
    p.add_argument('--panels', type=int, default=128)

    for i in (1, 2):
        for position in ('left', 'middle', 'right'):
            p.add_argument('--endpoint-bubble-'+str(i)+'-'+position, required=True)
    p.add_argument('--endpoint-root-tolerance', type=float, default=2.e-12)
    p.add_argument('--endpoint-root-iterations', type=int, default=24)
    p.add_argument('--endpoint-root-backtracks', type=int, default=18)
    p.add_argument('--endpoint-root-armijo', type=float, default=1.e-4)
    p.add_argument('--endpoint-control-radius', type=float, default=2.)
    p.add_argument('--normal-stages', type=int, default=32)
    p.add_argument('--gamma-left', default='1/16')
    p.add_argument('--gamma-middle', default='1/8')
    p.add_argument('--gamma-right', default='3/16')
    p.add_argument('--seed-so3-checkpoint', type=Path)
    p.add_argument('--seed-so3-report', type=Path)
    moment_choice = p.add_mutually_exclusive_group(required=True)
    moment_choice.add_argument('--moment-trace-report', type=Path)
    moment_choice.add_argument('--moment-input', type=Path)
    p.add_argument('--moment-trace-report-sha256')
    p.add_argument('--moment-failed-report', type=Path)
    p.add_argument('--moment-input-sha256')
    p.add_argument('--moment-definition-sha256')
    p.add_argument('--moment-input-binding', choices=('same-reference', 'new-reference'), default='same-reference')
    a = p.parse_args()
    if a.moment_input_binding == 'new-reference' and a.moment_trace_report is not None:
        raise ValueError('The explicit new-reference mode adopts the published literal parameter input; it does not relabel an old trace as current')
    if a.moment_trace_report is not None:
        if a.moment_failed_report is None or a.moment_trace_report_sha256 is None or a.moment_input_sha256 is not None:
            raise ValueError('The actual-trace route needs its complete recorded failure and trace SHA; no small-file SHA is mixed in')
    elif (a.moment_input_sha256 is None or a.moment_definition_sha256 is None
            or a.moment_trace_report_sha256 is not None or a.moment_failed_report is not None):
        raise ValueError('The small fixed-parameter route needs its file SHA and the SAME complete definition identity')
    for digest in (a.moment_trace_report_sha256, a.moment_input_sha256, a.moment_definition_sha256):
        if digest is not None and (len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest)):
            raise ValueError('Use complete explicit SHA256 input identities')
    if bool(a.restart_checkpoint) != bool(a.restart_report):
        raise ValueError('A true SO3 restart needs both its own complete checkpoint and report')

    if bool(a.seed_so3_checkpoint) != bool(a.seed_so3_report):
        raise ValueError('A zero-closure seed needs the actual complete base checkpoint and report')
    if a.restart_checkpoint is not None and a.seed_so3_checkpoint is not None:
        raise ValueError('Choose a true zero-closure continuation or a new-field base seed, not both')
    for i in (1, 2):
        row = [Fraction(getattr(a, 'endpoint_bubble_'+str(i)+'_'+position))
            for position in ('left', 'middle', 'right')]
        if not 0 < row[0] < row[1] < row[2] < 1:
            raise ValueError('Declare complete strictly interior exact quintic bubble triples')
    if Fraction(a.endpoint_bubble_1_right) >= Fraction(a.endpoint_bubble_2_left):
        raise ValueError('The two complete bubble supports must be disjoint')
    gamma = [Fraction(getattr(a, 'gamma_'+position)) for position in ('left','middle','right')]
    if (not 0 < gamma[0] < gamma[1] < gamma[2] < 1
            or not any(Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_left')) < gamma[0]
                < gamma[2] < Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_right')) for i in (1,2))):
        raise ValueError('The complete independent gamma support must lie strictly inside an original bubble support')
    if (a.normal_stages < 1 or a.endpoint_root_iterations < 1 or a.endpoint_root_backtracks < 1
            or not 0 < a.endpoint_root_armijo < 1
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.endpoint_root_tolerance, a.endpoint_control_radius))):
        raise ValueError('Use explicit finite positive numerical endpoint-root parameters')
    if (min(a.directions, a.maxiter, a.line_trials, a.stage_block, a.angle_block,
            a.restoration_maxiter, a.active_rows, a.active_block_columns) < 1
            or a.restoration_directions < 0 or a.active_rows != 192
            or not 1 <= a.torch_threads <= 4 or a.angles != 2048 or a.panels < 1
            or not 0 < a.legacy_fraction < 1 or a.spectral_p < 2 or a.spectral_p%2
            or not 0 < a.reach_safety_factor < 1
            or not 0 < a.active_band < a.reach_safety_factor
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.damping, a.restoration_damping, a.target, a.spectral_epsilon,
                a.spectral_scale, a.radial_norm_length, a.angular_transition,
                a.inverse_root_tolerance, a.qp_rtol, a.reach_ratio))):
        raise ValueError('Use explicit valid full-space/fixed-target numerical parameters')
    for name in ('repo', 'reference_bundle', 'preparation_report', 'carrier', 'node_report',
                 'scalar_input', 'outdir', 'restart_checkpoint', 'restart_report',
                 'seed_so3_checkpoint', 'seed_so3_report', 'moment_trace_report',
                 'moment_failed_report', 'moment_input'):
        if getattr(a, name) is not None:
            setattr(a, name, getattr(a, name).resolve())
    a.manifest = [path.resolve() for path in a.manifest]
    return a


def main():
    total_started = time.monotonic()
    args = parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('Scientific closed SO3 construction and solving require public repository Actions')
    topic = args.repo/'topics/visible-flex-larger-amplitude'
    paths = {role: topic/relative for role, (relative, digest) in SOURCE_PINS.items()}
    for role, path in paths.items():
        if sha(path) != SOURCE_PINS[role][1]:
            raise ValueError('Changed actual complete scientific source '+role)
    if args.outdir.exists():
        raise FileExistsError('Use a fresh output directory for every actual complete budget')
    if args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('All scientific raw outputs and evaluation caches must stay outside the repository')
    args.outdir.mkdir(parents=True)
    output = args.outdir/'report.json'
    source_commit = subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip()
    preparation, reference_binding = actual_reference(args, paths)
    reference = load('_so3_independent_axisymmetric_reference', paths['reference'])
    meridian = load('_so3_actual_independent_axisymmetric_base', paths['meridian'])
    endpoint = load('_so3_independent_frozen_moment_zero_endpoint', paths['endpoint'])
    moment_binding = load('_so3_complete_frozen_moment_input', paths['frozen_moment_input'])
    new_moment_binding = load('_so3_explicit_new_reference_literal_Q', paths['new_moment_input'])
    geometry_module = load('_so3_complete_geometry_screen', paths['geometry'])
    spectral = load('_so3_same_spectral_loss', paths['spectral'])
    hessian = load('_so3_same_spectral_hessian', paths['hessian'])
    centered = load('_so3_same_centered_scalar', paths['centered'])
    qp = load('_so3_complete_QPv3', paths['qp'])
    history = load('_so3_complete_address_history', paths['history'])
    meridian.torch.set_num_threads(args.torch_threads)
    meridian.torch.set_num_interop_threads(1)
    context = reference.AxisymmetricReferenceContext.from_files(repo=args.repo,
        reference_bundle=args.reference_bundle,carrier=args.carrier,node_report=args.node_report,
        scalar_input=args.scalar_input,preparation_report=args.preparation_report,panels=args.panels)
    reference_problem, reference_prepared = context.create_problem(N=args.angles,stage_block=args.stage_block)
    fixed_profile = context.scalar_identity
    if context.model != preparation['reference_definition']:
        raise ValueError('The actual complete reference changed between report and construction')
    base = meridian.ClosedMeridianOperator(reference_problem,reference_prepared,reference,
        cache_directory=args.outdir/'fixed-axisymmetric-reference-cache',integration_order=args.integration_order,
        angle_block=args.angle_block,root_iterations=args.inverse_root_iterations,
        root_tolerance=args.inverse_root_tolerance,
        expected_parent_bundle_sha256=sha(args.reference_bundle))
    root_policy = endpoint.EndpointPolicy(endpoint_tolerance=args.endpoint_root_tolerance,
        maximum_iterations=args.endpoint_root_iterations,maximum_backtracks=args.endpoint_root_backtracks,
        armijo=args.endpoint_root_armijo,control_radius=args.endpoint_control_radius)
    normal_step_nodes = tuple(Fraction(i,args.normal_stages) for i in range(args.normal_stages+1))
    bubble_nodes = [[getattr(args, 'endpoint_bubble_'+str(i)+'_'+position)
        for position in ('left', 'middle', 'right')] for i in (1,2)]
    if args.moment_input_binding == 'new-reference':
        origin = moment_binding.from_parameter_file(args.moment_input,
            input_sha256=args.moment_input_sha256,
            expected_definition_identity_sha256=args.moment_definition_sha256)
        frozen_moment_input = new_moment_binding.bind_new_input(origin,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_definition_identity = new_moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_input_record = dict(mode='explicit NEW reference adopts complete published literal Q parameters',
            actual_parameter_file=file_record(args.moment_input),
            input_binding_source=file_record(paths['new_moment_input']),
            no_moment_or_inverse_recomputed=True, old_reference_or_initial_point_binding_inherited=False,
            same_mathematical_g_claimed=False, current_moment_inverse_property_claimed=False)
    else:
        if args.moment_trace_report is not None:
            frozen_moment_input = moment_binding.from_trace(args.repo, args.moment_trace_report,
                trace_report_sha256=args.moment_trace_report_sha256,
                failed_report=args.moment_failed_report,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference actual trace word extraction',
                actual_trace_report=file_record(args.moment_trace_report),
                actual_failed_report=file_record(args.moment_failed_report),
                no_moment_or_inverse_recomputed=True)
        else:
            frozen_moment_input = moment_binding.from_parameter_file(args.moment_input,
                input_sha256=args.moment_input_sha256,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference published complete parameter definition',
                actual_parameter_file=file_record(args.moment_input),
                no_moment_or_inverse_recomputed=True)
        moment_definition_identity = moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile, bubble_nodes=bubble_nodes)
    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],
        expected_base_schema='complete-independent-axisymmetric-so3-meridian-with-core-lift-v1',
        bubble_nodes=bubble_nodes, frozen_moment_input=frozen_moment_input, endpoint_policy=root_policy,
        normal_step_nodes=normal_step_nodes,
        gamma_nodes=(args.gamma_left,args.gamma_middle,args.gamma_right),
        new_input_binder=(new_moment_binding if args.moment_input_binding == 'new-reference' else None))
    coordinates = meridian.RotationH2Coordinates(q, radial_length=args.radial_norm_length,
        angular_transition=args.angular_transition, norm_kind=args.norm_kind)
    restart = seed_report = None
    if args.restart_checkpoint is not None:
        restart = json.loads(args.restart_report.read_text())
        if (restart.get('schema') != SCHEMA or restart.get('source_sha256') != sha(__file__)
                or restart.get('complete') is not True
                or restart.get('final_bundle_sha256') != sha(args.restart_checkpoint)
                or restart.get('model_identity_sha256') != q.identity
                or restart.get('fixed_scalar_metric', {}).get('identity_sha256') != fixed_profile
                or restart.get('observation_carrier_sha256') != sha(args.carrier)):
            raise ValueError('Continue only this true complete SO3 source and the identical exact mathematical field model')
        x = q.load_checkpoint(args.restart_checkpoint)
    elif args.seed_so3_checkpoint is not None:
        seed_report = json.loads(args.seed_so3_report.read_text())
        if (seed_report.get('schema') != 'complete-independent-axisymmetric-fixed-deep-so3-meridian-QP-v1'
                or seed_report.get('source_sha256') != SOURCE_PINS['axisymmetric_seed_driver'][1]
                or seed_report.get('complete') is not True
                or seed_report.get('final_bundle_sha256') != sha(args.seed_so3_checkpoint)
                or seed_report.get('model_identity_sha256') != base.identity
                or seed_report.get('fixed_scalar_metric', {}).get('identity_sha256') != fixed_profile
                or seed_report.get('observation_carrier_sha256') != sha(args.carrier)
                or seed_report.get('representation') != base.model):
            raise ValueError('Bind the actual complete direct-base field used only as original-variable seed')
        x = base.load_checkpoint(args.seed_so3_checkpoint)
    else:
        x = q.initial()
    address_parent = restart if restart is not None else seed_report
    address_parent_path = args.restart_report if restart is not None else args.seed_so3_report
    witnesses, radius_witnesses, history_record = all_locations(
        args, preparation, q, history, address_parent, address_parent_path)
    stage_weights = q.mixed_stage_weights(args.legacy_fraction)
    if not np.isfinite(stage_weights).all() or np.any(stage_weights <= 0):
        raise ValueError('Every original legacy/Gauss radial observation needs its positive weight')
    normalizer = float(stage_weights.sum()*q.full_N)
    parameters = spectral.Parameters(p=args.spectral_p, epsilon=args.spectral_epsilon, scale=args.spectral_scale)
    objective_key = 'centered_phi_normalized'
    # GeometryScreen is an independent new-field adapter. Its exact frozen
    # old selector is retained; no old physical point source is relabeled.
    budgets = geometry_module.Budgets(args.marked_diameter_budget, args.witness_lower_budget,
        q.R, args.amplitude_height_floor)
    screen = geometry_module.GeometryScreen(q, args.repo, budgets,
        reach_ratio=args.reach_ratio, reach_safety_factor=args.reach_safety_factor,
        amplitude_top_radius=args.amplitude_top_radius,
        amplitude_top_distance=args.amplitude_top_distance)
    report = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit,
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'), github_run_id=os.environ.get('GITHUB_RUN_ID'),
        source_paths={role: str(path) for role, path in paths.items()},
        source_sha256_by_role={role: sha(path) for role, path in paths.items()},
        complete=False, independent_preparation_report=file_record(args.preparation_report),
        input_bundle=str(args.reference_bundle), bundle_sha256=sha(args.reference_bundle),
        independent_reference_binding=reference_binding,
        observation_carrier=str(args.carrier), observation_carrier_sha256=sha(args.carrier),
        exact_tail_node_report_sha256=sha(args.node_report),
        exact_tail_scalar_input_sha256=sha(args.scalar_input),
        independent_reference_context=context.metadata(), model_identity_sha256=q.identity,
        M=q.M, J=q.J, N=q.full_N, all_full_rows=3*q.P*q.full_N,
        evaluated_orbit_rows=3*q.P*q.N, original_variables=q.free_size,
        fixed_scalar_metric=dict(identity_sha256=fixed_profile,
            exact_profile_definition=context.scalar_definition,
            target_fixed_before_first_direction=True, target_recomputed_from_current_field=False,
            moving_mean_projection=False, all_metric_mean_constraints_retained=True,
            formula='ds^2+a_deep(s)^2*dtheta0^2; fixed initial-core theta0 chart'),
        representation=q.model, coordinate_norm=coordinates.record,
        frozen_moment_Q_input=frozen_moment_input,
        frozen_moment_Q_definition_identity_sha256=moment_definition_identity,
        frozen_moment_Q_input_record=moment_input_record,
        actual_reference_initial_full_point_sha256=meridian.array_sha(base.initial()),
        moment_Q_recomputed_from_current_free_point=False,
        normal_auxiliary_nodes_are_physical_flex=False,
        normal_selection_changes_fixed_g=False,
        numerical_normal_stage_iterations_differentiated=False,
        final_implicit_J_uses_all_normal_stage_equations=True,
        previous_normal_frame_full_parameter_chain_retained=True,
        original_zero_control_target_full_parameter_chain_retained=True,
        final_original_physical_closure_is_separately_checked=True,
        moment_input_binding_mode=args.moment_input_binding,
        implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
        normal_stage_count=q.normal_stage_count,
        exact_normal_step_nodes=[str(v) for v in q.normal_step_nodes],
        complete_first_angular_implicit_dimension=6*q.normal_stage_count,
        complete_second_angular_implicit_dimension=9*q.normal_stage_count,
        stationary_KKT_selection_used=False,continuous_horizontal_ODE_solution_claimed=False,
        common_partition_for_all_angles_and_free_points=True,per_angle_adaptive_normal_partition=False,
        old_zero_field_or_root_certificate_inherited=False,
        changed_control_map_has_independent_model_identity=True,
        radial_weights=dict(legacy_fraction=args.legacy_fraction, normalizer=normalizer,
            positive_stage_weights_sha256=meridian.array_sha(stage_weights),
            positive_orbit_weights_sha256=meridian.array_sha(q.multiplicity),
            fixed_target_a_carrier_sha256=meridian.array_sha(q.a),
            every_original_row_positive=True),
        spectral_parameters=parameters.as_dict(), selected_scalar_objective_key=objective_key,
        numerical_reach_safety_factor=args.reach_safety_factor,
        amplitude_design_constraints=dict(budgets=budgets.metadata()),
        history=history_record, initial_permanent_position_counts=dict(curvature=len(witnesses), radius=len(radius_witnesses)),
        permanent_position_identity='cell and literal binary64 u/phi; no decimal rounding or byte cap',
        restart=None if restart is None else dict(report=file_record(args.restart_report),
            checkpoint=file_record(args.restart_checkpoint), previous_final_Phi_not_used_as_new_measure_value=True),
        new_zero_closure_seed_changes_physical_field=restart is None,
        direct_base_seed=None if seed_report is None else dict(report=file_record(args.seed_so3_report),
            checkpoint=file_record(args.seed_so3_checkpoint), actual_base_model_identity_sha256=base.identity,
            all_original_variables_copied=True, old_Phi_or_certificates_inherited=False),
        radial_metric_error_identically_zero=True,
        radial_identity_scope='exact unit-rotation integral definition; finite evaluation errors unpaid',
        radial_Gram_uses_complete_hprime_Delta=False,
        numerical_radial_Gram_row_retained=True,
        endpoint_implicit_J_separate_from_Newton=True,
        old_continuous_geometry_certificates_inherited=False,
        old_metric_acceptance_inherited=False,
        new_geometry_and_metric_reread_before_any_acceptance=True,
        maximum_requested_metric_directions=args.directions,
        maximum_requested_restoration_directions=args.restoration_directions,
        maxiter=args.maxiter, initial_damping=args.damping,
        restoration_damping=args.restoration_damping,
        restoration_maxiter=args.restoration_maxiter,
        initial_zero_feasibility_not_assumed=True,
        common_slack_residual_never_called_geometric_feasibility=True,
        target=args.target, target_is_not_README_original_solver_floor=True,
        metric_directions=[], restoration_directions=[],
        continuous_metric_certified=False, continuous_geometry_certified=False,
        closed_isometry_accepted=False,
        working_evaluation=dict(integration_order=args.integration_order,
            inverse_root_iterations=args.inverse_root_iterations,
            inverse_root_tolerance=args.inverse_root_tolerance, angle_block=args.angle_block,
            endpoint_root_policy=root_policy.metadata(),
            normal_stage_count=q.normal_stage_count,
            exact_normal_step_nodes=[str(v) for v in q.normal_step_nodes],
            actual_normal_step_carriers_binary64_hex=[v.hex() for v in q.normal_step_carriers],
            exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],
            exact_relative_gamma_nodes=q.model['exact_relative_gamma_nodes'],
            implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
            complete_first_angular_implicit_dimension=6*q.normal_stage_count,
            complete_second_angular_implicit_dimension=9*q.normal_stage_count,
            fixed_moment_Q_definition_identity_sha256=moment_definition_identity,
            old_endpoint_coordinate_ball_certificate_inherited=False,
            torch_threads=args.torch_threads, torch_version=meridian.torch.__version__,
            numpy_version=np.__version__, scipy_version=scipy.__version__,
            quadrature_error_enclosed=False, root_error_enclosed=False,
            evaluation_refinement_changes_exact_target=False))

    def save_report():
        report['latest_operator_metadata'] = q.metadata()
        report['current_permanent_position_counts'] = dict(curvature=len(witnesses), radius=len(radius_witnesses))
        report['peak_rss_KiB'] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        write_json(output, report)

    def statistics(point, native):
        raw = q.unweight(native)
        e, f, d = raw[..., 0], raw[..., 1], raw[..., 2]
        spectrum = spectral.statistics(raw, stage_weights, q.multiplicity, parameters)
        spectrum = centered.augment_statistics(raw, stage_weights, q.multiplicity, parameters,
            spectrum, stage_block=args.stage_block)
        old = raw[:q.legacy_P]
        maximum = lambda a: float(np.max((np.abs(a[..., 0]+a[..., 2])
            +np.hypot(a[..., 0]-a[..., 2], 2*a[..., 1]))/2))
        return dict(spectral=spectrum, max_relative_gram=maximum(raw), legacy_max_relative_gram=maximum(old),
            min_relative_E=float(np.min(1+e)),
            min_relative_determinant=float(np.min((1+e)*(1+d)-f*f)),
            fixed_scalar_metric_identity_sha256=fixed_profile, fixed_target=True,
            full_metric_mean_and_cross_rows_retained=True, domain=q.domain(point),
            endpoint_roots=endpoint_readout(q))

    def remember(geometry):
        # The screen returns exact physical locations actually read on this
        # field. Both complete permanent memories remain append-only.
        added = dict(curvature=0, radius=0)
        for value in geometry.get('new_curvature_locations', []):
            added['curvature'] += int(add_location(value, witnesses, q))
        for value in geometry.get('new_radius_locations', []):
            added['radius'] += int(add_location(value, radius_witnesses, q))
        return added

    def scan(point):
        result = screen.scan(point, witnesses, radius_witnesses)
        result['newly_remembered'] = remember(result)
        return result

    def physical_violation(geometry):
        if not geometry.get('complete', False):
            return None
        value = geometry.get('maximum_physical_g')
        if value is None or not math.isfinite(float(value)):
            return None
        return max(0., float(value))

    def geometric_feasible(geometry):
        return bool(geometry.get('complete', False) and geometry.get('passed', False)
            and physical_violation(geometry) == 0.)

    write_json(output, report)
    event(event='SO3_actual_complete_problem_prepared', model_identity_sha256=q.identity,
        fixed_scalar_metric_identity_sha256=fixed_profile, free_variables=q.free_size,
        full_orbit_rows=3*q.P*q.full_N, actual_quarter_rows=3*q.P*q.N,
        integration_order=args.integration_order, next_actual_operation='complete_new_field_metric_and_geometry')
    try:
        native = q.residual(x)
        current = statistics(x, native)
        geometry = scan(x)
    except (ValueError, RuntimeError, FloatingPointError, OverflowError) as error:
        report.update(complete=False, stop_reason='actual_initial_zero_closure_field_read_failed',
            actual_initial_read_error=repr(error), initial_endpoint_roots=endpoint_readout(q),
            total_actual_seconds=time.monotonic()-total_started,
            initial_failed_candidate_is_not_an_accepted_field=True)
        save_report()
        event(event='zero_closure_actual_initial_field_failure', report=str(output), error=repr(error),
            endpoint_roots=report['initial_endpoint_roots'], global_nonexistence_claimed=False)
        raise
    report['initial'] = current
    report['initial_geometry'] = geometry
    initial = args.outdir/'initial-new-field.npz'
    q.save(initial, x)
    report['initial_new_bundle'] = file_record(initial)
    report['current'] = current
    report['initial_actual_setup_and_full_read_seconds'] = time.monotonic()-total_started
    save_report()
    event(event='SO3_complete_new_field_initial_read', statistics=current,
        geometry_complete=geometry.get('complete'), geometric_feasible=geometric_feasible(geometry),
        maximum_physical_g=geometry.get('maximum_physical_g'))
    damping, restoration_damping = args.damping, args.restoration_damping
    metric_count, restoration_count, serial = 0, 0, 0
    stop_reason = 'declared_metric_direction_budget'
    while metric_count < args.directions:
        # Rejected trials can discover new permanent locations. The SAME
        # current parent is reread against that expanded set before its C.
        geometry = scan(x)
        feasible = geometric_feasible(geometry)
        if physical_violation(geometry) is None:
            stop_reason = 'current_true_geometry_not_defined; no linearization or global impossibility claimed'
            break
        phase = 'metric' if feasible else 'restoration'
        if phase == 'restoration' and restoration_count >= args.restoration_directions:
            stop_reason = 'declared_restoration_budget; actual_violation_remains_and_is_not_accepted'
            break
        if phase == 'metric' and current['max_relative_gram'] <= args.target:
            stop_reason = 'actual_sample_target_reached; no_continuous_or_refinement_claim'
            break
        started = time.monotonic()
        operator_counts_before = dict(q.counts)
        C, bounds, rows = screen.build_rows(x, coordinates.transpose,
            coordinate_size=q.free_size, witnesses=witnesses, radius_witnesses=radius_witnesses,
            current_geometry=geometry, matrix_workdir=args.outdir/f'rows-{serial:03d}',
            max_rows=args.active_rows, active_band=args.active_band,
            block_columns=args.active_block_columns)
        if rows.get('no_original_row_removed') is not True:
            raise ValueError('The original full 192 selection prefix must remain in every phase')
        if len(rows['rows']) != C.shape[0] or bounds.shape != (C.shape[0],):
            raise ValueError('Every selected row must keep its actual bound and full metadata')
        serial += 1
        record = dict(index=metric_count if phase == 'metric' else restoration_count,
            serial=serial-1, phase=phase, starting_statistics=current,
            starting_geometry=geometry, complete_selected_inequalities=rows,
            accepted=False, trials=[], original_geometry_rows_retained=rows['original_prefix_rows'],
            appended_amplitude_rows=rows['appended_amplitude_rows'])
        record['full_geometry_and_row_preparation_seconds'] = time.monotonic()-started
        if phase == 'metric':
            if np.min(bounds, initial=0.) < -args.qp_feasibility_tolerance:
                raise ValueError('The full typed C contradicts the freshly read feasible parent')
            bridge = hessian.NativeLinearization(q, x, stage_weights, parameters, spectral_module=spectral)
            factor = math.sqrt(parameters.k/(parameters.scale**2*normalizer))
            residual = factor*bridge.residual
            A = LinearOperator((len(residual), q.free_size), dtype=np.float64,
                matvec=lambda z: factor*bridge.operator.matvec(coordinates.lift(z)),
                rmatvec=lambda v: factor*coordinates.transpose(bridge.operator.rmatvec(v)))
            used_damping, maxiter = damping, args.maxiter
            record['quadratic_model'] = dict(schema='complete-SO3-R664-positive-residual-Hessian-v1',
                bridge=bridge.metadata(), outer_half_Hessian_factor=factor*factor,
                gradient_and_Hessian_units_unchanged_from_declared_Phi=True,
                physical_coordinate_norm=coordinates.record, damping=used_damping,
                virtual_rhs_norm_is_actual_Phi=False, all_metric_mean_constraints_retained=True)
            solve_C, solve_bounds = C, bounds
        else:
            relaxed = CommonSlackRows(C, bounds, rows)
            residual = np.array([relaxed.tau0])
            A = LinearOperator((1, q.free_size+1), dtype=np.float64,
                matvec=lambda z: np.array([np.asarray(z)[-1]]),
                rmatvec=lambda v: np.r_[np.zeros(q.free_size), np.asarray(v)[0]])
            used_damping, maxiter = restoration_damping, args.restoration_maxiter
            record['quadratic_model'] = dict(relaxed.record, damping=used_damping,
                original_geometry_rows_retained=rows['original_prefix_rows'],
                amplitude_rows_retained=rows['appended_amplitude_rows'])
            solve_C, solve_bounds = relaxed, relaxed.bounds
        record['actual_full_linearization_preparation_seconds'] = time.monotonic()-started
        event(event='SO3_actual_complete_quadratic_model_ready', phase=phase, serial=serial-1,
            full_variable_count=int(A.shape[1]), selected_row_count=int(solve_C.shape[0]),
            preparation_seconds=record['actual_full_linearization_preparation_seconds'],
            old_maximum_gram=current['max_relative_gram'],
            old_positive_physical_g=physical_violation(geometry), damping=used_damping)
        qp_started = time.monotonic()
        qp_counts_before = dict(q.counts)
        coordinate_step, qp_report = qp.solve(A, residual, solve_C, solve_bounds,
            damping=used_damping, block_columns=args.active_block_columns,
            parameters=qp.Parameters(maxiter=maxiter, atol=args.qp_atol, rtol=args.qp_rtol,
                feasibility_tolerance=args.qp_feasibility_tolerance,
                rank_tolerance=args.qp_rank_tolerance, progress_every=1),
            callback=lambda value: event(event='SO3_actual_QP_progress', phase=phase, serial=serial-1, progress=value))
        record['qp'] = qp_report
        record['actual_QP_seconds'] = time.monotonic()-qp_started
        record['actual_QP_operator_counts'] = {key: q.counts[key]-qp_counts_before[key] for key in q.counts}
        record['actual_damping'] = used_damping
        record['coordinate_step_norm'] = float(np.linalg.norm(coordinate_step))
        physical_coordinate_step = coordinate_step if phase == 'metric' else coordinate_step[:-1]
        original_linear_values = qp.StreamedRows(C, args.active_block_columns).matvec(physical_coordinate_step)
        record['selected_linear_physical_g'] = [float(row['physical_g']
            +row['row_normalization_scale']*value)
            for row, value in zip(rows['rows'], original_linear_values)]
        record['maximum_selected_linear_physical_g'] = max(record['selected_linear_physical_g'], default=None)
        step = coordinates.lift(physical_coordinate_step)
        old_merit = current['spectral'][objective_key]
        old_violation = physical_violation(geometry)
        if phase == 'metric':
            linear = A.matvec(coordinate_step)
            half_slope = float(residual@linear)
            predicted = 2*half_slope+float(linear@linear)
            record.update(half_objective_slope=half_slope,
                predicted_actual_Phi_change=predicted, old_actual_Phi=old_merit)
        else:
            half_slope, predicted = None, None
            record['computed_common_slack'] = float(relaxed.tau0+coordinate_step[-1])
            record['common_slack_not_used_as_nonlinear_feasibility'] = True
        record['old_actual_maximum_positive_physical_g'] = old_violation
        step_path = args.outdir/f'{phase}-direction-{record["index"]:03d}.npz'
        np.savez(step_path, full_physical_step=step, coordinate_step=coordinate_step,
            representation_identity_sha256=np.array(q.identity))
        record['direction'] = file_record(step_path)
        # Release the full positive residual-Hessian storage before trials.
        if phase == 'metric':
            del bridge
        del A, residual, coordinate_step, solve_C, solve_bounds
        alpha = 1.
        for trial_index in range(args.line_trials):
            trial_started = time.monotonic()
            candidate = x+alpha*step
            trial = dict(index=trial_index, alpha=alpha, accepted=False,
                metric_descent_required=phase == 'metric', full_true_geometry_read=False)
            trial_native, trial_statistics, trial_geometry = None, None, None
            try:
                trial_native = q.residual(candidate)
                trial_statistics = statistics(candidate, trial_native)
                domain_ok = (trial_statistics['min_relative_E'] > 0
                    and trial_statistics['min_relative_determinant'] > 0)
                trial_merit = trial_statistics['spectral'][objective_key]
                descent = (trial_merit < old_merit and (half_slope is None or half_slope >= 0
                    or trial_merit <= old_merit+.0002*alpha*half_slope))
                if domain_ok and (phase == 'restoration' or descent):
                    trial_geometry = scan(candidate)
                    trial['full_true_geometry_read'] = True
                trial_violation = None if trial_geometry is None else physical_violation(trial_geometry)
                if phase == 'metric':
                    accepted = domain_ok and descent and trial_geometry is not None and geometric_feasible(trial_geometry)
                else:
                    accepted = (domain_ok and trial_violation is not None
                        and trial_violation < old_violation
                        and trial_violation <= (1-1.e-4*alpha)*old_violation)
                trial.update(statistics=trial_statistics, domain_feasible=domain_ok,
                    actual_Phi_descent=descent, actual_positive_physical_g=trial_violation,
                    full_geometry=trial_geometry, accepted=bool(accepted),
                    physically_feasible=False if trial_geometry is None else geometric_feasible(trial_geometry))
            except (FloatingPointError, OverflowError, ValueError, RuntimeError) as exception:
                accepted = False
                trial.update(actual_read_error=repr(exception), accepted=False,
                    complete=False, scope='A true numerical trial failure, not global infeasibility')
            trial['endpoint_roots'] = endpoint_readout(q)
            trial['actual_seconds'] = time.monotonic()-trial_started
            record['trials'].append(trial)
            event(event='SO3_actual_trial', phase=phase, serial=serial-1,
                index=trial_index, alpha=alpha, accepted=bool(accepted),
                maximum_gram=None if trial_statistics is None else trial_statistics['max_relative_gram'],
                actual_Phi=None if trial_statistics is None else trial_statistics['spectral'][objective_key],
                actual_positive_physical_g=trial.get('actual_positive_physical_g'),
                actual_read_error=trial.get('actual_read_error'))
            if accepted:
                x, native, current, geometry = candidate, trial_native, trial_statistics, trial_geometry
                record.update(accepted=True, accepted_alpha=alpha, accepted_statistics=current,
                    accepted_geometry=geometry)
                accepted_path = args.outdir/f'accepted-{phase}-{record["index"]:03d}.npz'
                q.save(accepted_path, x)
                record['accepted_bundle'] = file_record(accepted_path)
                if phase == 'metric':
                    ratio = (old_merit-current['spectral'][objective_key])/(-predicted) if predicted < 0 else None
                    record['actual_to_full_prediction_ratio'] = ratio
                    if alpha == 1 and ratio is not None and ratio > .75:
                        damping = max(1.e-8, damping/2)
                elif geometric_feasible(geometry):
                    record['actual_restoration_reached_zero_true_violation'] = True
                break
            alpha /= 2
        if not record['accepted']:
            if phase == 'metric':
                damping *= 4
            else:
                restoration_damping *= 4
        record['seconds'] = time.monotonic()-started
        record['actual_complete_direction_operator_counts'] = {
            key: q.counts[key]-operator_counts_before[key] for key in q.counts}
        record['damping_after_direction'] = damping if phase == 'metric' else restoration_damping
        report[phase+'_directions'].append(record)
        report['current'] = current
        if phase == 'metric':
            metric_count += 1
        else:
            restoration_count += 1
        q.clear_base()
        del C, bounds, step
        if phase == 'restoration':
            del relaxed
        save_report()
    # All newly found addresses are screened on the SAME final field. The
    # screen itself has already read any extrema it proposes remembering.
    geometry = scan(x)
    current = statistics(x, q.residual(x))
    final = args.outdir/'final.npz'
    q.save(final, x)
    report.update(complete=True, stop_reason=stop_reason, final_statistics=current,
        total_actual_seconds=time.monotonic()-total_started,
        current=current, final_geometry=geometry, final_bundle=str(final), final_bundle_sha256=sha(final),
        final_damping=damping, final_restoration_damping=restoration_damping,
        actual_metric_directions=metric_count, actual_restoration_directions=restoration_count,
        actual_accepted_metric_directions=sum(bool(r['accepted']) for r in report['metric_directions']),
        actual_accepted_restoration_directions=sum(bool(r['accepted']) for r in report['restoration_directions']),
        final_curvature_memory=witnesses, final_radius_memory=radius_witnesses,
        final_permanent_position_counts=dict(curvature=len(witnesses), radius=len(radius_witnesses)),
        final_true_sampled_geometry_feasible=geometric_feasible(geometry),
        sample_target_reached=current['max_relative_gram'] <= args.target,
        independent_reference_context_final=context.metadata(),
        limitations='A complete finite new implicit-zero-closure field solve, not a closed-isometry or reach certificate. The full R695 uniform root conditions are unverified; successful numerical roots and first parameter implicit derivatives do not certify a continuous root branch. Ordinary quadrature, scalar-carrier normalization, core inverse roots and metric/geometry maxima need continuous same-field error bounds. Core/cap C2 identities are structural in the exact formula and their numerical evaluation errors remain unpaid. Full all-t and E3/held obligations, fixed-problem radial/angular/evaluation refinement and a meaningful solver floor remain. Restored common slack or a budget limit never proves physical feasibility, nonexistence or convergence.')
    save_report()
    event(event='SO3_complete_actual_numerical_budget_returned', report=str(output),
        final_bundle_sha256=sha(final), sample_target_reached=report['sample_target_reached'],
        true_sampled_geometry_feasible=report['final_true_sampled_geometry_feasible'],
        statistics=current, stop_reason=stop_reason)


if __name__ == '__main__':
    main()
