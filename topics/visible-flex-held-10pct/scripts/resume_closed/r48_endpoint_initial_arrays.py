"""Assemble one real R47/R48 high-mode initial state for the actual coupler.

Call only from the new actual run, using a completed literal M8 endpoint.
The original defining core is constructed once at its appended-zero seed.
Old physical PPoly values are evaluated on the actual forward physical nodes
of the NEW fixed-profile chart; the old raw x/y are not reused as states.
No initial RMS probe, inlet repair, physical export, mean, metric or DN is
performed.  The returned H is a complete new-dimensional request, not a
padded actual response.  The original new solver still has free q and controls.
"""
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
DEPENDENCIES = {
    HERE/'r47_endpoint_refinement_model.py':
        'd533b93dc78b1eed7656527aa8ac689772f9a4903e441cd5f49e51d2ef16b7b6',
    HERE/'r48_reference_state_transfer.py':
        'fe7decedceb9b20d9fa70715a40494b24670f40dd28a4c88fc80033d7a14610a',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def binary_sha(values):
    array = np.ascontiguousarray(np.asarray(values, dtype='<f8'))
    if not np.all(np.isfinite(array)):
        raise ValueError('Only finite complete arrays may enter the actual initializer')
    return hashlib.sha256(array.tobytes()).hexdigest()


def check_sources():
    for path, digest in DEPENDENCIES.items():
        if sha(path) != digest:
            raise ValueError('The bound R47/R48 construction source changed: '+str(path))


@dataclass(frozen=True)
class EndpointInitialArrays:
    environment: object
    model: object
    transfer: object
    x: np.ndarray
    s: np.ndarray
    y: np.ndarray
    p: np.ndarray
    H: np.ndarray
    inlet: np.ndarray
    descriptor: dict

    @property
    def obj(self):
        return self.model.obj

    def write(self, directory):
        """Save the once-constructed actual initial arrays, before any solve.

        Full arrays are scratch artifacts.  This function does not reconstruct
        an initializer, reevaluate a flow, or call an initial residual probe.
        """
        check_sources()
        self.transfer.check_parameters_unchanged()
        got = {key: binary_sha(getattr(self, key)) for key in ('x', 's', 'y', 'p', 'H', 'inlet')}
        if got != self.descriptor['array_binary64_sha256']:
            raise ValueError('A constructed initializer array changed before serialization')
        directory = Path(directory).resolve()
        directory.mkdir(parents=True, exist_ok=True)
        arrays = directory/'r48-initial-arrays.npz'
        with arrays.open('xb') as stream:
            np.savez_compressed(stream, initial_t=self.x, initial_s=self.s,
                initial_y=self.y, initial_p=self.p, initial_H=self.H,
                original_new_inlet=self.inlet)
        record = dict(self.descriptor, arrays=ref(arrays))
        record_path = directory/'r48-initializer.json'
        with record_path.open('x') as stream:
            json.dump(record, stream, indent=2, allow_nan=False)
            stream.write('\n')
        return dict(arrays=ref(arrays), record=ref(record_path))


def assemble(endpoint_binding, modes, angular, linear_port_path):
    """One necessary construction, to be called in the new actual solver run.

    endpoint_binding is the complete explicit lambda=1 physical reader.  It
    already locks the source CP and genuine tail identity.  No legacy restart
    or amplitude-power rule is invoked; all old seven parameter/scales bits
    and the actual source profile are handled by the bound R47 model factory.
    """
    check_sources()
    from r47_endpoint_refinement_model import EndpointModeEnvironment, exact
    from r48_reference_state_transfer import EndpointStateTransfer
    endpoint_binding.check_files()
    anchor = endpoint_binding.native_prefix()
    environment = EndpointModeEnvironment(anchor)
    model = environment.make(modes, angular, linear_port_path)
    if model.obj._core is not None or model.obj._core_key is not None:
        raise ValueError('Construct the new seed core only at this explicit initialization point')
    inlet = np.asarray(model.initialize_core(), dtype=float).copy()
    transfer = EndpointStateTransfer(model)
    x, chart_diagnostic = transfer.source_mesh_in_new_chart()
    p = model.parameters.copy()
    s, ds = model.obj.chart(x, float(p[0]))
    s, ds = np.asarray(s, float), np.asarray(ds, float)
    # The forward roundtrip may differ by ulps. Evaluate the continuous
    # transferred initial field at these actual new solver physical nodes,
    # not at the source PPoly.x with a mismatched normalized coordinate.
    if (x.ndim != 1 or s.shape != x.shape or ds.shape != x.shape or
            x[0] != 0. or x[-1] != 1. or s[0] != 0. or
            not exact(s[-1], anchor.flow.end) or not np.all(np.diff(s) > 0.) or
            not np.all(ds > 0.) or not np.all(np.isfinite(ds)) or
            not np.all(np.isfinite(s))):
        raise ValueError('The actual new fixed-profile chart must cover the common domain in order')
    y = transfer(s)
    if y.shape != (3*model.obj.M+1, len(x)) or not np.all(np.isfinite(y)):
        raise ValueError('The complete new three-block initial state is required')
    H = np.asarray(model.obj.bridge.sigma*model.obj.q*y[model.obj.iz:, -1], float)
    old_cut = np.asarray(anchor.polynomial(np.array([anchor.flow.end])), float)[:, 0]
    old_H = np.asarray(anchor.obj.bridge.sigma*anchor.obj.q*old_cut[anchor.obj.iz:], float)
    if (H.shape != (model.obj.M,) or not exact(H[:8], old_H) or
            not exact(H[8:], np.zeros(model.obj.M-8))):
        raise ValueError('The literal zero-window cut embedding must preserve every old H bit')
    transfer.check_parameters_unchanged()
    endpoint_binding.check_files()
    arrays = dict(x=x, s=s, y=y, p=p, H=H, inlet=inlet)
    descriptor = dict(scope=__doc__, assembly_source=ref(__file__),
        source_endpoint=endpoint_binding.descriptor(),
        model_definition=model.definition, state_transfer_definition=transfer.definition,
        model_definition_scope='Definition recorded before original initial(p); its nested construction-stage flags describe that earlier operation, not this completed assembly.',
        source_mesh_points=len(anchor.polynomial.x), nodes=len(x),
        state_components=y.shape[0], modes=model.obj.M,
        parameter_identity=model.parameter_identity(p),
        array_binary64_sha256={key: binary_sha(value) for key, value in arrays.items()},
        chart=chart_diagnostic,
        field_evaluation_coordinate='Actual s returned by the new original chart(x,p0), after the one inverse_chart of source physical knots.',
        initial_inlet_residual_max=float(np.max(np.abs(y[:, 0]-inlet))),
        source_physical_cut_H=old_H.tolist(), complete_new_request_H=H.tolist(),
        first_eight_cut_H_bitwise_equal=True, appended_cut_H_exact_zero=True,
        tail_request_scope='These are actual new-dimensional Dirichlet data only. No M8 tail state, momentum, DN/Jacobian/audit response or acceptance is embedded.',
        actual_primary_formula='seed_support_amplitude * exp(p0), not numerical_gauge * exp(p0)',
        new_model_initial_calls=1, new_seed_core_initialized=True,
        initial_field_transferred=True,
        initializer_RMS_evaluated=False, inlet_repair_applied=False,
        physical_quintic_exported=False, mean_integrated_or_copied=False,
        metric_audited=False, actual_tail_solver_invoked=False, BVP_solver_invoked=False,
        exact_floating_physical_map_identity_claim=False,
        README5_fixed_all_parameters_refinement_claim=False)
    return EndpointInitialArrays(environment, model, transfer, x, s, y, p, H, inlet, descriptor)
