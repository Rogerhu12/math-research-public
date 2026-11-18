"""R47 dynamic-M endpoint models on the actual endpoint's frozen profile.

This is a future construction interface, not a new numerical execution.
The input must be the explicit completed M8 lambda=1 reader.  The original
profile, material chart, gauge and warp are retained, while all old seven
physical controls occupy their original slots and new controls start at zero.

The original fixed=True equations are deliberately retained: p0 is now
log(actual_q / seed_q), and remains a solver unknown.  Thus an initialized
model has the same defining core, but a later solve may change q and every
control.  Free-parameter continuation must not be described as README #5
refinement with all physical parameters fixed.

The full-dimensional linear port is a separately bound input.  No actual DN
response, tail state, height Jacobian, mean-height primitive or physical
polynomial is manufactured or padded here.  R48 state transfer is separate.
"""
from dataclasses import dataclass
import copy
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
M3 = HERE.parent / 'resume_m3'
MODEL_KIND = 'exact_m3_R47_fixed_slot_endpoint_full_lift'
CONTROL_PATH = 'R47-fixed-trace-slots-5-and-6-v1'
WINDOW = (.5, .9)
DEPENDENCIES = {
    HERE / 'm3_trace_path_endpoint.py': 'e5ef9f62349e318fef3f844d603f6dc39a047107c3fff6ec4f3449a4367cd407',
    HERE / 'r47_fixed_slot_trace_basis.py': '93e69b2a09b1869638743b6735ee7e609815c37937a3fcd94d45706c9c9fcddb',
    HERE / 'r47_fixed_slot_trace_core.py': '71233d6eaef233f3af7862c14311e640ee39d127993f165f48dc01447b44c38a',
    M3 / 'm3_circle_trace_path_model.py': 'b5a26902c8af378d0f965269e4463814045ce98fa84f93935db9f31e1c5c950e',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def payload_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def exact(a, b):
    a, b = np.asarray(a, dtype=np.float64), np.asarray(b, dtype=np.float64)
    return a.shape == b.shape and a.tobytes() == b.tobytes()


def checked_count(value, minimum, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or value < minimum:
        raise ValueError(name + ' must be an integer at least ' + str(minimum))
    return int(value)


def check_dependencies():
    for path, expected in DEPENDENCIES.items():
        if sha(path) != expected:
            raise ValueError('A frozen endpoint/model dependency changed: ' + str(path))


@dataclass(frozen=True)
class EndpointModeModel:
    anchor: object
    obj: object
    parameters: np.ndarray
    definition: dict

    def initialize_core(self):
        """Explicitly construct the complete new core and inlet once if needed.

        This calls the original initial(p) with its original full-control
        positivity guard and analytic inlet derivatives.  It does not evaluate
        an initial-guess residual, run a tail, integrate a mean or solve a BVP.
        """
        check_dependencies()
        self.anchor.binding.check_files()
        p = self.parameters
        ans = self.obj.initial(p)
        flow = self.obj.flow(float(p[0]))
        old = self.anchor
        oldc = np.asarray(old.binding.record['physical_controls'], dtype=float)
        wanted = np.zeros(self.obj.M-1, dtype=float)
        wanted[:7] = oldc
        if (not exact(self.obj._core.c, wanted) or
                not exact([self.obj.support_amplitude, self.obj._core.q],
                          [old.core.q, old.core.q]) or
                flow.exact_lift_core is not self.obj._core or
                not exact(flow.exact_lift_initial, ans) or
                not self.obj._core.rho_lower > 1e-5):
            raise ValueError('The initialized full physical control/primary identity differs')
        return ans

    @property
    def flow(self):
        return self.obj.flow(float(self.parameters[0]))

    def parameter_identity(self, parameters=None):
        """Report the original free-parameter meaning, without changing a model.

        A caller should save this for the actual returned vector as well as the
        initial vector.  A changed vector is not a fixed-full-parameter result.
        """
        p = np.asarray(self.parameters if parameters is None else parameters, float)
        if p.shape != (self.obj.M,) or not np.all(np.isfinite(p)):
            raise ValueError('The complete M-dimensional parameter vector is required')
        actual_q = self.obj.seed_support_amplitude * math.exp(float(p[0]))
        controls = p[1:] * self.obj.pscale
        return dict(complete_parameters=p.tolist(), central_correction_scales=self.obj.pscale.tolist(),
            complete_physical_controls=controls.tolist(), gauge_amplitude=self.obj.q,
            seed_support_amplitude=self.obj.seed_support_amplitude, actual_primary_amplitude=actual_q,
            fixed_metric_flag=True, p0_scope='log(actual_q / seed_q); a free original solver unknown',
            profile_frozen=True, actual_q_frozen_by_equations=False,
            physical_controls_frozen_by_equations=False,
            same_initial_parameter_bits=exact(p, self.parameters),
            README5_fixed_all_parameters_refinement_claim=False)


class EndpointModeEnvironment:
    """Build fresh mode-specific classes from one genuine M8 endpoint.

    The caller first invokes the explicit endpoint reader in a fresh process.
    We reuse its already installed original source environment and immutable
    original cosine constructor.  Each make() captures a distinct fixed-slot
    factory inside a fresh original build_classes() call; no old object or
    cache is patched.  No numerical construction occurs merely on import.
    """

    def __init__(self, native_endpoint):
        check_dependencies()
        from m3_trace_path_endpoint import NativePathPrefix
        if not isinstance(native_endpoint, NativePathPrefix):
            raise TypeError('Use the explicit completed M8 lambda=1 native endpoint reader')
        native_endpoint.binding.check_files()
        self.anchor = native_endpoint
        r = native_endpoint.binding.record
        if (r['path_lambda'] != 1. or r['partial_lift_strength'] != 1. or
                r['config']['fixed_metric'] is not False or r['config']['modes'] != 8 or
                r['lift_window'] != list(WINDOW) or
                r['path_definition'].get('branch') != 'literal_R44_endpoint' or
                native_endpoint.obj.fixed or native_endpoint.obj.M != 8):
            raise ValueError('A partial-lift, rebased, or non-M8 source is not this entry')
        if (not exact([r['gauge_amplitude'], r['warp_reference_q']], [.06, .06]) or
                not exact(native_endpoint.core.c, r['physical_controls']) or
                not exact([native_endpoint.core.q], [r['actual_primary_amplitude']])):
            raise ValueError('The actual complete endpoint control/gauge identity differs')
        self.record = r
        self.chart = copy.deepcopy(r['chart'])
        self.profile = copy.deepcopy(r['frozen_profile'])
        self.settings = copy.deepcopy(r['core_round_settings'])
        self.settings['homotopy'] = 1.
        self.coupler = native_endpoint.environment.coupler
        self.original_cosine = native_endpoint.environment.original_cosine

    def _port(self, path, modes):
        """Bind a genuine complete linear-port file for construction only."""
        path = Path(path).resolve()
        file_ref = ref(path)
        port = json.loads(path.read_text())
        if not isinstance(port, dict) or not isinstance(port.get('cut'), dict):
            raise ValueError('A complete original linear-port JSON file is required')
        # This is the same explicit profile bridge insertion used by the old
        # cosine reader; it is not a new tail metric or a fitted DN coefficient.
        bridge = copy.deepcopy(self.profile['prefix_bridge'])
        if '_prefix_bridge' in port['cut'] and port['cut']['_prefix_bridge'] != bridge:
            raise ValueError('The supplied port carries a different physical bridge')
        port['cut']['_prefix_bridge'] = bridge
        if (payload_sha(port['parameters']) != payload_sha(self.record['physical_tail_parameters']) or
                payload_sha(port['cut']) != payload_sha(self.record['physical_tail_cut'])):
            raise ValueError('The full physical tail/profile definition changed')
        slopes = np.asarray(port['linearSlope'], dtype=float)
        labels = port.get('modes')
        if (slopes.ndim != 1 or len(slopes) < modes or not np.all(np.isfinite(slopes)) or
                labels is None or len(labels) != len(slopes) or
                labels[:modes] != list(range(3, 3*modes+1, 3))):
            raise ValueError('The supplied port lacks actual new-dimensional linear modes')
        port['_sha256'] = file_ref['sha256']
        return port, file_ref

    def make(self, modes, angular, linear_port_path):
        """Construct an uninitialized endpoint BVP and exact copied seed vector.

        No old restart method, ratio**j amplitude rule, projection of an old
        field, new actual-tail request, mean integration or solver is called.
        The numerical radial chart is freshly rebased to the frozen profile;
        its normalized t is not assumed equal to the old variable-profile t.
        """
        self.anchor.binding.check_files()
        check_dependencies()
        M = checked_count(modes, 8, 'modes')
        angular = checked_count(angular, 1, 'angular')
        port, port_ref = self._port(linear_port_path, M)
        for directory in (HERE, M3, M3/'round_raw_lib'):
            if str(directory) not in sys.path:
                sys.path.insert(0, str(directory))
        from plateau_core import PlateauSupportCore
        from r47_fixed_slot_trace_core import make_core_factory
        from synchronous_core_lift import install_synchronous_lift
        factory, descriptor = make_core_factory(PlateauSupportCore, self.original_cosine,
                                                self.settings, modes=M)
        # The original build_classes from-import captures this immutable
        # constructor. Existing model classes retain their prior closure.
        __import__('fixed_metric_mode3_core').PlanarSupportCore = factory
        __import__('fixed_metric_mode3_bvp').PlanarSupportCore = factory
        Flow, Base = self.coupler.adaptive.build_classes(copy.deepcopy(self.chart))
        Lift = install_synchronous_lift(Flow, Base, 1., window=WINDOW)
        class BVP(self.coupler.TailMixin, Lift):
            def initial(self, p):
                result = super().initial(p)
                if not self._core.rho_lower > 1e-5:
                    raise FloatingPointError('Keep the original full-control rho>1e-5 floor')
                return result
        qg, warp = self.record['gauge_amplitude'], self.record['warp_reference_q']
        obj = BVP(copy.deepcopy(self.profile), port, qg, M, angular, True, warp)
        if obj._core_key is not None or obj._core is not None:
            raise ValueError('Set the true support seed before the first core evaluation')
        obj.seed_support_amplitude = self.record['actual_primary_amplitude']
        oldp = np.asarray(self.record['parameters'], float)
        oldscales = np.asarray(self.record['central_correction_scales'], float)
        if oldp.shape != (8,) or not exact(obj.pscale[:7], oldscales):
            raise ValueError('The original first seven gauge/scales must remain byte-identical')
        p = np.zeros(M, dtype=float)
        p[1:8] = oldp[1:8]  # Preserve p bits, not a divide/multiply reconstruction.
        if (not exact(p[1:8], oldp[1:8]) or
                not exact(p[1:8]*obj.pscale[:7], self.record['physical_controls'])):
            raise ValueError('The full original physical controls were not retained')
        cfg = self.record['config']
        obj.bcweights = np.full(M, cfg['physical_bc_tol']/cfg['bc_tol'])
        f = obj.flow(0.)
        if (obj.cfg != self.profile or not obj.fixed or obj.M != M or obj.n != 3*M+1 or
                not exact([obj.q, obj.warp_q], [qg, warp]) or
                not exact([f.end, f.prefix_end], [self.anchor.flow.end, self.anchor.flow.prefix_end])):
            raise ValueError('The frozen physical profile/domain/gauge differs')
        if hasattr(obj, 'tail'):
            raise ValueError('No old lower-dimensional actual tail may be attached')
        definition = dict(scope=__doc__, core_kind=MODEL_KIND, control_path=CONTROL_PATH,
            source_endpoint=self.anchor.binding.descriptor(), source_mode_count=8,
            modes=M, state_components=3*M+1, parameters=M, controls=M-1,
            physical_trace_indices=[5, 6], parameter_trace_indices=[6, 7],
            lambda_value=1., full_lift_strength=1., lift_window=list(WINDOW),
            core_factory=descriptor, core_settings=copy.deepcopy(self.settings),
            frozen_profile=copy.deepcopy(self.profile), original_base_profile=copy.deepcopy(self.record['path_base_profile']),
            original_delta_parameter=float(oldp[0]), new_initial_parameter_zero=float(p[0]),
            rebasing_scope='The original delta shift is included exactly once in frozen_profile; new p0 controls log(q/qseed), not delta.',
            numerical_gauge=qg, seed_support_amplitude=obj.seed_support_amplitude,
            warp_reference=warp, angular_chart=copy.deepcopy(self.chart),
            chart_payload_sha256=payload_sha(self.chart),
            radial_chart_scope='Same physical s/profile; the fixed-profile normalized t chart is new. Transfer uses physical s, then the original new inverse_chart if a t mesh is requested.',
            angular_requested=angular, angular_effective=obj.nt,
            parameter_scales=obj.pscale.tolist(), complete_initial_parameters=p.tolist(),
            complete_initial_physical_controls=(p[1:]*obj.pscale).tolist(),
            linear_port_source=port_ref, linear_port_mode_count=len(port['linearSlope']),
            physical_tail_parameters=copy.deepcopy(port['parameters']), physical_tail_cut=copy.deepcopy(port['cut']),
            actual_tail_scope='A genuine M-dimensional original actual DN/Jac/audit response is still required. No lower-dimensional response is padded.',
            mean_height_scope='Not in these 3M+1 states. A final actual flow/solution requires its own original height_integral and audit.',
            parameter_scope='Original fixed=True equations leave p0 and every control free; initialized equality is not a fixed-all-parameter solve claim.',
            README5_fixed_all_parameters_refinement_claim=False,
            initialized_core_constructed=False, initial_field_transferred=False,
            BVP_solver_invoked=False, actual_tail_solver_invoked=False,
            mean_height_integrated=False, complete_metric_audited=False)
        obj.r47_definition = copy.deepcopy(definition)
        return EndpointModeModel(self.anchor, obj, p, definition)
