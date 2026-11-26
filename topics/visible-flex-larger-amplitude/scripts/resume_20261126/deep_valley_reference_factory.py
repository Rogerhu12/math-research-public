#!/usr/bin/env python3
"""NEW fixed-scalar fullclosed factory for the explicit deep-valley tail.

The target is fixed g_n=ds^2+a_n(s)^2 dtheta^2, not a moving angular mean.
All original q/core/H coordinates and all observation rows remain present.
The original R671 physical/J/J* machinery is reused with NEW complete scalar
profiles and a separate canonical model.  Old field certificates do not move.

The prepare command reads a real original lambda=1 canonical parent, writes
a declared new keep-q seed plus its new scalar/observation carriers, and
migrates only exact witness addresses.  It does not claim a solved direction.
Subsequent from_files calls accept only this new schema.
"""
from fractions import Fraction as Q
from pathlib import Path
from types import MethodType, ModuleType
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
import sys
import time

import numpy as np

SCHEMA = 'deep-valley-fixed-scalar-fullclosed-lift-v1'
BASE_FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
DEEP_SOURCE_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
FULLHOLD_SHA = 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'
INTEGER_SHA = 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'
HOLD_SHA = 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
SCALARS = ('h', 'hs', 'hss', 'f', 'fs', 'fss', 'k', 'ks', 'kss')
REFERENCE = ('a', 'as', 'ass', 'I', 'Is', 'Iss')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific deep-valley fullclosed work belongs only in public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def source_record(value):
    path = Path(value.__file__ if isinstance(value, ModuleType) else value).resolve()
    return dict(path=str(path), sha256=sha(path))


def load(path, expected, role):
    path = Path(path).resolve()
    if expected is not None and sha(path) != expected:
        raise ValueError('Changed byte-bound '+role)
    name = '_new_deep_valley_'+role+'_'+sha(path)[:16]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def dependencies(base_source=None, deep_source=None):
    here = Path(__file__).resolve()
    base_source = (here.parent.parent/'resume_20261120/exact_reference_tail_lift.py'
                   if base_source is None else Path(base_source))
    deep_source = here.with_name('deep_valley_tail_input.py') if deep_source is None else Path(deep_source)
    return (load(base_source, BASE_FACTORY_SHA, 'R671_factory'),
            load(deep_source, DEEP_SOURCE_SHA, 'deep_scalar'))


def _lambda(data):
    values = [float(data[key]) for key in ('reference_tail_lambda', 'exact_tail_lambda') if key in data]
    if not values or any(value != 1. for value in values):
        raise ValueError('This new input retains an explicitly canonical lambda=1 reference lift')
    return 1.


class TailLiftContext:
    """R671-compatible numerical API, with a different fixed exact scalar.

    Delegated methods are the byte-bound R671 complete physical equations;
    scalar identity, construction, carriers, migration and metadata are new.
    Normal continuation never silently converts an old canonical bundle.
    """
    def __getattr__(self, name):
        base = self.__dict__.get('base')
        method = None if base is None else getattr(base.TailLiftContext, name, None)
        if method is None:
            raise AttributeError(name)
        return MethodType(method, self) if callable(method) else method

    @classmethod
    def from_files(cls, *, bundle, carrier, node_report, scalar_input,
                   scalar_source, integer_source, hold_source, observed_source,
                   eta_start_node, lambda_value, panels=128,
                   base_factory_source=None, deep_scalar_source=None,
                   allow_original_parent=False, scalar_admission_seconds=300,
                   scalar_integral_tolerance='1e-18', scalar_tail_cutoff='1/8'):
        require_actions()
        if float(lambda_value) != 1.:
            raise ValueError('The deep-valley first branch fixes lambda=1; it is not a lambda homotopy')
        base, deep_module = dependencies(base_factory_source, deep_scalar_source)
        self = cls()
        self.base, self.deep_module = base, deep_module
        self.paths = {key: Path(value).resolve() for key, value in dict(bundle=bundle,
            carrier=carrier, node_report=node_report, scalar_input=scalar_input,
            scalar_source=scalar_source, integer_source=integer_source,
            hold_source=hold_source, observed_source=observed_source).items()}
        self.input_records = {role: source_record(path) for role, path in self.paths.items()}
        self.original_input_records = dict(self.input_records)
        for role, expected in (('scalar_source', FULLHOLD_SHA),
                               ('integer_source', INTEGER_SHA), ('hold_source', HOLD_SHA)):
            if self.input_records[role]['sha256'] != expected:
                raise ValueError('Changed complete original '+role)
        with np.load(self.paths['bundle'], allow_pickle=False) as data:
            self.data = {key: np.array(data[key], copy=True) for key in data.files}
        with np.load(self.paths['carrier'], allow_pickle=False) as data:
            self._input_carrier_arrays = {key: np.array(data[key], copy=True) for key in data.files}
        self.observed = base.load(self.paths['observed_source'], 'observed')
        self.plan = self.observed.ObservationPlan.from_arrays(self._input_carrier_arrays)
        for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
            if not np.array_equal(self.data[key], self._input_carrier_arrays[key]):
                raise ValueError('Bundle/carrier disagree on the actual '+key)
        _lambda(self.data)
        if 'reference_tail_model_json' not in self.data:
            raise ValueError('A real canonical source model is required')
        self._prior_definition = json.loads(str(self.data['reference_tail_model_json'].item()))
        self._original_migration = self._prior_definition.get('schema') == base.SCHEMA
        if self._original_migration and not allow_original_parent:
            raise ValueError('Use the explicit prepare command before this new fixed-scalar solve')
        if not self._original_migration and self._prior_definition.get('schema') != SCHEMA:
            raise ValueError('Unknown source model; no implicit profile-to-profile migration')
        if self._prior_definition.get('lambda_value') != 1.:
            raise ValueError('The actual canonical source lambda must equal one')
        self._source_parent_definition = self._prior_definition
        self._source_parent_model_identity = canonical_sha(self._prior_definition)
        self.mesh = np.array(self.data['mesh'], copy=True)
        self.S, self.radius = float(self.mesh[-1]), float(self.data['radius'])
        self.width = float(self.data['width'])
        self.M = (self.data['qjets'].shape[-1]-2)//3
        self.lambda_value, self.eta_start_node = 1., int(eta_start_node)
        report = json.loads(self.paths['node_report'].read_text())
        self._input_node_report = report
        if report['input_sha256'] != self.input_records['scalar_input']['sha256']:
            raise ValueError('The original scalar data do not match the symbolic node report')
        self.nodes = [(Q(row['S_coefficient']), Q(row['constant']))
                      for row in report['true_scalar_nodes']]
        matches = [j for j, node in enumerate(self.nodes) if node == (Q(1), -Q(self.width))]
        if len(matches) != 1:
            raise ValueError('Keep the actual unique exact S-width eta endpoint')
        self.eta_end_node = matches[0]
        if (len(self.nodes) != len(self.mesh)
                or self.plan.legacy_count != 2*len(self.mesh)-1
                or self.plan.lift_break_node != self.eta_end_node
                or not 0 < self.eta_start_node < self.eta_end_node < len(self.mesh)-1
                or float(report['S_carrier']) != self.S
                or float(report['radius_carrier']) != self.radius):
            raise ValueError('Changed current carrier layout or eta node identity')
        self.eta_left = float(self.mesh[self.eta_start_node])
        self.eta_right = float(self.mesh[self.eta_end_node])
        raw = self.paths['scalar_input'].read_bytes()
        scalar_data = json.loads(gzip.decompress(raw) if self.paths['scalar_input'].suffix == '.gz' else raw)
        scalar_module = base.load(self.paths['scalar_source'], 'fullhold')
        self.full = scalar_module.FullHold(scalar_data, self.paths['integer_source'],
                                          self.paths['hold_source'], panels=int(panels))
        if self.full.carrier(self.full.S) != self.S:
            raise ValueError('The new tail keeps the SAME original exact S and its carrier')
        if Q(self.width) <= self.full.out:
            raise ValueError('The existing eta=1 endpoint must precede the entire out ramp')
        left_box = self.full.affine_time(*self.nodes[self.eta_start_node])
        if Q(left_box[0], self.full.h.S) <= self.full.cut:
            raise ValueError('The original eta start remains strictly inside Hold')
        scalar_identity = {key: self.input_records[key]['sha256'] for key in
                           ('scalar_input', 'scalar_source', 'integer_source', 'hold_source')}
        self.deep = deep_module.DeepValleyTail(self.full, input_identity=scalar_identity,
            epsilon=Q(scalar_tail_cutoff), integral_tolerance=Q(scalar_integral_tolerance),
            admission_seconds=float(scalar_admission_seconds))
        self._scalar_working = dict(panels=int(panels), tail_cutoff=str(Q(scalar_tail_cutoff)),
            integral_tolerance=str(Q(scalar_integral_tolerance)),
            scalar_admission_seconds=float(scalar_admission_seconds))
        self.a_observations = np.array(self._input_carrier_arrays['a_observations'], copy=True)
        if self.a_observations.shape != (len(self.plan.cells),):
            raise ValueError('One actual a carrier is required at every original and added row')
        self._reference_cache, self._point_profiles = {}, {}
        self._old_profiles = self._profiles = None
        self._reference_values = self._reference_errors = self._reference_active = None
        self._operator_sources = {}
        self._carrier_output = None
        self._maximum_reference_errors = np.zeros(6)
        self._node_indices = {float(value): j for j, value in enumerate(self.mesh)}
        self._new_input_outputs = None
        self._original_context = None
        if self._original_migration:
            # This is only a source-model validation object.  Its q/H is not
            # evaluated as if it were the new scalar, and it produces no parent.
            self._original_context = base.TailLiftContext.from_files(bundle=bundle,
                carrier=carrier, node_report=node_report, scalar_input=scalar_input,
                scalar_source=scalar_source, integer_source=integer_source,
                hold_source=hold_source, observed_source=observed_source,
                eta_start_node=eta_start_node, lambda_value=1., panels=int(panels))
            if self.full.carrier(self.full.R) != self.radius:
                raise ValueError('The declared original parent is not on its true old FullHold R')
        else:
            if (report.get('schema') != 'deep-valley-fixed-scalar-symbolic-nodes-v1'
                    or report.get('scalar_model_identity_sha256') != self.deep.model_identity_sha256
                    or self._prior_definition.get('profile_identity_sha256') != self.deep.model_identity_sha256):
                raise ValueError('The current saved carrier does not describe this fixed new scalar')
        self._radius_error = base.upper_error(self.radius, self.deep.R, deep_module.SCALE)
        return self

    def _a_box_at_definition(self, definition):
        alpha, beta = definition
        p, d = self.full, self.deep_module
        t = d.box(-beta) if alpha == 1 else d.sub(
            d.scale(self.deep._from_old(p.S), 1-alpha), d.box(beta))
        low, high = Q(t[0], d.SCALE), Q(t[1], d.SCALE)
        anchor_t = self.deep.width/4
        if high <= anchor_t:
            return self.deep.reference_at_affine(alpha, beta)[0]
        if low >= anchor_t:
            return self.deep._from_old(p.at_box(p.affine_time(alpha, beta))[0])
        # The exact query is enclosed across the new anchor; a is 1-Lipschitz.
        fee = max(anchor_t-low, high-anchor_t)
        return d.add(self.deep.anchor_radius, d.box(-fee, fee))

    def prepare_new_inputs(self, output_directory):
        """Explicit old->new scalar migration, before building the new pair."""
        require_actions()
        if not self._original_migration or self._new_input_outputs is not None:
            raise ValueError('Only one explicit original-parent migration is allowed')
        directory = Path(output_directory).resolve()
        directory.mkdir(parents=True, exist_ok=False)
        self.radius = float(Q(self.deep.R[0]+self.deep.R[1], 2*self.deep_module.SCALE))
        self._radius_error = self.base.upper_error(self.radius, self.deep.R, self.deep_module.SCALE)
        self.data['radius'] = np.array(self.radius)
        values, errors = [], []
        retained = 0
        for stage, (cell, u) in enumerate(zip(self.plan.cells, self.plan.local_u)):
            definition = self._point_definition(int(cell), float(u))
            abox = self._a_box_at_definition(definition)
            alpha, beta = definition
            exact_t = (self.deep_module.box(-beta) if alpha == 1 else
                self.deep_module.sub(self.deep_module.scale(self.deep._from_old(self.full.S), 1-alpha),
                                     self.deep_module.box(beta)))
            if Q(exact_t[0], self.deep_module.SCALE) >= self.deep.width/4:
                value = float(self.a_observations[stage])
                retained += 1
            else:
                value = float(Q(abox[0]+abox[1], 2*self.deep_module.SCALE))
            if int(cell) == len(self.mesh)-2 and float(u) == 1.:
                value = self.radius
            values.append(value)
            errors.append(self.base.upper_error(value, abox, self.deep_module.SCALE))
        self.a_observations = np.array(values)
        self._a_observation_errors = np.array(errors)
        self.data['a_stages'] = self.a_observations[:self.plan.legacy_count].copy()
        self.data['a_stage_absolute_error'] = self._a_observation_errors[:self.plan.legacy_count].copy()
        carrier_arrays = dict(self._input_carrier_arrays)
        for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3',
                    'a_stage_absolute_error', 'stage_time_absolute_error'):
            if key in self.data:
                carrier_arrays[key] = np.array(self.data[key], copy=True)
        carrier_arrays.update(a_observations=self.a_observations,
            a_observation_absolute_error=self._a_observation_errors,
            deep_valley_scalar_identity_sha256=np.array(self.deep.model_identity_sha256))
        carrier_path = directory/'observations.npz'
        np.savez_compressed(carrier_path, **carrier_arrays)
        node_path = directory/'nodes.json'
        node = dict(schema='deep-valley-fixed-scalar-symbolic-nodes-v1',
            input_sha256=self.input_records['scalar_input']['sha256'],
            S_carrier=self.S, radius_carrier=self.radius,
            true_scalar_nodes=[dict(S_coefficient=str(a), constant=str(b)) for a, b in self.nodes],
            scalar_model_identity_sha256=self.deep.model_identity_sha256,
            scalar_model_definition=self.deep.definition,
            scalar=self.deep.metadata(), mesh_sha256=self.base.array_sha(self.mesh),
            new_carrier_sha256=sha(carrier_path), source_sha256=sha(__file__),
            original_node_report=self.original_input_records['node_report'],
            original_observation_carrier=self.original_input_records['carrier'],
            fixed_new_scalar_metric=True, original_fixed_metric_preserved=False,
            scalar_prefix_literal_carrier_rows_retained=retained,
            maximum_a_observation_absolute_error=float(np.max(self._a_observation_errors)),
            new_radius_absolute_carrier_error=self._radius_error,
            old_scalar_or_geometry_certificates_inherited=False)
        node_path.write_text(json.dumps(node, indent=2, allow_nan=False)+'\n')
        self.paths.update(carrier=carrier_path, node_report=node_path)
        self.input_records.update(carrier=source_record(carrier_path), node_report=source_record(node_path))
        self._new_input_outputs = dict(observation_carrier=source_record(carrier_path),
            node_report=source_record(node_path), radius_carrier=self.radius,
            scalar_prefix_literal_carrier_rows_retained=retained,
            maximum_a_observation_absolute_error=float(np.max(self._a_observation_errors)))
        return self._new_input_outputs

    def reference_at(self, cell, u):
        definition = self._point_definition(cell, u)
        if definition not in self._reference_cache:
            boxes = self.deep.reference_at_affine(*definition)
            values = np.array([float(Q(value[0]+value[1], 2*self.deep_module.SCALE)) for value in boxes])
            if definition == (Q(1), Q(0)):
                # mix_profile uses the persisted numerical R carrier literally
                # at the cap.  Pay ITS error, not a newly rounded midpoint's.
                values[0] = self.radius
            errors = np.array([self.base.upper_error(value, enclosure, self.deep_module.SCALE)
                               for value, enclosure in zip(values, boxes)])
            self._maximum_reference_errors = np.maximum(self._maximum_reference_errors, errors)
            values.setflags(write=False)
            errors.setflags(write=False)
            self._reference_cache[definition] = (values, errors)
        return self._reference_cache[definition]

    def create_pair(self, dense_source, batch_source, *, N=2048, stage_block=64, quarter=True):
        require_actions()
        if self._original_migration and self._new_input_outputs is None:
            raise ValueError('Materialize the explicit new a/R/node/observation inputs before solving')
        pair = self.base.TailLiftContext.create_pair(self, dense_source, batch_source,
            N=N, stage_block=stage_block, quarter=quarter)
        if self._original_context is not None:
            self._original_context._operator_sources = dict(self._operator_sources)
            expected = self._original_context.definition()
            if self._source_parent_definition != expected:
                raise ValueError('The real original parent canonical model does not match its complete source/input definition')
        elif self._prior_definition != self.definition():
            raise ValueError('The current saved new-scalar canonical model does not match its exact complete definition')
        return pair

    def definition(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__),
            base_reference_factory_source_sha256=BASE_FACTORY_SHA,
            deep_scalar_source_sha256=DEEP_SOURCE_SHA,
            profile_identity_sha256=self.deep.model_identity_sha256,
            profile_definition=self.deep.definition,
            fixed_new_scalar_metric=True,
            scalar_target='g_n=ds^2+a_new(s)^2*dtheta^2; a_new fixed by the complete deep-valley profile',
            target_is_a_moving_angular_mean=False,
            lambda_value=1., eta_start_node=self.eta_start_node, eta_end_node=self.eta_end_node,
            eta_start_symbolic=[str(v) for v in self.nodes[self.eta_start_node]],
            eta_end_symbolic=[str(v) for v in self.nodes[self.eta_end_node]],
            eta_start_carrier=self.eta_left, eta_end_carrier=self.eta_right,
            width_exact=str(Q(self.width)), mesh_sha256=self.base.array_sha(self.mesh), M=self.M,
            scalar_input_sha256=self.input_records['scalar_input']['sha256'],
            node_report_sha256=self.input_records['node_report']['sha256'],
            original_observation_carrier_sha256=self.input_records['carrier']['sha256'],
            observation_carrier_semantics='Literal complete observation carrier of THIS new scalar input',
            source_sha256s={key: self.input_records[key]['sha256'] for key in
                ('scalar_source', 'integer_source', 'hold_source', 'observed_source')},
            operator_source_sha256s={key: value['sha256'] for key, value in self._operator_sources.items()},
            scalar_columns=list(SCALARS), reference_columns=list(REFERENCE),
            formula='lambda=1: f=eta*a_new; h=eta; k=-eta*I_new',
            I_definition='Z_new(exact S)-Z_new(s), with the complete new deep-valley integrals',
            eta_definition='Original C2 quintic on the SAME declared symbolic eta nodes; eta=1 before the out ramp',
            cap_definition='Exact NEW radius R_new=a_new(S), free H, and the same flat disk interface')

    def metadata(self):
        definition = self.definition()
        active = 0 if self._reference_active is None else int(self._reference_active.sum())
        result = dict(schema=SCHEMA, definition=definition,
            model_identity_sha256=canonical_sha(definition),
            fixed_scalar_metric_identity_sha256=self.deep.model_identity_sha256,
            fixed_new_scalar_metric=True, moving_angular_mean_target=False,
            inputs=self.input_records, operator_sources=self._operator_sources,
            original_fullhold=self.full.metadata(), new_exact_scalar=self.deep.metadata(),
            scalar_working_accuracy=self._scalar_working,
            stages=len(self.plan.cells), legacy_stages=self.plan.legacy_count,
            reference_queried_rows=active, cached_exact_point_definitions=len(self._reference_cache),
            maximum_reference_carrier_absolute_errors=dict(zip(REFERENCE, self._maximum_reference_errors.tolist())),
            exact_new_radius_carrier_absolute_error=self._radius_error,
            original_symbolic_mesh_preserved=True, original_free_coordinates_preserved=True,
            original_target_a_carriers_preserved=not self._original_migration,
            new_scalar_input_outputs=self._new_input_outputs,
            source_parent_bundle=self.original_input_records['bundle'],
            source_parent_model_identity_sha256=self._source_parent_model_identity,
            original_parent_migration=self._original_migration,
            core_three_jets_preserved=True, cap_three_jets_for_NEW_radius=True,
            h_still_piecewise_quintic_on_same_eta_nodes=True,
            actual_point_adapter_and_complete_core_H_derivatives='Unchanged byte-bound R671 functions with THIS context lift_at',
            old_certificates_inherited=False, continuous_metric_certified=False,
            continuous_geometry_certified=False, nonlinear_solve_performed=False,
            carrier_scope='Finite numerical values on the declared original symbolic locations; all scalar approximation errors recorded, not a complete floating field certificate',
            physical_space='NEW exact deep-valley lift plus ALL original shared-quintic residual coordinates')
        if self._carrier_output is not None:
            result['reference_lift_carrier'] = self._carrier_output
        return result

    def transfer_seed(self, problem, x, *, source_lambda=1., mode='keep-q'):
        require_actions()
        if mode != 'keep-q' or float(source_lambda) != 1.:
            raise ValueError('This first new-scalar branch uses only explicit keep-q from lambda=1')
        if not self._operator_sources:
            raise ValueError('Construct the complete same-input observed/native pair first')
        if not self._original_migration and self._prior_definition != self.definition():
            raise ValueError('A continuation seed must keep the SAME new canonical scalar/model')
        result = np.array(x, copy=True)
        return result, dict(mode='keep-q', source_lambda=1., target_lambda=1.,
            source_bundle_sha256=self.original_input_records['bundle']['sha256'],
            source_model_identity_sha256=self._source_parent_model_identity,
            target_model_identity_sha256=canonical_sha(self.definition()),
            fixed_new_scalar_metric_identity_sha256=self.deep.model_identity_sha256,
            source_and_target_scalar_equal=not self._original_migration,
            physical_field_unchanged=not self._original_migration,
            same_coordinate_array=True, all_original_coordinates_remain_free=True,
            accepted_nonlinear_step=False, geometry_or_metric_inherited=False,
            old_radius_reused=False if self._original_migration else True,
            actual_followup='Read all original/Gauss Gram rows and every permanent geometry/amplitude point of THIS actual new field before accepting a direction')


def point_adapter(original):
    base, _ = dependencies()
    return base.point_adapter(original)


def fields_block_observed(problem, prepared, start, stop):
    base, _ = dependencies()
    return base.fields_block_observed(problem, prepared, start, stop)


def read_positions(paths, kind, old_carrier_sha):
    points, sources, seen = [], [], {}
    for path in paths:
        path = Path(path).resolve()
        payload = json.loads(path.read_text())
        if payload.get('carrier_sha256', old_carrier_sha) != old_carrier_sha:
            raise ValueError('The source location manifest is not on the actual old observation carrier')
        manifest_key = 'curvature_points' if kind == 'curvature' else 'radius_points'
        if manifest_key in payload:
            protected = {tuple(value) for value in payload.get('protected_curvature_points', [])}
            values = [dict(cell=value[0], u=value[1], phi=value[2],
                           protected=kind == 'curvature' and tuple(value) in protected)
                      for value in payload[manifest_key]]
        elif 'final_curvature_memory' in payload or 'final_radius_memory' in payload:
            values = payload['final_curvature_memory' if kind == 'curvature' else 'final_radius_memory']
        elif 'searches' in payload:
            values = [search['final'] for search in payload['searches'] if search['kind'] == kind]
        else:
            values = [payload['final']] if 'final' in payload else payload['witnesses']
        for value in values:
            item = dict(cell=int(value['cell']), u=float(value['u']), phi=float(value['phi']),
                        protected=bool(value.get('protected', False)))
            key = (item['cell'], item['u'].hex(), item['phi'].hex())
            if key in seen:
                points[seen[key]]['protected'] |= item['protected']
            else:
                seen[key] = len(points)
                points.append(item)
        sources.append(source_record(path))
    if not points:
        raise ValueError('Keep the complete declared source '+kind+' position memory')
    return points, sources


def prepare(args):
    require_actions()
    started = time.monotonic()
    context = TailLiftContext.from_files(bundle=args.bundle, carrier=args.observations,
        node_report=args.node_report, scalar_input=args.scalar_input,
        scalar_source=args.scalar_source, integer_source=args.integer_source,
        hold_source=args.hold_source, observed_source=args.observed_source,
        eta_start_node=args.eta_start_node, lambda_value=1., panels=args.panels,
        allow_original_parent=True, scalar_admission_seconds=args.scalar_admission_seconds,
        scalar_integral_tolerance=args.scalar_integral_tolerance,
        scalar_tail_cutoff=args.scalar_tail_cutoff)
    output = context.prepare_new_inputs(args.outdir)
    problem, native = context.create_pair(args.operator_source, args.batch_source,
        N=args.angles, stage_block=args.stage_block, quarter=True)
    x, affine = problem.pack(context.data['qjets'], float(context.data['Hcap']), require_affine=True)
    x, migration = context.transfer_seed(problem, x, source_lambda=1., mode='keep-q')
    profile = context.save_carrier(args.outdir/'reference-profiles.npz', args.outdir/'reference-profiles.json')
    seed_path = args.outdir/'seed.npz'
    arrays = context.bundle_arrays(problem, x)
    arrays.update(exact_tail_lambda=np.array(1.), exact_tail_eta_start_node=np.array(args.eta_start_node),
        fixed_new_scalar_metric_identity_sha256=np.array(context.deep.model_identity_sha256))
    np.savez_compressed(seed_path, **arrays)
    old_carrier_sha = context.original_input_records['carrier']['sha256']
    curvature, curvature_sources = read_positions(args.witness_input, 'curvature', old_carrier_sha)
    radius, radius_sources = read_positions(args.radius_witness_input, 'diameter', old_carrier_sha)
    for point in curvature+radius:
        if not 0 <= point['cell'] < len(context.mesh)-1 or not 0 <= point['u'] <= 1 or not np.isfinite(point['phi']):
            raise ValueError('A source witness address lies outside the unchanged exact mesh domain')
    locations = dict(schema='deep-valley-same-symbolic-location-transfer-v1',
        carrier_sha256=output['observation_carrier']['sha256'], bundle_sha256=sha(seed_path),
        original_carrier_sha256=old_carrier_sha,
        original_bundle_sha256=context.original_input_records['bundle']['sha256'],
        curvature_points=[[point[key] for key in ('cell', 'u', 'phi')] for point in curvature],
        radius_points=[[point[key] for key in ('cell', 'u', 'phi')] for point in radius],
        protected_curvature_points=[[point[key] for key in ('cell', 'u', 'phi')]
                                    for point in curvature if point['protected']],
        sources=dict(curvature=curvature_sources, radius=radius_sources),
        same_literal_symbolic_mesh=True, only_locations_transferred=True,
        original_metric_or_geometry_values_transferred=False,
        scope='Every source physical phi/cell/u address is retained; all values must be reread on the new scalar field')
    location_path = args.outdir/'locations.json'
    location_path.write_text(json.dumps(locations, indent=2, allow_nan=False)+'\n')
    report = dict(schema='deep-valley-fixed-scalar-keep-q-preparation-v1',
        source=source_record(__file__), original_inputs=context.original_input_records,
        new_inputs=output, new_seed=source_record(seed_path),
        new_locations=source_record(location_path), new_reference_profiles=profile,
        exact_tail_context=context.metadata(), migration=migration,
        fixed_new_scalar_metric=True, fixed_scalar_metric_identity_sha256=context.deep.model_identity_sha256,
        target_definition='g_n=ds^2+a_new(s)^2*dtheta^2; no moving angular mean',
        original_directions_or_certificates_inherited=False,
        current_core_and_q_and_H_words_preserved=True, affine=affine,
        M=problem.M, J=problem.J, full_angles=problem.full_N,
        complete_observation_stages=problem.P,
        curvature_locations=len(curvature), radius_locations=len(radius),
        whole_new_seed_Gram_or_geometry_read_performed=False,
        accepted_nonlinear_step=False, new_nonradial_exact_solution=False,
        topic_complete=False, elapsed_seconds=time.monotonic()-started,
        execution=dict(repository=os.environ['GITHUB_REPOSITORY'], run_id=os.environ.get('GITHUB_RUN_ID'),
            run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'), workflow_trigger_commit=os.environ.get('GITHUB_SHA')),
        followup='Use these new seed/observations/nodes/locations in the complete fixed-g_n amplitude-constrained fullclosed driver; keep the scalar profile identity fixed during all directions')
    report_path = args.outdir/'report.json'
    report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(schema=report['schema'], new_seed_sha256=sha(seed_path),
        fixed_scalar_metric_identity_sha256=context.deep.model_identity_sha256,
        new_observation_carrier_sha256=output['observation_carrier']['sha256'],
        new_node_report_sha256=output['node_report']['sha256'],
        new_locations_sha256=sha(location_path), all_original_variables_preserved=True,
        actual_solve_performed=False, report_sha256=sha(report_path)), sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--observations', type=Path, required=True)
    parser.add_argument('--node-report', type=Path, required=True)
    parser.add_argument('--scalar-input', type=Path, required=True)
    parser.add_argument('--scalar-source', type=Path, required=True)
    parser.add_argument('--integer-source', type=Path, required=True)
    parser.add_argument('--hold-source', type=Path, required=True)
    parser.add_argument('--observed-source', type=Path, required=True)
    parser.add_argument('--operator-source', type=Path, required=True)
    parser.add_argument('--batch-source', type=Path, required=True)
    parser.add_argument('--eta-start-node', type=int, required=True)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--scalar-admission-seconds', type=float, default=300)
    parser.add_argument('--scalar-integral-tolerance', default='1e-18')
    parser.add_argument('--scalar-tail-cutoff', default='1/8')
    parser.add_argument('--witness-input', type=Path, action='append', required=True)
    parser.add_argument('--radius-witness-input', type=Path, action='append', required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    prepare(parser.parse_args())
