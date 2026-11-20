#!/usr/bin/env python3
"""Physical coarse Gram SQP with actual sampled curvature/diameter screening.

Every original Gram row is retained.  The correction space is the existing
complete coarse three-jet space.  Active principal-curvature and radius
derivatives constrain its GN direction.  Acceptance always reads the actual
full node/midpoint Gram and the actual full point curvature and radius.
The necessary point screen is not a continuous reach certificate.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import cho_factor, cho_solve, eigh
from scipy.optimize import minimize


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    name = 'curvature_qp_dependency_' + sha(path)[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def synth_batch(o, values):
    M = o.M
    cosine = o._trig_values(np.stack((values[:, :M+1], values[:, 2*M+1:]), axis=1), 'cos')
    sine = o._trig_values(values[:, M+1:2*M+1], 'sin')
    result = np.empty((len(values), o.N, 3), dtype=values.dtype)
    result[:, :, 0], result[:, :, 1], result[:, :, 2] = cosine[:, 0], sine, cosine[:, 1]
    return result


def angular_second_coefficients(o, values):
    M, nu = o.M, o.freq
    result = np.zeros_like(values)
    result[:, 0] = -values[:, 0]
    r, t = values[:, 1:M+1], values[:, M+1:2*M+1]
    result[:, 1:M+1] = -(1+nu*nu)*r-2*nu*t
    result[:, M+1:2*M+1] = -(1+nu*nu)*t-2*nu*r
    result[:, 2*M+2:] = -nu*nu*values[:, 2*M+2:]
    return result


def fields_block(o, p, start, stop):
    y, u = o._stage_pair(p.jets, start, stop)
    stages = np.arange(start, stop)
    acc = p.jets[stages//2, 2].copy()
    odd = (stages % 2).astype(bool)
    if np.any(odd):
        cells = stages[odd]//2
        endpoints = np.stack((p.jets[cells], p.jets[cells+1]), axis=1).reshape(-1, 6, o.n)
        acc[odd] = np.einsum('bc,bcn->bn', o._mid_weights_array[cells, 2], endpoints)
    chi, cp, cpp, f, fp, fpp = o.lift_scalar[start:stop].T
    V, d = o._first_batch(p, start, stop)
    F = synth_batch(o, y)+f[:, None, None]*p.er[None]
    F[:, :, 2] += chi[:, None]*p.height
    ss, sp = o._linear_fields(u, acc)
    ss += fpp[:, None, None]*p.er[None]
    ss[:, :, 2] += cpp[:, None]*p.height
    sp += fp[:, None, None]*(p.rho[:, None]*p.et)[None]
    pp = synth_batch(o, angular_second_coefficients(o, y))
    pp += f[:, None, None]*(p.rho_phi[:, None]*p.et-p.rho[:, None]**2*p.er)[None]
    return dict(F=F, Fs=V, Fphi=d, Fss=ss, Fsphi=sp, Fphiphi=pp)


def pick_extremes(values, count, *, branches=False):
    flat = np.abs(values).ravel()
    take = min(len(flat), max(count*80, count))
    indices = np.argpartition(flat, len(flat)-take)[-take:]
    indices = indices[np.argsort(flat[indices])[::-1]]
    selected = []
    for index in indices:
        loc = tuple(int(v) for v in np.unravel_index(index, values.shape))
        if any(abs(loc[0]-old[0]) <= 2 and abs(loc[1]-old[1]) <= 8
               and (not branches or loc[2] == old[2]) for old in selected):
            continue
        selected.append(loc)
        if len(selected) == count:
            break
    if not selected:
        raise ValueError('No geometric sample')
    return selected


def scan_geometry(o, x, *, top_curvature=32, top_radius=4):
    p = o.prepare(x)
    kappas = np.empty((o.P, o.N, 2))
    radii = np.empty((o.P, o.N))
    minimum_area = float('inf')
    for start in range(0, o.P, o.stage_block):
        stop = min(start+o.stage_block, o.P)
        z = fields_block(o, p, start, stop)
        V, d = z['Fs'], z['Fphi']
        cross = np.cross(V, d)
        area = np.sqrt(np.sum(cross*cross, axis=2))
        minimum_area = min(minimum_area, float(np.min(area)))
        if np.any(area <= 0) or not np.isfinite(area).all():
            return dict(complete=False, min_area=minimum_area, first_invalid_stage=start), [], []
        normal = cross/area[:, :, None]
        E, F, G = np.sum(V*V, axis=2), np.sum(V*d, axis=2), np.sum(d*d, axis=2)
        e = np.sum(normal*z['Fss'], axis=2)
        f = np.sum(normal*z['Fsphi'], axis=2)
        g = np.sum(normal*z['Fphiphi'], axis=2)
        determinant = area*area
        trace = (e*G+g*E-2*f*F)/determinant
        gauss = (e*g-f*f)/determinant
        gap = np.sqrt(np.maximum(0., trace*trace-4*gauss))
        kappas[start:stop, :, 0] = (trace-gap)/2
        kappas[start:stop, :, 1] = (trace+gap)/2
        radii[start:stop] = np.sqrt(np.sum(z['F']*z['F'], axis=2))
    curvature_locations = pick_extremes(kappas, top_curvature, branches=True)
    radius_locations = pick_extremes(radii, top_radius)
    worst = tuple(int(v) for v in np.unravel_index(np.argmax(np.abs(kappas)), kappas.shape))
    farthest = tuple(int(v) for v in np.unravel_index(np.argmax(radii), radii.shape))
    K = float(abs(kappas[worst]))
    radius = float(radii[farthest])
    diameter = max(2., 2*abs(float(p.height)), 2*radius)
    summary = dict(complete=True, maximum_absolute_principal_curvature=K,
                   diameter_point_lower=diameter, maximum_radius=radius,
                   necessary_reach_product=.03*diameter*K, min_area=minimum_area,
                   worst=dict(stage=worst[0], angle=worst[1], branch=worst[2],
                              s=float(o.times[worst[0]]), phi=float(o.phi[worst[1]])),
                   farthest=dict(stage=farthest[0], angle=farthest[1],
                                 s=float(o.times[farthest[0]]), phi=float(o.phi[farthest[1]])),
                   point_count=o.P*o.N, continuous_geometry_certified=False)
    return summary, curvature_locations, radius_locations


def single_fields(o, p, stage, angle):
    return {name:values[angle].copy() for name, values in o.six_jets(p, stage).items()}


def analytic_kappa(z, branch):
    """Bilinear analytic branch, also suitable for complex-step checking."""
    V, d = z['Fs'], z['Fphi']
    cross = np.cross(V, d)
    area = np.sqrt(np.sum(cross*cross))
    n = cross/area
    E, F, G = np.sum(V*V), np.sum(V*d), np.sum(d*d)
    e, f, g = np.sum(n*z['Fss']), np.sum(n*z['Fsphi']), np.sum(n*z['Fphiphi'])
    trace = (e*G+g*E-2*f*F)/(area*area)
    gauss = (e*g-f*f)/(area*area)
    gap = np.sqrt(trace*trace-4*gauss)
    return (trace+(-1 if branch == 0 else 1)*gap)/2


def curvature_cotangent(z, branch):
    """Derivative of one simple generalized principal-curvature eigenvalue."""
    V, d = z['Fs'], z['Fphi']
    cross = np.cross(V, d)
    area = float(np.linalg.norm(cross))
    n = cross/area
    I = np.array([[V@V, V@d], [V@d, d@d]])
    II = np.array([[n@z['Fss'], n@z['Fsphi']], [n@z['Fsphi'], n@z['Fphiphi']]])
    values, vectors = eigh(II, I, check_finite=True)
    kappa = float(values[branch])
    v1, v2 = vectors[:, branch]
    t = v1*V+v2*d
    w = v1*v1*z['Fss']+2*v1*v2*z['Fsphi']+v2*v2*z['Fphiphi']
    a = (w-kappa*n)/area
    cotangent = dict(F=np.zeros(3),
        Fs=np.cross(d, a)-2*kappa*v1*t,
        Fphi=np.cross(a, V)-2*kappa*v2*t,
        Fss=v1*v1*n, Fsphi=2*v1*v2*n, Fphiphi=v2*v2*n)
    return kappa, cotangent, dict(principal_gap=float(values[1]-values[0]),
                                 unit_tangent_squared=float(t@t))


class CoarseGeometry:
    def __init__(self, operator, basis):
        self.o, self.b = operator, basis
        o, b = operator, basis
        self.stage_a = np.empty_like(b.stage_y)
        for k, jets in enumerate(b.node_jets):
            self.stage_a[::2, k] = jets[:, 2]
            for i, weights in enumerate(o.mid_weights):
                self.stage_a[2*i+1, k] = weights[2]@jets[i:i+2].ravel()
        self.stage_a[:, b.height_radial] += o.lift_scalar[:, 2]
        self.d2h = np.zeros_like(b.h)
        for j, (kind, m, _) in enumerate(b.channels):
            nu = 2*m
            co, si = np.cos(nu*o.phi), np.sin(nu*o.phi)
            if kind == 'R':
                self.d2h[:, j, 0], self.d2h[:, j, 1] = -(nu*nu+1)*co, -2*nu*si
            elif kind == 'T':
                self.d2h[:, j, 0], self.d2h[:, j, 1] = -2*nu*co, -(nu*nu+1)*si
            else:
                self.d2h[:, j, 2] = -nu*nu*co

    def row(self, stage, angle, cotangent):
        b = self.b
        ri, cj = b.pairs.T
        h, dh, d2h = b.h[angle], b.dh[angle], self.d2h[angle]
        a = h@cotangent['Fss']
        u = h@cotangent['Fs']+dh@cotangent['Fsphi']
        y = h@cotangent['F']+dh@cotangent['Fphi']+d2h@cotangent['Fphiphi']
        return self.stage_a[stage, ri]*a[cj]+b.stage_u[stage, ri]*u[cj]+b.stage_y[stage, ri]*y[cj]

    def constraints(self, x, curvature_locations, radius_locations, reach_ratio, safety):
        o, b = self.o, self.b
        p = o.prepare(x)
        curvature, radii = [], []
        for stage, angle, branch in curvature_locations:
            z = single_fields(o, p, stage, angle)
            k, cot, meta = curvature_cotangent(z, branch)
            curvature.append((k, self.row(stage, angle, cot), (stage, angle, branch), meta))
        for stage, angle in radius_locations:
            z = single_fields(o, p, stage, angle)
            radius = float(np.linalg.norm(z['F']))
            cot = {name:np.zeros(3) for name in z}
            cot['F'] = 2*z['F']/radius
            radii.append((2*radius, self.row(stage, angle, cot), (stage, angle)))
        # Explicit fixed core and cap-height diameter lower bounds are
        # also included, even if a sampled body radius currently dominates.
        radii.append((2., np.zeros(b.dimension), ('fixed_core',)))
        height_row = np.zeros(b.dimension)
        height_row[-1] = 2*np.sign(float(p.height))
        radii.append((2*abs(float(p.height)), height_row, ('cap_height',)))
        rows, bounds, metadata = [], [], []
        for k, dk, loc, meta in curvature:
            for D, dD, dloc in radii:
                rows.append(reach_ratio*(D*np.sign(k)*dk+abs(k)*dD))
                bounds.append(safety-reach_ratio*D*abs(k))
                metadata.append(dict(curvature_point=loc, diameter_point=dloc,
                                     curvature=k, diameter_lower=D, **meta))
        return np.asarray(rows), np.asarray(bounds), metadata


def derivative_probe(o, x, basis, geometry, location):
    p = o.prepare(x)
    stage, angle, branch = location
    z = single_fields(o, p, stage, angle)
    k, cot, metadata = curvature_cotangent(z, branch)
    if metadata['principal_gap'] <= 1.e-8:
        raise ValueError('Probe requires a simple principal branch')
    rng = np.random.default_rng(20261120)
    perturb = {name:rng.normal(size=3) for name in z}
    step = 1.e-25
    predicted = sum(cot[name]@perturb[name] for name in z)
    cs = analytic_kappa({name:z[name]+1j*step*perturb[name] for name in z}, branch).imag/step
    local_error = abs(cs-predicted)/max(1., abs(cs), abs(predicted))
    coefficients = rng.normal(size=basis.dimension)
    row = geometry.row(stage, angle, cot)
    free = basis.free_direction(coefficients)
    pc = o.prepare(x.astype(complex)+1j*step*free)
    zc = single_fields(o, pc, stage, angle)
    cs_coarse = analytic_kappa(zc, branch).imag/step
    coarse_predicted = row@coefficients
    coarse_error = abs(cs_coarse-coarse_predicted)/max(1., abs(cs_coarse), abs(coarse_predicted))
    cotD = {name:np.zeros(3) for name in z}
    cotD['F'] = 2*z['F']/np.linalg.norm(z['F'])
    diameter_predicted = geometry.row(stage, angle, cotD)@coefficients
    diameter_cs = (2*np.sqrt(np.sum(zc['F']*zc['F']))).imag/step
    diameter_error = abs(diameter_cs-diameter_predicted)/max(1., abs(diameter_cs), abs(diameter_predicted))
    report = dict(stage=stage, angle=angle, branch=branch, kappa=k,
                  local_sixjet_relative_error=float(local_error),
                  full_coarse_curvature_relative_error=float(coarse_error),
                  full_coarse_diameter_relative_error=float(diameter_error),
                  complex_step=step, **metadata)
    if max(local_error, coarse_error, diameter_error) > 2.e-9:
        raise ValueError('Curvature/diameter derivative probe failed: '+repr(report))
    return report


def constrained_direction(normal, gradient, Q, bounds, damping):
    scale = np.sqrt(np.maximum(np.diag(normal), np.max(np.diag(normal))*1.e-28))
    C = normal/scale[:, None]/scale[None, :]+damping*np.eye(len(scale))
    factor = cho_factor(C, lower=True, check_finite=False)
    z0 = cho_solve(factor, -gradient/scale, check_finite=False)
    rows = Q/scale[None, :]
    rownorm = np.linalg.norm(rows, axis=1)
    if np.any((rownorm <= 1.e-30) & (bounds < -1.e-12)):
        raise ValueError('Already infeasible constant curvature constraint')
    keep = rownorm > 1.e-30
    rows = rows[keep]/rownorm[keep, None]
    rhs = bounds[keep]/rownorm[keep]
    inverse_rows = cho_solve(factor, rows.T, check_finite=False)
    dual_normal = rows@inverse_rows
    dual_normal = (dual_normal+dual_normal.T)/2
    dual_linear = rhs-rows@z0
    def objective(lam):
        v = dual_normal@lam
        return float(.5*lam@v+dual_linear@lam), v+dual_linear
    result = minimize(objective, np.zeros(len(rhs)), jac=True, method='L-BFGS-B',
                      bounds=[(0., None)]*len(rhs),
                      options=dict(maxiter=1500, ftol=1.e-14, gtol=1.e-10, maxls=50))
    z = z0-inverse_rows@result.x
    violation = float(np.max(rows@z-rhs)) if len(rhs) else 0.
    # Inexact dual termination may leave a tiny positive row violation.
    # A radial contraction towards the feasible zero direction repairs it
    # explicitly; this does not change the nonlinear acceptance criteria.
    contraction = 1.
    actual_rows = Q@(z/scale)
    for value, bound in zip(actual_rows, bounds):
        if value > bound and value > 0:
            contraction = min(contraction, max(0., bound/value))
    if contraction < 1:
        z *= max(0., contraction*(1-1.e-10))
    direction = z/scale
    metadata = dict(dual_success=bool(result.success), dual_message=str(result.message),
                    dual_iterations=int(result.nit), constraints=len(bounds),
                    nonzero_dual=int(np.sum(result.x > 1.e-9)),
                    scaled_max_violation_before_repair=violation,
                    contraction=contraction,
                    maximum_primal_violation=float(np.max(Q@direction-bounds)),
                    original_gradient_dot_direction=float(gradient@direction),
                    step_norm=float(np.linalg.norm(direction)), damping=damping)
    return direction, metadata


def gram_stats(o, x):
    raw = o.raw_residual(x)
    e, f, g = raw[..., 0], raw[..., 1], raw[..., 2]
    norms = (np.abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2
    return dict(raw_sse=float(np.sum(o.multiplicity[None, :]*(e*e+2*f*f+g*g))),
                max_gram=float(np.max(norms)),
                min_determinant=float(np.min((1+e)*(1+g)-f*f)))


def main(args):
    started = time.monotonic()
    if args.out.exists() or args.out.with_suffix('.npz').exists():
        raise FileExistsError('Use a fresh output path')
    data = np.load(args.bundle, allow_pickle=False)
    batch, coarse = load(args.batch_source), load(args.coarse_source)
    o = batch.create(args.operator, data['mesh'], data['a_stages'], float(data['radius']),
                     data['fixed_core_first3'], M=(data['qjets'].shape[-1]-2)//3,
                     N=args.angles, width=float(data['width']), quarter=True,
                     stage_block=args.stage_block)
    x, affine = o.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    centers = [float(v) for v in args.centers.split(',')]
    basis = coarse.make_space(args.base_source, o, low_modes=args.low_modes, desired_centers=centers)
    geometry = CoarseGeometry(o, basis)
    o.set_base(x)
    initial_geometry, curvatures, radii = scan_geometry(o, x, top_curvature=args.top_curvature, top_radius=args.top_radius)
    if (not initial_geometry['complete'] or
            args.reach_ratio*initial_geometry['diameter_point_lower']*
            initial_geometry['maximum_absolute_principal_curvature'] > args.safety):
        raise ValueError('Input fails the declared necessary sampled screen')
    probe = derivative_probe(o, x, basis, geometry, curvatures[0])
    initial = state = gram_stats(o, x)
    current_geometry = initial_geometry
    records, damping, status = [], args.damping, 'iteration_budget'
    for iteration in range(args.steps):
        if time.monotonic()-started > args.seconds:
            status = 'time_budget'; break
        o.set_base(x)
        linear = basis.evaluate(o._base_first, o._base_p.rho, np.zeros(basis.dimension), linearize=True)
        Q, bounds, active = geometry.constraints(x, curvatures, radii, args.reach_ratio, args.safety)
        direction, qp = constrained_direction(linear['normal_matrix'], linear['gradient'], Q, bounds, damping)
        free = basis.free_direction(direction)
        record = dict(iteration=iteration, before=state, geometry_before=current_geometry,
                      qp=qp, active_constraints=active, trials=[])
        accepted = False
        for k in range(args.backtracks):
            alpha = 2.**(-k)
            candidate = x+alpha*free
            trial = gram_stats(o, candidate)
            item = dict(alpha=alpha, statistics=trial, accepted=False)
            if np.isfinite(trial['raw_sse']) and trial['raw_sse'] < state['raw_sse'] and trial['min_determinant'] > 0:
                checked, cpoints, rpoints = scan_geometry(o, candidate, top_curvature=args.top_curvature, top_radius=args.top_radius)
                product = (args.reach_ratio*checked.get('diameter_point_lower', float('inf'))*
                           checked.get('maximum_absolute_principal_curvature', float('inf')))
                item.update(geometry=checked, necessary_product=product)
                if checked['complete'] and product <= args.safety:
                    x, state, current_geometry = candidate, trial, checked
                    curvatures, radii = cpoints, rpoints
                    item['accepted'] = True
                    accepted = True
            record['trials'].append(item)
            if accepted:
                break
        damping = max(damping/2, 1.e-8) if accepted else damping*10
        record.update(accepted=accepted, elapsed_seconds=time.monotonic()-started)
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k != 'active_constraints'}), flush=True)
        args.out.with_suffix('.progress.json').write_text(json.dumps(dict(
            source_sha256=sha(__file__), input_sha256=sha(args.bundle),
            initial=initial, derivative_probe=probe, current=state,
            geometry=current_geometry, records=records), indent=2)+'\n')
    jets, height, _ = o.unpack(x)
    _, final_affine = o.pack(jets, height, require_affine=True)
    keys = ('mesh','a_stages','radius','width','fixed_core_first3',
            'a_stage_absolute_error','stage_time_absolute_error')
    arrays = {k:np.array(data[k], copy=True) for k in keys if k in data.files}
    arrays.update(qjets=jets, Hcap=np.asarray(height))
    output = args.out.with_suffix('.npz')
    np.savez_compressed(output, **arrays)
    report = dict(schema='fullclosed-coarse-curvature-QP-v1', status=status,
                  source_sha256=sha(__file__), input_sha256=sha(args.bundle),
                  output_bundle_sha256=sha(output), operator_sha256=sha(args.operator),
                  batch_source_sha256=sha(args.batch_source), base_source_sha256=sha(args.base_source),
                  coarse_source_sha256=sha(args.coarse_source), subspace_dimension=basis.dimension,
                  low_modes=args.low_modes, centers=[float(o.mesh[i]) for i in basis.center_nodes],
                  full_variables=o.free_size, all_original_gram_rows_retained=True,
                  full_rows=o.P*o.full_N*3, packed_rows=o.P*o.N*3,
                  initial=initial, final=state, initial_geometry=initial_geometry,
                  final_geometry=current_geometry, derivative_probe=probe,
                  reach_ratio=args.reach_ratio, numerical_safety=args.safety,
                  initial_affine=affine, final_affine=final_affine,
                  initial_height=float(data['Hcap']), final_height=float(height),
                  fixed_scalar_mesh_and_core_unchanged=True, iterations=records,
                  elapsed_seconds=time.monotonic()-started,
                  continuous_metric_certified=False, reach_certified=False,
                  held_amplitude_certified=False, exact_solution_claimed=False)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'iterations'}), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle','operator','batch-source','base-source','coarse-source','out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--low-modes', type=int, default=12)
    p.add_argument('--centers', default='.30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26')
    p.add_argument('--top-curvature', type=int, default=32)
    p.add_argument('--top-radius', type=int, default=4)
    p.add_argument('--reach-ratio', type=float, default=.03)
    p.add_argument('--safety', type=float, default=.98)
    p.add_argument('--damping', type=float, default=.001)
    p.add_argument('--steps', type=int, default=6)
    p.add_argument('--backtracks', type=int, default=12)
    p.add_argument('--seconds', type=float, default=900.)
    main(p.parse_args())
