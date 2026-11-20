#!/usr/bin/env python3
"""Complete coarse three-jet physical corrections for fixed-Hold Gram.

The original full finite objective and affine boundary conditions remain
unchanged.  Five coarse radial nodes x three jets x eleven angular
channels, seven free core-acceleration directions, and one global cap
height direction give 173 search coordinates.  The 1.33M-coordinate
problem is not replaced or claimed to be equivalent to this subspace.

Recovery status: the first draft was written locally but never executed.
This publication adapts its base-source CLI for a portable checkout.
No numerical result is attributed to this version before a fresh run.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    name = 'physical_subspace_v2_dependency_' + sha(path)[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polynomial_jets(coefficients, u, width):
    c = np.asarray(coefficients, dtype=float)
    d = np.arange(1, len(c))*c[1:]
    dd = np.arange(1, len(d))*d[1:]
    return np.stack((np.polynomial.polynomial.polyval(u, c),
                     np.polynomial.polynomial.polyval(u, d)/width,
                     np.polynomial.polynomial.polyval(u, dd)/width**2), axis=-1)


def make_space(base_source, operator, low_modes=3):
    base = load(base_source)

    class ThreeJetSpace(base.PhysicalSubspace):
        def __init__(self, o):
            super().__init__(o, low_modes=low_modes)
            position = self.node_jets[:self.bump_count].copy()
            extra_core = self.node_jets[self.core_radial].copy()
            extra_height = self.node_jets[self.height_radial].copy()
            old_names = self.radial_names[:self.bump_count]
            ids = self.center_nodes
            breaks = [0]+ids+[o.J-1]
            nodal = list(position)
            names = ['Y_'+s for s in old_names]
            for order in (1, 2):
                for k, mid in enumerate(ids):
                    left, right = breaks[k], breaks[k+2]
                    hl, hr = o.mesh[mid]-o.mesh[left], o.mesh[right]-o.mesh[mid]
                    b = np.zeros((o.J, 3))
                    if order == 1:
                        # Right derivative cardinal on left interval,
                        # left derivative cardinal on right interval.
                        cl = hl*np.array([0., 0., 0., -4., 7., -3.])
                        cr = hr*np.array([0., 1., 0., -6., 8., -3.])
                    else:
                        cl = hl*hl*np.array([0., 0., 0., .5, -1., .5])
                        cr = hr*hr*np.array([0., 0., .5, -1.5, 1.5, -.5])
                    b[left:mid+1] = polynomial_jets(
                        cl, (o.mesh[left:mid+1]-o.mesh[left])/hl, hl)
                    b[mid:right+1] = polynomial_jets(
                        cr, (o.mesh[mid:right+1]-o.mesh[mid])/hr, hr)
                    b[left] = 0.; b[right] = 0.; b[mid] = 0.; b[mid, order] = 1.
                    nodal.append(b)
                    names.append(('U_' if order == 1 else 'A_')+old_names[k])
            self.bump_count = len(nodal)
            self.core_radial = len(nodal)
            nodal.append(extra_core); names.append('global_core_second_jet')
            self.height_radial = len(nodal)
            nodal.append(extra_height); names.append('global_height_with_cap')
            self.node_jets = np.asarray(nodal)
            self.radial_names = names
            self.nb = len(nodal)
            self.stage_y = np.zeros((o.P, self.nb))
            self.stage_u = np.zeros((o.P, self.nb))
            for k, b in enumerate(nodal):
                self.stage_y[::2, k] = b[:, 0]
                self.stage_u[::2, k] = b[:, 1]
                for i, weights in enumerate(o.mid_weights):
                    v = weights @ b[i:i+2].ravel()
                    self.stage_y[2*i+1, k] = v[0]
                    self.stage_u[2*i+1, k] = v[1]
            self.stage_y[:, self.height_radial] += o.lift_scalar[:, 0]
            self.stage_u[:, self.height_radial] += o.lift_scalar[:, 1]
            pairs = [(k, j) for k in range(self.bump_count) for j in range(self.nc)]
            pairs += [(self.core_radial, j) for j, c in enumerate(self.channels) if c[0] != 'Z']
            pairs += [(self.height_radial, 1)]
            self.pairs = np.asarray(pairs, dtype=int)
            self.dimension = len(pairs)

        def free_direction(self, coefficients):
            o = self.o
            jets, height = self.candidate(np.zeros((o.J, 3, o.n)), 0., coefficients)
            return np.concatenate((np.zeros(o.M-o.K), jets[0, 2, :2*o.M+1],
                                   jets[1:-1].ravel(), [height]))

        def transpose_free(self, free_gradient):
            o = self.o
            grad = np.asarray(free_gradient)
            if grad.shape != (o.free_size,):
                raise ValueError('Wrong complete-space cotangent')
            jets = np.zeros((o.J, 3, o.n))
            at = o.M-o.K
            jets[0, 2, :2*o.M+1] = grad[at:at+2*o.M+1]
            at += 2*o.M+1
            jets[1:-1] = grad[at:-1].reshape((o.J-2, 3, o.n))
            result = np.array([np.sum(self.node_jets[k]*jets[:, :, self.channels[j][2]])
                               for k, j in self.pairs])
            result[-1] += grad[-1]
            return result

        def evaluate(self, base_first, rho, coefficients, *, linearize=False):
            """Separated 11x11 angular kernels, then exact radial expansion."""
            o = self.o
            c = self.coefficient_matrix(coefficients)
            yu, yy = self.stage_u @ c, self.stage_y @ c
            gram = np.zeros((self.dimension, self.dimension)) if linearize else None
            gradient = np.zeros(self.dimension) if linearize else None
            cost = 0.; maximum = 0.; determinant = float('inf'); worst = None
            ri, cj = self.pairs.T
            sw, mw = self.sqrt_multiplicity, self.multiplicity
            for stage, a in enumerate(o.a):
                V = base_first[0, stage] + np.einsum('c,nck->nk', yu[stage], self.h)
                d = base_first[1, stage] + np.einsum('c,nck->nk', yy[stage], self.dh)
                ar = a*rho
                r0 = np.sum(V*V, axis=1)-1.
                r1 = np.sum(V*d, axis=1)/ar
                r2 = np.sum(d*d, axis=1)/(ar*ar)-1.
                cost += float(mw @ (r0*r0+2*r1*r1+r2*r2))
                norm = (abs(r0+r2)+np.sqrt((r0-r2)**2+4*r1*r1))/2
                j = int(np.argmax(norm))
                if norm[j] > maximum:
                    maximum = float(norm[j])
                    worst = [stage, j, float(o.times[stage]), float(o.phi[j])]
                determinant = min(determinant, float(np.min((1+r0)*(1+r2)-r1*r1)))
                if not linearize:
                    continue
                by, bu = self.stage_y[stage, ri], self.stage_u[stage, ri]
                active = np.flatnonzero((by != 0) | (bu != 0))
                if active.size == 0:
                    continue
                v_h = np.einsum('nk,nck->nc', V, self.h)
                d_h = np.einsum('nk,nck->nc', d, self.h)
                v_dh = np.einsum('nk,nck->nc', V, self.dh)
                d_dh = np.einsum('nk,nck->nc', d, self.dh)
                a0 = (2*sw)[:,None]*v_h
                a1 = (sw/ar)[:,None]*d_h
                b1 = (sw/ar)[:,None]*v_dh
                b2 = (2*sw/(ar*ar))[:,None]*d_dh
                kuu = a0.T@a0 + 2*a1.T@a1
                kuy = 2*a1.T@b1
                kyy = 2*b1.T@b1 + b2.T@b2
                gu = a0.T@(sw*r0) + 2*a1.T@(sw*r1)
                gy = 2*b1.T@(sw*r1) + b2.T@(sw*r2)
                ci = cj[active]
                ix = np.ix_(ci, ci)
                u, y = bu[active], by[active]
                block = (np.outer(u, u)*kuu[ix] + np.outer(u, y)*kuy[ix]
                         + np.outer(y, u)*kuy.T[ix] + np.outer(y, y)*kyy[ix])
                gram[np.ix_(active, active)] += block
                gradient[active] += u*gu[ci] + y*gy[ci]
            return dict(raw_sse=cost, sampled_max_gram=maximum,
                        sampled_min_determinant=determinant, worst=worst,
                        normal_matrix=gram, gradient=gradient)

    return ThreeJetSpace(operator)


def summary(state):
    return {k:v for k,v in state.items() if k not in ('normal_matrix','gradient')}


def main(a):
    started = time.monotonic()
    source = sha(__file__)
    if a.out.exists() or a.out.with_suffix('.npz').exists():
        raise FileExistsError('Use a fresh output name')
    bundle = np.load(a.bundle, allow_pickle=False)
    arrays = {k:np.array(bundle[k], copy=True) for k in bundle.files}
    batch = load(a.batch_source)
    o = batch.create(a.operator, arrays['mesh'], arrays['a_stages'],
                     float(arrays['radius']), arrays['fixed_core_first3'],
                     M=(arrays['qjets'].shape[2]-2)//3, N=a.angles,
                     width=float(arrays['width']), quarter=True, stage_block=64)
    x0, affine0 = o.pack(arrays['qjets'], float(arrays['Hcap']), require_affine=True)
    cache = o.set_base(x0)
    b = make_space(a.base_source, o, low_modes=a.low_modes)
    coefficients = np.zeros(b.dimension)
    lm = a.damping; records = []; first = None; status = 'iteration_budget'
    for iteration in range(a.steps):
        if time.monotonic()-started > a.seconds:
            status = 'time_budget'; break
        state = b.evaluate(o._base_first, o._base_p.rho, coefficients, linearize=True)
        if first is None:
            first = summary(state)
        A, g = state['normal_matrix'], state['gradient']
        scale = np.sqrt(np.maximum(np.diag(A), np.max(np.diag(A))*1.e-28))
        C = A/scale[:,None]/scale[None,:]
        step = np.linalg.solve(C+lm*np.eye(b.dimension), -g/scale)/scale
        record = dict(iteration=iteration, before=summary(state), damping=lm,
                      direction_norm=float(np.linalg.norm(step)), trials=[])
        accepted = False
        for k in range(a.backtracks):
            alpha = 2.**(-k)
            trial = b.evaluate(o._base_first, o._base_p.rho, coefficients+alpha*step)
            ok = (np.isfinite(trial['raw_sse']) and trial['sampled_min_determinant'] > 0
                  and trial['raw_sse'] < state['raw_sse'])
            record['trials'].append(dict(alpha=alpha, accepted=ok, **summary(trial)))
            if ok:
                coefficients += alpha*step
                lm = max(lm/3, 1.e-10); accepted = True; break
        if not accepted:
            lm *= 10
        record['elapsed_seconds'] = time.monotonic()-started
        records.append(record)
        print(json.dumps(record), flush=True)
        a.out.with_suffix('.progress.json').write_text(json.dumps(dict(
            source_sha256=source, input_sha256=sha(a.bundle),
            scope='Running full coarse three-jet subspace, no accepted metric claim',
            coefficients=coefficients.tolist(), records=records), indent=2)+'\n')
    jets, height = b.candidate(arrays['qjets'], float(arrays['Hcap']), coefficients)
    candidate, affine1 = o.pack(jets, height, require_affine=True)
    final = b.evaluate(o._base_first, o._base_p.rho, coefficients)
    raw = o.raw_residual(candidate)
    ss, cross, pp = raw[...,0], raw[...,1], raw[...,2]
    native = dict(raw_sse=float(np.sum((ss*ss+2*cross*cross+pp*pp)*b.multiplicity[None,:])),
                  sampled_max_gram=float(np.max((abs(ss+pp)+np.sqrt((ss-pp)**2+4*cross*cross))/2)),
                  sampled_min_determinant=float(np.min((1+ss)*(1+pp)-cross*cross)))
    difference = abs(native['raw_sse']-final['raw_sse'])/max(1., native['raw_sse'])
    if difference > 1.e-9:
        raise ValueError('Subspace/actual-field discrepancy: '+repr(difference))
    arrays['qjets'] = jets; arrays['Hcap'] = np.asarray(height)
    output = a.out.with_suffix('.npz')
    np.savez_compressed(output, **arrays)
    report = dict(schema='fullclosed-physical-three-jet-subspace-v2', status=status,
                  source_sha256=source, base_source_sha256=sha(a.base_source),
                  batch_source_sha256=sha(a.batch_source), operator_sha256=sha(a.operator),
                  input_sha256=sha(a.bundle), output_bundle_sha256=sha(output),
                  full_variables=o.free_size, full_rows=o.P*o.full_N*3,
                  packed_rows=o.P*o.N*3, quarter_with_exact_multiplicity=True,
                  low_modes=a.low_modes, subspace_dimension=b.dimension,
                  centers=[float(o.mesh[i]) for i in b.center_nodes],
                  radial_names=b.radial_names, channels=b.channels,
                  pairs=b.pairs.tolist(), coefficients=coefficients.tolist(),
                  initial=first, final=summary(final), native_final=native,
                  native_sse_relative_difference=difference,
                  initial_height=float(bundle['Hcap']), final_height=height,
                  exact_core_curve_unchanged=True, all_original_residual_rows_retained=True,
                  fixed_scalar_and_mesh_unchanged=True, affine_initial=affine0,
                  affine_final=affine1, cache=cache, iterations=records,
                  sample_metric_accepted=native['sampled_max_gram']<=1.e-6,
                  continuous_metric_certified=False, exact_solution_claimed=False,
                  reach_certified=False, held_certified=False,
                  elapsed_seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()
                      if k not in ('iterations','pairs','coefficients','cache')}), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle','operator','batch-source','out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--base-source', '--basis-source', dest='base_source', type=Path,
                   default=Path(__file__).with_name('resume_20261120_physical_subspace.py'))
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--low-modes', type=int, default=3)
    p.add_argument('--steps', type=int, default=6)
    p.add_argument('--backtracks', type=int, default=8)
    p.add_argument('--damping', type=float, default=1.e-3)
    p.add_argument('--seconds', type=float, default=600.)
    main(p.parse_args())
