#!/usr/bin/env python3
"""Actions-only batched continuous curvature for polynomial and R671 fields.

Each scientific task covers one exact lift piece and a short, explicit
dyadic radial range, at every angle.  The proven R670/R672/R674 formulas
are retained.  Tasks return naturally; a finite admission budget never
kills an admitted task.  Complete block returns stay in a runner-local
journal, while --out contains only uniform bounds on named cell domains.

No scientific work runs on import.  Run this CLI only in this public
repository's Actions.  This program does not certify the target metric,
embedding, reach, noncongruence, or fixed-metric convergence.
"""
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace
import argparse
import hashlib
import importlib.util
import json
import math
import multiprocessing
import os
import resource
import sys
import time
import traceback

import numpy as np


SCHEMA = 'complete-curvature-batched-uniform-cover-v1'
JOURNAL_SCHEMA = 'complete-curvature-radial-block-journal-v1'
RETURN_SCHEMA = 'complete-curvature-radial-block-return-v1'
FAILURE_SCHEMA = 'complete-curvature-radial-block-failure-v1'
FIRST_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'
CURVATURE_SHA = '8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385'
REFERENCE_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
_WORKER = None


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            result.update(block)
    return result.hexdigest()


def load(name, path, expected):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('Changed declared mathematical source: '+str(path))
    name = '_batched_curvature_'+name+'_'+expected[:16]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp-'+str(os.getpid()))
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def announce(**value):
    print(json.dumps(value, allow_nan=False), flush=True)


def ranges(values):
    values = sorted(set(values))
    result = []
    for value in values:
        if not result or value != result[-1][1]+1:
            result.append([value, value])
        else:
            result[-1][1] = value
    return ','.join(str(lo) if lo == hi else str(lo)+'-'+str(hi) for lo, hi in result)


def parse_cells(value, count):
    if value == 'all':
        return list(range(count))
    result = set()
    for part in value.split(','):
        endpoints = [int(x) for x in part.split('-')]
        if len(endpoints) == 1:
            lo = hi = endpoints[0]
        elif len(endpoints) == 2:
            lo, hi = endpoints
        else:
            raise ValueError('Cells must be single indices or inclusive ranges')
        if not 0 <= lo <= hi < count:
            raise ValueError('Selected cells are outside the actual original domain')
        result.update(range(lo, hi+1))
    if not result:
        raise ValueError('At least one original cell is required')
    return sorted(result)


def parse_levels(value):
    result = []
    for item in value.split(','):
        pieces = item.split(':')
        if len(pieces) != 3:
            raise argparse.ArgumentTypeError('Use angles:radial:retained_modes')
        q, radial, modes = (int(v) for v in pieces)
        if (q < 4 or q & (q-1) or radial < 1 or radial & (radial-1)
                or modes < 1 or q <= 4*modes):
            raise argparse.ArgumentTypeError('Use dyadic angles/radial and 0 < modes < angles/4')
        result.append((q, radial, modes))
    if not result:
        raise argparse.ArgumentTypeError('At least one declared cover level is required')
    return result


def outside(path, repo):
    path = Path(path).resolve()
    try:
        path.relative_to(repo)
    except ValueError:
        return path
    raise ValueError('Scientific journal and outputs must stay outside the repository')


class Worker:
    def __init__(self, args):
        source = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
        self.runtime = load('first', source/'actions_closed_postprocess.py', FIRST_SHA)
        self.execution = self.runtime.actions_context()
        self.kernel = load('curvature', source/'actions_closed_curvature.py', CURVATURE_SHA)
        with np.load(args.bundle, allow_pickle=False) as data:
            canonical_reference = 'reference_tail_model_json' in data.files
            nonzero_tags = [key for key in ('reference_tail_lambda', 'exact_tail_lambda')
                            if key in data.files and F(float(data[key].item())) != 0]
            # Canonical writers may preserve both matching lambda tags.
            # The frozen R674 reader below checks the model, mandatory
            # reference tag, every optional tag and all input identities.
            if nonzero_tags and not canonical_reference:
                raise ValueError('Use a canonical supported field, not an unrecognized nonzero lift')
        if args.model == 'auto':
            self.kind = 'reference' if canonical_reference else 'polynomial'
        else:
            self.kind = args.model
        if self.kind == 'polynomial' and canonical_reference:
            raise ValueError('A tagged reference bundle must use its canonical R671 reader')
        q, radial, modes = args.levels[0]
        if self.kind == 'reference':
            if args.scalar_input is None:
                raise ValueError('The canonical reference field requires its original scalar input')
            ref = load('reference', source/'exact_reference_tail_interval.py', REFERENCE_SHA)
            self.reader = ref.ReferenceIntervalReader(repo=args.repo, bundle=args.bundle,
                node_report=args.node_report, scalar_input=args.scalar_input,
                reference_carrier=args.reference_carrier, angles=q, low_modes=modes,
                angular_taylor_degree=args.taylor_degree, scalar_degree=args.scalar_degree,
                radial_block=args.radial_block, panels=args.panels, beta=args.beta,
                first_geometry_report=args.first_geometry_report)
            self.base = self.reader.b
            self.curvature = self.reader.curvature
            self.input_paths = dict(self.base.paths, **self.reader.paths)
            self.model_definition = self.reader.model
            # Before eta the canonical field is exactly the polynomial field.
            # evaluate() still reads only this R671 reader's validated same-field
            # first-form bounds.  No R671 report is disguised as old R670 output.
        else:
            paths = self.runtime.source_paths(args.repo)
            request = SimpleNamespace(bundle=args.bundle, node_report=args.node_report,
                beta=args.beta, taylor_degree=args.taylor_degree, low_modes=modes,
                plan=[(q, radial)])
            self.base = self.runtime.make_direct_reader(request, paths)
            self.curvature = self.kernel.CurvatureReader(self.base,
                radial_block=args.radial_block, first_geometry_report=args.first_geometry_report)
            self.reader = self.curvature
            self.input_paths = dict(self.base.paths)
            self.model_definition = {'schema':'original-polynomial-lift'}
        self.input_paths.update(first_source=source/'actions_closed_postprocess.py',
            curvature_source=source/'actions_closed_curvature.py')
        if self.kind == 'reference':
            self.input_paths['reference_interval_source'] = source/'exact_reference_tail_interval.py'
        if args.first_geometry_report is not None:
            self.input_paths['first_geometry_report'] = args.first_geometry_report
        self.r, self.I = self.base.r, self.base.I
        self.block_limit = args.radial_block
        self._definition_cache = None
        self.binding = dict(model_kind=self.kind,
            inputs_sha256={key:sha(path) for key, path in self.input_paths.items()},
            model_definition=self.model_definition,
            J=self.r.J, M=self.r.M,
            exact_S_box=[str(v) for v in self.r.S_exact],
            exact_R_box=[str(v) for v in self.r.R_exact],
            exact_H=str(self.base.height_exact), exact_width=str(self.r.width),
            taylor_degree=args.taylor_degree, scalar_degree=args.scalar_degree,
            panels=args.panels, beta_exact=str(F(args.beta)), radial_block=args.radial_block)
        self.binding_sha = digest(self.binding)
        if any(modes > self.r.M for _, _, modes in args.levels):
            raise ValueError('Retained modes exceed the actual complete field bandwidth')

    def polynomial_on(self, cell):
        return self.kind == 'polynomial' or self.reader._old_formula_applies(cell)

    def pieces(self, cell):
        return (self.r._cell_pieces(cell) if self.polynomial_on(cell)
                else self.reader.pieces(cell))

    def tasks(self, cell, spec):
        q, radial, modes = spec
        degree = 6 if self.polynomial_on(cell) else self.reader.degree
        block = min(self.block_limit, max(1, (1 << 20)//(8*(degree+1)*q)))
        return [dict(cell=cell, piece=piece, angles=q, radial=radial, modes=modes,
            start=first, stop=min(radial, first+block),
            piece_kernel='polynomial' if self.polynomial_on(cell) else 'reference')
            for piece in range(len(self.pieces(cell))) for first in range(0, radial, block)]

    def polynomial_fields(self, task):
        """R672 coefficient/tail formulas, restricted to the named radial block.

        A direct exact-rational Bernstein restriction replaces creation of
        every radial subcell.  Each selected interval is still [j/r,(j+1)/r]
        in the SAME exact lift piece, and every angular tail is retained.
        """
        r, I, b, c = self.r, self.I, self.base, self.curvature
        key = task['cell'], task['piece']
        if self._definition_cache is None or self._definition_cache[0] != key:
            piece = r._cell_pieces(task['cell'])[task['piece']]
            self._definition_cache = key, c.piece_definitions(task['cell'], piece)
        definitions = self._definition_cache[1]
        lefts = range(task['start'], task['stop'])
        restrictions = [(r.fraction(F(j, task['radial'])),
                         r.fraction(F(j+1, task['radial']))) for j in lefts]
        groups, losses, addresses = ({'cos':[], 'sin':[]} for _ in range(3))
        fields = {name:[None, None, None] for name in definitions}
        L = b.low_modes
        for name, (channels, parities, scalar, remainder) in definitions.items():
            scalar_parts = I.stack([r.restrict(scalar, u, v) for u, v in restrictions])
            analytic = I.mul(I.exact(I.absolute_upper(scalar_parts)), I.exact(remainder))[1]
            for k, (component, parity) in enumerate(zip(channels, parities)):
                part = I.stack([r.restrict(component, u, v) for u, v in restrictions])
                high = I.sum_upper(I.absolute_upper(I.at(part, (..., slice(L+1, None)))), axis=-1)
                extra = analytic if k < 2 else np.zeros_like(high)
                loss = I.add(I.exact(high), I.exact(extra))[1]
                groups[parity].append(I.at(part, (..., slice(0, L+1))))
                losses[parity].append(loss)
                addresses[parity].append((name, k))
        for parity in ('cos', 'sin'):
            if not groups[parity]:
                continue
            values = b.angle.angle_boxes(I.stack(groups[parity]), parity)
            loss = np.asarray(losses[parity])[..., None]
            values = I.down(values[0]-loss), I.up(values[1]+loss)
            for j, (name, k) in enumerate(addresses[parity]):
                fields[name][k] = values[0][j].min(axis=-2), values[1][j].max(axis=-2)
        return fields

    def evaluate(self, task):
        started = time.monotonic()
        q, modes = task['angles'], task['modes']
        self.reader.set_resolution(q, modes)
        cell, part = task['cell'], task['piece']
        if task['piece_kernel'] != ('polynomial' if self.polynomial_on(cell) else 'reference'):
            raise ValueError('Task piece kernel differs from the exact current model')
        if self.polynomial_on(cell):
            fields = self.polynomial_fields(task)
        else:
            piece = self.reader.pieces(cell)[part]
            subpieces = [self.reader.subpiece(cell, piece, j, task['radial'])
                         for j in range(task['start'], task['stop'])]
            made = [self.reader.piece_definitions(cell, sub, 'curvature') for sub in subpieces]
            fields, _ = self.reader._field_batch([value[0] for value in made])
        r, I = self.r, self.I
        V, T = fields['V'], fields['T']
        N, E = r.cross(T, V), r.norm2(V)
        wa = r.norm2(N)
        wb = I.sub(I.mul(E, r.norm2(T)), I.square(r.dot(V, T)))
        W2 = np.maximum(wa[0], wb[0]), np.minimum(wa[1], wb[1])
        previous = self.reader.previous
        if previous is not None:
            E = np.maximum(E[0], previous[cell]['minimum_E_lower']), E[1]
            W2 = np.maximum(W2[0], previous[cell]['minimum_normal_squared_lower']), W2[1]
        if np.any(E[0] > E[1]) or np.any(W2[0] > W2[1]):
            raise ArithmeticError('Two valid same-field first-form intervals do not intersect')
        good = (E[0] > 0) & (W2[0] > 0)
        unpaid = int(np.count_nonzero(~good))
        K, worst = None, None
        if np.any(good):
            sub = lambda v:[I.at(x, good) for x in v]
            values = self.curvature.shape_upper(
                *[sub(fields[name]) for name in ('V', 'T', 'AA', 'VT', 'EE')],
                sub(N), I.at(W2, good), I.at(E, good))
            j = int(np.argmax(values))
            at = np.argwhere(good)[j]
            K = float(values[j]) if unpaid == 0 else None
            worst = dict(radial_subcell=task['start']+int(at[0]), angle_grid_index=int(at[1]),
                         angle_grid_denominator=q)
        record = dict(task=task, curvature_upper=K,
            minimum_E_lower=float(E[0].min()), minimum_normal_squared_lower=float(W2[0].min()),
            unpaid_immersion_boxes=unpaid, curvature_bound_certified=K is not None,
            worst_curvature=worst, seconds=time.monotonic()-started,
            worker_peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            every_angle_covered=True, exact_declared_radial_block_covered=True,
            all_original_modes_and_complete_analytic_tail_paid=True,
            actual_Euclidean_shape_operator=True, strict_outward_arithmetic=True)
        if K is not None and (not math.isfinite(K) or K < 0
                or record['minimum_E_lower'] <= 0 or record['minimum_normal_squared_lower'] <= 0):
            raise ArithmeticError('Invalid finite curvature return')
        canonical(record)
        return record


def evaluate_task(task):
    return _WORKER.evaluate(task)


class Schedule:
    def __init__(self, args, worker, started):
        self.args, self.worker, self.started = args, worker, started
        self.producer_sha = sha(__file__)
        self.target = F(args.target)
        self.selected = parse_cells(args.cells, worker.r.J-1)
        self.records, self.actual_hashes, self.errors = {}, {}, []
        self.failed_tasks = {}
        self.cell_covers, self.best = {}, {}
        self.new_blocks, self.new_seconds = 0, 0.
        self.last_checkpoint_blocks = 0
        self.state = 'initialized'
        self.active_tasks = []
        self.journal = args.journal
        header = self.journal/'header.json'
        if header.exists():
            if not args.resume:
                raise FileExistsError('Explicit --resume is required to consume this real local journal')
            old = json.loads(header.read_text())
            if (old.get('schema') != JOURNAL_SCHEMA
                    or old.get('producer_sha256') != self.producer_sha
                    or old.get('field_binding_sha256') != worker.binding_sha
                    or old.get('field_binding') != worker.binding
                    or old.get('execution', {}).get('GITHUB_RUN_ID') != worker.execution.get('GITHUB_RUN_ID')
                    or old.get('execution', {}).get('GITHUB_REPOSITORY') != worker.execution.get('GITHUB_REPOSITORY')):
                raise ValueError('Journal is not from this producer and actual same-field Actions run')
            for path in sorted((self.journal/'returns').glob('*.json')):
                value = json.loads(path.read_text())
                self.admit_return(value, path, new=False)
            for path in sorted((self.journal/'failures').glob('*.json')):
                value = json.loads(path.read_text())
                task = value.get('task')
                key = digest(task)
                if (value.get('schema') != FAILURE_SCHEMA or value.get('producer_sha256') != self.producer_sha
                        or value.get('field_binding_sha256') != worker.binding_sha or path.stem != key):
                    raise ValueError('A prior failed task has different source or field provenance')
                if key in self.records:
                    raise ValueError('A task has both a successful raw return and an exception record')
                if task not in worker.tasks(task['cell'], (task['angles'], task['radial'], task['modes'])):
                    raise ValueError('A failed task has an invalid exact domain')
                self.failed_tasks[key] = value
        else:
            if args.resume:
                raise FileNotFoundError('The declared scratch journal does not exist')
            write_json(header, dict(schema=JOURNAL_SCHEMA, producer_sha256=self.producer_sha,
                field_binding_sha256=worker.binding_sha, field_binding=worker.binding,
                execution=worker.execution,
                scope='Runner-local complete bounded-block returns; never publish this raw journal'))
        self.header_sha = sha(header)
        self.reused_blocks = len(self.records)

    def admit_return(self, value, path, *, new):
        if (value.get('schema') != RETURN_SCHEMA or value.get('producer_sha256') != self.producer_sha
                or value.get('field_binding_sha256') != self.worker.binding_sha):
            raise ValueError('A block return has different field/source provenance')
        row = value['record']
        task = row['task']
        spec = task['angles'], task['radial'], task['modes']
        key = digest(task)
        address = task['cell'], spec
        if address not in self.cell_covers:
            expected = {digest(t):t for t in self.worker.tasks(task['cell'], spec)}
            self.cell_covers[address] = dict(expected=expected, returned=set(),
                valid=True, K=None, E=None, W2=None)
        cover = self.cell_covers[address]
        if cover['expected'].get(key) != task:
            raise ValueError('Block address differs from the exact complete declared partition')
        if path.stem != key:
            raise ValueError('Immutable block filename does not match its exact task')
        if key in self.records:
            raise ValueError('Duplicate immutable return')
        if not all(row.get(k) is True for k in ('every_angle_covered',
                'exact_declared_radial_block_covered', 'all_original_modes_and_complete_analytic_tail_paid',
                'actual_Euclidean_shape_operator', 'strict_outward_arithmetic')):
            raise ValueError('Block lacks the complete mathematical scope')
        K = row.get('curvature_upper')
        if row.get('curvature_bound_certified') is not (K is not None):
            raise ValueError('Curvature-return flag and bound disagree')
        if K is not None and (not math.isfinite(K) or K < 0 or row['unpaid_immersion_boxes'] != 0
                or row['minimum_E_lower'] <= 0 or row['minimum_normal_squared_lower'] <= 0):
            raise ValueError('Block bound lacks finite curvature or positive first form')
        self.records[key] = row
        self.actual_hashes[key] = sha(path)
        cover['returned'].add(key)
        if K is None:
            cover['valid'] = False
        else:
            values = dict(K=F(K), E=F(row['minimum_E_lower']), W2=F(row['minimum_normal_squared_lower']))
            for field, number in values.items():
                operation = max if field == 'K' else min
                cover[field] = number if cover[field] is None else operation(cover[field], number)
        if cover['valid'] and cover['returned'] == set(cover['expected']):
            cell = task['cell']
            if cell not in self.best:
                self.best[cell] = {field:cover[field] for field in ('K', 'E', 'W2')}
            else:
                for field in ('K', 'E', 'W2'):
                    operation = min if field == 'K' else max
                    self.best[cell][field] = operation(self.best[cell][field], cover[field])
        if new:
            self.new_blocks += 1
            self.new_seconds += row['seconds']

    def save_return(self, row):
        key = digest(row['task'])
        path = self.journal/'returns'/(key+'.json')
        if path.exists():
            raise FileExistsError('Never replace an actual complete block return')
        value = dict(schema=RETURN_SCHEMA, producer_sha256=self.producer_sha,
            field_binding_sha256=self.worker.binding_sha, execution=self.worker.execution, record=row)
        write_json(path, value)
        self.admit_return(value, path, new=True)

    def save_failure(self, task, error, detail=None):
        key = digest(task)
        path = self.journal/'failures'/(key+'.json')
        value = dict(schema=FAILURE_SCHEMA, producer_sha256=self.producer_sha,
            field_binding_sha256=self.worker.binding_sha, execution=self.worker.execution,
            task=task, error=repr(error), traceback=detail,
            scope='No curvature bound was returned; this exact configuration is not silently retried',
            unreturned_worker_cost_is_not_assumed_zero=True)
        if path.exists():
            raise FileExistsError('Never replace a recorded failed task')
        write_json(path, value)
        self.failed_tasks[key] = value
        self.errors.append(dict(task=task, error=repr(error), traceback=detail))

    def best_cells(self):
        return self.best

    def compact(self):
        best = self.best_cells()
        valid = sorted(best)
        paid = [i for i in valid if best[i]['K'] <= self.target]
        expected = list(range(self.worker.r.J-1))
        missing = sorted(set(expected)-set(valid))
        above = sorted(set(valid)-set(paid))
        complete = valid == expected
        def cover(cells):
            if not cells:
                return dict(cell_ranges='', cell_count=0, curvature_upper_exact=None,
                    minimum_E_lower_exact=None, minimum_W2_lower_exact=None)
            return dict(cell_ranges=ranges(cells), cell_count=len(cells),
                curvature_upper_exact=str(max(best[i]['K'] for i in cells)),
                minimum_E_lower_exact=str(min(best[i]['E'] for i in cells)),
                minimum_W2_lower_exact=str(min(best[i]['W2'] for i in cells)))
        domains = dict(valid_domain=cover(valid), target_paid_domain=cover(paid))
        maximum = max((v['K'] for v in best.values()), default=None)
        cuff = best.get(self.worker.r.J-2)
        rho = None
        if cuff is not None:
            squared = cuff['W2']/self.worker.r.R_exact[1]**2
            unit = 1 << 80
            rho = F(math.isqrt((squared.numerator*unit*unit)//squared.denominator), unit)
        current = len(self.records)
        source_hashes = self.worker.binding['inputs_sha256']
        marker = self.worker.base.height_exact > 1 and self.worker.r.R_exact[0] > F(9, 20)
        result = dict(schema=SCHEMA, producer_sha256=self.producer_sha,
            kernel_source_sha256=CURVATURE_SHA,
            reference_kernel_source_sha256=REFERENCE_SHA if self.worker.kind == 'reference' else None,
            first_geometry_source_sha256=FIRST_SHA,
            execution=self.worker.execution, field_binding_sha256=self.worker.binding_sha,
            model_kind=self.worker.kind, model_definition_json=canonical(self.worker.model_definition),
            bundle_sha256=source_hashes['bundle'], node_report_sha256=source_hashes['node_report'],
            source_and_input_sha256_json=canonical(source_hashes),
            exact_R_box_json=canonical([str(v) for v in self.worker.r.R_exact]),
            exact_H=str(self.worker.base.height_exact), exact_width=str(self.worker.r.width),
            J=self.worker.r.J, M=self.worker.r.M,
            requested_levels=self.args.levels, target_exact=str(self.target),
            angular_taylor_degree=self.args.taylor_degree, scalar_degree=self.args.scalar_degree,
            panels=self.args.panels, beta_exact=str(F(self.args.beta)),
            requested_radial_block=self.args.radial_block, workers=self.args.workers,
            budget_seconds=self.args.budget_seconds, state=self.state,
            valid_cell_ranges=ranges(valid), target_paid_cell_ranges=ranges(paid),
            uncovered_cell_ranges=ranges(missing), above_target_cell_ranges=ranges(above),
            valid_cell_count=len(valid), target_paid_cell_count=len(paid), expected_cell_count=len(expected),
            selected_cell_ranges=ranges(self.selected),
            selected_target_paid=all(i in paid for i in self.selected),
            complete_scope=complete, full_closed_immersion_certified=complete,
            covered_scope_curvature_upper_exact=None if maximum is None else str(maximum),
            continuous_curvature_upper_exact=str(maximum) if complete else None,
            continuous_curvature_upper=float(maximum) if complete else None,
            target_certified=complete and len(paid) == len(expected),
            uniform_domains=domains,
            uniform_domains_json=canonical(domains),
            core_rho_lower_from_cuff_area_exact=None if rho is None else str(rho),
            conditional_four_p4_marker_curvature_upper_exact=
                str(max(maximum, F(5))) if complete and marker else None,
            flat_caps_curvature_upper=0., mirror_and_activity_phases_preserve_absolute_curvature=True,
            current_invocation_new_complete_blocks=self.new_blocks,
            current_invocation_worker_seconds_sum=self.new_seconds,
            reused_complete_blocks=self.reused_blocks, total_complete_blocks=current,
            journal_header_sha256=self.header_sha,
            journal_return_manifest_sha256=digest(self.actual_hashes),
            active_task_count=len(self.active_tasks), active_tasks=self.active_tasks,
            actual_error_count=len(self.errors), errors=self.errors,
            recorded_failed_block_count=len(self.failed_tasks),
            failed_blocks_are_unpaid_and_not_silently_retried=True,
            parent_peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            maximum_worker_peak_rss_kib=max((v['worker_peak_rss_kib'] for v in self.records.values()), default=None),
            maximum_worker_rss_is_not_simultaneous_total=True,
            seconds=time.monotonic()-self.started,
            embedding_certified=False, reach_certified=False, metric_certified=False,
            fixed_metric_refinement_certified=False, topic_completion_certified=False,
            all_original_modes_and_complete_analytic_lift_paid=True,
            raw_returns_published=False, compact_cross_job_import_implemented=False,
            scope='Uniform bounds apply only to the explicit complete original-cell domains; partial blocks remain runner-local')
        return result

    def checkpoint(self):
        result = self.compact()
        write_json(self.args.out, result)
        self.last_checkpoint_blocks = self.new_blocks
        announce(event='batched_curvature_checkpoint', state=self.state,
            complete_blocks=result['total_complete_blocks'], valid_cells=result['valid_cell_count'],
            target_paid_cells=result['target_paid_cell_count'], complete_scope=result['complete_scope'],
            continuous_curvature_upper=result['continuous_curvature_upper'],
            target_certified=result['target_certified'], seconds=result['seconds'],
            report_sha256=sha(self.args.out))
        return result

    def run(self):
        deadline = self.started+self.args.budget_seconds if self.args.budget_seconds > 0 else math.inf
        self.state = 'running'
        self.checkpoint()
        pool = ProcessPoolExecutor(max_workers=self.args.workers,
            mp_context=multiprocessing.get_context('fork'))
        stop = False
        try:
            for level, spec in enumerate(self.args.levels):
                best = self.best_cells()
                pending_cells = [c for c in self.selected if c not in best or best[c]['K'] > self.target]
                tasks = [task for cell in pending_cells for task in self.worker.tasks(cell, spec)
                         if digest(task) not in self.records and digest(task) not in self.failed_tasks]
                if not tasks:
                    continue
                announce(event='batched_curvature_level', level=level, angles=spec[0], radial=spec[1],
                    retained_modes=spec[2], pending_original_cells=len(pending_cells),
                    pending_bounded_blocks=len(tasks), seconds=time.monotonic()-self.started)
                cursor, futures = 0, {}
                while cursor < len(tasks) or futures:
                    while (not stop and cursor < len(tasks) and len(futures) < self.args.workers
                           and time.monotonic() < deadline):
                        task = tasks[cursor]
                        futures[pool.submit(evaluate_task, task)] = task
                        cursor += 1
                    if time.monotonic() >= deadline:
                        stop = True
                        self.state = 'budget_checkpoint'
                    self.active_tasks = list(futures.values())
                    if not futures:
                        break
                    done, _ = wait(futures, timeout=5., return_when=FIRST_COMPLETED)
                    if not done:
                        continue
                    for future in done:
                        task = futures.pop(future)
                        try:
                            self.save_return(future.result())
                        except Exception as error:
                            self.save_failure(task, error, traceback.format_exc())
                            self.state, stop = 'failed', True
                    self.active_tasks = list(futures.values())
                    if (self.new_blocks-self.last_checkpoint_blocks >= self.args.checkpoint_blocks
                            or not futures or self.errors):
                        self.checkpoint()
                    if self.errors:
                        # Already admitted scientific blocks still return naturally.
                        for future, task in list(futures.items()):
                            try:
                                self.save_return(future.result())
                            except Exception as error:
                                self.save_failure(task, error, traceback.format_exc())
                            futures.pop(future)
                        self.active_tasks = []
                        break
                if stop:
                    break
            if self.state != 'failed':
                summary = self.compact()
                if summary['target_certified']:
                    self.state = 'completed'
                elif summary['selected_target_paid']:
                    self.state = 'selected_targets_paid'
                elif not stop:
                    self.state = 'declared_plan_exhausted'
            self.active_tasks = []
            return self.checkpoint()
        finally:
            pool.shutdown(wait=True, cancel_futures=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'node-report', 'journal', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    for key in ('scalar-input', 'reference-carrier', 'first-geometry-report'):
        parser.add_argument('--'+key, type=Path)
    parser.add_argument('--model', choices=('auto', 'polynomial', 'reference'), default='auto')
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--cells', default='all')
    parser.add_argument('--levels', type=parse_levels,
        default=parse_levels('256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96'))
    parser.add_argument('--target', default='81/10')
    parser.add_argument('--taylor-degree', type=int, default=12)
    parser.add_argument('--scalar-degree', type=int, default=5)
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--radial-block', type=int, default=4)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--budget-seconds', type=float, default=600.)
    parser.add_argument('--checkpoint-blocks', type=int, default=16)
    parser.add_argument('--beta', default='1/4')
    args = parser.parse_args()
    args.repo = args.repo.resolve()
    args.bundle, args.node_report = args.bundle.resolve(), args.node_report.resolve()
    args.out, args.journal = outside(args.out, args.repo), outside(args.journal, args.repo)
    if args.out.exists():
        raise FileExistsError('Use a fresh compact output for this actual invocation')
    if (F(args.target) <= 0 or not F(0) < F(args.beta) <= F(1)
            or args.taylor_degree < 1 or not 3 <= args.scalar_degree <= 8
            or args.panels < 1 or args.radial_block < 1 or args.workers < 1
            or args.budget_seconds < 0 or args.checkpoint_blocks < 1):
        raise ValueError('Invalid positive bound, Taylor/scalar parameters or admission budget')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic()
    global _WORKER
    _WORKER = Worker(args)
    schedule = Schedule(args, _WORKER, started)
    result = schedule.run()
    announce(event='batched_curvature_returned', state=result['state'], report_sha256=sha(args.out),
        field_binding_sha256=result['field_binding_sha256'], new_blocks=result['current_invocation_new_complete_blocks'],
        reused_blocks=result['reused_complete_blocks'], complete_scope=result['complete_scope'],
        target_certified=result['target_certified'], research_complete=False)
    if result['state'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
