#!/usr/bin/env python3
"""One same-image radial reparameterization trial, with the original a(s).

Fits compact C2 scalar displacement columns using the complete original
mixed Simpson/Gauss finite objective.  Evaluates the actual composition
F_parent(sigma(s),phi), not a quintic resample.  Monotonicity is proved by
exact Fraction Bernstein coefficients of sigma' on every bump piece.
Finite Gram evaluations use the original numerical carriers; this is a
mechanism diagnostic, not a continuous metric certificate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module; spec.loader.exec_module(module)
    return module


class RadialBumps:
    def __init__(self):
        # Broad extension controls plus a few narrow controls around the
        # observed terminal metric basin. All parameters are exact binaries.
        centers = list(np.linspace(1.08, 2.20, 16))+[2.25, 2.275, 2.295, 2.307, 2.313, 2.316]
        widths = [min(.16, c-1., 2.319-c) for c in centers[:16]]+[.065, .043, .023, .011, .0055, .0025]
        self.centers, self.widths = np.array(centers), np.array(widths)
        self.dimension = len(centers)

    def evaluate(self, s):
        x = (np.asarray(s)[:, None]-self.centers)/self.widths
        active = np.abs(x) < 1
        z = np.where(active, 1-x*x, 0.)
        y = z**3
        u = np.where(active, -6*x*z*z/self.widths, 0.)
        acc = np.where(active, (-6+36*x*x-30*x**4)/(self.widths*self.widths), 0.)
        return y, u, acc

    def monotonicity(self, coefficients, S_lower, width):
        """Exact arithmetic proof for the binary map parameters, not samples."""
        centers = [F(float(v)) for v in self.centers]
        widths = [F(float(v)) for v in self.widths]
        coeff = [F(float(v)) for v in coefficients]
        breaks = sorted(set([c-w for c, w in zip(centers, widths)]+[c+w for c, w in zip(centers, widths)]))
        lower, upper, worst = F(1), F(1), None
        for piece, (left, right) in enumerate(zip(breaks, breaks[1:])):
            power = [F(1)]+[F(0)]*5
            midpoint = (left+right)/2
            for c, w, b in zip(centers, widths, coeff):
                if not c-w < midpoint < c+w or b == 0:
                    continue
                x0, dx = (left-c)/w, (right-left)/w
                for degree, multiplier in [(1, -6), (3, 12), (5, -6)]:
                    for k in range(degree+1):
                        power[k] += b*multiplier/w*math.comb(degree, k)*x0**(degree-k)*dx**k
            bernstein = [sum((power[k]*F(math.comb(j, k), math.comb(5, k)) for k in range(j+1)), F(0))
                         for j in range(6)]
            here = min(bernstein)
            if here < lower:
                lower, worst = here, dict(piece=piece, left_exact=str(left), right_exact=str(right))
            upper = max(upper, max(bernstein))
        support_left, support_right = breaks[0], breaks[-1]
        gap = F(S_lower)-F(width)-support_right
        if not support_left > 0 or not gap > 0:
            raise ValueError('The exact map support does not avoid the core or lift breakpoint')
        return dict(strictly_increasing=lower > 0, derivative_lower_exact=str(lower),
            derivative_lower_approximate=float(lower), derivative_upper_exact=str(upper),
            derivative_upper_approximate=float(upper), worst_piece=worst,
            support_left_exact=str(support_left), support_right_exact=str(support_right),
            core_identity_neighborhood_length_exact=str(support_left),
            lift_breakpoint_identity_neighborhood_lower_exact=str(gap),
            all_radial_pieces=len(breaks)-1,
            arithmetic='Exact Fraction coefficients and Bernstein convex hull; no sampled monotonicity',
            same_image_set=bool(lower > 0), identity_at_both_ends_and_near_lift_breakpoint=True)


class Trial:
    def __init__(self, args):
        self.args = args
        self.observed = load('radial_reparameterization_observations', args.observed_source)
        with np.load(args.bundle, allow_pickle=False) as data:
            self.data = {key: np.array(data[key]) for key in data.files}
        with np.load(args.carrier, allow_pickle=False) as data:
            self.carrier = {key: np.array(data[key]) for key in data.files}
        for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
            if not np.array_equal(self.data[key], self.carrier[key]):
                raise ValueError('The original same-g scalar observation carrier differs: '+key)
        d = self.data
        plan = self.observed.ObservationPlan.from_arrays(self.carrier)
        self.o = self.observed.create(args.operator, d['mesh'], d['a_stages'], float(d['radius']),
            d['fixed_core_first3'], batch_source=args.batch_source, observation_plan=plan,
            a_observations=self.carrier['a_observations'], M=(d['qjets'].shape[-1]-2)//3,
            N=args.angles, width=float(d['width']), quarter=True, stage_block=args.stage_block)
        x, self.affine = self.o.pack(d['qjets'], float(d['Hcap']), require_affine=True)
        self.p = self.o.prepare(x)
        self.basis = RadialBumps()
        self.Y, self.U, self.A = self.basis.evaluate(self.o.times)
        self.weights = self.o.mixed_stage_weights(.5)
        report = json.loads(args.node_report.read_text())
        self.S_lower = F(report['scalar']['S']['lower_exact'])

    def parent_fields(self, times):
        """Original quintic and analytic lift at freely moved radial points."""
        o, p = self.o, self.p
        times = np.asarray(times)
        cells = np.clip(np.searchsorted(o.mesh, times, side='right')-1, 0, o.J-2)
        h = o.mesh[cells+1]-o.mesh[cells]
        local = (times-o.mesh[cells])/h
        weights = np.array([self.observed.hermite_weights(hh, uu) for hh, uu in zip(h, local)])
        endpoints = np.stack((p.jets[cells], p.jets[cells+1]), axis=1).reshape((-1, 6, o.n))
        jets = np.einsum('bqc,bcn->bqn', weights, endpoints)
        V, T = o._linear_fields(jets[:, 0], jets[:, 1])
        lift = np.array([o._lift_scalar(float(s)) for s in times])
        V += lift[:, 4, None, None]*p.er[None]
        V[:, :, 2] += lift[:, 1, None]*p.height
        T += lift[:, 3, None, None]*(p.rho[:, None]*p.et)[None]
        return V, T, cells, local

    @staticmethod
    def stats_init():
        return dict(weighted_sse=0., all_raw_sse=0., legacy_raw_sse=0., max_gram=0.,
                    legacy_max_gram=0., added_max_gram=0., min_determinant=float('inf'),
                    component_max=[0., 0., 0.], worst=None)

    def accumulate(self, state, residual, start, moved=None):
        o = self.o; e, f, g = residual[..., 0], residual[..., 1], residual[..., 2]
        point_cost = e*e+2*f*f+g*g
        costs = point_cost@o.multiplicity
        state['weighted_sse'] += float(self.weights[start:start+len(residual)]@costs)
        state['all_raw_sse'] += float(costs.sum())
        count = max(0, min(len(residual), o.legacy_P-start))
        state['legacy_raw_sse'] += float(costs[:count].sum())
        norms = .5*(np.abs(e+g)+np.sqrt((e-g)**2+4*f*f))
        where = np.unravel_index(int(np.argmax(norms)), norms.shape)
        maximum = float(norms[where])
        if maximum > state['max_gram']:
            stage, angle = start+int(where[0]), int(where[1])
            state['max_gram'] = maximum
            state['worst'] = dict(stage=stage, target_s=float(o.times[stage]),
                phi=float(o.phi[angle]), components=residual[where].tolist(),
                parent_s=float(o.times[stage] if moved is None else moved[where[0]]))
        if count:
            state['legacy_max_gram'] = max(state['legacy_max_gram'], float(norms[:count].max()))
        if count < len(residual):
            state['added_max_gram'] = max(state['added_max_gram'], float(norms[count:].max()))
        state['min_determinant'] = min(state['min_determinant'], float(((1+e)*(1+g)-f*f).min()))
        state['component_max'] = [max(state['component_max'][j], float(np.max(np.abs(residual[..., j])))) for j in range(3)]

    def relative(self, V, T, start):
        o, p = self.o, self.p
        ar = o.a[start:start+len(V), None]*p.rho[None]
        return np.stack((o._bdot(V, V)-1, o._bdot(V, T)/ar, o._bdot(T, T)/(ar*ar)-1), axis=-1)

    def baseline_and_direction(self):
        o, p, b = self.o, self.p, self.basis
        state = self.stats_init(); normal = np.zeros((b.dimension, b.dimension)); gradient = np.zeros(b.dimension)
        unrestricted_local_reduction = 0.
        for start in range(0, o.P, o.stage_block):
            stop = min(start+o.stage_block, o.P)
            z = o.physical_jet_batch(p, start, stop)
            V, T, AA, VT = [z[k] for k in ('Fs', 'Fphi', 'Fss', 'Fsphi')]
            residual = self.relative(V, T, start)
            self.accumulate(state, residual, start)
            ar = o.a[start:stop, None]*p.rho[None]
            E, cross = o._bdot(V, V), o._bdot(V, T)
            shift = np.stack((2*o._bdot(V, AA), (o._bdot(AA, T)+o._bdot(V, VT))/ar,
                              2*o._bdot(T, VT)/(ar*ar)), axis=-1)
            stretch = np.stack((2*E, cross/ar, np.zeros_like(E)), axis=-1)
            angular = o.multiplicity[None, :, None]*np.array([1., 2., 1.])[None, None, :]
            reduce = lambda v: np.sum(v*angular, axis=(1, 2))*self.weights[start:stop]
            cc, cd, dd = reduce(shift*shift), reduce(shift*stretch), reduce(stretch*stretch)
            gc, gd = reduce(shift*residual), reduce(stretch*residual)
            Y, U = self.Y[start:stop], self.U[start:stop]
            normal += Y.T@(cc[:, None]*Y)+Y.T@(cd[:, None]*U)+U.T@(cd[:, None]*Y)+U.T@(dd[:, None]*U)
            gradient += Y.T@gc+U.T@gd
            # This upper envelope removes compatibility between xi and xi'.
            # It is diagnostic only, not an attainable map or an acceptance rule.
            for k in range(stop-start):
                matrix = np.array([[cc[k], cd[k]], [cd[k], dd[k]]])
                rhs = np.array([gc[k], gd[k]])
                unrestricted_local_reduction += float(rhs@np.linalg.pinv(matrix, rcond=1e-12)@rhs)
        scale = np.sqrt(np.diag(normal))
        if np.any(scale <= 0): raise ValueError('A proposed radial column has no original observation support')
        scaled = normal/scale[:, None]/scale[None, :]
        vals, vectors = np.linalg.eigh((scaled+scaled.T)/2)
        keep = vals > 1e-12*vals[-1]
        step = -(vectors[:, keep]@((vectors[:, keep].T@(gradient/scale))/vals[keep]))/scale
        predicted = state['weighted_sse']+2*float(gradient@step)+float(step@normal@step)
        state['weighted_mean_sse'] = state['weighted_sse']/(o.full_N*float(self.weights.sum()))
        return state, step, dict(dimension=b.dimension, retained_rank=int(np.count_nonzero(keep)),
            normalized_gram_smallest_eigenvalue=float(vals[0]), normalized_gram_largest_eigenvalue=float(vals[-1]),
            predicted_linear_weighted_sse=predicted,
            predicted_linear_fraction_reduced=(state['weighted_sse']-predicted)/state['weighted_sse'],
            unconstrained_stagewise_shift_stretch_reduction_upper=unrestricted_local_reduction,
            stagewise_note='Independent shift/stretch at every stage ignores derivative compatibility; this is only a linear diagnostic envelope',
            direction_max_abs_coefficient=float(np.max(np.abs(step))),
            derivative_formula='delta E=E_s xi+2E xi_prime; delta F=F_s xi+F xi_prime; delta G=G_s xi',
            fixed_reference_a_composed=False)

    def exact_composition_trial(self, coefficients):
        o = self.o
        displacement = self.Y@coefficients
        speed = 1+self.U@coefficients
        sigma = o.times+displacement
        state = self.stats_init()
        for start in range(0, o.P, o.stage_block):
            stop = min(start+o.stage_block, o.P)
            V, T, _, _ = self.parent_fields(sigma[start:stop])
            V *= speed[start:stop, None, None]
            residual = self.relative(V, T, start)
            self.accumulate(state, residual, start, sigma[start:stop])
        state['weighted_mean_sse'] = state['weighted_sse']/(o.full_N*float(self.weights.sum()))
        state.update(maximum_observed_displacement=float(np.max(np.abs(displacement))),
            minimum_observed_sigma_prime=float(speed.min()), maximum_observed_sigma_prime=float(speed.max()),
            actual_parent_composition_evaluated=True, quintic_resampling_used=False,
            a_evaluated_at_original_target_s=True)
        return state


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle', 'carrier', 'node-report', 'operator', 'batch-source', 'observed-source', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--line-trials', type=int, default=8)
    args = p.parse_args()
    if args.out.exists(): raise FileExistsError('Keep earlier trial results')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic(); trial = Trial(args)
    before, direction, fit = trial.baseline_and_direction()
    print(json.dumps(dict(event='radial_reparameterization_direction', baseline=before, fit=fit)), flush=True)
    report = dict(schema='same-image-radial-reparameterization-first-trial-20261120-v1',
        source_sha256=sha(__file__), parent_sha256=sha(args.bundle), observation_carrier_sha256=sha(args.carrier),
        node_report_sha256=sha(args.node_report), operator_sha256=sha(args.operator),
        batch_sha256=sha(args.batch_source), observed_sha256=sha(args.observed_source),
        full_angles=trial.o.full_N, evaluated_angles=trial.o.N, stages=trial.o.P,
        radial_weights='Original 1/2 legacy Simpson + 1/2 six-Gauss weights',
        radial_weight_sum=float(trial.weights.sum()), all_original_metric_rows_retained=True,
        basis_centers=trial.basis.centers.tolist(), basis_halfwidths=trial.basis.widths.tolist(),
        basis='psi_j(s)=(1-((s-center)/width)^2)^3 on |s-center|<width; zero elsewhere; globally C2',
        parent_affine=trial.affine, before=before, linear_fit=fit, trials=[], accepted_trial=None,
        field_definition='F_new(s,phi)=F_parent(sigma(s),phi), sigma(s)=s+sum b_j psi_j(s)',
        target_a_composed=False, new_quintic_field_claimed=False, continuous_metric_certified=False,
        additional_geometric_certificates_run=False)
    for number in range(args.line_trials):
        alpha = 2.**(-number); coefficients = alpha*direction
        proof = trial.basis.monotonicity(coefficients, trial.S_lower, float(trial.data['width']))
        item = dict(alpha=alpha, coefficients=coefficients.tolist(), monotonicity=proof, accepted=False)
        if proof['strictly_increasing']:
            item['statistics'] = trial.exact_composition_trial(coefficients)
            item['accepted'] = bool(np.isfinite(item['statistics']['weighted_sse']) and
                item['statistics']['weighted_sse'] < before['weighted_sse'])
        report['trials'].append(item)
        print(json.dumps(dict(event='radial_reparameterization_trial', alpha=alpha,
            derivative_lower=proof['derivative_lower_approximate'], accepted=item['accepted'],
            statistics=item.get('statistics'))), flush=True)
        if item['accepted']:
            report['accepted_trial'] = len(report['trials'])-1
            break
    report['elapsed_seconds'] = time.monotonic()-started
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(event='radial_reparameterization_complete', report_sha256=sha(args.out),
        elapsed_seconds=report['elapsed_seconds'], accepted_trial=report['accepted_trial'])), flush=True)


if __name__ == '__main__': main()
