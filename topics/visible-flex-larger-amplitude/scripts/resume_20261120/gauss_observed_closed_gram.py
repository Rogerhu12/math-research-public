#!/usr/bin/env python3
"""The same complete ClosedGram field with additional radial observations.

Original node/midpoint rows are the literal prefix.  Every original cell is
also observed at Gauss points, split at the analytic lift breakpoint when
needed.  Default order six covers the degree-five full physical Fs on each
piece.  All affine variables, core chains, analytic lift and angular orbit
weights are inherited from the published batched operator.

This is a finite numerical operator, not a continuous geometry certificate.
Scalar values at the new points must come from the same exact scalar oracle.
No interpolation of the old scalar carriers is performed here.
"""
from dataclasses import dataclass
from pathlib import Path
import importlib.util
import sys
import numpy as np


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path).resolve())
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def hermite_weights(h, u):
    """All three jets; endpoint order Y0,U0,A0,Y1,U1,A1.

    Six explicit Hermite basis polynomials are differentiated algebraically.
    No inversion or fitting occurs at an observation point.
    """
    h, u = float(h), float(u)
    coefficients = np.array([
        [1., 0., 0., -10., 15., -6.],
        [0., 1., 0., -6., 8., -3.],
        [0., 0., .5, -1.5, 1.5, -.5],
        [0., 0., 0., 10., -15., 6.],
        [0., 0., 0., -4., 7., -3.],
        [0., 0., 0., .5, -1., .5],
    ])
    endpoint_scale = np.array([1., h, h*h, 1., h, h*h])
    result = np.empty((3, 6))
    for order in range(3):
        value = np.zeros(6)
        for degree in range(5, order-1, -1):
            factor = 1
            for k in range(order):
                factor *= degree-k
            value = value*u+factor*coefficients[:, degree]
        result[order] = value*endpoint_scale/h**order
    return result


@dataclass
class ObservationPlan:
    cells: np.ndarray
    local_u: np.ndarray
    times: np.ndarray
    weights: np.ndarray
    quadrature_weights: np.ndarray
    legacy_simpson_weights: np.ndarray
    piece_cells: np.ndarray
    piece_u: np.ndarray
    gauss_indices: np.ndarray
    gauss_unit_nodes: np.ndarray
    gauss_unit_weights: np.ndarray
    legacy_count: int
    order: int
    lift_break_node: object

    def arrays(self):
        return dict(observation_cells=self.cells, observation_u=self.local_u,
            observation_times=self.times, observation_weights=self.weights,
            observation_quadrature_weights=self.quadrature_weights,
            observation_legacy_simpson_weights=self.legacy_simpson_weights,
            observation_piece_cells=self.piece_cells,
            observation_piece_u=self.piece_u, observation_gauss_indices=self.gauss_indices,
            observation_gauss_unit_nodes=self.gauss_unit_nodes,
            observation_gauss_unit_weights=self.gauss_unit_weights,
            observation_legacy_count=np.array(self.legacy_count),
            observation_order=np.array(self.order),
            observation_lift_break_node=np.array(-1 if self.lift_break_node is None else self.lift_break_node))

    @classmethod
    def from_arrays(cls, data):
        number = int(data['observation_lift_break_node'])
        return cls(cells=np.array(data['observation_cells']),
            local_u=np.array(data['observation_u']), times=np.array(data['observation_times']),
            weights=np.array(data['observation_weights']),
            quadrature_weights=np.array(data['observation_quadrature_weights']),
            legacy_simpson_weights=np.array(data['observation_legacy_simpson_weights']),
            piece_cells=np.array(data['observation_piece_cells']),
            piece_u=np.array(data['observation_piece_u']),
            gauss_indices=np.array(data['observation_gauss_indices']),
            gauss_unit_nodes=np.array(data['observation_gauss_unit_nodes']),
            gauss_unit_weights=np.array(data['observation_gauss_unit_weights']),
            legacy_count=int(data['observation_legacy_count']),
            order=int(data['observation_order']),
            lift_break_node=None if number < 0 else number)


def make_plan(mesh, width, *, order=6, lift_break_node=None):
    """Keep all old rows, then append order Gauss points per analytic piece.

    An exact symbolic node at S-width may be identified by lift_break_node.
    This avoids inventing a microscopic split from carrier subtraction.
    The actual original _lift_scalar implementation is never changed.
    """
    mesh = np.asarray(mesh, dtype=float)
    h = np.diff(mesh)
    J, legacy = len(mesh), 2*len(mesh)-1
    order = int(order)
    if (J < 2 or mesh[0] != 0 or not np.all(np.isfinite(mesh))
            or not np.all(h > 0) or order < 5 or not 0 < width < mesh[-1]):
        raise ValueError('Need the original positive mesh, lift width and Gauss order >=5')
    if lift_break_node is not None and not 0 < int(lift_break_node) < J-1:
        raise ValueError('The symbolic lift breakpoint must be an interior node')
    xi, wi = np.polynomial.legendre.leggauss(order)
    unit_nodes, unit_weights = (xi+1)/2, wi/2
    cells, local_u, times, weights = [], [], [], []
    simpson = np.zeros(legacy)
    for j in range(J):
        cell = min(j, J-2)
        u = 0. if j < J-1 else 1.
        w = np.zeros((3, 6))
        w[np.arange(3), np.arange(3)+(0 if u == 0 else 3)] = 1.
        cells.append(cell); local_u.append(u); times.append(mesh[j]); weights.append(w)
        if j < J-1:
            hm = h[j]
            w = np.array([[.5, 5*hm/32, hm*hm/64, .5, -5*hm/32, hm*hm/64],
                [-15/(8*hm), -7/16, -hm/32, 15/(8*hm), -7/16, hm/32],
                [0., -3/(2*hm), -.25, 0., 3/(2*hm), -.25]])
            cells.append(j); local_u.append(.5); times.append(mesh[j]+hm/2); weights.append(w)
            simpson[2*j] += hm/6
            simpson[2*j+1] += 2*hm/3
            simpson[2*j+2] += hm/6
    pieces, piece_u, indices, qw = [], [], [], [0.]*legacy
    breakpoint = float(mesh[-1]-width)
    if lift_break_node is not None:
        breakpoint = float(mesh[int(lift_break_node)])
    for cell, hm in enumerate(h):
        split = [0., 1.]
        if lift_break_node is None and mesh[cell] < breakpoint < mesh[cell+1]:
            split = [0., (breakpoint-mesh[cell])/hm, 1.]
        for lo, hi in zip(split[:-1], split[1:]):
            current = []
            uu = lo+(hi-lo)*unit_nodes
            if not np.all(np.diff(uu) > 0):
                raise ValueError('The declared piece has unresolved distinct double Gauss points')
            for u, omega in zip(uu, unit_weights):
                current.append(len(cells))
                cells.append(cell); local_u.append(float(u))
                times.append(mesh[cell]+hm*u)
                weights.append(hermite_weights(hm, u))
                qw.append(hm*(hi-lo)*omega)
            pieces.append(cell); piece_u.append((lo, hi)); indices.append(current)
    total = len(cells)
    old_weights = np.zeros(total); old_weights[:legacy] = simpson
    return ObservationPlan(np.array(cells, dtype=int), np.array(local_u), np.array(times),
        np.array(weights), np.array(qw), old_weights,
        np.array(pieces, dtype=int), np.array(piece_u), np.array(indices, dtype=int),
        np.array(unit_nodes), np.array(unit_weights), legacy, order, lift_break_node)


class ObservationMixin:
    def __init__(self, *args, observation_plan, a_observations, **kwargs):
        super().__init__(*args, **kwargs)
        plan = observation_plan
        legacy_a = self.a.copy()
        legacy_times = self.times.copy()
        values = np.asarray(a_observations, dtype=float)
        P = len(plan.cells)
        if (plan.legacy_count != self.P or plan.weights.shape != (P, 3, 6)
                or values.shape != (P,) or not np.all(np.isfinite(values))
                or not np.all(values > 0)
                or not np.array_equal(values[:self.P], legacy_a)
                or not np.array_equal(plan.times[:self.P], legacy_times)
                or not np.all((plan.cells >= 0) & (plan.cells < self.J-1))):
            raise ValueError('The observation extension must preserve all literal old scalar/time rows')
        self.legacy_P = self.P
        self.plan = plan
        self.P = P
        self.a = values.copy()
        self.times = plan.times.copy()
        self.observation_cells = plan.cells.copy()
        self.observation_weights = plan.weights.copy()
        self.observation_u = plan.local_u.copy()
        # Match the original source's literal midpoint weights, even if
        # a future caller constructs a plan by a different arithmetic order.
        self.observation_weights[1:self.legacy_P:2] = self._mid_weights_array
        self.lift_scalar = np.array([self._lift_scalar(float(s)) for s in self.times])
        self.stage_quadrature_weights = plan.quadrature_weights.copy()
        self.stage_legacy_simpson_weights = plan.legacy_simpson_weights.copy()
        self.clear_base()

    def mixed_stage_weights(self, legacy_fraction=.5):
        """Positive sum of composite Simpson and new Gauss weights.

        Returned values are squared row weights.  sqrt(weights) belongs on
        residual/Jv/transpose consistently.  No stage weighting is implicit
        in residual(), whose only built-in weight remains angular orbits.
        """
        t = float(legacy_fraction)
        if not 0 < t < 1:
            raise ValueError('Both retained row sets need positive mixture weight')
        return t*self.stage_legacy_simpson_weights+(1-t)*self.stage_quadrature_weights

    def _stage_all(self, jets, start, stop):
        cells = self.observation_cells[start:stop]
        endpoints = np.stack((jets[cells], jets[cells+1]), axis=1).reshape((-1, 6, self.n))
        return np.einsum('bqc,bcn->bqn', self.observation_weights[start:stop], endpoints)

    def _stage_triplet(self, jets, start, stop):
        values = self._stage_all(jets, start, stop)
        return values[:, 0], values[:, 1], values[:, 2]

    def _stage_pair(self, jets, start, stop):
        cells = self.observation_cells[start:stop]
        endpoints = np.stack((jets[cells], jets[cells+1]), axis=1).reshape((-1, 6, self.n))
        values = np.einsum('bqc,bcn->bqn', self.observation_weights[start:stop, :2], endpoints)
        return values[:, 0], values[:, 1]

    def _stage_pair_adjoint(self, grad, start, stop, gy, gu):
        cells = self.observation_cells[start:stop]
        weights = self.observation_weights[start:stop]
        contribution = (weights[:, 0, :, None]*gy[:, None, :]
                        +weights[:, 1, :, None]*gu[:, None, :])
        # Repeated cell indices are essential: every cell has >=6 new rows.
        np.add.at(grad, cells, contribution[:, :3])
        np.add.at(grad, cells+1, contribution[:, 3:])

    def stage_jets(self, jets, stage):
        cell = int(self.observation_cells[stage])
        return self.observation_weights[stage]@jets[cell:cell+2].reshape((6, self.n))

    def _stage_adjoint(self, grad, stage, gy, gu):
        cell = int(self.observation_cells[stage])
        w = self.observation_weights[stage]
        grad[cell:cell+2] += (w[0, :, None]*gy+w[1, :, None]*gu).reshape((2, 3, self.n))

    def _angular_second_batch(self, y):
        M, nu = self.M, self.freq
        c = np.zeros((len(y), 2, M+1), dtype=np.result_type(y.dtype, float))
        c[:, 0, 0] = -y[:, 0]
        c[:, 0, 1:] = -(1+nu*nu)*y[:, 1:M+1]-2*nu*y[:, M+1:2*M+1]
        c[:, 1, 1:] = -nu*nu*y[:, 2*M+2:]
        s = -(1+nu*nu)*y[:, M+1:2*M+1]-2*nu*y[:, 1:M+1]
        cv = self._trig_values(c, 'cos')
        sv = self._trig_values(s, 'sin')
        result = np.empty((len(y), self.N, 3), dtype=c.dtype)
        result[:, :, 0], result[:, :, 1], result[:, :, 2] = cv[:, 0], sv, cv[:, 1]
        return result

    def physical_jet_batch(self, prepared, start, stop):
        """All derivatives needed for true point principal curvatures."""
        values = self._stage_all(prepared.jets, start, stop)
        y, u, acc = values[:, 0], values[:, 1], values[:, 2]
        V, d = self._first_batch(prepared, start, stop)
        ss, sp = self._linear_fields(u, acc)
        pp = self._angular_second_batch(y)
        lift = self.lift_scalar[start:stop]
        ss += lift[:, 5, None, None]*prepared.er[None]
        ss[:, :, 2] += lift[:, 2, None]*prepared.height
        sp += lift[:, 4, None, None]*(prepared.rho[:, None]*prepared.et)[None]
        pp += lift[:, 3, None, None]*(prepared.rho_phi[:, None]*prepared.et
                                      -prepared.rho[:, None]**2*prepared.er)[None]
        return dict(Fs=V, Fphi=d, Fss=ss, Fsphi=sp, Fphiphi=pp)

    def observation_metadata(self):
        return dict(legacy_stages=self.legacy_P, total_stages=self.P,
            added_gauss_stages=self.P-self.legacy_P, order=self.plan.order,
            analytic_pieces=len(self.plan.piece_cells),
            full_angles=self.full_N, evaluated_angles=self.N,
            free_variables=self.free_size,
            quadrature_weight_sum=float(self.stage_quadrature_weights.sum()),
            legacy_simpson_weight_sum=float(self.stage_legacy_simpson_weights.sum()),
            radial_stage_weights_implicit=False,
            original_scalar_rows_preserved=True, original_affine_space_preserved=True,
            geometry_certified=False)


def create(dense_source, *args, batch_source, observation_plan, a_observations, **kwargs):
    dense = dense_source if hasattr(dense_source, 'ClosedGram') else load('_observed_gram_dense', dense_source)
    batch = batch_source if hasattr(batch_source, 'BatchedMixin') else load('_observed_gram_batch', batch_source)
    class ObservedClosedGram(ObservationMixin, batch.BatchedMixin, dense.ClosedGram):
        pass
    return ObservedClosedGram(*args, observation_plan=observation_plan,
                              a_observations=a_observations, **kwargs)


if __name__ == '__main__':
    raise SystemExit('Import create() with the original dense/batch sources and same-g scalar observation carriers.')
