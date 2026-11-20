#!/usr/bin/env python3
"""Curvature QP on every legacy and same-scalar Gauss observation.

The field and its original affine variables are unchanged.  All old rows
are retained; added rows use the supplied same-scalar oracle carriers.
The declared objective is radial L2: a positive 50/50 composite Simpson
and Gauss mixture.  It is NOT the old unweighted raw SSE.  Both old and
extended raw sums remain diagnostic outputs.  Max metric error and all
point curvature/diameter screening remain unweighted.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import MethodType
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    name = 'gauss_curvature_qp_dependency_' + sha(path)[:16]
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


def fields_block_observed(o, p, start, stop):
    """Reusable actual six-jet readout on the supplied observation plan."""
    result = o.physical_jet_batch(p, start, stop)
    y, _ = o._stage_pair(p.jets, start, stop)
    lift = o.lift_scalar[start:stop]
    position = synth_batch(o, y)+lift[:, 3, None, None]*p.er[None]
    position[:, :, 2] += lift[:, 0, None]*p.height
    result['F'] = position
    return result


def retarget_basis(o, basis, native_geometry):
    """Reuse literal nodal basis; rebuild all physical jets at new rows."""
    native = basis.o
    if (native.J != o.J or native.n != o.n or not np.array_equal(native.mesh, o.mesh)
            or not np.array_equal(native.phi, o.phi)):
        raise ValueError('Basis retarget requires the unchanged nodes and angles')
    nodes = np.transpose(basis.node_jets, (1, 2, 0))
    stages = np.empty((o.P, 3, basis.nb))
    for start in range(0, o.P, o.stage_block):
        stop = min(start+o.stage_block, o.P)
        cells = o.observation_cells[start:stop]
        endpoints = np.stack((nodes[cells], nodes[cells+1]), axis=1).reshape(-1, 6, basis.nb)
        stages[start:stop] = np.einsum('bqc,bck->bqk', o.observation_weights[start:stop], endpoints)
    stages[:, :, basis.height_radial] += o.lift_scalar[:, :3]
    basis.o = o
    basis.stage_y, basis.stage_u = stages[:, 0], stages[:, 1]
    native_geometry.o = o
    native_geometry.b = basis
    native_geometry.stage_a = stages[:, 2]
    return basis, native_geometry


def weighted_evaluate(self, base_first, rho, coefficients, *, linearize=False):
    """Exact original angular kernels with declared positive radial weights."""
    o = self.o
    c = self.coefficient_matrix(coefficients)
    yu, yy = self.stage_u@c, self.stage_y@c
    normal = np.zeros((self.dimension, self.dimension)) if linearize else None
    gradient = np.zeros(self.dimension) if linearize else None
    cost, raw, maximum, determinant = 0., 0., 0., float('inf')
    ri, cj = self.pairs.T
    sw, mw = self.sqrt_multiplicity, self.multiplicity
    for stage, a in enumerate(o.a):
        weight = self.radial_weights[stage]
        V = base_first[0, stage]+np.einsum('c,nck->nk', yu[stage], self.h)
        d = base_first[1, stage]+np.einsum('c,nck->nk', yy[stage], self.dh)
        ar = a*rho
        r0 = np.sum(V*V, axis=1)-1.
        r1 = np.sum(V*d, axis=1)/ar
        r2 = np.sum(d*d, axis=1)/(ar*ar)-1.
        local = float(mw@(r0*r0+2*r1*r1+r2*r2))
        cost += weight*local
        raw += local
        norm = (np.abs(r0+r2)+np.sqrt((r0-r2)**2+4*r1*r1))/2
        maximum = max(maximum, float(np.max(norm)))
        determinant = min(determinant, float(np.min((1+r0)*(1+r2)-r1*r1)))
        if not linearize:
            continue
        by, bu = self.stage_y[stage, ri], self.stage_u[stage, ri]
        active = np.flatnonzero((by != 0) | (bu != 0))
        if not active.size:
            continue
        vh = np.einsum('nk,nck->nc', V, self.h)
        dh = np.einsum('nk,nck->nc', d, self.h)
        vdh = np.einsum('nk,nck->nc', V, self.dh)
        ddh = np.einsum('nk,nck->nc', d, self.dh)
        a0 = (2*sw)[:, None]*vh
        a1 = (sw/ar)[:, None]*dh
        b1 = (sw/ar)[:, None]*vdh
        b2 = (2*sw/(ar*ar))[:, None]*ddh
        kuu = a0.T@a0+2*a1.T@a1
        kuy = 2*a1.T@b1
        kyy = 2*b1.T@b1+b2.T@b2
        gu = a0.T@(sw*r0)+2*a1.T@(sw*r1)
        gy = 2*b1.T@(sw*r1)+b2.T@(sw*r2)
        ci = cj[active]
        ix = np.ix_(ci, ci)
        u, y = bu[active], by[active]
        block = (np.outer(u, u)*kuu[ix]+np.outer(u, y)*kuy[ix]
                 +np.outer(y, u)*kuy.T[ix]+np.outer(y, y)*kyy[ix])
        normal[np.ix_(active, active)] += weight*block
        gradient[active] += weight*(u*gu[ci]+y*gy[ci])
    return dict(weighted_sse=cost, all_raw_sse=raw, max_gram=maximum,
                min_determinant=determinant, normal_matrix=normal, gradient=gradient)


def observed_stats(o, x, stage_weights):
    raw = o.raw_residual(x)
    e, f, g = raw[..., 0], raw[..., 1], raw[..., 2]
    point_cost = e*e+2*f*f+g*g
    radial_cost = point_cost@o.multiplicity
    norm = (np.abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2
    legacy = o.legacy_P
    cost = float(stage_weights@radial_cost)
    return dict(weighted_sse=cost,
                weighted_mean_sse=cost/(o.full_N*float(np.sum(stage_weights))),
                all_raw_sse=float(np.sum(radial_cost)),
                legacy_raw_sse=float(np.sum(radial_cost[:legacy])),
                max_gram=float(np.max(norm)), legacy_max_gram=float(np.max(norm[:legacy])),
                added_max_gram=float(np.max(norm[legacy:])),
                min_determinant=float(np.min((1+e)*(1+g)-f*f)))


def main(args):
    started = time.monotonic()
    if args.out.exists() or args.out.with_suffix('.npz').exists():
        raise FileExistsError('Use a fresh output path')
    base, memory_module = load(args.qp_source), load(args.memory_source)
    batch, observed, coarse = load(args.batch_source), load(args.observed_source), load(args.coarse_source)
    data = np.load(args.bundle, allow_pickle=False)
    carrier = np.load(args.carrier, allow_pickle=False)
    plan = observed.ObservationPlan.from_arrays(carrier)
    common = dict(M=(data['qjets'].shape[-1]-2)//3, N=args.angles,
                  width=float(data['width']), quarter=True, stage_block=args.stage_block)
    inputs = (data['mesh'], data['a_stages'], float(data['radius']), data['fixed_core_first3'])
    native = batch.create(args.operator, *inputs, **common)
    o = observed.create(args.operator, *inputs, batch_source=batch, observation_plan=plan,
                         a_observations=carrier['a_observations'], **common)
    x, affine = o.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    original_core = x[:o.M-o.K].copy()
    centers = [float(v) for v in args.centers.split(',')]
    basis = coarse.make_space(args.base_source, native, low_modes=args.low_modes, desired_centers=centers)
    native_geometry = base.CoarseGeometry(native, basis)
    basis, geometry = retarget_basis(o, basis, native_geometry)
    radial_weights = o.mixed_stage_weights(args.legacy_fraction)
    if not np.all(radial_weights > 0):
        raise ValueError('Every retained and added row must have positive radial weight')
    basis.radial_weights = radial_weights
    basis.evaluate = MethodType(weighted_evaluate, basis)
    base.fields_block = fields_block_observed
    memory = memory_module.ActiveMemory(args.memory_curvature, args.memory_radius)
    if args.memory_input is not None:
        payload = json.loads(args.memory_input.read_text())
        recorded_carrier = payload.get('observation_carrier_sha256')
        if recorded_carrier is not None and recorded_carrier != sha(args.carrier):
            raise ValueError('Remembered Gauss locations belong to a different carrier')
        memory.restore(args.memory_input)
        if recorded_carrier is None:
            if args.angles != 2048 or any(s >= o.legacy_P for s, _ in list(memory.curvature)+list(memory.radius)):
                raise ValueError('Unbound memory is allowed only for the documented 2048-angle legacy prefix')
    initial_memory = memory.state()
    def memory_state():
        value = memory.state()
        value.update(observation_carrier_sha256=sha(args.carrier), full_angles=o.full_N,
                     legacy_stages=o.legacy_P, total_stages=o.P)
        return value
    o.set_base(x)
    initial_geometry, curvatures, radii = base.scan_geometry(
        o, x, top_curvature=args.top_curvature, top_radius=args.top_radius)
    def product(z):
        return args.reach_ratio*z.get('diameter_point_lower', float('inf'))*z.get(
            'maximum_absolute_principal_curvature', float('inf'))
    if not initial_geometry['complete'] or product(initial_geometry) > args.safety:
        raise ValueError('Input fails the expanded-observation necessary screen: '+repr(initial_geometry))
    # Check the new interpolation-to-physical-basis map at an added Gauss
    # point.  The principal-curvature differential itself is unchanged.
    probe_stage = int(plan.gauss_indices[len(plan.gauss_indices)//2, plan.order//2])
    probe = base.derivative_probe(o, x, basis, geometry, (probe_stage, o.N//3, 0))
    initial = state = observed_stats(o, x, radial_weights)
    current_geometry = initial_geometry
    records, damping, status = [], args.damping, 'iteration_budget'
    initial_mapping_check = None
    for iteration in range(args.steps):
        if time.monotonic()-started > args.seconds:
            status = 'time_budget'; break
        o.set_base(x)
        linear = basis.evaluate(o._base_first, o._base_p.rho, np.zeros(basis.dimension), linearize=True)
        difference = abs(linear['weighted_sse']-state['weighted_sse'])/max(1., state['weighted_sse'])
        if difference > 2.e-10:
            raise ValueError('New weighted basis evaluator disagrees with actual operator')
        if initial_mapping_check is None:
            initial_mapping_check = difference
        cpoints, rpoints = memory.combine(curvatures, radii, o)
        Q, bounds, active = geometry.constraints(x, cpoints, rpoints, args.reach_ratio, args.safety)
        direction, qp = base.constrained_direction(linear['normal_matrix'], linear['gradient'], Q, bounds, damping)
        free = basis.free_direction(direction)
        record = dict(iteration=iteration, before=state, geometry_before=current_geometry,
                      qp=qp, active_curvature_branches=len(cpoints), active_radius_points=len(rpoints),
                      memory_before=memory_state(), active_constraints=active, trials=[])
        accepted = False
        for k in range(args.backtracks):
            alpha = 2.**(-k)
            candidate = x+alpha*free
            trial = observed_stats(o, candidate, radial_weights)
            item = dict(alpha=alpha, statistics=trial, accepted=False)
            if (np.isfinite(trial['weighted_sse']) and trial['weighted_sse'] < state['weighted_sse']
                    and trial['min_determinant'] > 0):
                checked, cnext, rnext = base.scan_geometry(
                    o, candidate, top_curvature=args.top_curvature, top_radius=args.top_radius)
                item.update(geometry=checked, necessary_product=product(checked))
                if checked['complete'] and product(checked) <= args.safety:
                    x, state, current_geometry = candidate, trial, checked
                    curvatures, radii = cnext, rnext
                    item['accepted'] = True
                    accepted = True
                else:
                    memory.observe(checked)
            record['trials'].append(item)
            if accepted:
                break
        damping = max(damping/2, 1.e-8) if accepted else damping*10
        record.update(accepted=accepted, memory_after=memory_state(),
                      elapsed_seconds=time.monotonic()-started)
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k != 'active_constraints'}), flush=True)
        args.out.with_suffix('.memory.json').write_text(json.dumps(memory_state(), indent=2)+'\n')
        args.out.with_suffix('.progress.json').write_text(json.dumps(dict(
            source_sha256=sha(__file__), input_sha256=sha(args.bundle), initial=initial,
            current=state, geometry=current_geometry, records=records), indent=2)+'\n')
    jets, height, _ = o.unpack(x)
    _, final_affine = o.pack(jets, height, require_affine=True)
    if not np.array_equal(x[:o.M-o.K], original_core):
        raise ValueError('Fixed core coefficients changed')
    keys = ('mesh','a_stages','radius','width','fixed_core_first3',
            'a_stage_absolute_error','stage_time_absolute_error')
    arrays = {k:np.array(data[k], copy=True) for k in keys if k in data.files}
    arrays.update(qjets=jets, Hcap=np.asarray(height))
    output = args.out.with_suffix('.npz')
    np.savez_compressed(output, **arrays)
    report = dict(schema='fullclosed-coarse-curvature-QP-gauss6-v3', status=status,
                  source_sha256=sha(__file__), qp_source_sha256=sha(args.qp_source),
                  memory_source_sha256=sha(args.memory_source),
                  observed_source_sha256=sha(args.observed_source),
                  observation_carrier_sha256=sha(args.carrier),
                  input_sha256=sha(args.bundle), output_bundle_sha256=sha(output),
                  operator_sha256=sha(args.operator), batch_source_sha256=sha(args.batch_source),
                  base_source_sha256=sha(args.base_source), coarse_source_sha256=sha(args.coarse_source),
                  memory_input_sha256=None if args.memory_input is None else sha(args.memory_input),
                  initial_memory=initial_memory, final_memory=memory_state(),
                  maximum_constraint_count=(args.top_curvature+2*args.memory_curvature)*
                      (args.top_radius+args.memory_radius+2),
                  subspace_dimension=basis.dimension, low_modes=args.low_modes,
                  centers=[float(o.mesh[i]) for i in basis.center_nodes],
                  full_variables=o.free_size, observation_metadata=o.observation_metadata(),
                  all_original_gram_rows_retained=True, full_rows=o.P*o.full_N*3,
                  packed_rows=o.P*o.N*3, legacy_full_rows=o.legacy_P*o.full_N*3,
                  objective='Radial integral Gram SSE with positive Simpson/Gauss mixture; different from old raw sum',
                  legacy_fraction=args.legacy_fraction,
                  radial_weight_min=float(np.min(radial_weights)),
                  radial_weight_max=float(np.max(radial_weights)),
                  radial_weight_sum=float(np.sum(radial_weights)),
                  initial_weighted_basis_to_operator_relative_difference=initial_mapping_check,
                  added_gauss_derivative_probe=probe,
                  initial=initial, final=state, initial_geometry=initial_geometry,
                  final_geometry=current_geometry, reach_ratio=args.reach_ratio,
                  numerical_safety=args.safety, initial_affine=affine, final_affine=final_affine,
                  initial_height=float(data['Hcap']), final_height=float(height),
                  fixed_scalar_mesh_and_core_unchanged=True, iterations=records,
                  elapsed_seconds=time.monotonic()-started, continuous_metric_certified=False,
                  reach_certified=False, held_amplitude_certified=False, exact_solution_claimed=False)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'iterations'}), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle','operator','batch-source','base-source','coarse-source','out',
                'qp-source','memory-source','observed-source','carrier'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--memory-input', type=Path)
    p.add_argument('--legacy-fraction', type=float, default=.5)
    p.add_argument('--memory-curvature', type=int, default=32)
    p.add_argument('--memory-radius', type=int, default=4)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--low-modes', type=int, default=12)
    p.add_argument('--centers', default='.30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26')
    p.add_argument('--top-curvature', type=int, default=32)
    p.add_argument('--top-radius', type=int, default=4)
    p.add_argument('--reach-ratio', type=float, default=.03)
    p.add_argument('--safety', type=float, default=.98)
    p.add_argument('--damping', type=float, default=.001)
    p.add_argument('--steps', type=int, default=12)
    p.add_argument('--backtracks', type=int, default=12)
    p.add_argument('--seconds', type=float, default=1800.)
    main(p.parse_args())
