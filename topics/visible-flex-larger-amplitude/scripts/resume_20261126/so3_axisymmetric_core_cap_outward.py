#!/usr/bin/env python3
"""Whole-angle core positivity, inverse chart and six core/cap outward fees.

This component uses one complete actual 606e/7f26 hDelta field and the complete
actual-node evaluator. It proves positivity on the entire circle, then encloses
the unique real inverse lift at each literal requested phi. Every working value
is reread by the actual 7f26 _core_and_cap; its difference from the true box pays
all numerical inverse, trigonometric, scalar-carrier and arithmetic errors.
It does not certify the remaining meridian integrals, a Gram matrix or geometry.
Scientific execution is restricted to the authorized public repository Actions.
"""
import argparse
from fractions import Fraction as F
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

SCHEMA = 'actual-whole-circle-core-inverse-cap-outward-v1'
REQUEST_SCHEMA = 'actual-core-cap-literal-angle-requests-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
NODE_RELATIVE = 'scripts/resume_20261126/so3_axisymmetric_outward_nodes.py'
NODE_SHA = '1371e4936af27d2122a84bb720e8c67db5d0db712df42eec12a4579f91943f89'
CONTINUOUS_SHA = 'a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6'
OPERATOR_SHA = '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'
REFERENCE_SHA = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
KEYS = ('Gamma', 'Gammaphi', 'Gammaphiphi', 'P', 'Pphi', 'Pphiphi')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific core/cap enclosures require this public repository Actions')


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
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))


def load(name, path, expected):
    if sha(path) != expected:
        raise ValueError('Changed complete source '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


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
        raise ValueError('Do not serialize nonfinite working values')
    return value


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(serialize(value), indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


class CoreCapOutward:
    """All-circle certificates and finite-angle actual core/cap error consumer.

    Call certify_charts() before evaluate(phi). The current and fixed core
    certificates are separate even if their literal coefficients coincide.
    evaluate returns six float64 (A,3) working arrays, corresponding pairs of
    integer object arrays, and exact Fraction Euclidean error arrays of shape A.
    fixed_chart.rho0 is a pair of integer arrays of shape A. Fractions denote
    exact rationals; all integer boxes use the actual e091 SCALE.
    """
    def __init__(self, actual, evaluator):
        require_actions()
        module = sys.modules.get(evaluator.__class__.__module__)
        actual_module = sys.modules.get(actual.__class__.__module__)
        if (module is None or sha(module.__file__) != NODE_SHA
                or actual_module is None or sha(actual_module.__file__) != CONTINUOUS_SHA
                or evaluator.actual is not actual):
            raise ValueError('Use the complete bound node evaluator and its original ActualInput')
        self.actual, self.node, self.node_module = actual, evaluator, module
        self.q, self.x = evaluator.q, evaluator.x
        self.op = evaluator.operator_module
        self.np = self.op.np
        self.d, self.kernel = evaluator.d, evaluator.kernel
        if (sha(self.q._core_and_cap.__func__.__code__.co_filename) != OPERATOR_SHA
                or sha(actual.paths['operator']) != OPERATOR_SHA
                or sha(actual.paths['reference']) != REFERENCE_SHA
                or self.q.model != actual.model or self.q.identity != actual.identity):
            raise ValueError('The actual current core/cap operator or complete field identity changed')
        core, omega, height = self.q.unpack(self.x)
        if (not self.np.array_equal(core, actual.data['core'])
                or not self.np.array_equal(omega, actual.omega)
                or not self.np.array_equal(self.q.parent_core, actual.context.core)
                or height != float(actual.data['Hcap'])):
            raise ValueError('Use every unchanged current core/omega/H and the actual fixed chart')
        self.core = tuple(F(float(v)) for v in core)
        self.fixed_core = tuple(F(float(v)) for v in actual.context.core)
        self.height = F(height)
        self.core_words = [float(v).hex() for v in core]
        self.fixed_words = [float(v).hex() for v in actual.context.core]
        radius_record = actual.context.model['radius_complete_enclosure']
        self.radius_exact = (F(radius_record['lower_exact']), F(radius_record['upper_exact']))
        if not 0 < self.radius_exact[0] <= self.radius_exact[1]:
            raise ValueError('The same complete scalar target must supply a positive true cap-radius enclosure')
        self.radius = self.d.box(*self.radius_exact)
        self.certificates = {}
        self.rho_states = {}
        self.counts = dict(rho_exact_L1_reads=0, rho_angle_cell_enclosures=0,
            inverse_equation_enclosures=0, inverse_interval_Newton_steps=0,
            working_core_cap_calls=0, working_angle_vectors=0,
            certified_angle_vectors=0, full_F_reads=0, full_J_reads=0,
            full_Jtranspose_reads=0)
        self.maximum_errors = {key: F(0) for key in KEYS}
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            node_source_sha256=NODE_SHA, continuous_input_source_sha256=CONTINUOUS_SHA,
            actual_operator_source_sha256=OPERATOR_SHA, actual_reference_source_sha256=REFERENCE_SHA,
            actual=actual.binding, node_binding_identity_sha256=canonical(evaluator.binding),
            complete_current_core_binary64_hex=self.core_words,
            complete_fixed_chart_core_binary64_hex=self.fixed_words,
            current_H_binary64_hex=height.hex(),
            same_target_radius_complete_enclosure=radius_record,
            actual_working_R_binary64_hex=float(self.q.R).hex(),
            radius_enclosure_source='actual complete 4e65 reference model, unchanged fixed scalar profile',
            interval_scale=str(self.d.SCALE),
            gamma_frame='ordinary normal frame at the certified current inverse phi_c, never er(Theta_c(phi_c))',
            cap_frame='fixed original er(theta0(phi)) and et(theta0(phi))',
            scalar_target_reintegrated_by_this_component=False,
            numeric_read_scope='fresh actual 7f26 core/cap arrays; prior solver batches are not assumed bitwise identical')

    def _core_identity(self, which):
        if which not in ('current', 'fixed'):
            raise ValueError('Choose the complete current or fixed-chart core')
        return canonical(dict(M=self.actual.M, complete_coefficients_binary64_hex=
            self.core_words if which == 'current' else self.fixed_words))

    def _rho_cell(self, core, low, high):
        # x=phi/pi. The rational partition covers [0,2] exactly; interval pi
        # multiplication covers every true angle of each closed subinterval.
        angle = self.d.mul(self.d.pi_box(), self.d.box(low, high))
        value = self.node.chart_for_core(core,
            (F(angle[0], self.d.SCALE), F(angle[1], self.d.SCALE)))['rho']
        self.counts['rho_angle_cell_enclosures'] += 1
        return dict(low=low, high=high, angle_box=angle, rho_box=value)

    def certify_rho(self, which, *, max_leaves=4096, admission_seconds=120.):
        """Full exact L1 proof or an adaptive complete closed-circle cover.

        This instance can continue its own still-complete partition by calling
        again with a larger explicit budget. No interval value is replaced by a
        sampled minimum. Exhaustion returns a valid cover and no positivity claim.
        """
        require_actions()
        if (max_leaves != int(max_leaves) or max_leaves < 1
                or not math.isfinite(admission_seconds) or admission_seconds < 0):
            raise ValueError('Use explicit finite nonnegative admission and a positive leaf budget')
        identity = self._core_identity(which)
        core = self.core if which == 'current' else self.fixed_core
        spread = sum((abs((1-(2*m)**2)*c) for m, c in enumerate(core, 1)), F(0))
        l1_lower, l1_upper = 1-spread, 1+spread
        self.counts['rho_exact_L1_reads'] += 1
        started = time.monotonic()
        base = dict(which=which, core_identity_sha256=identity,
            actual_checkpoint_sha256=self.actual.inputs['checkpoint']['sha256'],
            actual_fixed_scalar_identity_sha256=self.actual.profile,
            source_sha256=sha(__file__), node_source_sha256=NODE_SHA,
            every_original_core_coefficient_retained=True,
            circle_parameter='phi=pi*x, exact closed x in [0,2]',
            periodic_extension_to_all_real_phi=True,
            exact_L1_lower=l1_lower, exact_L1_upper=l1_upper,
            sampled_minimum_used=False, field_geometry_certified=False)
        if l1_lower > 0:
            result = dict(base, method='exact rational finite-Fourier L1',
                complete=True, all_circle_complete=True, certified_positive=True,
                lower=l1_lower, upper=l1_upper, leaves=0, complete_partition=[],
                stop_reason='strict exact L1 lower bound', seconds=time.monotonic()-started)
        else:
            leaves = self.rho_states.get(which)
            if leaves is None:
                leaves = [self._rho_cell(core, F(0), F(2))]
                self.rho_states[which] = leaves
            reason = None
            while True:
                worst = min(range(len(leaves)), key=lambda j: leaves[j]['rho_box'][0])
                if leaves[worst]['rho_box'][0] > 0:
                    reason = 'all complete-cover leaves have strictly positive lower endpoints'
                    break
                if len(leaves) >= max_leaves:
                    reason = 'explicit leaf admission budget; positivity not proved'
                    break
                if time.monotonic()-started >= admission_seconds:
                    reason = 'natural time admission budget; positivity not proved'
                    break
                old = leaves[worst]
                middle = (old['low']+old['high'])/2
                # Evaluate both children before replacing the parent. At every
                # completed operation the stored partition still covers all phi.
                left = self._rho_cell(core, old['low'], middle)
                right = self._rho_cell(core, middle, old['high'])
                leaves[worst:worst+1] = [left, right]
            ordered = sorted(leaves, key=lambda item: item['low'])
            if (ordered[0]['low'] != 0 or ordered[-1]['high'] != 2
                    or any(a['high'] != b['low'] for a, b in zip(ordered, ordered[1:]))):
                raise ArithmeticError('The exact whole-circle partition has a gap or overlap')
            lower = max(l1_lower, F(min(item['rho_box'][0] for item in ordered), self.d.SCALE))
            upper = min(l1_upper, F(max(item['rho_box'][1] for item in ordered), self.d.SCALE))
            if lower > upper:
                raise ArithmeticError('Independent global core bounds disagree')
            result = dict(base, method='complete integer-Fourier adaptive closed-angle cover',
                complete=True, all_circle_complete=True, certified_positive=lower > 0,
                lower=lower, upper=upper, leaves=len(ordered), complete_partition=ordered,
                stop_reason=reason, seconds=time.monotonic()-started)
        result['certificate_identity_sha256'] = canonical(serialize(result))
        self.certificates[which] = result
        return result

    def certify_charts(self, *, max_leaves=4096, admission_seconds=120.):
        """Pay both current and fixed-chart full-circle positivity proofs."""
        started = time.monotonic()
        current = self.certify_rho('current', max_leaves=max_leaves,
            admission_seconds=admission_seconds)
        fixed = self.certify_rho('fixed', max_leaves=max_leaves,
            admission_seconds=max(0., admission_seconds-(time.monotonic()-started)))
        return dict(current=current, fixed=fixed,
            both_all_circle_complete=current['all_circle_complete'] and fixed['all_circle_complete'],
            both_certified_positive=current['certified_positive'] and fixed['certified_positive'],
            actual_seconds=time.monotonic()-started,
            incomplete_positivity_is_not_a_nonpositivity_certificate=True)

    def _positive_certificates(self):
        for which in ('current', 'fixed'):
            item = self.certificates.get(which)
            if (item is None or item.get('all_circle_complete') is not True
                    or item.get('certified_positive') is not True or item['lower'] <= 0
                    or item['core_identity_sha256'] != self._core_identity(which)):
                raise ValueError('Both actual complete core charts need a true whole-circle positive lower bound')

    def _positive_inverse(self, raw, certificate):
        low = max(F(raw[0], self.d.SCALE), certificate['lower'])
        high = min(F(raw[1], self.d.SCALE), certificate['upper'])
        if not 0 < low <= high:
            raise ArithmeticError('The complete local/global positive rho enclosures disagree')
        # Fraction division avoids losing a tiny but proved positive lower bound
        # through an intermediate fixed-SCALE rounding down to zero.
        return self.d.box(1/high, 1/low), (low, high)

    def _equation(self, point, theta0):
        self.counts['inverse_equation_enclosures'] += 1
        return self.d.sub(self.node.chart_for_core(self.core, point)['theta'], theta0)

    def inverse(self, phi, *, candidate=None, tolerance=F(1, 10**24), max_iterations=80):
        """Unique global real lift of Theta_current(phi_c)=theta0(phi).

        A numerical candidate is just an arbitrary real rational point. It is
        never identified with another 2*pi lift by floating wrap arithmetic.
        The global delta and a true residual prove an initial enclosing interval;
        interval Newton and signed residual brackets preserve that same root.
        """
        require_actions()
        self._positive_certificates()
        phi, tolerance = self.node_module.exact(phi), F(tolerance)
        if tolerance <= 0 or max_iterations != int(max_iterations) or max_iterations < 0:
            raise ValueError('Use a positive exact root radius tolerance and a nonnegative iteration budget')
        fixed = self.node.fixed_chart(phi)
        certificate = self.certificates['current']
        seeds = [phi]
        if candidate is not None:
            value = self.node_module.exact(candidate)
            if value not in seeds:
                seeds.append(value)
        seed_records = []
        for seed in seeds:
            residual = self._equation(seed, fixed['theta'])
            radius = self.d.magnitude(residual)/certificate['lower']
            seed_records.append(dict(point=seed, true_equation_residual_box=residual,
                guaranteed_root_distance_upper=radius))
        chosen = min(seed_records, key=lambda item: item['guaranteed_root_distance_upper'])
        center, radius = chosen['point'], chosen['guaranteed_root_distance_upper']
        box = self.d.box(center-radius, center+radius)
        initial = box
        history = []
        reason = 'explicit interval-Newton iteration budget'
        for iteration in range(int(max_iterations)):
            if F(box[1]-box[0], 2*self.d.SCALE) <= tolerance:
                reason = 'requested exact enclosing radius reached'
                break
            middle = F(box[0]+box[1], 2*self.d.SCALE)
            residual = self._equation(middle, fixed['theta'])
            local_rho = self.node.chart_for_core(self.core,
                (F(box[0], self.d.SCALE), F(box[1], self.d.SCALE)))['rho']
            inverse, positive_rho = self._positive_inverse(local_rho, certificate)
            newton = self.d.sub(self.d.box(middle), self.d.mul(residual, inverse))
            contracted = self.d.intersect(box, newton)
            if residual[0] > 0:
                contracted = self.d.intersect(contracted, (box[0], self.d.box(middle)[1]))
            elif residual[1] < 0:
                contracted = self.d.intersect(contracted, (self.d.box(middle)[0], box[1]))
            history.append(dict(iteration=iteration, old_box=box,
                midpoint=middle, true_midpoint_residual_box=residual,
                complete_positive_derivative_interval=positive_rho,
                interval_Newton_image=newton, new_box=contracted))
            self.counts['inverse_interval_Newton_steps'] += 1
            if contracted == box:
                reason = 'current complete interval arithmetic did not further contract'
                break
            box = contracted
        reached = F(box[1]-box[0], 2*self.d.SCALE) <= tolerance
        if reached:
            reason = 'requested exact enclosing radius reached'
        local = self.node.chart_for_core(self.core,
            (F(box[0], self.d.SCALE), F(box[1], self.d.SCALE)))
        inverse_rho, positive_rho = self._positive_inverse(local['rho'], certificate)
        return dict(phi=phi, root_box=box, initial_root_box=initial,
            initial_candidates=seed_records, chosen_candidate=chosen['point'],
            fixed_chart=fixed, current_rho_box=local['rho'],
            complete_current_positive_rho_interval=positive_rho,
            current_rho_inverse_box=inverse_rho,
            global_current_lower=certificate['lower'], global_fixed_lower=self.certificates['fixed']['lower'],
            true_unique_global_real_lift_enclosed=True, numerical_candidate_accuracy_assumed=False,
            floating_periodic_wrap_used=False, root_radius_tolerance=tolerance,
            root_radius_upper=F(box[1]-box[0], 2*self.d.SCALE),
            tolerance_reached=reached, interval_Newton_history=history, stop_reason=reason)

    def _support(self, normal_angle):
        d = self.d
        support, derivative = d.ONE, d.ZERO
        angle = d.box(*normal_angle)
        for m, coefficient in enumerate(self.core, 1):
            if coefficient == 0:
                continue
            nu = 2*m
            sine, cosine = d.sine_cosine(d.scale(angle, nu))
            support = d.add(support, d.scale(cosine, coefficient))
            derivative = d.add(derivative, d.scale(sine, -nu*coefficient))
        return support, derivative

    def enclose(self, phi, *, candidate=None, root_tolerance=F(1, 10**24), max_root_iterations=80):
        require_actions()
        root = self.inverse(phi, candidate=candidate, tolerance=root_tolerance,
            max_iterations=max_root_iterations)
        d, r = self.d, self.node.rotation
        normal_angle = tuple(F(v, d.SCALE) for v in root['root_box'])
        ordinary_frame = self.node.normal_frame(normal_angle)
        er, et = ordinary_frame['er'], ordinary_frame['et']
        support, support_p = self._support(normal_angle)
        fixed = root['fixed_chart']
        rho0, rhop0 = fixed['rho'], fixed['rho_phi']
        rho02 = r.square(rho0)
        Gamma = r.vadd(r.vmul(support, er), r.vmul(support_p, et))
        Gammaphi = r.vmul(rho0, et)
        Gammapp = r.vadd(r.vmul(rhop0, et),
            r.vmul(d.neg(d.mul(rho02, root['current_rho_inverse_box'])), er))
        ez = (d.ZERO, d.ZERO, d.ONE)
        P = r.vadd(r.vmul(self.radius, fixed['er']), r.vmul(d.box(self.height), ez))
        Pphi = r.vmul(d.mul(self.radius, rho0), fixed['et'])
        Ppp = r.vmul(self.radius, r.vadd(r.vmul(rhop0, fixed['et']),
            r.vmul(d.neg(rho02), fixed['er'])))
        return dict(intervals=dict(Gamma=Gamma, Gammaphi=Gammaphi,
            Gammaphiphi=Gammapp, P=P, Pphi=Pphi, Pphiphi=Ppp),
            inverse=root, fixed_chart=fixed, current_normal_frame=ordinary_frame,
            complete_current_support_box=support, complete_current_support_phi_box=support_p,
            same_target_radius_box=self.radius, exact_current_H=self.height,
            complete_core_cap_enclosure=True, full_field_or_metric_certified=False)

    def _angles(self, phi):
        raw = self.np.asarray(phi)
        if raw.ndim != 1 or not len(raw):
            raise ValueError('Use a nonempty one-dimensional literal angle array')
        values = []
        for value in raw:
            exact = self.node_module.exact(value)
            word = float(value)
            if not math.isfinite(word) or F(word) != exact:
                raise ValueError('evaluate needs literal binary64 angles; use enclose for an arbitrary exact rational')
            values.append(word)
        return self.np.array(values, dtype=self.np.float64)

    def working(self, phi):
        """Fresh same-source complete Gamma/P arrays; no F, J or integral read."""
        require_actions()
        angles = self._angles(phi)
        core, omega, height = self.q.unpack(self.x)
        if (tuple(F(float(v)) for v in core) != self.core or F(height) != self.height
                or not self.np.array_equal(omega, self.actual.omega)
                or tuple(F(float(v)) for v in self.q.parent_core) != self.fixed_core):
            raise ValueError('The bound complete working vector changed before its actual reread')
        with self.op.torch.no_grad():
            core_t, _, height_t = self.q._unpack_torch(self.op.tensor(self.x))
            Gamma, P, rho0 = self.q._core_and_cap(core_t, height_t, angles)
        tensors = dict(zip(KEYS, (*Gamma, *P)))
        values = {key: self.np.array(value.detach().numpy(), dtype=self.np.float64, copy=True)
            for key, value in tensors.items()}
        if any(value.shape != (len(angles), 3) or not self.np.isfinite(value).all()
                for value in values.values()):
            raise FloatingPointError('Every actual core/cap jet must be finite with shape (A,3)')
        rho = self.np.array(rho0.detach().numpy(), dtype=self.np.float64, copy=True)
        if rho.shape != (len(angles),) or not self.np.isfinite(rho).all():
            raise FloatingPointError('The actual fixed-chart rho array must be finite with shape (A,)')
        self.counts['working_core_cap_calls'] += 1
        self.counts['working_angle_vectors'] += len(angles)
        return dict(working=values, working_rho0=rho, phi=angles,
            working_source_sha256=OPERATOR_SHA,
            actual_core_inverse_diagnostics=dict(
                maximum_inverse_root_residual=self.q.maximum_inverse_root_residual,
                minimum_inverse_root_rho=self.q.minimum_inverse_root_rho),
            no_working_trigonometry_or_Newton_accuracy_assumed=True)

    def evaluate(self, phi, *, root_tolerance=F(1, 10**24), max_root_iterations=80):
        require_actions()
        self._positive_certificates()
        read = self.working(phi)
        angles = read['phi']
        shape = (len(angles), 3)
        intervals = {key: (self.np.empty(shape, dtype=object), self.np.empty(shape, dtype=object)) for key in KEYS}
        errors = {key: self.np.empty(shape, dtype=object) for key in KEYS}
        norms = {key: self.np.empty(len(angles), dtype=object) for key in KEYS}
        chart = {key: (self.np.empty(len(angles), dtype=object), self.np.empty(len(angles), dtype=object))
            for key in ('theta0', 'rho0', 'rho0_phi')}
        roots = []
        for a, angle in enumerate(angles):
            # atan2 is merely a finite candidate proposal. The true residual
            # proof does not assume its accuracy or identify different lifts.
            gp = read['working']['Gammaphi'][a]
            proposal = math.atan2(-float(gp[0]), float(gp[1]))
            truth = self.enclose(F(float(angle)), candidate=F(proposal),
                root_tolerance=root_tolerance, max_root_iterations=max_root_iterations)
            roots.append(truth['inverse'])
            for output, field in (('theta0', 'theta'), ('rho0', 'rho'), ('rho0_phi', 'rho_phi')):
                chart[output][0][a], chart[output][1][a] = truth['fixed_chart'][field]
            for key in KEYS:
                component = []
                for j, box in enumerate(truth['intervals'][key]):
                    intervals[key][0][a, j], intervals[key][1][a, j] = box
                    word = F(float(read['working'][key][a, j]))
                    fee = max(abs(F(box[0], self.d.SCALE)-word), abs(F(box[1], self.d.SCALE)-word))
                    errors[key][a, j] = fee
                    component.append(fee)
                norms[key][a] = self.kernel.sqrt_upper(sum((v*v for v in component), F(0)))
                self.maximum_errors[key] = max(self.maximum_errors[key], norms[key][a])
        self.counts['certified_angle_vectors'] += len(angles)
        return dict(working=read['working'], intervals=intervals,
            component_error_upper=errors, norm_error_upper=norms,
            fixed_chart=chart, working_rho0=read['working_rho0'],
            phi=angles, phi_hex=[float(v).hex() for v in angles], shape=shape,
            inverse_certificates=roots,
            both_core_positivity_certificates={key: value['certificate_identity_sha256']
                for key, value in self.certificates.items()},
            all_unique_inverse_roots_enclosed=True,
            all_requested_root_tolerances_reached=all(item['tolerance_reached'] for item in roots),
            component_interval_scale=self.d.SCALE,
            binding_identity_sha256=canonical(self.binding),
            actual_core_inverse_diagnostics=read['actual_core_inverse_diagnostics'],
            entire_working_core_cap_error_paid_by_true_box_to_actual_word=True,
            paid_errors=['all current support coefficients and current inverse lift',
                'all fixed-chart coefficients and derivatives',
                'complete same-target cap-radius enclosure versus its working carrier',
                'actual current H, trigonometric, division, Newton and vector arithmetic'],
            working_values_are_this_complete_reread_only=True,
            full_meridian_integral_Gram_or_geometry_certified=False)

    def metadata(self):
        return dict(schema=SCHEMA, binding=self.binding, binding_identity_sha256=canonical(self.binding),
            actual_counts=dict(self.counts), actual_counts_are_this_execution_only=True,
            working_operator_shared_counts=dict(self.q.counts),
            whole_circle_certificates=self.certificates,
            maximum_core_cap_norm_error_upper=self.maximum_errors,
            all_original_core_coefficients_retained=True,
            previous_solver_working_words_not_assumed_identical=True,
            finite_angle_fees_not_a_continuous_angular_interpolation_certificate=True,
            continuous_metric_or_reach_certified=False, closed_isometry_accepted=False)


def main(args):
    require_actions()
    started = time.monotonic()
    node_path = args.repo.resolve()/TOPIC/NODE_RELATIVE
    node = load('_core_cap_complete_node_evaluator', node_path, NODE_SHA)
    actual = node.load_actual(args)
    if args.outdir.exists():
        raise ValueError('Use a fresh explicit core/cap output directory; never overwrite a certificate')
    args.outdir.mkdir(parents=True)
    cache = args.outdir.parent/(args.outdir.name+'-working-cache-'+uuid.uuid4().hex)
    evaluator = node.NodeOutwardEvaluator(actual, working_cache_directory=cache)
    component = CoreCapOutward(actual, evaluator)
    if args.requests is None:
        angles = evaluator.q.phi.copy()
        request = dict(kind='all actual original working angular addresses',
            phi_hex=[float(v).hex() for v in angles], full_N=evaluator.q.full_N,
            number_of_actual_angles=len(angles))
    else:
        request_data = json.loads(args.requests.read_text())
        if request_data.get('schema') != REQUEST_SCHEMA:
            raise ValueError('Use the explicit literal-angle request schema')
        angles = component.np.array([node.literal_float(v) for v in request_data['phi_hex']],
            dtype=component.np.float64)
        request = dict(kind='explicit literal binary64 angles', request_file=file_record(args.requests),
            phi_hex=[float(v).hex() for v in angles], number_of_actual_angles=len(angles),
            complete_original_angular_grid_not_assumed=True)
    angles = component._angles(angles)
    report_path, journal = args.outdir/'report.json', args.outdir/'angle-blocks.jsonl'
    journal.write_text('')
    source_commit = subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip()
    identity = dict(schema=SCHEMA, source_sha256=sha(__file__),
        actual_binding_identity_sha256=canonical(component.binding), query_plan_sha256=canonical(request),
        root_tolerance=str(args.root_tolerance), max_root_iterations=args.max_root_iterations,
        angle_block=args.angle_block)
    chain = canonical(identity)
    processed = 0
    charts = None
    failure = None

    def save():
        positive = charts is not None and charts['both_certified_positive']
        complete = positive and processed == len(angles) and failure is None
        result = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit,
            identity=identity, identity_sha256=canonical(identity), query_plan=request,
            actual_binding=actual.binding, core_cap=component.metadata(),
            complete=complete, complete_requested_finite_angles=complete,
            actual_processed_angles=processed, requested_angles=len(angles),
            both_whole_circle_positive=positive,
            whole_circle_positivity_does_not_by_itself_certify_the_field=True,
            processed_angle_maxima=component.maximum_errors,
            requested_scope_maxima=component.maximum_errors if complete else None,
            raw_journal=file_record(journal), journal_chain_sha256=chain,
            actual_seconds=time.monotonic()-started, admission_seconds=args.admission_seconds,
            working_cache_path=str(cache), failure=failure,
            all_remaining_integral_and_closed_field_arithmetic_fees_unpaid=True,
            continuous_metric_or_geometry_certified=False, closed_isometry_accepted=False,
            execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
                run_id=os.environ.get('GITHUB_RUN_ID'), attempt=os.environ.get('GITHUB_RUN_ATTEMPT')))
        write_json(report_path, result)
        return result

    save()
    try:
        charts = component.certify_charts(max_leaves=args.rho_max_leaves,
            admission_seconds=min(args.rho_admission_seconds, args.admission_seconds))
        save()
        if charts['both_certified_positive']:
            while processed < len(angles):
                if time.monotonic()-started >= args.admission_seconds:
                    break
                last = min(len(angles), processed+args.angle_block)
                result = component.evaluate(angles[processed:last], root_tolerance=args.root_tolerance,
                    max_root_iterations=args.max_root_iterations)
                record = dict(first_angle=processed, last_angle_exclusive=last, payload=serialize(result))
                next_chain = canonical(dict(previous=chain, record=record))
                with journal.open('a') as stream:
                    stream.write(json.dumps(dict(previous_record_identity_sha256=chain,
                        record_identity_sha256=next_chain, record=record),
                        separators=(',', ':'), allow_nan=False)+'\n')
                    stream.flush()
                    os.fsync(stream.fileno())
                chain, processed = next_chain, last
                save()
                print(json.dumps(dict(event='actual_core_cap_outward_angle_block',
                    completed_angles=processed, requested_angles=len(angles),
                    root_tolerances_reached=result['all_requested_root_tolerances_reached']),
                    separators=(',', ':')), flush=True)
    except Exception as exc:
        failure = dict(type=type(exc).__name__, message=str(exc), next_angle=processed)
        save()
        raise
    report = save()
    print(json.dumps(dict(event='actual_core_cap_component_returned', complete=report['complete'],
        both_whole_circle_positive=report['both_whole_circle_positive'],
        completed_angles=processed, requested_angles=len(angles), report_sha256=sha(report_path),
        actual_seconds=report['actual_seconds'], full_field_or_geometry_certified=False)), flush=True)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'report', 'checkpoint', 'reference-bundle', 'carrier', 'node-report',
                 'scalar-input', 'preparation-report', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--state', choices=('initial', 'final'), default='final')
    p.add_argument('--panels', type=int, default=128)
    p.add_argument('--requests', type=Path)
    p.add_argument('--angle-block', type=int, default=8)
    p.add_argument('--rho-max-leaves', type=int, default=4096)
    p.add_argument('--rho-admission-seconds', type=float, default=120.)
    p.add_argument('--root-tolerance', type=F, default=F(1, 10**24))
    p.add_argument('--max-root-iterations', type=int, default=80)
    p.add_argument('--admission-seconds', type=float, default=600.)
    args = p.parse_args()
    if (args.panels < 1 or args.angle_block < 1 or args.rho_max_leaves < 1
            or args.max_root_iterations < 0 or args.root_tolerance <= 0
            or any(not math.isfinite(v) or v <= 0
                for v in (args.rho_admission_seconds, args.admission_seconds))):
        raise ValueError('Use explicit positive arithmetic and natural-return budgets')
    return args


if __name__ == '__main__':
    main(parse_args())
