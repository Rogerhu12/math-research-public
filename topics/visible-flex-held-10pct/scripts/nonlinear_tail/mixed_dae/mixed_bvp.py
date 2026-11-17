"""Hermite--Simpson BVP for the complete finite (v,t,L) momentum equations.

The local algebraic equations are retained as rows of one global Newton
system. No local A, Gram matrix, or Schur complement is inverted here.
This experimental implementation does not replace the positive-A tail solver.
"""
from __future__ import annotations

import warnings
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import MatrixRankWarning, spsolve


class MixedBVP:
    def __init__(self, fields, x, profile, left_v, right_t):
        self.f = fields
        self.x = np.asarray(x, dtype=float)
        if len(self.x) < 3 or len(self.x) % 2 != 1 or np.any(np.diff(self.x) <= 0):
            raise ValueError('Need increasing endpoint/midpoint nodes')
        if not np.allclose(self.x[1::2], (self.x[:-2:2] + self.x[2::2])/2,
                           rtol=0, atol=1e-14):
            raise ValueError('Interior odd nodes must be interval midpoints')
        self.n = len(x)
        self.k = (self.n-1)//2
        self.profile = profile
        self.left_v = np.asarray(left_v, float)
        self.right_t = np.asarray(right_t, float)
        if self.left_v.shape != (fields.d,) or self.right_t.shape != (fields.d,):
            raise ValueError('Full represented boundary vectors are required')
        self.size = self.n * fields.width

    def evaluate(self, Y, jacobian=False):
        f = self.f
        d, width, n = f.d, f.width, self.n
        Y = np.asarray(Y, float).reshape(n, width)
        p = self.profile(self.x)
        e = f.evaluate(Y, **p, jacobian=jacobian)
        flow = e['flow']
        rows = [e['algebraic'].ravel()]
        triplets = []

        def block(row, col, value):
            value = np.asarray(value)
            ii, jj = np.nonzero(value)
            triplets.append((row+ii, col+jj, value[ii, jj]))

        if jacobian:
            for j in range(n):
                block(j*f.J, j*width, e['algebraic_jacobian'][j])
        row = n*f.J
        selector = np.eye(2*d, width)
        for j in range(self.k):
            l, m, r = 2*j, 2*j+1, 2*j+2
            h = self.x[r]-self.x[l]
            rm = Y[m, :2*d] - .5*(Y[l, :2*d]+Y[r, :2*d]) - h/8*(flow[l]-flow[r])
            re = Y[r, :2*d] - Y[l, :2*d] - h/6*(flow[l]+4*flow[m]+flow[r])
            rows.extend([rm, re])
            if jacobian:
                jf = e['flow_jacobian']
                block(row, l*width, -.5*selector-h/8*jf[l])
                block(row, m*width, selector)
                block(row, r*width, -.5*selector+h/8*jf[r])
                block(row+2*d, l*width, -selector-h/6*jf[l])
                block(row+2*d, m*width, -2*h/3*jf[m])
                block(row+2*d, r*width, selector-h/6*jf[r])
            row += 4*d
        rows.extend([Y[0, :d]-self.left_v, Y[-1, d:2*d]-self.right_t])
        if jacobian:
            block(row, 0, np.eye(d, width))
            sel_t = np.zeros((d, width))
            sel_t[:, d:2*d] = np.eye(d)
            block(row+d, (n-1)*width, sel_t)
        residual = np.concatenate(rows)
        if residual.size != self.size:
            raise AssertionError('Mixed BVP dimension mismatch')
        result = dict(residual=residual, fields=e,
                      ode_residual=float(np.max(abs(residual[n*f.J:-2*d]))),
                      boundary_residual=float(np.max(abs(residual[-2*d:]))),
                      root_relative=float(np.max(e['root_relative'])))
        if jacobian:
            ii = np.concatenate([v[0] for v in triplets])
            jj = np.concatenate([v[1] for v in triplets])
            vv = np.concatenate([v[2] for v in triplets])
            result['jacobian'] = coo_matrix((vv, (ii, jj)), shape=(self.size, self.size)).tocsc()
        return result

    def solve(self, initial, max_iterations=16, root_tol=8e-14, ode_tol=1e-11,
              callback=None):
        Y = np.asarray(initial, float).reshape(self.n, self.f.width).copy()
        initial_e = self.evaluate(Y)
        f = self.f
        # These fixed row scales change neither the equations nor their final
        # acceptance tests. They only balance the Newton merit function.
        root_scale = max(initial_e['fields']['max_quad'], float(np.max(abs(Y[:, f.d:2*f.d]))), 1e-15)
        state_scale = np.maximum(np.max(abs(Y[:, :2*f.d]), axis=0), 1e-3)
        scales = np.r_[np.full(self.n*f.J, root_scale),
                       np.tile(state_scale, 2*self.k),
                       state_scale[:f.d], state_scale[f.d:]]
        history = []
        stopped = 'maximum_iterations'
        for iteration in range(max_iterations+1):
            e = self.evaluate(Y, True)
            residual = e['residual']
            merit = float(np.linalg.norm(residual/scales))
            row = dict(iteration=iteration, merit=merit,
                       root_relative=e['root_relative'], ode_residual=e['ode_residual'],
                       boundary_residual=e['boundary_residual'], minD=e['fields']['minD'],
                       minS=e['fields']['minS'], minA=e['fields']['minA'])
            history.append(row)
            if callback:
                callback(row)
            if e['root_relative'] <= root_tol and max(e['ode_residual'], e['boundary_residual']) <= ode_tol:
                stopped = 'accepted'
                break
            if iteration == max_iterations:
                break
            # Only the complete mixed Jacobian is factored. Neither G nor an
            # elimination of the pointwise L equations is factored separately.
            with warnings.catch_warnings():
                warnings.simplefilter('error', MatrixRankWarning)
                try:
                    step = spsolve(e['jacobian'], -residual)
                except (MatrixRankWarning, RuntimeError) as error:
                    stopped = 'global_linear_solve_failed: '+str(error)
                    break
            if not np.all(np.isfinite(step)):
                stopped = 'nonfinite_global_newton_step'
                break
            row['linear_residual'] = float(np.max(abs(e['jacobian']@step+residual)))
            step = step.reshape(Y.shape)
            accepted = False
            for power in range(25):
                alpha = 2.**(-power)
                try:
                    trial = self.evaluate(Y+alpha*step)
                    trial_merit = float(np.linalg.norm(trial['residual']/scales))
                except FloatingPointError:
                    continue
                if trial_merit < merit*(1-1e-4*alpha):
                    Y += alpha*step
                    row['step_scale'] = alpha
                    accepted = True
                    break
            if not accepted:
                stopped = 'global_line_search_failed'
                break
        final = self.evaluate(Y, True)
        return dict(Y=Y, success=stopped == 'accepted', stop_reason=stopped,
                    history=history, final=final, row_scales=scales,
                    root_tolerance=root_tol, ode_tolerance=ode_tol)
