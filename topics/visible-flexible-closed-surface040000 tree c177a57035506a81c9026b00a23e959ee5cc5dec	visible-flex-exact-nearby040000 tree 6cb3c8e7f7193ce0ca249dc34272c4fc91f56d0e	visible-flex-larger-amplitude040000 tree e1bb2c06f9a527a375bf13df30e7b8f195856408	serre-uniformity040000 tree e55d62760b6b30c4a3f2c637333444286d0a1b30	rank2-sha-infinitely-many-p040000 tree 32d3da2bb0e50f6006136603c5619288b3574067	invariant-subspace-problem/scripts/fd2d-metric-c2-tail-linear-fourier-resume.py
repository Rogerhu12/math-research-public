#!/usr/bin/env python3
"""Resume proved tail cells; use Fourier absolute sums before angular subdivision.

The unchanged continuous consumer defines the geometry and linear strain.
Each row covers its full exact radial box and all angular modes. Old bounds
are reused only for the identical reconstructed box and defining inputs.
Every new row is a closed gzip member; a stop file is checked at box edges.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time

HERE = Path(__file__).resolve().parent


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE/filename)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


E = module('fd2d_resumed_tail_engine', 'fd2d-metric-c2-tail-linear-continuous.py')
normal = module('fd2d_resumed_tail_normal', 'fd2d-metric-normal-interval-arithmetic.py')
NORMAL_POLICY = normal.install(E.poly, narrow_owner=E.linear)
original_packet = E.stream.frozen.load_packet


def materialized_packet(*args, **kwargs):
    meta, archive, path = original_packet(*args, **kwargs)
    arrays = {name: archive[name].copy() for name in archive.files}
    archive.close()
    return meta, arrays, path


E.stream.frozen.load_packet = materialized_packet


class Tail(E.Tail):
    def bound(self, left, right, angular):
        main, noise, r, frame, packet_row, span = self.polynomials(left, right)
        radius = E.linear.range_poly(r)
        if radius.lo <= 0 or frame.lo <= 0:
            raise ValueError('Nonpositive target frame')
        def whole_angle(p):
            c = E.linear.coefficient_ranges(p)
            remainder = E.poly.positive_sum_upper(c[0, 1:].abs().hi)
            return c[0, 0]+E.I(-remainder, remainder)
        values = [whole_angle(p)+whole_angle(q) for p, q in zip(main, noise)]
        upper = E.linear.matrix_norm(values[0]/frame,
                                     values[1]/(radius*frame.sqrt()),
                                     values[2]/radius.square())
        self.last_fourier_l1_upper = upper
        if upper <= self.quick_threshold:
            self.last_angular_method = 'complete Fourier absolute-coefficient sum'
            return upper, packet_row, span
        self.last_angular_method = 'complete continuous angular arcs after Fourier bound'
        return super().bound(left, right, angular)

    def polynomials(self, left, right):
        key = (left, right)
        if getattr(self, '_cached_polynomial_key', None) != key:
            self._cached_polynomial = super().polynomials(left, right)
            self._cached_polynomial_key = key
        return self._cached_polynomial


def identity(path):
    return E.identity(Path(path))


def read_prior(path, args, model):
    if path is None:
        return {}, None
    events = [json.loads(line) for line in gzip.decompress(path.read_bytes()).decode().splitlines()]
    starts = [row for row in events if row['stage'] == 'start']
    if len(starts) != 1:
        raise ValueError('A single original computation header is required')
    header = starts[0]
    if header['engine_sha256'] != identity(HERE/'fd2d-metric-c2-tail-linear-continuous.py')['sha256']:
        raise ValueError('Changed original mathematical engine')
    argv = header['argv']
    def option(name, default=None):
        return argv[argv.index('--'+name)+1] if '--'+name in argv else default
    bindings = {}
    for name in ('manifest', 'packet', 'field'):
        recorded = Path(option(name))
        requested = getattr(args, name)
        if recorded.resolve() != requested.resolve():
            raise ValueError('Original checkpoint names another defining '+name)
        bindings[name] = identity(requested)
    if int(option('start', 0)) != 0 or int(option('radial-subdivisions', 1)) != args.radial_subdivisions:
        raise ValueError('Unsupported original selected radial partition')
    models = [row for row in events if row['stage'] == 'tail_model_done']
    if len(models) != 1 or models[0]['radial_cells'] != len(model.mesh)-1:
        raise ValueError('Original exact mesh has a different size')
    rows = {}
    for row in events:
        if row['stage'] != 'cell_done':
            continue
        ordinal = row['ordinal']
        if ordinal != len(rows)+1:
            raise ValueError('Original completed boxes are not a contiguous ordered prefix')
        cell, sub = divmod(ordinal-1, args.radial_subdivisions)
        if cell >= len(model.mesh)-1:
            raise ValueError('Original cell is outside the actual field domain')
        a, b = model.mesh[cell:cell+2]
        left = a+(b-a)*Q(sub, args.radial_subdivisions)
        right = a+(b-a)*Q(sub+1, args.radial_subdivisions)
        if Q(row['left_exact']) != left or Q(row['right_exact']) != right:
            raise ValueError('Original exact cell endpoints differ')
        entry = min(bisect.bisect_right(model.starts, left)-1, len(model.segments)-1)
        pl, pr, packet_row, span = model.segments[entry]
        if not pl <= left < right <= pr or row['packet_row'] != packet_row or row['tail_span'] != span:
            raise ValueError('Original cell uses another background or geometry span')
        upper = row['linear_operator_upper']
        if not math.isfinite(upper) or upper < 0:
            raise ValueError('Invalid original interval upper bound')
        rows[cell, sub] = dict(cell=cell, subdivision=sub, left_exact=str(left), right_exact=str(right),
                              packet_row=packet_row, tail_span=span, linear_operator_upper=upper,
                              angular_arcs=int(option('angular', 256)), reused_closed_interval=True)
    return rows, dict(checkpoints=identity(path), original_engine_sha256=header['engine_sha256'],
                      defining_inputs_observed_at_resume=bindings,
                      identity_scope='The original header records paths and engine SHA. These immutable saved inputs are hashed here; the old header did not contain their hashes.',
                      completed_exact_intervals=len(rows),
                      exact_endpoints_and_packet_spans_reconstructed=True,
                      all_prior_complete_gzip_members_verified=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('manifest', 'packet', 'field', 'out', 'rows'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--reuse-checkpoints', type=Path)
    p.add_argument('--stop-file', type=Path)
    p.add_argument('--start', type=int, default=0)
    p.add_argument('--stop', type=int)
    p.add_argument('--angular', type=int, default=1024)
    p.add_argument('--maximum-angular', type=int, default=4096)
    p.add_argument('--radial-subdivisions', type=int, default=1)
    p.add_argument('--threshold', type=float, default=1.9e-9)
    args = p.parse_args()
    checkpoint = args.out.with_suffix('.checkpoints.jsonl.gz')
    progress = args.out.with_name(args.out.stem+'-progress.json')
    if any(path.exists() for path in (args.out, args.rows, checkpoint, progress)):
        raise FileExistsError('Use new output paths')
    if args.rows.suffix != '.gz' or min(args.angular, args.radial_subdivisions) < 1:
        raise ValueError('Positive subdivisions and gzip rows are required')
    started = time.monotonic()
    def event(stage, **values):
        row = dict(stage=stage, seconds=time.monotonic()-started,
                   peak_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024, **values)
        with checkpoint.open('ab') as sink:
            sink.write(gzip.compress((json.dumps(row, separators=(',', ':'))+'\n').encode(), mtime=0))
        if stage != 'cell_done' or values['ordinal'] % 100 == 0 or values.get('first_new'):
            print(json.dumps(row), flush=True)
    event('start', engine_sha256=identity(HERE/'fd2d-metric-c2-tail-linear-continuous.py')['sha256'],
          adapter=identity(__file__), normal_adapter=identity(HERE/'fd2d-metric-normal-interval-arithmetic.py'),
          defining_inputs={name: identity(getattr(args, name)) for name in ('manifest', 'packet', 'field')},
          argv=sys.argv[1:])
    field = E.linear.Field(args.field)
    event('field_loaded', nodes=len(field.x), modes=field.M, field_bindings=field.bindings)
    model = Tail(args.manifest, args.packet, field)
    model.quick_threshold = args.threshold
    total = len(model.mesh)-1
    event('tail_model_done', radial_cells=total)
    stop = total if args.stop is None else min(total, args.stop)
    if not 0 <= args.start < stop:
        raise ValueError('Invalid selected radial cells')
    prior, prior_identity = read_prior(args.reuse_checkpoints, args, model)
    event('prior_reconstructed', completed_exact_intervals=len(prior), prior_checkpoint=prior_identity)
    maximum, worst, reused, computed, ordinal, stopped = 0., None, 0, 0, 0, False
    for cell in range(args.start, stop):
        a, b = model.mesh[cell:cell+2]
        for sub in range(args.radial_subdivisions):
            left = a+(b-a)*Q(sub, args.radial_subdivisions)
            right = a+(b-a)*Q(sub+1, args.radial_subdivisions)
            old = prior.get((cell, sub))
            if old is not None and old['linear_operator_upper'] <= args.threshold:
                row = old
                upper = row['linear_operator_upper']
                reused += 1
            else:
                angular = args.angular
                upper, packet_row, span = model.bound(left, right, angular)
                attempts = [dict(angular=angular, upper=upper, angular_method=model.last_angular_method, fourier_absolute_upper=model.last_fourier_l1_upper)]
                while upper > args.threshold and 2*angular <= args.maximum_angular:
                    angular *= 2
                    refined, _, _ = model.bound(left, right, angular)
                    attempts.append(dict(angular=angular, upper=refined, angular_method=model.last_angular_method, fourier_absolute_upper=model.last_fourier_l1_upper))
                    upper = min(upper, refined)
                row = dict(cell=cell, subdivision=sub, left_exact=str(left), right_exact=str(right),
                           packet_row=packet_row, tail_span=span, linear_operator_upper=upper,
                           all_angle_attempts=attempts, reused_closed_interval=False,
                           prior_upper_if_refined=None if old is None else old['linear_operator_upper'])
                computed += 1
            with args.rows.open('ab') as sink:
                sink.write(gzip.compress((json.dumps(row, separators=(',', ':'))+'\n').encode(), mtime=0))
            ordinal += 1
            if upper > maximum:
                maximum, worst = upper, row
            event('cell_done', ordinal=ordinal, first_new=computed == 1 and not row['reused_closed_interval'], **row)
        state = dict(schema='fd2d-tail-linear-progress-v1', complete_tail_activity_domain=False,
                     next_cell=cell+1, start=args.start, total_radial_cells=total, maximum=maximum,
                     worst_interval=worst, reused_intervals=reused, newly_computed_intervals=computed,
                     seconds=time.monotonic()-started)
        temporary = progress.with_suffix('.tmp')
        temporary.write_text(json.dumps(state, indent=2)+'\n')
        temporary.replace(progress)
        if args.stop_file is not None and args.stop_file.exists():
            stop, stopped = cell+1, True
            break
    complete = args.start == 0 and stop == total
    report = dict(schema='fd2d-continuous-tail-linear-material-residual-v1', scope=__doc__,
                  script=identity(__file__), mathematical_engine=identity(HERE/'fd2d-metric-c2-tail-linear-continuous.py'),
                  interval_arithmetic_adapter=identity(HERE/'fd2d-metric-normal-interval-arithmetic.py'),
                  interval_arithmetic_policy=NORMAL_POLICY, prior_checkpoint=prior_identity,
                  reused_intervals=reused, newly_computed_intervals=computed,
                  stopped_at_complete_cell=stopped,
                  manifest=identity(args.manifest), packet=identity(args.packet),
                  low_memory_defining_reader=identity(HERE/'fd2d-light-tail-definition-reader.py'),
                  packet_data=identity(model.packet_data), field=identity(args.field), field_bindings=field.bindings,
                  exact_domain=list(map(str, (model.mesh[0], model.mesh[-1]))),
                  total_radial_cells=total, selected_cell_range=[args.start, stop],
                  selected_exact_domain=list(map(str, (model.mesh[args.start], model.mesh[stop]))),
                  selected_radial_cells=stop-args.start, radial_subdivisions=args.radial_subdivisions,
                  angular_arcs_covering_one_threefold_period=args.angular, maximum_angular_arcs=args.maximum_angular,
                  angular_refinement='Use the complete Fourier coefficient absolute sum if sufficient; otherwise cover all continuous angular arcs. All actual finite modes remain included.',
                  fourier_absolute_bound_proof='For c0+sum(cj cos(3ju)) or sum(cj sin(3ju)), coefficient Bernstein hulls and |sin|,|cos|<=1 enclose all u. Add the full positive sum of coefficient magnitudes outwards. This changes only the angular enclosure, not the defining polynomial.',
                  all_finite_angular_modes_covered=True, complete_tail_activity_domain=complete,
                  linear_operator_upper=maximum, worst_interval=worst,
                  threshold=args.threshold, threshold_met=complete and maximum <= args.threshold,
                  field_coordinates='p is meridian sigma displacement; stored two jets use physical r and u',
                  target_kind='original common rotational tail metric, same frozen background packet',
                  background_definition_hashes=model.packet.get('background_definition_hashes'),
                  nonlinear_pullback_certified=False, deep_tail_included=False, whole_surface_certified=False,
                  row_data=identity(args.rows), row_format='Concatenated closed gzip members, one JSON line per exact interval',
                  completed_cell_checkpoints=identity(checkpoint), seconds=time.monotonic()-started)
    for path in (args.rows, checkpoint):
        if path.stat().st_size >= 5_000_000:
            raise ValueError('Split interval rows to respect the per-file limit')
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), complete=complete, linear_operator_upper=maximum,
                          reused=reused, computed=computed, seconds=report['seconds'])), flush=True)


if __name__ == '__main__':
    main()
