#!/usr/bin/env python3
"""R696 complete angular-unit field, all free coordinates, and full J/J*.

The exact field is a centered angular primitive plus a radial scalar height:
V=exp([omega]x)et((1-lambda)theta0+lambda*psi_current),
C=int_0^phi rho0*V-ex*int_0^(pi/2)rho0*Vx,
F=a*C+[I+(J/Jstar)*(H-Istar)+r]ez.
I=int c, J=int c*w, w=S5(s/epsilon) near the core and one thereafter.
This is a NEW representation of the same fixed R690 scalar metric.
Every actual Gram entry is read. Numerical quadrature, inverse roots,
symbolic-domain carriers, and floating arithmetic are not certified here.
Importing this source performs no scientific calculation.
"""
from collections import OrderedDict
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np
import torch

SCHEMA = 'complete-R696-angular-unit-centered-field-v1'
REFERENCE_JET_SHA = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
TORCH_VERSION = '2.5.1'
HEIGHT_EPSILON = F(1, 20)
FIELD_KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')

def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific SO3 fields require the public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def tensor(value):
    return torch.as_tensor(np.array(value, dtype=np.float64, copy=True),
        dtype=torch.float64, device='cpu')


def hat(value):
    x, y, z = value.unbind(-1)
    zero = torch.zeros_like(x)
    return torch.stack((zero, -z, y, z, zero, -x, -y, x, zero), -1).reshape(
        value.shape[:-1]+(3, 3))


def rotation_coefficients(z):
    """A(z),B(z) and two z derivatives, including their removable origins."""
    # Safe arguments also protect the unused branch of torch.where and its
    # higher derivatives.  The small branch is the explicitly stated Taylor
    # evaluation; it is numerical evaluation, not an interval enclosure.
    small = z < .25
    safe = torch.clamp(z, min=.25)
    t = torch.sqrt(safe)
    sn, co = torch.sin(t), torch.cos(t)
    exact = (sn/t, (1-co)/safe,
        (t*co-sn)/(2*t**3), (t*sn-2*(1-co))/(2*t**4),
        (-t*t*sn-3*t*co+3*sn)/(4*t**5),
        (t*t*co-5*t*sn+8*(1-co))/(4*t**6))
    series = []
    for derivative in (0, 1, 2):
        for offset in (1, 2):
            result = torch.zeros_like(z)
            for power in range(12, derivative-1, -1):
                factor = math.factorial(power)//math.factorial(power-derivative)
                result = result*z+((-1.)**power)*factor/math.factorial(2*power+offset)
            series.append(result)
    return tuple(torch.where(small, polynomial, formula)
        for polynomial, formula in zip(series, exact))



def angular_unit_jets(w, ws, wss, wp, E, Es, Ess, Ep, *,
                      second_radial, angular_derivative):
    """Complete first/second radial and first angular jets of Exp(w)E."""
    z = (w*w).sum(-1)
    A, B, Az, Bz, Azz, Bzz = rotation_coefficients(z)
    W, Ws = hat(w), hat(ws)
    W2 = W@W
    expand = lambda value: value[..., None, None]
    eye = torch.eye(3, dtype=w.dtype, device=w.device)
    R = eye+expand(A)*W+expand(B)*W2
    zs = 2*(w*ws).sum(-1)
    Rs = (expand(Az*zs)*W+expand(A)*Ws+expand(Bz*zs)*W2
          +expand(B)*(Ws@W+W@Ws))
    apply = lambda matrix, vector: (matrix@vector[..., None])[..., 0]
    result = dict(V=apply(R, E), Vs=apply(Rs, E)+apply(R, Es))
    if second_radial:
        Wss = hat(wss)
        zss = 2*((ws*ws).sum(-1)+(w*wss).sum(-1))
        Rss = (expand(Azz*zs*zs+Az*zss)*W+expand(2*Az*zs)*Ws+expand(A)*Wss
            +expand(Bzz*zs*zs+Bz*zss)*W2
            +expand(2*Bz*zs)*(Ws@W+W@Ws)
            +expand(B)*(Wss@W+2*(Ws@Ws)+W@Wss))
        result['Vss'] = apply(Rss, E)+2*apply(Rs, Es)+apply(R, Ess)
    if angular_derivative:
        Wp = hat(wp)
        zp = 2*(w*wp).sum(-1)
        Rp = (expand(Az*zp)*W+expand(A)*Wp+expand(Bz*zp)*W2
              +expand(B)*(Wp@W+W@Wp))
        result['Vp'] = apply(Rp, E)+apply(R, Ep)
    return result


def positive_gauss(order):
    if int(order) != order or order < 4:
        raise ValueError('Use a declared complete Gauss order of at least four')
    root, weight = np.polynomial.legendre.leggauss(int(order))
    u, w = (root+1)/2, weight/2
    if (not np.isfinite(u).all() or not np.isfinite(w).all()
            or np.any(w <= 0) or np.any(u <= 0) or np.any(u >= 1)):
        raise ArithmeticError('Every auxiliary Gauss node and weight must be finite and positive')
    primitives = []
    for j in range(int(order)):
        p = np.polynomial.Polynomial([1.])
        for k in range(int(order)):
            if j != k:
                p *= np.polynomial.Polynomial([-u[k], 1.])/(u[j]-u[k])
        primitives.append(p.integ())
    return u, w, primitives


def smoothstep(u):
    return u*u*u*(10+u*(-15+6*u))


class ClosedMeridianOperator:
    """New angular representation; the public operator name is an API only."""
    def __init__(self, parent_problem, parent_prepared, parent_jet_module, *,
                 cache_directory, integration_order=8, angle_block=8,
                 root_iterations=18, root_tolerance=2.e-12,
                 angular_cells=128, angular_integration_order=8,
                 field_stage_block=16, initial_height=None,
                 expected_parent_bundle_sha256=None):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Use the declared CPU PyTorch '+TORCH_VERSION)
        if sha(parent_jet_module.__file__) != REFERENCE_JET_SHA:
            raise ValueError('Bind the complete actual independent reference source')
        if (int(angular_cells) != angular_cells or angular_cells < 1
                or int(angle_block) != angle_block or angle_block < 1
                or int(field_stage_block) != field_stage_block or field_stage_block < 1
                or int(root_iterations) != root_iterations or root_iterations < 4
                or not math.isfinite(root_tolerance) or root_tolerance <= 0):
            raise ValueError('Use explicit positive complete block, integration, and root parameters')
        self.parent, self.reference = parent_problem, parent_jet_module
        self.context = c = parent_problem.axisymmetric_reference_context
        if (c.model.get('schema') != 'R690-independent-axisymmetric-SO3-reference-input-v1'
                or c.model.get('source_sha256') != REFERENCE_JET_SHA
                or c.input_records['reference_bundle']['sha256'] != expected_parent_bundle_sha256
                or not np.array_equal(np.asarray(parent_prepared.core), c.core)):
            raise ValueError('Keep the actual reference, fixed chart, and scalar input')
        self.M, self.K, self.J = int(parent_problem.M), int(parent_problem.K), int(parent_problem.J)
        if self.K != 3 or self.M != 160 or self.J != 923:
            raise ValueError('The first angular entry keeps the complete original 923/160 input')
        self.n = 3*self.M+2
        self.mesh = np.array(parent_problem.mesh, dtype=float, copy=True)
        if (self.mesh.shape != (self.J,) or self.mesh[0] != 0
                or not np.isfinite(self.mesh).all() or np.any(np.diff(self.mesh) <= 0)):
            raise ValueError('Use the full original increasing symbolic-mesh carrier')
        self.S, self.R = float(self.mesh[-1]), float(parent_problem.R)
        if not self.S > float(HEIGHT_EPSILON):
            raise ValueError('The fixed scalar domain must contain the declared core height transition')
        self.P, self.N = int(parent_problem.P), int(parent_problem.N)
        self.full_N, self.legacy_P = int(parent_problem.full_N), int(parent_problem.legacy_P)
        self.phi = np.array(parent_problem.phi, copy=True)
        self.times = np.array(parent_problem.times, copy=True)
        self.observation_cells = np.array(parent_problem.observation_cells, copy=True)
        self.observation_u = np.array(parent_problem.observation_u, copy=True)
        self.multiplicity = np.array(parent_problem.multiplicity, copy=True)
        self.sqrt_multiplicity = np.sqrt(self.multiplicity)
        self.a = np.array(parent_problem.a, copy=True)
        self.stage_block = int(parent_problem.stage_block)
        if (self.N != self.full_N//4+1 or self.full_N != 2048 or self.P != 7377
                or self.a.shape != (self.P,) or np.any(self.a <= 0)
                or not np.isfinite(self.a).all() or self.multiplicity.sum() != self.full_N):
            raise ValueError('Retain every original positive observation and angular orbit')
        self.freq = 2*np.arange(1, self.M+1, dtype=float)
        self.qfreq = 1-self.freq**2
        self.parent_core = np.array(c.core, copy=True)
        self.fixed_core = tensor(self.parent_core[:self.K])
        self.core_size = self.M-self.K
        self.xy_channels, self.z_channels = 2*(self.M+1), self.M
        self.xy_free = np.arange(3, 3*(self.J-1), dtype=np.int64)
        self.z_free = np.arange(2, 3*(self.J-1), dtype=np.int64)
        self.profile_free = self.xy_free.copy()
        self.xy_size = len(self.xy_free)*self.xy_channels
        self.z_size = len(self.z_free)*self.z_channels
        self.rotation_size = self.xy_size+self.z_size
        self.profile_size = len(self.profile_free)
        self.free_size = self.core_size+self.rotation_size+self.profile_size+1
        if self.free_size != 1334847:
            raise ValueError('The complete R696 coordinate count changed')
        self._xy_free_torch = torch.tensor(self.xy_free, dtype=torch.long)
        self._z_free_torch = torch.tensor(self.z_free, dtype=torch.long)
        self._profile_free_torch = torch.tensor(self.profile_free, dtype=torch.long)
        self.angle_block, self.field_stage_block = int(angle_block), int(field_stage_block)
        self.root_iterations, self.root_tolerance = int(root_iterations), float(root_tolerance)
        self.integration_order = int(integration_order)
        self.angular_cells, self.angular_integration_order = int(angular_cells), int(angular_integration_order)
        self.gauss_u, self.gauss_w, self._partial_polynomials = positive_gauss(integration_order)
        self.angular_u, self.angular_w, self._angular_partial = positive_gauss(angular_integration_order)
        self.angular_width = (np.pi/2)/self.angular_cells
        self.angular_phi = ((np.arange(self.angular_cells)[:, None]+self.angular_u[None])
                            *self.angular_width).ravel()
        self.angular_full_weights = np.tile(self.angular_w*self.angular_width, self.angular_cells)
        self._hermite = c.observed.hermite_weights
        self.cache_directory = Path(cache_directory).resolve()
        if self.cache_directory == c.repo or c.repo in self.cache_directory.parents:
            raise ValueError('All scientific field caches must remain outside the repository')
        self.cache_directory.mkdir(parents=True, exist_ok=False)
        self._basis_cache, self._angle_plan_cache, self._inverse_cache = OrderedDict(), OrderedDict(), OrderedDict()
        self._query_cache, self._scalar_cache = {}, {}
        self._residual_cache = self._domain_cache = self._grid_cache = None
        self.maximum_inverse_root_residual = 0.
        self.minimum_inverse_root_rho = float('inf')
        self.maximum_scalar_a_error = 0.
        self.maximum_scalar_jet_errors = np.zeros(4)
        self.counts = dict(residual_calls=0, J_calls=0, Jtranspose_calls=0,
            point_covectors=0, evaluated_field_points=0, angular_integrand_points=0,
            actual_inverse_chart_solves=0, inverse_chart_cache_hits=0,
            scalar_queries=0, actual_full_grid_reads=0, grid_cache_hits=0)
        self._initial_height = float(c.height if initial_height is None else initial_height)
        if not math.isfinite(self._initial_height):
            raise ValueError('The declared new initial free height must be finite')
        self._a_observation_cache = {}
        for i, (cell, u) in enumerate(zip(self.observation_cells, self.observation_u)):
            key = (int(cell), float(u).hex())
            # Different observation rows at one address must already agree.
            if key in self._a_observation_cache and self._a_observation_cache[key] != float(self.a[i]):
                raise ValueError('The bound observation target has conflicting words at one address')
            self._a_observation_cache[key] = float(self.a[i])
        self._prepare_scalar_integrals()
        self.grid_query = self.make_query(self.observation_cells, self.observation_u)
        self.model = dict(schema=SCHEMA, source_sha256=sha(__file__),
            reference_meridian_kernel_sha256=REFERENCE_JET_SHA,
            fixed_scalar_metric_identity_sha256=c.scalar_identity,
            fixed_scalar_profile_definition=c.scalar_definition,
            initial_reference_bundle_sha256=c.input_records['reference_bundle']['sha256'],
            initial_reference_model_identity_sha256=c.identity,
            complete_axisymmetric_reference_model=c.model,
            fixed_chart_core_sha256=array_sha(self.parent_core),
            frozen_material_chart='theta0(phi)=Theta_actual_initial_reference_core(phi)',
            fixed_metric='ds^2+a_deep(s)^2*dtheta0^2',
            physical_S='same exact original S and affine nodes; binary mesh is only an evaluation carrier',
            M=self.M, J=self.J, mesh_sha256=array_sha(self.mesh),
            radius_hex=self.R.hex(), fixed_core_first3=[float(v).hex() for v in self.parent_core[:self.K]],
            omega_basis=dict(x='sin((2m+1)phi), m=0..M', y='cos((2m+1)phi), m=0..M',
                z='sin(2m phi), m=1..M', radial='complete shared C2 quintic physical node jets',
                xy_core_and_cap_three_jets_zero=True,
                z_core_value_slope_zero_second_derivative_free=True,
                z_cap_three_jets_zero=True),
            beta='theta0+(1-S5(s/S))*(psi_current-theta0)',
            unit_angular_tangent='V=Exp(omega cross)*et(beta)',
            centered_primitive='C=int_0^phi rho0*V-ex*int_0^(pi/2)rho0*Vx',
            vertical_profile=dict(I='int_0^s c(t)dt', J='int_0^s c(t)w(t)dt',
                w='S5(s/epsilon) on [0,epsilon], then 1', epsilon_exact=str(HEIGHT_EPSILON),
                height_basis='h=J/J(S)', z='I+h*(H-I(S))+r',
                r='all shared C2 quintic radial jets with both endpoint triples zero',
                r_independent_of_angle=True),
            field='F=a*C+z*ez', core='Gamma_current(psi_current); Theta_current(psi_current)=theta0',
            cap='unchanged fixed R661 p4 cap recipe at this true deep R and free H',
            all_current_free_core_coefficients_retained=True, current_height_free=True,
            all_free_radial_profile_jets_retained=True,
            angular_Gram_error_identically_zero=True, radial_Gram_error_identically_zero=False,
            closed_angular_sections_identically=True,
            rotation_gauge='right rotations about et(beta); full chart-pullback gauge retained',
            old_q_or_radial_unit_space_bijection_claimed=False,
            numerical_integration_rule_part_of_mathematical_target=False)
        self.identity = canonical(self.model)

    def initial(self):
        return np.r_[self.parent_core[self.K:],
            np.zeros(self.rotation_size+self.profile_size), self._initial_height]

    def unpack_complete(self, x):
        x = np.asarray(x, dtype=float)
        if x.shape != (self.free_size,) or not np.isfinite(x).all():
            raise ValueError('Use every finite core, rotation, radial-profile, and height variable')
        core = np.r_[self.parent_core[:self.K], x[:self.core_size]]
        first, last = self.core_size, self.core_size+self.xy_size
        xy = np.zeros((3*self.J, self.xy_channels))
        xy[self.xy_free] = x[first:last].reshape(len(self.xy_free), self.xy_channels)
        z = np.zeros((3*self.J, self.z_channels))
        z[self.z_free] = x[last:last+self.z_size].reshape(len(self.z_free), self.z_channels)
        profile = np.zeros(3*self.J)
        profile[self.profile_free] = x[last+self.z_size:-1]
        omega = np.c_[xy, z].reshape(self.J, 3, self.n)
        return core, omega, profile.reshape(self.J, 3), float(x[-1])

    def unpack(self, x):
        core, omega, _, height = self.unpack_complete(x)
        return core, omega, height

    def prepare(self, x):
        core, jets, profile, height = self.unpack_complete(x)
        return SimpleNamespace(x=np.asarray(x).copy(), core=core, jets=jets,
                               vertical_profile_jets=profile, height=height)

    def _unpack_torch(self, x):
        core = torch.cat((self.fixed_core, x[:self.core_size]))
        first, last = self.core_size, self.core_size+self.xy_size
        xy = torch.zeros((3*self.J, self.xy_channels), dtype=x.dtype, device=x.device).index_copy(
            0, self._xy_free_torch, x[first:last].reshape(len(self.xy_free), self.xy_channels))
        z = torch.zeros((3*self.J, self.z_channels), dtype=x.dtype, device=x.device).index_copy(
            0, self._z_free_torch, x[last:last+self.z_size].reshape(len(self.z_free), self.z_channels))
        profile = torch.zeros(3*self.J, dtype=x.dtype, device=x.device).index_copy(
            0, self._profile_free_torch, x[last+self.z_size:-1]).reshape(self.J, 3)
        return core, torch.cat((xy, z), dim=1).reshape(self.J, 3, self.n), profile, x[-1]

    @staticmethod
    def _limited_cache(cache, key, value, maximum):
        cache[key] = value
        cache.move_to_end(key)
        while len(cache) > maximum:
            cache.popitem(last=False)
        return value

    def _height_weight(self, s):
        u = np.clip(np.asarray(s, dtype=float)/float(HEIGHT_EPSILON), 0., 1.)
        w = smoothstep(u)
        derivative = 30*u*u*(1-u)*(1-u)/float(HEIGHT_EPSILON)
        return w, derivative

    def _prepare_scalar_integrals(self):
        """Actual complete auxiliary I/J words; neither integral is certified."""
        C, Q = self.J-1, self.integration_order
        cells, local = np.repeat(np.arange(C), Q), np.tile(self.gauss_u, C)
        values, errors = [], []
        for cell, u in zip(cells, local):
            v, e = self.context.reference_at(int(cell), float(u))
            values.append(v)
            errors.append(e)
        self._scalar_gauss_values = np.asarray(values).reshape(C, Q, 4)
        self._scalar_gauss_errors = np.asarray(errors).reshape(C, Q, 4)
        self.maximum_scalar_jet_errors = np.maximum(self.maximum_scalar_jet_errors,
            np.max(self._scalar_gauss_errors.reshape(-1, 4), axis=0))
        widths = np.diff(self.mesh)
        s = self.mesh[:-1, None]+widths[:, None]*self.gauss_u[None]
        w, _ = self._height_weight(s)
        cc = self._scalar_gauss_values[:, :, 1]
        self._I_integrand = cc.copy()
        self._J_integrand = cc*w
        self._I_cells = (self._I_integrand*self.gauss_w[None]).sum(1)*widths
        self._J_cells = (self._J_integrand*self.gauss_w[None]).sum(1)*widths
        self._I_prefix = np.r_[0., np.cumsum(self._I_cells)]
        self._J_prefix = np.r_[0., np.cumsum(self._J_cells)]
        self.Istar, self.Jstar = float(self._I_prefix[-1]), float(self._J_prefix[-1])
        if (not np.isfinite(self._scalar_gauss_values).all()
                or not np.isfinite(self._scalar_gauss_errors).all()
                or np.any(self._scalar_gauss_errors < 0)
                or not math.isfinite(self.Istar) or not math.isfinite(self.Jstar) or self.Jstar <= 0):
            raise ArithmeticError('The complete scalar I/J working integrals are invalid')
        carrier = self.context.input_records['carrier']['path']
        with np.load(carrier, allow_pickle=False) as data:
            observed_error = np.array(data['a_observation_absolute_error'], copy=True)
        if (observed_error.shape != (self.P,) or np.any(observed_error < 0)
                or not np.isfinite(observed_error).all()):
            raise ValueError('Keep the actual complete target-observation errors')
        self._a_error_cache = {}
        for cell, u, error in zip(self.observation_cells, self.observation_u, observed_error):
            key = (int(cell), float(u).hex())
            self._a_error_cache[key] = max(self._a_error_cache.get(key, 0.), float(error))
        self.maximum_scalar_a_error = float(np.max(observed_error))
        d, full = self.context.modules['deep_scalar'], self.context.full
        raw = self.context.model['radius_complete_enclosure']
        self._true_R = d.box(F(raw['lower_exact']), F(raw['upper_exact']))
        width, kappa = F(full.out), F(full.kp)
        if (not 0 < width < F(1, 40) or kappa != F(3, 2)
                or str(width) != self.context.scalar_definition['out_width_exact']):
            raise ValueError('Bind the actual exact original out-width, including its binary-rational definition')
        self._tail_anchor = width/4
        self._beta_max = width*kappa*F(29, 4096)
        # For x<=1/4, old P(x)<=29/4096. The deep beta is <=
        # kappa*width*exp(-16) <= kappa*width*24/16^4,
        # which is smaller. A convex cutoff preserves this full bound.
        if F(24, 16**4) >= F(29, 4096):
            raise ArithmeticError('The complete tail-angle elementary bound changed')
        old_anchor = full.at_box(full.affine_time(F(1), -self._tail_anchor))[0]
        self._anchor_a = d.box(F(old_anchor[0], full.h.S), F(old_anchor[1], full.h.S))
        self.scalar_integral_metadata = dict(
            rule='Every original radial cell, complete positive Gauss rule; exact Lagrange partial polynomials evaluated in binary64',
            radial_integration_order=Q, actual_complete_cells=C,
            c_values_are_original_unrenormalized_reference_carriers=True,
            Istar_working=self.Istar, Jstar_working=self.Jstar,
            height_transition_exact=str(HEIGHT_EPSILON),
            I_integrand_sha256=array_sha(self._I_integrand),
            J_integrand_sha256=array_sha(self._J_integrand),
            I_cell_words_sha256=array_sha(self._I_cells),
            J_cell_words_sha256=array_sha(self._J_cells),
            maximum_four_scalar_node_error_carriers=self.maximum_scalar_jet_errors.tolist(),
            scalar_integral_error_enclosed=False,
            whole_height_profile_error_enclosed=False,
            fixed_exact_height_basis='J(s)/J(S), with exact c and exact epsilon',
            conservative_tail_a_carrier_bound='R+[t*(1-beta_max^2/2),t], using true R box and exact affine t',
            complete_tail_beta_upper_exact=str(self._beta_max))

    def _a_at(self, cell, u, definition):
        key = (int(cell), float(u).hex())
        if key in self._a_observation_cache:
            return self._a_observation_cache[key], self._a_error_cache[key]
        d, full = self.context.modules['deep_scalar'], self.context.full
        alpha, beta = definition
        if definition == (F(0), F(0)):
            value = d.ONE
        elif definition == (F(1), F(0)):
            value = self._true_R
        else:
            Sbox = d.box(F(full.S[0], full.h.S), F(full.S[1], full.h.S))
            t = d.box(-beta) if alpha == 1 else d.sub(d.scale(Sbox, 1-alpha), d.box(beta))
            low, high = F(t[0], d.SCALE), F(t[1], d.SCALE)
            if low < 0:
                raise ValueError('An exact affine radial address reaches past the cap')
            if low >= self._tail_anchor:
                raw = full.at_box(full.affine_time(alpha, beta))[0]
                value = d.box(F(raw[0], full.h.S), F(raw[1], full.h.S))
            elif high <= self._tail_anchor:
                value = d.add(self._true_R,
                    d.box(low*(1-self._beta_max**2/2), high))
            else:
                fee = max(self._tail_anchor-low, high-self._tail_anchor)
                value = d.add(self._anchor_a, d.box(-fee, fee))
        word, error = self.reference.midpoint_and_error(value, d.SCALE)
        if not math.isfinite(word) or not math.isfinite(error) or word <= 0 or error < 0:
            raise ArithmeticError('The complete arbitrary-point scalar carrier is invalid')
        self.maximum_scalar_a_error = max(self.maximum_scalar_a_error, error)
        return word, error

    def make_query(self, cells, local, *, integration_query=False):
        require_actions()
        cells, local = np.asarray(cells, dtype=np.int64), np.asarray(local, dtype=float)
        if (cells.ndim != 1 or cells.shape != local.shape or not len(cells)
                or np.any(cells < 0) or np.any(cells >= self.J-1)
                or not np.isfinite(local).all() or np.any(local < 0) or np.any(local > 1)):
            raise ValueError('Use complete finite original cell/local addresses')
        key = tuple((int(c), float(u).hex()) for c, u in zip(cells, local))
        if key in self._query_cache:
            return self._query_cache[key]
        widths = self.mesh[cells+1]-self.mesh[cells]
        s = self.mesh[cells]+widths*local
        weights = np.array([self._hermite(h, u) for h, u in zip(widths, local)])
        partial = np.array([[h*(p(u)-p(0.)) for p in self._partial_polynomials]
                            for h, u in zip(widths, local)])
        scalar, scalar_errors, aa, ae = [], [], [], []
        for cell, u in zip(cells, local):
            definition = self.reference.point_definition(self.context.nodes, int(cell), float(u))
            value, error = self.context.reference_at(int(cell), float(u))
            scalar.append(value)
            scalar_errors.append(error)
            aword, aerror = self._a_at(int(cell), float(u), definition)
            aa.append(aword)
            ae.append(aerror)
        scalar, scalar_errors, aa = np.asarray(scalar), np.asarray(scalar_errors), np.asarray(aa)
        self.maximum_scalar_jet_errors = np.maximum(self.maximum_scalar_jet_errors, scalar_errors.max(0))
        self.counts['scalar_queries'] += len(cells)
        I = self._I_prefix[cells]+np.sum(partial*self._I_integrand[cells], axis=1)
        J = self._J_prefix[cells]+np.sum(partial*self._J_integrand[cells], axis=1)
        core_mask = (cells == 0)&(local == 0.)
        cap_mask = (cells == self.J-2)&(local == 1.)
        I[core_mask], J[core_mask] = 0., 0.
        I[cap_mask], J[cap_mask] = self.Istar, self.Jstar
        b, cc, bs, cs = scalar.T
        w, wp = self._height_weight(s)
        h, hp, hpp = J/self.Jstar, cc*w/self.Jstar, (cs*w+cc*wp)/self.Jstar
        h[core_mask], hp[core_mask], hpp[core_mask] = 0., 0., 0.
        h[cap_mask], hp[cap_mask], hpp[cap_mask] = 1., 0., 0.
        t = s/self.S
        lam = 1-smoothstep(t)
        lamp = -30*t*t*(1-t)*(1-t)/self.S
        lampp = -60*t*(1-t)*(1-2*t)/(self.S*self.S)
        lam[core_mask], lamp[core_mask], lampp[core_mask] = 1., 0., 0.
        lam[cap_mask], lamp[cap_mask], lampp[cap_mask] = 0., 0., 0.
        values = dict(a=aa, b=b, c=cc, bs=bs, cs=cs, I=I, J=J, h=h, hp=hp,
            hpp=hpp, lam=lam, lamp=lamp, lampp=lampp)
        if any(not np.isfinite(value).all() for value in values.values()):
            raise FloatingPointError('A full scalar query returned a nonfinite value')
        selected = np.unique(np.r_[cells, cells+1])
        lookup = np.empty(self.J, dtype=np.int64)
        lookup[selected] = np.arange(len(selected))
        result = dict(cells=cells.copy(), local=local.copy(), s=s, widths=widths,
            weights=tensor(weights), partial=partial, selected_nodes=selected,
            selected_nodes_torch=torch.tensor(selected, dtype=torch.long),
            left_torch=torch.tensor(lookup[cells], dtype=torch.long),
            right_torch=torch.tensor(lookup[cells+1], dtype=torch.long),
            core_mask=torch.tensor(core_mask), cap_mask=torch.tensor(cap_mask),
            scalar={name:tensor(value) for name,value in values.items()},
            maximum_a_error=max(ae), scalar_error_carriers=scalar_errors)
        self._query_cache[key] = result
        return result

    def _radial(self, values, query, order):
        selected = values.index_select(0, query['selected_nodes_torch'])
        ends = torch.stack((selected[query['left_torch']], selected[query['right_torch']]), 1)
        ends = ends.reshape((len(query['cells']), 6)+tuple(values.shape[2:]))
        shape = (len(query['cells']), 6)+(1,)*(ends.ndim-2)
        return (ends*query['weights'][:, order].reshape(shape)).sum(1)

    def _from_selected(self, values, query, order):
        ends = torch.stack((values[query['left_torch']], values[query['right_torch']]), 1)
        ends = ends.reshape((len(query['cells']), 6)+tuple(values.shape[2:]))
        shape = (len(query['cells']), 6)+(1,)*(ends.ndim-2)
        return (ends*query['weights'][:, order].reshape(shape)).sum(1)

    def _angular_basis(self, phi, order):
        phi = np.asarray(phi, dtype=float)
        key = (int(order), tuple(float(v).hex() for v in phi))
        if key in self._basis_cache:
            self._basis_cache.move_to_end(key)
            return self._basis_cache[key]
        p = tensor(phi)
        odd, even = tensor(2*np.arange(self.M+1)+1), tensor(self.freq)
        a, b = p[:, None]*odd[None], p[:, None]*even[None]
        if order == 0:
            answer = torch.sin(a), torch.cos(a), torch.sin(b)
        elif order == 1:
            answer = torch.cos(a)*odd, -torch.sin(a)*odd, torch.cos(b)*even
        else:
            raise ValueError('This full six-jet representation uses angular orders zero and one')
        return self._limited_cache(self._basis_cache, key, answer, 12)

    def _angular_values(self, jets, phi, order):
        bx, by, bz = self._angular_basis(phi, order)
        first = self.M+1
        return torch.stack((jets[..., :first]@bx.T,
            jets[..., first:2*first]@by.T, jets[..., 2*first:]@bz.T), dim=-1)

    def _angle_plan(self, phi):
        phi = np.asarray(phi, dtype=float)
        if phi.ndim != 1 or not len(phi) or not np.isfinite(phi).all():
            raise ValueError('Use complete finite literal angular query addresses')
        key = tuple(float(v).hex() for v in phi)
        if key in self._angle_plan_cache:
            self._angle_plan_cache.move_to_end(key)
            return self._angle_plan_cache[key]
        quarter = np.pi/2
        left_count = max(0, int(math.ceil(-float(np.min(phi))/self.angular_width)))
        right_count = max(0, int(math.ceil((float(np.max(phi))-quarter)/self.angular_width)))
        pieces = []
        if left_count:
            lower = min(-left_count*self.angular_width, float(np.min(phi)))
            pieces.append(np.linspace(lower, 0., left_count+1)[:-1])
        pieces.append(np.linspace(0., quarter, self.angular_cells+1))
        if right_count:
            upper = max(quarter+right_count*self.angular_width, float(np.max(phi)))
            pieces.append(np.linspace(quarter, upper, right_count+1)[1:])
        edges = np.concatenate(pieces)
        widths = np.diff(edges)
        if (not np.isfinite(edges).all() or np.any(widths <= 0)
                or edges[0] > np.min(phi) or edges[-1] < np.max(phi)):
            raise ArithmeticError('Every requested angular primitive interval must be covered')
        nodes = (edges[:-1, None]+widths[:, None]*self.angular_u[None]).ravel()
        full_weights = (widths[:, None]*self.angular_w[None]).ravel()
        Q = self.angular_integration_order

        def row(t):
            cell = min(len(widths)-1, max(0, int(np.searchsorted(edges, t, side='right')-1)))
            u = (t-edges[cell])/widths[cell]
            if not 0 <= u <= 1:
                raise ArithmeticError('An actual partial angular interval left its complete cell')
            result = np.zeros(len(nodes))
            result[:cell*Q] = full_weights[:cell*Q]
            result[cell*Q:(cell+1)*Q] = widths[cell]*np.array([
                p(u)-p(0.) for p in self._angular_partial])
            # At an actual cell endpoint, reuse the actual full-cell weights.
            if t == edges[cell+1]:
                result[cell*Q:(cell+1)*Q] = full_weights[cell*Q:(cell+1)*Q]
            return result

        origin = row(0.)
        weights = np.array([row(float(t))-origin for t in phi])
        center = row(quarter)-origin
        result = dict(phi=phi.copy(), nodes=nodes, weights=tensor(weights),
            center=tensor(center), actual_cells=len(widths),
            complete_positive_full_weights=full_weights,
            exact_definition='integral_0^phi rho0*V, centered by its x integral to exact pi/2',
            ordinary_pi_and_partial_quadrature_errors_enclosed=False)
        return self._limited_cache(self._angle_plan_cache, key, result, 20)

    def _chart(self, core, phi):
        phi = np.asarray(phi, dtype=float)
        core_words = np.array(core.detach().cpu().numpy(), copy=True)
        key = (array_sha(core_words), tuple(float(v).hex() for v in phi))
        if key in self._inverse_cache:
            root = self._inverse_cache[key]
            self._inverse_cache.move_to_end(key)
            self.counts['inverse_chart_cache_hits'] += len(phi)
        else:
            nu, qnu = self.freq, self.qfreq
            theta0_words = phi+np.sin(phi[:, None]*nu[None])@((qnu/nu)*self.parent_core)
            amplitude = float(np.sum(np.abs((qnu/nu)*core_words)))
            lower, upper = theta0_words-amplitude-1.e-14, theta0_words+amplitude+1.e-14
            pc = np.clip(phi, lower, upper)
            actual_iterations = 0
            for iteration in range(self.root_iterations):
                phase = pc[:, None]*nu[None]
                value = pc+np.sin(phase)@((qnu/nu)*core_words)-theta0_words
                rho = 1+np.cos(phase)@(qnu*core_words)
                if (not np.isfinite(value).all() or not np.isfinite(rho).all()
                        or np.any(rho <= 0)):
                    raise ValueError('The actual current inverse chart left its positive finite domain')
                actual_iterations = iteration+1
                if np.max(np.abs(value)) <= self.root_tolerance:
                    break
                lower = np.where(value < 0, pc, lower)
                upper = np.where(value > 0, pc, upper)
                candidate = pc-value/rho
                use = np.isfinite(candidate)&(candidate > lower)&(candidate < upper)
                pc = np.where(use, candidate, (lower+upper)/2)
            root = dict(pc=pc.copy(), actual_iterations=actual_iterations)
            self._limited_cache(self._inverse_cache, key, root, 24)
            self.counts['actual_inverse_chart_solves'] += len(phi)
        nu, qnu, p = tensor(self.freq), tensor(self.qfreq), tensor(phi)
        phase0 = p[:, None]*nu[None]
        theta0 = p+(torch.sin(phase0)*(qnu/nu)*tensor(self.parent_core)).sum(-1)
        rho0 = 1+(torch.cos(phase0)*qnu*tensor(self.parent_core)).sum(-1)
        rhop0 = -(torch.sin(phase0)*nu*qnu*tensor(self.parent_core)).sum(-1)
        fixed_root = tensor(root['pc'])
        fixed_phase = fixed_root[:, None]*nu[None]
        numerator = theta0-fixed_root-(torch.sin(fixed_phase)*(qnu/nu)*core).sum(-1)
        denominator = 1+(torch.cos(fixed_phase)*qnu*core).sum(-1)
        # Value preserving implicit surrogate: the value is the actually
        # solved root; its full first parameter derivative is -DTheta/rho.
        # The finite root residual is still measured and remains unpaid.
        pc = fixed_root+(numerator-numerator.detach())/denominator
        phase = pc[:, None]*nu[None]
        rho = 1+(torch.cos(phase)*qnu*core).sum(-1)
        equation = pc+(torch.sin(phase)*(qnu/nu)*core).sum(-1)-theta0
        root_error = float(equation.detach().abs().max())
        rho_min = float(rho.detach().min())
        if (not math.isfinite(root_error) or root_error > self.root_tolerance
                or not math.isfinite(rho_min) or rho_min <= 0
                or not bool(torch.isfinite(pc.detach()).all())
                or not bool(torch.isfinite(rho0).all()) or bool((rho0 <= 0).any())):
            raise ValueError('The actual complete inverse chart did not meet its declared working tolerance')
        self.maximum_inverse_root_residual = max(self.maximum_inverse_root_residual, root_error)
        self.minimum_inverse_root_rho = min(self.minimum_inverse_root_rho, rho_min)
        zero = torch.zeros_like(pc)
        er = torch.stack((torch.cos(pc), torch.sin(pc), zero), -1)
        et = torch.stack((-torch.sin(pc), torch.cos(pc), zero), -1)
        er0 = torch.stack((torch.cos(theta0), torch.sin(theta0), zero), -1)
        et0 = torch.stack((-torch.sin(theta0), torch.cos(theta0), zero), -1)
        support = 1+(torch.cos(phase)*core).sum(-1)
        support_p = -(torch.sin(phase)*nu*core).sum(-1)
        return dict(theta0=theta0, rho0=rho0, rhop0=rhop0, psi=pc, rho=rho,
            er=er, et=et, er0=er0, et0=et0,
            Gamma=support[:, None]*er+support_p[:, None]*et,
            Gammap=rho0[:, None]*et,
            Gammapp=rhop0[:, None]*et-(rho0*rho0/rho)[:, None]*er)

    def _units(self, core, omega, query, phi, *, curvature, need_phi):
        chart = self._chart(core, phi)
        scalar = query['scalar']
        delta = chart['psi']-chart['theta0']
        beta = chart['theta0'][None]+scalar['lam'][:, None]*delta[None]
        beta = torch.where(query['core_mask'][:, None], chart['psi'][None], beta)
        beta = torch.where(query['cap_mask'][:, None], chart['theta0'][None], beta)
        bs = scalar['lamp'][:, None]*delta[None]
        bss = scalar['lampp'][:, None]*delta[None]
        bp = chart['rho0'][None]*(1-scalar['lam'][:, None]
                                     +scalar['lam'][:, None]/chart['rho'][None])
        zero = torch.zeros_like(beta)
        er = torch.stack((torch.cos(beta), torch.sin(beta), zero), -1)
        E = torch.stack((-torch.sin(beta), torch.cos(beta), zero), -1)
        Es = -bs[..., None]*er
        Ess = -bss[..., None]*er-bs[..., None]**2*E if curvature else None
        Ep = -bp[..., None]*er if need_phi else None
        selected = omega.index_select(0, query['selected_nodes_torch'])
        nodes = self._angular_values(selected, phi, 0)
        w = self._from_selected(nodes, query, 0)
        ws = self._from_selected(nodes, query, 1)
        wss = self._from_selected(nodes, query, 2) if curvature else None
        wp = (self._from_selected(self._angular_values(selected, phi, 1), query, 0)
              if need_phi else None)
        return angular_unit_jets(w, ws, wss, wp, E, Es, Ess, Ep,
            second_radial=curvature, angular_derivative=need_phi), chart

    @staticmethod
    def _centered_integral(values, rho0, plan):
        integrand = values*rho0[None, :, None]
        partial = torch.einsum('aq,pqj->paj', plan['weights'], integrand)
        center = torch.einsum('q,pq->p', plan['center'], integrand[..., 0])
        ex = tensor([1., 0., 0.])
        return partial-center[:, None, None]*ex

    def fields_torch(self, x, query, phi, *, curvature=True, query_label=None):
        require_actions()
        core, omega, profile, height = self._unpack_torch(x)
        plan = self._angle_plan(phi)
        integral_units, integral_chart = self._units(core, omega, query, plan['nodes'],
            curvature=curvature, need_phi=False)
        actual_units, chart = self._units(core, omega, query, plan['phi'],
            curvature=curvature, need_phi=curvature)
        C = self._centered_integral(integral_units['V'], integral_chart['rho0'], plan)
        Cs = self._centered_integral(integral_units['Vs'], integral_chart['rho0'], plan)
        Css = (self._centered_integral(integral_units['Vss'], integral_chart['rho0'], plan)
               if curvature else None)
        cm, sm = query['core_mask'][:, None, None], query['cap_mask'][:, None, None]
        # These are the exact R696 endpoint identities, evaluated directly.
        # They keep every permitted core/Css parameter derivative.
        C = torch.where(cm, chart['Gamma'][None], C)
        C = torch.where(sm, chart['er0'][None], C)
        Cs = torch.where(cm|sm, torch.zeros_like(Cs), Cs)
        if curvature:
            horizontal = tensor([1., 1., 0.])
            Css = torch.where(cm, Css*horizontal, Css)
            Css = torch.where(sm, torch.zeros_like(Css), Css)
        scalar = query['scalar']
        rr = self._radial(profile, query, 0)
        rs = self._radial(profile, query, 1)
        rss = self._radial(profile, query, 2) if curvature else None
        dz = height-self.Istar
        zz = scalar['I']+scalar['h']*dz+rr
        zs = scalar['c']+scalar['hp']*dz+rs
        zss = scalar['cs']+scalar['hpp']*dz+rss if curvature else None
        # Endpoint vertical values follow the same exact formulas; their
        # direct evaluation avoids a needless H-Istar+Istar cancellation.
        zz = torch.where(query['core_mask'], torch.zeros_like(zz), zz)
        zz = torch.where(query['cap_mask'], height.expand_as(zz), zz)
        zs = torch.where(query['core_mask'], torch.ones_like(zs), zs)
        zs = torch.where(query['cap_mask'], torch.zeros_like(zs), zs)
        if curvature:
            zss = torch.where(query['core_mask']|query['cap_mask'], torch.zeros_like(zss), zss)
        ez = tensor([0., 0., 1.])
        a, b = scalar['a'][:, None, None], scalar['b'][:, None, None]
        rho = chart['rho0'][None, :, None]
        result = dict(F=a*C+zz[:, None, None]*ez,
            Fs=b*C+a*Cs+zs[:, None, None]*ez,
            Fphi=a*rho*actual_units['V'], rho0=chart['rho0'])
        if curvature:
            result.update(Fss=scalar['bs'][:, None, None]*C+2*b*Cs+a*Css+zss[:, None, None]*ez,
                Fsphi=rho*(b*actual_units['V']+a*actual_units['Vs']),
                Fphiphi=a*(chart['rhop0'][None, :, None]*actual_units['V']
                                  +rho*actual_units['Vp']))
        self.counts['evaluated_field_points'] += len(query['cells'])*len(plan['phi'])
        self.counts['angular_integrand_points'] += len(query['cells'])*len(plan['nodes'])
        return result

    def _stage_blocks(self):
        for begin in range(0, self.P, self.field_stage_block):
            yield begin, min(begin+self.field_stage_block, self.P)

    def _stage_query(self, begin, end):
        return self.make_query(self.observation_cells[begin:end], self.observation_u[begin:end])

    def _raw_stage(self, x, begin, end):
        fields = self.fields_torch(x, self._stage_query(begin, end), self.phi, curvature=False)
        V, W = fields['Fs'], fields['Fphi']
        denominator = tensor(self.a[begin:end])[:, None]*fields['rho0'][None]
        e = (V*V).sum(-1)-1
        f = (V*W).sum(-1)/denominator
        g = (W*W).sum(-1)/(denominator*denominator)-1
        return torch.stack((e, f, g), -1)*tensor(self.sqrt_multiplicity)[None, :, None]

    def residual(self, x):
        require_actions()
        self.counts['residual_calls'] += 1
        x = np.asarray(x, dtype=float)
        if self._residual_cache is not None and np.array_equal(x, self._residual_cache[0]):
            return self._residual_cache[1].copy()
        self.domain(x)
        answer = np.empty((self.P, self.N, 3))
        with torch.no_grad():
            xt = tensor(x)
            for begin, end in self._stage_blocks():
                answer[begin:end] = self._raw_stage(xt, begin, end).detach().numpy()
        if not np.isfinite(answer).all():
            raise FloatingPointError('Nonfinite complete R696 three-entry Gram')
        self._residual_cache = x.copy(), answer.copy()
        return answer

    def unweight(self, native):
        return np.asarray(native).reshape(self.P, self.N, 3)/self.sqrt_multiplicity[None, :, None]

    def jvp(self, x, direction):
        require_actions()
        self.counts['J_calls'] += 1
        self.domain(x)
        if np.asarray(direction).shape != (self.free_size,) or not np.isfinite(direction).all():
            raise ValueError('Use every finite full R696 direction coordinate')
        answer = np.empty((self.P, self.N, 3))
        xt, dt = tensor(x), tensor(direction)
        for begin, end in self._stage_blocks():
            _, product = torch.autograd.functional.jvp(
                lambda value: self._raw_stage(value, begin, end), xt, dt,
                create_graph=False, strict=False)
            answer[begin:end] = product.detach().numpy()
        if not np.isfinite(answer).all():
            raise FloatingPointError('Nonfinite complete angular-field J product')
        return answer

    def vjp(self, x, cotangent):
        require_actions()
        self.counts['Jtranspose_calls'] += 1
        self.domain(x)
        cotangent = np.asarray(cotangent).reshape(self.P, self.N, 3)
        if not np.isfinite(cotangent).all():
            raise ValueError('Use a finite complete three-entry residual cotangent')
        answer = np.zeros(self.free_size)
        for begin, end in self._stage_blocks():
            xt = tensor(x).requires_grad_(True)
            value = self._raw_stage(xt, begin, end)
            gradient, = torch.autograd.grad(value, xt, tensor(cotangent[begin:end]),
                                            create_graph=False, retain_graph=False)
            answer += gradient.detach().numpy()
        if not np.isfinite(answer).all():
            raise FloatingPointError('Nonfinite complete angular-field transpose product')
        return answer

    def grid_fields(self, x):
        require_actions()
        self.domain(x)
        token = array_sha(np.asarray(x, dtype=float))
        if self._grid_cache is None or self._grid_cache['point'] != token:
            if self._grid_cache is not None:
                self._grid_cache['array']._mmap.close()
            self._grid_cache = None
            path = self.cache_directory/'same-field-complete-six-jets.dat'
            values = np.memmap(path, dtype=np.float64, mode='w+',
                shape=(len(FIELD_KEYS), self.P, self.N, 3))
            try:
                with torch.no_grad():
                    xt = tensor(x)
                    for begin, end in self._stage_blocks():
                        fields = self.fields_torch(xt, self._stage_query(begin, end),
                                                   self.phi, curvature=True)
                        for index, name in enumerate(FIELD_KEYS):
                            block = fields[name].detach().numpy()
                            if block.shape != (end-begin, self.N, 3) or not np.isfinite(block).all():
                                raise FloatingPointError('An actual complete R696 grid jet is invalid')
                            values[index, begin:end] = block
                        rho0 = np.array(fields['rho0'].detach().numpy(), copy=True)
                values.flush()
                self._grid_cache = dict(point=token, array=values, rho0=rho0, path=path)
                self.counts['actual_full_grid_reads'] += 1
            except Exception:
                values._mmap.close()
                raise
        else:
            self.counts['grid_cache_hits'] += 1
        for begin in range(0, self.N, self.angle_block):
            end = min(begin+self.angle_block, self.N)
            fields = {name:self._grid_cache['array'][index, :, begin:end]
                      for index, name in enumerate(FIELD_KEYS)}
            fields['rho0'] = self._grid_cache['rho0'][begin:end]
            yield begin, end, fields

    def _point_query(self, cell, u):
        return self.make_query([int(cell)], [float(u)])

    def point_fields(self, x, cell, u, phi):
        require_actions()
        self.domain(x)
        with torch.no_grad():
            result = self.fields_torch(tensor(x), self._point_query(cell, u),
                                       [float(phi)], curvature=True)
            answer = {name:np.array(result[name][0, 0].detach().numpy(), copy=True)
                      for name in FIELD_KEYS}
        if any(not np.isfinite(value).all() for value in answer.values()):
            raise FloatingPointError('Nonfinite full R696 point jet')
        return answer

    def point_vjp(self, x, cell, u, phi, cotangent):
        require_actions()
        self.counts['point_covectors'] += 1
        self.domain(x)
        if (set(cotangent) != set(FIELD_KEYS)
                or any(np.asarray(v).shape != (3,) or not np.isfinite(v).all()
                       for v in cotangent.values())):
            raise ValueError('Use the complete finite six-world-jet point covector')
        xt = tensor(x).requires_grad_(True)
        result = self.fields_torch(xt, self._point_query(cell, u), [float(phi)], curvature=True)
        loss = sum((result[key][0, 0]*tensor(value)).sum() for key, value in cotangent.items())
        gradient, = torch.autograd.grad(loss, xt, create_graph=False, retain_graph=False)
        answer = gradient.detach().numpy()
        if answer.shape != (self.free_size,) or not np.isfinite(answer).all():
            raise FloatingPointError('The full R696 point pullback omitted a free coordinate')
        return answer

    def domain(self, x):
        require_actions()
        x = np.asarray(x, dtype=float)
        if self._domain_cache is not None and np.array_equal(x, self._domain_cache[0]):
            return dict(self._domain_cache[1])
        core, omega, profile, height = self.unpack_complete(x)
        count = max(16384, 8*self.full_N)
        angles = np.arange(count)*2*np.pi/count
        minimum = float('inf')
        for start in range(0, count, 512):
            rho = 1+np.cos(angles[start:start+512, None]*self.freq[None])@(self.qfreq*core)
            minimum = min(minimum, float(rho.min()))
        if not math.isfinite(minimum) or minimum <= 0 or not math.isfinite(height):
            raise ValueError('Current complete core fails its declared positive-chart sample domain')
        result = dict(core_rho_sample_min=minimum, core_domain_angles=count,
            continuous_core_rho_certified=False, H=height,
            all_free_core_coefficients=self.core_size,
            all_free_rotation_coefficients=self.rotation_size,
            all_free_radial_profile_coefficients=self.profile_size,
            inverse_chart_iterations=self.root_iterations,
            inverse_chart_tolerance=self.root_tolerance)
        self._domain_cache = x.copy(), result
        return dict(result)

    def mixed_stage_weights(self, fraction):
        return self.parent.mixed_stage_weights(fraction)

    def _working_definition(self):
        return dict(radial_integration_order=self.integration_order,
            angular_integration_cells=self.angular_cells,
            angular_integration_order=self.angular_integration_order,
            field_stage_block=self.field_stage_block, angle_block=self.angle_block,
            inverse_root_iterations=self.root_iterations, inverse_root_tolerance=self.root_tolerance,
            original_full_angles=self.full_N, Istar_hex=self.Istar.hex(), Jstar_hex=self.Jstar.hex(),
            radial_gauss_u_sha256=array_sha(self.gauss_u),
            radial_gauss_w_sha256=array_sha(self.gauss_w),
            angular_gauss_u_sha256=array_sha(self.angular_u),
            angular_gauss_w_sha256=array_sha(self.angular_w),
            full_scalar_integral_metadata=self.scalar_integral_metadata)

    def save(self, path, x):
        require_actions()
        core, omega, profile, height = self.unpack_complete(x)
        working = self._working_definition()
        np.savez(path, schema=np.array(SCHEMA), omega_jets=omega,
            vertical_profile_jets=profile, core=core, Hcap=np.array(height),
            mesh=self.mesh, fixed_chart_core=self.parent_core,
            angular_model_json=np.array(json.dumps(self.model,sort_keys=True,separators=(',',':'))),
            angular_model_identity_sha256=np.array(self.identity),
            working_definition_json=np.array(json.dumps(working,sort_keys=True,separators=(',',':'))),
            working_definition_identity_sha256=np.array(canonical(working)),
            fixed_scalar_metric_identity_sha256=np.array(self.context.scalar_identity))

    def load_checkpoint(self, path):
        require_actions()
        with np.load(path, allow_pickle=False) as data:
            working = json.loads(str(data['working_definition_json'].item()))
            if (str(data['schema'].item()) != SCHEMA
                    or str(data['angular_model_identity_sha256'].item()) != self.identity
                    or json.loads(str(data['angular_model_json'].item())) != self.model
                    or working != self._working_definition()
                    or str(data['working_definition_identity_sha256'].item()) != canonical(working)
                    or not np.array_equal(data['mesh'], self.mesh)
                    or not np.array_equal(data['fixed_chart_core'], self.parent_core)
                    or not np.array_equal(data['core'][:self.K], self.parent_core[:self.K])
                    or data['omega_jets'].shape != (self.J,3,self.n)
                    or data['vertical_profile_jets'].shape != (self.J,3)):
                raise ValueError('Continuation requires this identical complete new field and working definition')
            omega = np.array(data['omega_jets'],copy=True).reshape(3*self.J,self.n)
            profile = np.array(data['vertical_profile_jets'],copy=True).reshape(3*self.J)
            blocked_xy = np.r_[np.arange(3), np.arange(3*(self.J-1),3*self.J)]
            blocked_z = np.r_[np.arange(2), np.arange(3*(self.J-1),3*self.J)]
            if (np.any(omega[blocked_xy,:self.xy_channels] != 0)
                    or np.any(omega[blocked_z,self.xy_channels:] != 0)
                    or np.any(profile[blocked_xy] != 0)):
                raise ValueError('A structural core/cap endpoint jet changed')
            answer = np.r_[data['core'][self.K:],
                omega[self.xy_free,:self.xy_channels].ravel(),
                omega[self.z_free,self.xy_channels:].ravel(),
                profile[self.profile_free],float(data['Hcap'])]
        self.unpack_complete(answer)
        return answer

    def clear_base(self):
        self._residual_cache = None

    def metadata(self):
        finite = lambda value: float(value) if math.isfinite(float(value)) else None
        return dict(schema=SCHEMA, source_sha256=sha(__file__), model=self.model,
            model_identity_sha256=self.identity,
            axisymmetric_reference_binding=self.context.input_records,
            free_variables=self.free_size, free_core_variables=self.core_size,
            free_rotation_variables=self.rotation_size,
            free_radial_profile_variables=self.profile_size, all_free_height_variables=1,
            initial_height_word=self._initial_height,
            working_definition=self._working_definition(),
            numerical_inverse_chart_method='safeguarded real Newton; value-preserving full first-parameter implicit surrogate',
            maximum_actual_inverse_chart_residual=self.maximum_inverse_root_residual,
            minimum_actual_inverse_root_rho=finite(self.minimum_inverse_root_rho),
            inverse_root_error_enclosed=False,
            angular_integral_and_center_error_enclosed=False,
            scalar_height_integral_error_enclosed=False,
            scalar_a_carrier_error_upper=self.maximum_scalar_a_error,
            maximum_four_scalar_jet_error_carriers=self.maximum_scalar_jet_errors.tolist(),
            symbolic_mesh_and_lambda_carrier_error_enclosed=False,
            full_field_arithmetic_error_enclosed=False,
            endpoint_identity_direct_evaluation=True,
            actual_all_three_Gram_entries_read=True, working_angular_Gram_forced_to_zero=False,
            stage_block=self.field_stage_block, output_angle_block=self.angle_block,
            actual_counts=dict(self.counts),
            torch_version=torch.__version__,torch_device='cpu',torch_dtype='float64',
            J_method='complete first-parameter AD through all centered integrals, radial profile, core implicit chain, and H',
            Jtranspose_method='transpose of that same complete declared working first-variation graph',
            finite_difference_J=False,
            old_metric_or_geometry_certificates_inherited=False,
            closed_exact_isometry_certified=False)


class RotationH2Coordinates:
    """Explicit full R696 positive node-jet norm; no old-space norm claim."""
    def __init__(self, problem, *, radial_length=.05, angular_transition=24.,
                 norm_kind='jet-sum'):
        require_actions()
        if (norm_kind != 'jet-sum' or not math.isfinite(radial_length) or radial_length <= 0
                or not math.isfinite(angular_transition) or angular_transition <= 0):
            raise ValueError('The first complete angular entry uses its explicit positive jet-sum norm')
        self.problem = q = problem
        self.size = q.free_size
        self.norm_kind = norm_kind
        self.radial_length, self.angular_transition = float(radial_length), float(angular_transition)
        widths = np.diff(q.mesh)
        mass = np.r_[widths[0]/2, (widths[:-1]+widths[1:])/2, widths[-1]/2]
        all_diagonal = (mass[:, None]*np.array([1., radial_length**2, radial_length**4])[None]).ravel()
        if not np.isfinite(all_diagonal).all() or np.any(all_diagonal <= 0):
            raise ArithmeticError('Every free radial node jet needs an actual positive finite norm weight')
        self.xy_diagonal = 1/np.sqrt(all_diagonal[q.xy_free])
        self.z_diagonal = 1/np.sqrt(all_diagonal[q.z_free])
        self.profile_diagonal = 1/np.sqrt(all_diagonal[q.profile_free])
        odd = 2*np.arange(q.M+1)+1
        self.xy_sigma = np.sqrt(1+(np.r_[odd, odd]/angular_transition)**2)
        self.z_sigma = np.sqrt(1+(q.freq/angular_transition)**2)
        self.core_scale = 1/np.maximum(1., np.abs(q.qfreq[q.K:]))
        self.record = dict(schema='complete-R696-positive-node-jet-H2-type-norm-v1',
            norm_kind=norm_kind, radial_length=radial_length, angular_transition=angular_transition,
            norm='sum_rotation node_mass*sigma(actual_frequency)^2*(domega^2+ell^2*domega_s^2+ell^4*domega_ss^2) + sum_radial_profile node_mass*(dr^2+ell^2*dr_s^2+ell^4*dr_ss^2) + sum_free_core((1-nu^2)dc)^2+dH^2',
            exact_radial_Sobolev_integral=False,
            all_free_core_rotation_radial_profile_and_height_retained=True,
            original_q_or_radial_unit_mother_norm_claimed_unchanged=False,
            rotation_gauge_removed=False, positive_damping_controls_all_redundant_directions=True,
            node_mass_sha256=array_sha(mass), all_node_jet_weights_sha256=array_sha(all_diagonal),
            xy_radial_scale_sha256=array_sha(self.xy_diagonal),
            z_radial_scale_sha256=array_sha(self.z_diagonal),
            profile_radial_scale_sha256=array_sha(self.profile_diagonal),
            xy_angular_scale_sha256=array_sha(self.xy_sigma),
            z_angular_scale_sha256=array_sha(self.z_sigma),
            core_scale_sha256=array_sha(self.core_scale),
            free_variables=q.free_size, free_radial_profile_variables=q.profile_size)
        self.record['norm_identity_sha256'] = canonical(self.record)

    def lift(self, value):
        require_actions()
        q = self.problem
        value = np.asarray(value, dtype=float)
        if value.shape != (q.free_size,) or not np.isfinite(value).all():
            raise ValueError('Use the entire finite R696 norm-coordinate vector')
        result = np.empty_like(value)
        result[:q.core_size] = value[:q.core_size]*self.core_scale
        first, last = q.core_size, q.core_size+q.xy_size
        result[first:last] = (value[first:last].reshape(len(q.xy_free),q.xy_channels)
            *self.xy_diagonal[:,None]/self.xy_sigma[None]).ravel()
        result[last:last+q.z_size] = (value[last:last+q.z_size].reshape(len(q.z_free),q.z_channels)
            *self.z_diagonal[:,None]/self.z_sigma[None]).ravel()
        result[last+q.z_size:-1] = value[last+q.z_size:-1]*self.profile_diagonal
        result[-1] = value[-1]
        return result

    def transpose(self, value):
        # The complete declared coordinate map is diagonal and real.
        return self.lift(value)
