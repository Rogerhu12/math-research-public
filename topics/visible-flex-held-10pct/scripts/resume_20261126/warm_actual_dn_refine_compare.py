#!/usr/bin/env python3
"""Compare two accepted adjacent actual-DN refinements at one fixed problem.

All six Cartesian jets include the same literal mean1168 and its true
primitive, evaluated numerically. Angular/radial samples and two positive
Gauss rules are observations, not continuous C2 or Cauchy certificates.
The phase-only bounds separately use exact rational triangle estimates and
an outward interval for true pi in the declared v3 frequencies.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import warm_actual_dn_refine_model as model
from warm_true_dn_solve import sha, load, module, write
from warm_fixed_m3_compare_c2 import complete_jets, JETS


def binary_fraction(value):
    sign, mantissa, exponent, bitcount = value
    if not isinstance(exponent, int) or bitcount < 0:
        raise ValueError('Expected a finite mpmath binary endpoint')
    answer = Q(int(mantissa))
    answer = answer*2**exponent if exponent >= 0 else answer/Q(2**(-exponent))
    return -answer if sign else answer


def outward_upper(value):
    if value < 0:
        raise ValueError('An absolute upper bound cannot be negative')
    if not value:
        return dict(upper=0., upper_exact='0')
    number = float(value)
    if not math.isfinite(number):
        raise FloatingPointError('The finite phase difference bound overflows binary64')
    if Q.from_float(number) < value:
        number = float(np.nextafter(number, np.inf))
    if not math.isfinite(number) or Q.from_float(number) < value:
        raise ArithmeticError('The printed phase bound is not an outward rational enclosure')
    return dict(upper=number, upper_exact=str(Q.from_float(number)))


def phase_difference_bounds(first, second, family):
    if (float(first.halfwidth) != float(second.halfwidth)
            or float(first.transition) != float(second.transition)):
        raise ValueError('The two physical phase windows differ')
    width, S = map(lambda x: Q.from_float(float(x)), (first.transition, first.halfwidth))
    if not width > 0 or not S > 0:
        raise ValueError('The declared exact binary-rational window is invalid')
    count = max(len(first.controls), len(second.controls))
    left, right = [Q(0)]*count, [Q(0)]*count
    for target, source in ((left, first.controls), (right, second.controls)):
        for j, value in enumerate(source):
            target[j] = Q.from_float(float(value))
    delta = [b-a for a, b in zip(left, right)]
    pi_record = None
    if family == 'complementary_arc_sine_v1':
        previous = mp.iv.dps
        try:
            mp.iv.dps = 75
            low, high = map(binary_fraction, mp.iv.pi._mpi_)
        finally:
            mp.iv.dps = previous
        if not high >= low > 3 or low/3-S <= width:
            raise ArithmeticError('The true complementary-arc interval is invalid')
        # Interval division with independent endpoint enclosures is outward;
        # no rounded binary64 frequency defines the mathematical target.
        omega_lo = [j*low/(high/3-S) for j in range(1, count+1)]
        omega_hi = [j*high/(low/3-S) for j in range(1, count+1)]
        pi_record = dict(lower_exact=str(low), upper_exact=str(high),
                         interval_precision_decimal=75)
        frequency = 'j*pi/(pi/3-S), true pi enclosed before rational arithmetic'
    elif family == 'full_period_sine_v1':
        omega_lo = omega_hi = [Q(3*j) for j in range(1, count+1)]
        frequency = 'exact integer 3*j'
    else:
        raise ValueError('No phase difference estimate for this declared finite family')
    D1 = Q(630, 256)/width
    D2 = Q(2520, 64)/width**2
    D3 = (Q(7560, 16)+Q(5040, 64))/width**3
    C = {r: sum((abs(d)*hi**r/(lo+D1) for d, lo, hi in
                 zip(delta, omega_lo, omega_hi)), Q(0)) for r in range(4)}
    bounds = dict(phase=C[0], phase_u=C[1]+D1*C[0],
        phase_uu=C[2]+2*D1*C[1]+D2*C[0],
        phase_uuu=C[3]+3*D1*C[2]+3*D2*C[1]+D3*C[0])
    weighted = {}
    for exponent in (0, 2, 4):
        value = sum(((1 if exponent == 0 else 1+j**exponent)*abs(d)
                     for j, d in enumerate(delta, 1)), Q(0))
        weighted[str(exponent)] = dict(exact=str(value), **outward_upper(value))
    return dict(phase_basis_family=family, frequency_definition=frequency,
        zero_extended_delta_d_exact=[str(value) for value in delta],
        literal_control_sequence_weighted_l1=weighted,
        coefficient_norm_scope='Exact j-weighted sequence norms, separately from physical derivative bounds',
        S_exact=str(S), b_exact=str(width), true_pi_interval=pi_record,
        window_derivative_bounds_exact=[str(x) for x in (Q(1), D1, D2, D3)],
        uniform_derivative_upper={key: outward_upper(value) for key, value in bounds.items()},
        phase_only_uniform_bounds_certified=True,
        full_map_C2_or_infinite_limit_inferred=False,
        proof='For Psi_j=W sin(omega_j*v)/(omega_j+D1), use the product rule, '
              '|sin|,|cos|<=1 and exact W derivative bounds. The complete common '
              'baseline, lambda, window and phase family are checked before subtraction.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'first-run', 'second-run', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--angular', type=int, nargs='+')
    parser.add_argument('--radial-count', type=int, default=151)
    parser.add_argument('--height-orders', type=int, nargs=2, default=[6, 12])
    parser.add_argument('--batch', type=int, default=8)
    args = parser.parse_args()
    begin = time.monotonic()
    repo = args.repo.resolve()
    paths = [args.first_run.resolve(), args.second_run.resolve()]
    if args.radial_count < 2 or args.batch < 1 or not 0 < args.height_orders[0] < args.height_orders[1]:
        raise ValueError('Use actual positive comparison resolutions')
    records = [model.accepted_input(path, repo=repo) for path in paths]
    contract = model.require_same_problem(repo, *records)
    if (records[1]['model_kind'] != model.KIND
            or Path(records[1]['actual_source_run']).resolve() != paths[0]
            or records[1]['actual_source_run_sha256'] != sha(paths[0])):
        raise ValueError('Compare the actual adjacent accepted refinement, not unrelated fields')
    objects = model.build_models(repo, records)
    current = repo/'topics/visible-flex-held-10pct/scripts/resume_20261126'
    audit = module('_actual_refine_compare_physical',
        current.parent/'resume_m3/audit_full_relative_metric.py')
    physicals = [audit.load_physical(path.parent/'physical.npz') for path in paths]
    for obj, physical, record in zip(objects, physicals, records):
        if physical.source_sha256 != record['physical_sha256']:
            raise ValueError('An actual accepted physical field changed')
        obj.initial(physical.p)
        if not np.array_equal(obj._core.controls, record['returned_phase_controls']):
            raise ValueError('The actual raw phase coordinates differ from the declared physical controls')
    flows = [obj.flow(physical.p[0]) for obj, physical in zip(objects, physicals)]
    if physicals[0].x[0] != physicals[1].x[0] or physicals[0].x[-1] != physicals[1].x[-1]:
        raise ValueError('The fixed physical meridian interval changed')
    lo, hi = physicals[0].x[[0, -1]]
    radial = [np.linspace(lo, hi, args.radial_count)]
    for physical in physicals:
        radial += [physical.x, (physical.x[:-1]+physical.x[1:])/2.,
                   np.nextafter(physical.x[1:-1], lo)]
    s = np.unique(np.concatenate(radial))
    positions, primitive_changes = [], []
    for flow, physical in zip(flows, physicals):
        low = flow.height_integral(physical, s, 1168, args.height_orders[0])
        high = flow.height_integral(physical, s, 1168, args.height_orders[1])
        if not np.all(np.isfinite(low)) or not np.all(np.isfinite(high)):
            raise FloatingPointError('A true finite-mean primitive evaluation was nonfinite')
        primitive_changes.append(float(np.max(np.abs(high-low))))
        positions.append(high)
    floor = 16*(3*max(record['modes'] for record in records)+1)
    angles = sorted(set(max(floor, n) for n in (args.angular or [floor, 2*floor])))
    results = []
    for N in angles:
        maxima, peaks = {key: 0. for key in JETS}, {key: None for key in JETS}
        theta = 2*np.pi*np.arange(N)/N
        cores = [obj._core.evaluate(theta) for obj in objects]
        core_differences = {}
        for key, label in (('F', 'position'), ('Ft', 'first'), ('Ftt', 'second')):
            values = np.linalg.norm(cores[1][key]-cores[0][key], axis=-1)
            if not np.all(np.isfinite(values)):
                raise FloatingPointError('A complete actual core jet comparison was nonfinite')
            core_differences[label] = float(np.max(values))
        for start in range(0, len(s), args.batch):
            sl = slice(start, start+args.batch)
            jets = [complete_jets(obj, flow, field, s[sl], N, 1168, heights[sl])
                    for obj, flow, field, heights in zip(objects, flows, physicals, positions)]
            for key in JETS:
                difference = np.linalg.norm(jets[1][key]-jets[0][key], axis=-1)
                if not np.all(np.isfinite(difference)):
                    raise FloatingPointError('An actual complete Cartesian jet difference was nonfinite')
                ir, ia = np.unravel_index(np.argmax(difference), difference.shape)
                if difference[ir, ia] > maxima[key]:
                    maxima[key] = float(difference[ir, ia])
                    peaks[key] = dict(s=float(s[start+ir]), psi=float(2*np.pi*ia/N))
        results.append(dict(angular=N, sampled_complete_C2_jet_difference=maxima,
                            peaks=peaks, sampled_complete_core_C2_difference=core_differences))
        print(json.dumps(dict(event='complete_actual_c2_grid', angular=N, jets=maxima)), flush=True)
    family = ('complementary_arc_sine_v1' if records[0]['linear_source_model_kind'].endswith('-v3')
              else 'full_period_sine_v1')
    phase = phase_difference_bounds(objects[0]._core, objects[1]._core, family)
    result = dict(scope=__doc__, status='evaluated', source_runs=list(map(str, paths)),
        source_run_sha256=list(map(sha, paths)), physical_sha256=[p.source_sha256 for p in physicals],
        same_complete_actual_problem=True, fixed_problem=contract,
        modes=[obj.M for obj in objects], angular_samples=angles,
        radial_samples=len(s), radial_range=[float(lo), float(hi)],
        coordinate='common physical s and fixed material psi; same original frozen angular chart',
        mean_nodes=1168, mean_primitive_origin=0., height_orders=args.height_orders,
        observed_height_quadrature_change=primitive_changes,
        height_quadrature_error_certified=False, rows=results, phase_difference_bounds=phase,
        actual_full_height_packet_sha256=[record['tail_seam']['tail_packet_sha256'] for record in records],
        actual_tail_residuals=[record['result']['tail_residual'] for record in records],
        full_tail_field_C2_comparison_paid=False,
        continuous_C2_bound_certified=False, C2_convergence_proven=False,
        infinite_tail_limit_proven=False, full_closed_surface=False,
        source_hashes={str(path): sha(path) for path in
            (Path(__file__), current/'warm_actual_dn_refine_model.py',
             current/'warm_actual_dn_refine_acceptance.py', current/'warm_actual_dn_acceptance.py',
             current/'warm_fixed_m3_compare_c2.py')},
        elapsed=time.monotonic()-begin)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    write(args.out, result)


if __name__ == '__main__':
    main()
