#!/usr/bin/env python3
"""R674 cancellation-preserving relative Gram for canonical R671 fields.

This independent consumer keeps R657's exact radial numerator polynomials,
all angular modes and nonlinear closed-arc bounds.  It consumes the new
reference-tail scalar Taylor jets and pays their physical field errors.
No scientific work runs on import; the CLI requires public Actions.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import resource
import sys
import time

import numpy as np


REFERENCE_INTERVAL_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
LEGACY_GRAM_SHA = '5bbf821f45fec3a8ecd29ebd64dce8058bb302f7d53416b50158cca743065a13'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path, expected):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('Changed stated complete interval source: '+str(path))
    name = '_reference_tail_gram_'+name+'_'+expected[:16]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def make_reader(*, repo, bundle, node_report, scalar_input, reference_carrier=None,
                angles=8192, radial_subdivisions=16, scalar_degree=5, panels=128):
    src = Path(repo).resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    reference_path, gram_path = src/'exact_reference_tail_interval.py', src/'fullclosed_relative_gram_interval.py'
    reference_module = load('profile', reference_path, REFERENCE_INTERVAL_SHA)
    legacy = load('numerators', gram_path, LEGACY_GRAM_SHA)
    profile = reference_module.ReferenceIntervalReader(repo=repo, bundle=bundle,
        node_report=node_report, scalar_input=scalar_input, reference_carrier=reference_carrier,
        angles=256, low_modes=24, angular_taylor_degree=12,
        scalar_degree=scalar_degree, radial_block=1, panels=panels, beta='1/4')

    class TightGram(legacy.Gram):
        def __init__(self):
            self.profile = profile
            self.subdivisions = int(radial_subdivisions)
            if self.subdivisions < 1 or self.subdivisions & (self.subdivisions-1):
                raise ValueError('Use a positive dyadic radial subdivision count')
            paths = profile.old_paths
            super().__init__(bundle, node_report, paths['interval_source'], paths['geometry_source'],
                profile.paths['scalar_polynomial_source'], scalar_input,
                angles=int(angles), subdivisions=self.subdivisions, scalar_degree=scalar_degree)
            self._q_cache = None

        def raw_components(self, cell, piece):
            r, I = self.r, self.I
            if self._q_cache is None or self._q_cache[0] != cell:
                h = r.width_box(r.nodes[cell], r.nodes[cell+1])
                q = r.hermite(I.at(r.jets, cell), I.at(r.jets, cell+1), h)
                self._q_cache = cell, (q, r.derivative(q, h))
            q, v = [r.restrict(value, piece[2], piece[3]) for value in self._q_cache[1]]
            U = [self.grid_jets(c, parity) for c, parity in r.channels(v, 0)]
            T0 = [self.grid_jets(c, parity) for c, parity in r.channels(q, 1)]
            return U, T0

        def new_numerators(self, cell, piece, p):
            """Exact approximate-field P+C*cos(delta)+S*sin(delta) form.

            p is a common Taylor profile, not a new target metric.  Its
            physical errors are paid only after R657 relative normalization.
            No old-chi active flag skips a potentially active eta lift.
            """
            I = self.I
            U, T0 = self.raw_components(cell, piece)
            c, d, f = [self.scalar_poly(v) for v in (p['f'][1], p['z'][1], p['f'][0])]
            A = self.scalar_poly(p['a_poly0'])
            rho2 = self.multiply(self.rho_poly, self.rho_poly)
            Pe = self.sub(self.dot(U, U), self.constant(1))
            Pe = self.add(Pe, self.add(self.multiply(c, c), self.multiply(d, d)))
            Pe = self.add(Pe, I.scale(self.multiply(d, U[2]), 2))
            Ce, Se = I.scale(self.multiply(c, U[0]), 2), I.scale(self.multiply(c, U[1]), 2)
            Pm = self.add(self.dot(U, T0), self.multiply(d, T0[2]))
            fr = self.multiply(f, self.rho_poly)
            Cm = self.add(self.multiply(c, T0[0]), self.multiply(fr, U[1]))
            Sm = self.sub(self.multiply(c, T0[1]), self.multiply(fr, U[0]))
            exact_reference_region = bool(self.profile.lam == 1
                and self.profile.scalar.cmp(self.profile.eta_right, piece[0]) <= 0)
            if exact_reference_region:
                # The same formal Taylor polynomial is f=A here.  The
                # difference f^2-A^2 is identically zero, including its
                # common uncertain coefficients; no interval subtraction.
                Pg = self.dot(T0, T0)
            else:
                pure = self.sub(self.multiply(f, f), self.multiply(A, A))
                Pg = self.add(self.dot(T0, T0), self.multiply(pure, rho2))
            Cg, Sg = I.scale(self.multiply(fr, T0[1]), 2), I.scale(self.multiply(fr, T0[0]), -2)
            return [(Pe, Ce, Se), (Pm, Cm, Sm), (Pg, Cg, Sg)], exact_reference_region

        def actual_entries(self, numerators, A_box, p, rho_box):
            """R657 target correction once, then R674 physical-field fees.

            The resulting entries enclose the ACTUAL new reference field.
            In epsilon_W, rho is cancelled symbolically before bounds.
            """
            I = self.I
            entries, a, target_fee = self.relative(numerators, A_box, p['a_error0'], rho_box)
            BV = I.sqrt(I.add(I.exact(1.), entries[0]))[1]
            BW = I.sqrt(I.add(I.exact(1.), entries[2]))[1]
            ev = I.sqrt(I.add(I.square(I.exact(p['f_error'][1])),
                             I.square(I.exact(p['z_error'][1]))))[1]
            # |delta(F_phi)/(a*rho)| <= e_f0/a, since rho>0.
            ew = I.div(I.exact(p['f_error'][0]), a)[1]
            v, w = I.exact(ev), I.exact(ew)
            bv, bw = I.exact(BV), I.exact(BW)
            de = I.add(I.scale(I.mul(bv, v), 2), I.square(v))[1]
            dm = I.add(I.add(I.mul(bw, v), I.mul(bv, w)), I.mul(v, w))[1]
            dg = I.add(I.scale(I.mul(bw, w), 2), I.square(w))[1]
            fees = [de, dm, dg]
            actual = [I.add(value, (-fee, fee)) for value, fee in zip(entries, fees)]
            return actual, a, target_fee, fees

        def certify(self, cell):
            if not 0 <= cell < self.r.J-1:
                raise ValueError('Selected original cell is outside the exact carrier')
            if self.profile._old_formula_applies(cell):
                result = super().certify(cell)
                result.update(reference_lift_active=False, current_candidate_recomputed=True,
                              old_candidate_bounds_inherited=False)
                return result
            I, r = self.I, self.r
            started = time.monotonic()
            result = dict(cell=cell, symbolic_left=[str(v) for v in r.nodes[cell]],
                symbolic_right=[str(v) for v in r.nodes[cell+1]],
                continuous_relative_gram_operator_upper=0., actual_supremum_lower=0.,
                maximum_component_absolute_upper=[0., 0., 0.], minimum_a_lower=None,
                minimum_rho_lower=float(r.rho[0].min()),
                scalar_target_remainder_relative_gram_upper=0.,
                new_physical_scalar_gram_fee_component_upper=[0., 0., 0.],
                nonlinear_angular_fourth_order_padding_upper=0.,
                numerator_coefficient_interval_width_upper=0.,
                maximum_numerator_degree=0, reference_f2_minus_A2_cancelled_subpieces=0,
                scalar_pieces=[], worst=None, actual_lower_witness=None)
            pieces = self.profile.pieces(cell)
            for part, piece in enumerate(pieces):
                for sub in range(self.subdivisions):
                    exact_piece = self.profile.subpiece(cell, piece, sub, self.subdivisions)
                    p = self.profile.profile_controls(exact_piece, include_target=True)
                    triples, cancelled = self.new_numerators(cell, exact_piece, p)
                    result['reference_f2_minus_A2_cancelled_subpieces'] += int(cancelled)
                    result['maximum_numerator_degree'] = max(result['maximum_numerator_degree'],
                        *(len(value[0])-1 for triple in triples for value in triple))
                    grid = [self.nonlinear_grid(triple) for triple in triples]
                    N = []
                    for jets, fourth in grid:
                        box, _, nonlinear = self.angle_enclosure(jets, fourth)
                        N.append((box[0].min(axis=0), box[1].max(axis=0)))
                        result['nonlinear_angular_fourth_order_padding_upper'] = max(
                            result['nonlinear_angular_fourth_order_padding_upper'], float(np.max(nonlinear)))
                        width = I.sub(I.at(jets, (slice(None), 0)), I.at(jets, (slice(None), 0)))
                        result['numerator_coefficient_interval_width_upper'] = max(
                            result['numerator_coefficient_interval_width_upper'], float(width[1].max()))
                    A = p['a_poly0']
                    A_box = np.asarray(A[0].min()), np.asarray(A[1].max())
                    entries, a, target_fee, fees = self.actual_entries(N, A_box, p, r.rho)
                    norm = self.norm_interval(entries)
                    index = int(np.argmax(norm[1]))
                    if float(norm[1][index]) > result['continuous_relative_gram_operator_upper']:
                        result['continuous_relative_gram_operator_upper'] = float(norm[1][index])
                        result['worst'] = dict(piece=part, radial_subcell=sub, angle_grid_index=index)
                    for k, entry in enumerate(entries):
                        result['maximum_component_absolute_upper'][k] = max(
                            result['maximum_component_absolute_upper'][k], float(I.absolute_upper(entry).max()))
                        result['new_physical_scalar_gram_fee_component_upper'][k] = max(
                            result['new_physical_scalar_gram_fee_component_upper'][k], float(np.max(fees[k])))
                    low_a = float(np.min(a[0]))
                    result['minimum_a_lower'] = low_a if result['minimum_a_lower'] is None else min(result['minimum_a_lower'], low_a)
                    result['scalar_target_remainder_relative_gram_upper'] = max(
                        result['scalar_target_remainder_relative_gram_upper'], float(np.max(target_fee)))
                    result['scalar_pieces'].append(dict(piece=part, radial_subcell=sub,
                        symbolic_left=[str(v) for v in exact_piece[0]],
                        symbolic_right=[str(v) for v in exact_piece[1]],
                        target_a_error=p['a_error0'], f_errors=p['f_error'], z_errors=p['z_error'],
                        **p['detail']))
                    # Actual exact endpoint/angle witnesses; all new scalar
                    # errors remain paid.  These are lower bounds, not a
                    # replacement for the closed-arc upper calculation.
                    rho_grid = I.at(self.rho_jets, (0, r.angle_slice))
                    for endpoint in (0, -1):
                        point = [I.at(jets, (endpoint, 0, r.angle_slice)) for jets, _ in grid]
                        actual, _, _, _ = self.actual_entries(point, I.at(A, endpoint), p, rho_grid)
                        lower = self.norm_interval(actual)[0]
                        j = int(np.argmax(lower))
                        if float(lower[j]) > result['actual_supremum_lower']:
                            result['actual_supremum_lower'] = max(0., float(lower[j]))
                            result['actual_lower_witness'] = dict(piece=part, radial_subcell=sub,
                                endpoint=endpoint, angle_grid_index=j)
            result.update(exact_pieces=len(pieces), reference_lift_active=True,
                radial_subdivisions_per_joint_piece=self.subdivisions,
                all_radial_and_angular_points_covered=True,
                complete_original_fourier_modes_and_untruncated_analytic_lift=True,
                new_physical_scalar_remainders_paid=True, target_a_remainder_paid_exactly_once=True,
                rho_cancelled_before_angular_field_scalar_fee=True,
                old_candidate_bounds_inherited=False, strict_under_stated_IEEE_arithmetic=True,
                target_1e_minus6_certified=result['continuous_relative_gram_operator_upper'] <= 1e-6,
                same_candidate_cannot_reach_1e_minus6_by_certificate_refinement=result['actual_supremum_lower'] > 1e-6,
                seconds=time.monotonic()-started)
            return result

        def metadata(self):
            result = self.profile.metadata()
            result.update(source_sha256=sha(__file__),
                schema='R674-reference-tail-cancellation-preserving-relative-Gram-v1',
                reference_interval_source_sha256=sha(reference_path),
                legacy_Gram_source_sha256=sha(gram_path), angles=self.Q,
                radial_subdivisions_per_joint_piece=self.subdivisions,
                relative_matrix='[[|Fs|^2-1,Fs.Fphi/(a*rho)],[same,|Fphi|^2/(a^2*rho^2)-1]]',
                numerator_structure='Exact Bernstein P+C*cos(delta)+S*sin(delta) for common Taylor approximate field; true target and physical scalar fees then paid',
                finite_bandwidth_normalization=self.m,
                nonlinear_angle_cover='All finite modes; first/second grid derivatives; complete fourth-derivative Bell remainder on closed arcs',
                approximate_scalar_used_as_new_metric=False,
                no_fixed_degree6_or_degree12_assumption=True,
                geometric_or_solver_convergence_claimed=False)
            result['source_inputs'] = dict(result['source_inputs'],
                reference_interval_source=dict(path=str(reference_path), sha256=sha(reference_path)),
                legacy_Gram_source=dict(path=str(gram_path), sha256=sha(gram_path)))
            return result

    return TightGram()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'node-report', 'scalar-input', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--reference-carrier', type=Path)
    parser.add_argument('--cells', required=True, help='Explicit comma-separated original cells, or all')
    parser.add_argument('--angles', type=int, default=8192)
    parser.add_argument('--radial-subdivisions', type=int, default=16)
    parser.add_argument('--scalar-degree', type=int, default=5)
    parser.add_argument('--panels', type=int, default=128)
    args = parser.parse_args()
    src = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    interval = load('context', src/'exact_reference_tail_interval.py', REFERENCE_INTERVAL_SHA)
    first = interval.load('execution', interval.source_paths(args.repo)['first_source'], interval.FIRST_SHA)
    execution = first.actions_context()
    if args.out.exists():
        raise FileExistsError('Preserve prior actual new-field reports')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic()
    reader = make_reader(repo=args.repo, bundle=args.bundle, node_report=args.node_report,
        scalar_input=args.scalar_input, reference_carrier=args.reference_carrier,
        angles=args.angles, radial_subdivisions=args.radial_subdivisions,
        scalar_degree=args.scalar_degree, panels=args.panels)
    cells = list(range(reader.r.J-1)) if args.cells == 'all' else sorted(set(int(v) for v in args.cells.split(',')))
    if not cells or cells[0] < 0 or cells[-1] >= reader.r.J-1:
        raise ValueError('Requested original cells are outside the actual carrier')
    report = dict(reader.metadata(), execution=execution, requested_cells=cells,
        complete_scope=False, covered_cells=[], records=[], metric_certified=False,
        status='running', mesh_frequency_refinement_convergence_claimed=False)
    for cell in cells:
        row = reader.certify(cell)
        report['records'].append(row); report['covered_cells'].append(cell)
        report.update(reader.metadata())
        report.update(seconds=time.monotonic()-started,
            process_peak_rss_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        first.write_json(args.out, report)
        first.announce(event='reference_tail_tight_Gram_cell', cell=cell,
            upper=row['continuous_relative_gram_operator_upper'], lower=row['actual_supremum_lower'],
            seconds=row['seconds'], total_seconds=report['seconds'])
    upper = max(row['continuous_relative_gram_operator_upper'] for row in report['records'])
    lower = max(row['actual_supremum_lower'] for row in report['records'])
    complete = cells == list(range(reader.r.J-1))
    report.update(reader.metadata())
    report.update(status='completed', complete_scope=complete,
        covered_relative_gram_operator_upper=upper, covered_actual_supremum_lower=lower,
        complete_relative_gram_operator_upper=upper if complete else None,
        metric_certified=bool(complete and upper <= 1e-6),
        cap_metrics_exact_and_reflection_preserves_gram=True,
        seconds=time.monotonic()-started)
    first.write_json(args.out, report)
    first.announce(event='reference_tail_tight_Gram_completed', report_sha256=sha(args.out),
        bundle_sha256=sha(args.bundle), complete_scope=complete,
        upper=upper, lower=lower, seconds=report['seconds'])


if __name__ == '__main__':
    main()
