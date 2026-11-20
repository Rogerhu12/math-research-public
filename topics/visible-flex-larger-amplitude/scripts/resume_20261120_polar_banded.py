#!/usr/bin/env python3
"""All-mode fixed-core polar steps with exact original Gram acceptance.

The local target minimizes ||V-Q1||^2+||d/a-rho*Q2||^2, Q.T Q=I.
Every original free interior three-jet, core horizontal acceleration, and
Hcap participates.  Core support coefficients are frozen during this
solver.  No change of scalar metric, mesh, analytic lift or Gram rows is
made.  A small continuous derivative regularizer selects the otherwise
underdetermined Z0 sampled-jet correction.  It is an auxiliary solver
term, not a change to the reported nonlinear objective.

FrozenCoreEnergy also supplies mutually transposed full-space right
factor actions.  Their core-coordinate block is an explicit scalar;
those actions retain every original free coordinate for a full solver.
No scientific work runs on import.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import cholesky_banded, cho_solve_banded, solve_banded


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    name = 'polar_banded_dependency_' + sha(path)[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def radial_rows(h, u):
    """Original quintic Y,U evaluation in endpoint (Y,U,A,Y,U,A) order."""
    if u == 0.:
        return np.array([1.,0,0,0,0,0]), np.array([0.,1,0,0,0,0])
    if u == 1.:
        return np.array([0.,0,0,1.,0,0]), np.array([0.,0,0,0,1.,0])
    if u == .5:
        return (np.array([.5,5*h/32,h*h/64,.5,-5*h/32,h*h/64]),
                np.array([-15/(8*h),-7/16,-h/32,15/(8*h),-7/16,h/32]))
    y = np.array([1-10*u**3+15*u**4-6*u**5,
                  h*(u-6*u**3+8*u**4-3*u**5),
                  h*h*(u*u-3*u**3+3*u**4-u**5)/2,
                  10*u**3-15*u**4+6*u**5,
                  h*(-4*u**3+7*u**4-3*u**5),
                  h*h*(u**3-2*u**4+u**5)/2])
    v = np.array([-30*u*u*(1-u)**2/h,
                  1-18*u*u+32*u**3-15*u**4,
                  h*(u-4.5*u*u+6*u**3-2.5*u**4),
                  30*u*u*(1-u)**2/h,
                  -12*u*u+28*u**3-15*u**4,
                  h*(1.5*u*u-4*u**3+2.5*u**4)])
    return y, v


def add_block(ab, start, block):
    for k in range(6):
        ab[k, start:start+6-k] += np.diagonal(block, offset=-k)


def band_action(ab, x):
    out = ab[0]*x
    for k in range(1, len(ab)):
        if k < len(x):
            out[k:] += ab[k, :-k]*x[:-k]
            out[:-k] += ab[k, :-k]*x[k:]
    return out


class RadialFactor:
    """Equilibrated lower-band Cholesky, A=D L L.T D."""

    def __init__(self, lower_band):
        self.band = np.array(lower_band, copy=True)
        self.n = self.band.shape[1]
        self.bandwidth = min(self.band.shape[0]-1, self.n-1)
        if np.any(self.band[0] <= 0) or not np.isfinite(self.band).all():
            raise ValueError('Nonpositive or nonfinite radial normal diagonal')
        self.scale = np.sqrt(self.band[0])
        scaled = self.band.copy()
        for k in range(len(scaled)):
            if k >= self.n:
                scaled[k] = 0.
                continue
            scaled[k, :self.n-k] /= self.scale[k:]*self.scale[:self.n-k]
            if k:
                scaled[k, self.n-k:] = 0.
        self.lower = cholesky_banded(scaled, lower=True, check_finite=False)
        self.upper = None

    def solve(self, rhs):
        return cho_solve_banded((self.lower, True), rhs/self.scale,
                                check_finite=False)/self.scale

    def right(self, x):
        """D^-1 L^-T x; its product with its transpose is A^-1."""
        if self.upper is None:
            bw = self.lower.shape[0]-1
            upper = np.zeros_like(self.lower)
            for k in range(bw+1):
                if k < self.n:
                    upper[bw-k, k:] = self.lower[k, :self.n-k]
            self.upper = upper
        return solve_banded((0, self.upper.shape[0]-1), self.upper, x,
                            check_finite=False)/self.scale

    def right_transpose(self, x):
        return solve_banded((self.lower.shape[0]-1, 0), self.lower,
                            x/self.scale, check_finite=False)

    def residual_ratio(self, solution, rhs):
        residual = (band_action(self.band, solution)-rhs)/self.scale
        return float(np.linalg.norm(residual)/max(1., np.linalg.norm(rhs/self.scale)))


class FrozenCoreEnergy:
    """All modes and all free jets; banded radial normal plus Z0/H border.

    Native data energy is sum_stage,angle multiplicity *
        (|delta Fs-targetV|^2 + |delta Fphi-targetd|^2/a^2).
    Add eta*sum_cell h^-1 int_cell |delta Fs|^2 ds, integrated after
    splitting at the analytic chi breakpoint.  eta>0 removes the exact
    Z0 node/midpoint underintegration kernel without dropping variables.

    Future stage interface: observations may be a list of dictionaries
    {left: cell index, u: local coordinate, a: exact supplied scalar,
     weight: positive stage weight}.  The nodal fields and their boundary
    conditions are unchanged; this only builds the corresponding linear
    energy.  A future nonlinear operator must supply its own matching
    actual fields and Gram rows.  This module's CLI uses native stages.
    """

    def __init__(self, operator, *, regularization=1.e-6, observations=None):
        self.o = o = operator
        self.eta = float(regularization)
        if not self.eta > 0 or not np.isfinite(self.eta):
            raise ValueError('Positive finite continuous regularization required')
        self.native_stages = observations is None
        if observations is None:
            observations = []
            for stage, a in enumerate(o.a):
                if stage % 2:
                    left, u = stage//2, .5
                elif stage//2 == o.J-1:
                    left, u = o.J-2, 1.
                else:
                    left, u = stage//2, 0.
                observations.append(dict(left=left, u=u, a=float(a), weight=1.))
        self.observations = [dict(z) for z in observations]
        self.count = len(self.observations)
        self.rows_y = np.empty((self.count, 6))
        self.rows_u = np.empty((self.count, 6))
        self.cells = np.empty(self.count, dtype=int)
        self.weights = np.empty(self.count)
        self.cp = np.empty(self.count)
        self.stage_a = np.empty(self.count)
        size = 3*o.J
        velocity, position, regular = (np.zeros((6, size)) for _ in range(3))
        cross = np.zeros(size)
        cross_regular = np.zeros(size)
        height, height_regular = 0., 0.
        for j, z in enumerate(self.observations):
            i, u, a = int(z['left']), float(z['u']), float(z['a'])
            w = float(z.get('weight', 1.))
            if not (0 <= i < o.J-1 and 0 <= u <= 1 and a > 0 and w > 0
                    and np.isfinite([u, a, w]).all()):
                raise ValueError('Invalid radial observation')
            h = o.mesh[i+1]-o.mesh[i]
            y, v = radial_rows(h, u)
            s = o.mesh[i] if u == 0 else o.mesh[i+1] if u == 1 else o.mesh[i]+u*h
            cp = o._lift_scalar(float(s))[1]
            self.cells[j], self.weights[j], self.cp[j], self.stage_a[j] = i, w, cp, a
            self.rows_y[j], self.rows_u[j] = y, v
            add_block(velocity, 3*i, w*np.outer(v, v))
            add_block(position, 3*i, (w/(a*a))*np.outer(y, y))
            cross[3*i:3*i+6] += w*cp*v
            height += w*cp*cp
        points, weights = np.polynomial.legendre.leggauss(5)
        breakpoint = o.S-o.width
        for i, h in enumerate(np.diff(o.mesh)):
            lo, hi = o.mesh[i], o.mesh[i+1]
            cuts = [0., 1.]
            if lo < breakpoint < hi:
                cuts.insert(1, (breakpoint-lo)/h)
            for ul, ur in zip(cuts[:-1], cuts[1:]):
                for p, w in zip(points, weights):
                    u = ul+(ur-ul)*(p+1)/2
                    weight = (ur-ul)*w/2
                    _, v = radial_rows(h, u)
                    cp = o._lift_scalar(float(lo+h*u))[1]
                    add_block(regular, 3*i, weight*np.outer(v, v))
                    cross_regular[3*i:3*i+6] += weight*cp*v
                    height_regular += weight*cp*cp
        self.velocity = velocity+self.eta*regular
        self.position = position
        self.cross_full = cross+self.eta*cross_regular
        self.height_normal = height+self.eta*height_regular
        self.stop = 3*(o.J-1)
        self.factors = {}
        self.zfactor = self.factor('z', 0)
        self.cross = self.cross_full[3:self.stop]
        self.height_response = self.zfactor.solve(self.cross)
        self.schur = float(self.height_normal-self.cross@self.height_response)
        if not self.schur > 0 or not np.isfinite(self.schur):
            raise ValueError('Nonpositive Z0/H Schur complement: '+repr(self.schur))
        self.sqrt_schur = np.sqrt(self.schur)

    def factor(self, kind, frequency_squared):
        key = kind, int(frequency_squared)
        if key not in self.factors:
            start = 2 if kind == 'xy' else 3
            band = (self.velocity+frequency_squared*self.position)[:, start:self.stop].copy()
            n = band.shape[1]
            for k in range(1, len(band)):
                band[k, max(n-k, 0):] = 0.
            self.factors[key] = RadialFactor(band)
        return self.factors[key]

    def adjoint_block(self, start, gy, gu, grad):
        """Add radial transpose; angular weights already belong in gy/gu."""
        height = 0.
        z0 = 2*self.o.M+1
        for b in range(len(gy)):
            j = start+b
            i, w = self.cells[j], self.weights[j]
            value = w*(self.rows_y[j, :, None]*gy[b]
                       + self.rows_u[j, :, None]*gu[b])
            grad[i:i+2] += value.reshape(2, 3, self.o.n)
            height += w*self.cp[j]*gu[b, z0]
        return float(height)

    def _put(self, jets, slot, values, start):
        flat = np.zeros(3*self.o.J)
        flat[start:self.stop] = values
        jets[:, :, slot] = flat.reshape(self.o.J, 3)

    def solve(self, gradient_jets, gradient_height):
        """Solve the exact stated regularized linear subproblem in float64."""
        o, M, N = self.o, self.o.M, self.o.full_N
        g = np.asarray(gradient_jets)
        if g.shape != (o.J, 3, o.n):
            raise ValueError('Wrong nodal cotangent shape')
        result = np.zeros_like(g)
        errors = []
        def scalar(slot, kind, lam, norm):
            start = 2 if kind == 'xy' else 3
            rhs = g[:, :, slot].ravel()[start:self.stop]/norm
            factor = self.factor(kind, lam)
            value = factor.solve(rhs)
            errors.append(factor.residual_ratio(value, rhs))
            self._put(result, slot, value, start)
        scalar(0, 'xy', 1, N)
        root2 = np.sqrt(2.)
        for m in range(1, M+1):
            r = g[:, :, m].ravel()[2:self.stop]/(N/2)
            t = g[:, :, M+m].ravel()[2:self.stop]/(N/2)
            fp, fm = self.factor('xy', (2*m+1)**2), self.factor('xy', (2*m-1)**2)
            rp, rm = (r+t)/root2, (r-t)/root2
            p, n = fp.solve(rp), fm.solve(rm)
            errors += [fp.residual_ratio(p, rp), fm.residual_ratio(n, rm)]
            self._put(result, m, (p+n)/root2, 2)
            self._put(result, M+m, (p-n)/root2, 2)
            scalar(2*M+1+m, 'z', (2*m)**2, N/2)
        rhs = g[:, :, 2*M+1].ravel()[3:self.stop]/N
        rh = float(gradient_height)/N
        unconstrained = self.zfactor.solve(rhs)
        height = float((rh-self.cross@unconstrained)/self.schur)
        z = unconstrained-self.height_response*height
        self._put(result, 2*M+1, z, 3)
        qres = (band_action(self.zfactor.band, z)+self.cross*height-rhs)/self.zfactor.scale
        hres = (self.cross@z+self.height_normal*height-rh)/np.sqrt(self.height_normal)
        denom = max(1., np.linalg.norm(rhs/self.zfactor.scale), abs(rh)/np.sqrt(self.height_normal))
        errors.append(float(np.hypot(np.linalg.norm(qres), hres)/denom))
        info = dict(max_scaled_linear_residual=max(errors),
                    regularization=self.eta, z0_height_schur=self.schur,
                    radial_factor_count=len(self.factors), all_modes=M)
        return result, height, info

    def pack_direction(self, jets, height, core=None):
        o = self.o
        if core is None:
            core = np.zeros(o.M-o.K)
        return np.concatenate((core, jets[0, 2, :2*o.M+1],
                               jets[1:-1].ravel(), [height]))

    def _right_action(self, vector, *, transpose, core_scale):
        o, M, N = self.o, self.o.M, self.o.full_N
        if not np.isfinite(core_scale) or core_scale <= 0:
            raise ValueError('Positive finite full-space core scale required')
        vector = np.asarray(vector)
        jets, h, _ = o.unpack(vector, tangent=True)
        result = np.zeros_like(jets)
        root2 = np.sqrt(2.)
        def action(f, x):
            return f.right_transpose(x) if transpose else f.right(x)
        def scalar(slot, kind, lam, norm):
            start = 2 if kind == 'xy' else 3
            x = jets[:, :, slot].ravel()[start:self.stop]
            y = action(self.factor(kind, lam), x)/np.sqrt(norm)
            self._put(result, slot, y, start)
        scalar(0, 'xy', 1, N)
        for m in range(1, M+1):
            r = jets[:, :, m].ravel()[2:self.stop]
            t = jets[:, :, M+m].ravel()[2:self.stop]
            p = action(self.factor('xy', (2*m+1)**2), (r+t)/root2)/np.sqrt(N/2)
            n = action(self.factor('xy', (2*m-1)**2), (r-t)/root2)/np.sqrt(N/2)
            self._put(result, m, (p+n)/root2, 2)
            self._put(result, M+m, (p-n)/root2, 2)
            scalar(2*M+1+m, 'z', (2*m)**2, N/2)
        z = jets[:, :, 2*M+1].ravel()[3:self.stop]
        if transpose:
            zh = (h-self.height_response@z)/(np.sqrt(N)*self.sqrt_schur)
            znew = self.zfactor.right_transpose(z)/np.sqrt(N)
        else:
            zh = h/(np.sqrt(N)*self.sqrt_schur)
            znew = self.zfactor.right(z)/np.sqrt(N)-self.height_response*zh
        self._put(result, 2*M+1, znew, 3)
        return self.pack_direction(result, zh, core_scale*vector[:M-o.K])

    def right_factor(self, vector, *, core_scale=1.):
        return self._right_action(vector, transpose=False, core_scale=core_scale)

    def right_factor_transpose(self, vector, *, core_scale=1.):
        return self._right_action(vector, transpose=True, core_scale=core_scale)


def gram_stats(o, x):
    raw = o.raw_residual(x)
    ss, cross, pp = raw[..., 0], raw[..., 1], raw[..., 2]
    norm = (np.abs(ss+pp)+np.sqrt((ss-pp)**2+4*cross*cross))/2
    worst = np.unravel_index(int(np.argmax(norm)), norm.shape)
    return dict(raw_sse=float(np.sum(o.multiplicity[None, :]*(ss*ss+2*cross*cross+pp*pp))),
                sampled_max_gram=float(norm[worst]),
                sampled_min_determinant=float(np.min((1+ss)*(1+pp)-cross*cross)),
                worst=[int(worst[0]), int(worst[1]), float(o.times[worst[0]]), float(o.phi[worst[1]])])


def polar_direction(o, x, energy):
    if not energy.native_stages or energy.count != o.P:
        raise ValueError('CLI polar target requires native original stages')
    o.set_base(x)
    p = o._base_p
    if np.any(p.rho <= 0):
        raise ValueError('Nonpositive material density')
    grad = np.zeros((o.J, 3, o.n))
    gh, distance, min_sigma, orthogonality = 0., 0., float('inf'), 0.
    for start in range(0, o.P, o.stage_block):
        stop = min(start+o.stage_block, o.P)
        V, d = o._first_batch(p, start, stop)
        a = o.a[start:stop, None]
        T = np.stack((V, d*(p.rho[None, :]/a)[:, :, None]), axis=-1)
        U, singular, Vh = np.linalg.svd(T, full_matrices=False)
        Q = U@Vh
        target_v = Q[..., 0]-V
        target_d = (a*p.rho[None, :])[:, :, None]*Q[..., 1]-d
        weighted_v = target_v*o.multiplicity[None, :, None]
        weighted_d = target_d*(o.multiplicity[None, :]/(a*a))[:, :, None]
        gy, gu = o._linear_fields_adjoint(weighted_v, weighted_d)
        gh += energy.adjoint_block(start, gy, gu, grad)
        distance += float(np.sum(o.multiplicity[None, :]*(np.sum(target_v*target_v, axis=2)
                         +np.sum(target_d*target_d, axis=2)/(a*a))))
        min_sigma = min(min_sigma, float(np.min(singular[..., -1])))
        orthogonality = max(orthogonality,
                           float(np.max(np.abs(np.swapaxes(Q, -1, -2)@Q-np.eye(2)))))
    jets, height, info = energy.solve(grad, gh)
    info.update(local_target_distance=distance, local_min_singular=min_sigma,
                local_max_orthogonality_error=orthogonality)
    return energy.pack_direction(jets, height), info


def gradient_direction(o, x, energy):
    residual = o.residual(x)
    residual[..., 1] *= 2
    grad = o.vjp(x, residual)
    grad[:o.M-o.K] = 0.
    gjets, gh, _ = o.unpack(-grad, tangent=True)
    jets, height, info = energy.solve(gjets, gh)
    direction = energy.pack_direction(jets, height)
    jv = o.jvp(x, direction)
    denom = float(np.sum(jv[..., 0]**2+2*jv[..., 1]**2+jv[..., 2]**2))
    descent = float(-grad@direction)
    if not (descent > 0 and denom > 0 and np.isfinite([descent, denom]).all()):
        raise ValueError('No finite strict preconditioned-gradient descent')
    scale = descent/denom
    info.update(gradient_dot_negative_direction=descent,
                linearized_optimal_scale=scale)
    return scale*direction, info


def line_search(o, x, direction, before, backtracks):
    trials = []
    for k in range(backtracks):
        alpha = 2.**(-k)
        candidate = x+alpha*direction
        try:
            state = gram_stats(o, candidate)
            accepted = (np.isfinite(state['raw_sse'])
                        and state['sampled_min_determinant'] > 0
                        and state['raw_sse'] < before['raw_sse'])
            trials.append(dict(alpha=alpha, accepted=accepted, **state))
        except (FloatingPointError, OverflowError) as error:
            accepted = False
            trials.append(dict(alpha=alpha, accepted=False, error=repr(error)))
        if accepted:
            return candidate, state, trials
    return x, before, trials


def main(args):
    started = time.monotonic()
    if args.out.exists() or args.out.with_suffix('.npz').exists():
        raise FileExistsError('Use a fresh output path')
    bundle = np.load(args.bundle, allow_pickle=False)
    batch = load(args.batch_source)
    o = batch.create(args.operator, bundle['mesh'], bundle['a_stages'],
                     float(bundle['radius']), bundle['fixed_core_first3'],
                     M=(bundle['qjets'].shape[-1]-2)//3, N=args.angles,
                     width=float(bundle['width']), quarter=True, stage_block=args.stage_block)
    x, affine0 = o.pack(bundle['qjets'], float(bundle['Hcap']), require_affine=True)
    x_initial = x.copy()
    energy = FrozenCoreEnergy(o, regularization=args.regularization)
    initial = state = gram_stats(o, x)
    records, status = [], 'iteration_budget'
    for iteration in range(args.steps):
        if time.monotonic()-started > args.seconds:
            status = 'time_budget'
            break
        before = state
        direction, diagnostic = polar_direction(o, x, energy)
        candidate, newstate, trials = line_search(o, x, direction, before, args.backtracks)
        mode = 'polar'
        attempts = [dict(mode=mode, direction_norm=float(np.linalg.norm(direction)),
                         diagnostic=diagnostic, trials=trials)]
        if candidate is x and not args.no_gradient_fallback:
            mode = 'energy_preconditioned_original_gradient'
            direction, diagnostic = gradient_direction(o, x, energy)
            candidate, newstate, trials = line_search(o, x, direction, before, args.backtracks)
            attempts.append(dict(mode=mode, direction_norm=float(np.linalg.norm(direction)),
                                 diagnostic=diagnostic, trials=trials))
        accepted = candidate is not x
        record = dict(iteration=iteration, before=before, after=newstate,
                      accepted=accepted, accepted_mode=mode if accepted else None,
                      attempts=attempts, elapsed_seconds=time.monotonic()-started)
        records.append(record)
        x, state = candidate, newstate
        print(json.dumps(record), flush=True)
        args.out.with_suffix('.progress.json').write_text(json.dumps(dict(
            source_sha256=sha(__file__), input_sha256=sha(args.bundle),
            initial=initial, current=state, records=records), indent=2)+'\n')
        if not accepted:
            status = 'line_search_failed'
            break
    jets, height, _ = o.unpack(x)
    _, affine1 = o.pack(jets, height, require_affine=True)
    final = gram_stats(o, x)
    if not np.array_equal(x[:o.M-o.K], x_initial[:o.M-o.K]):
        raise ValueError('Frozen core changed')
    keys = ('mesh','a_stages','radius','width','fixed_core_first3',
            'a_stage_absolute_error','stage_time_absolute_error')
    arrays = {k:np.array(bundle[k], copy=True) for k in keys if k in bundle.files}
    arrays.update(qjets=jets, Hcap=np.asarray(height))
    output = args.out.with_suffix('.npz')
    np.savez_compressed(output, **arrays)
    report = dict(schema='fullclosed-all-mode-polar-banded-v1', status=status,
                  source_sha256=sha(__file__), operator_sha256=sha(args.operator),
                  batch_source_sha256=sha(args.batch_source), input_sha256=sha(args.bundle),
                  output_bundle_sha256=sha(output), initial=initial, final=final,
                  initial_height=float(bundle['Hcap']), final_height=float(height),
                  full_variables=o.free_size,
                  local_free_variables=o.free_size-(o.M-o.K), core_coefficients_frozen=True,
                  all_original_residual_rows_retained=True, full_rows=o.P*o.full_N*3,
                  packed_rows=o.P*o.N*3, regularization=args.regularization,
                  regularization_definition='sum_cells h^-1 integral |delta Fs|^2 ds',
                  regularization_only_in_step=True, band_lower_width=5,
                  quadrature_order=5, chi_break_split=True,
                  radial_factors=len(energy.factors), z0_height_schur=energy.schur,
                  exact_affine_initial=affine0, exact_affine_final=affine1,
                  fixed_metric_scalar_and_mesh_unchanged=True,
                  iterations=records, elapsed_seconds=time.monotonic()-started,
                  sampled_metric_accepted=final['sampled_max_gram'] <= 1.e-6,
                  continuous_metric_certified=False, exact_solution_claimed=False,
                  reach_certified=False, held_certified=False)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'iterations'}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle','operator','batch-source','out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--regularization', type=float, default=1.e-6)
    parser.add_argument('--steps', type=int, default=6)
    parser.add_argument('--backtracks', type=int, default=12)
    parser.add_argument('--seconds', type=float, default=600.)
    parser.add_argument('--no-gradient-fallback', action='store_true')
    main(parser.parse_args())
