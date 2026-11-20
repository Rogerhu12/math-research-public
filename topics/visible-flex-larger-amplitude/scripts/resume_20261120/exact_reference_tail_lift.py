#!/usr/bin/env python3
"""R671 exact-reference-tail lift on the ORIGINAL complete free coordinates.

This module is a new physical representation, not a reinterpretation of an
old candidate or certificate.  It keeps the original scalar, mesh, angular
basis, all free jets/core coefficients/H, and every observed Gram row.

Nine scalar columns are (h,h_s,h_ss,f,f_s,f_ss,k,k_s,k_ss):
    F = q + f e_r(Theta) + (h H + k) e_z.
The public six-column lift_scalar view is the first six columns.  The old
complete Gram Jv/VJP and six-jet cotangent formulas therefore remain exact;
the NEW actual-field entry points also include the fixed k offset.

lambda=0 returns the unchanged original operator classes.  lambda>0 uses
the original FullHold oracle, never a fitted a or an interpolated I.
No scientific calculation runs on import.  All actual construction/solve
commands belong in this repository's public GitHub Actions.
"""
from fractions import Fraction as Q
from pathlib import Path
from types import FunctionType, ModuleType, SimpleNamespace
import argparse
import gzip
import hashlib
import importlib.util
import json
import sys
import time

import numpy as np


SCHEMA = 'R671-exact-reference-tail-lift-v1'
SCALARS = ('h', 'hs', 'hss', 'f', 'fs', 'fss', 'k', 'ks', 'kss')
REFERENCE = ('a', 'as', 'ass', 'I', 'Is', 'Iss')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    digest = hashlib.sha256()
    digest.update(str(value.dtype).encode())
    digest.update(json.dumps(list(value.shape)).encode())
    digest.update(value.tobytes())
    return digest.hexdigest()


def load(source, label):
    if isinstance(source, ModuleType):
        return source
    path = Path(source).resolve()
    name = '_exact_reference_tail_' + label + '_' + sha(path)[:16]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def source_record(source):
    path = Path(source.__file__ if isinstance(source, ModuleType) else source).resolve()
    return dict(path=str(path), sha256=sha(path))


def upper_error(carrier, box, denominator):
    error = max(abs(Q(float(carrier))-Q(box[0], denominator)),
                abs(Q(float(carrier))-Q(box[1], denominator)))
    value = float(error)
    if Q(value) < error:
        value = float(np.nextafter(value, np.inf))
    return value


def smoothstep_jets(s, left, right):
    if s <= left:
        return np.array([0., 0., 0.])
    if s >= right:
        return np.array([1., 0., 0.])
    width = right-left
    u = (s-left)/width
    return np.array([u*u*u*(10+u*(-15+6*u)),
                     30*u*u*(1-u)*(1-u)/width,
                     60*u*(1-u)*(1-2*u)/(width*width)])


class TailLiftContext:
    """One explicit same-scalar/model binding, shared by observed/native maps.

    from_files() reads the original inputs and instantiates FullHold.  The
    actual tail scalar queries occur when create_pair() builds the tables
    or when a new arbitrary geometric point is requested.  Those queries
    use exact binary u on the original symbolic alpha*S+beta nodes.
    """

    @classmethod
    def from_files(cls, *, bundle, carrier, node_report, scalar_input,
                   scalar_source, integer_source, hold_source, observed_source,
                   eta_start_node, lambda_value, panels=128):
        self = cls()
        self.paths = {key: Path(value).resolve() for key, value in dict(
            bundle=bundle, carrier=carrier, node_report=node_report,
            scalar_input=scalar_input, scalar_source=scalar_source,
            integer_source=integer_source, hold_source=hold_source,
            observed_source=observed_source).items()}
        self.input_records = {key: source_record(path) for key, path in self.paths.items()}
        self.lambda_value = float(lambda_value)
        if not np.isfinite(self.lambda_value) or not 0 <= self.lambda_value <= 1:
            raise ValueError('R671 uses an explicit fixed lambda in [0,1]')
        self.eta_start_node = int(eta_start_node)
        self.observed = load(self.paths['observed_source'], 'observed')
        with np.load(self.paths['bundle'], allow_pickle=False) as data:
            self.data = {key: np.array(data[key], copy=True) for key in data.files}
        with np.load(self.paths['carrier'], allow_pickle=False) as data:
            self.plan = self.observed.ObservationPlan.from_arrays(data)
            self.a_observations = np.array(data['a_observations'], copy=True)
            for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
                if not np.array_equal(data[key], self.data[key]):
                    raise ValueError('Reference lift must retain the literal original '+key)
        self.mesh = np.array(self.data['mesh'], copy=True)
        self.S = float(self.mesh[-1])
        self.radius = float(self.data['radius'])
        self.width = float(self.data['width'])
        self.M = (self.data['qjets'].shape[-1]-2)//3
        report = json.loads(self.paths['node_report'].read_text())
        if self.input_records['scalar_input']['sha256'] != report['input_sha256']:
            raise ValueError('The scalar source data must match the original symbolic node report')
        self.nodes = [(Q(v['S_coefficient']), Q(v['constant']))
                      for v in report['true_scalar_nodes']]
        endpoint_definition = (Q(1), -Q(self.width))
        matches = [j for j, value in enumerate(self.nodes) if value == endpoint_definition]
        if len(matches) != 1:
            raise ValueError('Need the original unique symbolic S-width node')
        self.eta_end_node = matches[0]
        if (len(self.nodes) != len(self.mesh)
                or self.plan.legacy_count != 2*len(self.mesh)-1
                or self.plan.lift_break_node != self.eta_end_node
                or not 0 < self.eta_start_node < self.eta_end_node < len(self.mesh)-1
                or float(report['S_carrier']) != self.S
                or float(report['radius_carrier']) != self.radius):
            raise ValueError('Changed mesh/port identity or invalid existing eta nodes')
        self.eta_left = float(self.mesh[self.eta_start_node])
        self.eta_right = float(self.mesh[self.eta_end_node])
        raw = self.paths['scalar_input'].read_bytes()
        scalar_data = json.loads(gzip.decompress(raw) if str(self.paths['scalar_input']).endswith('.gz') else raw)
        scalar_module = load(self.paths['scalar_source'], 'fullhold')
        self.full = scalar_module.FullHold(scalar_data, self.paths['integer_source'],
                                          self.paths['hold_source'], panels=panels)
        if self.full.carrier(self.full.S) != self.S or self.full.carrier(self.full.R) != self.radius:
            raise ValueError('The original FullHold endpoint/radius carriers changed')
        left_box = self._node_box(self.eta_start_node)
        if Q(left_box[0], self.full.h.S) <= self.full.cut:
            raise ValueError('eta must start strictly inside the original Hold extension')
        if Q(self.width) <= self.full.out:
            raise ValueError('The declared old lift start must precede the whole out ramp')
        self._reference_cache = {}
        self._point_profiles = {}
        self._old_profiles = None
        self._profiles = None
        self._reference_values = None
        self._reference_errors = None
        self._reference_active = None
        self._operator_sources = {}
        self._carrier_output = None
        self._maximum_reference_errors = np.zeros(6)
        self._node_indices = {float(s): j for j, s in enumerate(self.mesh)}
        self._prior_definition = None
        if 'reference_tail_model_json' in self.data:
            self._prior_definition = json.loads(str(self.data['reference_tail_model_json'].item()))
        return self

    def _node_box(self, index):
        alpha, beta = self.nodes[index]
        return self.full.affine_time(alpha, beta)

    def _point_definition(self, cell, u):
        cell, u = int(cell), float(u)
        if not 0 <= cell < len(self.mesh)-1 or not np.isfinite(u) or not 0 <= u <= 1:
            raise ValueError('Point must lie in an original physical cell')
        left, right = self.nodes[cell], self.nodes[cell+1]
        uu = Q(u)
        return ((1-uu)*left[0]+uu*right[0], (1-uu)*left[1]+uu*right[1])

    def _angle_curvature(self, sbox):
        """Original continuous alpha/kappa, including exact boundary boxes.

        This is the R669 TailScalar formula, evaluated through FullHold's
        integer arithmetic.  It never uses sqrt(1-a_s^2) near the cap.
        """
        p, h = self.full, self.full.h
        o, denominator = p.o, h.S
        lo, hi = Q(sbox[0], denominator), Q(sbox[1], denominator)
        if sbox == p.S:
            return h.scale(p.pi, -Q(1, 2)), h.interval(Q(0))
        kmax = Q(5, 2)
        kprime = Q(4653, 1000)*Q(15, 8)/p.f
        endpoint_k = [p.K, h.interval(p.kn), h.interval(p.kn),
                      h.interval(p.kp), h.interval(p.kp), h.interval(Q(0))]
        for j, boundary in enumerate(p.time):
            left, right = Q(boundary[0], denominator), Q(boundary[1], denominator)
            if lo <= right and hi >= left:
                fee = max(abs(lo-right), abs(hi-left))
                return (h.add(p.alpha[j], o.box(-kmax*fee, kmax*fee)),
                        h.add(endpoint_k[j], o.box(-kprime*fee, kprime*fee)))
        j = next((i for i in range(5) if lo > Q(p.time[i][1], denominator)
                  and hi < Q(p.time[i+1][0], denominator)), None)
        if j is None:
            raise ValueError('The new lift scalar point is outside one original Hold segment')
        tbox = o.subtract(sbox, p.time[j])
        if j not in p.ramps:
            k = p.kn if j == 1 else p.kp
            return o.subtract(p.alpha[j], h.scale(tbox, k)), h.interval(k)
        ramp = p.ramps[j]
        tl, th = Q(tbox[0], denominator), Q(tbox[1], denominator)
        mid, radius = (tl+th)/2, (th-tl)/2
        u = mid/ramp.width
        smooth = 10*u**3-15*u**4+6*u**5
        k = h.add(h.scale(ramp.left, 1-smooth), h.scale(ramp.right, smooth))
        return (h.add(ramp.angle(mid), o.box(-kmax*radius, kmax*radius)),
                h.add(k, o.box(-kprime*radius, kprime*radius)))

    def reference_at(self, cell, u):
        definition = self._point_definition(cell, u)
        if definition in self._reference_cache:
            return self._reference_cache[definition]
        p, h = self.full, self.full.h
        sbox = p.affine_time(*definition)
        a, increment = p.at_box(sbox)
        if increment is None:
            raise ValueError('I is queried only where the original Hold height is defined')
        alpha, kappa = self._angle_curvature(sbox)
        ap, c = h.sine_cosine(alpha)
        I = p.o.subtract(p.height_increment, increment)
        if definition == (Q(1), Q(0)):
            a = p.R
            ap, c, kappa, I = (h.interval(Q(v)) for v in (-1, 0, 0, 0))
        boxes = (a, ap, h.neg(h.multiply(kappa, c)), I,
                 h.neg(c), h.neg(h.multiply(kappa, ap)))
        values = np.array([p.carrier(box) for box in boxes])
        errors = np.array([upper_error(value, box, h.S) for value, box in zip(values, boxes)])
        self._maximum_reference_errors = np.maximum(self._maximum_reference_errors, errors)
        values.setflags(write=False); errors.setflags(write=False)
        self._reference_cache[definition] = (values, errors)
        return values, errors

    def _eta(self, cell, u, s):
        # Symbolic node membership chooses the constant branches.  The
        # original binary mesh/stage times are numerical carriers of it.
        if cell < self.eta_start_node or (cell == self.eta_start_node and u == 0.):
            return np.array([0., 0., 0.])
        if cell >= self.eta_end_node or (cell+1 == self.eta_end_node and u == 1.):
            return np.array([1., 0., 0.])
        return smoothstep_jets(s, self.eta_left, self.eta_right)

    def mix_profile(self, old, cell, u, s, *, lambda_value=None):
        lam = self.lambda_value if lambda_value is None else float(lambda_value)
        old = np.asarray(old, dtype=float)
        if old.shape != (6,) or not np.isfinite(old).all() or not 0 <= lam <= 1:
            raise ValueError('Need the literal six old scalar values and lambda in [0,1]')
        if lam == 0:
            return np.r_[old, np.zeros(3)]
        eta, ep, epp = self._eta(int(cell), float(u), float(s))
        if eta == ep == epp == 0:
            return np.r_[old, np.zeros(3)]
        values, _ = self.reference_at(cell, u)
        a, ap, app, I, Ip, Ipp = values
        hnew = (1-lam)*old[:3]+lam*np.array([eta, ep, epp])
        fnew = (1-lam)*old[3:]+lam*np.array(
            [eta*a, ep*a+eta*ap, epp*a+2*ep*ap+eta*app])
        knew = -lam*np.array([eta*I, ep*I+eta*Ip, epp*I+2*ep*Ip+eta*Ipp])
        # Literal port carriers avoid turning enclosure uncertainty into
        # nonzero cap jets. These endpoint identities are exact in R671.
        if int(cell) == len(self.mesh)-2 and float(u) == 1.:
            return np.array([1., 0., 0., self.radius, -1., 0., 0., 0., 0.])
        return np.r_[hnew, fnew, knew]

    def _build_tables(self, old_profiles):
        old_profiles = np.asarray(old_profiles, dtype=float)
        P = len(self.plan.cells)
        if old_profiles.shape != (P, 6):
            raise ValueError('Need every original and Gauss old lift row before mixing')
        self._old_profiles = old_profiles.copy()
        self._profiles = np.zeros((P, 9))
        self._reference_values = np.zeros((P, 6))
        self._reference_errors = np.zeros((P, 6))
        self._reference_active = np.zeros(P, dtype=bool)
        for stage, (cell, u, s) in enumerate(zip(self.plan.cells, self.plan.local_u, self.plan.times)):
            self._profiles[stage] = self.mix_profile(old_profiles[stage], cell, u, s)
            if self.lambda_value != 0 and np.any(self._eta(int(cell), float(u), float(s))):
                values, errors = self.reference_at(cell, u)
                self._reference_active[stage] = True
                self._reference_values[stage], self._reference_errors[stage] = values, errors
        self._profiles.setflags(write=False)
        return self._profiles

    def create_pair(self, dense_source, batch_source, *, N=2048, stage_block=64, quarter=True):
        """Return (all-observations operator, legacy-structure basis operator).

        The native object is solely a structural template for the complete
        nodal B/B^T and the physical H compensation. No old-only objective
        is substituted for the all-row objective.
        """
        dense = load(dense_source, 'dense')
        batch = load(batch_source, 'batch')
        self._operator_sources = dict(dense=source_record(dense), batch=source_record(batch),
                                      observed=source_record(self.observed))
        inputs = (self.mesh, self.data['a_stages'], self.radius, self.data['fixed_core_first3'])
        common = dict(M=self.M, N=int(N), width=self.width, quarter=bool(quarter),
                      stage_block=int(stage_block))
        if self.lambda_value == 0:
            observed = self.observed.create(dense, *inputs, batch_source=batch,
                observation_plan=self.plan, a_observations=self.a_observations, **common)
            native = batch.create(dense, *inputs, **common)
            self._build_tables(observed.lift_scalar)
            return observed, native

        class ReferenceObserved(ReferenceTailMixin, self.observed.ObservationMixin,
                                batch.BatchedMixin, dense.ClosedGram):
            pass

        class ReferenceNative(ReferenceTailMixin, batch.BatchedMixin, dense.ClosedGram):
            pass

        observed = ReferenceObserved(*inputs, tail_context=self,
            observation_plan=self.plan, a_observations=self.a_observations, **common)
        native = ReferenceNative(*inputs, tail_context=self, **common)
        return observed, native

    def definition(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__),
            lambda_value=self.lambda_value,
            eta_start_node=self.eta_start_node, eta_end_node=self.eta_end_node,
            eta_start_symbolic=[str(v) for v in self.nodes[self.eta_start_node]],
            eta_end_symbolic=[str(v) for v in self.nodes[self.eta_end_node]],
            eta_start_carrier=self.eta_left, eta_end_carrier=self.eta_right,
            mesh_sha256=array_sha(self.mesh), M=self.M,
            scalar_input_sha256=self.input_records['scalar_input']['sha256'],
            node_report_sha256=self.input_records['node_report']['sha256'],
            original_observation_carrier_sha256=self.input_records['carrier']['sha256'],
            source_sha256s={key: self.input_records[key]['sha256'] for key in
                ('scalar_source', 'integer_source', 'hold_source', 'observed_source')},
            operator_source_sha256s={key: value['sha256'] for key, value in self._operator_sources.items()},
            scalar_columns=list(SCALARS), reference_columns=list(REFERENCE),
            formula='f=(1-lambda)*chi*(R+S-s)+lambda*eta*a; h=(1-lambda)*chi+lambda*eta; k=-lambda*eta*I',
            I_definition='Integral from s to exact S of the ORIGINAL FullHold cos(alpha)',
            eta_definition='C2 quintic smoothstep on the two declared original symbolic nodes; eta=1 before the out ramp')

    def metadata(self):
        definition = self.definition()
        active = 0 if self._reference_active is None else int(self._reference_active.sum())
        result = dict(schema=SCHEMA, definition=definition,
            model_identity_sha256=canonical_sha(definition), inputs=self.input_records,
            operator_sources=self._operator_sources, fullhold=self.full.metadata(),
            stages=len(self.plan.cells), legacy_stages=self.plan.legacy_count,
            reference_queried_rows=active, cached_exact_point_definitions=len(self._reference_cache),
            maximum_reference_carrier_absolute_errors=dict(zip(REFERENCE, self._maximum_reference_errors.tolist())),
            original_target_a_carriers_preserved=True, original_symbolic_mesh_preserved=True,
            original_free_coordinates_preserved=True, core_and_cap_three_jets_preserved=True,
            lambda_zero_original_operator_classes=self.lambda_value == 0,
            gauss_polynomial_exactness_claimed=False,
            old_certificates_inherited=False, continuous_metric_certified=False,
            continuous_geometry_certified=False, nonlinear_solve_performed=False,
            scalar_scope='Original integer/Fraction oracle encloses a/I and derivatives on active tail rows only; zero reference-array placeholders outside the active mask are NOT scalar values',
            carrier_scope='Numerical finite operator on original double mesh/stages; original symbolic locations and new scalar carrier errors are recorded, not a full floating field enclosure',
            physical_space='R671 new analytic lift plus ALL original shared-quintic residual coordinates')
        if active:
            result['maximum_lift_a_carrier_difference_from_target_carrier'] = float(np.max(np.abs(
                self._reference_values[self._reference_active, 0]-self.a_observations[self._reference_active])))
        if self._carrier_output is not None:
            result['reference_lift_carrier'] = self._carrier_output
        return result

    def save_carrier(self, npz_path, json_path):
        """Write local Actions raw and a compact source/input manifest."""
        if self._profiles is None:
            raise ValueError('Construct the observed/native pair first')
        npz_path, json_path = Path(npz_path).resolve(), Path(json_path).resolve()
        if npz_path.exists() or json_path.exists():
            raise FileExistsError('Choose new reference-lift carrier outputs')
        npz_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        definition = self.definition()
        np.savez_compressed(npz_path, lift_scalar9=self._profiles,
            old_lift_scalar=self._old_profiles, reference_values=self._reference_values,
            reference_absolute_error=self._reference_errors, reference_active=self._reference_active,
            mesh=self.mesh, observation_cells=self.plan.cells, observation_u=self.plan.local_u,
            observation_times=self.plan.times, target_a_observations=self.a_observations,
            lambda_value=np.array(self.lambda_value), eta_start_node=np.array(self.eta_start_node),
            eta_end_node=np.array(self.eta_end_node),
            model_definition_json=np.array(json.dumps(definition, sort_keys=True)))
        self._carrier_output = dict(path=str(npz_path), sha256=sha(npz_path),
                                    bytes=npz_path.stat().st_size)
        metadata = self.metadata()
        json_path.write_text(json.dumps(metadata, indent=2, allow_nan=False)+'\n')
        return dict(**self._carrier_output, report_path=str(json_path),
                    report_sha256=sha(json_path), model_identity_sha256=canonical_sha(definition))

    def transfer_seed(self, problem, x, *, source_lambda=0., mode='keep-q'):
        """Declare a new field; optionally preserve old nodal jets by projection.

        A nonzero source lambda is accepted only for the same eta/scalar
        definition recorded in this input bundle.  The Fourier projection
        is a FINITE current-grid projection of residual coefficients, not
        a truncation of the new analytic e_r(Theta) lift. Interior fields
        and all certificates must be reread even if nodal defects are tiny.
        """
        source_lambda = float(source_lambda)
        if mode not in ('keep-q', 'nodal-projection') or not 0 <= source_lambda <= 1:
            raise ValueError('Declare keep-q or nodal-projection and source lambda in [0,1]')
        if source_lambda != 0:
            old = self._prior_definition
            now = self.definition()
            keys = ('eta_start_node', 'eta_end_node', 'eta_start_symbolic', 'eta_end_symbolic',
                    'mesh_sha256', 'M', 'scalar_input_sha256', 'node_report_sha256',
                    'source_sha256', 'source_sha256s', 'operator_source_sha256s',
                    'original_observation_carrier_sha256')
            if old is None or any(old.get(key) != now.get(key) for key in keys) or old.get('lambda_value') != source_lambda:
                raise ValueError('A nonzero previous lambda needs its actual matching model definition')
        elif self._prior_definition is not None and self._prior_definition.get('lambda_value', 0.) != 0:
            raise ValueError('Cannot label a previously nonzero-lambda field as the old lambda=0 model')
        x = np.array(x, copy=True)
        info = dict(mode=mode, source_lambda=source_lambda, target_lambda=self.lambda_value,
            source_bundle_sha256=self.input_records['bundle']['sha256'],
            target_model_identity_sha256=canonical_sha(self.definition()),
            accepted_nonlinear_step=False, geometry_or_metric_inherited=False,
            all_original_coordinates_remain_free=True)
        if mode == 'keep-q' or source_lambda == self.lambda_value:
            info['physical_field_unchanged'] = source_lambda == self.lambda_value
            info['same_coordinate_array'] = True
            return x, info
        if self._old_profiles is None:
            raise ValueError('Construct the model before transferring a seed')
        prepared = problem.prepare(x)
        jets, height, _ = problem.unpack(x)
        jets = np.array(jets, copy=True)
        projected_er = np.zeros(problem.n)
        cr = problem.cos.T@(problem.multiplicity*prepared.er[:, 0])
        ct = problem.sin.T@(problem.multiplicity*prepared.er[:, 1])
        projected_er[:problem.M+1] = 2*cr/problem.full_N
        projected_er[0] *= .5
        projected_er[problem.M+1:2*problem.M+1] = 2*ct/problem.full_N
        discrete_er_defect = problem.synth(projected_er)-prepared.er
        old_node_profiles, target_node_profiles = [], []
        for j in range(problem.J):
            cell, u = (j, 0.) if j < problem.J-1 else (problem.J-2, 1.)
            stage = 2*j
            old_node_profiles.append(self.mix_profile(self._old_profiles[stage], cell, u,
                self.mesh[j], lambda_value=source_lambda))
            target_node_profiles.append(self._profiles[stage])
        difference = np.asarray(old_node_profiles)-np.asarray(target_node_profiles)
        for order in range(3):
            jets[:, order] += difference[:, 3+order, None]*projected_er[None]
            jets[:, order, 2*problem.M+1] += difference[:, order]*height+difference[:, 6+order]
        original_jets, _, _ = problem.unpack(x)
        jets[0] = original_jets[0]
        jets[-1] = original_jets[-1]
        result, affine = problem.pack(jets, height, require_affine=True)
        per_order = [float(np.max(np.abs(difference[:, 3+k, None, None]*discrete_er_defect[None])))
                     for k in range(3)]
        info.update(physical_field_unchanged=False, same_coordinate_array=False,
            affine=affine, finite_projection_full_angles=problem.full_N,
            finite_projection_modes=problem.M,
            nodal_projection_defect_components_max_per_radial_order=per_order,
            core_and_terminal_arrays_preserved_literally=True,
            projection_scope='Discrete full-orbit Fourier projection of analytic er into residual R/T modes at nodes only; no claim of continuous projection accuracy or of preserving between-node fields',
            subsequent_readout='Recompute full Gram, all six jets, remembered geometric points and applicable continuous certificates on THIS new field')
        return result, info

    def bundle_arrays(self, problem, x):
        """Preserve scalar carriers and attach the new physical-field identity."""
        keys = ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3',
                'a_stage_absolute_error', 'stage_time_absolute_error')
        arrays = {key: np.array(self.data[key], copy=True) for key in keys if key in self.data}
        jets, height, core = problem.unpack(x)
        arrays.update(qjets=jets, Hcap=np.asarray(height), core_coefficients=core,
            reference_tail_lambda=np.array(self.lambda_value),
            reference_tail_model_json=np.array(json.dumps(self.definition(), sort_keys=True)))
        if self._carrier_output is not None:
            arrays['reference_tail_carrier_sha256'] = np.array(self._carrier_output['sha256'])
        return arrays


class ReferenceTailMixin:
    def __init__(self, *args, tail_context, **kwargs):
        self.reference_tail_context = tail_context
        self._reference_ready = False
        super().__init__(*args, **kwargs)
        context = self.reference_tail_context
        if self.P == len(context.plan.cells):
            profiles = context._build_tables(self.lift_scalar)
        elif self.P == context.plan.legacy_count and context._profiles is not None:
            if not np.array_equal(self.lift_scalar, context._old_profiles[:self.P]):
                raise ValueError('Observed and native old lifts differ on their literal shared rows')
            profiles = context._profiles[:self.P]
        else:
            raise ValueError('Build the all-observation object before its native structural template')
        self.lift_scalar9 = profiles
        self.lift_scalar = profiles[:, :6]
        self._reference_ready = True
        self.clear_base()

    def _old_lift(self, s):
        return super()._lift_scalar(float(s))

    def _lift_scalar(self, s):
        if not self._reference_ready:
            return self._old_lift(s)
        context = self.reference_tail_context
        node = context._node_indices.get(float(s))
        if node is not None:
            return context._profiles[2*node, :6].copy()
        if not 0 <= s <= self.S:
            raise ValueError('Reference lift query lies outside the original radial domain')
        cell = min(self.J-2, max(0, int(np.searchsorted(self.mesh, s, side='right')-1)))
        u = (float(s)-self.mesh[cell])/(self.mesh[cell+1]-self.mesh[cell])
        return self.lift_at(cell, float(np.clip(u, 0., 1.)))[:6].copy()

    def lift_at(self, cell, u):
        cell, u = int(cell), float(u)
        context = self.reference_tail_context
        context._point_definition(cell, u)  # Explicit domain validation.
        key = (cell, u)
        if key not in context._point_profiles:
            s = float(self.mesh[cell]+(self.mesh[cell+1]-self.mesh[cell])*u)
            profile = context.mix_profile(self._old_lift(s), cell, u, s)
            profile.setflags(write=False)
            context._point_profiles[key] = profile
        return context._point_profiles[key]

    def _first_batch_uncached(self, p, start, stop):
        V, d = super()._first_batch_uncached(p, start, stop)
        V[:, :, 2] += self.lift_scalar9[start:stop, 7, None]
        return V, d

    def _first(self, p, stage):
        V, d = self._first_batch(p, stage, stage+1)
        return V[0], d[0]

    def _reference_triplet(self, jets, start, stop):
        if hasattr(self, '_stage_all'):
            values = self._stage_all(jets, start, stop)
        else:
            values = np.stack([self.stage_jets(jets, j) for j in range(start, stop)])
        return values[:, 0], values[:, 1], values[:, 2]

    def _reference_synth(self, y):
        c = self._trig_values(np.stack((y[:, :self.M+1], y[:, 2*self.M+1:]), axis=1), 'cos')
        s = self._trig_values(y[:, self.M+1:2*self.M+1], 'sin')
        out = np.empty((len(y), self.N, 3), dtype=np.result_type(y.dtype, float))
        out[:, :, 0], out[:, :, 1], out[:, :, 2] = c[:, 0], s, c[:, 1]
        return out

    def _reference_angular_second(self, y):
        M, nu = self.M, self.freq
        c = np.zeros((len(y), 2, M+1), dtype=np.result_type(y.dtype, float))
        c[:, 0, 0] = -y[:, 0]
        c[:, 0, 1:] = -(1+nu*nu)*y[:, 1:M+1]-2*nu*y[:, M+1:2*M+1]
        c[:, 1, 1:] = -nu*nu*y[:, 2*M+2:]
        s = -(1+nu*nu)*y[:, M+1:2*M+1]-2*nu*y[:, 1:M+1]
        cv, sv = self._trig_values(c, 'cos'), self._trig_values(s, 'sin')
        out = np.empty((len(y), self.N, 3), dtype=c.dtype)
        out[:, :, 0], out[:, :, 1], out[:, :, 2] = cv[:, 0], sv, cv[:, 1]
        return out

    def physical_fields_batch(self, p, start, stop):
        y, u, acc = self._reference_triplet(p.jets, start, stop)
        lift = self.lift_scalar9[start:stop]
        F = self._reference_synth(y)+lift[:, 3, None, None]*p.er[None]
        F[:, :, 2] += lift[:, 0, None]*p.height+lift[:, 6, None]
        V, d = self._first_batch(p, start, stop)
        ss, sp = self._linear_fields(u, acc)
        ss += lift[:, 5, None, None]*p.er[None]
        ss[:, :, 2] += lift[:, 2, None]*p.height+lift[:, 8, None]
        sp += lift[:, 4, None, None]*(p.rho[:, None]*p.et)[None]
        pp = self._reference_angular_second(y)
        pp += lift[:, 3, None, None]*(p.rho_phi[:, None]*p.et-p.rho[:, None]**2*p.er)[None]
        return dict(F=F, Fs=V, Fphi=d, Fss=ss, Fsphi=sp, Fphiphi=pp)

    def physical_jet_batch(self, p, start, stop):
        return self.physical_fields_batch(p, start, stop)

    def six_jets(self, p, stage):
        return {key: value[0] for key, value in self.physical_fields_batch(p, stage, stage+1).items()}

    def observation_metadata(self):
        parent = getattr(super(), 'observation_metadata', None)
        result = parent() if parent is not None else dict(
            legacy_stages=self.P, total_stages=self.P, full_angles=self.full_N,
            evaluated_angles=self.N, free_variables=self.free_size,
            radial_stage_weights_implicit=False, geometry_certified=False)
        result.update(original_affine_space_preserved=False,
            original_free_coordinates_preserved=True, representation='R671 exact reference tail lift',
            reference_lift_model_identity_sha256=canonical_sha(self.reference_tail_context.definition()),
            gauss_polynomial_exactness_claimed=False, geometry_certified=False)
        return result

    def affine_diagnostics(self, x):
        result = super().affine_diagnostics(x)
        # The last Gauss row is not the cap. The original endpoint is in
        # the retained legacy prefix, at its literal node-stage index.
        terminal = 2*(self.J-1)
        result.update(lift_core_three_jets_exact_zero=bool(np.all(self.lift_scalar9[0] == 0)),
            lift_terminal_radial_three_jets=self.lift_scalar9[terminal, 3:6].tolist(),
            lift_terminal_height_multiplier_three_jets=self.lift_scalar9[terminal, :3].tolist(),
            lift_terminal_fixed_height_three_jets=self.lift_scalar9[terminal, 6:].tolist(),
            terminal_node_stage=terminal, representation=SCHEMA,
            original_free_coordinates_preserved=True, old_certificates_inherited=False)
        return result


def fields_block_observed(o, p, start, stop):
    """New full six-jet adapter; lambda=0 delegates to the old formulas."""
    if hasattr(o, 'physical_fields_batch'):
        return o.physical_fields_batch(p, start, stop)
    result = o.physical_jet_batch(p, start, stop)
    y, _ = o._stage_pair(p.jets, start, stop)
    cv = o._trig_values(np.stack((y[:, :o.M+1], y[:, 2*o.M+1:]), axis=1), 'cos')
    sv = o._trig_values(y[:, o.M+1:2*o.M+1], 'sin')
    F = np.empty((len(y), o.N, 3), dtype=np.result_type(y.dtype, float))
    F[:, :, 0], F[:, :, 1], F[:, :, 2] = cv[:, 0], sv, cv[:, 1]
    F += o.lift_scalar[start:stop, 3, None, None]*p.er[None]
    F[:, :, 2] += o.lift_scalar[start:stop, 0, None]*p.height
    result['F'] = F
    return result


class _PointView:
    def __init__(self, original, cell, phi, weights, lift):
        self.original = original
        self.phi = np.array([phi]); self.N = self.P = 1
        self.observation_cells = np.array([cell], dtype=int)
        self.observation_weights = np.asarray(weights)[None]
        self.lift_scalar = np.asarray(lift[:6])[None]
    def __getattr__(self, name):
        return getattr(self.original, name)


def _point_context(problem, prepared, cell, u, phi, observed_module):
    cell, u, phi = int(cell), float(u), float(phi)
    if not np.isfinite(phi):
        raise ValueError('Need a finite point angle')
    lift = problem.lift_at(cell, u)
    weights = observed_module.hermite_weights(problem.mesh[cell+1]-problem.mesh[cell], u)
    co, si = np.cos(problem.freq*phi), np.sin(problem.freq*phi)
    rho = 1+co@(problem.qfreq*prepared.core)
    rhop = -si@(problem.freq*problem.qfreq*prepared.core)
    delta = si@((problem.qfreq/problem.freq)*prepared.core)
    er = np.array([np.cos(delta), np.sin(delta), 0.])
    et = np.array([-np.sin(delta), np.cos(delta), 0.])
    p = SimpleNamespace(rho=np.array([rho]), rho_phi=np.array([rhop]), er=er[None], et=et[None])
    view = _PointView(problem, cell, phi, weights, lift)
    return view, p, co, si, weights, lift


def _new_fields_at(problem, prepared, cell, u, phi, observed_module):
    _, p, co, si, weights, lift = _point_context(problem, prepared, cell, u, phi, observed_module)
    q, M, nu = problem, problem.M, problem.freq
    co0 = np.r_[1., co]
    y, v, acc = weights@prepared.jets[int(cell):int(cell)+2].reshape(6, q.n)
    def synth(a):
        return np.array([co0@a[:M+1], si@a[M+1:2*M+1], co0@a[2*M+1:]])
    def angular(a, order=1):
        r, t, z = a[:M+1], a[M+1:2*M+1], a[2*M+1:]
        R, T = co0@r, si@t
        Rp, Tp, Zp = -si@(nu*r[1:]), co@(nu*t), -si@(nu*z[1:])
        if order == 1:
            return np.array([Rp-T, Tp+R, Zp])
        return np.array([-co@(nu*nu*r[1:])-2*Tp-R,
                         -si@(nu*nu*t)+2*Rp-T, -co@(nu*nu*z[1:])])
    h, hp, hpp, f, fp, fpp, k, kp, kpp = lift
    er, et, rho, rhop = p.er[0], p.et[0], p.rho[0], p.rho_phi[0]
    F, V, ss = synth(y)+f*er, synth(v)+fp*er, synth(acc)+fpp*er
    F[2] += h*prepared.height+k
    V[2] += hp*prepared.height+kp
    ss[2] += hpp*prepared.height+kpp
    return dict(F=F, Fs=V, Fphi=angular(y)+f*rho*et,
        Fss=ss, Fsphi=angular(v)+fp*rho*et,
        Fphiphi=angular(y, 2)+f*(rhop*et-rho*rho*er))


def point_adapter(original):
    """Isolated copy of the existing point module, with correct new fields.

    Its original exact pullback needs only the new first six scalar
    columns. All functions are rebound into the isolated namespace, so
    witness/row routines call these new arbitrary-point functions too.
    The imported original module and every source file stay unchanged.
    """
    original = load(original, 'point')
    adapter_name = original.__name__+'_reference_tail'
    module = ModuleType(adapter_name)
    namespace = module.__dict__
    namespace.update(original.__dict__)
    namespace['__name__'] = adapter_name
    for name, value in list(original.__dict__.items()):
        if isinstance(value, FunctionType) and value.__globals__ is original.__dict__:
            rebound = FunctionType(value.__code__, namespace, name, value.__defaults__, value.__closure__)
            rebound.__kwdefaults__ = value.__kwdefaults__
            rebound.__dict__.update(value.__dict__)
            namespace[name] = rebound
    legacy_fields, legacy_pullback = original.fields_at, original.pullback_at
    def fields_at(problem, prepared, cell, u, phi, observed_module):
        if not hasattr(problem, 'reference_tail_context'):
            return legacy_fields(problem, prepared, cell, u, phi, observed_module)
        return _new_fields_at(problem, prepared, cell, u, phi, observed_module)
    def pullback_at(problem, prepared, cell, u, phi, cotangent, observed_module):
        if not hasattr(problem, 'reference_tail_context'):
            return legacy_pullback(problem, prepared, cell, u, phi, cotangent, observed_module)
        view, p, _, _, _, _ = _point_context(problem, prepared, cell, u, phi, observed_module)
        return namespace['pullback'](view, p, 0, 0, cotangent)
    namespace.update(fields_at=fields_at, pullback_at=pullback_at,
        reference_tail_adapter_source_sha256=sha(__file__),
        reference_tail_original_source=source_record(original))
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--carrier', type=Path, required=True)
    parser.add_argument('--node-report', type=Path, required=True)
    parser.add_argument('--scalar-input', type=Path, required=True)
    parser.add_argument('--eta-start-node', type=int, required=True)
    parser.add_argument('--lambda-value', type=float, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--dense-source', type=Path)
    parser.add_argument('--batch-source', type=Path)
    parser.add_argument('--observed-source', type=Path)
    parser.add_argument('--scalar-source', type=Path)
    parser.add_argument('--integer-source', type=Path)
    parser.add_argument('--hold-source', type=Path)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--write-seed', choices=('keep-q', 'nodal-projection'))
    parser.add_argument('--source-lambda', type=float, default=0.)
    a = parser.parse_args()
    started = time.monotonic()
    topic = a.repo.resolve()/'topics/visible-flex-larger-amplitude'
    source_dir = topic/'scripts/resume_20261120'
    a.outdir = a.outdir.resolve()
    a.outdir.mkdir(parents=True, exist_ok=False)
    context = TailLiftContext.from_files(bundle=a.bundle, carrier=a.carrier,
        node_report=a.node_report, scalar_input=a.scalar_input,
        observed_source=a.observed_source or source_dir/'gauss_observed_closed_gram.py',
        scalar_source=a.scalar_source or topic/'notes/2026-11-17-parallel-model-full-hold-oracle.py',
        integer_source=a.integer_source or topic/'notes/2026-11-17-parallel-inward-integral-enclosure.py',
        hold_source=a.hold_source or topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py',
        eta_start_node=a.eta_start_node, lambda_value=a.lambda_value)
    problem, _ = context.create_pair(
        a.dense_source or topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        a.batch_source or topic/'scripts/resume_20261120_batched_closed_gram.py',
        N=a.angles, stage_block=a.stage_block, quarter=True)
    carrier = context.save_carrier(a.outdir/'reference-tail-carrier.npz', a.outdir/'reference-tail-carrier.json')
    report = dict(schema=SCHEMA+'-materialization', source_sha256=sha(__file__),
        carrier=carrier, model=context.metadata(), nonlinear_solve_performed=False,
        actual_field_screening_performed=False, old_certificates_inherited=False)
    if a.write_seed:
        x, affine = problem.pack(context.data['qjets'], float(context.data['Hcap']), require_affine=True)
        x, transfer = context.transfer_seed(problem, x, source_lambda=a.source_lambda, mode=a.write_seed)
        seed = a.outdir/'new-representation-seed.npz'
        np.savez_compressed(seed, **context.bundle_arrays(problem, x))
        report.update(seed=dict(path=str(seed), sha256=sha(seed), affine=affine, transfer=transfer,
            accepted=False, needs_true_Gram_and_geometry_readout=True))
    report['seconds'] = time.monotonic()-started
    output = a.outdir/'report.json'
    output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(event='reference_tail_materialized', report=str(output),
        report_sha256=sha(output), model_identity_sha256=canonical_sha(context.definition()),
        lambda_value=a.lambda_value, seconds=report['seconds'],
        field_screening_performed=False)), flush=True)


if __name__ == '__main__':
    main()
