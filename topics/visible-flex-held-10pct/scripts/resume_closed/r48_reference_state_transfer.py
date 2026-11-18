"""R48 blockwise continuous state compensation for a genuine R47 endpoint.

This module prepares a callable initial field, not a new quintic or accepted
BVP.  All derivatives returned are physical-s derivatives.  It uses the
actual two finite inlet projections and the original a(s)*chi(s) window.
Only the omitted mean height remains separate; no old primitive is silently
copied and no new primitive is integrated here.

The algebraic identity assumes the same defining Gamma. R47 append-zero
controls provide that definition. Floating core inversion/projection and
arithmetic may differ by mode count; no byte or continuous numerical bound
for the resulting full physical maps is asserted by this source interface.
"""
import numpy as np


WINDOW = (.5, .9)


def checked_modes(value):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or value < 8:
        raise ValueError('The fixed-slot transfer requires integer M>=8')
    return int(value)


def exact(a, b):
    a, b = np.asarray(a, np.float64), np.asarray(b, np.float64)
    return a.shape == b.shape and a.tobytes() == b.tobytes()


def block_indices(old_modes, new_modes):
    """Map [R0,R1..RM,T1..TM,Z1..ZM] to its larger actual blocks."""
    M, N = checked_modes(old_modes), checked_modes(new_modes)
    if N < M:
        raise ValueError('A mode extension cannot remove a retained state column')
    return np.asarray([*range(M+1), *range(N+1, N+M+1),
                       *range(2*N+1, 2*N+M+1)], dtype=int)


def embed_state(values, old_modes, new_modes, axis=0):
    """Copy each original state coefficient without a numerical projection."""
    M, N = checked_modes(old_modes), checked_modes(new_modes)
    values = np.asarray(values)
    if values.ndim == 0:
        raise ValueError('A state array needs its explicit component axis')
    view = np.moveaxis(values, axis, 0)
    if view.shape[0] != 3*M+1:
        raise ValueError('The full old three-block state vector is required')
    out = np.zeros((3*N+1, *view.shape[1:]), dtype=values.dtype)
    out[block_indices(M, N)] = view
    return np.moveaxis(out, 0, axis)


def reference_jets(flow, physical_s):
    """Literal original full-lift h,h',h'' at physical s."""
    s = np.atleast_1d(np.asarray(physical_s, dtype=float))
    if s.ndim != 1 or not np.all(np.isfinite(s)) or np.any(s < 0.) or np.any(s > flow.end):
        raise ValueError('Use finite physical points in the saved common domain')
    aa, av, acc = flow.profile(s)
    lo, hi = WINDOW
    span = (hi-lo)*flow.prefix_end
    if not span > 0.:
        raise ValueError('The original positive full-lift window is required')
    x = np.clip((s-lo*flow.prefix_end)/span, 0., 1.)
    chi = 1-x**3*(10-15*x+6*x*x)
    chip = -30*x*x*(1-x)**2/span
    chipp = -60*x*(1-x)*(1-2*x)/span**2
    return aa*chi, av*chi+aa*chip, acc*chi+2*av*chip+aa*chipp


class EndpointStateTransfer:
    """A continuous R48 initial field sourced from the actual physical PPoly.

    The input new model must have called its original initial(p) at its exact
    copied seed.  No original solver cubic, raw.y or reconstructed fictitious
    derivative is substituted for the saved physical polynomial.
    """

    def __init__(self, mode_model):
        from r47_endpoint_refinement_model import EndpointModeModel
        if not isinstance(mode_model, EndpointModeModel):
            raise TypeError('Use the explicit new endpoint mode-model interface')
        self.model = mode_model
        old = mode_model.anchor
        old.binding.check_files()
        self.old_obj, self.new_obj = old.obj, mode_model.obj
        self.old_flow, self.new_flow = old.flow, mode_model.flow
        self.M, self.N = self.old_obj.M, self.new_obj.M
        self.indices = block_indices(self.M, self.N)
        self.polynomial = old.polynomial
        self.parameters = mode_model.parameters.copy()
        self.old_parameters = np.asarray(old.binding.record['parameters'], float)
        if (self.M != 8 or self.N < 8 or not exact(self.parameters[0], 0.) or
                self.new_obj._core is None or
                self.new_flow.exact_lift_core is not self.new_obj._core):
            raise ValueError('Initialize the explicit appended-zero endpoint model first')
        oldc = np.asarray(old.core.c, float)
        newc = np.asarray(self.new_obj._core.c, float)
        if (newc.shape != (self.N-1,) or not exact(newc[:7], oldc) or
                not exact(newc[7:], np.zeros(self.N-8)) or
                not exact([old.core.q, self.old_obj.q, self.old_flow.end, self.old_flow.prefix_end],
                          [self.new_obj._core.q, self.new_obj.q, self.new_flow.end, self.new_flow.prefix_end]) or
                self.new_obj.cfg != old.binding.record['frozen_profile'] or
                mode_model.definition['lambda_value'] != 1. or
                mode_model.definition['lift_window'] != list(WINDOW)):
            raise ValueError('The defining core, profile, chart, gauge or window differs')
        if getattr(self.polynomial, 'extrapolate', None) is not False:
            raise ValueError('The saved physical PPoly must forbid extrapolation')
        self.old_initial = np.asarray(self.old_flow.exact_lift_initial, float).copy()
        self.new_initial = np.asarray(self.new_flow.exact_lift_initial, float).copy()
        if (self.old_initial.shape != (3*self.M+1,) or self.new_initial.shape != (3*self.N+1,) or
                not exact(self.old_initial, self.old_obj._initial) or
                not exact(self.new_initial, self.new_obj._initial)):
            raise ValueError('Use the actual finite inlet projections attached to both lifts')
        self.delta_initial = self.new_initial-embed_state(self.old_initial, self.M, self.N)
        self.definition = dict(scope=__doc__, source_checkpoint=old.binding.descriptor()['checkpoint'],
            old_modes=self.M, new_modes=self.N, old_state_components=3*self.M+1,
            new_state_components=3*self.N+1, component_layout='R0,R1..RM,T1..TM,Z1..ZM',
            physical_trace_indices=[5, 6], lambda_value=1., lift_window=list(WINDOW),
            state_rule='Z_N=E Z_M+a(s) chi(s) (I_N-E I_M)',
            first_rule='Z_N_s=E Z_M_s+(a_s chi+a chi_s) (I_N-E I_M)',
            second_rule='Z_N_ss=E Z_M_ss+(a_ss chi+2a_s chi_s+a chi_ss) (I_N-E I_M)',
            coordinate_scope='Derivatives are physical-s jets. Normalized solver coordinates require the new original chart.',
            actual_inlet_projection_scope='Use each already constructed finite binary64 I; neither is treated as an exact Fourier integral.',
            zero_window_scope='If a window factor is literally zero, copy the embedded state jet without a floating +0 operation.',
            source_polynomial_scope='Saved complete physical quintic only; not raw cubic or raw.y.',
            new_polynomial_created=False, inlet_repair_applied=False,
            mean_height_scope='The common mean in R48 is a separate hypothesis. No source mean primitive is copied or recomputed.',
            finite_core_roundoff_scope='Appending zero gives the same defining Gamma; independently evaluated numerical cores may differ. This interface supplies no bound for that difference.',
            genuine_new_dimensional_tail_required=True,
            exact_floating_physical_identity_claim=False, continuous_error_certificate=False,
            README5_fixed_all_parameters_refinement_claim=False)

    def check_parameters_unchanged(self):
        """Do not reuse a frozen transfer after a solver changes its core."""
        if (not exact(self.model.parameters, self.parameters) or
                not exact(self.parameters, self.new_obj._core_key) or
                not exact(self.old_parameters[1:], self.old_obj._core_key) or
                not exact(self.new_initial, self.new_flow.exact_lift_initial) or
                not exact(self.old_initial, self.old_flow.exact_lift_initial)):
            raise ValueError('The old/new core changed after the transfer was defined')

    def __call__(self, physical_s, nu=0):
        if isinstance(nu, (bool, np.bool_)) or not isinstance(nu, (int, np.integer)) or nu not in (0, 1, 2):
            raise ValueError('Only physical position-state and its first two s jets are implemented')
        self.check_parameters_unchanged()
        s = np.atleast_1d(np.asarray(physical_s, float))
        factors = reference_jets(self.new_flow, s)
        old_values = self.polynomial(s, nu=nu)
        if old_values.shape != (3*self.M+1, len(s)) or not np.all(np.isfinite(old_values)):
            raise ValueError('The complete physical polynomial jet is required inside its domain')
        out = embed_state(old_values, self.M, self.N)
        active = factors[nu] != 0.
        # In particular all cut values/physical jets are literal block copies.
        # No new-mode tail value or extra boundary response is inferred.
        out[:, active] += self.delta_initial[:, None]*factors[nu][None, active]
        return out

    def physical_jets(self, physical_s):
        return tuple(self(physical_s, nu) for nu in (0, 1, 2))

    def source_mesh_in_new_chart(self):
        """Map the actual saved physical mesh using the original inverse_chart.

        The original inverse_chart convergence gate remains in force.  The
        finite forward roundtrip is reported as a diagnostic, not forced to
        equal zero.  A caller may refine this mesh separately; this method
        performs no projection, end repair, BVP or residual audit.
        """
        self.check_parameters_unchanged()
        s = np.asarray(self.polynomial.x, float).copy()
        t = self.new_obj.inverse_chart(s, float(self.parameters[0]))
        forward, ds = self.new_obj.chart(t, float(self.parameters[0]))
        if (not np.all(np.isfinite(t)) or not np.all(np.diff(t) > 0) or
                np.any(t < 0.) or np.any(t > 1.) or not np.all(ds > 0.)):
            raise ValueError('The original new normalized chart did not preserve the mesh domain/order')
        return t, dict(physical_source='saved physical PPoly.x', normalized_chart='new fixed-profile original inverse_chart',
            source_mesh_points=len(s), forward_physical_roundtrip_max=float(np.max(abs(forward-s))),
            old_normalized_raw_mesh_reused=False, coordinate_roundtrip_exact_claim=False)
