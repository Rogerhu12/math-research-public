"""All-core plus three-geometry-parameter actual-prefix class factory.

The actual nonlinear tail methods are attached outside this module.  This
class keeps all M core coefficients as boundary unknowns, adds physical
delta/LB/vp offsets, and appends three actual core constraints.  Its saved
material and numerical reference charts and representation gauge are fixed;
the physical prefix metric changes when a geometry control changes.
"""
from __future__ import annotations
import gc
import math
from types import SimpleNamespace
import numpy as np
import root_radial_batching as radial


LAYOUT = ('p[0:M]=all core parameters: log(c2/gauge), (c4-reference_c4)/scale[0], '
          'c6+/scale[1:]; p[M:M+3]=physical delta,boost_length,boost_speed offsets')
GEOMETRY_CONTROLS = ('delta', 'boost_length', 'boost_speed')


def make_augmented(source_factory, utility, adaptive, charts, chart, reference,
                   raw_record, raw_values, target, provenance, warm=None,
                   external_shifts=None):
    """Return a base for Actual, whose final bc_jac must be replaced explicitly.

    raw_values are the exact accepted baseline x/y/p; they are not re-labelled
    as an accepted solution after any target, field or profile change.  A
    tangent warm carries the full fixed-J field and all-core parameter part,
    plus a separate physical three-control increment.
    """
    Base = utility.make_fixed(SimpleNamespace(make_dual=source_factory),
        adaptive, charts, chart, reference['chart_reference_coefficients'],
        reference['chart_reference_frequencies'])
    baseline_profile = dict(reference['frozen_profile'])
    baseline_gauge = float(reference['gauge_amplitude'])
    baseline_reference = np.asarray(reference['chart_reference_coefficients'], float)
    baseline_frequencies = list(reference['chart_reference_frequencies'])
    reference_t = np.asarray(raw_record['identity']['numerical_reference_knots'], float)
    target = np.asarray(target, float).copy()
    external_shifts = dict(external_shifts or {})
    base_profile = {**baseline_profile,
        **{name: baseline_profile[name]+value for name, value in external_shifts.items()}}
    if target.shape != (3,) or not np.isfinite(target).all() or target[0] <= 0:
        raise ValueError('Three finite actual low-core targets are required')

    class Augmented(Base):
        def __init__(self, cfg, port, q, M, angular):
            # Parent all-knots initialization constructs a Flow immediately.
            self.ref_frequencies = baseline_frequencies.copy()
            self._augmented_initial_geometry_key = None
            if cfg != base_profile or float(q) != baseline_gauge:
                raise ValueError('The explicit design base or representation gauge changed')
            if M != int(reference['modes']) or angular != int(reference['config']['angular']):
                raise ValueError('This continuation preserves the accepted M/N; use a separate refinement')
            super().__init__(cfg, port, q, M, angular)
            self.fixed = False
            self.second_control = 'boost_length'
            self.ref_coeff = baseline_reference.copy()
            self.ref_frequencies = baseline_frequencies.copy()
            self.controls = np.zeros(M+3)
            self._special_layout = LAYOUT
            self._neck_knots = reference_t.copy()
            self.chart_breaks = reference_t.copy()
            self._flow = None
            self._flow_key = None
            self._core_key = None
            self._initial = None
            self._augmented_initial_geometry_key = None
            self._strong_target = target.copy()
            self._strong_constraint_weights = np.r_[q, self.pscale[:2]]
            self.design_provenance = dict(provenance)
            self.design_provenance.update(parameter_layout=LAYOUT,
                all_core_coefficients_unknown=True,
                prescribed_actual_low_core=target.tolist(),
                geometric_control_order=list(GEOMETRY_CONTROLS),
                constraint_weights=self._strong_constraint_weights.tolist(),
                physical_metric_frozen=False,
                fixed_external_profile_shifts=external_shifts,
                material_angle_reference_preserved=True,
                numerical_reference_knots_preserved=True)
            for key in ('parameters', 'cut'):
                if self.port[key] != reference['physical_tail_'+('parameters' if key == 'parameters' else 'cut')]:
                    raise ValueError('The physical tail '+key+' changed')
            # Before a tangent/profile deformation, the same t must map to
            # the old physical s exactly up to the constructor's roundoff.
            initial_flow = self.flow()
            if not external_shifts:
                old_breaks = np.asarray(reference['numerical_meridian_chart']['physical_s'])
                if (len(initial_flow.breaks) != len(old_breaks)
                        or np.max(abs(initial_flow.breaks-old_breaks)) > 2e-13):
                    raise ValueError('The baseline physical knots do not reproduce')

        def make_flow(self, *args, **kwargs):
            # Dual.__init__ temporarily assigns its own default reference.
            # Always restore the explicit immutable material reference before
            # constructing any actual Flow, including that first one.
            self.ref_coeff = baseline_reference.copy()
            self.ref_frequencies = baseline_frequencies.copy()
            return super().make_flow(*args, **kwargs)

        def select(self, p):
            p = np.asarray(p, float)
            if p.ndim != 1 or len(p) not in (self.M, self.M+3):
                raise ValueError('Unexpected all-core plus geometry parameter layout')
            # Length M occurs only in the inherited constructor; the actual
            # BVP seed and every callback use exactly M+3 parameters.
            self.controls = p.copy()

        def geometry_offsets(self):
            return (np.asarray(self.controls[self.M:self.M+3], float)
                    if len(self.controls) == self.M+3 else np.zeros(3))

        def flow(self, unused_p0=0.):
            key = tuple(map(float, self.geometry_offsets()))
            if getattr(self, '_flow_key', None) != key or getattr(self, '_flow', None) is None:
                physical = dict(self.cfg)
                for name, value in zip(GEOMETRY_CONTROLS, key):
                    physical[name] = float(self.cfg[name]+value)
                if not .002 < physical['delta'] < 1.:
                    raise FloatingPointError('The actual delta control left its physical domain')
                if not physical['boost_length'] > 0.:
                    raise FloatingPointError('The actual boost length is nonpositive')
                if not physical['vu'] < physical['boost_speed'] < 1.:
                    raise FloatingPointError('The actual boost speed left its angle-profile domain')
                self._flow = self.Flow(physical, self.port, self.M, self.q,
                    self.nt, self.base_mode, self.bridge)
                self._flow_key = key
            return self._flow

        def actual_coefficients(self, p):
            p = np.asarray(p, float)
            result = np.r_[self.q*math.exp(float(p[0])), p[1:self.M]*self.pscale]
            result[1] += self.ref_coeff[1]
            return result

        def initial(self, p):
            self.select(p)
            geometry_key = tuple(self.geometry_offsets())
            if geometry_key != self._augmented_initial_geometry_key:
                self._core_key = None
                self._initial = None
            value = super().initial(np.asarray(p[:self.M], float))
            if self._initial_jac.shape == (self.n, self.M):
                self._initial_jac = np.pad(self._initial_jac, ((0, 0), (0, 3)))
            elif self._initial_jac.shape != (self.n, self.M+3):
                raise ValueError('The inherited analytic all-core inlet Jacobian has changed')
            self._augmented_initial_geometry_key = geometry_key
            return value

        def fun(self, t, y, p):
            self.select(p)
            f = self.flow()
            s, ds = self.chart(t, 0.)
            return ds[None, :]*radial.value(f, s, y, p)

        def fun_jac(self, t, y, p):
            self.select(p)
            baseline_flow, baseline_key = self.flow(), self._flow_key
            s, ds = self.chart(t, 0.)
            state = radial.state_jacobian(baseline_flow, s, y, p)
            state *= ds[None, None, :]
            parameter = np.zeros((self.n, self.M+3, len(t)))
            try:
                for local, name in enumerate(GEOMETRY_CONTROLS):
                    j = self.M+local
                    step = 1e-6*max(.1, abs(self.cfg[name]+p[j]))
                    plus, minus = p.copy(), p.copy()
                    plus[j] += step
                    minus[j] -= step
                    parameter[:, j] = (self.fun(t, y, plus)-self.fun(t, y, minus))/(2*step)
            finally:
                self.select(p)
                self._flow, self._flow_key = baseline_flow, baseline_key
                gc.collect()
            # First M direct RHS columns are zero: core coefficients are
            # boundary data. The three geometry columns include ds/dt and
            # physical s(t), not just an autonomous physical-flow derivative.
            return state, parameter

        def bc(self, ya, yb, p):
            self.select(p)
            inlet = ya-self.initial(p)
            terminal = self.terminal(yb, p)
            constraints = (self.actual_coefficients(p)[:3]-self._strong_target)/self._strong_constraint_weights
            return np.r_[inlet, terminal, constraints]

        def augmented_bc_jac(self, ya, yb, p):
            self.select(p)
            self.initial(p)
            f, key = self.flow(), self._flow_key
            rows, columns = self.n+self.M+3, self.M+3
            A = np.zeros((rows, self.n))
            A[:self.n] = np.eye(self.n)
            B = np.zeros_like(A)
            P = np.zeros((rows, columns))
            P[:self.n] = -self._initial_jac
            J, _ = f.fun_jac(np.array([f.end]), np.asarray(yb, np.longdouble)[:, None], p)
            _, height_jac = self.tail_boundary(yb)
            if np.shape(height_jac) != (self.M, self.M):
                raise ValueError('The actual tail slope derivative must retain the complete H vector')
            T = self.q*J[self.iz:, :, 0]
            T[:, self.iz:] -= self.q*self.bridge.sigma*height_jac/math.sqrt(self.port['cut']['E'])
            B[self.n:self.n+self.M] = T/self.bcweights[:, None]
            core_units = np.r_[self.actual_coefficients(p)[0], self.pscale[:2]]
            P[-3:, :3] = np.diag(core_units/self._strong_constraint_weights)
            try:
                for local, name in enumerate(GEOMETRY_CONTROLS):
                    j = self.M+local
                    step = 2e-6*max(.1, abs(self.cfg[name]+p[j]))
                    plus, minus = p.copy(), p.copy()
                    plus[j] += step
                    minus[j] -= step
                    # The whole boundary residual is differentiated; no
                    # unverified zero terminal or inlet design column is used.
                    P[:, j] = (self.bc(ya, yb, plus)-self.bc(ya, yb, minus))/(2*step)
            finally:
                self.select(p)
                self._flow, self._flow_key = f, key
                self.initial(p)
                gc.collect()
            return A, B, P

        def seed(self, nodes):
            raise ValueError('This actual continuation requires its explicit accepted full-field restart')

        def restart_from(self, saved, pullback, nodes, warm_scale):
            if nodes != 0 or warm_scale != 'none':
                raise ValueError('Use nodes=0 and warm-scale=none for exact accepted-mesh continuation')
            if saved.rec['core']['coefficients'] != reference['core']['coefficients']:
                raise ValueError('The physical restart is not the complete accepted reference')
            x, y = raw_values['x'].copy(), raw_values['y'].copy()
            old_p = raw_values['p']
            p = np.r_[old_p[:self.M], np.zeros(3)]
            if not np.array_equal(self.actual_coefficients(p), reference['core']['coefficients']):
                raise ValueError('All-core parameter units fail to reproduce the accepted core')
            if not np.array_equal(self._neck_knots, raw_record['identity']['numerical_reference_knots']):
                raise ValueError('The accepted numerical reference chart changed')
            record = dict(scope='Exact accepted raw fields on their recorded numerical reference; subsequent tangent steps are a new-design warm guess only.',
                prior_parameter_count=len(old_p), parameter_count=len(p),
                all_prior_core_parameters_retained=True, geometry_offsets_rebased_to_frozen_physical_profile=True,
                old_and_new_gauge=self.q, amplitude_scaling='none',
                raw_mesh_retained_bitwise=True, nominal_field_retained_before_tangent=True,
                numerical_reference_knots_retained_bitwise=True,
                actual_target_core=self._strong_target.tolist(), physical_design_changed=True,
                final_acceptance_bypassed=False)
            if warm is not None:
                direction = np.asarray(warm['fixed_parameter_and_field_increment'])
                nm = y.size
                if direction.shape != (nm+self.M,):
                    raise ValueError('The fixed-J full-field tangent shape differs')
                y += direction[:nm].reshape(y.shape, order='F')
                p[:self.M] += direction[nm:]
                p[self.M:] = warm['geometry_increment']
                # A linear log-parameter prediction does not enforce the
                # physical c2 target exactly. This explicit warm-only inlet
                # correction also enforces the other two prescribed targets.
                p[0] = math.log(self._strong_target[0]/self.q)
                p[1] = (self._strong_target[1]-self.ref_coeff[1])/self.pscale[0]
                p[2] = self._strong_target[2]/self.pscale[1]
                self.select(p)
                f = self.flow()
                s, _ = self.chart(x, 0.)
                correction = self.initial(p)-y[:, 0]
                y += correction[:, None]*np.maximum(0., 1-s/(f.Tu/2))[None, :]**3
                record['whole_field_actual_tangent'] = warm['provenance']
                record['warm_inlet_correction_max'] = float(np.max(abs(correction)))
            self.select(p)
            self.initial(p)
            record['warm_physical_profile'] = dict(self.flow().cfg)
            record['warm_actual_core'] = self.actual_coefficients(p).tolist()
            self.design_provenance['accepted_raw_restart_conversion'] = record
            return x, y, p, record

    return Augmented
