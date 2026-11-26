#!/usr/bin/env python3
"""Freeze ONE full continuous true-material-Haar metric, with moment carriers.

The exact target is the full-circle material integral of one actual
canonical frozen F_star. Quadrature Q and valid moment intervals are
working accuracy only. Current q/core/H may vary in the separate solver;
they never redefine the frozen target or its angular weight.

The fixed wrapper retains every original row and complete J/J* through
positive diagonal scaling. It does not apply a moving mean projection.
Creating this manifest explicitly chooses a NEW target. It is not a
refinement step for a previous physical finite mean or fixed scalar g_n.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import math
import os
import sys

import numpy as np


SCHEMA = 'R691-frozen-true-material-Haar-metric-v1'
MOMENTS_SHA = '1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010'
DEEP_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
BASE_FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
DEEP_FACTORY_SHA = '4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
INPUT_ROLES = ('bundle', 'node_report', 'scalar_input', 'observation_carrier', 'reference_carrier')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual frozen Haar target work belongs only in public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def record(path, repo=None):
    path = Path(path).resolve()
    result = dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
    if repo is not None:
        try:
            result['repo_relative'] = str(path.relative_to(Path(repo).resolve()))
        except ValueError:
            pass
    return result


def load(name, path, expected):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('Changed actual frozen source: '+str(path))
    name = '_frozen_true_Haar_'+name+'_'+expected[:16]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def resolve(value, repo, override=None):
    choices = [Path(override).resolve()] if override is not None else [Path(value['path'])]
    if override is None and value.get('repo_relative'):
        choices.append(Path(repo).resolve()/value['repo_relative'])
    for path in choices:
        if path.is_file() and sha(path) == value['sha256']:
            return path.resolve()
    raise FileNotFoundError('Missing exact recorded bytes for '+value['path'])


def source_from_report(report, role, report_role, repo, override=None):
    """Recover the SAME source bytes after an old source worktree vanished."""
    declared = Path(report['source_paths'][report_role])
    wanted = report['source_sha256_by_role'][report_role]
    choices = [Path(override).resolve()] if override is not None else [declared]
    if override is None:
        parts = declared.parts
        for j in range(len(parts)-1):
            if parts[j:j+2] == ('topics', 'visible-flex-larger-amplitude'):
                choices.append(Path(repo).resolve().joinpath(*parts[j:]))
    for path in choices:
        if path.is_file() and sha(path) == wanted:
            value = record(path, repo)
            value.update(report_source_role=report_role, reported_path=str(declared))
            return value
    raise FileNotFoundError('Need actual recorded source bytes for '+role+' ('+wanted+')')


def mean_definition():
    return dict(averaging='exact full-circle material Haar integral',
        physical_coordinate='phi; dtheta=rho_star(phi)*dphi',
        diagonal_E='integral rho_star*|F_star,s|^2 dphi/(2*pi)',
        diagonal_C='integral |F_star,phi|^2/rho_star dphi/(2*pi)',
        off_diagonal='zero by exact full-circle reflection parity',
        radial_rule='Frozen complete exact-symbolic shared-quintic q plus its SAME canonical analytic f/h/k, at every s',
        angular_rule='Frozen P,Q,ell,b are EXACT integrals; all numeric moments carry complete error',
        target_does_not_depend_on_current_field=True,
        working_quadrature_nodes_not_part_of_metric_definition=True,
        working_moment_midpoints_not_frozen_as_exact_coefficients=True)


def cap_recipe():
    return dict(schema='R661-fixed-p4-graphs-v1', a='3/20',
        radii=['1/25', '9/200', '1/20', '11/200'], height='1/1000',
        upper_centers_xy=[['3/20', '0'], ['0', '3/20'], ['-3/20', '0']],
        lower_centers_xy=[['0', '0']],
        metric_rule='own induced graph metric; height translation independent')


def identity_payload(manifest):
    model = manifest['canonical_model']
    if canonical(model) != manifest['canonical_model_identity_sha256']:
        raise ValueError('The full frozen canonical model identity is inconsistent')
    if canonical(manifest['angular_definition']) != manifest['angular_identity_sha256']:
        raise ValueError('The exact angular definition identity is inconsistent')
    return dict(schema=manifest['schema'],
        canonical_model_identity_sha256=manifest['canonical_model_identity_sha256'],
        angular_identity_sha256=manifest['angular_identity_sha256'],
        inputs={role: manifest['inputs'][role]['sha256'] for role in INPUT_ROLES},
        sources={role: value['sha256'] for role, value in manifest['sources'].items()},
        domain=manifest['domain'], mean_definition=manifest['mean_definition'],
        cap_recipe=manifest['cap_recipe'])


def target_identity(manifest):
    return canonical(identity_payload(manifest))


def read_manifest(path):
    value = json.loads(Path(path).read_text())
    if (value.get('schema') != SCHEMA or value.get('mean_definition') != mean_definition()
            or value.get('cap_recipe') != cap_recipe()
            or value.get('target_identity_sha256') != target_identity(value)
            or value.get('frozen') is not True
            or value.get('exact_material_Haar') is not True
            or value.get('finite_quadrature_is_metric_definition') is not False
            or value['sources']['moments']['sha256'] != MOMENTS_SHA
            or value['sources']['arithmetic']['sha256'] != DEEP_SHA):
        raise ValueError('Need the complete distinct exact material-Haar target manifest')
    model = value['canonical_model']
    schema = model.get('schema')
    if schema == 'R671-exact-reference-tail-lift-v1':
        expected = BASE_FACTORY_SHA
    elif schema == 'deep-valley-fixed-scalar-fullclosed-lift-v1':
        expected = DEEP_FACTORY_SHA
    else:
        raise ValueError('Unsupported frozen physical model')
    if (model.get('source_sha256') != expected or value['sources']['factory']['sha256'] != expected):
        raise ValueError('The actual canonical factory was changed')
    return value


def freeze_actual_report(*, repo, report_path, bundle_path, moments_path,
                         out, moments_source=None, arithmetic_source=None,
                         input_overrides=None, source_overrides=None):
    require_actions()
    repo, report_path, bundle_path = [Path(path).resolve() for path in (repo, report_path, bundle_path)]
    out = Path(out).resolve()
    input_overrides = {} if input_overrides is None else input_overrides
    source_overrides = {} if source_overrides is None else source_overrides
    if set(input_overrides)-set(INPUT_ROLES) or input_overrides.get('bundle') is not None:
        raise ValueError('Declare the actual final bundle with --bundle, and override only its other exact inputs')
    if out.exists():
        raise FileExistsError('Create a new explicit target manifest, never overwrite a prior one')
    report = json.loads(report_path.read_text())
    if report.get('complete') is not True or report.get('final_bundle_sha256') != sha(bundle_path):
        raise ValueError('Freeze the actual final bundle of its real completed scientific report')
    context = report.get('exact_tail_context_final') or report['exact_tail_context']
    model = context['definition']
    if canonical(model) != context['model_identity_sha256']:
        raise ValueError('The actual complete source model is inconsistent')
    with np.load(bundle_path, allow_pickle=False) as z:
        bundle_model = json.loads(str(z['reference_tail_model_json'].item()))
        domain = dict(S_carrier_hex=float(z['mesh'][-1]).hex(),
            R_carrier_hex=float(z['radius']).hex(), width_hex=float(z['width']).hex(),
            fixed_core_first3_hex=[float(value).hex() for value in z['fixed_core_first3']],
            eta_start_affine=model['eta_start_symbolic'], eta_end_affine=model['eta_end_symbolic'])
        profile_carrier_sha = str(z['reference_tail_carrier_sha256'].item())
    if bundle_model != model:
        raise ValueError('The actual frozen bundle is not the report canonical model')
    topic = repo/'topics/visible-flex-larger-amplitude'
    moments_source = Path(moments_source or topic/'scripts/resume_20261126/material_haar_moments.py').resolve()
    arithmetic_source = Path(arithmetic_source or topic/'scripts/resume_20261126/deep_valley_tail_input.py').resolve()
    module = load('accurate_angular_moments', moments_source, MOMENTS_SHA)
    kernel = module.MomentKernel(moments_path, arithmetic_source,
                               expected_bundle_sha256=sha(bundle_path))
    _, _, actual_angular, _ = module.exact_core_input(bundle_path, repo)
    if actual_angular != kernel.raw['definition']:
        raise ValueError('The complete true angular moments describe a different actual core')
    inputs = dict(bundle=bundle_path, node_report=Path(report['exact_tail_node_report']),
        scalar_input=Path(report['exact_tail_scalar_input']),
        observation_carrier=Path(report['observation_carrier']),
        reference_carrier=Path(report['exact_tail_profile_carrier']))
    inputs.update({role: Path(path).resolve() for role, path in input_overrides.items()})
    for role, key in (('node_report', 'node_report_sha256'),
                      ('scalar_input', 'scalar_input_sha256'),
                      ('observation_carrier', 'original_observation_carrier_sha256')):
        if sha(inputs[role]) != model[key]:
            raise ValueError('The frozen actual '+role+' differs from its full model')
    if sha(inputs['reference_carrier']) != profile_carrier_sha:
        raise ValueError('Use the frozen bundle own actual reference carrier')
    source_roles = dict(factory='exact_tail', operator='operator', observed='implementation',
                        batch='base_batch', scalar='tail_scalar', integer='tail_integer', hold='tail_hold')
    if model['schema'] == 'deep-valley-fixed-scalar-fullclosed-lift-v1':
        source_roles.update(base_factory='base_tail', deep_scalar='deep_scalar')
    if set(source_overrides)-set(source_roles):
        raise ValueError('Override only named actual physical source roles')
    sources = dict(evaluator=record(__file__, repo), moments=record(moments_source, repo),
                   arithmetic=record(arithmetic_source, repo))
    for role, key in source_roles.items():
        sources[role] = source_from_report(report, role, key, repo, source_overrides.get(role))
    for key, role in (('scalar_source', 'scalar'), ('integer_source', 'integer'),
                      ('hold_source', 'hold'), ('observed_source', 'observed')):
        if model['source_sha256s'][key] != sources[role]['sha256']:
            raise ValueError('Frozen scalar/observation source differs: '+key)
    for key, role in (('dense', 'operator'), ('batch', 'batch'), ('observed', 'observed')):
        if model['operator_source_sha256s'][key] != sources[role]['sha256']:
            raise ValueError('Frozen actual full operator source differs: '+key)
    value = dict(schema=SCHEMA, frozen=True, exact_material_Haar=True,
        inputs={role: record(path, repo) for role, path in inputs.items()}, sources=sources,
        canonical_model=model, canonical_model_identity_sha256=canonical(model),
        angular_definition=kernel.raw['definition'],
        angular_identity_sha256=kernel.raw['angular_identity_sha256'],
        domain=domain, mean_definition=mean_definition(), cap_recipe=cap_recipe(),
        working_moments=record(moments_path),
        working_accuracy_scope='Moment carrier and Q/p are replaceable valid approximations to THIS same exact integral; excluded from target identity',
        provenance=dict(actual_final_report=record(report_path), parent_report_schema=report.get('schema'),
            parent_declared_target=report.get('fixed_scalar_metric', report.get('mean_metric_design')),
            source_commit=report.get('source_commit'), actual_run_id=report.get('github_run_id'),
            frozen_bundle_sha256=sha(bundle_path)),
        explicit_new_target_choice=True, parent_objective_or_target_preserved=False,
        old_finite_physical_or_fixed_scalar_refinement_claimed=False,
        finite_quadrature_is_metric_definition=False, target_certified=False,
        exact_nonradial_solution_existence_certified=False, continuous_metric_error_certified=False,
        geometry_certified=False, fixed_g_refinement_evidence=False, topic_complete=False)
    value['target_identity_sha256'] = target_identity(value)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    return value


class FrozenHaarTarget:
    """One exact full continuous frozen metric, evaluated by moment carriers."""
    def __init__(self, manifest_path, *, repo, input_overrides=None,
                 source_overrides=None, moment_carrier=None, stage_block=64,
                 scalar_admission_seconds=300, scalar_integral_tolerance='1e-18',
                 scalar_tail_cutoff='1/8'):
        require_actions()
        self.repo = Path(repo).resolve()
        self.manifest_path = Path(manifest_path).resolve()
        self.manifest = read_manifest(self.manifest_path)
        self.manifest_sha256 = sha(self.manifest_path)
        self.identity = self.manifest['target_identity_sha256']
        self.averaging = 'exact-material-Haar'
        self.full_angles = None
        input_overrides = {} if input_overrides is None else input_overrides
        source_overrides = {} if source_overrides is None else source_overrides
        self.inputs = {role: resolve(value, self.repo, input_overrides.get(role))
                       for role, value in self.manifest['inputs'].items()}
        self.sources = {role: resolve(value, self.repo, source_overrides.get(role))
                        for role, value in self.manifest['sources'].items()}
        if self.manifest['sources']['evaluator']['sha256'] != sha(__file__):
            raise ValueError('The exact frozen evaluator source identity changed')
        self.moments_module = load('moments', self.sources['moments'], MOMENTS_SHA)
        selected = (resolve(self.manifest['working_moments'], self.repo)
                    if moment_carrier is None else Path(moment_carrier).resolve())
        self.moments = self.moments_module.MomentKernel(selected, self.sources['arithmetic'],
            expected_bundle_sha256=sha(self.inputs['bundle']))
        if (self.moments.raw['angular_identity_sha256'] != self.manifest['angular_identity_sha256']
                or self.moments.raw['definition'] != self.manifest['angular_definition']):
            raise ValueError('Improved working moments must enclose the SAME frozen angular integrals')
        self.working_moment_carrier = record(selected)
        self.working_moment_full_angles = self.moments.raw['quadrature_work']['full_angles']
        model = self.manifest['canonical_model']
        self.factory = load('physical_factory', self.sources['factory'], model['source_sha256'])
        extra = {}
        if model['schema'] == 'deep-valley-fixed-scalar-fullclosed-lift-v1':
            extra = dict(base_factory_source=self.sources['base_factory'],
                deep_scalar_source=self.sources['deep_scalar'],
                scalar_admission_seconds=scalar_admission_seconds,
                scalar_integral_tolerance=scalar_integral_tolerance,
                scalar_tail_cutoff=scalar_tail_cutoff)
        self.context = self.factory.TailLiftContext.from_files(
            bundle=self.inputs['bundle'], carrier=self.inputs['observation_carrier'],
            node_report=self.inputs['node_report'], scalar_input=self.inputs['scalar_input'],
            scalar_source=self.sources['scalar'], integer_source=self.sources['integer'],
            hold_source=self.sources['hold'], observed_source=self.sources['observed'],
            eta_start_node=model['eta_start_node'], lambda_value=model['lambda_value'], **extra)
        structural_N = 1
        while structural_N <= 4*model['M']:
            structural_N *= 2
        self.structural_full_angles = structural_N
        self.problem, _ = self.context.create_pair(self.sources['operator'], self.sources['batch'],
            N=structural_N, stage_block=stage_block, quarter=True)
        self.x, _ = self.problem.pack(self.context.data['qjets'], float(self.context.data['Hcap']), require_affine=True)
        self.x, _ = self.context.transfer_seed(self.problem, self.x,
            source_lambda=model['lambda_value'], mode='keep-q')
        if self.context.definition() != model:
            raise ValueError('Rebuilt frozen physical formula differs from its literal model')
        self._compatible(self.problem)
        self.x.setflags(write=False)
        self.prepared = self.problem.prepare(self.x)
        actual_core = [float(value).hex() for value in self.context.data['qjets'][0, 0, 1:self.problem.M+1]]
        if actual_core != self.manifest['angular_definition']['original_core_binary64_hex']:
            raise ValueError('The frozen full field and exact moment core differ')
        with np.load(self.inputs['bundle'], allow_pickle=False) as z:
            if str(z['reference_tail_carrier_sha256'].item()) != sha(self.inputs['reference_carrier']):
                raise ValueError('The complete frozen field needs its own exact saved scalar carrier')
        with np.load(self.inputs['reference_carrier'], allow_pickle=False) as z:
            if (json.loads(str(z['model_definition_json'].item())) != model
                    or not np.array_equal(z['mesh'], self.context.mesh)
                    or z['lift_scalar9'].shape != (len(z['observation_cells']), 9)):
                raise ValueError('Frozen saved scalar profiles are not from the exact same field')
            profiles = np.array(z['lift_scalar9'], copy=True)
            if not np.isfinite(profiles).all():
                raise ValueError('Frozen numerical profiles must be finite')
            self._known_profiles = {(int(cell), float(u).hex()): profiles[j]
                for j, (cell, u) in enumerate(zip(z['observation_cells'], z['observation_u']))}
        self.last_materialization = None

    def _compatible(self, current):
        context = current.reference_tail_context
        wanted, model = self.manifest['canonical_model'], context.definition()
        for key in ('schema', 'source_sha256', 'lambda_value', 'eta_start_symbolic', 'eta_end_symbolic',
                    'scalar_input_sha256', 'source_sha256s', 'operator_source_sha256s'):
            if model.get(key) != wanted.get(key):
                raise ValueError('Current field changes the frozen profile/source/physical eta: '+key)
        if wanted['schema'] == 'deep-valley-fixed-scalar-fullclosed-lift-v1':
            for key in ('profile_identity_sha256', 'profile_definition', 'deep_scalar_source_sha256',
                        'base_reference_factory_source_sha256'):
                if model.get(key) != wanted.get(key):
                    raise ValueError('Current field changed the same exact deep scalar: '+key)
        domain = self.manifest['domain']
        if (float(current.S).hex() != domain['S_carrier_hex']
                or float(current.R).hex() != domain['R_carrier_hex']
                or float(current.width).hex() != domain['width_hex']
                or [float(value).hex() for value in context.data['fixed_core_first3']]
                   != domain['fixed_core_first3_hex']):
            raise ValueError('Current field changes fixed S/R/width/core datum')
        return context

    @staticmethod
    def _affine_parameter(point, left, right):
        diff = (right[0]-left[0], right[1]-left[1])
        index = 0 if diff[0] else 1
        if not diff[index]:
            raise ValueError('Coincident exact symbolic frozen endpoints')
        u = (point[index]-left[index])/diff[index]
        if any(point[k]-left[k] != u*diff[k] for k in (0, 1)) or not 0 <= u <= 1:
            raise ValueError('Use a genuine exact nested refinement of the frozen radial grid')
        return u

    def locations_for_operator(self, current):
        context = self._compatible(current)
        intervals = []
        for j, (left, right) in enumerate(zip(context.nodes[:-1], context.nodes[1:])):
            midpoint = float(current.mesh[j]+(current.mesh[j+1]-current.mesh[j])/2)
            cell = min(len(self.context.nodes)-2, max(0,
                int(np.searchsorted(self.context.mesh, midpoint, side='right')-1)))
            a, b = self.context.nodes[cell:cell+2]
            lo, hi = self._affine_parameter(left, a, b), self._affine_parameter(right, a, b)
            if not lo < hi:
                raise ValueError('The actual nested radial orientation changed')
            intervals.append((cell, lo, hi))
        cells = np.empty(current.P, dtype=np.int64)
        local = np.empty(current.P, dtype=float)
        maximum_error, count = F(0), 0
        for stage, (newcell, u) in enumerate(zip(current.observation_cells, current.observation_u)):
            cell, lo, hi = intervals[int(newcell)]
            exact = lo+(hi-lo)*F(float(u))
            value = float(exact)
            fee = abs(F(value)-exact)
            maximum_error = max(maximum_error, fee)
            count += bool(fee)
            cells[stage], local[stage] = cell, value
        return cells, local, dict(current_rows=int(current.P),
            exact_nested_symbolic_cell_mapping=True, rounded_local_coordinate_count=count,
            maximum_local_u_rounding_error_exact=str(maximum_error),
            numerical_materialization_outward=False,
            frozen_mean_arrays_interpolated=False,
            exact_full_circle_target_replaced_by_current_grid=False)

    def evaluate_locations(self, cells, local, *, stage_block=64):
        require_actions()
        cells, local = np.asarray(cells, dtype=np.int64), np.asarray(local, dtype=float)
        q, prepared = self.problem, self.prepared
        if (cells.ndim != 1 or cells.shape != local.shape or stage_block < 1
                or np.any(cells < 0) or np.any(cells >= q.J-1)
                or not np.isfinite(local).all() or np.any(local < 0) or np.any(local > 1)):
            raise ValueError('Use actual frozen cells/local coordinates and a positive block')
        E, C = np.empty(len(cells)), np.empty(len(cells))
        for start in range(0, len(cells), int(stage_block)):
            stop = min(len(cells), start+int(stage_block))
            y, v = np.empty((stop-start, q.n)), np.empty((stop-start, q.n))
            lift = np.empty((stop-start, 9))
            for j, (cell, u) in enumerate(zip(cells[start:stop], local[start:stop])):
                width = q.mesh[cell+1]-q.mesh[cell]
                weights = self.context.observed.hermite_weights(width, float(u))
                jets = weights@prepared.jets[cell:cell+2].reshape(6, q.n)
                y[j], v[j] = jets[:2]
                known = self._known_profiles.get((int(cell), float(u).hex()))
                lift[j] = q.lift_at(int(cell), float(u)) if known is None else known
            zs = lift[:, 1]*prepared.height+lift[:, 7]
            E[start:stop], C[start:stop] = self.moments.numerical_means(
                y, v, lift[:, 3], lift[:, 4], zs)
        if not np.isfinite(E).all() or not np.isfinite(C).all() or np.any(E <= 0) or np.any(C <= 0):
            raise ValueError('Frozen true-Haar numerical target positivity is unpaid')
        return E, C

    def evaluate_for_operator(self, current, *, stage_block=64):
        cells, local, detail = self.locations_for_operator(current)
        E, C = self.evaluate_locations(cells, local, stage_block=stage_block)
        detail.update(target_identity_sha256=self.identity,
            target_manifest_sha256=self.manifest_sha256,
            angular_identity_sha256=self.manifest['angular_identity_sha256'],
            working_moment_carrier=self.working_moment_carrier,
            working_moment_full_angles=self.working_moment_full_angles,
            frozen_structural_grid_not_a_mean_quadrature=self.structural_full_angles,
            exact_target='Full continuous material Haar, independent of every working angle grid',
            E_min=float(E.min()), E_max=float(E.max()), C_min=float(C.min()), C_max=float(C.max()),
            frozen_core_and_weight_retained=True,
            current_core_or_angle_grid_changes_target=False,
            numeric_matrix_and_radial_arithmetic_certified=False,
            accurate_coefficient_intervals_available=True,
            full_continuous_target_positivity_or_metric_error_certified=False)
        self.last_materialization = detail
        return E, C, detail


class FixedHaarTransform:
    """Complete fixed-target relative Gram conversion, without mean projection."""
    def __init__(self, raw, radial, angular):
        self.raw = np.asarray(raw)
        self.radial, self.angular = np.asarray(radial), np.asarray(angular)
        if (self.raw.ndim != 3 or self.raw.shape[-1] != 3
                or self.radial.shape != self.raw.shape[:1] or self.angular.shape != self.radial.shape):
            raise ValueError('Use all complete current rows and one fixed diagonal per radial point')
        self.scale = np.stack((1/self.radial, 1/np.sqrt(self.radial*self.angular),
                               1/self.angular), axis=-1)
        self.result = self.raw*self.scale[:, None, :]
        self.result[..., 0] += 1/self.radial[:, None]-1
        self.result[..., 2] += 1/self.angular[:, None]-1


class FrozenHaarOperator:
    """All original J/J* followed by the SAME immutable diagonal row scaling."""
    def __init__(self, original_operator, target, *, stage_block=64):
        require_actions()
        self.original_operator, self.target = original_operator, target
        self.averaging = target.averaging
        E, C, self.target_materialization = target.evaluate_for_operator(
            original_operator, stage_block=stage_block)
        self.fixed_radial, self.fixed_angular = E, C/original_operator.a**2
        if (not np.isfinite(self.fixed_radial).all() or not np.isfinite(self.fixed_angular).all()
                or np.any(self.fixed_radial <= 0) or np.any(self.fixed_angular <= 0)):
            raise ValueError('Fixed true-Haar target needs positive finite working diagonals')
        self.fixed_scale = np.stack((1/self.fixed_radial,
            1/np.sqrt(self.fixed_radial*self.fixed_angular), 1/self.fixed_angular), axis=-1)
        for value in (self.fixed_radial, self.fixed_angular, self.fixed_scale):
            value.setflags(write=False)
        self._base_x = self._base_state = None

    def __getattr__(self, name):
        return getattr(self.original_operator, name)

    def _state(self, x):
        x = np.asarray(x)
        if (self._base_x is not None and x.shape == self._base_x.shape
                and x.dtype == self._base_x.dtype and np.array_equal(x, self._base_x)):
            return self._base_state
        return FixedHaarTransform(self.original_operator.raw_residual(x),
                                  self.fixed_radial, self.fixed_angular)

    def set_base(self, x):
        detail = self.original_operator.set_base(x)
        self._base_x = np.array(x, copy=True)
        self._base_x.setflags(write=False)
        self._base_state = FixedHaarTransform(self.original_operator.raw_residual(x),
                                              self.fixed_radial, self.fixed_angular)
        return dict(detail, fixed_target_identity=self.target.identity,
            exact_target_kind='true-material-Haar', moving_mean_projection=False,
            fixed_final_metric=True, all_original_mean_constraints_retained=True)

    def clear_base(self):
        self.original_operator.clear_base()
        self._base_x = self._base_state = None

    def raw_residual(self, x):
        return self._state(x).result.copy()

    def residual(self, x):
        return self.raw_residual(x)*self.sqrt_multiplicity[None, :, None]

    def jvp(self, x, direction):
        return self.original_operator.jvp(x, direction)*self.fixed_scale[:, None, :]

    def vjp(self, x, weights):
        weights = np.asarray(weights).reshape(self.P, self.N, 3)
        return self.original_operator.vjp(x, weights*self.fixed_scale[:, None, :])

    def observation_metadata(self):
        return dict(self.original_operator.observation_metadata(),
            fixed_target_identity=self.target.identity, exact_target_kind='true-material-Haar',
            working_moment_full_angles=self.target.working_moment_full_angles,
            current_full_angles=self.full_N, fixed_final_metric=True,
            moving_mean_projection=False, target_materialization=self.target_materialization,
            all_original_mean_constraints_retained=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'report', 'bundle', 'moments', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--moments-source', type=Path)
    parser.add_argument('--arithmetic-source', type=Path)
    parser.add_argument('--input-overrides', type=Path,
        help='JSON role:path mapping to the SAME exact non-bundle input bytes')
    parser.add_argument('--source-overrides', type=Path,
        help='JSON physical role:path mapping to the SAME exact reported source bytes')
    args = parser.parse_args()
    value = freeze_actual_report(repo=args.repo, report_path=args.report, bundle_path=args.bundle,
        moments_path=args.moments, out=args.out, moments_source=args.moments_source,
        arithmetic_source=args.arithmetic_source,
        input_overrides=None if args.input_overrides is None else json.loads(args.input_overrides.read_text()),
        source_overrides=None if args.source_overrides is None else json.loads(args.source_overrides.read_text()))
    print(json.dumps(dict(schema=SCHEMA, target_identity_sha256=value['target_identity_sha256'],
        angular_identity_sha256=value['angular_identity_sha256'], manifest_sha256=sha(args.out),
        exact_material_Haar=True, frozen=True, exact_solution_certified=False,
        fixed_g_refinement_evidence=False, topic_complete=False)), flush=True)
