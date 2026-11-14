#!/usr/bin/env python3
"""Compute only parameter densities for an immutable selected g0 prefix.

The selected zero-order reports are checked by the unchanged mathematical
validator and are never recomputed or rewritten. Each parameter proof and
density has its own process lifetime. A completed block is reusable only with
the very same selected g0 SHA. Its final inventory includes the original
read-only g0 inputs, and artifact-paths.txt lists the portable closure.

No partial block is a full forward return. All cross-block chronological
Fourier terms remain the responsibility of the original accumulators.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gc
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback
from types import SimpleNamespace

from fourfold_ci_density_block_v3 import (
    BASE, DESCRIPTOR, COVER, G0, PRECOMPUTE, sha, save, run_child, inventory,
)


def path_row(path, wanted=None):
    path = Path(path)
    digest = sha(path)
    if wanted is not None and digest != wanted:
        raise ValueError('immutable selected input bytes changed: '+str(path))
    return dict(path=str(path), sha256=digest, bytes=path.stat().st_size)


def unique_rows(rows):
    by_path = {}
    for row in rows:
        previous = by_path.get(row['path'])
        if previous is not None and previous != row:
            raise ValueError('conflicting immutable file inventory entries')
        by_path[row['path']] = row
    return [by_path[name] for name in sorted(by_path)]


def new_log(directory, stem):
    """Retain every earlier failure log when a block is explicitly resumed."""
    path = directory/(stem+'.log')
    count = 0
    while path.exists():
        count += 1
        path = directory/(stem+'.attempt%03d.log' % count)
    return path


def parameter_arguments(scope, source):
    return SimpleNamespace(
        source_versions={sha(source): source}, descriptor=DESCRIPTOR,
        uniform_half_width=Fraction(0) if scope == 'center' else Fraction(1, 10**9),
        label_strip='1/256', inner_strip='3/1024',
        spatial_strip=Fraction(7, 2048))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--g0-index', type=Path, required=True)
    p.add_argument('--g0-index-sha256', required=True)
    p.add_argument('--start', type=int, required=True)
    p.add_argument('--stop', type=int, required=True)
    p.add_argument('--run-tag', required=True)
    p.add_argument('--parameter-pipeline', type=Path,
        default=Path('scripts/fourfold_parameter_density_pipeline_efficient_v5.py'))
    p.add_argument('--plan-only', action='store_true')
    a = p.parse_args()
    if (not 0 <= a.start < a.stop <= 550
        or not re.fullmatch(r'[A-Za-z0-9_.-]+', a.run_tag)
        or not re.fullmatch(r'[0-9a-f]{64}', a.g0_index_sha256)):
        raise ValueError('invalid exact selected block, tag or index hash')
    directory = BASE/'step5_ci_forward_blocks'/a.run_tag/(
        'block_%04d_%04d' % (a.start, a.stop))
    directory.mkdir(parents=True, exist_ok=True)
    logs = directory/'logs'
    logs.mkdir(exist_ok=True)
    report_path = directory/'block-manifest.json'
    if report_path.exists():
        previous_raw = report_path.read_bytes()
        previous = json.loads(previous_raw)
        if (previous.get('selected_g0_index_sha256') != a.g0_index_sha256
            or previous.get('requested_segment_interval') != [a.start, a.stop]):
            raise ValueError('refuse to replace a different selected block')
        if previous.get('complete'):
            raise ValueError('this completed immutable block already exists')
        archived = directory/('previous-block-'+hashlib.sha256(previous_raw).hexdigest()[:20]+'.json')
        if archived.exists() and archived.read_bytes() != previous_raw:
            raise ValueError('previous block archive collision')
        archived.write_bytes(previous_raw)
    started = time.monotonic()
    external = []
    report = dict(
        kind='actual_independent_forward_density_block', complete=False,
        source_sha256=sha(__file__), source_commit=os.environ.get('GITHUB_SHA'),
        requested_segment_interval=[a.start, a.stop], run_tag=a.run_tag,
        descriptor_sha256=sha(DESCRIPTOR), field_cover_sha256=sha(COVER),
        g0_pipeline_path=str(G0), g0_pipeline_sha256=sha(G0),
        parameter_pipeline_path=str(a.parameter_pipeline),
        parameter_pipeline_sha256=sha(a.parameter_pipeline),
        parameter_precompute_source_sha256=sha(PRECOMPUTE),
        g0_validator_source_sha256=sha(Path(__file__).with_name('fourfold_forward_density_cover_v9.py')),
        parameter_validator_source_sha256=sha(Path(__file__).with_name('fourfold_parameter_density_cover_efficient_v4.py')),
        selected_g0_index_path=str(a.g0_index),
        selected_g0_index_sha256=a.g0_index_sha256,
        selected_g0_reports_are_read_only=True, zero_order_resampled=False,
        full_forward_leg_claimed=False, actual_R31_accepted=False,
        final_global_cross_block_terms_still_required=True, leaves=[])
    save(report_path, report)
    try:
        from flint import ctx
        from fourfold_saved_circle_field_multidomain_budget import read
        from fourfold_phase_domain_cover_verify import Closure
        from fourfold_retarget_reference_jets import RetargetReference
        from fourfold_forward_density_cover_v9 import (
            load_cover, exact_case_leaves, check_reference_seams, validate_saved)
        from fourfold_parameter_density_cover_efficient_v4 import validate_parameter_report
        from fourfold_phase_unified_scalar_time_circle import exact_time

        ctx.prec = 320
        ctx.cap = 24
        external.append(path_row(a.g0_index, a.g0_index_sha256))
        index = read(a.g0_index)
        if (index.get('descriptor_sha256') != sha(DESCRIPTOR)
            or index.get('completed_segments', 0) < a.stop
            or Fraction(index['label_strip']) != Fraction(1, 256)
            or Fraction(index['inner_strip']) != Fraction(3, 1024)):
            raise ValueError('selected index has another object, strip or incomplete prefix')
        # This worker deliberately supports the selected v9 g0 leaves only.
        # Other historical kernel sources remain the original cover's job.
        declared_v9 = [(name, digest) for name, digest in index['pipeline_sources'].items()
                       if Path(name).name == G0.name]
        if len(declared_v9) != 1 or declared_v9[0][1] != sha(G0):
            raise ValueError('the selected v9 source is absent or changed')
        reference = RetargetReference(DESCRIPTOR)
        closure = Closure(Path.cwd(), reference.doc['target_object']['sha256'],
                          reference.doc['target_root']['sha256'])
        grid = read(reference.doc['old_forward_reference']['path'])
        seams = check_reference_seams(
            Path('notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json'),
            DESCRIPTOR, reference)
        cover, cases = load_cover(COVER, DESCRIPTOR, reference, closure)
        report['reference_seams'] = seams
        if len(cases) != 550:
            raise ValueError('the full exact forward field partition is absent')
        selected = {}
        for row in index['leaves']:
            segment = int(row['segment'])
            if a.start <= segment < a.stop:
                key = (segment, *map(Fraction, row['normalized_subspan']))
                if key in selected:
                    raise ValueError('duplicate selected g0 leaf')
                selected[key] = row
        verified = []
        expected_keys = set()
        actual_times = []
        validation_args = SimpleNamespace(
            label_strip='1/256', inner_strip='3/1024', descriptor=DESCRIPTOR)
        for segment in range(a.start, a.stop):
            domains = exact_case_leaves(cases[('forward', segment)], cover, grid, closure)
            for domain in domains:
                left, right, domain_path, domain_sha, domain_doc = domain
                key = (segment, left, right)
                expected_keys.add(key)
                if key not in selected:
                    raise ValueError('a requested actual field leaf has no selected g0 input')
                row = selected[key]
                g0_path = Path(row['path'])
                external.append(path_row(g0_path, row['sha256']))
                g0, first, original_domain = validate_saved(
                    g0_path, reference, validation_args, closure, {sha(G0): G0})
                if (g0['domain_sha256'] != domain_sha
                    or g0['identity']['reference']['segment'] != segment
                    or list(map(Fraction, g0['identity']['reference']['normalized_subspan'])) != [left, right]):
                    raise ValueError('selected g0 is not the requested exact field/reference leaf')
                if ('current_field_cover_domain_sha256' in row
                    and row['current_field_cover_domain_sha256'] != domain_sha):
                    raise ValueError('selected current field-cover identity changed')
                external.append(path_row(g0['first_integral_file']['path'],
                                         g0['first_integral_file']['sha256']))
                expanded = g0.get('expanded_true_field_domain')
                if expanded:
                    links = [expanded] + expanded.get('attempts', [])
                    for link in links:
                        external.append(path_row(link['path'], link['sha256']))
                verified.append((row, domain, g0))
                actual_times.append(domain_doc['exact_time_endpoints'])
                del first
        if set(selected) != expected_keys:
            raise ValueError('selected g0 block has an unrequested leaf or interval')
        for previous, current in zip(actual_times, actual_times[1:]):
            if exact_time(previous[1]) != exact_time(current[0]):
                raise ValueError('the selected actual zero-order block has a time gap')
        if (not actual_times
            or exact_time(actual_times[0][0]) != exact_time(grid['exact_time_endpoints'][a.start])
            or exact_time(actual_times[-1][1]) != exact_time(grid['exact_time_endpoints'][a.stop])):
            raise ValueError('selected block endpoints differ from the exact reference grid')
        if sha(a.g0_index) != a.g0_index_sha256:
            raise ValueError('immutable selected index changed during validation')
        report.update(
            requested_exact_domain_leaves=[
                dict(path=str(domain[2]), sha256=domain[3]) for _, domain, _ in verified],
            complete_requested_g0_block=True,
            exact_begin=actual_times[0][0], exact_end=actual_times[-1][1],
            original_g0_validator_applied_to_every_leaf=True,
            selected_read_only_input_files=unique_rows(external))
        save(report_path, report)
        if a.plan_only:
            report.update(plan_only=True, requested_domain_partition_proved=True)
            report['selected_plan'] = [
                dict(segment=row['segment'], normalized_subspan=row['normalized_subspan'],
                     domain_path=str(domain[2]), domain_sha256=domain[3],
                     g0_report_path=row['path'], g0_report_sha256=row['sha256'],
                     first_integral_file=g0['first_integral_file'])
                for row, domain, g0 in verified]
        else:
            for row, domain, g0 in verified:
                g0_path = Path(row['path'])
                key = (int(row['segment']), *map(Fraction, row['normalized_subspan']))
                item = dict(segment=row['segment'], normalized_subspan=row['normalized_subspan'],
                    domain_path=str(domain[2]), domain_sha256=domain[3],
                    g0_report_path=str(g0_path), g0_report_sha256=row['sha256'])
                expanded = g0.get('expanded_true_field_domain')
                expanded_args = ['--expanded-domain-directory', str(directory/'expanded-field')]
                if expanded and expanded.get('proved'):
                    expanded_args += ['--expanded-domain', expanded['path']]
                for scope in ('center', 'uniform'):
                    target = '1e-9' if scope == 'center' else '1e-7'
                    half_width = '0' if scope == 'center' else '1/1000000000'
                    stem = g0_path.name.removesuffix('.json.gz')+'_'+scope
                    out = directory/(stem+'.json.gz')
                    if not (out.exists() and read(out).get('complete')):
                        prep = directory/(stem+'_precompute.json')
                        run_child([sys.executable, '-u', str(PRECOMPUTE),
                            '--domain', str(domain[2]), '--descriptor', str(DESCRIPTOR),
                            '--uniform-half-width', half_width, *expanded_args,
                            '--parameter-proof-directory', str(directory/'expanded-parameter'),
                            '--parameter-proof-lock-directory', str(directory/'locks'),
                            '--expanded-proof-nodes', '512', '--root-nodes', '1024',
                            '--log-directory', str(logs/'parameter-proof'),
                            '--out', str(prep)], new_log(logs, stem+'_precompute'))
                        item[scope+'_precompute_report_path'] = str(prep)
                        item[scope+'_precompute_report_sha256'] = sha(prep)
                        command = [sys.executable, '-u', str(a.parameter_pipeline),
                            '--descriptor', str(DESCRIPTOR), '--domain', str(domain[2]),
                            '--reference-certificate', str(g0_path),
                            '--reference-source', str(G0), '--uniform-half-width', half_width,
                            '--target', target, '--primitive-nodes', '384', '--root-nodes', '1024',
                            '--bits', '256', '--coefficient-bits', '160',
                            '--directory', str(directory/stem), *expanded_args,
                            '--parameter-proof-directory', str(directory/'expanded-parameter'),
                            '--parameter-proof-lock-directory', str(directory/'locks'),
                            '--out', str(out)]
                        if scope == 'uniform':
                            command.append('--second-only')
                        run_child(command, new_log(logs, stem))
                    parameter, _ = validate_parameter_report(
                        out, g0_path, parameter_arguments(scope, a.parameter_pipeline), key)
                    for name, digest in parameter['dependency_sha256'].items():
                        path_row(Path('scripts')/name, digest)
                    if parameter['source_sha256'] != sha(a.parameter_pipeline):
                        raise ValueError('the completed actual parameter source changed')
                    item[scope+'_report_path'] = str(out)
                    item[scope+'_report_sha256'] = sha(out)
                report['leaves'].append(item)
                save(report_path, report)
                print('COMPLETED_SELECTED_PARAMETER_LEAF', row['segment'], row['normalized_subspan'], flush=True)
                gc.collect()
            report.update(complete=True, only_zero_order_requested=False,
                          complete_center_and_uniform_g2_block=True)
    except Exception as exc:
        report.update(failure=type(exc).__name__+': '+str(exc), traceback=traceback.format_exc())
    report['wall_seconds'] = time.monotonic()-started
    save(report_path, report)
    local_rows = [row for row in inventory(directory)
                  if Path(row['path']).name not in ('artifact-paths.txt', 'artifact-all-paths.txt')]
    rows = unique_rows(local_rows+external)
    files_path = directory/'files.json'
    save(files_path, dict(kind='completed_or_failed_actual_block_file_inventory',
        block_manifest_sha256=sha(report_path),
        external_read_only_inputs_preserve_original_paths=True, files=rows))
    # Paths are relative to the topic cwd and safe for tar -T. The list itself
    # is operational packaging metadata, not an extra mathematical assumption.
    artifacts = sorted({row['path'] for row in local_rows} | {str(report_path), str(files_path)})
    all_artifacts = sorted({row['path'] for row in rows} | {str(report_path), str(files_path)})
    if any('\n' in name or name.startswith('/') or '..' in Path(name).parts for name in artifacts):
        raise ValueError('artifact inventory contains a nonportable path')
    (directory/'artifact-paths.txt').write_text('\n'.join(artifacts)+'\n')
    (directory/'artifact-all-paths.txt').write_text('\n'.join(all_artifacts)+'\n')
    print({k: report.get(k) for k in
           ('complete', 'plan_only', 'complete_requested_g0_block', 'failure', 'wall_seconds')}, flush=True)
    return 0 if report['complete'] or (a.plan_only and not report.get('failure')) else 2


if __name__ == '__main__':
    raise SystemExit(main())
