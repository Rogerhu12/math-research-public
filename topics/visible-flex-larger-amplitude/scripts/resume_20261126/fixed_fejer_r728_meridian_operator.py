#!/usr/bin/env python3
"""Complete closed SO(3)-meridian field and its actual discrete J/J*.

The fixed scalar metric comes from one byte-bound independent complete R690
reference. T0 is the explicitly bound paired-halfwave seed, frozen from that
reference's original core and H. The moving core, H and every complete outer
rotation coefficient remain free; no current omega is overwritten by a seed.
The exact mathematical field is G+h*(Gamma-G(0)), G=Pcap+integral_S^s T,
T=exp([omega]x)T0.  Therefore Fs=T+h'*(Gamma-G(0)), NOT merely T.

All queries below use ordinary CPU binary64 quadrature and root arithmetic.
Their errors are reported as unpaid; no old metric/geometry certificate is
inherited.  Importing this source performs no scientific calculation.
"""
import hashlib
import json
import math
import os
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from scipy.linalg import cholesky_banded, solve_banded
import torch


SCHEMA = 'complete-fixed-fejer-r728-so3-meridian-with-core-lift-v1'
REFERENCE_JET_SHA = 'c6fc04db9223981e1829620613c71de4c0bec93813ec0eeaf5f8ef7770217e86'
ORIGINAL_REFERENCE_SHA = 'e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb'
TORCH_VERSION = '2.5.1'


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


def rotated_jets(w, ws, wp, wpp, parent, curvature):
    """All physical world jets, differentiated through the complete rotation."""
    z = (w*w).sum(-1)
    A, B, Az, Bz, Azz, Bzz = rotation_coefficients(z)
    W, Wp = hat(w), hat(wp)
    W2 = W@W
    I = torch.eye(3, dtype=w.dtype, device=w.device)
    expand = lambda value: value[..., None, None]
    R = I+expand(A)*W+expand(B)*W2
    zp = 2*(w*wp).sum(-1)
    Rp = (expand(Az*zp)*W+expand(A)*Wp+expand(Bz*zp)*W2
        +expand(B)*(Wp@W+W@Wp))
    apply = lambda matrix, vector: (matrix@vector[..., None])[..., 0]
    result = {'T': apply(R, parent['T0']),
        'Tp': apply(Rp, parent['T0'])+apply(R, parent['T0_phi'])}
    if curvature:
        Ws, Wpp = hat(ws), hat(wpp)
        zs = 2*(w*ws).sum(-1)
        zpp = 2*((wp*wp).sum(-1)+(w*wpp).sum(-1))
        Rs = (expand(Az*zs)*W+expand(A)*Ws+expand(Bz*zs)*W2
            +expand(B)*(Ws@W+W@Ws))
        Rpp = (expand(Azz*zp*zp+Az*zpp)*W+expand(2*Az*zp)*Wp
            +expand(A)*Wpp+expand(Bzz*zp*zp+Bz*zpp)*W2
            +expand(2*Bz*zp)*(Wp@W+W@Wp)
            +expand(B)*(Wpp@W+2*(Wp@Wp)+W@Wpp))
        result['Ts'] = apply(Rs, parent['T0'])+apply(R, parent['T0_s'])
        result['Tpp'] = (apply(Rpp, parent['T0'])
            +2*apply(Rp, parent['T0_phi'])+apply(R, parent['T0_phiphi']))
    return result


class ClosedMeridianOperator:
    """All original core variables, H, and all shared-quintic rotation jets.

    The fixed domain coordinate phi is the selected initial core's chart;
    its material angle theta0(phi) never changes with the current core.
    This freezes a chart, not the moving core.  Continuous omega gives a
    local rotation chart away from antiparallel meridians when the stated
    classical angular derivatives exist.  Finite Fourier/shared-quintic
    omega is only the complete chosen trial space: its approximation and
    refinement properties still need proof.  It is not a bijection of the
    old q variables or an assertion about all global C2 immersions.
    """
    def __init__(self, parent_problem, parent_prepared, parent_jet_module, *,
                 cache_directory, integration_order=8, angle_block=8,
                 root_iterations=18, root_tolerance=2.e-12,
                 expected_parent_bundle_sha256=None,
                 seed_parameters=None, seed_mean_kernel_module=None):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Use the declared CPU PyTorch '+TORCH_VERSION)
        if sha(parent_jet_module.__file__) != REFERENCE_JET_SHA:
            raise ValueError('Bind the complete fixed paired-halfwave world-meridian reference kernel')
        if (integration_order < 4 or integration_order != int(integration_order)
                or angle_block < 1 or root_iterations < 4 or root_tolerance <= 0):
            raise ValueError('Use explicit complete integration/root/block parameters')
        self.parent = parent_problem
        self.parent_jet = parent_jet_module.SupportedUnitMeridianJet(parent_problem,
            parent_prepared, expected_bundle_sha256=expected_parent_bundle_sha256,
            seed_parameters=seed_parameters, mean_kernel_module=seed_mean_kernel_module,
            cache_directory=cache_directory)
        if self.parent_jet.model['schema'] != 'complete-fixed-fejer-R728-reversed-spherical-boundary-paired-halfwave-meridian-seed-reference-v1':
            raise ValueError('This entry uses a complete explicitly bound fixed paired-halfwave seed')
        self.context = parent_problem.axisymmetric_reference_context
        if (self.context.model.get('source_sha256') != ORIGINAL_REFERENCE_SHA
                or self.parent_jet.model['complete_axisymmetric_reference_model'] != self.context.model
                or self.parent_jet.model['initial_reference_model_identity_sha256'] != self.context.identity):
            raise ValueError('The seed must retain its actual complete original axisymmetric reference')
        self.M, self.K, self.J = int(parent_problem.M), int(parent_problem.K), int(parent_problem.J)
        if self.K != 3:
            raise ValueError('Retain exactly the originally fixed first three core coefficients')
        self.n = 3*self.M+2
        self.mesh = np.array(parent_problem.mesh, copy=True)
        if self.mesh[0] != 0 or np.any(np.diff(self.mesh) <= 0):
            raise ValueError('Use the complete original increasing mesh from core zero to cap S')
        self.S, self.R = float(self.mesh[-1]), float(parent_problem.R)
        self.P, self.N = int(parent_problem.P), int(parent_problem.N)
        self.full_N = int(parent_problem.full_N)
        self.legacy_P = int(parent_problem.legacy_P)
        self.phi = np.array(parent_problem.phi, copy=True)
        self.times = np.array(parent_problem.times, copy=True)
        self.observation_cells = np.array(parent_problem.observation_cells, copy=True)
        self.observation_u = np.array(parent_problem.observation_u, copy=True)
        self.multiplicity = np.array(parent_problem.multiplicity, copy=True)
        self.sqrt_multiplicity = np.sqrt(self.multiplicity)
        self.a = np.array(parent_problem.a, copy=True)
        self.stage_block = int(parent_problem.stage_block)
        if (self.N != self.full_N//4+1 or self.full_N%4 or self.a.shape != (self.P,)
                or np.any(self.a <= 0) or self.multiplicity.sum() != self.full_N):
            raise ValueError('Retain every actual original positive target/angle orbit')
        self.freq = 2*np.arange(1, self.M+1, dtype=float)
        self.qfreq = 1-self.freq**2
        self.parent_core = np.array(parent_prepared.core, copy=True)
        self.fixed_core = tensor(self.parent_core[:self.K])
        self.angle_block = int(angle_block)
        self.root_iterations, self.root_tolerance = int(root_iterations), float(root_tolerance)
        self.integration_order = Q = int(integration_order)
        self.radial_free = np.array([i for i in range(3*self.J)
            if i not in (0, 3*(self.J-1), 3*(self.J-1)+1)], dtype=np.int64)
        self.rotation_size = len(self.radial_free)*self.n
        self.core_size = self.M-self.K
        self.free_size = self.core_size+self.rotation_size+1
        self._radial_free_torch = torch.tensor(self.radial_free, dtype=torch.long)
        self._hermite = self.context.observed.hermite_weights
        gx, gw = np.polynomial.legendre.leggauss(Q)
        self.gauss_u, self.gauss_w = (gx+1)/2, gw/2
        if np.any(self.gauss_w <= 0):
            raise ArithmeticError('The complete meridian Gauss weights must remain positive')
        self.integration_cells = np.repeat(np.arange(self.J-1), Q)
        self.integration_u = np.tile(self.gauss_u, self.J-1)
        self._partial_polynomials = []
        for j in range(Q):
            polynomial = np.polynomial.Polynomial([1.])
            for k in range(Q):
                if j != k:
                    polynomial *= np.polynomial.Polynomial([-self.gauss_u[k], 1.])/(self.gauss_u[j]-self.gauss_u[k])
            self._partial_polynomials.append(polynomial.integ())
        self.integration_query = self.make_query(self.integration_cells, self.integration_u,
            integration_query=True)
        self.grid_query = self.make_query(self.observation_cells, self.observation_u)
        self.cache_directory = Path(cache_directory)
        self.cache_directory.mkdir(parents=True, exist_ok=False)
        self._cache = {}
        self._query_cache = {}
        self._residual_cache = None
        self._domain_cache = None
        self.counts = dict(residual_calls=0, J_calls=0, Jtranspose_calls=0,
            point_covectors=0, reference_jet_evaluations=0, reference_jet_points=0,
            evaluated_field_points=0, inverse_chart_solves=0)
        self.maximum_inverse_root_residual = 0.
        self.minimum_inverse_root_rho = float('inf')
        self.maximum_requested_reference_norm_deviation = 0.
        self.model = dict(schema=SCHEMA, source_sha256=sha(__file__),
            reference_meridian_kernel_sha256=REFERENCE_JET_SHA,
            fixed_scalar_metric_identity_sha256=self.context.scalar_identity,
            fixed_scalar_profile_definition=self.context.scalar_definition,
            initial_reference_bundle_sha256=self.parent_jet.binding['reference_bundle']['sha256'],
            initial_reference_model_identity_sha256=self.context.identity,
            complete_axisymmetric_reference_model=self.context.model,
            original_axisymmetric_reference_source_sha256=ORIGINAL_REFERENCE_SHA,
            fixed_supported_unit_seed_model=self.parent_jet.model,
            fixed_supported_unit_seed_identity_sha256=self.parent_jet.model_identity,
            fixed_supported_unit_seed_source_sha256=REFERENCE_JET_SHA,
            fixed_supported_unit_seed_mean_kernel_sha256=self.parent_jet.model['mean_kernel_source_sha256'],
            fixed_supported_unit_seed_working_definition=self.parent_jet.working_definition,
            fixed_chart_core_sha256=array_sha(self.parent_core),
            frozen_material_chart='theta0(phi)=Theta_cbar(phi); predeclared RN-even64 Fejer B=1/4,n=7, not an optimized warm chart',
            fixed_metric='ds^2+a_deep(s)^2*dtheta0^2',
            M=self.M, J=self.J, mesh_sha256=array_sha(self.mesh),
            radius_hex=self.R.hex(), fixed_core_first3=[float(v).hex() for v in self.parent_core[:3]],
            physical_S='same exact original S and affine symbolic nodes as the bound reference; mesh is its numerical carrier',
            omega_basis=dict(x='sin((2m+1)phi), m=0..M', y='cos((2m+1)phi), m=0..M',
                z='sin(2m phi), m=1..M', radial='complete shared C2 quintic node jets',
                fixed_zero_radial_slots=[0, 3*(self.J-1), 3*(self.J-1)+1]),
            closure_lift='h(s)=1-10(s/S)^3+15(s/S)^4-6(s/S)^5',
            field='Pcap+integral_S^s exp(omega cross)T0+h*(Gamma_c-Pcap+integral_0^S exp(omega cross)T0)',
            T0='complete fixed R728 reversed spherical-boundary seed from original reference core/H; full complement, R725 epsilon=1/8 three-piece C3 cutoff and equal six-piece central halfwaves with source-fixed signs [-1,+1]',
            fixed_reference_not_recomputed_from_current_omega=True,
            all_original_outer_free_variables_and_norm_layout_unchanged=True,
            core='Gamma_c(theta0), implicit Theta_c(phi_c)=theta0',
            cap='same fixed R661 p4 cap recipe at fixed deep R, translated by free H',
            all_current_free_core_coefficients_retained=True, current_height_free=True,
            radial_Gram_error_identically_zero=False,
            rotation_gauge='right rotations about T0; chart-pullback gauge retained, literal parallel variation only at omega=0',
            numerical_integration_rule_part_of_mathematical_target=False)
        self.identity = canonical(self.model)

    def initial(self):
        return np.r_[self.parent_core[self.K:], np.zeros(self.rotation_size), self.parent_jet.height]

    def unpack(self, x):
        x = np.asarray(x, dtype=float)
        if x.shape != (self.free_size,) or not np.isfinite(x).all():
            raise ValueError('Use every finite original core and full rotation variable')
        core = np.r_[self.parent_core[:self.K], x[:self.core_size]]
        jets = np.zeros((3*self.J, self.n))
        jets[self.radial_free] = x[self.core_size:-1].reshape(len(self.radial_free), self.n)
        return core, jets.reshape(self.J, 3, self.n), float(x[-1])

    def prepare(self, x):
        core, jets, height = self.unpack(x)
        return SimpleNamespace(x=np.asarray(x).copy(), core=core, jets=jets, height=height)

    def _unpack_torch(self, x):
        core = torch.cat((self.fixed_core, x[:self.core_size]))
        zero = torch.zeros((3*self.J, self.n), dtype=x.dtype, device=x.device)
        jets = zero.index_copy(0, self._radial_free_torch,
            x[self.core_size:-1].reshape(len(self.radial_free), self.n)).reshape(self.J, 3, self.n)
        return core, jets, x[-1]

    def make_query(self, cells, local, *, integration_query=False):
        cells, local = np.asarray(cells, dtype=np.int64), np.asarray(local, dtype=float)
        if (cells.ndim != 1 or cells.shape != local.shape or not len(cells)
                or np.any(cells < 0) or np.any(cells >= self.J-1)
                or not np.isfinite(local).all() or np.any(local < 0) or np.any(local > 1)):
            raise ValueError('Use actual exact-binary addresses on the unchanged exact reference mesh')
        widths = self.mesh[cells+1]-self.mesh[cells]
        weights = np.array([self._hermite(h, u) for h, u in zip(widths, local)])
        s = self.mesh[cells]+widths*local
        t = s/self.S
        h = 1-10*t**3+15*t**4-6*t**5
        hp = (-30*t*t+60*t**3-30*t**4)/self.S
        hpp = (-60*t+180*t*t-120*t**3)/self.S**2
        result = dict(cells=cells.copy(), local=local.copy(), s=s, widths=widths,
            cells_torch=torch.tensor(cells, dtype=torch.long), weights=tensor(weights),
            h=tensor(h)[:, None, None], hp=tensor(hp)[:, None, None],
            hpp=tensor(hpp)[:, None, None])
        if not integration_query:
            partial = np.column_stack([polynomial(local)-polynomial(0.)
                for polynomial in self._partial_polynomials])
            # Exact endpoints are explicit in the stated quadrature rule.
            partial[local == 0] = 0.
            partial[local == 1] = self.gauss_w
            result['partial'] = tensor(widths[:, None]*partial)
        return result

    def _parent(self, query, phi, label):
        angles = np.asarray(phi, dtype=float)
        key = (label, tuple(float(v).hex() for v in angles))
        if label in ('integration', 'grid') and key in self._cache:
            return self._cache[key]
        result = self.parent_jet.evaluate(query['cells'], query['local'], angles)
        self.counts['reference_jet_evaluations'] += 1
        self.counts['reference_jet_points'] += len(query['cells'])*len(angles)
        self.maximum_requested_reference_norm_deviation = max(self.maximum_requested_reference_norm_deviation,
            float(np.max(np.abs(result['norm']-1))))
        answer = {name: tensor(result[name]) for name in ('T0', 'T0_s', 'T0_phi', 'T0_phiphi')}
        if label in ('integration', 'grid'):
            # This is a replaceable evaluation cache, not permanent witness
            # memory.  The full source/object binding remains in metadata.
            digest = canonical(dict(label=label, phi=[float(v).hex() for v in angles]))
            path = self.cache_directory/(digest+'.npz')
            np.savez(path, **{name: result[name] for name in answer})
            # Keep compact path references; do not hold every AD-ready block.
            self._cache[key] = dict(cache_path=path)
        return answer

    def _parent_tensor(self, query, phi, label):
        record = self._parent(query, phi, label)
        if 'cache_path' in record:
            with np.load(record['cache_path'], allow_pickle=False) as data:
                return {name: tensor(data[name]) for name in data.files}
        return record

    def _angular_nodes(self, jets, phi, order):
        p = tensor(phi)
        odd = tensor(2*np.arange(self.M+1)+1)
        even = tensor(self.freq)
        a, b = p[:, None]*odd[None], p[:, None]*even[None]
        if order == 0:
            bx, by, bz = torch.sin(a), torch.cos(a), torch.sin(b)
        elif order == 1:
            bx, by, bz = torch.cos(a)*odd, -torch.sin(a)*odd, torch.cos(b)*even
        elif order == 2:
            bx, by, bz = -torch.sin(a)*odd**2, -torch.cos(a)*odd**2, -torch.sin(b)*even**2
        else:
            raise ValueError('Only the complete required angular orders are requested')
        first = self.M+1
        return torch.stack((jets[..., :first]@bx.T,
            jets[..., first:2*first]@by.T, jets[..., 2*first:]@bz.T), dim=-1)

    @staticmethod
    def _radial(nodes, query, order):
        cells = query['cells_torch']
        ends = torch.stack((nodes[cells], nodes[cells+1]), 1).reshape(
            len(cells), 6, nodes.shape[-2], 3)
        return torch.einsum('pc,pcaj->paj', query['weights'][:, order], ends)

    def _meridians(self, nodes, nodes_p, nodes_pp, query, phi, label, curvature):
        w = self._radial(nodes, query, 0)
        wp = self._radial(nodes_p, query, 0)
        ws = self._radial(nodes, query, 1) if curvature else None
        wpp = self._radial(nodes_pp, query, 0) if curvature else None
        parent = self._parent_tensor(query, phi, label)
        return rotated_jets(w, ws, wp, wpp, parent, curvature)

    def _core_and_cap(self, core, height, phi):
        phi_array = np.asarray(phi, dtype=float)
        nu = tensor(self.freq)
        qfreq = 1-nu*nu
        p = tensor(phi_array)
        parent_core = tensor(self.parent_core)
        phase = p[:, None]*nu[None]
        theta0 = p+(torch.sin(phase)*(qfreq/nu)*parent_core).sum(-1)
        rho0 = 1+(torch.cos(phase)*qfreq*parent_core).sum(-1)
        rhop0 = -(torch.sin(phase)*nu*qfreq*parent_core).sum(-1)
        pc = p
        for _ in range(self.root_iterations):
            phase_c = pc[:, None]*nu[None]
            value = pc+(torch.sin(phase_c)*(qfreq/nu)*core).sum(-1)-theta0
            rho = 1+(torch.cos(phase_c)*qfreq*core).sum(-1)
            pc = pc-value/rho
        phase_c = pc[:, None]*nu[None]
        equation = pc+(torch.sin(phase_c)*(qfreq/nu)*core).sum(-1)-theta0
        rho = 1+(torch.cos(phase_c)*qfreq*core).sum(-1)
        root_error = float(equation.detach().abs().max())
        rho_min = float(rho.detach().min())
        if (not math.isfinite(root_error) or root_error > self.root_tolerance
                or not math.isfinite(rho_min) or rho_min <= 0
                or not bool(torch.isfinite(pc.detach()).all())):
            raise ValueError('Current full-core inverse chart did not converge in its positive domain')
        self.counts['inverse_chart_solves'] += len(phi_array)
        self.maximum_inverse_root_residual = max(self.maximum_inverse_root_residual, root_error)
        self.minimum_inverse_root_rho = min(self.minimum_inverse_root_rho, rho_min)
        zero = torch.zeros_like(pc)
        er = torch.stack((torch.cos(pc), torch.sin(pc), zero), -1)
        et = torch.stack((-torch.sin(pc), torch.cos(pc), zero), -1)
        support = 1+(torch.cos(phase_c)*core).sum(-1)
        support_p = -(torch.sin(phase_c)*nu*core).sum(-1)
        Gamma = support[:, None]*er+support_p[:, None]*et
        Gammap = rho0[:, None]*et
        Gammapp = rhop0[:, None]*et-(rho0*rho0/rho)[:, None]*er
        er0 = torch.stack((torch.cos(theta0), torch.sin(theta0), zero), -1)
        et0 = torch.stack((-torch.sin(theta0), torch.cos(theta0), zero), -1)
        ez = tensor([0., 0., 1.])
        P = self.R*er0+height*ez
        Pp = self.R*rho0[:, None]*et0
        Ppp = self.R*(rhop0[:, None]*et0-rho0[:, None]**2*er0)
        return (Gamma, Gammap, Gammapp), (P, Pp, Ppp), rho0

    def _integrate(self, value, query):
        block = value.reshape(self.J-1, self.integration_order, value.shape[-2], 3)
        widths = tensor(np.diff(self.mesh))
        cell_total = (block*tensor(self.gauss_w)[None, :, None, None]).sum(1)*widths[:, None, None]
        prefix = torch.cat((torch.zeros_like(cell_total[:1]), torch.cumsum(cell_total, 0)), 0)
        partial = torch.einsum('pq,pqaj->paj', query['partial'], block[query['cells_torch']])
        return prefix[query['cells_torch']]+partial, prefix[-1]

    def fields_torch(self, x, query, phi, *, curvature=True, query_label='arbitrary'):
        core, jets, height = self._unpack_torch(x)
        nodes = self._angular_nodes(jets, phi, 0)
        nodes_p = self._angular_nodes(jets, phi, 1)
        nodes_pp = self._angular_nodes(jets, phi, 2) if curvature else None
        integrated = self._meridians(nodes, nodes_p, nodes_pp, self.integration_query,
            phi, 'integration', curvature)
        direct = self._meridians(nodes, nodes_p, nodes_pp, query, phi, query_label, curvature)
        core_jets, cap_jets, rho0 = self._core_and_cap(core, height, phi)
        h, hp, hpp = query['h'], query['hp'], query['hpp']
        result = {}
        deltas = []
        for key, component, index in (('F', 'T', 0), ('Fphi', 'Tp', 1)):
            integral, total = self._integrate(integrated[component], query)
            C, P = core_jets[index][None], cap_jets[index][None]
            delta = C-P+total[None]
            deltas.append(delta)
            result[key] = (1-h)*P+h*C+integral-(1-h)*total[None]
        result['Fs'] = direct['T']+hp*deltas[0]
        if curvature:
            integral, total = self._integrate(integrated['Tpp'], query)
            C, P = core_jets[2][None], cap_jets[2][None]
            result['Fphiphi'] = (1-h)*P+h*C+integral-(1-h)*total[None]
            result['Fss'] = direct['Ts']+hpp*deltas[0]
            result['Fsphi'] = direct['Tp']+hp*deltas[1]
        result['rho0'] = rho0
        result['closure_delta'] = deltas[0][0]
        self.counts['evaluated_field_points'] += len(query['cells'])*len(phi)
        return result

    def _raw_block(self, x, begin, end):
        fields = self.fields_torch(x, self.grid_query, self.phi[begin:end],
            curvature=False, query_label='grid')
        V, W = fields['Fs'], fields['Fphi']
        denominator = tensor(self.a)[:, None]*fields['rho0'][None]
        e = (V*V).sum(-1)-1
        f = (V*W).sum(-1)/denominator
        g = (W*W).sum(-1)/(denominator*denominator)-1
        return torch.stack((e, f, g), -1)*tensor(self.sqrt_multiplicity[begin:end])[None, :, None]

    def _blocks(self):
        for begin in range(0, self.N, self.angle_block):
            yield begin, min(begin+self.angle_block, self.N)

    def residual(self, x):
        require_actions()
        self.counts['residual_calls'] += 1
        x = np.asarray(x, dtype=float)
        if self._residual_cache is not None and np.array_equal(x, self._residual_cache[0]):
            return self._residual_cache[1].copy()
        self.domain(x)
        result = np.empty((self.P, self.N, 3))
        with torch.no_grad():
            xt = tensor(x)
            for begin, end in self._blocks():
                result[:, begin:end] = self._raw_block(xt, begin, end).numpy()
        if not np.isfinite(result).all():
            raise FloatingPointError('Nonfinite complete SO3 Gram')
        self._residual_cache = (x.copy(), result.copy())
        return result

    def unweight(self, native):
        return np.asarray(native).reshape(self.P, self.N, 3)/self.sqrt_multiplicity[None, :, None]

    def jvp(self, x, direction):
        require_actions()
        self.counts['J_calls'] += 1
        self.domain(x)
        result = np.empty((self.P, self.N, 3))
        xt, dt = tensor(x), tensor(direction)
        for begin, end in self._blocks():
            _, product = torch.autograd.functional.jvp(
                lambda value: self._raw_block(value, begin, end), xt, dt,
                create_graph=False, strict=False)
            result[:, begin:end] = product.detach().numpy()
        if not np.isfinite(result).all():
            raise FloatingPointError('Nonfinite full SO3 J product')
        return result

    def vjp(self, x, cotangent):
        require_actions()
        self.counts['Jtranspose_calls'] += 1
        self.domain(x)
        result = np.zeros(self.free_size)
        cotangent = np.asarray(cotangent).reshape(self.P, self.N, 3)
        for begin, end in self._blocks():
            xt = tensor(x).requires_grad_(True)
            value = self._raw_block(xt, begin, end)
            gradient, = torch.autograd.grad(value, xt, tensor(cotangent[:, begin:end]),
                create_graph=False, retain_graph=False)
            result += gradient.detach().numpy()
        if not np.isfinite(result).all():
            raise FloatingPointError('Nonfinite full SO3 transpose product')
        return result

    def grid_fields(self, x):
        self.domain(x)
        with torch.no_grad():
            xt = tensor(x)
            for begin, end in self._blocks():
                fields = self.fields_torch(xt, self.grid_query, self.phi[begin:end],
                    curvature=True, query_label='grid')
                yield begin, end, {name: value.numpy() for name, value in fields.items()}

    def _point_query(self, cell, u):
        key = (int(cell), float(u).hex())
        if key not in self._query_cache:
            self._query_cache[key] = self.make_query([int(cell)], [float(u)])
        return self._query_cache[key]

    def point_fields(self, x, cell, u, phi):
        with torch.no_grad():
            result = self.fields_torch(tensor(x), self._point_query(cell, u), [float(phi)],
                curvature=True)
            return {key: result[key][0, 0].numpy() for key in
                ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')}

    def point_vjp(self, x, cell, u, phi, cotangent):
        self.counts['point_covectors'] += 1
        xt = tensor(x).requires_grad_(True)
        result = self.fields_torch(xt, self._point_query(cell, u), [float(phi)], curvature=True)
        loss = sum((result[key][0, 0]*tensor(value)).sum() for key, value in cotangent.items())
        gradient, = torch.autograd.grad(loss, xt)
        answer = gradient.detach().numpy()
        if not np.isfinite(answer).all():
            raise FloatingPointError('Nonfinite full closed-meridian point covector')
        return answer

    def domain(self, x):
        x = np.asarray(x, dtype=float)
        if self._domain_cache is not None and np.array_equal(x, self._domain_cache[0]):
            return dict(self._domain_cache[1])
        core, _, height = self.unpack(x)
        # Full dense core sampling is an actual domain diagnostic.  It is
        # explicitly NOT relabeled as an interval certificate of rho>0.
        angles = np.arange(max(16384, 8*self.full_N))*2*np.pi/max(16384, 8*self.full_N)
        minimum = float('inf')
        for start in range(0, len(angles), 512):
            rho = 1+np.cos(angles[start:start+512, None]*self.freq[None])@(self.qfreq*core)
            minimum = min(minimum, float(rho.min()))
        if not math.isfinite(minimum) or minimum <= 0 or not math.isfinite(height):
            raise ValueError('Current complete core fails the declared positive-chart sample domain')
        result = dict(core_rho_sample_min=minimum, core_domain_angles=len(angles),
            continuous_core_rho_certified=False, H=height, all_free_core_coefficients=self.core_size,
            inverse_chart_iterations=self.root_iterations, inverse_chart_tolerance=self.root_tolerance)
        self._domain_cache = (x.copy(), result)
        return dict(result)

    def mixed_stage_weights(self, fraction):
        return self.parent.mixed_stage_weights(fraction)

    def save(self, path, x):
        core, jets, height = self.unpack(x)
        np.savez(path, schema=np.array(SCHEMA), omega_jets=jets, core=core, Hcap=np.array(height),
            mesh=self.mesh, fixed_chart_core=self.parent_core,
            so3_model_json=np.array(json.dumps(self.model, sort_keys=True, separators=(',', ':'))),
            so3_model_identity_sha256=np.array(self.identity),
            initial_reference_bundle_sha256=np.array(self.model['initial_reference_bundle_sha256']),
            fixed_scalar_metric_identity_sha256=np.array(self.context.scalar_identity),
            working_integration_order=np.array(self.integration_order),
            working_full_angles=np.array(self.full_N))

    def load_checkpoint(self, path):
        with np.load(path, allow_pickle=False) as data:
            if (str(data['schema'].item()) != SCHEMA
                    or str(data['so3_model_identity_sha256'].item()) != self.identity
                    or json.loads(str(data['so3_model_json'].item())) != self.model
                    or not np.array_equal(data['mesh'], self.mesh)
                    or not np.array_equal(data['fixed_chart_core'], self.parent_core)
                    or not np.array_equal(data['core'][:self.K], self.parent_core[:self.K])
                    or data['omega_jets'].shape != (self.J, 3, self.n)):
                raise ValueError('A continuation must retain the identical complete reference, scalar and representation')
            jets = np.array(data['omega_jets'], copy=True).reshape(3*self.J, self.n)
            if np.any(jets[[0, 3*(self.J-1), 3*(self.J-1)+1]] != 0):
                raise ValueError('The full structural core/cap rotation slots changed')
            result = np.r_[data['core'][self.K:], jets[self.radial_free].ravel(), float(data['Hcap'])]
        self.unpack(result)
        return result

    def clear_base(self):
        self._residual_cache = None

    def metadata(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__), model=self.model,
            model_identity_sha256=self.identity, axisymmetric_reference_binding=self.parent_jet.binding,
            fixed_supported_unit_seed=self.parent_jet.metadata(),
            fixed_supported_unit_seed_identity_sha256=self.parent_jet.model_identity,
            seed_mean_Jacobian_not_a_certificate_for_current_closure_control_Jacobian=True,
            free_variables=self.free_size, free_core_variables=self.core_size,
            free_rotation_variables=self.rotation_size, all_free_height_variables=1,
            working_integration_order=self.integration_order,
            quadrature_rule='whole-cell positive Gauss; exact Lagrange partial weights; ordinary binary64',
            integration_error_enclosed=False, unit_meridian_normalization_outward=False,
            symbolic_mesh_carrier_rounding_error_enclosed=False,
            field_derivatives_are_jets_of_exact_integral_definition=True,
            numerical_F_and_derivative_quadrature_defects_enclosed=False,
            maximum_actual_inverse_chart_residual=self.maximum_inverse_root_residual,
            minimum_actual_inverse_root_rho=self.minimum_inverse_root_rho,
            root_iteration_error_enclosed=False,
            maximum_requested_reference_norm_deviation=self.maximum_requested_reference_norm_deviation,
            angular_block=self.angle_block, actual_counts=dict(self.counts),
            torch_version=torch.__version__, torch_device='cpu', torch_dtype='float64',
            J_method='autograd.functional.jvp through every rotation, core-root, H and integral term',
            Jtranspose_method='exact transpose of the same declared discrete forward graph by autograd',
            finite_difference_J=False, old_metric_or_geometry_certificates_inherited=False,
            closed_exact_isometry_certified=False)


class RotationH2Coordinates:
    """Explicit new full-variable norm, including its chosen numerical units.

    jet-sum is a positive node-jet H2-type norm, not the exact Sobolev
    integral. integral is the full polynomial integral with diagonal
    equilibration, and does not silently substitute a different norm if
    its ordinary band Cholesky fails on a severely graded mesh.
    """
    def __init__(self, problem, *, radial_length=.05, angular_transition=24.,
                 norm_kind='jet-sum'):
        require_actions()
        if radial_length <= 0 or angular_transition <= 0:
            raise ValueError('Use positive explicit SO3 mother-norm parameters')
        self.problem = q = problem
        self.size = q.free_size
        self.radial_length = float(radial_length)
        self.angular_transition = float(angular_transition)
        if norm_kind not in ('jet-sum', 'integral'):
            raise ValueError('Choose an explicit full-variable norm')
        self.norm_kind = norm_kind
        odd = 2*np.arange(q.M+1)+1
        modes = np.r_[odd, odd, q.freq]
        self.sigma = np.sqrt(1+(modes/angular_transition)**2)
        self.core_scale = 1/np.maximum(1., np.abs(q.qfreq[q.K:]))
        if norm_kind == 'jet-sum':
            widths = np.diff(q.mesh)
            node_mass = np.r_[widths[0]/2, (widths[:-1]+widths[1:])/2, widths[-1]/2]
            diagonal = (node_mass[:, None]*np.array([1., radial_length**2,
                radial_length**4])[None]).ravel()[q.radial_free]
            if not np.isfinite(diagonal).all() or np.any(diagonal <= 0):
                raise ArithmeticError('Every free node jet needs an actual positive finite norm weight')
            self.diagonal_scale = 1/np.sqrt(diagonal)
            self.record = dict(schema='complete-SO3-positive-node-jet-H2-type-norm-v1',
                norm_kind=norm_kind, radial_length=radial_length,
                angular_transition=angular_transition,
                norm='sum_nodes_modes Voronoi_mass(node)*sigma_m^2*(omega^2+ell^2 omega_s^2+ell^4 omega_ss^2) + sum_free_core((1-nu^2)dc)^2+dH^2',
                exact_radial_Sobolev_integral=False,
                all_original_free_core_and_height_retained=True,
                all_complete_rotation_jets_retained=True,
                rotation_gauge_removed=False, positive_damping_controls_redundant_directions=True,
                original_q_physical_mother_norm_claimed_unchanged=False,
                node_mass_sha256=array_sha(node_mass), diagonal_sha256=array_sha(diagonal),
                angular_scale_sha256=array_sha(self.sigma), core_scale_sha256=array_sha(self.core_scale))
            self.record['norm_identity_sha256'] = canonical(self.record)
            return
        free = q.radial_free
        lookup = {int(index): j for j, index in enumerate(free)}
        count, bandwidth = len(free), 5
        band = np.zeros((bandwidth+1, count))
        roots, weights = np.polynomial.legendre.leggauss(6)
        for cell, width in enumerate(np.diff(q.mesh)):
            local = np.zeros((6, 6))
            for root, weight in zip((roots+1)/2, weights/2):
                W = q._hermite(width, root)
                local += width*weight*(np.outer(W[0], W[0])
                    +radial_length**2*np.outer(W[1], W[1])
                    +radial_length**4*np.outer(W[2], W[2]))
            slots = np.arange(3*cell, 3*cell+6)
            for i, old_i in enumerate(slots):
                if int(old_i) not in lookup:
                    continue
                ii = lookup[int(old_i)]
                for j, old_j in enumerate(slots[:i+1]):
                    if int(old_j) not in lookup:
                        continue
                    jj = lookup[int(old_j)]
                    band[ii-jj, jj] += local[i, j]
        self.equilibration = 1/np.sqrt(band[0])
        equilibrated = band.copy()
        for offset in range(bandwidth+1):
            equilibrated[offset, :count-offset] *= (
                self.equilibration[offset:]*self.equilibration[:count-offset])
        self.lower = cholesky_banded(equilibrated, lower=True, check_finite=True)
        self.upper = np.zeros_like(self.lower)
        for offset in range(bandwidth+1):
            self.upper[bandwidth-offset, offset:] = self.lower[offset, :count-offset]
        self.record = dict(schema='complete-SO3-radial-H2-positive-whitening-v1',
            norm_kind=norm_kind, radial_length=radial_length, angular_transition=angular_transition,
            norm='sum_modes sigma_m^2 integral(omega_m^2+ell^2 omega_ms^2+ell^4 omega_mss^2) ds + sum_free_core((1-nu^2)dc)^2+dH^2',
            radial_gauss_order=6, radial_bandwidth=bandwidth,
            full_radial_mass_and_derivative_integrals=True,
            all_original_free_core_and_height_retained=True,
            all_complete_rotation_jets_retained=True,
            rotation_gauge_removed=False,
            positive_damping_controls_redundant_directions=True,
            original_q_physical_mother_norm_claimed_unchanged=False,
            band_sha256=array_sha(band), lower_factor_sha256=array_sha(self.lower),
            diagonal_equilibration_sha256=array_sha(self.equilibration),
            angular_scale_sha256=array_sha(self.sigma), core_scale_sha256=array_sha(self.core_scale))
        self.record['norm_identity_sha256'] = canonical(self.record)

    def lift(self, value):
        q = self.problem
        value = np.asarray(value, dtype=float)
        result = np.empty_like(value)
        result[:q.core_size] = value[:q.core_size]*self.core_scale
        rhs = value[q.core_size:-1].reshape(len(q.radial_free), q.n)/self.sigma[None]
        if self.norm_kind == 'jet-sum':
            result[q.core_size:-1] = (self.diagonal_scale[:, None]*rhs).ravel()
        else:
            result[q.core_size:-1] = (self.equilibration[:, None]*solve_banded(
                (0, 5), self.upper, rhs, check_finite=False)).ravel()
        result[-1] = value[-1]
        return result

    def transpose(self, value):
        q = self.problem
        value = np.asarray(value, dtype=float)
        result = np.empty_like(value)
        result[:q.core_size] = value[:q.core_size]*self.core_scale
        rhs = value[q.core_size:-1].reshape(len(q.radial_free), q.n)
        if self.norm_kind == 'jet-sum':
            result[q.core_size:-1] = (self.diagonal_scale[:, None]*rhs/self.sigma[None]).ravel()
        else:
            result[q.core_size:-1] = (solve_banded((5, 0), self.lower,
                self.equilibration[:, None]*rhs, check_finite=False)/self.sigma[None]).ravel()
        result[-1] = value[-1]
        return result


