#!/usr/bin/env python3
"""Small physical C2 subspace in the complete fixed-Hold Gram problem.

This is an optional warm improvement, not a replacement for the full model.
It preserves every angular/stage residual, the fixed scalar, the original
core curve, and the exact affine end conditions.  Raw outputs stay outside
the repository.  No runtime action occurs on import.
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
    name = 'physical_subspace_dependency_' + sha(path)[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def smoothstep_jets(t, width):
    u = np.asarray(t) / width
    return np.stack((u**3 * (10 + u * (-15 + 6*u)),
                     30*u**2*(1-u)**2/width,
                     60*u*(1-u)*(1-2*u)/width**2), axis=-1)


class PhysicalSubspace:
    """Literal nodal corrections plus their exact shared-quintic stages.

    Each compact radial hat uses two quintics, with flat 2-jets at
    its two ends and at its peak.  Knots are existing model nodes.
    A global quintic height direction changes H simultaneously, so its
    physical derivative has no isolated chi'/width spike.
    """

    def __init__(self, operator, low_modes=3,
                 desired_centers=(.60, 1.05, 1.35, 1.75, 2.15)):
        o = self.o = operator
        if not 0 <= low_modes <= o.M:
            raise ValueError('Invalid low angular cutoff')
        self.channels = [('R', 0, 0), ('Z', 0, 2*o.M+1)]
        for m in range(1, low_modes+1):
            self.channels += [('R', m, m), ('T', m, o.M+m),
                              ('Z', m, 2*o.M+1+m)]
        self.nc = len(self.channels)
        ids = sorted(set(int(np.argmin(abs(o.mesh-s)))
                         for s in desired_centers if 0 < s < o.S))
        if not ids or ids[0] == 0 or ids[-1] == o.J-1:
            raise ValueError('Need distinct interior radial centers')
        self.center_nodes = ids
        breaks = [0] + ids + [o.J-1]
        self.radial_names = []
        nodal = []
        for k, mid in enumerate(ids):
            left, right = breaks[k], breaks[k+2]
            b = np.zeros((o.J, 3))
            b[left:mid+1] = smoothstep_jets(
                o.mesh[left:mid+1]-o.mesh[left], o.mesh[mid]-o.mesh[left])
            fall = smoothstep_jets(o.mesh[mid:right+1]-o.mesh[mid],
                                   o.mesh[right]-o.mesh[mid])
            fall[:, 0] = 1-fall[:, 0]
            fall[:, 1:] *= -1
            b[mid:right+1] = fall
            b[left] = 0.; b[mid] = [1., 0., 0.]; b[right] = 0.
            nodal.append(b)
            self.radial_names.append('hat_at_' + repr(float(o.mesh[mid])))
        self.bump_count = len(nodal)
        # This degree-five function may change A0_XY, which is a free
        # variable of the original complete model.  It does not change
        # core position/velocity and has zero terminal two-jet.
        u = o.mesh/o.S
        c = np.stack((u*u*(1-u)**3,
                      (2*u-9*u*u+12*u**3-5*u**4)/o.S,
                      (2-18*u+36*u*u-20*u**3)/o.S**2), axis=-1)
        c[0] = [0., 0., 2/o.S**2]; c[-1] = 0.
        self.core_radial = len(nodal)
        nodal.append(c); self.radial_names.append('global_core_second_jet')
        # H -> H+1 together with q_Z -> q_Z+B-chi.  The stored
        # polynomial, not an unrecorded analytic surrogate, is used.
        b = smoothstep_jets(o.mesh, o.S)
        chi = np.array([o._lift_scalar(float(s))[:3] for s in o.mesh])
        h = b-chi
        h[0] = 0.; h[-1] = 0.
        self.height_radial = len(nodal)
        nodal.append(h); self.radial_names.append('global_height_with_cap')
        self.node_jets = np.array(nodal)
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
        self.pairs = [(k, j) for k in range(self.bump_count)
                      for j in range(self.nc)]
        self.pairs += [(self.core_radial, j)
                       for j, channel in enumerate(self.channels)
                       if channel[0] != 'Z']
        self.pairs += [(self.height_radial, 1)]
        self.pairs = np.asarray(self.pairs, dtype=int)
        self.dimension = len(self.pairs)
        self.sqrt_multiplicity = np.array(getattr(o, 'sqrt_multiplicity',
                                                 np.ones(o.N)), copy=True)
        self.multiplicity = self.sqrt_multiplicity**2
        self.h = np.zeros((o.N, self.nc, 3))
        self.dh = np.zeros_like(self.h)
        for j, (kind, m, _) in enumerate(self.channels):
            nu = 2*m
            co, si = np.cos(nu*o.phi), np.sin(nu*o.phi)
            if kind == 'R':
                self.h[:, j, 0] = co
                self.dh[:, j, 0] = -nu*si
                self.dh[:, j, 1] = co
            elif kind == 'T':
                self.h[:, j, 1] = si
                self.dh[:, j, 0] = -si
                self.dh[:, j, 1] = nu*co
            else:
                self.h[:, j, 2] = co
                self.dh[:, j, 2] = -nu*si

    def coefficient_matrix(self, coefficients):
        c = np.zeros((self.nb, self.nc))
        c[self.pairs[:, 0], self.pairs[:, 1]] = coefficients
        return c

    def candidate(self, base_jets, base_height, coefficients):
        c = self.coefficient_matrix(coefficients)
        result = base_jets.copy()
        for k in range(self.nb):
            for j, (_, _, slot) in enumerate(self.channels):
                if c[k, j]:
                    result[:, :, slot] += c[k, j]*self.node_jets[k]
        return result, float(base_height + coefficients[-1])

    def evaluate(self, base_first, rho, coefficients, *, linearize=False):
        """Use all original finite rows, with Frobenius weights (1,2,1)."""
        o = self.o
        c = self.coefficient_matrix(coefficients)
        yu, yy = self.stage_u @ c, self.stage_y @ c
        gram = np.zeros((self.dimension, self.dimension)) if linearize else None
        gradient = np.zeros(self.dimension) if linearize else None
        cost = 0.; maximum = 0.; determinant = float('inf')
        worst = None
        ri, cj = self.pairs.T
        for stage, a in enumerate(o.a):
            V = base_first[0, stage] + np.einsum('c,nck->nk', yu[stage], self.h)
            d = base_first[1, stage] + np.einsum('c,nck->nk', yy[stage], self.dh)
            ar = a*rho
            r0 = np.sum(V*V, axis=1)-1.
            r1 = np.sum(V*d, axis=1)/ar
            r2 = np.sum(d*d, axis=1)/(ar*ar)-1.
            cost += float(self.multiplicity @ (r0*r0+2*r1*r1+r2*r2))
            opnorm = (abs(r0+r2)+np.sqrt((r0-r2)**2+4*r1*r1))/2
            j = int(np.argmax(opnorm))
            if opnorm[j] > maximum:
                maximum = float(opnorm[j])
                worst = [stage, j, float(o.times[stage]), float(o.phi[j])]
            determinant = min(determinant, float(np.min((1+r0)*(1+r2)-r1*r1)))
            if not linearize:
                continue
            bv, bu = self.stage_y[stage, ri], self.stage_u[stage, ri]
            active = np.flatnonzero((bv != 0) | (bu != 0))
            if active.size == 0:
                continue
            channels = cj[active]
            v_h = np.einsum('nk,nck->nc', V, self.h)
            d_h = np.einsum('nk,nck->nc', d, self.h)
            v_dh = np.einsum('nk,nck->nc', V, self.dh)
            d_dh = np.einsum('nk,nck->nc', d, self.dh)
            j0 = 2*v_h[:, channels]*bu[active]
            j1 = (d_h[:, channels]*bu[active] + v_dh[:, channels]*bv[active])/ar[:, None]
            j2 = 2*d_dh[:, channels]*bv[active]/(ar*ar)[:, None]
            j0 *= self.sqrt_multiplicity[:, None]
            j1 *= self.sqrt_multiplicity[:, None]
            j2 *= self.sqrt_multiplicity[:, None]
            gram[np.ix_(active, active)] += j0.T@j0 + 2*(j1.T@j1) + j2.T@j2
            gradient[active] += (j0.T@(r0*self.sqrt_multiplicity) +
                                 2*(j1.T@(r1*self.sqrt_multiplicity)) +
                                 j2.T@(r2*self.sqrt_multiplicity))
        return dict(raw_sse=cost, sampled_max_gram=maximum,
                    sampled_min_determinant=determinant, worst=worst,
                    normal_matrix=gram, gradient=gradient)


def summary(result):
    return {k:v for k,v in result.items() if k not in ('normal_matrix','gradient')}


def main(args):
    started = time.monotonic()
    source = sha(__file__)
    if args.out.exists() or args.out.with_suffix('.npz').exists():
        raise FileExistsError('Choose a fresh output path')
    bundle = np.load(args.bundle, allow_pickle=False)
    arrays = {k:np.array(bundle[k], copy=True) for k in bundle.files}
    fft = load(args.fft_source)
    extra = dict(quarter=True, stage_block=64) if args.quarter else {}
    o = fft.create(args.operator, arrays['mesh'], arrays['a_stages'],
                   float(arrays['radius']), arrays['fixed_core_first3'],
                   M=(arrays['qjets'].shape[2]-2)//3, N=args.angles,
                   width=float(arrays['width']), **extra)
    x0, affine = o.pack(arrays['qjets'], float(arrays['Hcap']), require_affine=True)
    cache = o.set_base(x0)
    b = PhysicalSubspace(o, low_modes=args.low_modes)
    coefficients = np.zeros(b.dimension)
    lm = args.damping
    records = []
    first = None
    status = 'iteration_budget'
    for iteration in range(args.steps):
        if time.monotonic()-started > args.seconds:
            status = 'time_budget'; break
        state = b.evaluate(o._base_first, o._base_p.rho, coefficients, linearize=True)
        if first is None:
            first = summary(state)
        A, g = state['normal_matrix'], state['gradient']
        scale = np.sqrt(np.maximum(np.diag(A), np.max(np.diag(A))*1.e-28))
        normalized = A/scale[:,None]/scale[None,:]
        step = np.linalg.solve(normalized+lm*np.eye(b.dimension), -g/scale)/scale
        attempt = dict(iteration=iteration, before=summary(state), damping=lm,
                       direction_norm=float(np.linalg.norm(step)), trials=[])
        accepted = False
        for j in range(args.backtracks):
            alpha = 2.**(-j)
            trial = b.evaluate(o._base_first, o._base_p.rho, coefficients+alpha*step)
            ok = (np.isfinite(trial['raw_sse']) and
                  trial['sampled_min_determinant'] > 0 and
                  trial['raw_sse'] < state['raw_sse'])
            attempt['trials'].append(dict(alpha=alpha, accepted=ok, **summary(trial)))
            if ok:
                coefficients += alpha*step
                lm = max(lm/3, 1.e-10)
                accepted = True
                break
        if not accepted:
            lm *= 10
        attempt['elapsed_seconds'] = time.monotonic()-started
        records.append(attempt)
        print(json.dumps(attempt), flush=True)
        args.out.with_suffix('.progress.json').write_text(json.dumps(dict(
            scope='Running optional physical subspace, not accepted full solution',
            input_sha256=sha(args.bundle), source_sha256=source,
            coefficients=coefficients.tolist(), records=records), indent=2)+'\n')
    jets, height = b.candidate(arrays['qjets'], float(arrays['Hcap']), coefficients)
    candidate, affine_final = o.pack(jets, height, require_affine=True)
    final = b.evaluate(o._base_first, o._base_p.rho, coefficients)
    # This is the actual original operator at the resulting new free
    # vector, not a second implementation on an invented fixture.
    raw = o.raw_residual(candidate) if hasattr(o, 'raw_residual') else o.residual(candidate)
    ss, cross, pp = raw[...,0], raw[...,1], raw[...,2]
    native = dict(raw_sse=float(np.sum((ss*ss+2*cross*cross+pp*pp)*b.multiplicity[None,:])),
                  sampled_max_gram=float(np.max((abs(ss+pp)+np.sqrt((ss-pp)**2+4*cross*cross))/2)),
                  sampled_min_determinant=float(np.min((1+ss)*(1+pp)-cross*cross)))
    denominator = max(1., native['raw_sse'])
    difference = abs(native['raw_sse']-final['raw_sse'])/denominator
    if difference > 1.e-9:
        raise ValueError('Physical subspace and actual operator disagree: '+repr(difference))
    arrays['qjets'] = jets
    arrays['Hcap'] = np.asarray(height)
    output_bundle = args.out.with_suffix('.npz')
    np.savez_compressed(output_bundle, **arrays)
    report = dict(schema='fullclosed-physical-subspace-v1', status=status,
                  source_sha256=source, input_sha256=sha(args.bundle),
                  operator_sha256=sha(args.operator), fft_source_sha256=sha(args.fft_source),
                  full_variables=o.free_size,
                  full_rows=o.P*getattr(o, 'full_N', o.N)*3,
                  packed_rows=o.P*o.N*3, quarter_with_exact_multiplicity=args.quarter,
                  low_modes=args.low_modes, subspace_dimension=b.dimension,
                  centers=[float(o.mesh[i]) for i in b.center_nodes],
                  radial_names=b.radial_names, channels=b.channels,
                  pairs=b.pairs.tolist(), coefficients=coefficients.tolist(),
                  initial=first, final=summary(final), native_final=native,
                  native_sse_relative_difference=difference,
                  initial_height=float(bundle['Hcap']), final_height=height,
                  exact_core_curve_unchanged=True, all_original_residual_rows_retained=True,
                  fixed_scalar_and_mesh_unchanged=True, affine_initial=affine,
                  affine_final=affine_final, cache=cache, iterations=records,
                  output_bundle_sha256=sha(output_bundle),
                  sample_metric_accepted=native['sampled_max_gram']<=1.e-6,
                  continuous_metric_certified=False, exact_solution_claimed=False,
                  reach_certified=False, held_certified=False,
                  elapsed_seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()
                      if k not in ('iterations','pairs','coefficients','cache')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle','operator','fft-source','out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--quarter', action='store_true')
    parser.add_argument('--low-modes', type=int, default=3)
    parser.add_argument('--steps', type=int, default=6)
    parser.add_argument('--backtracks', type=int, default=8)
    parser.add_argument('--damping', type=float, default=1.e-3)
    parser.add_argument('--seconds', type=float, default=600.)
    main(parser.parse_args())
