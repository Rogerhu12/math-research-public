#!/usr/bin/env python3
"""Complete continuous Gram bounds against ONE exact material-Haar target.

The frozen target is the full continuous integral, not a finite angular
rule or the midpoint of an approximate moment vector. Complete outward
R691 moment matrices are contracted with exact shared-quintic Bernstein
controls before radial hulls. R689/R674 retain the current field's complete
Fourier and analytic angular lift, exact common-square cancellation and
normalization fees. Every scientific call is restricted to public Actions.

This first independent consumer binds R671 lambda-one physics on both
sides, including true mesh/M refinement with the same scalar, eta and
width. It does not relabel a deep model as the old interval reader.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


SCHEMA = 'R691-frozen-accurate-Haar-continuous-Gram-v1'
TASK_SCHEMA = 'R691-frozen-accurate-Haar-continuous-Gram-piece-v1'
SUPPORT_SHA = '4552c2eafebb98b732d5ab7717b1b72665680a839b18a51c34c08f718f69381f'
KERNEL_SHA = 'fd4cd58045e16a969c8c1be48468ab4c1a7be929ef9b95e2a9a24ca546176b2d'
PROFILE_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
TARGET_SHA = 'c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64'
MOMENTS_SHA = '1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010'
ARITHMETIC_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
README_TARGET = F(1, 1000000)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('Complete continuous scientific bounds belong in the public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def identity(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def load(path, expected, role):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('Changed complete published '+role+' source')
    name = '_accurate_Haar_interval_'+role+'_'+expected[:16]
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


def target_contract(repo, manifest_path, moments_path=None, input_overrides=None,
                    source_overrides=None):
    """Read actual manifest/bytes; do not materialize a numeric frozen field."""
    require_actions()
    source = Path(repo).resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    evaluator = load(source/'frozen_material_haar_metric.py', TARGET_SHA, 'target')
    manifest = evaluator.read_manifest(manifest_path)
    model = manifest['canonical_model']
    if (model.get('schema') != 'R671-exact-reference-tail-lift-v1'
            or model.get('source_sha256') != FACTORY_SHA or model.get('lambda_value') != 1):
        raise ValueError('This independent complete interval chain uses actual R671 lambda-one physics')
    input_roles = {'bundle', 'node_report', 'scalar_input', 'observation_carrier', 'reference_carrier'}
    source_roles = {'evaluator', 'moments', 'arithmetic', 'factory', 'operator',
                    'observed', 'batch', 'scalar', 'integer', 'hold'}
    if set(manifest['inputs']) != input_roles or set(manifest['sources']) != source_roles:
        raise ValueError('Need every exact Haar target input and actual physical source role')
    input_overrides = {} if input_overrides is None else input_overrides
    source_overrides = {} if source_overrides is None else source_overrides
    if set(input_overrides)-input_roles or set(source_overrides)-source_roles:
        raise ValueError('Unknown same-byte target override role')
    resolved_inputs = {role: evaluator.resolve(record, repo, input_overrides.get(role))
        for role, record in manifest['inputs'].items()}
    resolved_sources = {role: evaluator.resolve(record, repo, source_overrides.get(role))
        for role, record in manifest['sources'].items()}
    expected = dict(evaluator=TARGET_SHA, moments=MOMENTS_SHA, arithmetic=ARITHMETIC_SHA,
        factory=FACTORY_SHA, operator=model['operator_source_sha256s']['dense'],
        batch=model['operator_source_sha256s']['batch'],
        observed=model['operator_source_sha256s']['observed'],
        scalar=model['source_sha256s']['scalar_source'],
        integer=model['source_sha256s']['integer_source'],
        hold=model['source_sha256s']['hold_source'])
    for role, wanted in expected.items():
        if manifest['sources'][role]['sha256'] != wanted:
            raise ValueError('Frozen accurate target source is not its full canonical source: '+role)
    for role, key in (
            ('node_report', 'node_report_sha256'), ('scalar_input', 'scalar_input_sha256'),
            ('observation_carrier', 'original_observation_carrier_sha256')):
        if manifest['inputs'][role]['sha256'] != model[key]:
            raise ValueError('Frozen actual input disagrees with the canonical model: '+role)
    with np.load(resolved_inputs['bundle'], allow_pickle=False) as raw:
        if (json.loads(str(raw['reference_tail_model_json'].item())) != model
                or str(raw['reference_tail_carrier_sha256'].item())
                   != manifest['inputs']['reference_carrier']['sha256']):
            raise ValueError('Use the actual frozen bundle and its own reference carrier')
    selected = (Path(moments_path).resolve() if moments_path is not None
        else evaluator.resolve(manifest['working_moments'], repo))
    module = load(resolved_sources['moments'], MOMENTS_SHA, 'moments')
    moments = module.MomentKernel(selected, resolved_sources['arithmetic'],
        expected_bundle_sha256=manifest['inputs']['bundle']['sha256'])
    if (moments.raw['angular_identity_sha256'] != manifest['angular_identity_sha256']
            or moments.raw['definition'] != manifest['angular_definition']):
        raise ValueError('Do not substitute another frozen core or a finite angular target')
    return dict(manifest=manifest, manifest_record=identity(manifest_path),
        inputs=resolved_inputs, sources=resolved_sources,
        moments=moments, moment_module=module, moment_record=identity(selected))


def make_reader(*, repo, current_arguments, contract, angles=8192,
                scalar_degree=5, panels=128):
    require_actions()
    repo = Path(repo).resolve()
    path = repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/frozen_mean_metric_interval.py'
    support = load(path, SUPPORT_SHA, 'R689_support')

    class FrozenHaarGram(support.FrozenMeanGram):
        def __init__(self):
            # The inherited finite-target constructor is deliberately NOT
            # called. Only its exact common-domain/current-Gram operations
            # and their independently proved normalization are reused.
            self.repo = repo
            self.kernel, self.kernel_path = support.load_kernel(repo)
            self.angles = support.positive_dyadic(angles, 'Continuous current angle cover')
            self.scalar_degree, self.panels = int(scalar_degree), int(panels)
            if not 3 <= self.scalar_degree <= 8 or self.panels < 1:
                raise ValueError('Use the complete supported scalar Taylor degree and positive panels')
            self.frozen_angles = None
            self.contract, self.moments = contract, contract['moments']
            self.manifest = contract['manifest']
            self.frozen_identity = self.manifest['target_identity_sha256']
            clean = {key: Path(value).resolve() for key, value in current_arguments.items()
                     if value is not None}
            allowed = {'bundle', 'node_report', 'scalar_input', 'reference_carrier'}
            if set(clean)-allowed or not {'bundle', 'node_report', 'scalar_input'} <= set(clean):
                raise ValueError('Need all actual current field/scalar/node inputs')
            target_args = {key: contract['inputs'][key] for key in allowed}
            self.arguments = dict(current=clean, target=target_args)
            if sha(clean['scalar_input']) != self.manifest['inputs']['scalar_input']['sha256']:
                raise ValueError('Current and frozen field must use the same exact scalar')
            self.current = self.kernel.make_reader(repo=repo, **clean, angles=self.angles,
                radial_subdivisions=1, scalar_degree=self.scalar_degree, panels=self.panels)
            frozen_M = int(self.manifest['canonical_model']['M'])
            self.target_evaluation_angles = 256
            while self.target_evaluation_angles < 12*frozen_M:
                self.target_evaluation_angles *= 2
            self.target = self.kernel.make_reader(repo=repo, **target_args,
                angles=self.target_evaluation_angles, radial_subdivisions=1,
                scalar_degree=self.scalar_degree, panels=self.panels)
            self.I = self.current.I
            for reader in (self.current, self.target):
                if (reader.profile.model.get('schema') != 'R671-exact-reference-tail-lift-v1'
                        or reader.profile.model.get('source_sha256') != FACTORY_SHA
                        or reader.profile.model.get('lambda_value') != 1):
                    raise ValueError('Do not pass another canonical scalar model into the R674 interval kernel')
            self._validate_common_definition()
            self._validate_frozen_manifest()
            self._target_q_cache = None
            self._coefficient_blocks = self._blocks()
            self.joint = self._intersection()
            self.binding = dict(
                current_inputs={key: identity(value) for key, value in clean.items()},
                frozen_inputs={key: identity(value) for key, value in contract['inputs'].items()},
                current_model_identity_sha256=self.current.profile.model_sha,
                frozen_model_identity_sha256=self.target.profile.model_sha,
                frozen_metric_identity=self.frozen_identity,
                angular_identity_sha256=self.manifest['angular_identity_sha256'],
                frozen_averaging='exact-material-Haar', frozen_full_angles=None,
                working_moment_carrier=contract['moment_record'],
                working_moment_full_angles=self.moments.raw['quadrature_work']['full_angles'],
                working_moment_derivative_order=self.moments.raw['quadrature_work']['derivative_order'],
                target_rho_cover_angles=self.target_evaluation_angles,
                target_rho_cover_is_a_metric_quadrature_rule=False,
                current_M=self.current.r.M, frozen_M=self.target.r.M,
                current_J=self.current.r.J, frozen_J=self.target.r.J,
                same_exact_f_lambda=True,
                common_scalar_input_sha256=sha(clean['scalar_input']),
                current_global_rho_lower=float(self.current.r.rho[0].min()),
                frozen_global_rho_lower=float(self.target.r.rho[0].min()),
                common_lift_definition=dict(lambda_value=self.current.profile.model['lambda_value'],
                    eta_start_symbolic=support.endpoint_symbolic(self.current.profile.eta_left),
                    eta_end_symbolic=support.endpoint_symbolic(self.current.profile.eta_right),
                    width_exact=str(self.current.r.width)),
                complete_source_hashes=dict(consumer=sha(__file__), R689_support=SUPPORT_SHA,
                    R674_current_Gram=KERNEL_SHA, R671_interval=PROFILE_SHA,
                    frozen_evaluator=TARGET_SHA, accurate_moments=MOMENTS_SHA,
                    integer_arithmetic=ARITHMETIC_SHA, physical_factory=FACTORY_SHA),
                frozen_actual_sources={key: identity(value) for key, value in contract['sources'].items()},
                target_moment_error_in_all_coefficient_intervals=True,
                working_moment_midpoints_used_for_certificate=False)

        def _validate_frozen_manifest(self):
            reader = self.target
            if (self.manifest['canonical_model'] != reader.profile.model
                    or self.manifest['canonical_model_identity_sha256'] != reader.profile.model_sha):
                raise ValueError('The actual frozen continuous field differs from its entire target model')
            if (self.moments.M != reader.r.M
                    or [float(v).hex() for v in reader.r.core]
                       != self.manifest['angular_definition']['original_core_binary64_hex']):
                raise ValueError('The full frozen radial field and exact angular moments have different core')
            domain = dict(S_carrier_hex=float(reader.r.mesh[-1]).hex(),
                R_carrier_hex=float(reader.r.radius_carrier).hex(),
                width_hex=float(reader.r.width).hex(),
                fixed_core_first3_hex=[float(v).hex() for v in reader.r.fixed_core],
                eta_start_affine=support.endpoint_symbolic(reader.profile.eta_left),
                eta_end_affine=support.endpoint_symbolic(reader.profile.eta_right))
            if domain != self.manifest['domain']:
                raise ValueError('The actual frozen radial domain differs from the fixed complete target')

        def _blocks(self):
            result = {}
            module, d = self.contract['moment_module'], self.moments.d
            for name, values in self.moments.interval_blocks().items():
                vector = name in ('ellR', 'ellT', 'bZ')
                rows = [values] if vector else values
                endpoints = np.array([[module.interval_float(value, d) for value in row]
                    for row in rows], dtype=float)
                if vector:
                    endpoints = endpoints[0]
                lo, hi = endpoints[..., 0], endpoints[..., 1]
                if not np.isfinite(endpoints).all() or np.any(lo > hi):
                    raise ValueError('The complete integer angular coefficient box is not finite')
                lo.setflags(write=False)
                hi.setflags(write=False)
                result[name] = (lo, hi)
            return result

        def _bilinear(self, x, matrix, y):
            I = self.I
            if x[0].ndim != 1 or y[0].ndim != 1 or matrix[0].shape != (len(x[0]), len(y[0])):
                raise ValueError('Complete moment bilinear dimensions do not match')
            terms = I.mul(I.mul((x[0][:, None], x[1][:, None]), matrix),
                          (y[0][None, :], y[1][None, :]))
            return support.interval_sum(I, support.interval_sum(I, terms))

        def _bilinear_controls(self, x, matrix, y):
            """Exact Bernstein product weights; every scalar sum rounds outward."""
            I, r = self.I, self.target.r
            m, n = len(x[0])-1, len(y[0])-1
            controls = []
            for k in range(m+n+1):
                value = I.exact(0.)
                for i in range(max(0, k-n), min(m, k)+1):
                    j = k-i
                    weight = r.fraction(F(math.comb(m, i)*math.comb(n, j), math.comb(m+n, k)))
                    term = self._bilinear(I.at(x, i), matrix, I.at(y, j))
                    value = I.add(value, I.mul(weight, term))
                controls.append(value)
            return I.stack(controls)

        def _linear_controls(self, x, vector):
            values = self.I.mul(x, (vector[0][None, :], vector[1][None, :]))
            return support.interval_sum(self.I, values)

        def target_polynomials(self, cell, piece, p):
            """Exact Haar mean Bernstein controls, all moment and scalar errors paid."""
            reader, r, I = self.target, self.target.r, self.I
            if self._target_q_cache is None or self._target_q_cache[0] != cell:
                width = r.width_box(r.nodes[cell], r.nodes[cell+1])
                q = r.hermite(I.at(r.jets, cell), I.at(r.jets, cell+1), width)
                self._target_q_cache = cell, (q, r.derivative(q, width))
            q, u = [r.restrict(value, piece[2], piece[3]) for value in self._target_q_cache[1]]
            M = self.moments.M
            slices = {'R': slice(0, M+1), 'T': slice(M+1, 2*M+1), 'Z': slice(2*M+1, None)}
            blocks = self._coefficient_blocks
            select = lambda value, key: I.at(value, (slice(None), slices[key]))
            add = lambda a, b: support.scalar_add(reader, a, b)
            product = reader.profile.product
            E_residual = C_residual = I.exact(np.array([0.]))
            for key, block_P, block_Q in (('R', 'Prr', 'Qrr'), ('T', 'Ptt', 'Qtt'), ('Z', 'Pzz', 'Qzz')):
                uu, qq = select(u, key), select(q, key)
                E_residual = add(E_residual, self._bilinear_controls(uu, blocks[block_P], uu))
                C_residual = add(C_residual, self._bilinear_controls(qq, blocks[block_Q], qq))
            C_residual = add(C_residual, I.scale(self._bilinear_controls(
                select(q, 'R'), blocks['Qrt'], select(q, 'T')), 2))
            lu = add(self._linear_controls(select(u, 'R'), blocks['ellR']),
                     self._linear_controls(select(u, 'T'), blocks['ellT']))
            lq = add(self._linear_controls(select(q, 'R'), blocks['ellR']),
                     self._linear_controls(select(q, 'T'), blocks['ellT']))
            bu = self._linear_controls(select(u, 'Z'), blocks['bZ'])
            f, fs, zs = p['f'][0], p['f'][1], p['z'][1]
            E_residual = add(E_residual, I.scale(product(fs, lu), 2))
            E_residual = add(E_residual, I.scale(product(zs, bu), 2))
            E_residual = add(E_residual, product(zs, zs))
            C_residual = add(C_residual, I.scale(product(f, lq), 2))
            E = add(E_residual, product(fs, fs))
            C = add(C_residual, product(f, f))
            # dmu=rho_star*dphi/(2*pi) is a positive probability measure.
            # The same Cauchy-Schwarz norm perturbation fee is valid for
            # these mean-square norms, with |delta Fs|<=ev and
            # |delta Ftheta|<=ef0. No finite point average is used.
            fees = self.field_fees(reader, p, support.scalar_hull(E), support.scalar_hull(C))
            return dict(E=E, C=C, E_residual=E_residual, C_residual=C_residual,
                E_fee=float(fees[0]), C_fee=float(fees[2]))

        def certify_piece(self, joint_index, radial_index=0, radial_subdivisions=1):
            # The entire R689 exact-common-square/closed-arc/normalization
            # calculation is reused on the NEW true-Haar polynomials.
            row = super().certify_piece(joint_index, radial_index, radial_subdivisions)
            row.pop('frozen_finite_rule_changed', None)
            row.update(exact_full_circle_material_Haar=True,
                fixed_complete_angular_moment_intervals_used=True,
                complete_periodic_integration_tails_paid=True,
                working_moment_midpoints_used_for_certificate=False,
                target_finite_angular_rule_used=False,
                moment_carrier_sha256=self.contract['moment_record']['sha256'],
                angular_identity_sha256=self.manifest['angular_identity_sha256'],
                frozen_metric_identity_sha256=self.frozen_identity,
                frozen_scalar_fee_uses_positive_Haar_L2_Cauchy_Schwarz=True)
            return row

    return FrozenHaarGram(), support


def validate_return(support, row, task, reader, radial):
    support.validate_return(row, task, reader, radial)
    for flag in ('exact_full_circle_material_Haar', 'fixed_complete_angular_moment_intervals_used',
                 'complete_periodic_integration_tails_paid',
                 'frozen_scalar_fee_uses_positive_Haar_L2_Cauchy_Schwarz'):
        if row.get(flag) is not True:
            raise ValueError('Incomplete accurate-Haar scope flag: '+flag)
    if (row.get('working_moment_midpoints_used_for_certificate') is not False
            or row.get('target_finite_angular_rule_used') is not False
            or row.get('moment_carrier_sha256') != reader.contract['moment_record']['sha256']
            or row.get('angular_identity_sha256') != reader.manifest['angular_identity_sha256']
            or row.get('frozen_metric_identity_sha256') != reader.frozen_identity):
        raise ValueError('The exact target or its actual complete working coefficient boxes changed')


def main():
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'node-report', 'scalar-input', 'frozen-target', 'journal', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--reference-carrier', type=Path)
    parser.add_argument('--target-moments', type=Path)
    parser.add_argument('--target-input-overrides', type=Path)
    parser.add_argument('--target-source-overrides', type=Path)
    parser.add_argument('--angles', type=int, default=8192)
    parser.add_argument('--radial-subdivisions', type=int, default=1)
    parser.add_argument('--scalar-degree', type=int, default=5)
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--budget-seconds', type=float, default=600.)
    parser.add_argument('--maximum-new-pieces', type=int, default=64)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    if (not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0
            or args.maximum_new_pieces < 1):
        raise ValueError('Use a positive natural complete-piece admission budget')
    support_path = args.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/frozen_mean_metric_interval.py'
    support = load(support_path, SUPPORT_SHA, 'R689_support')
    radial = support.positive_dyadic(args.radial_subdivisions, 'Radial subdivision count')
    args.journal, args.out = [support.outside(path, args.repo) for path in (args.journal, args.out)]
    if args.out.exists():
        raise FileExistsError('Preserve actual prior summary bytes')
    if args.journal.exists() != args.resume:
        raise ValueError('Use a new journal or explicitly resume the same actual run')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic()
    contract = target_contract(args.repo, args.frozen_target, args.target_moments,
        input_overrides=None if args.target_input_overrides is None else json.loads(args.target_input_overrides.read_text()),
        source_overrides=None if args.target_source_overrides is None else json.loads(args.target_source_overrides.read_text()))
    current = dict(bundle=args.bundle, node_report=args.node_report,
                   scalar_input=args.scalar_input, reference_carrier=args.reference_carrier)
    reader, support = make_reader(repo=args.repo, current_arguments=current, contract=contract,
        angles=args.angles, scalar_degree=args.scalar_degree, panels=args.panels)
    execution = {key: os.environ.get(key) for key in (
        'GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_WORKFLOW', 'GITHUB_SHA')}
    execution['actual_source_commit'] = subprocess.check_output(
        ['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip()
    signature = dict(schema=SCHEMA, producer_sha256=sha(__file__), binding=reader.binding,
        angles=args.angles, radial_subdivisions=radial,
        scalar_degree=args.scalar_degree, panels=args.panels,
        frozen_manifest_sha256=sha(args.frozen_target),
        cap_metric_rule=contract['manifest']['cap_recipe'],
        runner_identity={key: execution[key] for key in (
            'GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT')})
    binding_sha = canonical(signature)
    header = args.journal/'definition.json'
    if args.resume:
        if json.loads(header.read_text()) != signature:
            raise ValueError('Journal is for another actual field, exact target, coefficient box, cover or run')
    else:
        args.journal.mkdir(parents=True)
        support.atomic_json(header, signature)
    tasks = [(piece['index'], sub) for piece in reader.joint for sub in range(radial)]
    task_set = set(tasks)
    returns, failures = {}, {}
    for path in sorted(args.journal.glob('piece-*.json')):
        value = json.loads(path.read_text())
        task = tuple(value.get('task', []))
        if (value.get('schema') != TASK_SCHEMA or value.get('binding_sha256') != binding_sha
                or task not in task_set or task in returns or task in failures):
            raise ValueError('Invalid or duplicate actual same-field interval return')
        if value.get('state') == 'returned':
            validate_return(support, value['record'], task, reader, radial)
            returns[task] = value['record']
        elif value.get('state') == 'failed':
            failures[task] = value
        else:
            raise ValueError('Unknown exact-piece journal state')

    def summary(status, admitted):
        covered, paid, cell_rows = [], [], {}
        required = {cell: [] for cell in range(reader.current.r.J-1)}
        for joint, sub in tasks:
            required[reader.joint[joint]['current_cell']].append((joint, sub))
        for cell, needed in required.items():
            if needed and all(task in returns for task in needed):
                rows = [returns[task] for task in needed]
                upper = max(row['continuous_relative_gram_operator_upper'] for row in rows)
                cell_rows[cell] = dict(upper=upper,
                    lower=max(row['actual_supremum_lower'] for row in rows),
                    E_lower=min(row['minimum_frozen_E_lower'] for row in rows),
                    C_lower=min(row['minimum_frozen_C_lower'] for row in rows))
                covered.append(cell)
                if F(upper) <= README_TARGET:
                    paid.append(cell)
        complete = len(covered) == reader.current.r.J-1
        upper = max((row['upper'] for row in cell_rows.values()), default=None)
        lower = max((row['actual_supremum_lower'] for row in returns.values()), default=None)
        witness = max(returns.values(), key=lambda row: row['actual_supremum_lower']) if returns else None
        compact = None if witness is None else {key: witness[key] for key in (
            'current_cell', 'frozen_cell', 'joint_piece', 'radial_subcell', 'radial_subdivisions',
            'symbolic_left', 'symbolic_right', 'actual_supremum_lower', 'actual_lower_witness')}
        metric = bool(complete and F(upper) <= README_TARGET)
        result = dict(schema=SCHEMA, source_sha256=sha(__file__), execution=execution,
            binding=reader.binding, binding_sha256=binding_sha,
            current_bundle_sha256=reader.binding['current_inputs']['bundle']['sha256'],
            current_node_report_sha256=reader.binding['current_inputs']['node_report']['sha256'],
            frozen_bundle_sha256=reader.binding['frozen_inputs']['bundle']['sha256'],
            frozen_metric_identity_sha256=reader.frozen_identity,
            angular_identity_sha256=reader.manifest['angular_identity_sha256'],
            working_moment_carrier_sha256=contract['moment_record']['sha256'],
            working_moment_full_angles=reader.binding['working_moment_full_angles'],
            working_moment_derivative_order=reader.binding['working_moment_derivative_order'],
            frozen_manifest=contract['manifest_record'],
            cap_metric_rule=contract['manifest']['cap_recipe'],
            angles=args.angles, radial_subdivisions=radial,
            scalar_degree=args.scalar_degree, panels=args.panels,
            expected_current_cells=reader.current.r.J-1, exact_joint_pieces=len(reader.joint),
            expected_piece_tasks=len(tasks), returned_piece_tasks=len(returns), failed_piece_tasks=len(failures),
            admitted_piece_tasks_this_invocation=admitted,
            maximum_new_pieces=args.maximum_new_pieces, admission_seconds=args.budget_seconds,
            status=status, covered_cells_ranges=support.ranges(covered),
            target_paid_cells_ranges=support.ranges(paid),
            covered_cells_count=len(covered), target_paid_cells_count=len(paid),
            covered_relative_gram_operator_upper=upper,
            covered_relative_gram_operator_upper_exact=None if upper is None else str(F(upper)),
            complete_relative_gram_operator_upper=upper if complete else None,
            complete_relative_gram_operator_upper_exact=str(F(upper)) if complete else None,
            covered_actual_supremum_lower=lower,
            returned_point_supremum_lower_exact=None if lower is None else str(F(lower)),
            actual_lower_witness_json=json.dumps(compact, sort_keys=True, separators=(',', ':'), allow_nan=False),
            complete_scope=complete, README_target_exact=str(README_TARGET),
            metric_certified=metric, all_t_metric_certified=metric,
            minimum_covered_frozen_E_lower=min((v['E_lower'] for v in cell_rows.values()), default=None),
            minimum_covered_frozen_C_lower=min((v['C_lower'] for v in cell_rows.values()), default=None),
            actual_candidate_proved_above_target=bool(lower is not None and F(lower) > README_TARGET),
            worst_upper_cells=sorted((dict(cell=cell, **value) for cell, value in cell_rows.items()),
                key=lambda item: item['upper'], reverse=True)[:8],
            failure_types=sorted(set(v['error_type'] for v in failures.values())),
            exact_full_circle_material_Haar=True,
            working_moment_midpoints_used_for_certificate=False,
            target_finite_angular_rule_used=False,
            complete_periodic_angular_integration_tails_paid=True,
            exact_common_lift_squares_cancelled=True,
            both_current_and_frozen_scalar_remainders_paid=True,
            target_inferred_from_current_field=False,
            caps_relative_error_exact='0', reflection_preserves_relative_gram=True,
            phase_scope='R248 conjugacy for the one fixed accurate rotational Haar target and fixed induced cap metrics',
            embedding_certified=False, reach_certified=False,
            fixed_metric_convergence_certified=False, topic_completion_certified=False,
            journal_policy='Actual exact-piece returns remain runner-local; publish source, inputs and compact covered-domain statements',
            seconds=time.monotonic()-started,
            process_peak_rss_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        support.atomic_json(args.out, result)
        return result

    admitted = 0
    summary('ready', admitted)
    for task in tasks:
        if task in returns or task in failures:
            continue
        if admitted and (time.monotonic()-started >= args.budget_seconds
                         or admitted >= args.maximum_new_pieces):
            break
        begin = time.monotonic()
        record = dict(schema=TASK_SCHEMA, binding_sha256=binding_sha, task=list(task))
        try:
            row = reader.certify_piece(*task, radial_subdivisions=radial)
            validate_return(support, row, task, reader, radial)
            record.update(state='returned', record=row)
            returns[task] = row
        except Exception as error:
            record.update(state='failed', error_type=type(error).__name__, error=str(error),
                          mathematical_contribution='No bound on this exact piece')
            failures[task] = record
        record['call_seconds'] = time.monotonic()-begin
        path = args.journal/('piece-'+str(task[0]).zfill(6)+'-'+str(task[1]).zfill(6)+'.json')
        if path.exists():
            raise FileExistsError('Never overwrite a real complete-piece return')
        support.atomic_json(path, record)
        admitted += 1
        value = summary('running', admitted)
        print(json.dumps(dict(event='accurate_Haar_Gram_piece_return', task=list(task),
            state=record['state'], call_seconds=record['call_seconds'],
            covered_cells=value['covered_cells_count'], complete_scope=value['complete_scope'],
            metric_certified=value['metric_certified'])), flush=True)
    status = ('complete' if len(returns) == len(tasks)
              else 'incomplete_with_failed_pieces' if failures else 'natural_complete_piece_budget_return')
    value = summary(status, admitted)
    print(json.dumps(dict(event='accurate_Haar_Gram_batch_return', report_sha256=sha(args.out),
        status=status, complete_scope=value['complete_scope'],
        covered_cells=value['covered_cells_count'], expected_cells=value['expected_current_cells'],
        target_identity=reader.frozen_identity, moment_carrier_sha256=contract['moment_record']['sha256'],
        metric_certified=value['metric_certified'], fixed_metric_convergence_certified=False)), flush=True)


if __name__ == '__main__':
    main()
