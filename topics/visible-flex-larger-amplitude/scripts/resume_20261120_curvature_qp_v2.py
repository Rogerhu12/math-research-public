#!/usr/bin/env python3
"""Continue the physical curvature QP with bounded rejected-peak memory.

Every remembered location is differentiated at the actual current field.
Both principal branches are included, regardless of the earlier branch or
sign.  Current extremes are retained as well.  The complete original Gram
and full native-stage point geometry still decide every accepted trial.
"""
import argparse
from collections import OrderedDict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    name = 'curvature_memory_dependency_' + sha(path)[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


class ActiveMemory:
    def __init__(self, curvature_capacity=32, radius_capacity=4):
        if curvature_capacity < 1 or radius_capacity < 1:
            raise ValueError('Positive bounded memory capacities required')
        self.curvature_capacity, self.radius_capacity = curvature_capacity, radius_capacity
        self.curvature, self.radius = OrderedDict(), OrderedDict()
        self.insertions, self.evictions = 0, 0

    def _put(self, target, location, capacity):
        point = (int(location[0]), int(location[1]))
        target.pop(point, None)
        target[point] = None
        self.insertions += 1
        while len(target) > capacity:
            target.popitem(last=False)
            self.evictions += 1

    def observe(self, geometric_report):
        if not geometric_report.get('complete'):
            return
        k, r = geometric_report['worst'], geometric_report['farthest']
        self._put(self.curvature, (k['stage'], k['angle']), self.curvature_capacity)
        self._put(self.radius, (r['stage'], r['angle']), self.radius_capacity)

    def restore(self, path):
        payload = json.loads(Path(path).read_text())
        if 'curvature_locations' in payload:
            for loc in payload['curvature_locations']:
                self._put(self.curvature, loc, self.curvature_capacity)
            for loc in payload['radius_locations']:
                self._put(self.radius, loc, self.radius_capacity)
        else:
            for iteration in payload.get('iterations', payload.get('records', [])):
                for trial in iteration.get('trials', []):
                    if not trial.get('accepted') and 'geometry' in trial:
                        self.observe(trial['geometry'])

    def combine(self, curvature, radius, operator):
        all_curvature = list(curvature)
        for stage, angle in self.curvature:
            if not 0 <= stage < operator.P or not 0 <= angle < operator.N:
                raise ValueError('Remembered point is outside this fixed stage/angle grid')
            all_curvature.extend(((stage, angle, 0), (stage, angle, 1)))
        all_radius = list(radius)+list(self.radius)
        for stage, angle in all_radius:
            if not 0 <= stage < operator.P or not 0 <= angle < operator.N:
                raise ValueError('Remembered radius point is outside this fixed grid')
        return list(dict.fromkeys(all_curvature)), list(dict.fromkeys(all_radius))

    def state(self):
        return dict(schema='bounded-curvature-qp-point-memory-v1',
                    curvature_capacity=self.curvature_capacity, radius_capacity=self.radius_capacity,
                    curvature_locations=list(self.curvature), radius_locations=list(self.radius),
                    insertion_count=self.insertions, eviction_count=self.evictions,
                    scope='Only fixed-grid locations; no old values, signs, eigenvectors, or derivatives')


def main(args):
    started = time.monotonic()
    if args.out.exists() or args.out.with_suffix('.npz').exists():
        raise FileExistsError('Use a fresh output path')
    base, batch, coarse = load(args.qp_source), load(args.batch_source), load(args.coarse_source)
    data = np.load(args.bundle, allow_pickle=False)
    o = batch.create(args.operator, data['mesh'], data['a_stages'], float(data['radius']),
                     data['fixed_core_first3'], M=(data['qjets'].shape[-1]-2)//3,
                     N=args.angles, width=float(data['width']), quarter=True,
                     stage_block=args.stage_block)
    x, affine = o.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    original_core = x[:o.M-o.K].copy()
    centers = [float(v) for v in args.centers.split(',')]
    basis = coarse.make_space(args.base_source, o, low_modes=args.low_modes, desired_centers=centers)
    geometry = base.CoarseGeometry(o, basis)
    memory = ActiveMemory(args.memory_curvature, args.memory_radius)
    if args.memory_input is not None:
        memory.restore(args.memory_input)
    initial_memory = memory.state()
    o.set_base(x)
    initial_geometry, curvatures, radii = base.scan_geometry(
        o, x, top_curvature=args.top_curvature, top_radius=args.top_radius)
    def product(z):
        return args.reach_ratio*z.get('diameter_point_lower', float('inf'))*z.get(
            'maximum_absolute_principal_curvature', float('inf'))
    if not initial_geometry['complete'] or product(initial_geometry) > args.safety:
        raise ValueError('Input fails the declared necessary sampled screen')
    # The analytic derivative implementation is unchanged from its recorded
    # v1 execution.  Do not repeat its already successful complex-step check.
    initial = state = base.gram_stats(o, x)
    current_geometry = initial_geometry
    records, damping, status = [], args.damping, 'iteration_budget'
    for iteration in range(args.steps):
        if time.monotonic()-started > args.seconds:
            status = 'time_budget'; break
        o.set_base(x)
        linear = basis.evaluate(o._base_first, o._base_p.rho, np.zeros(basis.dimension), linearize=True)
        cpoints, rpoints = memory.combine(curvatures, radii, o)
        Q, bounds, active = geometry.constraints(x, cpoints, rpoints, args.reach_ratio, args.safety)
        direction, qp = base.constrained_direction(linear['normal_matrix'], linear['gradient'], Q, bounds, damping)
        free = basis.free_direction(direction)
        record = dict(iteration=iteration, before=state, geometry_before=current_geometry,
                      qp=qp, active_curvature_branches=len(cpoints), active_radius_points=len(rpoints),
                      memory_before=memory.state(), active_constraints=active, trials=[])
        accepted = False
        for k in range(args.backtracks):
            alpha = 2.**(-k)
            candidate = x+alpha*free
            trial = base.gram_stats(o, candidate)
            item = dict(alpha=alpha, statistics=trial, accepted=False)
            if np.isfinite(trial['raw_sse']) and trial['raw_sse'] < state['raw_sse'] and trial['min_determinant'] > 0:
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
        record.update(accepted=accepted, memory_after=memory.state(),
                      elapsed_seconds=time.monotonic()-started)
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k != 'active_constraints'}), flush=True)
        args.out.with_suffix('.memory.json').write_text(json.dumps(memory.state(), indent=2)+'\n')
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
    report = dict(schema='fullclosed-coarse-curvature-QP-memory-v2', status=status,
                  source_sha256=sha(__file__), qp_source_sha256=sha(args.qp_source),
                  input_sha256=sha(args.bundle), output_bundle_sha256=sha(output),
                  operator_sha256=sha(args.operator), batch_source_sha256=sha(args.batch_source),
                  base_source_sha256=sha(args.base_source), coarse_source_sha256=sha(args.coarse_source),
                  memory_input_sha256=None if args.memory_input is None else sha(args.memory_input),
                  initial_memory=initial_memory, final_memory=memory.state(),
                  memory_policy='LRU fixed-grid curvature locations, both branches recomputed; radius locations; old values not retained',
                  maximum_constraint_count=(args.top_curvature+2*args.memory_curvature)*
                      (args.top_radius+args.memory_radius+2),
                  subspace_dimension=basis.dimension, low_modes=args.low_modes,
                  centers=[float(o.mesh[i]) for i in basis.center_nodes],
                  full_variables=o.free_size, all_original_gram_rows_retained=True,
                  full_rows=o.P*o.full_N*3, packed_rows=o.P*o.N*3,
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
    for key in ('bundle','operator','batch-source','base-source','coarse-source','out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--qp-source', type=Path,
                   default=Path(__file__).with_name('resume_20261120_curvature_qp.py'))
    p.add_argument('--memory-input', type=Path)
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
    p.add_argument('--seconds', type=float, default=1200.)
    main(p.parse_args())
