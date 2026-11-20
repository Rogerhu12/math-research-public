#!/usr/bin/env python3
"""Add same-g Gauss observations and read actual closed-field point geometry.

Inputs are existing candidates, the original fullclosed node-definition
report, and the same exact scalar input/sources.  No nonlinear solve or
old dense probe is run.  New scalar values come only from FullHold.at_box.
Output arrays are scratch data reproducible from this complete script.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path).resolve())
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def event(**values):
    print(json.dumps(values), flush=True)


def upper_float(value):
    result = float(value)
    if Q(result) < value:
        result = np.nextafter(result, np.inf)
    return float(result)


def box_error(carrier, box, scale):
    value = Q(float(carrier))
    return max(abs(value-Q(box[0], scale)), abs(value-Q(box[1], scale)))


def prepare_observations(module, template, node_report_path, scalar_input,
                         scalar_source, integer_source, hold_source, order):
    """Literal old carriers plus new rational-u queries of the same scalar.

    The binary local-u values are declared exact observation parameters on
    the original symbolic mesh alpha*S+beta.  They approximate ideal Gauss
    roots; no IEEE-exact quadrature identity is claimed.
    """
    node_report = json.loads(Path(node_report_path).read_text())
    if sha(scalar_input) != node_report['input_sha256']:
        raise ValueError('The new scalar values must use the original node report scalar input')
    raw = Path(scalar_input).read_bytes()
    scalar_data = json.loads(gzip.decompress(raw) if str(scalar_input).endswith('.gz') else raw)
    scalar_module = load('gauss_reader_exact_hold', scalar_source)
    full = scalar_module.FullHold(scalar_data, integer_source, hold_source, panels=128)
    definitions = [(Q(d['S_coefficient']), Q(d['constant']))
                   for d in node_report['true_scalar_nodes']]
    mesh = np.asarray(template['mesh'])
    width = float(template['width'])
    if (len(definitions) != len(mesh)
            or float(node_report['S_carrier']) != float(mesh[-1])
            or float(node_report['radius_carrier']) != float(template['radius'])
            or full.carrier(full.S) != float(mesh[-1])
            or full.carrier(full.R) != float(template['radius'])):
        raise ValueError('The candidate must retain the same exact scalar and symbolic node model')
    break_definition = (Q(1), -Q(width))
    breakpoint_node = next((j for j, d in enumerate(definitions)
                            if d == break_definition), None)
    plan = module.make_plan(mesh, width, order=order, lift_break_node=breakpoint_node)
    values = np.empty(len(plan.cells))
    a_errors = np.empty_like(values)
    time_errors = np.empty_like(values)
    values[:plan.legacy_count] = template['a_stages']
    a_errors[:plan.legacy_count] = template['a_stage_absolute_error']
    time_errors[:plan.legacy_count] = template['stage_time_absolute_error']
    started = time.monotonic()
    for index in range(plan.legacy_count, len(plan.cells)):
        cell = int(plan.cells[index])
        u = Q(float(plan.local_u[index]))
        left, right = definitions[cell], definitions[cell+1]
        coefficient = (1-u)*left[0]+u*right[0]
        constant = (1-u)*left[1]+u*right[1]
        time_box = full.affine_time(coefficient, constant)
        a_box, _ = full.at_box(time_box)
        values[index] = full.carrier(a_box)
        a_errors[index] = upper_float(box_error(values[index], a_box, full.h.S))
        time_errors[index] = upper_float(box_error(plan.times[index], time_box, full.h.S))
        if (index+1-plan.legacy_count) % 256 == 0:
            event(event='same_scalar_gauss_progress',
                  generated=index+1-plan.legacy_count,
                  total=len(plan.cells)-plan.legacy_count,
                  seconds=time.monotonic()-started)
    metadata = dict(scalar=full.metadata(), scalar_input_sha256=sha(scalar_input),
        node_report_sha256=sha(node_report_path),
        original_nodes=len(mesh), old_rows=plan.legacy_count,
        new_rows=len(plan.cells)-plan.legacy_count, total_rows=len(plan.cells),
        order=order, analytic_pieces=len(plan.piece_cells),
        symbolic_lift_break_node=breakpoint_node,
        observation_parameter='Exact binary local_u on the unchanged alpha*S+beta mesh; approximates ideal Gauss nodes',
        time_box_recipe='affine_time((1-u)*alpha_i+u*alpha_next,(1-u)*beta_i+u*beta_next)',
        scalar_recipe='Same FullHold.at_box(time_box), midpoint carrier and outward absolute error',
        old_carriers_preserved=True, scalar_interpolation_used=False,
        maximum_a_carrier_absolute_error=float(a_errors.max()),
        maximum_time_carrier_absolute_error=float(time_errors.max()),
        new_maximum_a_carrier_absolute_error=float(a_errors[plan.legacy_count:].max()),
        seconds=time.monotonic()-started, continuous_field_rounding_certified=False)
    return plan, values, a_errors, time_errors, metadata


def empty_summary():
    return dict(stages=0, max_relative_gram=-1., min_relative_determinant=float('inf'),
        min_relative_E=float('inf'), ss_max=0., sphi_max=0., phiphi_max=0.,
        raw_frobenius_sse=0., min_area=float('inf'),
        maximum_absolute_principal_curvature=-1., maximum_Fss_norm=0.,
        invalid_area_points=0, worst_gram=None, worst_curvature=None)


def location(problem, stages, index):
    row, angle = index
    stage = int(stages[row])
    return dict(stage=stage, s=float(problem.times[stage]),
        phi=float(problem.phi[angle]), parent_cell=int(problem.observation_cells[stage]),
        parent_cell_u=float(problem.observation_u[stage]),
        is_legacy=stage < problem.legacy_P)


def read_candidate(problem, x):
    """Stream every old/new point through the actual complete physical jets."""
    prepared = problem.prepare(x)
    groups = {name: empty_summary() for name in ('old_rows', 'new_gauss_rows', 'all_rows')}
    gauss_sse = 0.
    gauss_velocity_energy = 0.
    started = time.monotonic()
    for start in range(0, problem.P, problem.stage_block):
        stop = min(start+problem.stage_block, problem.P)
        stages = np.arange(start, stop)
        jets = problem.physical_jet_batch(prepared, start, stop)
        V, d = jets['Fs'], jets['Fphi']
        E = np.einsum('bni,bni->bn', V, V)
        F = np.einsum('bni,bni->bn', V, d)
        G = np.einsum('bni,bni->bn', d, d)
        ar = problem.a[start:stop, None]*prepared.rho[None]
        ess, esp, epp = E-1, F/ar, G/(ar*ar)-1
        relative = (np.abs(ess+epp)+np.sqrt((ess-epp)**2+4*esp*esp))/2
        relative_det = (1+ess)*(1+epp)-esp*esp
        sse_by_stage = np.sum((ess*ess+2*esp*esp+epp*epp)*problem.multiplicity[None], axis=1)
        gauss_sse += float(problem.stage_quadrature_weights[start:stop]@sse_by_stage)
        gauss_velocity_energy += float(problem.stage_quadrature_weights[start:stop]
            @np.sum(E*problem.multiplicity[None], axis=1))
        normal = np.cross(V, d)
        area2 = np.einsum('bni,bni->bn', normal, normal)
        area = np.sqrt(area2)
        valid = np.isfinite(area) & (area > 0)
        np.divide(normal, area[:, :, None], out=normal, where=valid[:, :, None])
        e = np.einsum('bni,bni->bn', jets['Fss'], normal)
        f = np.einsum('bni,bni->bn', jets['Fsphi'], normal)
        g = np.einsum('bni,bni->bn', jets['Fphiphi'], normal)
        trace = np.zeros_like(area)
        determinant = np.zeros_like(area)
        np.divide(e*G+g*E-2*f*F, area2, out=trace, where=valid)
        np.divide(e*g-f*f, area2, out=determinant, where=valid)
        curvature = (np.abs(trace)+np.sqrt(np.maximum(0., trace*trace-4*determinant)))/2
        curvature[~valid] = -1.
        ss_norm = np.linalg.norm(jets['Fss'], axis=2)
        masks = dict(old_rows=stages < problem.legacy_P,
                     new_gauss_rows=stages >= problem.legacy_P,
                     all_rows=np.ones(len(stages), dtype=bool))
        for name, mask in masks.items():
            if not np.any(mask):
                continue
            record = groups[name]
            selected = stages[mask]
            record['stages'] += len(selected)
            local = relative[mask]
            index = np.unravel_index(int(np.argmax(local)), local.shape)
            maximum = float(local[index])
            if maximum > record['max_relative_gram']:
                record['max_relative_gram'] = maximum
                record['worst_gram'] = location(problem, selected, index)
            record['min_relative_determinant'] = min(record['min_relative_determinant'], float(relative_det[mask].min()))
            record['min_relative_E'] = min(record['min_relative_E'], float(E[mask].min()))
            for key, values in (('ss_max', ess), ('sphi_max', esp), ('phiphi_max', epp)):
                record[key] = max(record[key], float(np.max(np.abs(values[mask]))))
            record['raw_frobenius_sse'] += float(sse_by_stage[mask].sum())
            record['min_area'] = min(record['min_area'], float(area[mask].min()))
            record['maximum_Fss_norm'] = max(record['maximum_Fss_norm'], float(ss_norm[mask].max()))
            record['invalid_area_points'] += int(np.count_nonzero(~valid[mask]))
            local = curvature[mask]
            index = np.unravel_index(int(np.argmax(local)), local.shape)
            maximum = float(local[index])
            if maximum > record['maximum_absolute_principal_curvature']:
                record['maximum_absolute_principal_curvature'] = maximum
                record['worst_curvature'] = location(problem, selected, index)
    for record in groups.values():
        record['evaluated_points'] = record['stages']*problem.N
        record['full_orbit_points'] = record['stages']*problem.full_N
        record['point_immersion_valid'] = record['invalid_area_points'] == 0
    rho_derivative_bound = float(np.sum(np.abs(problem.freq*problem.qfreq*prepared.core)))
    return dict(**groups, rho_sample_min=float(prepared.rho.min()),
        rho_lipschitz_lower=float(prepared.rho.min()-np.pi/problem.full_N*rho_derivative_bound),
        gauss_radial_frobenius_sse=gauss_sse,
        gauss_radial_frobenius_mean=gauss_sse/(problem.S*problem.full_N),
        gauss_radial_full_Fs_energy=gauss_velocity_energy,
        seconds=time.monotonic()-started,
        scope='All retained old rows and all appended Gauss rows at all finite angle orbits; actual shared-quintic physical jets; point values only',
        continuous_gram_certified=False, continuous_curvature_certified=False,
        reach_certified=False, nonlinear_solve=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, action='append', required=True)
    parser.add_argument('--node-report', type=Path, required=True)
    parser.add_argument('--scalar-input', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--module', type=Path)
    parser.add_argument('--batch-source', type=Path)
    parser.add_argument('--dense-source', type=Path)
    parser.add_argument('--scalar-source', type=Path)
    parser.add_argument('--integer-source', type=Path)
    parser.add_argument('--hold-source', type=Path)
    parser.add_argument('--order', type=int, default=6)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--carrier-only', action='store_true')
    args = parser.parse_args()
    topic = args.repo.resolve()/'topics/visible-flex-larger-amplitude'
    paths = dict(
        module=args.module or Path(__file__).resolve().with_name('gauss_observed_closed_gram.py'),
        batch=args.batch_source or topic/'scripts/resume_20261120_batched_closed_gram.py',
        dense=args.dense_source or topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        scalar=args.scalar_source or topic/'notes/2026-11-17-parallel-model-full-hold-oracle.py',
        integer=args.integer_source or topic/'notes/2026-11-17-parallel-inward-integral-enclosure.py',
        hold=args.hold_source or topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py')
    paths = {key: path.resolve() for key, path in paths.items()}
    args.outdir = args.outdir.resolve()
    args.outdir.mkdir(parents=True, exist_ok=False)
    bundles = [path.resolve() for path in args.bundle]
    with np.load(bundles[0], allow_pickle=False) as loaded:
        template = {key: np.array(loaded[key]) for key in loaded.files}
    module = load('same_scalar_gauss_observed_operator', paths['module'])
    plan, values, a_errors, time_errors, scalar_meta = prepare_observations(module,
        template, args.node_report.resolve(), args.scalar_input.resolve(),
        paths['scalar'], paths['integer'], paths['hold'], args.order)
    prepared_path = args.outdir/'same-scalar-gauss-observations.npz'
    arrays = plan.arrays()
    arrays.update(a_observations=values, a_observation_absolute_error=a_errors,
        observation_time_absolute_error=time_errors,
        mesh=template['mesh'], a_stages=template['a_stages'],
        radius=template['radius'], width=template['width'],
        fixed_core_first3=template['fixed_core_first3'])
    np.savez_compressed(prepared_path, **arrays)
    report = dict(schema='same-scalar-complete-Gauss-observation-readout-20261120-v1',
        source_sha256=sha(__file__), sources={key: dict(path=str(path), sha256=sha(path)) for key, path in paths.items()},
        scalar_preparation=scalar_meta,
        observation_carrier_path=str(prepared_path), observation_carrier_sha256=sha(prepared_path),
        order=args.order, full_angles=args.angles, stage_block=args.stage_block,
        candidates=[], old_diagnostics_repeated=False, nonlinear_solve=False)
    report_path = args.outdir/'report.json'
    report_path.write_text(json.dumps(report, indent=2)+'\n')
    event(event='same_scalar_gauss_carriers_ready', **{key: scalar_meta[key]
        for key in ('old_rows', 'new_rows', 'total_rows', 'order', 'maximum_a_carrier_absolute_error')})
    if not args.carrier_only:
        for path in bundles:
            with np.load(path, allow_pickle=False) as data:
                for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
                    if not np.array_equal(data[key], template[key]):
                        raise ValueError('All read candidates must keep the same scalar/carrier model: '+key)
                M = (data['qjets'].shape[-1]-2)//3
                problem = module.create(paths['dense'], data['mesh'], data['a_stages'],
                    float(data['radius']), data['fixed_core_first3'], batch_source=paths['batch'],
                    observation_plan=plan, a_observations=values, M=M, N=args.angles,
                    width=float(data['width']), quarter=True, stage_block=args.stage_block)
                x, affine = problem.pack(data['qjets'], float(data['Hcap']), require_affine=True)
            record = dict(bundle=str(path), bundle_sha256=sha(path), M=M,
                observation=problem.observation_metadata(), affine=affine,
                readout=read_candidate(problem, x))
            report['candidates'].append(record)
            report_path.write_text(json.dumps(report, indent=2)+'\n')
            event(event='actual_gauss_candidate_read', bundle=str(path),
                old_gram=record['readout']['old_rows']['max_relative_gram'],
                new_gram=record['readout']['new_gauss_rows']['max_relative_gram'],
                old_curvature=record['readout']['old_rows']['maximum_absolute_principal_curvature'],
                new_curvature=record['readout']['new_gauss_rows']['maximum_absolute_principal_curvature'],
                seconds=record['readout']['seconds'])
    event(event='same_scalar_gauss_readout_complete', report=str(report_path),
          report_sha256=sha(report_path), observation_sha256=sha(prepared_path),
          candidates=len(report['candidates']))


if __name__ == '__main__':
    main()
