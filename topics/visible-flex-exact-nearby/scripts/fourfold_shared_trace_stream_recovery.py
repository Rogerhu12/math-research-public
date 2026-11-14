#!/usr/bin/env python3
"""Restore missing historical backward chunks from an exact saved knot state.

This uses the frozen branch RHS and the very same per-knot solve_ivp options.
Only the transient solve/save lifecycle changes.  Every published chunk must
match its historical SHA256.  The historical final rows and metadata already
occur in every verified surviving chunk; the replayed final rows must match
them as binary64 arrays.  This is recovery of floating reference data, not an
ODE existence or residual certificate.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
from pathlib import Path
import time

import numpy as np

import fourfold_phase_exact_affine_nodes as runner
import fourfold_phase_knot_aligned_probe as alignment
import fourfold_phase_shared_grid_adaptive_chunks as adaptive
from fourfold_phase_symmetric_geometry import load_exact_object


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(1 << 20), b''):
            value.update(block)
    return value.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.writing')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


class TailSaved(Exception):
    """Return before the frozen branch materializes all dense output again."""


class StreamingRecovery(adaptive.AdaptiveSharedMap):
    def configure(self, *, template, last_piece, prefix_stop, resume_index,
                  resume_state, resume_time, expected, trace_stem, report,
                  report_path):
        self.template = template
        self.last_piece = last_piece
        self.prefix_stop = prefix_stop
        self.resume_index = resume_index
        self.resume_state = resume_state
        self.resume_time = resume_time
        self.expected = expected
        self.trace_stem = trace_stem
        self.recovery_report = report
        self.recovery_report_path = report_path
        self.chunk_steps = int(template['maximum_segments_per_chunk'])
        self.total_steps = int(template['branch_total_accepted_segments'])
        self.buffer = []
        self.overlap_verified = []

    def checkpoint(self):
        self.recovery_report.update(
            elapsed_seconds=time.monotonic()-self.started,
            replayed_RHS_calls=self.calls-self.recovery_report['initial_RHS_count'],
            replayed_maximum_N=self.maximum_N,
            replayed_minimum_qbar=self.minimum_qbar)
        save(self.recovery_report_path, self.recovery_report)

    def publish_buffer(self):
        if not self.buffer:
            return
        first = self.buffer[0]['index']
        last = self.buffer[-1]['index']+1
        if first % self.chunk_steps or (last-first != self.chunk_steps and last != self.total_steps):
            raise ValueError('streamed chunk does not have the historical chunk boundary')
        count = self.last_piece['accepted_state'].shape[-1]
        states = [self.buffer[0]['y_old']]+[row['y_new'] for row in self.buffer]
        metadata = dict(self.template)
        metadata.update(first_accepted_segment=first, accepted_segment_stop=last)
        arrays = dict(
            accepted_tau=np.array([self.buffer[0]['t_old']]+[row['t_new'] for row in self.buffer]),
            accepted_state=np.stack(states).reshape(len(states), 3, count),
            dense_t_old=np.array([row['t_old'] for row in self.buffer]),
            dense_h=np.array([row['h'] for row in self.buffer]),
            dense_y_old=np.stack([row['y_old'] for row in self.buffer]).reshape(last-first, 3, count),
            dense_F=np.stack([row['F'] for row in self.buffer]).reshape(last-first, 7, 3, count),
            initial_angles=states[0].reshape(3, count)[0],
            final_angles=self.last_piece['final_angles'],
            final_jacobian=self.last_piece['final_jacobian'],
            final_parameter_column=self.last_piece['final_parameter_column'],
            metadata=np.array(json.dumps(metadata, sort_keys=True)))
        packed, extension = runner.packed_npz(arrays)
        destination = self.trace_stem.parent/(self.trace_stem.name+f'.part{first:04d}'+extension)
        wanted = self.expected[str(destination)]
        actual = hashlib.sha256(packed).hexdigest()
        if actual != wanted['sha256'] or len(packed) != wanted['bytes']:
            mismatch = self.recovery_report_path.parent/(destination.name+'.mismatch')
            mismatch.write_bytes(packed)
            raise ValueError(f'replayed historical chunk differs: {destination}; kept {mismatch}')
        if destination.exists():
            if sha(destination) != actual:
                raise ValueError('refusing to overwrite a different existing chunk')
        else:
            temporary = destination.with_name(destination.name+'.writing')
            temporary.write_bytes(packed)
            temporary.replace(destination)
        self.recovery_report['published_chunks'].append(dict(
            path=str(destination), sha256=actual, bytes=len(packed),
            first_accepted_segment=first, accepted_segment_stop=last,
            historical_hash_exact_match=True))
        self.buffer.clear()
        del arrays, packed, states
        gc.collect()
        self.checkpoint()
        print(json.dumps(dict(progress='historical chunk exactly recovered',
                              first=first, stop=last, sha256=actual)), flush=True)

    def _solve_aligned(self, fun, interval, initial, **kwargs):
        start, finish = interval
        if start <= finish or self.resume_time > start or self.resume_time < finish:
            raise ValueError('this recovery entry supports the saved backward leg only')
        if not np.array_equal(initial.reshape(3, -1)[0], self.recovery_report['original_initial_angles']):
            raise ValueError('frozen branch initial angles changed')
        cuts = self.cuts[(self.cuts < self.resume_time)&(self.cuts > finish)][::-1]
        times = np.r_[self.resume_time, cuts, finish]
        current = np.array(self.resume_state, copy=True).ravel()
        step = self.resume_index
        old_first = int(self.template['first_accepted_segment'])
        for left, right in zip(times[:-1], times[1:]):
            options = dict(kwargs)
            options['first_step'] = min(abs(right-left), options.get('max_step', np.inf))
            solved = alignment.scipy_solve_ivp(fun, (float(left), float(right)), current, **options)
            if not solved.success:
                raise RuntimeError(solved.message)
            for j, polynomial in enumerate(solved.sol.interpolants):
                row = dict(index=step, t_old=polynomial.t_old, t_new=solved.t[j+1],
                           h=polynomial.h, y_old=polynomial.y_old.copy(),
                           y_new=solved.y[:, j+1].copy(), F=polynomial.F.copy())
                if step < self.prefix_stop:
                    offset = step-old_first
                    if offset < 0 or offset >= len(self.last_piece['dense_h']):
                        raise ValueError('overlap lies outside the verified last chunk')
                    pairs = [
                        (row['t_old'], self.last_piece['dense_t_old'][offset]),
                        (row['t_new'], self.last_piece['accepted_tau'][offset+1]),
                        (row['h'], self.last_piece['dense_h'][offset]),
                        (row['y_old'].reshape(3, -1), self.last_piece['dense_y_old'][offset]),
                        (row['y_new'].reshape(3, -1), self.last_piece['accepted_state'][offset+1]),
                        (row['F'].reshape(7, 3, -1), self.last_piece['dense_F'][offset])]
                    if not all(np.array_equal(a, b) for a, b in pairs):
                        raise ValueError(f'first replayed overlapping accepted step {step} differs')
                    self.overlap_verified.append(step)
                    self.recovery_report['exact_replayed_overlap_steps'] = list(self.overlap_verified)
                    self.checkpoint()
                    print(json.dumps(dict(progress='overlap step exactly reproduced', step=step)), flush=True)
                else:
                    self.buffer.append(row)
                    if len(self.buffer) == self.chunk_steps:
                        self.publish_buffer()
                step += 1
            current = solved.y[:, -1].copy()
            self.recovery_report['last_completed_knot_restart'] = dict(
                tau=float(right), accepted_segment_stop=step)
            self.checkpoint()
            del solved
            gc.collect()
        if step != self.total_steps or not self.overlap_verified:
            raise ValueError('replayed step count changed or no overlap was checked')
        self.publish_buffer()
        self.replayed_final = current.reshape(3, -1)
        raise TailSaved()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hash-manifest', type=Path, required=True)
    parser.add_argument('--old-report', type=Path, required=True)
    parser.add_argument('--root-certificate', type=Path, required=True)
    parser.add_argument('--trace-dir', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--progress', type=Path)
    args = parser.parse_args()
    expected = {row['path']:row for row in read(args.hash_manifest)['files']}
    stem = args.trace_dir/'block_0000_backward'
    forward_path = args.trace_dir/'block_0000_forward.trace.json'
    if sha(forward_path) != expected[str(forward_path)]['sha256']:
        raise ValueError('forward manifest is not the exact historical input')
    forward = read(forward_path)
    old = read(args.old_report)
    if old['status'] != 'complete' or len(old['completed_blocks']) != 1:
        raise ValueError('expected a completed historical one-block shared-grid report')
    historical_refs = [row for row in old['completed_blocks'][0]['dense_traces']
                       if Path(row['path']).name.startswith(stem.name+'.part')]
    prefix = []
    for row in historical_refs:
        path = Path(row['path'])
        if not path.exists():
            break
        if sha(path) != row['sha256'] or row['sha256'] != expected[str(path)]['sha256']:
            raise ValueError('an existing backward chunk has a different historical hash')
        prefix.append(row)
    if not prefix:
        raise ValueError('a surviving exact backward chunk is required')
    last = runner.load_npz(prefix[-1]['path'])
    template = json.loads(str(last['metadata']))
    identity = dict(forward['identity'])
    identity.update(sign=1., start=np.pi/2, finish=-np.pi/2)
    if template['identity'] != identity:
        raise ValueError('backward metadata and forward historical identity differ')
    dependencies = {
        'fourfold_phase_exact_affine_nodes.py':identity['run_source_sha256'],
        'fourfold_phase_shared_grid_adaptive_chunks.py':identity['integration_driver_source_sha256'],
        'fourfold_phase_shared_knot_nodes.py':identity['previous_shared_driver_sha256'],
        'fourfold_phase_knot_aligned_probe.py':identity['knot_alignment_source_sha256'],
        'fourfold_phase_symmetric_geometry.py':identity['geometry_source_sha256']}
    for name, value in dependencies.items():
        if sha(Path(__file__).with_name(name)) != value:
            raise ValueError(f'frozen dependency changed: {name}')
    if sha(identity['object_file']) != identity['source_sha256'] or sha(args.root_certificate) != identity['root_certificate_sha256']:
        raise ValueError('object or historical root source changed')
    prefix_stop = int(template['accepted_segment_stop'])
    cuts = np.asarray(identity['knot_alignment']['tau_cuts'])
    candidate = [i for i, tau in enumerate(last['accepted_tau'][:-1]) if np.any(cuts == tau)]
    if not candidate and len(prefix) != len(historical_refs):
        raise ValueError('last historical chunk has no earlier exact knot restart')
    offset = candidate[-1] if candidate else 0
    resume_index = int(template['first_accepted_segment'])+offset
    report = dict(kind='historical_floating_backward_trace_stream_recovery', status='running',
        source_sha256=sha(__file__), frozen_dependency_sha256=dependencies,
        hash_manifest_sha256=sha(args.hash_manifest), old_report_sha256=sha(args.old_report),
        original_failed_session_exit_code=137,
        recovered_from_existing_prefix=len(prefix), existing_prefix_stop=prefix_stop,
        resumed_at_exact_knot_step=resume_index, resumed_at_tau=float(last['accepted_tau'][offset]),
        original_initial_angles=forward['final_angles'], initial_RHS_count=forward['rhs_calls'],
        historical_identity=identity, exact_replayed_overlap_steps=[], published_chunks=[],
        limitations=['recovers an existing floating reference by exact bytes',
                     'not an interval ODE residual or existence certificate',
                     'historical final rows and metadata are reused only from verified old chunks',
                     'new actual tail final values and every emitted chunk are checked exactly'])
    save(args.out, report)
    if len(prefix) != len(historical_refs):
        geometry, definition = load_exact_object(identity['object_file'], identity['quarter_nodes'])
        common = {key:value for key, value in identity.items() if key not in ('sign','start','finish','root')}
        mapper = StreamingRecovery(geometry, identity['root'], common, args.progress)
        if mapper.common != common or not np.array_equal(mapper.cuts, cuts):
            raise ValueError('frozen numerical knot restart rule changed')
        mapper.maximum_N, mapper.minimum_qbar = forward['maximum_N'], forward['minimum_qbar']
        mapper.calls = forward['rhs_calls']
        mapper.configure(template=template, last_piece=last, prefix_stop=prefix_stop,
            resume_index=resume_index, resume_state=last['accepted_state'][offset],
            resume_time=float(last['accepted_tau'][offset]), expected=expected,
            trace_stem=stem, report=report, report_path=args.out)
        theta = np.asarray(forward['final_angles'])
        try:
            mapper.branch(theta, 1., np.pi/2, -np.pi/2, identity['ode_rtol'], stem)
        except TailSaved:
            pass
        else:
            raise RuntimeError('streaming solver did not return by its bounded-memory exit')
        final = mapper.replayed_final
        jacobian = np.exp(final[1])
        raw_start = geometry.principal_quantities(np.full_like(theta, mapper.root), theta)
        raw_finish = geometry.principal_quantities(np.full_like(theta, -mapper.root), final[0])
        start_speed, finish_speed = -raw_start['m']/raw_start['n'], -raw_finish['m']/raw_finish['n']
        column = final[2]+mapper.root_parameter_derivative*(-jacobian*start_speed-finish_speed)
        checks = dict(final_angles=np.array_equal(final[0], last['final_angles']),
                      final_jacobian=np.array_equal(jacobian, last['final_jacobian']),
                      final_parameter_column=np.array_equal(column, last['final_parameter_column']),
                      replay_chart_maximum_not_larger=mapper.maximum_N <= template['maximum_N'],
                      replay_root_quotient_minimum_not_smaller=mapper.minimum_qbar >= template['minimum_qbar'])
        report['replayed_final_checks'] = {key:bool(value) for key, value in checks.items()}
        if not all(checks.values()):
            save(args.out, report)
            raise ValueError('replayed tail final state differs from historical final rows')
        mapper.checkpoint()
    for row in historical_refs:
        if sha(row['path']) != row['sha256']:
            raise ValueError('not every historical backward trace chunk is present and exact')
    record = dict(identity=identity, initial_angles=forward['final_angles'],
        final_angles=last['final_angles'].tolist(), final_jacobian=last['final_jacobian'].tolist(),
        final_parameter_column=last['final_parameter_column'].tolist(), traces=historical_refs,
        accepted_steps=int(template['branch_total_accepted_segments']),
        rhs_calls=old['rhs_calls']-forward['rhs_calls'],
        maximum_N=template['maximum_N'], minimum_qbar=template['minimum_qbar'])
    payload = (json.dumps(record, indent=2)+'\n').encode()
    manifest = stem.with_suffix('.trace.json')
    actual = hashlib.sha256(payload).hexdigest()
    if actual != expected[str(manifest)]['sha256']:
        manifest.with_name(manifest.name+'.reconstructed-mismatch').write_bytes(payload)
        raise ValueError('reconstructed complete backward manifest differs from historical SHA')
    manifest.write_bytes(payload)
    report.update(status='complete', all_historical_chunks_and_manifest_exact=True,
                  verified_backward_files=len(historical_refs)+1,
                  trace_manifest_sha256=actual)
    save(args.out, report)
    print(json.dumps(dict(status='complete', backward_files=len(historical_refs)+1,
                          trace_manifest_sha256=actual)), flush=True)


if __name__ == '__main__':
    main()
