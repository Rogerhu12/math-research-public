#!/usr/bin/env python3
"""Finite radial phase solve in the exact R33 unit-tangent chart.

The finite beta/gamma phase polynomials define an infinite angular tangent.
Its norm and its angular mean are exact by the formula, not by Fourier
truncation. Radial metric equations are minimized with Gauss quadrature and
an FFT approximation to the zero-mean primitive. Diagnostics distinguish
the derivatives of that finite primitive from the exact tangent formula.
Nothing here is a closed-surface or validated-numerics existence proof.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import BSpline, make_interp_spline
from scipy.sparse import coo_matrix

from fourfold_newton_refined import SplineNewton, CombinedMean, parity_matrix
from fourfold_overcollocation import normal_gauss_newton
from fourfold_banded_normal import banded_gauss_newton
from fourfold_unit_tangent import fourier_primitive
import poschl_teller_fourfold_series as ps


def primitive_quarter(samples):
    """FFT approximation to P_theta in the rotating cylindrical frame.

    Samples cover one quarter turn. Components have the R33 symmetries.
    The Nyquist coefficient is discarded. For n=4k, the horizontal inverse
    is ((in,1),(-1,in))/(1-n^2); the vertical inverse is 1/(in).
    """
    count = samples.shape[-2]
    value = np.fft.rfft(samples, axis=-2)
    n = 4*np.arange(value.shape[-2])
    out = np.zeros_like(value)
    out[..., 0] = (1j*n*value[..., 0]+value[..., 1])/(1-n*n)
    out[..., 1] = (-value[..., 0]+1j*n*value[..., 1])/(1-n*n)
    out[..., 1:, 2] = value[..., 1:, 2]/(1j*n[1:])
    out[..., -1, :] = 0.
    return np.fft.irfft(out, n=count, axis=-2)


def angular_derivative_quarter(samples):
    """Actual Cartesian angular derivative, returned in the rotating frame."""
    count = samples.shape[-2]
    value = np.fft.rfft(samples, axis=-2)
    n = 4*np.arange(value.shape[-2])
    out = 1j*n[..., None]*value
    out[..., 0] -= value[..., 1]
    out[..., 1] += value[..., 0]
    out[..., -1, :] = 0.
    return np.fft.irfft(out, n=count, axis=-2)


def tangent_fields(beta, gamma, beta_x, gamma_x, sine, cosine,
                   beta_xx=None, gamma_xx=None):
    """Vectorized exact R33 tangent and partials in cylindrical coordinates."""
    b, p = beta@sine, gamma@sine
    bx, px = beta_x@sine, gamma_x@sine
    cb, sb, cp, sp = np.cos(b), np.sin(b), np.cos(p), np.sin(p)
    zero = np.zeros_like(b)
    t = np.stack((-cp*sb, cp*cb, sp), axis=-1)
    # Preserve the quadratic angular correction at the polar end; computing
    # cos(p)*cos(b)-1 by subtraction loses it long before radial weighting.
    hp, hb = np.sin(p/2)**2, np.sin(b/2)**2
    delta_t = np.stack((-cp*sb, -2*hp-2*hb+4*hp*hb, sp), axis=-1)
    tb = np.stack((-cp*cb, -cp*sb, zero), axis=-1)
    tp = np.stack((sp*sb, -sp*cb, cp), axis=-1)
    tbb = np.stack((cp*sb, -cp*cb, zero), axis=-1)
    tbp = np.stack((sp*cb, sp*sb, zero), axis=-1)
    tx = tb*bx[..., None]+tp*px[..., None]
    result = dict(T=t, DeltaT=delta_t, Tx=tx, Tb=tb, Tg=tp,
                  Tbx=tbb*bx[..., None]+tbp*px[..., None],
                  Tgx=tbp*bx[..., None]-t*px[..., None])
    if beta_xx is not None:
        bxx, pxx = beta_xx@sine, gamma_xx@sine
        result['Txx'] = (tb*bxx[..., None]+tp*pxx[..., None]
                         +tbb*(bx*bx)[..., None]
                         +2*tbp*(bx*px)[..., None]-t*(px*px)[..., None])
        frequency = 4*np.arange(1, beta.shape[-1]+1)
        bt, pt = (beta*frequency)@cosine, (gamma*frequency)@cosine
        result['Ttheta'] = np.stack((
            sp*pt*sb-cp*cb*(1+bt),
            -sp*pt*cb-cp*sb*(1+bt), cp*pt), axis=-1)
    return result


class PhaseNewton(SplineNewton):
    components = 2

    def __init__(self, modes=16, points=151, length=3., mu_scale=4.,
                 means=3, gauge='none', profile_points=1201, mesh='graded'):
        super().__init__(modes, points, length, mu_scale, means, gauge,
                         profile_points, mesh)
        self.radius_shift = None

    def pack(self, coeff, alpha):
        return np.r_[np.asarray(coeff).ravel(), np.broadcast_to(alpha, (self.mean_count,))]

    def unpack(self, vector):
        return (vector[:-self.mean_count].reshape(self.modes, 2, self.points),
                vector[-self.mean_count:])

    def mean(self, x, alpha, derivative=0):
        out = CombinedMean(self, alpha)(x, nu=derivative)
        if self.radius_shift is not None:
            out[..., 0] += self.radius_shift(x, nu=derivative)
        return out

    def phases(self, vector, x, derivatives=2):
        if derivatives not in (0, 1, 2):
            raise ValueError('this solver evaluator provides only radial jets of orders 0, 1, 2')
        x = np.atleast_1d(x)
        coeff, _ = self.unpack(vector)
        a, ap, app = (self.base_spline(x, nu=j)[:, 0] for j in range(3))
        output = np.empty((derivatives+1, len(x), self.modes, 2))
        for c, power in enumerate((3, 2)):
            basis = [parity_matrix(self.knots, 5, x, j, bool(c))
                     for j in range(derivatives+1)]
            raw = [np.asarray(mat@coeff[:, c].T) for mat in basis]
            w = a**power
            w1 = power*a**(power-1)*ap
            output[0, :, :, c] = w[:, None]*raw[0]
            if derivatives:
                output[1, :, :, c] = w[:, None]*raw[1]+w1[:, None]*raw[0]
            if derivatives > 1:
                w2 = power*(power-1)*a**(power-2)*ap*ap+power*a**(power-1)*app
                output[2, :, :, c] = (w[:, None]*raw[2]+2*w1[:, None]*raw[1]
                                       +w2[:, None]*raw[0])
        return output

    def from_position(self, path, angular_nodes=256):
        """Convert a position checkpoint and store its circumference-radius shift.

        The shift is a genuine even quintic spline. Its value is computed
        from the mean speed of the source curve, not identified with the
        old cylindrical mean radius. Conversion is a floating initial guess.
        """
        with np.load(path, allow_pickle=False) as f:
            metadata = json.loads(str(f['metadata']))
            vector = f['vector']
        old = SplineNewton(**metadata['parameters'])
        candidate = old.candidate(vector, metadata['epsilon'])
        alpha = old.unpack(vector)[1]
        if len(alpha) != self.mean_count:
            raise ValueError('source and target must have the same mean family')
        theta = 2*np.pi*np.arange(angular_nodes)/(4*angular_nodes)
        ft = ps.evaluate_candidate(candidate, self.x, theta, False)[2]
        beta = np.arctan2(-ft[..., 0], ft[..., 1])
        gamma = np.arctan2(ft[..., 2], np.linalg.norm(ft[..., :2], axis=2))
        coeff = np.empty((self.modes, 2, self.points))
        a = self.base_spline(self.x)[:, 0]
        for c, (field, power) in enumerate(((beta, 3), (gamma, 2))):
            fourier = -2*np.fft.rfft(field, axis=1).imag/angular_nodes
            for k in range(self.modes):
                coeff[k, c] = self.value_lu[c].solve(fourier[:, k+1]/a**power)
        grid = np.linspace(0., self.length, self.profile_points)
        shift = np.empty_like(grid)
        nonmean = dict(candidate, splines={m: sp for m, sp in candidate['splines'].items() if m})
        for start in range(0, len(grid), 64):
            xx = grid[start:start+64]
            delta = ps.evaluate_candidate(nonmean, xx, theta, False)[2]
            old_radius = candidate['splines'][0](xx)[:, 0, None]
            difference = 2*old_radius*delta[..., 1]+np.sum(delta*delta, axis=2)
            speed = np.sqrt(old_radius*old_radius+difference)
            shift[start:start+64] = np.mean(difference/(speed+old_radius), axis=1)
        self.radius_shift = make_interp_spline(
            np.r_[-grid[:0:-1], grid], np.r_[shift[:0:-1], shift], k=5)
        self.source_position = str(path)
        self.source_position_metadata = metadata
        return self.pack(coeff, alpha)

    def prepare(self, beta_waist, gauss=3, angles=128):
        if angles < 4*self.modes+8 or angles % 4:
            raise ValueError('quarter-period angle count must be a multiple of 4 >=4M+8')
        self.angles, self.collocation_rule = angles, gauss
        self.beta_waist = float(beta_waist)
        self.waist = self.beta_waist  # generic optimizer checkpoint argument
        self.greville = self.x.copy()
        breaks = np.unique(np.r_[0., self.knots[self.knots > 0]])
        q, w = leggauss(gauss)
        lo, hi = breaks[:-1, None], breaks[1:, None]
        self.x = ((lo+hi)/2+(hi-lo)*q/2).ravel()
        self.quadrature_weights = ((hi-lo)*w/2).ravel()
        self.even = [parity_matrix(self.knots, 5, self.x, j, False) for j in range(3)]
        self.odd = [parity_matrix(self.knots, 5, self.x, j, True) for j in range(3)]
        self.phi = 2*np.pi*np.arange(angles)/angles
        self.sin = np.sin(np.arange(1, self.modes+1)[:, None]*self.phi)
        self.cos = np.cos(np.arange(1, self.modes+1)[:, None]*self.phi)
        self.a = self.base_spline(self.x)[:, 0]
        self.ap = self.base_spline(self.x, nu=1)[:, 0]
        self.mean_values = np.stack([sp(self.x) for sp in self.mean_splines])
        self.mean_derivatives = np.stack([sp(self.x, nu=1) for sp in self.mean_splines])
        sx = np.linalg.norm(self.base_spline(self.x, nu=1), axis=1)
        self.objective_modes = angles//2-1
        self.row_scale = np.tile(np.stack((sx*self.a, sx*sx), axis=1)*self.a[:, None]**3,
                                 (1, self.objective_modes))
        self.row_weight = np.sqrt(self.quadrature_weights)[:, None]
        self.at_end = [parity_matrix(self.knots, 5, [self.length], j, False) for j in range(2)]
        al = self.base_spline(np.array([self.length]))[0, 0]
        apl = self.base_spline(np.array([self.length]), nu=1)[0, 0]
        self.end_rate = self.mode*self.mu+3*apl/al
        self.waist_row = parity_matrix(self.knots, 5, [0.], 0, False).toarray().ravel()
        self.waist_row *= self.base_spline(np.array([0.]))[0, 0]**3
        self.pivot = int(np.argmax(abs(self.waist_row)))
        size = 2*self.modes*self.points+self.mean_count
        self.keep = np.delete(np.arange(size), self.pivot)
        free_column = np.full(size, -1, dtype=int)
        free_column[self.keep] = np.arange(size-1)
        rows, cols, values = self.keep.tolist(), list(range(size-1)), [1.]*(size-1)
        self.offset = np.zeros(size)
        self.offset[self.pivot] = self.beta_waist/self.waist_row[self.pivot]
        for j in np.flatnonzero(self.waist_row):
            if j == self.pivot:
                continue
            rows.append(self.pivot)
            cols.append(int(free_column[j]))
            values.append(float(-self.waist_row[j]/self.waist_row[self.pivot]))
        self.projector = coo_matrix((values, (rows, cols)), shape=(size, size-1)).tocsc()
        self.last_free = None
        self.last_values = None
        self.ncall = 0

    def expand(self, free):
        return self.offset+self.projector@free

    def extract(self, xx, xt):
        fx = 2*np.fft.rfft(xx, axis=1).real[:, 1:-1]/self.angles
        ft = -2*np.fft.rfft(xt, axis=1).imag[:, 1:-1]/self.angles
        return np.stack((ft, fx), axis=-1).reshape(len(self.x), -1)

    def values(self, free):
        if self.last_free is not None and np.array_equal(free, self.last_free):
            return self.last_values
        vector = self.expand(free)
        coeff, alpha = self.unpack(vector)
        phase = self.phases(vector, self.x, derivatives=1)
        fields = tangent_fields(phase[0, :, :, 0], phase[0, :, :, 1],
                                phase[1, :, :, 0], phase[1, :, :, 1], self.sin, self.cos)
        delta_sp, sx = primitive_quarter(fields['DeltaT']), primitive_quarter(fields['Tx'])
        sp = delta_sp.copy()
        sp[..., 0] += 1.
        mean, derivative = (self.mean(self.x, alpha, j) for j in (0, 1))
        if np.min(mean[:, 0]) <= 0 or np.min(derivative[:, 2]) <= 0:
            raise ValueError('mean phase chart lost positive circumference radius or vertical slope')
        delta_fx = derivative[:, 0, None, None]*delta_sp+mean[:, 0, None, None]*sx
        base_fx = derivative[:, None, :]
        fx = base_fx+delta_fx
        ft = mean[:, 0, None, None]*fields['T']
        delta_ft = mean[:, 0, None, None]*fields['DeltaT']
        dxx = 2*np.sum(base_fx*delta_fx, axis=2)+np.sum(delta_fx*delta_fx, axis=2)
        dxt = (np.sum(base_fx*delta_ft, axis=2)+mean[:, 0, None]*delta_fx[..., 1]
               +np.sum(delta_fx*delta_ft, axis=2))
        tensor = self.extract(dxx, dxt)
        base = tensor/self.row_scale
        boundary = np.array([float(((self.at_end[1]+rate*self.at_end[0])@coeff[k, 0])[0])
                             for k, rate in enumerate(self.end_rate)])
        residual = np.r_[(base*self.row_weight).ravel(), boundary]
        self.last_free = free.copy()
        self.last_values = dict(vector=vector, residual=residual, base=base, boundary=boundary,
                                fx=fx, ft=ft, fields=fields, primitive=sp, primitive_x=sx,
                                primitive_delta=delta_sp, delta_fx=delta_fx, delta_ft=delta_ft,
                                mean=mean, derivative=derivative)
        return self.last_values

    def fun(self, free):
        value = self.values(free)
        residual = value['residual']
        self.ncall += 1
        record = dict(call=self.ncall, cost=float(residual@residual/2),
                      maximum_weighted_tensor=float(abs(value['base']).max()),
                      maximum_robin=float(abs(value['boundary']).max()),
                      alpha=self.unpack(value['vector'])[1].tolist())
        self.history.append(record)
        if hasattr(self, 'snapshot_path') and record['cost'] < getattr(self, 'best_cost', float('inf')):
            self.best_cost = record['cost']
            self.save(value['vector'], self.snapshot_path, self.beta_waist)
        print(json.dumps(record), flush=True)
        return residual

    def linearization(self, free):
        value = self.values(free)
        q, kout, kin = len(self.x), 2*self.objective_modes, 2*self.modes
        aa, bb = np.zeros((q, kout, kin)), np.zeros((q, kout, kin))
        fx, ft = value['fx'], value['ft']
        a, ap = value['mean'][:, 0], value['derivative'][:, 0]
        fields = value['fields']
        for j in range(kin):
            k, c = divmod(j, 2)
            power = 3-c
            weight = self.a**power
            weight_x = power*self.ap/self.a*weight
            tangent = fields['Tg' if c else 'Tb']*self.sin[k][None, :, None]
            tangent_x = fields['Tgx' if c else 'Tbx']*self.sin[k][None, :, None]
            primitive = primitive_quarter(tangent)
            primitive_x = primitive_quarter(tangent_x)
            dx = ((ap*weight+a*weight_x)[:, None, None]*primitive
                  +(a*weight)[:, None, None]*primitive_x)
            dt = (a*weight)[:, None, None]*tangent
            dxd = (a*weight)[:, None, None]*primitive
            aa[:, :, j] = self.extract(2*np.sum(fx*dx, axis=2),
                                       np.sum(fx*dt+ft*dx, axis=2))
            bb[:, :, j] = self.extract(2*np.sum(fx*dxd, axis=2), np.sum(ft*dxd, axis=2))
        mean_columns = np.empty((q, kout, self.mean_count))
        for j in range(self.mean_count):
            da, dap = self.mean_values[j, :, 0], self.mean_derivatives[j, :, 0]
            delta_dx = dap[:, None, None]*value['primitive_delta']+da[:, None, None]*value['primitive_x']
            base_dx = self.mean_derivatives[j, :, None, :]
            dx = base_dx+delta_dx
            dt = da[:, None, None]*fields['T']
            dxx = 2*np.sum(value['derivative'][:, None, :]*delta_dx
                           +value['delta_fx']*base_dx+value['delta_fx']*delta_dx, axis=2)
            mean_columns[:, :, j] = self.extract(dxx,
                                                 np.sum(fx*dt+ft*dx, axis=2))
        scale = self.row_weight/self.row_scale
        aa *= scale[:, :, None]
        bb *= scale[:, :, None]
        mean_columns *= scale[:, :, None]
        return aa, bb, mean_columns

    def jvp(self, free, direction):
        aa, bb, mc = self.linearization(free)
        coeff, alpha = self.unpack(self.projector@direction)
        value, derivative = [], []
        for k in range(self.modes):
            for c, basis in enumerate((self.even, self.odd)):
                value.append(basis[0]@coeff[k, c])
                derivative.append(basis[1]@coeff[k, c])
        r = (np.einsum('qoj,jq->qo', aa, np.array(value))
             +np.einsum('qoj,jq->qo', bb, np.array(derivative))+mc@alpha)
        boundary = [float(((self.at_end[1]+rate*self.at_end[0])@coeff[k, 0])[0])
                    for k, rate in enumerate(self.end_rate)]
        return np.r_[r.ravel(), boundary]

    def normal_system(self, free):
        aa, bb, mc = self.linearization(free)
        residual = self.values(free)['residual']
        n, q, kin, kout = self.points, len(self.x), 2*self.modes, 2*self.objective_modes
        matrices = [self.even[0].tocsr(), self.odd[0].tocsr(),
                    self.even[1].tocsr(), self.odd[1].tocsr()]
        width = 5
        bands = np.zeros((n, 2*width+1, kin, kin))
        cross_mean = np.zeros((n, kin, self.mean_count))
        mean_gram = np.zeros((self.mean_count, self.mean_count))
        gradient, mean_gradient = np.zeros((n, kin)), np.zeros(self.mean_count)
        rmat = residual[:q*kout].reshape(q, kout)
        for row in range(q):
            support = np.unique(np.concatenate([mat.getrow(row).indices for mat in matrices]))
            weights = [mat.getrow(row)[:, support].toarray().ravel() for mat in matrices]
            blocks = []
            for j in range(len(support)):
                val = np.tile([weights[0][j], weights[1][j]], self.modes)
                der = np.tile([weights[2][j], weights[3][j]], self.modes)
                blocks.append(aa[row]*val[None, :]+bb[row]*der[None, :])
            local = np.concatenate(blocks, axis=1)
            gram, lg, cross = local.T@local, local.T@rmat[row], local.T@mc[row]
            mean_gram += mc[row].T@mc[row]
            mean_gradient += mc[row].T@rmat[row]
            for ii, node_i in enumerate(support):
                i = slice(ii*kin, (ii+1)*kin)
                gradient[node_i] += lg[i]
                cross_mean[node_i] += cross[i]
                for jj, node_j in enumerate(support):
                    offset = int(node_j-node_i)
                    if abs(offset) > width:
                        raise RuntimeError('unexpected phase-spline support width')
                    bands[node_i, offset+width] += gram[i, jj*kin:(jj+1)*kin]
        boundary = residual[q*kout:]
        for k, rate in enumerate(self.end_rate):
            end = (self.at_end[1]+rate*self.at_end[0]).tocoo()
            c = 2*k
            for node_i, vi in zip(end.col, end.data):
                gradient[node_i, c] += vi*boundary[k]
                for node_j, vj in zip(end.col, end.data):
                    bands[node_i, int(node_j-node_i)+width, c, c] += vi*vj
        rows, cols, values = [], [], []
        ir, ic = np.indices((kin, kin))
        for i in range(n):
            for d in range(-width, width+1):
                j = i+d
                if not 0 <= j < n:
                    continue
                block = bands[i, d+width]
                mask = block != 0.
                rows.append((i*kin+ir[mask]).astype(np.int32))
                cols.append((j*kin+ic[mask]).astype(np.int32))
                values.append(block[mask])
        cross = cross_mean.reshape(n*kin, self.mean_count)
        ir, ic = np.indices(cross.shape)
        rows.extend((ir.ravel().astype(np.int32), (n*kin+ic).ravel().astype(np.int32)))
        cols.extend(((n*kin+ic).ravel().astype(np.int32), ir.ravel().astype(np.int32)))
        values.extend((cross.ravel(), cross.ravel()))
        ir, ic = np.indices(mean_gram.shape)
        rows.append((n*kin+ir).ravel().astype(np.int32))
        cols.append((n*kin+ic).ravel().astype(np.int32))
        values.append(mean_gram.ravel())
        del aa, bb, mc, bands, cross_mean
        full = coo_matrix((np.concatenate(values), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(n*kin+self.mean_count, n*kin+self.mean_count)).tocsc()
        del rows, cols, values
        radial_to_mode = np.r_[(np.arange(kin)[None, :]*n+np.arange(n)[:, None]).ravel(),
                               np.arange(n*kin, n*kin+self.mean_count)]
        transform = self.projector[radial_to_mode, :]
        reduced = (transform.T@full@transform).tocsc()
        gradient = np.asarray(transform.T@np.r_[gradient.ravel(), mean_gradient]).ravel()
        return reduced, gradient

    def geometry(self, vector, x, angles=256):
        x = np.atleast_1d(x)
        phase = self.phases(vector, x, 2)
        phi = 2*np.pi*np.arange(angles)/angles
        sine = np.sin(np.arange(1, self.modes+1)[:, None]*phi)
        cosine = np.cos(np.arange(1, self.modes+1)[:, None]*phi)
        fields = tangent_fields(phase[0, :, :, 0], phase[0, :, :, 1],
                                phase[1, :, :, 0], phase[1, :, :, 1], sine, cosine,
                                phase[2, :, :, 0], phase[2, :, :, 1])
        sp, sx, sxx = (primitive_quarter(fields[key]) for key in ('T', 'Tx', 'Txx'))
        mean, derivative, second = (self.mean(x, self.unpack(vector)[1], j) for j in range(3))
        a, ap, app = mean[:, 0, None, None], derivative[:, 0, None, None], second[:, 0, None, None]
        f, fx, fxx = a*sp, ap*sp+a*sx, app*sp+2*ap*sx+a*sxx
        f[..., 2] += mean[:, 2, None]
        fx[..., 2] += derivative[:, 2, None]
        fxx[..., 2] += second[:, 2, None]
        ds = angular_derivative_quarter(sp)
        finite = (f, fx, a*ds, fxx, ap*ds+a*angular_derivative_quarter(sx),
                  a*angular_derivative_quarter(ds))
        exact_angular = (a*fields['T'], ap*fields['T']+a*fields['Tx'], a*fields['Ttheta'])
        return finite, exact_angular, phase, fields

    def diagnostic(self, vector, samples=1201, angles=256):
        x = np.unique(np.r_[np.linspace(0., self.length, samples), self.x])
        peak, radius, kmax, support, derivative_defect = 0., 0., 0., float('inf'), 0.
        at, waist, gap, fourth = None, None, None, None
        low_peak, high_peak, low_at, high_at = 0., 0., None, None
        for start in range(0, len(x), 48):
            xx = x[start:start+48]
            jets, exact, _, _ = self.geometry(vector, xx, angles)
            f, fx, ft, fxx, fxt, ftt = jets
            derivative_defect = max(derivative_defect,
                                    *(float(abs(a-b).max()) for a, b in zip((ft, fxt, ftt), exact)))
            gxx, gxt, gtt = np.sum(fx*fx, axis=2), np.sum(fx*ft, axis=2), np.sum(ft*ft, axis=2)
            ex, et = gxx.mean(axis=1)[:, None], gtt.mean(axis=1)[:, None]
            aa, bb, cc = (gxx-ex)/ex, gxt/np.sqrt(ex*et), (gtt-et)/et
            fourier = np.stack((2*np.fft.rfft(cc, axis=1).real,
                                -2*np.fft.rfft(bb, axis=1).imag,
                                2*np.fft.rfft(aa, axis=1).real))/angles
            for k in range(1, fourier.shape[-1]-1):
                block = fourier[:, :, k]
                ii = np.unravel_index(np.argmax(abs(block)), block.shape)
                value = float(abs(block[ii]))
                where = dict(mode=4*k, component=('tt', 'xt', 'xx')[ii[0]], x=float(xx[ii[1]]))
                if k <= self.modes and value > low_peak:
                    low_peak, low_at = value, where
                if k > self.modes and value > high_peak:
                    high_peak, high_at = value, where
            center, rad = (aa+cc)/2, np.sqrt(((aa-cc)/2)**2+bb*bb)
            norm = np.maximum(abs(center-rad), abs(center+rad))
            index = np.unravel_index(np.argmax(norm), norm.shape)
            if norm[index] > peak:
                peak, at = float(norm[index]), (float(xx[index[0]]), float(np.pi*index[1]/(2*angles)))
            radius = max(radius, float(np.linalg.norm(f, axis=2).max()))
            cross = np.cross(ft, fx)
            jac = np.linalg.norm(cross, axis=2)
            normal = cross/jac[:, :, None]
            l, m, n = (np.sum(normal*v, axis=2) for v in (fxx, fxt, ftt))
            det = l*n-m*m
            gauss = det/(jac*jac)
            trace = (l*gtt-2*m*gxt+n*gxx)/(jac*jac)
            root = np.sqrt(np.maximum(0., trace*trace-4*gauss))
            kmax = max(kmax, float(np.maximum(abs((trace-root)/2), abs((trace+root)/2)).max()))
            support = min(support, float(np.sum(f*normal, axis=2).min()))
            for i in np.nonzero(xx == 0.)[0]:
                gap = float(f[i, 0, 0]-f[i, angles//2, 0])
                fourth = float(2*np.fft.rfft(f[i, :, 0]).real[1]/angles)
                waist = dict(detII_min=float(det[i].min()), detII_max=float(det[i].max()),
                             N_min=float(n[i].min()), N_max=float(n[i].max()),
                             gauss_min=float(gauss[i].min()), gauss_max=float(gauss[i].max()))
        return dict(kind='floating_actual_finite_primitive_samples_not_bounds',
                    radial_samples=int(len(x)), quarter_period_angles=angles,
                    metric_operator_norm_sample=peak, at_x=at[0], at_theta=at[1],
                    exact_angular_formula_vs_finite_primitive_jet_max=derivative_defect,
                    twice_sampled_radius=2*radius, waist_radial_gap=gap,
                    gap_ratio_sample=gap/(2*radius), actual_U4_at_waist=fourth,
                    beta4_at_waist=float(self.phases(vector, [0.], 0)[0, 0, 0, 0]),
                    phase_retained_metric_coefficient_sample=low_peak, phase_retained_peak=low_at,
                    above_phase_cutoff_metric_coefficient_sample=high_peak, above_phase_cutoff_peak=high_at,
                    max_abs_principal_curvature_sample=kmax, minimum_support_sample=support,
                    waist_second_form_samples=waist)

    def primitive_audit(self, vector, radial_points=(0., .1, .25, .5, 1.)):
        """Independent full-circle helper budgets and quarter-FFT comparison.

        Strip and alias bounds are evaluated in ordinary double arithmetic;
        they do not include interval or floating-point rounding certification.
        """
        output = []
        for x in radial_points:
            jets, exact, phase, fields = self.geometry(vector, [x], angles=self.angles)
            data = dict(beta=phase[0, 0, :, 0], gamma=phase[0, 0, :, 1],
                        beta_x=phase[1, 0, :, 0], gamma_x=phase[1, 0, :, 1],
                        beta_xx=phase[2, 0, :, 0], gamma_xx=phase[2, 0, :, 1])
            best = None
            for sigma in (.025, .04, .06, .08, .1, .15, .2, .25):
                try:
                    helper = fourier_primitive(**data, nodes=4*self.angles,
                                               keep=2*self.angles-3, sigma=sigma)
                except (ValueError, OverflowError):
                    continue
                score = max(max(v['total']) for v in helper.budgets.values())
                if best is None or score < best[0]:
                    best = score, helper
            if best is None:
                output.append(dict(x=x, status='no finite strip bound among candidates'))
                continue
            helper = best[1]
            theta = 2*np.pi*np.arange(self.angles)/(4*self.angles)
            independent = helper.evaluate(theta)
            co, si = np.cos(theta), np.sin(theta)
            quarter = primitive_quarter(fields['T'])[0]
            cartesian = quarter.copy()
            cartesian[:, 0] = co*quarter[:, 0]-si*quarter[:, 1]
            cartesian[:, 1] = si*quarter[:, 0]+co*quarter[:, 1]
            fine_helper = fourier_primitive(**data, nodes=8*self.angles,
                                             keep=4*self.angles-3, sigma=helper.sigma)
            fine = fine_helper.evaluate(theta)
            mean, mean_x, mean_xx = (self.mean(np.array([x]), self.unpack(vector)[1], j)[0]
                                     for j in range(3))
            a, ap, app = abs(mean[0]), abs(mean_x[0]), abs(mean_xx[0])
            e, ex, exx = (np.asarray(helper.budgets[key]['total'])
                          for key in ('T', 'T_x', 'T_xx'))
            geometry_budget = dict(F=float(a*e[0]), Fx=float(ap*e[0]+a*ex[0]),
                                   Ftheta=float(a*e[1]),
                                   Fxx=float(app*e[0]+2*ap*ex[0]+a*exx[0]),
                                   Fxtheta=float(ap*e[1]+a*ex[1]), Fthetatheta=float(a*e[2]))
            nx = float(np.linalg.norm(jets[1], axis=2).max())
            nt = float(np.linalg.norm(jets[2], axis=2).max())
            dx, dt = geometry_budget['Fx'], geometry_budget['Ftheta']
            metric_budget = dict(xx=2*nx*dx+dx*dx, xt=nx*dt+nt*dx+dx*dt,
                                 tt=2*nt*dt+dt*dt)
            output.append(dict(x=x, quarter_period_nodes=self.angles,
                               equivalent_full_circle_nodes=4*self.angles,
                               equivalent_full_circle_cutoff=2*self.angles-3,
                               selected_sigma=helper.sigma,
                               full_circle_vs_quarter_primitive_sample=float(abs(independent['T']-cartesian).max()),
                               doubled_FFT_primitive_jet_sample_max=max(
                                   float(abs(fine[key]-independent[key]).max()) for key in independent),
                               analytic_tail_alias_bounds=helper.budgets,
                               geometry_jet_tail_alias_bounds=geometry_budget,
                               absolute_metric_entry_tail_alias_bounds=metric_budget,
                               roundoff_included=False))
        return output

    def save(self, vector, path, amplitude):
        metadata = dict(kind='floating_R33_phase_candidate_not_closed_surface_proof',
                        parameters=dict(modes=self.modes, points=self.points, length=self.length,
                                        mu_scale=self.mu/2**.5, means=self.mean_count, gauge='none',
                                        profile_points=self.profile_points, mesh=self.mesh),
                        beta_waist=float(amplitude), quarter_period_angles=self.angles,
                        radial_gauss_points_per_interval=self.collocation_rule,
                        amplitude_gauge='beta4(0), not U4(0) or kernel projection',
                        mean_radius='circumference radius; includes explicitly saved source conversion shift',
                        source_position=getattr(self, 'source_position', None),
                        limitations=['Floating arithmetic', 'Finite radial splines and Robin endpoint',
                                     'FFT primitive approximates exact infinite angular field',
                                     'No fixed caps or certified reach'])
        data = dict(vector=vector, metadata=np.array(json.dumps(metadata)))
        if self.radius_shift is not None:
            data.update(radius_shift_knots=self.radius_shift.t,
                        radius_shift_coefficients=self.radius_shift.c,
                        radius_shift_degree=np.array(self.radius_shift.k))
        temporary = Path(str(path)+'.tmp.npz')
        np.savez_compressed(temporary, **data)
        temporary.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--start-position', type=Path)
    ap.add_argument('--start-phase', type=Path)
    ap.add_argument('--modes', type=int, default=16)
    ap.add_argument('--points', type=int, default=151)
    ap.add_argument('--mesh', choices=('uniform', 'graded'), default='graded')
    ap.add_argument('--gauss', type=int, default=3)
    ap.add_argument('--angles', type=int, default=128)
    ap.add_argument('--beta-waist', type=float)
    ap.add_argument('--iterations', type=int, default=8)
    ap.add_argument('--regularization', type=float, default=1e-6)
    ap.add_argument('--linear-method', choices=('banded', 'normal'), default='banded')
    ap.add_argument('--cache', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    s = PhaseNewton(modes=args.modes, points=args.points, mesh=args.mesh)
    if bool(args.start_position) == bool(args.start_phase):
        raise ValueError('specify exactly one of --start-position and --start-phase')
    if args.start_position:
        initial = s.from_position(args.start_position)
        beta_reference = None
    else:
        with np.load(args.start_phase, allow_pickle=False) as f:
            metadata = json.loads(str(f['metadata']))
            old = PhaseNewton(**metadata['parameters'])
            if 'radius_shift_knots' in f:
                s.radius_shift = BSpline(f['radius_shift_knots'], f['radius_shift_coefficients'],
                                         int(f['radius_shift_degree']))
            s.source_position = metadata.get('source_position')
            beta_reference = metadata['beta_waist']
            old_vector = f['vector']
        old_coeff, alpha = old.unpack(old_vector)
        coeff = np.zeros((s.modes, 2, s.points))
        phase = old.phases(old_vector, s.x, 0)[0]
        a = s.base_spline(s.x)[:, 0]
        for k in range(min(s.modes, old.modes)):
            for c, power in enumerate((3, 2)):
                coeff[k, c] = s.value_lu[c].solve(phase[:, k, c]/a**power)
        initial = s.pack(coeff, alpha)
    beta_waist = args.beta_waist
    if beta_waist is None:
        beta_waist = (float(s.phases(initial, [0.], 0)[0, 0, 0, 0])
                      if beta_reference is None else float(beta_reference))
    s.prepare(beta_waist, args.gauss, args.angles)
    args.cache.parent.mkdir(parents=True, exist_ok=True)
    s.snapshot_path = args.cache
    solve = banded_gauss_newton if args.linear_method == 'banded' else normal_gauss_newton
    result = solve(s, initial[s.keep], args.iterations, args.regularization)
    vector = s.expand(result.x)
    s.save(vector, args.cache, beta_waist)
    diagnostic = s.diagnostic(vector)
    report = dict(kind='floating_R33_phase_overcollocation_not_proof',
                  arguments={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
                  cost=float(result.cost), message=result.message, optimality=result.optimality,
                  diagnostic=diagnostic, primitive_audit=s.primitive_audit(vector), history=s.history)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(diagnostic=diagnostic, cost=result.cost)), flush=True)


if __name__ == '__main__':
    main()
