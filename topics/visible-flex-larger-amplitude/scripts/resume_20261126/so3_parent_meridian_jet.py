#!/usr/bin/env python3
"""World meridian jets of one real frozen R671/deep parent, for an SO(3) seed.

No scientific work runs on import. Public repository Actions alone may
construct this object or evaluate its fields. This module keeps the entire
same shared-quintic q, core, H and context-owned analytic f/h/k chain.
The original point adapter is not modified or relabeled.

The old point/six-jet routines return physical derivative components in
the phi-dependent cylindrical frame. We include every frame connection
term, then rotate ALL physical derivatives into one world Cartesian
frame. Returned T0_phi/T0_phiphi are derivatives in the supplied physical
phi coordinate, not derivatives in the frozen material angle.

This is a numerical initializer/jet kernel. Requested-point positivity
and ordinary floating normalization do not certify continuous positivity,
integrability, the new metric, closed gluing, embedding, amplitude or reach.
"""
import hashlib
import json
import os
from pathlib import Path

import numpy as np


SCHEMA = 'complete-frozen-parent-world-meridian-jet-v1'
BASE_FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
DEEP_FACTORY_SHA = '4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
DEEP_SCALAR_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
EXPECTED_OPERATORS = {
    'dense': 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d',
    'batch': '02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a',
    'observed': '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d',
}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('Scientific parent meridian jets run only in the public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode('utf-8')).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256()
    h.update(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def function_source(value, expected, role):
    function = getattr(value, '__func__', value)
    code = getattr(function, '__code__', None)
    if code is None:
        raise ValueError('Need the actual published Python function: '+role)
    path = Path(code.co_filename).resolve()
    actual = sha(path)
    if actual != expected:
        raise ValueError('Changed real function source '+role+': '+actual)
    return dict(path=str(path), sha256=actual)


def readonly_real(value, name, shape=None):
    array = np.asarray(value)
    if (np.iscomplexobj(array) or array.dtype.kind != 'f'
            or not np.isfinite(array).all()
            or (shape is not None and array.shape != shape)):
        raise ValueError('Need finite real complete parent '+name)
    result = np.array(array, copy=True)
    result.setflags(write=False)
    return result


def world_frame(value, phi):
    """Rotate physical derivative components; derivatives already include connection."""
    value = np.asarray(value)
    co, si = np.cos(phi), np.sin(phi)
    result = np.empty_like(value)
    result[..., 0] = co[None]*value[..., 0]-si[None]*value[..., 1]
    result[..., 1] = si[None]*value[..., 0]+co[None]*value[..., 1]
    result[..., 2] = value[..., 2]
    return result


class ParentMeridianJet:
    """Freeze one actual parent's complete q/core/H, retaining its exact physical context.

    Construct once after the ordinary byte-bound factory/create_pair and
    problem.prepare(parent_x). Calling evaluate later does not rehash all
    sources or re-copy the parent arrays. The caller keeps this parent
    problem/context immutable while solving for independent SO(3) variables.

    cells/local are matching one-dimensional radial arrays. phi is an
    independent one-dimensional angular vector. All physical vector jets
    have shape (len(cells), len(phi), 3). No angle truncation occurs beyond
    the actual parent's complete M-mode representation and exact lift.
    """

    def __init__(self, problem, prepared, *, expected_model_identity_sha256=None,
                 expected_bundle_sha256=None):
        require_actions()
        # A fixed-target wrapper may expose its original physical operator.
        self.problem = getattr(problem, 'original_operator', problem)
        o = self.problem
        context = o.reference_tail_context
        self.context = context
        model = context.definition()
        model_schema = model.get('schema')
        if model_schema == 'R671-exact-reference-tail-lift-v1':
            factory_sha = BASE_FACTORY_SHA
        elif model_schema == 'deep-valley-fixed-scalar-fullclosed-lift-v1':
            factory_sha = DEEP_FACTORY_SHA
            if (model.get('base_reference_factory_source_sha256') != BASE_FACTORY_SHA
                    or model.get('deep_scalar_source_sha256') != DEEP_SCALAR_SHA
                    or model.get('fixed_new_scalar_metric') is not True
                    or model.get('target_is_a_moving_angular_mean') is not False
                    or canonical(model['profile_definition']) != model['profile_identity_sha256']):
                raise ValueError('Retain the complete same exact deep scalar and its real base factory')
        else:
            raise ValueError('Need an actual completed R671 or fixed-deep canonical parent')
        if (model.get('source_sha256') != factory_sha
                or model.get('lambda_value') != 1
                or model.get('operator_source_sha256s') != EXPECTED_OPERATORS):
            raise ValueError('This parent initializer binds the full actual lambda-one physical model')
        self.model_identity = canonical(model)
        if (expected_model_identity_sha256 is not None
                and expected_model_identity_sha256 != self.model_identity):
            raise ValueError('The actual full parent model identity differs from the declared parent')

        source_binding = {
            'factory_definition': function_source(context.definition, factory_sha, 'context.definition'),
            'factory_constructor': function_source(context.create_pair, factory_sha, 'context.create_pair'),
            'lift_at': function_source(o.lift_at, BASE_FACTORY_SHA, 'physical lift_at'),
            'mix_profile': function_source(context.mix_profile, BASE_FACTORY_SHA, 'complete f/h/k mixture'),
            'point_definition': function_source(context._point_definition, BASE_FACTORY_SHA, 'exact affine point'),
            'prepare': function_source(o.prepare, EXPECTED_OPERATORS['batch'], 'complete prepare'),
            'shared_quintic': function_source(context.observed.hermite_weights,
                EXPECTED_OPERATORS['observed'], 'shared quintic Hermite weights'),
        }
        source_binding['reference_at'] = function_source(context.reference_at,
            factory_sha, 'same actual exact reference')
        if factory_sha == DEEP_FACTORY_SHA:
            source_binding['deep_scalar'] = function_source(context.deep.reference_at_affine,
                DEEP_SCALAR_SHA, 'complete deep reference at exact affine point')
        for role, expected in EXPECTED_OPERATORS.items():
            record = context._operator_sources[role]
            if record['sha256'] != expected or sha(record['path']) != expected:
                raise ValueError('Changed complete parent operator role '+role)
            source_binding[role] = dict(record)
        if set(context._operator_sources) != set(EXPECTED_OPERATORS):
            raise ValueError('Need the complete declared dense/batch/observed source triple')

        scalar_roles = ('scalar_source', 'integer_source', 'hold_source', 'observed_source')
        if set(model['source_sha256s']) != set(scalar_roles):
            raise ValueError('Retain every actual scalar, integer, Hold and observation source')
        for role in scalar_roles:
            record = context.input_records[role]
            if (record['sha256'] != model['source_sha256s'][role]
                    or sha(context.paths[role]) != record['sha256']):
                raise ValueError('Changed actual complete scalar dependency '+role)
            source_binding[role] = dict(record)
        for role, model_key in (
                ('scalar_input', 'scalar_input_sha256'),
                ('node_report', 'node_report_sha256'),
                ('carrier', 'original_observation_carrier_sha256')):
            record = context.input_records[role]
            if record['sha256'] != model[model_key] or sha(context.paths[role]) != record['sha256']:
                raise ValueError('Changed actual parent input '+role)

        if 'reference_tail_model_json' not in context.data:
            raise ValueError('Do not reinterpret a pre-canonical coordinate bundle as this parent')
        bundle_model = json.loads(str(context.data['reference_tail_model_json'].item()))
        if bundle_model != model:
            raise ValueError('The saved actual parent canonical definition differs from its rebuilt context')
        parent_record = dict(context.input_records['bundle'])
        parent_bundle = context.paths['bundle']
        if sha(parent_bundle) != parent_record['sha256']:
            raise ValueError('The actual parent input bundle bytes changed after construction')
        if expected_bundle_sha256 is not None and expected_bundle_sha256 != parent_record['sha256']:
            raise ValueError('The complete parent bundle is not the selected actual parent')

        self.M, self.J, self.n = int(o.M), int(o.J), int(o.n)
        if self.n != 3*self.M+2 or model['M'] != self.M or self.J != len(o.mesh):
            raise ValueError('The complete parent Fourier/shared-quintic dimensions changed')
        self.mesh = readonly_real(o.mesh, 'mesh', (self.J,))
        self.jets = readonly_real(prepared.jets, 'qjets', (self.J, 3, self.n))
        self.core = readonly_real(prepared.core, 'core', (self.M,))
        self.freq = readonly_real(o.freq, 'frequencies', (self.M,))
        self.qfreq = readonly_real(o.qfreq, 'core-to-rho factors', (self.M,))
        height = np.asarray(prepared.height)
        if height.shape != () or np.iscomplexobj(height) or not np.isfinite(height):
            raise ValueError('Need the real actual complete parent height')
        self.height = float(height)
        if (not np.array_equal(self.mesh, context.data['mesh'])
                or not np.array_equal(self.jets, context.data['qjets'])
                or self.jets.dtype != context.data['qjets'].dtype
                or self.height.hex() != float(context.data['Hcap']).hex()
                or not np.array_equal(self.core, self.jets[0, 0, 1:self.M+1])
                or not np.array_equal(self.freq, 2*np.arange(1, self.M+1, dtype=float))
                or not np.array_equal(self.qfreq, 1-self.freq*self.freq)):
            raise ValueError('Freeze exactly the saved parent q/core/H; do not substitute another candidate')
        if (not np.array_equal(self.mesh, context.mesh)
                or model['mesh_sha256'] != array_sha(self.mesh)
                or not np.all(np.diff(self.mesh) > 0)):
            raise ValueError('The parent uses a different exact shared radial mesh')
        self._hermite_weights = context.observed.hermite_weights
        self.model = model
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            parent_bundle=parent_record, parent_model_identity_sha256=self.model_identity,
            physical_factory_sha256=factory_sha, source_binding=source_binding,
            parent_qjets_sha256=array_sha(self.jets), parent_core_sha256=array_sha(self.core),
            parent_height_hex=self.height.hex(), M=self.M, J=self.J,
            full_shared_quintic_and_analytic_lift=True,
            old_point_adapter_modified=False, original_parent_field_unchanged=True,
            returned_coordinate_frame='world Cartesian; derivatives with respect to physical phi',
            numerical_normalization_not_outward=True,
            no_new_field_metric_or_geometry_certificate=True)

    def evaluate(self, cells, local, phi):
        require_actions()
        raw_cells, local, phi = np.asarray(cells), np.asarray(local), np.asarray(phi)
        if (raw_cells.ndim != 1 or local.ndim != 1 or phi.ndim != 1
                or len(raw_cells) != len(local) or len(local) == 0 or len(phi) == 0
                or np.iscomplexobj(raw_cells) or np.iscomplexobj(local) or np.iscomplexobj(phi)
                or not np.isfinite(raw_cells).all() or not np.isfinite(local).all()
                or not np.isfinite(phi).all()):
            raise ValueError('Use complete finite real radial rows and an independent angular vector')
        cells = raw_cells.astype(np.int64)
        if (not np.array_equal(raw_cells, cells) or np.any(cells < 0)
                or np.any(cells >= self.J-1) or np.any(local < 0) or np.any(local > 1)):
            raise ValueError('Each literal radial point must lie inside its actual parent cell')
        local, phi = np.asarray(local, dtype=float), np.asarray(phi, dtype=float)
        M, P, A = self.M, len(cells), len(phi)
        nu = self.freq
        angle = phi[:, None]*nu[None]
        co, si = np.cos(angle), np.sin(angle)
        co0 = np.column_stack((np.ones(A), co))
        rho = 1+co@(self.qfreq*self.core)
        rho_phi = -si@(nu*self.qfreq*self.core)
        delta = si@((self.qfreq/nu)*self.core)
        if not np.isfinite(rho).all() or np.any(rho <= 0):
            raise ValueError('The actual frozen parent material chart fails positivity at requested angles')
        er = np.column_stack((np.cos(delta), np.sin(delta), np.zeros(A)))
        et = np.column_stack((-np.sin(delta), np.cos(delta), np.zeros(A)))

        radial = np.empty((P, 3, self.n), dtype=float)
        profiles = np.empty((P, 9), dtype=float)
        for j, (cell, u) in enumerate(zip(cells, local)):
            cell, u = int(cell), float(u)
            weights = self._hermite_weights(self.mesh[cell+1]-self.mesh[cell], u)
            radial[j] = weights@self.jets[cell:cell+2].reshape(6, self.n)
            profiles[j] = self.problem.lift_at(cell, u)
        if not np.isfinite(radial).all() or not np.isfinite(profiles).all():
            raise ValueError('Nonfinite complete same-parent radial/reference jet')
        # y, qs, qss are all complete parent modes. The value y is not
        # needed for a meridian direction, but comes from the SAME quintic.
        qs, qss = radial[:, 1], radial[:, 2]

        def synth(value):
            result = np.empty((P, A, 3), dtype=float)
            result[..., 0] = value[:, :M+1]@co0.T
            result[..., 1] = value[:, M+1:2*M+1]@si.T
            result[..., 2] = value[:, 2*M+1:]@co0.T
            return result

        def angular(value, order):
            r = value[:, :M+1]
            t = value[:, M+1:2*M+1]
            z = value[:, 2*M+1:]
            R, T = r@co0.T, t@si.T
            Rp = -(r[:, 1:]*nu[None])@si.T
            Tp = (t*nu[None])@co.T
            Zp = -(z[:, 1:]*nu[None])@si.T
            result = np.empty((P, A, 3), dtype=float)
            if order == 1:
                result[..., 0], result[..., 1], result[..., 2] = Rp-T, Tp+R, Zp
            elif order == 2:
                result[..., 0] = -(r[:, 1:]*nu[None]**2)@co.T-2*Tp-R
                result[..., 1] = -(t*nu[None]**2)@si.T+2*Rp-T
                result[..., 2] = -(z[:, 1:]*nu[None]**2)@co.T
            else:
                raise ValueError('This exact algebraic meridian jet needs angular orders one and two')
            return result

        hp, hpp = profiles[:, 1], profiles[:, 2]
        fp, fpp = profiles[:, 4], profiles[:, 5]
        kp, kpp = profiles[:, 7], profiles[:, 8]
        V = synth(qs)+fp[:, None, None]*er[None]
        Vs = synth(qss)+fpp[:, None, None]*er[None]
        V[..., 2] += (hp*self.height+kp)[:, None]
        Vs[..., 2] += (hpp*self.height+kpp)[:, None]
        Vphi = angular(qs, 1)+fp[:, None, None]*(rho[:, None]*et)[None]
        Vphiphi = angular(qs, 2)+fp[:, None, None]*(
            rho_phi[:, None]*et-rho[:, None]**2*er)[None]
        if any(not np.isfinite(value).all() for value in (V, Vs, Vphi, Vphiphi)):
            raise ValueError('Nonfinite full physical parent derivative')
        norm_squared = np.sum(V*V, axis=-1)
        if not np.isfinite(norm_squared).all() or np.any(norm_squared <= 0):
            raise ValueError('The complete actual parent Fs must be nonzero at every requested point')
        norm = np.sqrt(norm_squared)
        T = V/norm[..., None]
        norm_s = np.sum(T*Vs, axis=-1)
        norm_phi = np.sum(T*Vphi, axis=-1)
        Ts = (Vs-T*norm_s[..., None])/norm[..., None]
        Tphi = (Vphi-T*norm_phi[..., None])/norm[..., None]
        norm_phiphi = (np.sum(Vphi*Vphi+V*Vphiphi, axis=-1)-norm_phi**2)/norm
        Tphiphi = (Vphiphi-T*norm_phiphi[..., None]
            -2*Tphi*norm_phi[..., None])/norm[..., None]
        if any(not np.isfinite(value).all() for value in (T, Ts, Tphi, Tphiphi)):
            raise ValueError('Nonfinite actual normalized parent meridian jet')

        # Each derivative above is already a physical derivative expressed
        # in the rotating frame. Rotating it ONCE gives its world value.
        result = dict(T0=world_frame(T, phi), T0_s=world_frame(Ts, phi),
            T0_phi=world_frame(Tphi, phi), T0_phiphi=world_frame(Tphiphi, phi),
            Fs=world_frame(V, phi), Fss=world_frame(Vs, phi),
            Fsphi=world_frame(Vphi, phi), Fsphiphi=world_frame(Vphiphi, phi),
            norm=norm, norm_s=norm_s, norm_phi=norm_phi, norm_phiphi=norm_phiphi,
            phi=np.array(phi, copy=True), theta_parent=phi+delta,
            rho_parent=rho, rho_phi_parent=rho_phi,
            metadata=dict(schema=SCHEMA, parent_model_identity_sha256=self.model_identity,
                parent_bundle_sha256=self.binding['parent_bundle']['sha256'],
                kernel_source_sha256=self.binding['source_sha256'],
                radial_rows=P, angular_columns=A, complete_parent_modes=M,
                minimum_Fs_norm=float(norm.min()), maximum_Fs_norm=float(norm.max()),
                minimum_rho_at_requested_angles=float(rho.min()),
                positive_Fs_norm_at_all_requested_points=True,
                positive_rho_at_all_requested_angles=True,
                continuous_positive_Fs_norm_certified=False,
                continuous_positive_rho_certified=False,
                angular_derivative_coordinate='physical phi, including every cylindrical-frame connection',
                returned_coordinate_frame='world Cartesian',
                same_complete_parent_q_H_k=True,
                numerical_jet_arithmetic_certified=False,
                metric_or_geometry_of_any_new_SO3_field_certified=False))
        for value in result.values():
            if isinstance(value, np.ndarray):
                value.setflags(write=False)
        return result


def parent_meridian_jets(problem, prepared, cells, local, phi, *,
                         expected_model_identity_sha256=None,
                         expected_bundle_sha256=None):
    """One-shot convenience; repeated integrations should retain ParentMeridianJet."""
    frozen = ParentMeridianJet(problem, prepared,
        expected_model_identity_sha256=expected_model_identity_sha256,
        expected_bundle_sha256=expected_bundle_sha256)
    return frozen.evaluate(cells, local, phi)
