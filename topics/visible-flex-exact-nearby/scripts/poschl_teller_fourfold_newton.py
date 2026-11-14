#!/usr/bin/env python3
"""Floating finite-Fourier Newton continuation; no existence certificate.

Uses the R16 background inverse as a matrix-free left preconditioner.  The
critical fourth-mode amplitude is fixed, while one axisymmetric mean parameter
is solved together with all retained nonzero modes.  High output frequencies
are evaluated and reported even though they are not all Newton equations.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.integrate import cumulative_simpson
from scipy.sparse import bmat, coo_matrix, csc_matrix, diags
from scipy.sparse.linalg import LinearOperator, gmres, splu
import poschl_teller_fourfold_series as ps


class FourfoldNewton:
    def __init__(self, series, modes=8, mean_directions=1, tail_weight=0, mean_gauge="none", first_shift=0):
        self.series, self.modes = series, modes
        self.x = series["x"]
        self.points = len(self.x)
        self.h, self.v, self.z, self.q = (series[k] for k in ["h", "v", "z", "q"])
        self.a, self.w = 1/self.h, self.v/self.h
        self.tail_weight, self.mean_gauge = tail_weight, mean_gauge
        self.gamma = self.a**tail_weight
        self.mu = series["parameters"]["mu"]
        self.first_shift = first_shift
        _, (self.de, self.do, self.d2e) = ps.finite_difference(
            self.points, float(self.x[-1]), first_shift=first_shift)
        self.y = np.cosh(self.x)**(-4*self.mu)
        self.angles = max(64, 4*modes+8)
        self.phi = 2*np.pi*np.arange(self.angles)/self.angles
        self.cos = np.cos(np.arange(1, modes+1)[:, None]*self.phi)
        self.sin = np.sin(np.arange(1, modes+1)[:, None]*self.phi)
        self.mode = 4*np.arange(1, modes+1)
        self.seed_c, self.seed_d = series["fields"][1][4]
        alpha2 = next(r["mean_previous"] for r in series["recursion"]
                      if r["order"] == 3)
        self.mean_c, self.mean_d = tuple(
            c/alpha2 for c in series["fields"][2][0])
        self.mean_count = mean_directions
        self.means_c = [self.mean_c]
        self.means_d = [self.mean_d]
        for radius in [.25, .5, .8, 1.2][:mean_directions-1]:
            ph, php = ps.bump(self.x, radius)
            height = -2*cumulative_simpson(ph/self.h**2, x=self.x, initial=0.)
            self.means_c.append(np.stack([-self.a*ph,
                                          np.zeros_like(self.x), height]))
            self.means_d.append(np.stack([self.a*self.w*ph-self.a*php,
                                          np.zeros_like(self.x), -2*self.a*self.a*ph]))
        if len(self.means_c) != self.mean_count:
            raise ValueError("mean_directions must be from 1 to 5")
        self.means_c = np.stack(self.means_c)
        self.means_d = np.stack(self.means_d)
        self.seed_scaled = self.seed_c.copy()
        self.seed_scaled[:2] *= self.h
        self.seed_scaled /= self.gamma
        self.weights = np.ones(self.points)
        self.weights[1:-1:2] = 4
        self.weights[2:-1:2] = 2
        self.weights *= (self.x[1]-self.x[0])/3
        self.kernel_row = self.weights*self.y
        self.kernel_norm = self.kernel_row@self.y
        self.amplitude_row = self.kernel_row*self.gamma
        self.solvers = {}
        self.base_x = np.zeros((self.points, self.angles, 3))
        self.base_t = np.zeros_like(self.base_x)
        self.base_x[:, :, 0] = (-self.v/self.h**2)[:, None]
        self.base_x[:, :, 2] = (1/self.h**2)[:, None]
        self.base_t[:, :, 1] = self.a[:, None]
        seed = np.zeros((modes, 3, self.points))
        seed[0] = self.seed_scaled
        zx, zt = self.jets(self.pack(seed, 0.))
        vx, vt = self.jets(self.pack(np.zeros_like(seed), 1.))
        self.unit = -self.cross_coeff(zx, zt, vx, vt)
        self.unit_eta, self.unit_mult = self.solve_eta(4, self.eliminate(4, self.unit[0])[3])
        self.history = []

    def pack(self, coeff, alpha):
        alpha = np.atleast_1d(alpha)
        if alpha.size == 1 and self.mean_count > 1:
            alpha = np.r_[alpha, np.zeros(self.mean_count-1)]
        return np.r_[coeff.ravel(), alpha]

    def unpack(self, vector):
        return (vector[:-self.mean_count].reshape(self.modes, 3, self.points),
                vector[-self.mean_count:])

    def jets(self, vector):
        coeff, alpha = self.unpack(vector)
        dx = np.zeros((self.points, self.angles, 3))
        dt = np.zeros_like(dx)
        for k, m in enumerate(self.mode):
            u = self.gamma*coeff[k, 0]/self.h
            t = self.gamma*coeff[k, 1]/self.h
            w = self.gamma*coeff[k, 2]
            ux = self.gamma*(self.de@coeff[k, 0]-(self.tail_weight+1)*self.w*coeff[k, 0])/self.h
            tx = self.gamma*(self.de@coeff[k, 1]-(self.tail_weight+1)*self.w*coeff[k, 1])/self.h
            wx = self.gamma*(self.do@coeff[k, 2]-self.tail_weight*self.w*coeff[k, 2])
            co, si = self.cos[k], self.sin[k]
            dx[:, :, 0] += ux[:, None]*co
            dx[:, :, 1] += tx[:, None]*si
            dx[:, :, 2] += wx[:, None]*co
            dt[:, :, 0] -= (m*u+t)[:, None]*si
            dt[:, :, 1] += (u+m*t)[:, None]*co
            dt[:, :, 2] -= (m*w)[:, None]*si
        mean_c = np.tensordot(alpha, self.means_c, axes=(0, 0))
        mean_d = np.tensordot(alpha, self.means_d, axes=(0, 0))
        dx += mean_d.T[:, None, :]
        dt[:, :, 1] += mean_c[0, :, None]
        return dx, dt

    def extract(self, xx, xt, tt):
        fft = [np.fft.rfft(c, axis=1)/self.angles for c in [tt, xt, xx]]
        return np.stack([np.stack([2*fft[0][:, k].real,
                                  -2*fft[1][:, k].imag,
                                  2*fft[2][:, k].real])
                         for k in range(1, self.modes+1)])

    def cross_coeff(self, ax, at, bx, bt):
        return self.extract(2*np.sum(ax*bx, axis=2),
                            np.sum(ax*bt+bx*at, axis=2),
                            2*np.sum(at*bt, axis=2))

    def residual(self, vector):
        current, alpha = self.unpack(vector)
        vx, vt = self.jets(self.pack(current, np.zeros(self.mean_count)))
        mc = np.tensordot(alpha, self.means_c, axes=(0, 0))
        md = np.tensordot(alpha, self.means_d, axes=(0, 0))
        ax = self.base_x+md.T[:, None, :]
        at = self.base_t.copy()
        at[:, :, 1] += mc[0, :, None]
        fx, ft = ax+vx, at+vt
        # Compute the nonconstant tensor before adding the axisymmetric part.
        # This avoids losing a^3-sized angular terms near the polar endpoints.
        dxx = 2*np.sum(ax*vx, axis=2)+np.sum(vx*vx, axis=2)
        dxt = np.sum(ax*vt+vx*at+vx*vt, axis=2)
        dtt = 2*np.sum(at*vt, axis=2)+np.sum(vt*vt, axis=2)
        coeff = self.extract(dxx, dxt, dtt)
        ex = np.sum(ax[:, 0, :]**2, axis=1)+dxx.mean(axis=1)
        et = np.sum(at[:, 0, :]**2, axis=1)+dtt.mean(axis=1)
        ea = (dxx-dxx.mean(axis=1)[:, None])/ex[:, None]
        eb = dxt/np.sqrt(ex*et)[:, None]
        ec = (dtt-dtt.mean(axis=1)[:, None])/et[:, None]
        cen = (ea+ec)/2
        rad = np.sqrt(((ea-ec)/2)**2+eb*eb)
        full = np.maximum(abs(cen-rad), abs(cen+rad))
        scales = np.stack([et, np.sqrt(ex*et), ex])
        scaled_coeff = abs(coeff)/scales[None, :, :]
        low = float(np.max(scaled_coeff))
        outer_xx = float(np.max(scaled_coeff[:, 2, -1]))
        system_coeff = scaled_coeff/self.gamma[None, None, :]
        system_coeff[:, 2, -1] = 0.
        robin = max(abs(float((self.de.getrow(self.points-1)@current[k, 0])[0]
                              +(m*self.mu-self.tail_weight*self.w[-1])*current[k, 0, -1]))
                    for k, m in enumerate(self.mode))
        system_residual = max(float(system_coeff.max()), robin)
        core = self.x <= min(3., self.x[-1])
        stats = dict(low_coefficient_residual=low,
                     retained_robin_system_residual=system_residual,
                     system_tail_weight=self.tail_weight,
                     outer_xx_metric_coeff_residual=outer_xx,
                     robin_residual=robin,
                     full_metric_sample=float(full[core].max()),
                     full_metric_all_x_sample=float(full.max()),
                     alpha=(float(alpha[0]) if self.mean_count == 1 else alpha.tolist()))
        return coeff, stats, fx, ft

    def eliminate(self, m, pqr):
        p, qmix, r = pqr
        c = self.h*p/2
        cp = self.de@c
        j = self.v*c+self.h*cp-m*self.h*self.h*qmix
        f = m*m*self.h*self.h*r/2-self.do@j
        return c, cp, j, f

    def solve_eta(self, m, f):
        if m not in self.solvers:
            mat = (-self.d2e+diags(m*m*self.q)).tolil()
            mat[-1, :] = self.de.getrow(self.points-1)
            mat[-1, -1] += m*self.mu
            mat = mat.tocsc()
            if m == 4:
                col = self.y.copy()
                col[-1] = 0.
                mat = bmat([[mat, csc_matrix(col[:, None])],
                            [csc_matrix(self.kernel_row[None, :]),
                             csc_matrix((1, 1))]], format="csc")
            self.solvers[m] = splu(mat)
        right = f.copy()
        right[-1] = 0.
        if m == 4:
            answer = self.solvers[m].solve(np.r_[right, 0.])
            return answer[:-1], float(answer[-1])
        return self.solvers[m].solve(right), 0.

    def precondition(self, target, epsilon):
        result = np.zeros((self.modes, 3, self.points))
        pqr0 = target[0].copy()
        eta0, mult0 = self.solve_eta(4, self.eliminate(4, pqr0)[3])
        dalpha = -mult0/(epsilon*self.unit_mult)
        pqr0 += epsilon*dalpha*self.unit[0]
        eta0 += epsilon*dalpha*self.unit_eta
        for k, m in enumerate(self.mode):
            pqr = pqr0 if k == 0 else target[k]
            c, cp, j, f = self.eliminate(m, pqr)
            eta = eta0 if k == 0 else self.solve_eta(m, f)[0]
            ep = self.de@eta
            result[k, 0] = eta
            result[k, 1] = (self.h*c-eta)/m
            result[k, 2] = self.w*eta-ep/m**2+j/m**2
        result /= self.gamma[None, None, :]
        return self.pack(result, dalpha)


    def direct_step(self, vector, epsilon, residual, fx, ft):
        """Assemble the true differentiated finite system, with a Robin row.

        Radial-major block ordering retains the local radial bandwidth.
        One Schur complement imposes the critical-amplitude condition.
        """
        n, ksize = self.points, 3*self.modes
        aa = np.zeros((n, ksize, ksize))
        bb = np.zeros_like(aa)
        for index in range(ksize):
            k, component = divmod(index, 3)
            m, co, si = self.mode[k], self.cos[k], self.sin[k]
            dxv = np.zeros_like(fx)
            dxd = np.zeros_like(fx)
            dtv = np.zeros_like(ft)
            horizontal = self.gamma/self.h
            if component == 0:
                dxv[:, :, 0] = (-(self.tail_weight+1)*self.w*horizontal)[:, None]*co
                dxd[:, :, 0] = horizontal[:, None]*co
                dtv[:, :, 0] = (-m*horizontal)[:, None]*si
                dtv[:, :, 1] = horizontal[:, None]*co
            elif component == 1:
                dxv[:, :, 1] = (-(self.tail_weight+1)*self.w*horizontal)[:, None]*si
                dxd[:, :, 1] = horizontal[:, None]*si
                dtv[:, :, 0] = (-horizontal)[:, None]*si
                dtv[:, :, 1] = (m*horizontal)[:, None]*co
            else:
                dxv[:, :, 2] = (-self.tail_weight*self.w*self.gamma)[:, None]*co
                dxd[:, :, 2] = self.gamma[:, None]*co
                dtv[:, :, 2] = -m*self.gamma[:, None]*si
            aa[:, :, index] = self.cross_coeff(
                fx, ft, dxv, dtv).transpose(2, 0, 1).reshape(n, ksize)
            bb[:, :, index] = self.cross_coeff(
                fx, ft, dxd, np.zeros_like(ft)).transpose(2, 0, 1).reshape(n, ksize)
        sx = np.sqrt(1+self.v*self.v)/self.h**2
        scale = np.tile(np.stack([self.a*self.a, sx*self.a, sx*sx], axis=1),
                        (1, self.modes))
        scale *= self.gamma[:, None]
        aa /= scale[:, :, None]
        bb /= scale[:, :, None]
        boundary_rows = np.arange(2, ksize, 3)
        aa[-1, boundary_rows, :] = 0.
        bb[-1, boundary_rows, :] = 0.
        row, col, val = [], [], []
        nodes = np.arange(n, dtype=np.int32)
        eqs = np.arange(ksize, dtype=np.int32)
        ir = (nodes[:, None, None]*ksize+eqs[None, :, None])
        ic = (nodes[:, None, None]*ksize+eqs[None, None, :])
        row.append(np.broadcast_to(ir, aa.shape).ravel())
        col.append(np.broadcast_to(ic, aa.shape).ravel())
        val.append(aa.ravel())
        even, odd = self.de.tocoo(), self.do.tocoo()
        for index in range(ksize):
            deriv = odd if index % 3 == 2 else even
            rr = deriv.row.astype(np.int32)
            cc = deriv.col.astype(np.int32)
            values = bb[rr, :, index]*deriv.data[:, None]
            row.append((rr[:, None]*ksize+eqs).ravel())
            col.append(np.broadcast_to(cc[:, None]*ksize+index,
                                       values.shape).ravel())
            val.append(values.ravel())
        rvec = (residual.transpose(2, 0, 1).reshape(n, ksize)/scale).ravel()
        current_coeff, current_alpha = self.unpack(vector)
        nonmean_x, nonmean_t = self.jets(self.pack(current_coeff, np.zeros(self.mean_count)))
        mean_cols = []
        for mean_index in range(self.mean_count):
            direction = np.zeros(self.mean_count)
            direction[mean_index] = 1.
            vx, vt = self.jets(self.pack(
                np.zeros((self.modes, 3, self.points)), direction))
            mean_cols.append((self.cross_coeff(nonmean_x, nonmean_t, vx, vt).transpose(2, 0, 1).
                              reshape(n, ksize)/scale).ravel())
        mean_col = np.stack(mean_cols, axis=1)
        coeff, _ = self.unpack(vector)
        end = self.de.getrow(n-1)
        for k, m in enumerate(self.mode):
            equation = (n-1)*ksize+3*k+2
            row.append(np.full(end.nnz+1, equation, dtype=np.int32))
            col.append(np.r_[end.indices*ksize+3*k, (n-1)*ksize+3*k].astype(np.int32))
            rate = m*self.mu-self.tail_weight*self.w[-1]
            val.append(np.r_[end.data, rate])
            rvec[equation] = float((end@coeff[k, 0])[0]+rate*coeff[k, 0, -1])
            mean_col[equation, :] = 0.
        matrix = coo_matrix((np.concatenate(val),
                             (np.concatenate(row), np.concatenate(col))),
                            shape=(n*ksize, n*ksize)).tocsc()
        matrix.eliminate_zeros()
        lu = splu(matrix)
        answers = lu.solve(np.column_stack([-rvec, mean_col]))
        av = answers[0::ksize, 0]@self.amplitude_row
        au = self.amplitude_row@answers[0::ksize, 1:]
        amplitude_error = self.amplitude_row@coeff[0, 0]-epsilon*self.kernel_norm
        if self.mean_count == 1:
            dalpha = np.array([(av+amplitude_error)/au[0]])
        else:
            # Choose the free means to minimize a discrete C2-weighted step.
            # This is a numerical selection rule, not an infinite-dimensional
            # inverse theorem or a residual certificate.
            shaped = answers.reshape(n, ksize, 1+self.mean_count)
            physical = np.tile(np.stack([self.a, self.a, np.ones(n)], axis=1),
                               (1, self.modes))*self.gamma[:, None]
            angular = np.repeat(1+self.mode*self.mode, 3)
            weighted = shaped*(physical*angular[None, :]*
                               np.sqrt(self.weights)[:, None])[:, :, None]
            second = (shaped[2:]-2*shaped[1:-1]+shaped[:-2])/(self.x[1]-self.x[0])**2
            second *= (physical[1:-1]*np.sqrt(self.weights[1:-1])[:, None])[:, :, None]
            costs = np.concatenate([weighted.reshape(-1, 1+self.mean_count),
                                    second.reshape(-1, 1+self.mean_count)], axis=0)
            bb_cost, aa_cost = costs[:, 0], costs[:, 1:]
            constraints = [au]
            targets = [av+amplitude_error]
            if self.mean_gauge == "waist":
                waist = self.means_c[:, 0, 0]
                constraints.append(waist)
                targets.append(-waist@current_alpha)
            elif self.mean_gauge == "radius":
                values = np.zeros((n, self.angles, 3))
                mean_value = np.tensordot(current_alpha, self.means_c, axes=(0, 0))
                values[:, :, 0] = (self.a+mean_value[0])[:, None]
                values[:, :, 2] = (self.z+mean_value[2])[:, None]
                for kk in range(self.modes):
                    values[:, :, 0] += (self.gamma*coeff[kk, 0]/self.h)[:, None]*self.cos[kk]
                    values[:, :, 1] += (self.gamma*coeff[kk, 1]/self.h)[:, None]*self.sin[kk]
                    values[:, :, 2] += (self.gamma*coeff[kk, 2])[:, None]*self.cos[kk]
                squared = np.sum(values*values, axis=2)
                ip, jp = np.unravel_index(np.argmax(squared), squared.shape)
                unit = values[ip, jp]/np.sqrt(squared[ip, jp])
                linear_point = np.zeros(ksize)
                for kk in range(self.modes):
                    linear_point[3*kk:3*kk+3] = (
                        self.gamma[ip]*np.array([
                            unit[0]*self.cos[kk, jp]/self.h[ip],
                            unit[1]*self.sin[kk, jp]/self.h[ip],
                            unit[2]*self.cos[kk, jp]]))
                point_answers = linear_point@answers[ip*ksize:(ip+1)*ksize]
                point_means = self.means_c[:, :, ip]@unit
                constraints.append(point_answers[1:]-point_means)
                targets.append(point_answers[0])
            constraints = np.array(constraints)
            targets = np.array(targets)
            particular = np.linalg.lstsq(constraints, targets, rcond=1e-12)[0]
            _, sing, vh = np.linalg.svd(constraints, full_matrices=True)
            rank = np.sum(sing > sing[0]*1e-12)
            null = vh[rank:].T
            penalty = np.sum(self.means_c*self.means_c+self.means_d*self.means_d,
                             axis=(1, 2))*(self.x[1]-self.x[0])
            regularizer = np.diag(np.sqrt(1e-8*np.maximum(penalty, 1.)))
            if null.shape[1]:
                reduced = np.vstack([aa_cost@null, regularizer@null])
                reduced_rhs = np.r_[bb_cost-aa_cost@particular,
                                    -regularizer@particular]
                free = np.linalg.lstsq(reduced, reduced_rhs, rcond=1e-12)[0]
                dalpha = particular+null@free
            else:
                dalpha = particular
        dc = answers[:, 0]-answers[:, 1:]@dalpha
        delta = self.pack(dc.reshape(n, self.modes, 3).transpose(1, 2, 0), dalpha)
        discrepancy = matrix@dc+mean_col@dalpha+rvec
        return delta, dict(linear_method="sparse_direct",
                           jacobian_nnz=int(matrix.nnz),
                           linear_residual=float(np.max(abs(discrepancy))),
                           mean_schur=au.tolist())

    def seed(self, epsilon, order=7):
        coeff = np.zeros((self.modes, 3, self.points))
        alpha = 0.
        for degree, modes in self.series["fields"].items():
            if degree > order:
                continue
            for m, (c, _) in modes.items():
                if m == 0:
                    record = next(r for r in self.series["recursion"]
                                  if r["order"] == degree+1)
                    alpha += epsilon**degree*record["mean_previous"]
                elif m//4 <= self.modes:
                    scaled = c.copy()
                    scaled[:2] *= self.h
                    scaled /= self.gamma
                    coeff[m//4-1] += epsilon**degree*scaled
        amplitude = self.amplitude_row@coeff[0, 0]/self.kernel_norm
        coeff[0] += (epsilon-amplitude)*self.seed_scaled
        return self.pack(coeff, alpha)

    def solve(self, epsilon, initial=None, max_newton=12, tolerance=1e-9,
              restart=35, cycles=4, linear_method="gmres"):
        vector = self.seed(epsilon) if initial is None else initial.copy()
        for iteration in range(max_newton):
            residual, stats, fx, ft = self.residual(vector)
            record = dict(epsilon=epsilon, iteration=iteration, **stats)
            self.history.append(record)
            print(json.dumps(record), flush=True)
            if stats["retained_robin_system_residual"] < tolerance:
                return vector, True
            right = self.precondition(-residual, epsilon)
            calls = []

            def action(delta):
                dx, dt = self.jets(delta)
                return self.precondition(self.cross_coeff(fx, ft, dx, dt), epsilon)

            op = LinearOperator((vector.size, vector.size), matvec=action)
            if linear_method == "direct":
                delta, direct_info = self.direct_step(
                    vector, epsilon, residual, fx, ft)
                record.update(direct_info)
            else:
                delta, info = gmres(op, right, rtol=2e-4, atol=0.,
                                    restart=restart, maxiter=cycles,
                                    callback=lambda x: calls.append(float(x)),
                                    callback_type="pr_norm")
                record["gmres_info"] = int(info)
                record["gmres_iterations"] = len(calls)
                record["gmres_final"] = calls[-1] if calls else None
            accepted = False
            record["maximum_step"] = float(np.max(abs(delta)))
            for damping in [2.**(-j) for j in range(14)]:
                trial = vector+damping*delta
                _, trial_stats, _, _ = self.residual(trial)
                if trial_stats["retained_robin_system_residual"] < stats["retained_robin_system_residual"]:
                    vector = trial
                    record["damping"] = damping
                    accepted = True
                    break
            if not accepted:
                print(json.dumps(dict(stalled=record)), flush=True)
                return vector, False
        return vector, False

    def from_saved(self, saved):
        candidate = ps.make_candidate(saved, 1., order=1)
        coeff = np.zeros((self.modes, 3, self.points))
        for k, m in enumerate(self.mode):
            if int(m) in candidate["splines"]:
                coeff[k] = candidate["splines"][int(m)](self.x).T
                coeff[k, :2] *= self.h
                coeff[k] /= self.gamma
        alpha = np.array(saved["parameters"].get("mean_parameters", [0.]))
        alpha = np.r_[alpha, np.zeros(max(0, self.mean_count-alpha.size))]
        if alpha.size != self.mean_count:
            raise ValueError("saved state has more mean directions than requested")
        return self.pack(coeff, alpha)

    def saved_candidate(self, vector, epsilon):
        coeff, alpha = self.unpack(vector)
        modes = {0: (np.tensordot(alpha, self.means_c, axes=(0, 0)),
                     np.tensordot(alpha, self.means_d, axes=(0, 0)))}
        for k, m in enumerate(self.mode):
            c = coeff[k].copy()*self.gamma
            c[:2] /= self.h
            cd = np.stack([self.de@c[0], self.de@c[1], self.do@c[2]])
            modes[int(m)] = (c, cd)
        out = dict(self.series)
        out["fields"] = {1: modes}
        out["parameters"] = dict(self.series["parameters"], order=1,
                                 actual_epsilon=epsilon, modes=self.modes,
                                 mean_parameters=alpha.tolist(), mean_directions=self.mean_count,
                                 tail_weight=self.tail_weight, mean_gauge=self.mean_gauge,
                                 first_shift=self.first_shift,
                                 interpretation="make_candidate(series,1,order=1)")
        out["recursion"] = self.history
        return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mu-scale", type=float, default=4.)
    ap.add_argument("--points", type=int, default=801)
    ap.add_argument("--length", type=float, default=3.)
    ap.add_argument("--first-shift", type=int, choices=[0,1,2], default=0)
    ap.add_argument("--tail-weight", type=int, default=0)
    ap.add_argument("--mean-gauge", choices=["none","waist","radius"], default="none")
    ap.add_argument("--mean-directions", type=int, default=1)
    ap.add_argument("--mean", choices=["depth","bump"], default="depth")
    ap.add_argument("--bump-radius", type=float, default=.25)
    ap.add_argument("--modes", type=int, default=8)
    ap.add_argument("--epsilons", type=float, nargs="+",
                    default=[.02,.03,.04,.05,.06])
    ap.add_argument("--max-newton", type=int, default=12)
    ap.add_argument("--start-cache", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--cache", type=Path, required=True)
    ap.add_argument("--linear-method", choices=["gmres","direct"], default="gmres")
    ap.add_argument("--restart", type=int, default=35)
    ap.add_argument("--cycles", type=int, default=4)
    args = ap.parse_args()
    base = ps.build_series(order=7, points=args.points, length=args.length,
                           mean=args.mean, bump_radius=args.bump_radius,
                           mu_scale=args.mu_scale)
    solver = FourfoldNewton(base, modes=args.modes, mean_directions=args.mean_directions,
                            tail_weight=args.tail_weight, mean_gauge=args.mean_gauge,
                            first_shift=args.first_shift)
    if args.mean_directions > 1 and args.linear_method != "direct":
        raise ValueError("multiple means currently require --linear-method direct")
    previous = None
    last_eps = None
    if args.start_cache is not None:
        saved = ps.load_series(args.start_cache)
        if abs(saved["parameters"]["mu"]-base["parameters"]["mu"]) > 1e-12:
            raise ValueError("restart background mu does not match")
        previous = solver.from_saved(saved)
        last_eps = saved["parameters"]["actual_epsilon"]
    summaries = []
    for epsilon in args.epsilons:
        if previous is not None:
            coeff, alpha = solver.unpack(previous)
            coeff = coeff.copy()
            coeff[0] += (epsilon-last_eps)*solver.seed_scaled
            previous = solver.pack(coeff, alpha)
        answer, success = solver.solve(epsilon, previous, args.max_newton,
                                       restart=args.restart, cycles=args.cycles,
                                       linear_method=args.linear_method)
        candidate = solver.saved_candidate(answer, epsilon)
        diag = ps.metric_diagnostic(candidate, 1., 1, core=min(3.,args.length))
        summaries.append(dict(epsilon=epsilon, success=success,
                              actual_spline_metric=diag))
        ps.save_series(candidate, args.cache)
        cache_metadata = dict(
            kind="floating_partial_nonlinear_candidate_not_proof",
            file=args.cache.name, bytes=args.cache.stat().st_size,
            sha256=hashlib.sha256(args.cache.read_bytes()).hexdigest(),
            parameters=candidate["parameters"],
            retained_robin_system_solved=success,
            actual_spline_metric=diag,
            evaluator="load_series(path); make_candidate(series,1.0,order=1)",
            limitations=["finite Robin endpoint", "finite angular equations",
                         "ordinary double precision and sampled residuals",
                         "not a closed exact fixed-cap flexible family"])
        args.cache.with_suffix(".json").write_text(
            json.dumps(cache_metadata, indent=2)+"\n")
        args.out.write_text(json.dumps(dict(
            kind="floating_finite_fourier_newton_not_proof",
            parameters=vars(args) | {"out": str(args.out), "cache": str(args.cache),
                                     "start_cache": str(args.start_cache) if args.start_cache else None},
            history=solver.history, summaries=summaries), indent=2)+"\n")
        if not success:
            break
        previous, last_eps = answer, epsilon
    print(json.dumps(dict(summaries=summaries)), flush=True)


if __name__ == "__main__":
    main()
