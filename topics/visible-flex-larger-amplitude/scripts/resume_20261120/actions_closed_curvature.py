#!/usr/bin/env python3
"""Actions-only full-field curvature with complete low-mode six-jet bounds.

Uses the exact R670 field model, every original mode, and the complete
analytic lift.  The multiplier (-rho**2+i*rho_phi)*P_K is expanded with
ALL Laurent coefficients before any bounded-tail separation.  Actual
Euclidean first/second forms determine the shape operator; sampled a(s)
never normalizes geometry.  Only cells above the requested bound refine.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

import numpy as np


FIRST_GEOMETRY_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class CurvatureReader:
    def __init__(self, base, *, radial_block=4, first_geometry_report=None):
        self.b, self.r, self.I = base, base.r, base.I
        self.radial_block = int(radial_block)
        if self.radial_block < 1:
            raise ValueError('Positive radial block count required')
        self.previous = None
        self.previous_identity = None
        self.maximum_transform_group_entries = 0
        if first_geometry_report is not None:
            old = json.loads(Path(first_geometry_report).read_text())
            sources = old.get('source_inputs', {})
            if (old.get('source_sha256') != FIRST_GEOMETRY_SHA
                    or not old.get('complete_scope')
                    or sources.get('bundle', {}).get('sha256') != sha(base.paths['bundle'])
                    or sources.get('node_report', {}).get('sha256') != sha(base.paths['node_report'])
                    or [v['cell'] for v in old.get('records', [])] != list(range(self.r.J-1))):
                raise ValueError('Optional first-geometry bounds must be from this exact current candidate and model')
            self.previous = old['records']
            self.previous_identity = dict(path=str(Path(first_geometry_report).resolve()),
                sha256=sha(first_geometry_report), scope='Only same-candidate per-cell E/W2 lower bounds reused')
        self._prepare_second_multiplier()

    def _prepare_second_multiplier(self):
        """Full real Laurent coefficients of (-rho^2+i*rho_phi) P_K."""
        b, I, M = self.b, self.I, self.r.M
        phase = np.zeros(2*M+1), np.zeros(2*M+1)
        half = I.scale(b.phase, .5)
        for j in range(1, M+1):
            phase[0][M+j], phase[1][M+j] = I.at(half, j-1)
            phase[0][M-j], phase[1][M-j] = I.neg(I.at(half, j-1))
        term = I.exact(np.array([1.]))
        total = I.exact(np.array([1.]))
        for order in range(1, b.taylor_degree+1):
            term = I.div(b.convolution(term, phase), I.exact(order))
            total = I.add((np.pad(total[0], (M, M)), np.pad(total[1], (M, M))), term)
        rho = np.zeros(2*M+1), np.zeros(2*M+1)
        rho[0][M] = rho[1][M] = 1.
        half = I.scale(I.at(b.rho_coeff, slice(1, None)), .5)
        # i*rho_phi has REAL antisymmetric Laurent coefficients.
        # At +j it is -nu_j*rho_j/2; at -j it is +nu_j*rho_j/2.
        imaginary_rhop = np.zeros(4*M+1), np.zeros(4*M+1)
        for j in range(1, M+1):
            value = I.at(half, j-1)
            rho[0][M+j], rho[1][M+j] = value
            rho[0][M-j], rho[1][M-j] = value
            derivative = I.scale(value, 2*j)
            imaginary_rhop[0][2*M+j], imaginary_rhop[1][2*M+j] = I.neg(derivative)
            imaginary_rhop[0][2*M-j], imaginary_rhop[1][2*M-j] = derivative
        multiplier = I.add(I.neg(b.convolution(rho, rho)), imaginary_rhop)
        complete = b.convolution(total, multiplier)
        cosine, sine = b._cos_sin(complete)
        self.second_cos, self.second_sin, self.second_laurent_tail = b._split_coefficients(cosine, sine)
        prime_coeff = I.scale(I.at(b.rho_coeff, slice(1, None)), 2*np.arange(1, M+1))
        self.rho_prime_abs_upper = float(I.sum_upper(I.absolute_upper(prime_coeff)))
        square_rho = I.square(I.exact(b.rho_upper))
        multiplier_norm = I.sqrt(I.add(I.square(square_rho), I.square(I.exact(self.rho_prime_abs_upper))))
        self.second_multiplier_abs_upper = float(multiplier_norm[1])
        analytic_remainder = I.mul(I.exact(self.second_multiplier_abs_upper), I.exact(b.taylor_remainder))
        self.second_analytic_remainder = float(analytic_remainder[1])
        self.second_total_tail = float(I.add(I.exact(self.second_laurent_tail), analytic_remainder)[1])
        self.full_second_laurent_degree = (b.taylor_degree+2)*M

    def set_resolution(self, angles, modes):
        b = self.b
        if b.angle.Q == angles and b.low_modes == modes:
            return
        b.low_modes = modes
        b.set_angles(angles)

    def piece_definitions(self, cell, piece, *, include_position=False):
        """Exact degree <=6 coefficient rows for all physical jets.

        The return also carries the scalar multiplying each complete
        angular lift remainder.  It is split BEFORE absolute values, so
        radial refinement tightens its controlwise remainder payment.
        """
        b, r, I = self.b, self.r, self.I
        left, right, u0, u1, active = piece
        h = r.width_box(r.nodes[cell], r.nodes[cell+1])
        if float(h[0]) <= 0:
            raise ValueError('Original exact node width must be positive')
        y = r.hermite(I.at(b.basejets, cell), I.at(b.basejets, cell+1), h)
        v = r.derivative(y, h)
        acc = r.derivative(v, h)
        y, v, acc = [r.elevate(r.restrict(q, u0, u1)) for q in (y, v, acc)]
        lift = r.lift_controls(left, right, active)
        def horizontal(controls, order, scalar, C, S):
            return b.add_horizontal(b.channels(controls, order), scalar, C, S)
        V = b.add_z0(b.channels(v, 0), lift['cp'], b.H)
        V = b.add_horizontal(V, lift['fp'], b.er_cos, b.er_sin)
        T = horizontal(y, 1, lift['f'], I.neg(b.rhoer_sin), b.rhoer_cos)
        AA = b.add_z0(b.channels(acc, 0), lift['cpp'], b.H)
        AA = b.add_horizontal(AA, lift['fpp'], b.er_cos, b.er_sin)
        VT = horizontal(v, 1, lift['fp'], I.neg(b.rhoer_sin), b.rhoer_cos)
        EE = horizontal(y, 2, lift['f'], self.second_cos, self.second_sin)
        even, odd = ('cos', 'sin', 'cos'), ('sin', 'cos', 'sin')
        result = dict(V=(V, even, lift['fp'], b.er_tail),
            T=(T, odd, lift['f'], b.rhoer_tail),
            AA=(AA, even, lift['fpp'], b.er_tail),
            VT=(VT, odd, lift['fp'], b.rhoer_tail),
            EE=(EE, even, lift['f'], self.second_total_tail))
        if include_position:
            X = b.add_z0(b.channels(y, 0), lift['chi'], b.H)
            X = b.add_horizontal(X, lift['f'], b.er_cos, b.er_sin)
            result['X'] = X, even, lift['f'], b.er_tail
        return result

    def field_blocks(self, definitions, radial):
        """Bound small batches of radial subcells, retaining every tail."""
        b, r, I = self.b, self.r, self.I
        L = b.low_modes
        r.subdivisions = radial
        prepared = {}
        for name, (channels, parities, scalar, remainder) in definitions.items():
            scalar_parts = I.stack(r.radial_parts(scalar))
            analytic = I.mul(I.exact(I.absolute_upper(scalar_parts)), I.exact(remainder))[1]
            prepared[name] = ([(I.stack(r.radial_parts(component)), parity)
                for component, parity in zip(channels, parities)], analytic)
        # <=2^20 real transform entries per group at the normal levels.
        # A single very large Q still gets one radial subcell, never a
        # full-radial transform.  The original coefficient arrays are small.
        largest_group = max(sum(parity == kind for entries, _ in prepared.values()
                                for _, parity in entries) for kind in ('cos', 'sin'))
        block = min(self.radial_block, max(1, (1 << 20)//(largest_group*7*b.angle.Q)))
        for start in range(0, radial, block):
            stop = min(radial, start+block)
            self.maximum_transform_group_entries = max(self.maximum_transform_group_entries,
                largest_group*(stop-start)*7*b.angle.Q)
            sl = slice(start, stop)
            groups, remainders, addresses = ({'cos': [], 'sin': []} for _ in range(3))
            tail_summary = {}
            for name, (entries, analytic) in prepared.items():
                high_max, analytic_max = 0., 0.
                for k, (component, parity) in enumerate(entries):
                    part = I.at(component, (sl, slice(None), slice(None)))
                    high = I.sum_upper(I.absolute_upper(I.at(part, (..., slice(L+1, None)))), axis=-1)
                    extra = analytic[sl] if k < 2 else np.zeros_like(high)
                    loss = I.add(I.exact(high), I.exact(extra))[1]
                    groups[parity].append(I.at(part, (..., slice(0, L+1))))
                    remainders[parity].append(loss)
                    addresses[parity].append((name, k))
                    high_max = max(high_max, float(high.max()))
                    analytic_max = max(analytic_max, float(extra.max()))
                tail_summary[name] = dict(remaining_finite_mode_component_upper=high_max,
                    complete_lift_tail_component_upper=analytic_max)
            fields = {name: [None, None, None] for name in definitions}
            for parity in ('cos', 'sin'):
                if not groups[parity]:
                    continue
                values = b.angle.angle_boxes(I.stack(groups[parity]), parity)
                loss = np.asarray(remainders[parity])[..., None]
                values = I.down(values[0]-loss), I.up(values[1]+loss)
                for j, (name, k) in enumerate(addresses[parity]):
                    fields[name][k] = values[0][j].min(axis=-2), values[1][j].max(axis=-2)
            yield start, stop, fields, tail_summary

    def shape_upper(self, V, T, AA, VT, EE, N, W2, E):
        """Exact true-first-form Gram--Schmidt shape matrix enclosure."""
        I, r = self.I, self.r
        Fg = r.dot(V, T)
        e, f, g = [r.dot(N, vector) for vector in (AA, VT, EE)]
        W = I.sqrt(W2)
        FE = I.div(Fg, E)
        B11 = I.div(e, I.mul(W, E))
        B12 = I.div(I.sub(f, I.mul(FE, e)), W2)
        numerator = I.add(I.sub(g, I.scale(I.mul(FE, f), 2)), I.mul(I.square(FE), e))
        B22 = I.div(I.mul(E, numerator), I.mul(W, W2))
        a, b, d = [I.exact(I.absolute_upper(value)) for value in (B11, B12, B22)]
        majorant = I.scale(I.add(I.add(a, d), I.sqrt(I.add(I.square(I.sub(a, d)),
            I.scale(I.square(b), 4)))), .5)[1]
        trace_abs = I.exact(I.absolute_upper(I.add(B11, B22)))
        signed = I.scale(I.add(trace_abs, I.sqrt(I.add(I.square(I.sub(B11, B22)),
            I.scale(I.square(B12), 4)))), .5)[1]
        return np.minimum(majorant, signed)

    def cell(self, cell, radial):
        if not 0 <= cell < self.r.J-1 or radial < 1 or radial & (radial-1):
            raise ValueError('Use an original cell and positive dyadic radial count')
        started = time.monotonic()
        r, I = self.r, self.I
        best = 0.
        minW2, minE = None, None
        unpaid = 0
        worst = None
        pieces = r._cell_pieces(cell)
        tail_summary = {}
        old = None if self.previous is None else self.previous[cell]
        for piece_index, piece in enumerate(pieces):
            definitions = self.piece_definitions(cell, piece)
            for first, stop, fields, tails in self.field_blocks(definitions, radial):
                for key, value in tails.items():
                    row = tail_summary.setdefault(key, {name: 0. for name in value})
                    for name, bound in value.items():
                        row[name] = max(row[name], bound)
                V, T, AA, VT, EE = [fields[key] for key in ('V', 'T', 'AA', 'VT', 'EE')]
                N = r.cross(T, V)
                E = r.norm2(V)
                W2a = r.norm2(N)
                W2b = I.sub(I.mul(E, r.norm2(T)), I.square(r.dot(V, T)))
                W2 = np.maximum(W2a[0], W2b[0]), np.minimum(W2a[1], W2b[1])
                if old is not None:
                    E = np.maximum(E[0], old['minimum_E_lower']), E[1]
                    W2 = np.maximum(W2[0], old['minimum_normal_squared_lower']), W2[1]
                if np.any(E[0] > E[1]) or np.any(W2[0] > W2[1]):
                    raise ArithmeticError('Two same-field enclosures do not intersect')
                wl, el = float(W2[0].min()), float(E[0].min())
                minW2 = wl if minW2 is None else min(minW2, wl)
                minE = el if minE is None else min(minE, el)
                good = (W2[0] > 0) & (E[0] > 0)
                unpaid += int(np.count_nonzero(~good))
                if not np.any(good):
                    continue
                subset = lambda vector: [I.at(value, good) for value in vector]
                values = self.shape_upper(*[subset(z) for z in (V, T, AA, VT, EE, N)],
                    I.at(W2, good), I.at(E, good))
                index = int(np.argmax(values))
                bound = float(values[index])
                if bound > best:
                    where = np.argwhere(good)[index]
                    best = bound
                    worst = dict(piece=piece_index, radial_subcell=first+int(where[0]),
                        angle_grid_index=int(where[1]), angle_grid_denominator=self.b.angle.Q)
        return dict(cell=cell, angles=self.b.angle.Q, retained_angle_modes=self.b.low_modes,
            radial_subdivisions_per_piece=radial, requested_radial_block=self.radial_block,
            exact_lift_pieces=len(pieces), all_original_points_covered=True,
            unpaid_immersion_boxes=unpaid, minimum_E_lower=minE,
            minimum_normal_squared_lower=minW2, curvature_upper=best if unpaid == 0 else None,
            curvature_bound_certified=unpaid == 0, worst_curvature=worst,
            tail_diagnostics=tail_summary,
            full_original_modes_and_complete_analytic_lift_paid=True,
            actual_first_form_used=True, sampled_a_used_as_geometry=False,
            optional_same_candidate_first_form_lower_bounds_used=old is not None,
            strict_outward_arithmetic=True, seconds=time.monotonic()-started)

    def metadata(self):
        b, r = self.b, self.r
        return dict(J=r.J, M=r.M, exact_S_box=[str(v) for v in r.S_exact],
            exact_R_box=[str(v) for v in r.R_exact], exact_width=str(r.width),
            exact_H=str(b.height_exact), scalar_identity=self.b.d.scalar_identity,
            taylor_degree=b.taylor_degree, phase_l1_upper=b.base_phase_l1,
            rho_absolute_upper=b.rho_upper, rho_prime_absolute_upper=self.rho_prime_abs_upper,
            exponential_remainder_upper=b.taylor_remainder,
            er_laurent_tail_upper=b.er_fourier_tail,
            rhoer_laurent_tail_upper=b.rhoer_fourier_tail,
            second_multiplier_absolute_upper=self.second_multiplier_abs_upper,
            second_laurent_tail_upper=self.second_laurent_tail,
            second_exponential_remainder_upper=self.second_analytic_remainder,
            second_complete_tail_upper=self.second_total_tail,
            complete_second_laurent_degree=self.full_second_laurent_degree,
            expected_full_second_support_size=2*self.full_second_laurent_degree+1,
            optional_first_geometry=self.previous_identity,
            original_polynomial_lift_only=True,
            R671_nonpolynomial_reference_lift_supported=False,
            normal_orientation='F_phi cross F_s', curvature='Absolute eigenvalues of actual Euclidean shape operator')


def parse_levels(value):
    levels = []
    for item in value.split(','):
        numbers = [int(v) for v in item.split(':')]
        if len(numbers) != 3:
            raise argparse.ArgumentTypeError('Levels are angles:radial_subdivisions:retained_modes')
        Q, radial, modes = numbers
        if (Q < 4 or Q & (Q-1) or radial < 1 or radial & (radial-1)
                or modes < 1 or Q <= 4*modes):
            raise argparse.ArgumentTypeError('Use dyadic Q/radial and 0 < retained modes < Q/4')
        levels.append(tuple(numbers))
    if not levels:
        raise argparse.ArgumentTypeError('At least one finite cover level is required')
    return levels


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'work', 'bundle', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    for key in ('node-report', 'carrier', 'first-geometry-source', 'first-geometry-report'):
        parser.add_argument('--'+key, type=Path)
    parser.add_argument('--manifest', type=Path, action='append', default=[])
    parser.add_argument('--cells', default='all')
    parser.add_argument('--levels', type=parse_levels,
        default=parse_levels('256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96'))
    parser.add_argument('--target', default='8.1')
    parser.add_argument('--taylor-degree', type=int, default=12)
    parser.add_argument('--radial-block', type=int, default=4)
    parser.add_argument('--beta', default='1/4')
    a = parser.parse_args()
    source = a.first_geometry_source or (a.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_postprocess.py')
    if sha(source) != FIRST_GEOMETRY_SHA:
        raise ValueError('Use the declared complete R670 exact field and angular remainder source')
    runtime = load('complete_R670_first_geometry', source)
    context = runtime.actions_context()
    a.command = 'curvature'
    runtime.common_paths(a)
    if a.out.exists():
        raise FileExistsError('Use a fresh current-Actions continuous curvature report')
    target = F(a.target)
    if target <= 0 or a.taylor_degree < 1:
        raise ValueError('Positive exact curvature target and Taylor degree required')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic()
    paths = runtime.source_paths(a.repo)
    firstQ, firstRadial, firstModes = a.levels[0]
    base_args = SimpleNamespace(bundle=a.bundle, node_report=a.node_report,
        beta=a.beta, taylor_degree=a.taylor_degree, low_modes=firstModes,
        plan=[(firstQ, firstRadial)])
    base = runtime.make_direct_reader(base_args, paths)
    reader = CurvatureReader(base, radial_block=a.radial_block,
                             first_geometry_report=a.first_geometry_report)
    cells = list(range(reader.r.J-1)) if a.cells == 'all' else sorted(set(int(v) for v in a.cells.split(',')))
    if not cells or cells[0] < 0 or cells[-1] >= reader.r.J-1:
        raise ValueError('Selected original cells are out of range')
    full = cells == list(range(reader.r.J-1))
    lineage = runtime.read_manifest_locations(a)
    report = dict(schema='fullclosed-complete-lowmode-sixjet-curvature-actions-v1',
        execution=context, source_sha256=sha(__file__), first_geometry_source_sha256=sha(source),
        source_inputs={key: dict(path=str(Path(value).resolve()), sha256=sha(value))
                       for key, value in base.paths.items()},
        metadata=reader.metadata(), levels=a.levels, target_exact=str(target),
        selected_cells=cells, covered_original_cells=[], attempts=[], best={},
        complete_scope=False, continuous_curvature_upper=None, target_certified=False,
        supplied_location_manifests=lineage,
        old_candidate_curvature_values_inherited=False, historical_candidate_hash_assumed=False,
        full_closed_embedding_certified=False, reach_certified=False, metric_certified=False,
        scope='Only this Actions run actual original fullclosed model; no R671 nonpolynomial lift',
        arithmetic='f512 nextafter outward binary64; exact rational controls and all finite/Laurent/Taylor tails')
    best = {}
    for level, (Q, radial, modes) in enumerate(a.levels):
        pending = [cell for cell in cells if cell not in best or F(best[cell]['curvature_upper']) > target]
        if not pending:
            break
        reader.set_resolution(Q, modes)
        runtime.announce(event='lowmode_curvature_level_start', level=level, angles=Q,
            radial_subdivisions=radial, retained_angle_modes=modes, pending=len(pending),
            seconds=time.monotonic()-started)
        for count, cell in enumerate(pending, 1):
            value = reader.cell(cell, radial)
            value['level'] = level
            report['attempts'].append(value)
            if value['curvature_bound_certified'] and (cell not in best
                    or value['curvature_upper'] < best[cell]['curvature_upper']):
                best[cell] = value
            if count % 32 == 0 or count == len(pending):
                report.update(best={str(k): v for k, v in best.items()},
                    covered_original_cells=sorted(best), seconds=time.monotonic()-started,
                    peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                    maximum_transform_group_entries=reader.maximum_transform_group_entries,
                    target_paid_cell_count=sum(F(v['curvature_upper']) <= target for v in best.values()))
                runtime.write_json(a.out, report)
                runtime.announce(event='lowmode_curvature_progress', level=level,
                    completed_in_level=count, total_in_level=len(pending),
                    cells_with_valid_bound=len(best), target_paid=report['target_paid_cell_count'],
                    maximum_valid_bound=max((v['curvature_upper'] for v in best.values()), default=None),
                    seconds=report['seconds'])
    complete_selected = sorted(best) == cells
    complete_closed = bool(full and complete_selected)
    maximum = max((v['curvature_upper'] for v in best.values()), default=None)
    remaining = [cell for cell in cells if cell not in best or F(best[cell]['curvature_upper']) > target]
    marker_hypotheses = base.height_exact > 1 and reader.r.R_exact[0] > F(9, 20)
    core_rho_lower = float(base.rho[0].min())
    cuff_rho_lower = None
    if reader.r.J-2 in best:
        # At the exact cuff W^2=R^2*rho^2.  A strict complete cuff-cell
        # lower bound forbids zeros of continuous rho; its mean is 1,
        # so the nonzero sign is positive on the whole angular circle.
        I = reader.I
        cuff_rho_lower = float(I.div(I.sqrt(I.exact(
            best[reader.r.J-2]['minimum_normal_squared_lower'])), reader.r.R)[0])
        core_rho_lower = max(core_rho_lower, cuff_rho_lower)
    report.update(best={str(k): v for k, v in best.items()}, covered_original_cells=sorted(best),
        complete_selected_scope=complete_selected, complete_scope=complete_closed,
        continuous_curvature_upper=maximum if complete_closed else None,
        selected_scope_curvature_upper=maximum if complete_selected else None,
        flat_caps_curvature_upper=0., mirror_and_activity_phases_preserve_absolute_curvature=True,
        full_closed_immersion_certified=complete_closed,
        target_certified=bool(complete_closed and not remaining), remaining_above_target=remaining,
        new_core_rho_lower=core_rho_lower, core_rho_lower_from_cuff_area=cuff_rho_lower,
        conditional_four_p4_marker_curvature_upper=max(maximum, 5.) if complete_closed and marker_hypotheses else None,
        manifest_positions_covered_by_full_continuous_domain=complete_closed,
        full_closed_embedding_certified=False, reach_certified=False, metric_certified=False,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        maximum_transform_group_entries=reader.maximum_transform_group_entries,
        seconds=time.monotonic()-started)
    runtime.write_json(a.out, report)
    runtime.announce(event='lowmode_curvature_cover_returned', report_sha256=sha(a.out),
        complete_scope=complete_closed, continuous_curvature_upper=report['continuous_curvature_upper'],
        target_certified=report['target_certified'], remaining_above_target=len(remaining),
        seconds=time.monotonic()-started)


if __name__ == '__main__':
    main()
