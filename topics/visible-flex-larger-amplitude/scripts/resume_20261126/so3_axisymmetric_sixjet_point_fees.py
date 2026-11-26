#!/usr/bin/env python3
"""Complete same-field six-jet and relative Gram fees at actual observations.

The actual full 7f26 operator is reread. Exact rational reconstruction of
its component working words pays every remaining arithmetic and batch
reevaluation difference. True h/h'/h'', closure, core/cap, signed meridian
integrals, direct meridian jets and target denominator all retain their
independent outward errors. Finite observation certification is explicitly
separate from continuous-surface and all-family geometry certification.
Scientific execution belongs only to this public repository Actions.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid

TOPIC = 'topics/visible-flex-larger-amplitude'
SCHEMA = 'actual-complete-hDelta-sixjet-and-point-Gram-fees-v1'
REQUEST_SCHEMA = 'actual-hDelta-sixjet-literal-observation-requests-v1'
NODE_SHA = '1371e4936af27d2122a84bb720e8c67db5d0db712df42eec12a4579f91943f89'
CORE_SHA = '69c5aae0dea9c15645a4484b3e4bfe9d6809f2a922763ca91c623774fd1e4bb2'
INTEGRAL_SHA = '1a46002ad6b1763479340b4f16472983c88d4f11c6530ce5465f78bfc64c3c4b'
OPERATOR_SHA = '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'
LOW_ORDER_SHA = '30ae7dc70ea836ab6f30e34b9b886f968c6e61c6646c807cd96a8611029c2636'
JET_KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')
INTEGRAL_KEYS = ('T', 'Tp', 'Tpp')
CORE_KEYS = ('Gamma', 'Gammaphi', 'Gammaphiphi')
CAP_KEYS = ('P', 'Pphi', 'Pphiphi')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Complete same-field scientific fees require the public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def load(name, path, expected):
    if sha(path) != expected:
        raise ValueError('Use the complete byte-bound dependency '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def exact(value):
    if isinstance(value, F):
        return value
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Every actual working word must be finite')
    return F(value)


def serialize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item) for item in value]
    if hasattr(value, 'tolist'):
        return serialize(value.tolist())
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('A nonfinite working result cannot be a certified record')
    return value


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(serialize(value), indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


class CompleteSixJetPointFees:
    """Same exact field, complete working arithmetic, finite actual points."""
    def __init__(self, actual, node, core_cap, integrals):
        require_actions()
        for component, expected in ((node, NODE_SHA), (core_cap, CORE_SHA),
                (integrals, INTEGRAL_SHA)):
            module = sys.modules.get(component.__class__.__module__)
            if module is None or sha(module.__file__) != expected:
                raise ValueError('A complete fee component has the wrong actual source')
        if (node.actual is not actual or core_cap.actual is not actual
                or core_cap.node is not node or integrals.actual is not actual
                or integrals.node is not node or integrals.q is not node.q):
            raise ValueError('Every component must share this complete actual field and numerical operator')
        self.actual, self.node, self.core, self.integrals = actual, node, core_cap, integrals
        self.q, self.x, self.op = node.q, node.x, node.operator_module
        self.np, self.d, self.k = self.op.np, node.d, node.kernel
        if (sha(self.q.fields_torch.__func__.__code__.co_filename) != OPERATOR_SHA
                or sha(self.k.__file__) != LOW_ORDER_SHA
                or self.q.identity != actual.identity or self.q.model != actual.model):
            raise ValueError('The actual full field/source/low-order algebra changed')
        carrier = actual.inputs['carrier']['path']
        if sha(carrier) != actual.inputs['carrier']['sha256']:
            raise ValueError('The actual target observation carrier changed')
        with self.np.load(carrier, allow_pickle=False) as saved:
            av = self.np.array(saved['a_observations'], copy=True)
            ae = self.np.array(saved['a_observation_absolute_error'], copy=True)
            scalar_identity = str(saved['fixed_scalar_metric_identity_sha256'].item())
        if (av.shape != (self.q.P,) or ae.shape != av.shape
                or not self.np.isfinite(av).all() or not self.np.isfinite(ae).all()
                or self.np.any(ae < 0) or not self.np.array_equal(av, self.q.a)
                or scalar_identity != actual.profile):
            raise ValueError('Bind every same-target observation and its original outward evaluation error')
        self.a_boxes = tuple((F(float(a))-F(float(e)), F(float(a))+F(float(e)))
            for a, e in zip(av, ae))
        if any(lo <= 0 or hi < lo for lo, hi in self.a_boxes):
            raise ValueError('Each true same-target observation denominator needs a strict positive scalar bound')
        self.current_phi = None
        self.core_read = None
        self.counts = dict(actual_full_sixjet_calls=0, actual_full_Gram_evaluations=0,
            certified_observation_angle_pairs=0, closure_working_reads=0,
            exact_h_evaluations=0, full_J_calls=0, full_Jtranspose_calls=0)
        self.maxima = {key: F(0) for key in JET_KEYS}
        self.maximum_Gram_fee = F(0)
        self.maximum_true_Gram_upper = F(0)
        self.maximum_true_Gram_lower = F(0)
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            actual=actual.binding, node_source_sha256=NODE_SHA,
            core_cap_source_sha256=CORE_SHA, integral_source_sha256=INTEGRAL_SHA,
            operator_source_sha256=OPERATOR_SHA, low_order_source_sha256=LOW_ORDER_SHA,
            node_binding_identity_sha256=canonical(node.binding),
            core_cap_binding_identity_sha256=canonical(core_cap.binding),
            integral_binding_identity_sha256=canonical(integrals.binding),
            actual_target_observation_input=actual.inputs['carrier'],
            target_interval_source='4e65 actual outward a_observation_absolute_error literal upper words',
            true_metric='diag(1,(a_deep(s)*rho0(phi))^2) in the original fixed material chart',
            complete_hDelta_field=True, zero_closure_assumed=False,
            original_solver_batch_bitwise_identity_assumed=False,
            working_offdiagonal_is_f_not_sqrt2f=True,
            physical_Gram_without_angle_orbit_multiplicity=True,
            scope='Actual finite original observation addresses, with all six field fees. No continuous interpolation.')

    def norm(self, values):
        return self.k.sqrt_upper(sum((exact(v)*exact(v) for v in values), F(0)))

    def distance(self, numeric, reference):
        return self.norm([F(float(a))-exact(b) for a, b in zip(numeric, reference)])

    def _h(self, cell, local):
        """Exact h on alpha*S+beta: retain cancellation in s/S=alpha+beta/S."""
        d = self.d
        u = F(float(local))
        alpha, beta = self.node.continuous.affine(self.actual.context.nodes, int(cell), u)
        S = self.node.scalar.exact_affine_box((F(1), F(0)))
        inverse = d.inverse(S)
        t = d.add(d.box(alpha), d.scale(inverse, beta))
        def polynomial(coefficients):
            answer = d.ZERO
            for value in reversed(coefficients):
                answer = d.add(d.mul(answer, t), d.box(value))
            return answer
        h = polynomial((1, 0, 0, -10, 15, -6))
        hp = d.mul(polynomial((0, 0, -30, 60, -30)), inverse)
        hpp = d.mul(polynomial((0, -60, 180, -120)), d.mul(inverse, inverse))
        self.counts['exact_h_evaluations'] += 1
        return dict(h=h, hp=hp, hpp=hpp,
            exact_affine_definition=(alpha, beta), true_S_box=S,
            exact_ratio_box=t, scalar_carrier_differences_not_assumed_zero=True)

    def _box_fee(self, box, carrier):
        word = F(float(carrier))
        return max(abs(F(box[0], self.d.SCALE)-word), abs(F(box[1], self.d.SCALE)-word))

    def prepare_core(self, phi, *, root_tolerance=F(1, 10**24), max_root_iterations=80):
        """The integration component must already have all same-angle cells."""
        require_actions()
        angles = self.core._angles(phi)
        if (not self.integrals.complete
                or [float(v).hex() for v in angles]
                   != [float(v).hex() for v in self.integrals.phi]):
            raise ValueError('The complete meridian quadrature and core/cap need identical literal angles')
        # query() independently refuses an incomplete integral preparation.
        self.core_read = self.core.evaluate(angles, root_tolerance=root_tolerance,
            max_root_iterations=max_root_iterations)
        self.current_phi = angles.copy()
        return self.core_read

    def _closure(self, query):
        """Actual 7f26 sum order, compared with exact words plus total quadrature."""
        result, errors, norms = {}, {}, {}
        with self.op.torch.no_grad():
            for j, key in enumerate(INTEGRAL_KEYS):
                values = self.integrals.integrated_working[key]
                _, total = self.q._integrate(self.op.tensor(values), query)
                C = self.op.tensor(self.core_read['working'][CORE_KEYS[j]])
                P = self.op.tensor(self.core_read['working'][CAP_KEYS[j]])
                words = self.np.array((C-P+total).detach().numpy(), copy=True)
                if words.shape != (len(self.current_phi), 3) or not self.np.isfinite(words).all():
                    raise FloatingPointError('Every actual closure jet must be a finite full vector')
                result[key] = words
                fees = self.np.empty(len(self.current_phi), dtype=object)
                true_norms = self.np.empty(len(self.current_phi), dtype=object)
                for a in range(len(self.current_phi)):
                    reference = [F(float(self.core_read['working'][CORE_KEYS[j]][a, k]))
                        -F(float(self.core_read['working'][CAP_KEYS[j]][a, k]))
                        +self.integrals.total_exact[key][a, k] for k in range(3)]
                    fees[a] = self.distance(words[a], reference)
                    total_error = (self.core_read['norm_error_upper'][CORE_KEYS[j]][a]
                        +self.core_read['norm_error_upper'][CAP_KEYS[j]][a]
                        +self.integrals.total_error[key][a]+fees[a])
                    true_norms[a] = self.norm([F(float(v)) for v in words[a]])+total_error
                errors[key], norms[key] = fees, true_norms
        self.counts['closure_working_reads'] += 1
        return dict(working=result, arithmetic_errors=errors, true_norm_uppers=norms)

    def _observation_indices(self, indices):
        raw = self.np.asarray(indices)
        if raw.ndim != 1 or not len(raw) or raw.dtype.kind not in ('i', 'u'):
            raise ValueError('Use explicit original observation integer indices')
        if self.np.any(raw < 0) or self.np.any(raw >= self.q.P):
            raise ValueError('An observation index lies outside the original complete 7377-point array')
        return self.np.array(raw, dtype=self.np.int64, copy=True)

    def evaluate(self, observation_indices):
        """All six fees and physical 2x2 Gram enclosures for requested points."""
        require_actions()
        if self.current_phi is None or self.core_read is None:
            raise ValueError('Prepare the complete same-angle integrals and certified core/cap first')
        if (not self.integrals.complete
                or [float(v).hex() for v in self.current_phi]
                   != [float(v).hex() for v in self.integrals.phi]):
            raise ValueError('The integral angle block changed after core preparation; prepare both again')
        indices = self._observation_indices(observation_indices)
        cells, local = self.q.observation_cells[indices], self.q.observation_u[indices]
        signed = self.integrals.query(cells, local)
        query = signed['query']
        direct = self.node.evaluate(cells, local, self.current_phi)
        closure = self._closure(query)
        P, A = len(indices), len(self.current_phi)
        with self.op.torch.no_grad():
            tensors = self.q.fields_torch(self.op.tensor(self.x), query, self.current_phi,
                curvature=True, query_label='arbitrary')
            full = {key: self.np.array(tensors[key].detach().numpy(), copy=True) for key in JET_KEYS}
            denominator = self.op.tensor(self.q.a[indices])[:, None]*tensors['rho0'][None]
            V, W = tensors['Fs'], tensors['Fphi']
            gram = self.op.torch.stack(((V*V).sum(-1)-1,
                (V*W).sum(-1)/denominator,
                (W*W).sum(-1)/(denominator*denominator)-1), -1)
            working_Gram = self.np.array(gram.detach().numpy(), copy=True)
            working_denominator = self.np.array(denominator.detach().numpy(), copy=True)
        if (any(value.shape != (P, A, 3) or not self.np.isfinite(value).all() for value in full.values())
                or working_Gram.shape != (P, A, 3) or not self.np.isfinite(working_Gram).all()
                or working_denominator.shape != (P, A)
                or not self.np.isfinite(working_denominator).all()
                or self.np.any(working_denominator <= 0)):
            raise FloatingPointError('The actual complete six jets, denominator and three Gram entries must be finite')
        hwords = {key: self.np.array(query[key].detach().numpy(), copy=True).reshape(P)
            for key in ('h', 'hp', 'hpp')}
        fees = {key: self.np.empty((P, A), dtype=object) for key in JET_KEYS}
        arithmetic = {key: self.np.empty((P, A), dtype=object) for key in JET_KEYS}
        gram_fees = self.np.empty((P, A), dtype=object)
        gram_arithmetic = self.np.empty((P, A), dtype=object)
        gram_upper = self.np.empty((P, A), dtype=object)
        gram_lower = self.np.empty((P, A), dtype=object)
        true_denominators = [[None for _ in range(A)] for _ in range(P)]
        h_enclosures, detailed = [], []
        for p, (cell, u, index) in enumerate(zip(cells, local, indices)):
            htruth = self._h(int(cell), float(u))
            h_enclosures.append(htruth)
            h, hp, hpp = [F(float(hwords[key][p])) for key in ('h', 'hp', 'hpp')]
            herr = {key: self._box_fee(htruth[key], hwords[key][p]) for key in ('h', 'hp', 'hpp')}
            for a in range(A):
                for j, key in enumerate(('F', 'Fphi', 'Fphiphi')):
                    C = self.core_read['working'][CORE_KEYS[j]][a]
                    cap = self.core_read['working'][CAP_KEYS[j]][a]
                    exact_combination = [h*F(float(C[k]))+(1-h)*F(float(cap[k]))
                        +signed['signed_exact'][INTEGRAL_KEYS[j]][p, a, k] for k in range(3)]
                    arithmetic[key][p, a] = self.distance(full[key][p, a], exact_combination)
                for key, meridian, derivative, delta in (
                        ('Fs', 'T', hp, 'T'), ('Fsphi', 'Tp', hp, 'Tp'),
                        ('Fss', 'Ts', hpp, 'T')):
                    exact_combination = [F(float(direct['working'][meridian][p, a, k]))
                        +derivative*F(float(closure['working'][delta][a, k])) for k in range(3)]
                    arithmetic[key][p, a] = self.distance(full[key][p, a], exact_combination)
                propagation = self.k.complete_field_error(
                    h_carrier=h, hp_carrier=hp, hpp_carrier=hpp,
                    h_error=herr['h'], hp_error=herr['hp'], hpp_error=herr['hpp'],
                    core_jet_errors=[self.core_read['norm_error_upper'][key][a] for key in CORE_KEYS],
                    cap_jet_errors=[self.core_read['norm_error_upper'][key][a] for key in CAP_KEYS],
                    total_integral_errors=[self.integrals.total_error[key][a] for key in INTEGRAL_KEYS],
                    closure_arithmetic_errors=[closure['arithmetic_errors'][key][a] for key in INTEGRAL_KEYS],
                    field_integral_errors=[signed['signed_error'][key][p, a] for key in INTEGRAL_KEYS],
                    delta_norm_uppers=[closure['true_norm_uppers'][key][a] for key in INTEGRAL_KEYS],
                    direct_T_error=direct['norm_error_upper']['T'][p, a],
                    direct_Ts_error=direct['norm_error_upper']['Ts'][p, a],
                    direct_Tphi_error=direct['norm_error_upper']['Tp'][p, a],
                    field_arithmetic_errors={key: arithmetic[key][p, a] for key in JET_KEYS})
                for key in JET_KEYS:
                    fees[key][p, a] = propagation['six_jet_norm_errors'][key]
                    self.maxima[key] = max(self.maxima[key], fees[key][p, a])
                # The target is a_deep times the FIXED rho0. The actual
                # denominator carrier is the true full-field call's word.
                rho = tuple(F(self.core_read['fixed_chart']['rho0'][j][a], self.d.SCALE)
                    for j in (0, 1))
                alo, ahi = self.a_boxes[int(index)]
                if rho[0] <= 0:
                    # Intersect the local box with the independent all-circle
                    # fixed-chart positive certificate without dropping width.
                    cert = self.core.certificates['fixed']
                    rho = (max(rho[0], cert['lower']), min(rho[1], cert['upper']))
                if not 0 < rho[0] <= rho[1]:
                    raise ArithmeticError('The true local and all-circle fixed chart bounds disagree')
                target_box = (alo*rho[0], ahi*rho[1])
                true_denominators[p][a] = target_box
                denom = F(float(working_denominator[p, a]))
                fs = [F(float(v)) for v in full['Fs'][p, a]]
                fp = [F(float(v)) for v in full['Fphi'][p, a]]
                exact_Gram = (sum(v*v for v in fs)-1,
                    sum(v*w for v, w in zip(fs, fp))/denom,
                    sum(w*w for w in fp)/(denom*denom)-1)
                difference = [F(float(w))-r for w, r in zip(working_Gram[p, a], exact_Gram)]
                # Complete operator-norm arithmetic fee, not one scalar entry.
                gram_arithmetic[p, a] = max(abs(difference[0])+abs(difference[1]),
                    abs(difference[1])+abs(difference[2]))
                gram_propagation = self.k.relative_gram_error(
                    Fs_hat_norm_upper=self.norm(fs), Fphi_hat_norm_upper=self.norm(fp),
                    Fs_error=fees['Fs'][p, a], Fphi_error=fees['Fphi'][p, a],
                    target_denominator_interval=target_box,
                    target_denominator_carrier=denom,
                    numerical_Gram_arithmetic_error=gram_arithmetic[p, a])
                gram_fees[p, a] = gram_propagation['spectral_norm_error']
                e, f, g = [F(float(v)) for v in working_Gram[p, a]]
                radius = self.k.sqrt_upper((e-g)**2+4*f*f)
                numerical_upper = (abs(e+g)+radius)/2
                numerical_lower = (abs(e+g)+max(F(0), radius-F(1, 1 << 96)))/2
                gram_upper[p, a] = numerical_upper+gram_fees[p, a]
                gram_lower[p, a] = max(F(0), numerical_lower-gram_fees[p, a])
                self.maximum_Gram_fee = max(self.maximum_Gram_fee, gram_fees[p, a])
                self.maximum_true_Gram_upper = max(self.maximum_true_Gram_upper, gram_upper[p, a])
                self.maximum_true_Gram_lower = max(self.maximum_true_Gram_lower, gram_lower[p, a])
                detailed.append(dict(observation_index=int(index), angle_block_index=a,
                    h_errors=herr, field_propagation=propagation, Gram_propagation=gram_propagation))
        self.counts['actual_full_sixjet_calls'] += 1
        self.counts['actual_full_Gram_evaluations'] += P*A
        self.counts['certified_observation_angle_pairs'] += P*A
        return dict(schema=SCHEMA, binding_identity_sha256=canonical(self.binding),
            observation_indices=indices, cells=cells, local_u_hex=[float(v).hex() for v in local],
            phi_hex=[float(v).hex() for v in self.current_phi],
            actual_working_six_jets=full, six_jet_norm_errors=fees,
            complete_remaining_six_jet_arithmetic_errors=arithmetic,
            actual_closure_working=closure['working'],
            closure_arithmetic_errors=closure['arithmetic_errors'],
            true_closure_norm_uppers=closure['true_norm_uppers'],
            true_h_enclosures=h_enclosures, detailed_point_fee_algebra=detailed,
            actual_working_physical_relative_Gram=working_Gram,
            actual_working_denominator=working_denominator,
            true_target_denominator_intervals=true_denominators,
            normalized_Gram_spectral_error_upper=gram_fees,
            complete_Gram_arithmetic_error_upper=gram_arithmetic,
            true_relative_Gram_norm_lower=gram_lower, true_relative_Gram_norm_upper=gram_upper,
            every_six_jet_term_and_target_evaluation_fee_paid=True,
            signed_partial_quadrature_and_mass_defect_retained=True,
            exact_radial_E_equals_one_assumed=False,
            old_solver_batch_words_assumed_identical=False,
            angle_orbit_multiplicity_in_physical_Gram=False,
            continuous_surface_metric_certified=False, continuous_geometry_certified=False,
            closed_isometry_accepted=False)

    def metadata(self):
        return dict(schema=SCHEMA, binding=self.binding, binding_identity_sha256=canonical(self.binding),
            actual_counts=dict(self.counts), maximum_processed_six_jet_errors=(dict(self.maxima)
                if self.counts['certified_observation_angle_pairs'] else None),
            maximum_processed_Gram_spectral_fee=(self.maximum_Gram_fee
                if self.counts['certified_observation_angle_pairs'] else None),
            maximum_processed_true_Gram_norm_upper=(self.maximum_true_Gram_upper
                if self.counts['certified_observation_angle_pairs'] else None),
            maximum_processed_true_Gram_norm_lower=(self.maximum_true_Gram_lower
                if self.counts['certified_observation_angle_pairs'] else None),
            all_original_variables_and_target_coefficients_retained=True,
            processed_points_not_promoted_to_continuous_surface=True,
            continuous_metric_or_geometry_certified=False, closed_isometry_accepted=False)


def requests(component, path, *, angle_block, observation_block):
    q, np = component.q, component.np
    if path is None:
        indices = np.arange(q.P, dtype=np.int64)
        angles = q.phi.copy()
        scope = 'all original observation addresses and all original quarter-orbit working angles'
        source = None
    else:
        raw = json.loads(Path(path).read_text())
        if raw.get('schema') != REQUEST_SCHEMA:
            raise ValueError('Use the explicit original-observation literal-angle request schema')
        if (not isinstance(raw.get('observation_indices'), list)
                or any(isinstance(v, bool) or not isinstance(v, int) for v in raw['observation_indices'])):
            raise ValueError('Use explicit original integer observation indices without coercion')
        indices = component._observation_indices(raw['observation_indices'])
        angles = component.core._angles([float.fromhex(v) for v in raw['phi_hex']])
        if [float(v).hex() for v in angles] != raw['phi_hex']:
            raise ValueError('Every requested angle must use its canonical literal binary64 spelling')
        scope = 'only the explicitly listed original observation addresses and literal angles'
        source = file_record(path)
    if (len(set(int(v) for v in indices)) != len(indices)
            or len(set(float(v).hex() for v in angles)) != len(angles)):
        raise ValueError('A declared finite coverage plan must not duplicate addresses')
    full_original = np.array_equal(indices, np.arange(q.P)) and np.array_equal(angles, q.phi)
    plan = dict(scope=scope, request_file=source,
        observation_indices=[int(v) for v in indices], phi_hex=[float(v).hex() for v in angles],
        same_exact_original_observation_addresses=True,
        all_original_observations_and_angle_orbits=bool(full_original),
        full_N=int(q.full_N), quarter_working_angles=int(q.N),
        original_observations=int(q.P), requested_point_pairs=len(indices)*len(angles),
        angle_block=angle_block, observation_block=observation_block,
        traversal='angle block outer, original requested observation block inner')
    blocks = [(a, min(a+angle_block, len(angles)), p, min(p+observation_block, len(indices)))
        for a in range(0, len(angles), angle_block) for p in range(0, len(indices), observation_block)]
    return indices, angles, blocks, plan


def main(args):
    require_actions()
    started = time.monotonic()
    args.repo, args.outdir = args.repo.resolve(), args.outdir.resolve()
    if args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('Full scientific reports and raw journals must remain outside the repository')
    source = args.repo/TOPIC/'scripts/resume_20261126'
    node_module = load('_complete_sixjet_actual_nodes', source/'so3_axisymmetric_outward_nodes.py', NODE_SHA)
    core_module = load('_complete_sixjet_actual_core_cap', source/'so3_axisymmetric_core_cap_outward.py', CORE_SHA)
    integral_module = load('_complete_sixjet_actual_signed_integrals',
        source/'so3_actual_signed_meridian_integrals.py', INTEGRAL_SHA)
    actual = node_module.load_actual(args)
    cache = args.outdir.parent/(args.outdir.name+'-working-cache-'+uuid.uuid4().hex)
    node = node_module.NodeOutwardEvaluator(actual, working_cache_directory=cache, exp_order=args.exp_order)
    core = core_module.CoreCapOutward(actual, node)
    integrals = integral_module.SignedMeridianIntegrals(actual, node,
        envelope_report=args.envelope_report, envelope_journal=args.envelope_journal)
    component = CompleteSixJetPointFees(actual, node, core, integrals)
    indices, angles, blocks, plan = requests(component, args.requests,
        angle_block=args.angle_block, observation_block=args.observation_block)
    identity = dict(schema=SCHEMA, source_sha256=sha(__file__),
        actual_component_binding_sha256=canonical(component.binding),
        query_plan_sha256=canonical(plan), root_tolerance=str(args.root_tolerance),
        max_root_iterations=args.max_root_iterations, rho_max_leaves=args.rho_max_leaves)
    chain = canonical(identity)
    report_path, journal = args.outdir/'report.json', args.outdir/'point-blocks.jsonl'
    processed, pairs = 0, 0
    maxima = {key: F(0) for key in JET_KEYS}
    gram_fee, gram_upper, gram_lower = F(0), F(0), F(0)
    if args.outdir.exists():
        if not args.resume or not report_path.is_file() or not journal.is_file():
            raise ValueError('Resume only an explicit existing complete-bound point journal')
        previous = json.loads(report_path.read_text())
        if previous['identity'] != identity or previous['query_plan'] != plan:
            raise ValueError('The source, actual field, exact target or declared finite coverage changed')
        with journal.open() as stream:
            for line in stream:
                entry = json.loads(line)
                record = entry['record']
                if (processed >= len(blocks) or record['block'] != processed
                        or tuple(record['block_address']) != blocks[processed]
                        or entry['previous_record_identity_sha256'] != chain
                        or entry['record_identity_sha256'] != canonical(dict(previous=chain, record=record))):
                    raise ValueError('The exact finite-point coverage journal is missing or reordered')
                raw_path = Path(record['raw_record']['path']).resolve()
                if (raw_path.parent != args.outdir/'raw-point-blocks'
                        or sha(raw_path) != record['raw_record']['sha256']):
                    raise ValueError('A previously completed raw same-field point block changed')
                payload = json.loads(gzip.decompress(raw_path.read_bytes()))
                a, b, p, q = blocks[processed]
                if (payload['schema'] != SCHEMA
                        or payload['binding_identity_sha256'] != canonical(component.binding)
                        or payload['observation_indices'] != [int(v) for v in indices[p:q]]
                        or payload['phi_hex'] != [float(v).hex() for v in angles[a:b]]
                        or payload['every_six_jet_term_and_target_evaluation_fee_paid'] is not True
                        or payload['continuous_surface_metric_certified'] is not False):
                    raise ValueError('A raw point block does not retain the same complete actual provenance and scope')
                for key in JET_KEYS:
                    computed = max(F(value) for row in payload['six_jet_norm_errors'][key] for value in row)
                    if computed != F(record['maxima'][key]):
                        raise ValueError('A processed six-jet maximum changed')
                    maxima[key] = max(maxima[key], computed)
                for field, scalar in (('normalized_Gram_spectral_error_upper', 'maximum_Gram_fee'),
                        ('true_relative_Gram_norm_upper', 'maximum_true_Gram_upper'),
                        ('true_relative_Gram_norm_lower', 'maximum_true_Gram_lower')):
                    computed = max(F(value) for row in payload[field] for value in row)
                    if computed != F(record[scalar]):
                        raise ValueError('A processed physical Gram maximum changed')
                gram_fee = max(gram_fee, F(record['maximum_Gram_fee']))
                gram_upper = max(gram_upper, F(record['maximum_true_Gram_upper']))
                gram_lower = max(gram_lower, F(record['maximum_true_Gram_lower']))
                pairs += int(record['point_pairs'])
                chain, processed = entry['record_identity_sha256'], processed+1
    else:
        if args.resume:
            raise ValueError('An explicit point resume requires its existing actual journal')
        args.outdir.mkdir(parents=True)
        journal.write_text('')
    raw_directory = args.outdir/'raw-point-blocks'
    raw_directory.mkdir(exist_ok=True)
    source_commit = subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip()
    initial_processed = processed
    failure = None
    charts = previous.get('full_circle_core_certificates') if args.resume else None
    preparation = None
    current_angle_start = None

    def save():
        complete = processed == len(blocks) and failure is None
        value = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit,
            identity=identity, identity_sha256=canonical(identity), query_plan=plan,
            actual_binding=actual.binding, complete=complete,
            complete_declared_finite_observation_scope=complete,
            completed_blocks=processed, requested_blocks=len(blocks),
            processed_point_pairs=pairs, requested_point_pairs=plan['requested_point_pairs'],
            newly_completed_blocks=processed-initial_processed,
            processed_six_jet_error_maxima=maxima if pairs else None,
            processed_Gram_error_maximum=gram_fee if pairs else None,
            processed_true_Gram_norm_maximum_upper=gram_upper if pairs else None,
            processed_true_Gram_norm_maximum_lower=gram_lower if pairs else None,
            requested_finite_scope_Gram_upper=gram_upper if complete else None,
            requested_finite_scope_meets_metric_threshold=bool(complete and gram_upper <= args.metric_threshold),
            processed_point_refutes_metric_threshold=bool(pairs and gram_lower > args.metric_threshold),
            metric_threshold_exact=args.metric_threshold,
            full_surface_metric_threshold_certified=False,
            partial_points_not_promoted_to_full_scope=not complete,
            point_journal=file_record(journal), journal_chain_sha256=chain,
            latest_complete_integral_preparation=preparation,
            full_circle_core_certificates=charts,
            current_component_metadata=component.metadata(),
            current_component_counts_are_this_execution_only=True,
            resumed_completed_blocks_not_recomputed_as_new_science=initial_processed,
            actual_seconds=time.monotonic()-started, admission_seconds=args.admission_seconds,
            working_cache_path=str(cache), failure=failure,
            no_missing_component_error_assumed_zero=True,
            continuous_metric_or_geometry_certified=False, closed_isometry_accepted=False,
            execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
                run_id=os.environ.get('GITHUB_RUN_ID'), attempt=os.environ.get('GITHUB_RUN_ATTEMPT')))
        write_json(report_path, value)
        return value

    save()
    try:
        if processed < len(blocks):
            charts = core.certify_charts(max_leaves=args.rho_max_leaves,
                admission_seconds=min(args.rho_admission_seconds,
                    max(0., args.admission_seconds-(time.monotonic()-started))))
            save()
        while processed < len(blocks) and charts['both_certified_positive']:
            if time.monotonic()-started >= args.admission_seconds:
                break
            a, b, p, q = blocks[processed]
            if current_angle_start != a:
                directory = args.outdir/('integrals-angle-'+str(a).zfill(7))
                remaining = max(0., args.admission_seconds-(time.monotonic()-started))
                preparation = integrals.prepare(angles[a:b], journal_directory=directory,
                    resume=directory.exists(), admission_seconds=remaining)
                save()
                if not preparation['complete']:
                    break
                component.prepare_core(angles[a:b], root_tolerance=args.root_tolerance,
                    max_root_iterations=args.max_root_iterations)
                current_angle_start = a
                if time.monotonic()-started >= args.admission_seconds:
                    break
            block_started = time.monotonic()
            payload = component.evaluate(indices[p:q])
            for key in JET_KEYS:
                maxima[key] = max(maxima[key], max(payload['six_jet_norm_errors'][key].flat))
            block_fee = max(payload['normalized_Gram_spectral_error_upper'].flat)
            block_upper = max(payload['true_relative_Gram_norm_upper'].flat)
            block_lower = max(payload['true_relative_Gram_norm_lower'].flat)
            gram_fee, gram_upper, gram_lower = max(gram_fee, block_fee), max(gram_upper, block_upper), max(gram_lower, block_lower)
            raw_path = raw_directory/('block-'+str(processed).zfill(7)+'.json.gz')
            if raw_path.exists():
                raise ValueError('Never overwrite an already produced complete raw point block')
            raw = json.dumps(serialize(payload), separators=(',', ':'), allow_nan=False).encode()
            temporary = raw_path.with_name(raw_path.name+'.partial')
            temporary.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
            temporary.replace(raw_path)
            record = dict(block=processed, block_address=[a, b, p, q],
                point_pairs=(b-a)*(q-p), raw_record=file_record(raw_path),
                maxima={key: str(max(payload['six_jet_norm_errors'][key].flat)) for key in JET_KEYS},
                maximum_Gram_fee=str(block_fee), maximum_true_Gram_upper=str(block_upper),
                maximum_true_Gram_lower=str(block_lower),
                actual_block_seconds=time.monotonic()-block_started,
                node_counts_after_actual_read=dict(node.counts),
                full_operator_counts_after_actual_read=dict(component.q.counts))
            next_chain = canonical(dict(previous=chain, record=record))
            with journal.open('a') as stream:
                stream.write(json.dumps(dict(previous_record_identity_sha256=chain,
                    record_identity_sha256=next_chain, record=record), separators=(',', ':'), allow_nan=False)+'\n')
                stream.flush()
                os.fsync(stream.fileno())
            chain, processed, pairs = next_chain, processed+1, pairs+record['point_pairs']
            save()
            print(json.dumps(dict(event='complete_actual_sixjet_point_block',
                completed_blocks=processed, requested_blocks=len(blocks),
                processed_point_pairs=pairs, maximum_true_Gram_upper=str(gram_upper),
                maximum_Gram_fee=str(gram_fee), block_seconds=record['actual_block_seconds']),
                separators=(',', ':'), allow_nan=False), flush=True)
    except Exception as exc:
        failure = dict(type=type(exc).__name__, message=str(exc), next_block=processed)
        save()
        raise
    report = save()
    print(json.dumps(dict(event='complete_actual_sixjet_point_admission_returned',
        complete=report['complete'], completed_blocks=processed, requested_blocks=len(blocks),
        processed_point_pairs=pairs, report_sha256=sha(report_path),
        actual_seconds=report['actual_seconds'], continuous_surface_certified=False),
        separators=(',', ':'), allow_nan=False), flush=True)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'report', 'checkpoint', 'reference-bundle', 'carrier', 'node-report',
                 'scalar-input', 'preparation-report', 'envelope-report', 'envelope-journal', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--state', choices=('initial', 'final'), default='final')
    p.add_argument('--panels', type=int, default=128)
    p.add_argument('--exp-order', type=int, default=24)
    p.add_argument('--requests', type=Path)
    p.add_argument('--angle-block', type=int, default=8)
    p.add_argument('--observation-block', type=int, default=32)
    p.add_argument('--rho-max-leaves', type=int, default=4096)
    p.add_argument('--rho-admission-seconds', type=float, default=120.)
    p.add_argument('--root-tolerance', type=F, default=F(1, 10**24))
    p.add_argument('--max-root-iterations', type=int, default=80)
    p.add_argument('--metric-threshold', type=F, default=F(1, 10**6))
    p.add_argument('--admission-seconds', type=float, default=600.)
    p.add_argument('--resume', action='store_true')
    args = p.parse_args()
    if (args.panels < 1 or args.exp_order < 2 or args.angle_block < 1
            or args.observation_block < 1 or args.rho_max_leaves < 1
            or args.max_root_iterations < 0 or args.root_tolerance <= 0
            or args.metric_threshold <= 0
            or any(not math.isfinite(v) or v <= 0 for v in (args.admission_seconds, args.rho_admission_seconds))):
        raise ValueError('Use explicit positive arithmetic, physical threshold and natural-return budgets')
    return args


if __name__ == '__main__':
    main(parse_args())
