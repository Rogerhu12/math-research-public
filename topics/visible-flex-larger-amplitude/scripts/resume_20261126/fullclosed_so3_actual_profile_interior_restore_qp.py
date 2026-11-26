#!/usr/bin/env python3
"""Full closed SO(3) optimization with a strict Phase I interior search target.

This is an independently declared representation.  All rotation modes and
shared-quintic jets, all formerly free core coefficients, and H are used.
The explicit closure lift is inside every Gram and geometric derivative.
The exact old 192-row selection is retained through a genuine new-field
adapter, and its prefix is followed by the complete selected amplitude
rows.  A common-slack Phase I is a numerical restoration, never a proof
that a residual slack is geometrically feasible. The explicit positive interior
margin only tightens the Phase I search model; the original physical g and
all true nonlinear acceptance conditions remain unchanged.
"""
import argparse
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


SCHEMA = 'complete-actual-fixed-deep-parent-closed-so3-interior-restore-QP-v1'
TRUSTED_PREDECESSOR_SCHEMA = 'complete-actual-fixed-deep-parent-closed-so3-meridian-QP-v1'
TRUSTED_PREDECESSOR_SOURCE_SHA256 = '7e9095b3a765f064baae9a36e9593667d5c469686232b6095065e0c3cf22c55b'
SOURCE_PINS = {
    'actual_parent_binding': ('scripts/resume_20261126/so3_same_parent_fixed_scalar_binding.py', '9ca39afd9f840ba89fbb75d7365220c2d85d26ddb26b2d66b6c55e611313fd55'),
    'dense': ('notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py', 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d'),
    'batch': ('scripts/resume_20261120_batched_closed_gram.py', '02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a'),
    'observed': ('scripts/resume_20261120/gauss_observed_closed_gram.py', '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d'),
    'factory': ('scripts/resume_20261126/deep_valley_reference_factory.py', '4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'),
    'base_factory': ('scripts/resume_20261120/exact_reference_tail_lift.py', '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'),
    'deep_scalar': ('scripts/resume_20261126/deep_valley_tail_input.py', 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'),
    'scalar': ('notes/2026-11-17-parallel-model-full-hold-oracle.py', 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'),
    'integer': ('notes/2026-11-17-parallel-inward-integral-enclosure.py', 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'),
    'hold': ('scripts/parallel_20261117_negative_hold_profile_ivp.py', 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'),
    'parent_jet': ('scripts/resume_20261126/so3_parent_meridian_jet.py', 'd3f25bb74e179865b20f7759bc1ee8dcdf2c2771f062ac096ee4d5398a8be4b9'),
    'meridian': ('scripts/resume_20261126/so3_closed_meridian_operator.py', '234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42'),
    'geometry': ('scripts/resume_20261126/so3_closed_meridian_geometry.py', '72f3825913c9ac07b30dcbc47f34e4d8ad901c2f6b6cab0cdc50f35ab99a3cc6'),
    'qp': ('scripts/resume_20261120/fullspace_feasible_active_cg_v3.py', 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'),
    'spectral': ('scripts/resume_20261120/positive_spectral_gram_weights.py', 'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'),
    'hessian': ('scripts/resume_20261120/positive_spectral_gram_hessian.py', '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4'),
    'centered': ('scripts/resume_20261126/centered_spectral_statistics.py', '5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'),
    'history': ('scripts/resume_20261120/launch_refinement_from_full_report.py', '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'),
    'deep_parent': ('scripts/resume_20261126/fullclosed_deep_scalar_amplitude_qp.py', 'd3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95'),
    'deep_soc_parent': ('scripts/resume_20261126/fullclosed_deep_amplitude_separation_soc.py', '329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90'),
    'deep_parent_binder': ('scripts/resume_20261126/derive_deep_amplitude_separation_soc.py', 'd80f9af278b89796d64cebf708080499cd44e3a8cde089be1009b7c26e2105ec'),
}


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


def actual_parent(args, paths):
    binder = load('_so3_actual_same_parent_input_binding', paths['actual_parent_binding'])
    return binder.bind_actual_parent(args, paths)


def all_locations(args, parent, q, history, restart=None):
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

    if int(parent['N']) != q.full_N or (restart is not None and int(restart['N']) != q.full_N):
        raise ValueError('Never reinterpret a tagged parent grid index under another full angle count')
    points = history.Locations(q.J, q.P, q.full_N)
    sources = [file_record(args.parent_report)]
    points.walk(parent, path=('actual_frozen_parent_report',))
    if restart is not None:
        points.walk(restart, path=('complete_actual_SO3_restart_report',))
        sources.append(file_record(args.restart_report))
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
        new_locations_use='fixed frozen-parent material chart phi0, never the moving internal phi_c',
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

    For an explicitly declared eps_in>0, every original physical row has
    g_i+dg_i[Tz]+eps_in <= tau0+delta_tau. The original C_i and physical
    g_i metadata remain unchanged. Positive row renormalization is applied
    to BOTH sides; the extra row imposes tau0+delta_tau>=0. This is a stricter
    search target, never an allowance of positive true physical g.
    """
    def __init__(self, matrix, bounds, metadata, *, interior_margin):
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
        if not math.isfinite(interior_margin) or interior_margin <= 0:
            raise ValueError('The declared Phase I interior search margin must be strictly positive')
        goal_g = gs+interior_margin
        if not np.isfinite(goal_g).all():
            raise FloatingPointError('The explicit interior search target must remain finite')
        # This padding only initializes a feasible augmented slack point.
        # interior_margin is separate, explicit, and never an acceptance tolerance.
        self.tau0 = max(0., float(goal_g.max(initial=0.)))+8*np.finfo(float).eps*(1+float(np.max(np.abs(goal_g), initial=0.)))
        denominator = np.hypot(norms, 1.)
        self.factors = scales/denominator
        self.slack_column = -1/denominator
        self.bounds = np.r_[(self.tau0-goal_g)/denominator, self.tau0]
        self.shape = (self.m+1, self.n+1)
        self.record = dict(schema='complete-all-typed-C-interior-common-slack-phase-I-v1',
            original_rows=self.m, augmented_rows=self.m+1,
            all_original_rows_retained=True, tau_initial=self.tau0,
            current_physical_g_max=float(gs.max(initial=0.)),
            search_interior_margin=float(interior_margin),
            current_search_target_g_max=float(goal_g.max(initial=0.)),
            original_physical_g_changed=False,
            original_nonlinear_acceptance_relaxed=False,
            stricter_search_target=True,
            maximum_margin_formula_discrepancy=float(discrepancy),
            zero_physical_gradient_rows_retained=int(np.count_nonzero(norms == 0)),
            objective='.5*(tau0+delta_tau)^2+.5*mu_restore^2*(|z|^2+delta_tau^2)',
            constraints='g_i+dg_i[Tz]+eps_in <= tau0+delta_tau for EVERY selected typed row; tau0+delta_tau>=0; eps_in>0 is only a search target',
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


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'parent-bundle', 'parent-report', 'carrier', 'node-report', 'scalar-input', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--manifest', type=Path, action='append', required=True)
    p.add_argument('--restart-checkpoint', type=Path)
    p.add_argument('--restart-report', type=Path)
    p.add_argument('--eta-start-node', type=int, required=True)
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
    p.add_argument('--restoration-interior-margin', type=float, default=1.e-8)
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
    p.add_argument('--scalar-admission-seconds', type=float, default=300.)
    p.add_argument('--scalar-integral-tolerance', default='1e-18')
    p.add_argument('--scalar-tail-cutoff', default='1/8')
    a = p.parse_args()
    if bool(a.restart_checkpoint) != bool(a.restart_report):
        raise ValueError('A true SO3 restart needs both its own complete checkpoint and report')
    if (min(a.directions, a.maxiter, a.line_trials, a.stage_block, a.angle_block,
            a.restoration_maxiter, a.active_rows, a.active_block_columns) < 1
            or a.restoration_directions < 0 or a.active_rows != 192
            or not 1 <= a.torch_threads <= 4 or a.angles%4 or a.angles < 2048
            or not 0 < a.legacy_fraction < 1 or a.spectral_p < 2 or a.spectral_p%2
            or not 0 < a.reach_safety_factor < 1
            or not 0 < a.active_band < a.reach_safety_factor
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.damping, a.restoration_damping, a.target, a.spectral_epsilon,
                a.spectral_scale, a.radial_norm_length, a.angular_transition,
                a.inverse_root_tolerance, a.qp_rtol, a.reach_ratio,
                a.restoration_interior_margin))):
        raise ValueError('Use explicit valid full-space/fixed-target numerical parameters')
    for name in ('repo', 'parent_bundle', 'parent_report', 'carrier', 'node_report',
                 'scalar_input', 'outdir', 'restart_checkpoint', 'restart_report'):
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
    parent_report, parent_binding = actual_parent(args, paths)
    # Freeze the actual canonical target once, before constructing any new field.
    fixed_profile = parent_binding['fixed_scalar_target']['identity_sha256']
    actual_binding = load('_so3_actual_rebuilt_context_binding', paths['actual_parent_binding'])
    factory = load('_so3_same_deep_factory', paths['factory'])
    batch = load('_so3_parent_complete_batch', paths['batch'])
    meridian = load('_so3_complete_closed_meridian', paths['meridian'])
    parent_jets = load('_so3_exact_parent_world_jets', paths['parent_jet'])
    geometry_module = load('_so3_complete_geometry_screen', paths['geometry'])
    spectral = load('_so3_same_spectral_loss', paths['spectral'])
    hessian = load('_so3_same_spectral_hessian', paths['hessian'])
    centered = load('_so3_same_centered_scalar', paths['centered'])
    qp = load('_so3_complete_QPv3', paths['qp'])
    history = load('_so3_complete_address_history', paths['history'])
    meridian.torch.set_num_threads(args.torch_threads)
    meridian.torch.set_num_interop_threads(1)
    context = factory.TailLiftContext.from_files(bundle=args.parent_bundle,
        carrier=args.carrier, node_report=args.node_report, scalar_input=args.scalar_input,
        scalar_source=paths['scalar'], integer_source=paths['integer'], hold_source=paths['hold'],
        observed_source=paths['observed'], eta_start_node=args.eta_start_node, lambda_value=1.,
        base_factory_source=paths['base_factory'], deep_scalar_source=paths['deep_scalar'],
        scalar_admission_seconds=args.scalar_admission_seconds,
        scalar_integral_tolerance=args.scalar_integral_tolerance,
        scalar_tail_cutoff=args.scalar_tail_cutoff)
    parent_problem, _ = context.create_pair(paths['dense'], batch,
        N=args.angles, stage_block=args.stage_block, quarter=True)
    parent_x, affine = parent_problem.pack(context.data['qjets'], float(context.data['Hcap']), require_affine=True)
    rebuilt_parent_binding = actual_binding.bind_rebuilt_context(context, parent_report, parent_binding)
    if (context.deep.model_identity_sha256 != fixed_profile
            or context.definition() != parent_report['exact_tail_context_final']['definition']):
        raise ValueError('The actual full same-parent context or immutable scalar profile changed')
    q = meridian.ClosedMeridianOperator(parent_problem, parent_problem.prepare(parent_x), parent_jets,
        cache_directory=args.outdir/'frozen-parent-meridian-cache', integration_order=args.integration_order,
        angle_block=args.angle_block, root_iterations=args.inverse_root_iterations,
        root_tolerance=args.inverse_root_tolerance,
        expected_parent_bundle_sha256=parent_report['final_bundle_sha256'])
    coordinates = meridian.RotationH2Coordinates(q, radial_length=args.radial_norm_length,
        angular_transition=args.angular_transition, norm_kind=args.norm_kind)
    restart = None
    if args.restart_checkpoint is not None:
        restart = json.loads(args.restart_report.read_text())
        predecessor_path = topic/'scripts/resume_20261126/fullclosed_so3_actual_profile_qp.py'
        if sha(predecessor_path) != TRUSTED_PREDECESSOR_SOURCE_SHA256:
            raise ValueError('The explicitly permitted complete predecessor source changed')
        permitted_pairs = {(SCHEMA, sha(__file__)),
            (TRUSTED_PREDECESSOR_SCHEMA, TRUSTED_PREDECESSOR_SOURCE_SHA256)}
        if ((restart.get('schema'), restart.get('source_sha256')) not in permitted_pairs
                or restart.get('source_sha256_by_role') != {role: digest for role, (_, digest) in SOURCE_PINS.items()}
                or restart.get('bundle_sha256') != sha(args.parent_bundle)
                or restart.get('original_parent_report', {}).get('sha256') != sha(args.parent_report)
                or restart.get('exact_tail_node_report_sha256') != sha(args.node_report)
                or restart.get('exact_tail_scalar_input_sha256') != sha(args.scalar_input)
                or restart.get('coordinate_norm', {}).get('norm_identity_sha256') != coordinates.record['norm_identity_sha256']
                or restart.get('complete') is not True
                or restart.get('final_bundle_sha256') != sha(args.restart_checkpoint)
                or restart.get('model_identity_sha256') != q.identity
                or restart.get('fixed_scalar_metric', {}).get('identity_sha256') != fixed_profile
                or restart.get('observation_carrier_sha256') != sha(args.carrier)):
            raise ValueError('Continue only the two explicitly trusted complete source/schema pairs with identical inputs, norm and exact field model')
        x = q.load_checkpoint(args.restart_checkpoint)
    else:
        x = q.initial()
    witnesses, radius_witnesses, history_record = all_locations(args, parent_report, q, history, restart)
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
        complete=False, original_parent_report=file_record(args.parent_report),
        input_bundle=str(args.parent_bundle), bundle_sha256=sha(args.parent_bundle),
        frozen_parent_binding=parent_binding, rebuilt_parent_context_binding=rebuilt_parent_binding,
        frozen_parent_affine=affine,
        observation_carrier=str(args.carrier), observation_carrier_sha256=sha(args.carrier),
        exact_tail_node_report_sha256=sha(args.node_report),
        exact_tail_scalar_input_sha256=sha(args.scalar_input),
        exact_tail_context=context.metadata(), model_identity_sha256=q.identity,
        M=q.M, J=q.J, N=q.full_N, all_full_rows=3*q.P*q.full_N,
        evaluated_orbit_rows=3*q.P*q.N, original_variables=q.free_size,
        fixed_scalar_metric=dict(identity_sha256=fixed_profile,
            exact_profile_definition=context.deep.definition,
            target_fixed_before_first_direction=True, target_recomputed_from_current_field=False,
            moving_mean_projection=False, all_metric_mean_constraints_retained=True,
            formula='ds^2+a_deep(s)^2*dtheta0^2; fixed parent theta0 chart'),
        representation=q.model, coordinate_norm=coordinates.record,
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
            checkpoint=file_record(args.restart_checkpoint),
            previous_schema=restart['schema'], previous_source_sha256=restart['source_sha256'],
            all_underlying_source_roles_and_four_inputs_preserved=True,
            previous_final_Phi_not_used_as_new_measure_value=True),
        new_unit_meridian_seed_changes_physical_field=restart is None,
        radial_metric_error_identically_zero=False,
        radial_Gram_uses_complete_hprime_Delta=True,
        old_continuous_geometry_certificates_inherited=False,
        old_metric_acceptance_inherited=False,
        new_geometry_and_metric_reread_before_any_acceptance=True,
        maximum_requested_metric_directions=args.directions,
        maximum_requested_restoration_directions=args.restoration_directions,
        maxiter=args.maxiter, initial_damping=args.damping,
        restoration_damping=args.restoration_damping,
        restoration_maxiter=args.restoration_maxiter,
        restoration_interior_margin=args.restoration_interior_margin,
        restoration_interior_margin_is_only_a_stricter_search_target=True,
        original_physical_g_and_nonlinear_acceptance_unchanged=True,
        initial_zero_feasibility_not_assumed=True,
        common_slack_residual_never_called_geometric_feasibility=True,
        target=args.target, target_is_not_README_original_solver_floor=True,
        metric_directions=[], restoration_directions=[],
        continuous_metric_certified=False, continuous_geometry_certified=False,
        closed_isometry_accepted=False,
        working_evaluation=dict(integration_order=args.integration_order,
            inverse_root_iterations=args.inverse_root_iterations,
            inverse_root_tolerance=args.inverse_root_tolerance, angle_block=args.angle_block,
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
            full_metric_mean_and_cross_rows_retained=True, domain=q.domain(point))

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
    native = q.residual(x)
    current = statistics(x, native)
    geometry = scan(x)
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
            relaxed = CommonSlackRows(C, bounds, rows,
                interior_margin=args.restoration_interior_margin)
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
        exact_tail_context_final=context.metadata(),
        limitations='A complete finite new-field solve, not a closed-isometry or reach certificate. Ordinary quadrature, parent normalization, core inverse roots and metric/geometry maxima need continuous same-field error bounds. Core/cap C2 identities are structural in the exact formula and their numerical evaluation errors remain unpaid. Full all-t and E3/held obligations, fixed-problem radial/angular/evaluation refinement and a meaningful solver floor remain. Restored common slack or a budget limit never proves physical feasibility, nonexistence or convergence.')
    save_report()
    event(event='SO3_complete_actual_numerical_budget_returned', report=str(output),
        final_bundle_sha256=sha(final), sample_target_reached=report['sample_target_reached'],
        true_sampled_geometry_feasible=report['final_true_sampled_geometry_feasible'],
        statistics=current, stop_reason=stop_reason)


if __name__ == '__main__':
    main()
