#!/usr/bin/env python3
"""Continue a real accepted endpoint with original same-g and response jobs.

The response route converts an accepted design to its genuine fixed view,
audits its original physical quintic, and computes all thirteen complete
control responses. The refine-response route additionally performs the
existing M32 -> M40, 1280 -> 1536 same-g nonlinear refinement and the existing
complete-mean comparison before computing the new response at the fine state.

Every numerical phase uses an existing production entry and its original
mathematical gates. Inputs keep their bytes and local basenames in one output
data directory. There is no queue service, publish operation, timeout, file
size gate, approval step, or claim that an unaccepted iterate is a solution.
"""
from __future__ import annotations

import argparse
import copy
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

FIELDS = ('delta', 'boost_length', 'boost_speed', 'vu',
          'descending_turn_curvature', 'start_acceleration',
          'initial_speed_frontload', 'vd', 'descending_sync_curvature',
          'loop_curvature', 'loop_radius', 'loop_speed', 'terminal_peak_fraction')
PHYSICAL = ('frozen_profile', 'physical_tail_parameters', 'physical_tail_cut',
            'angular_chart', 'chart_reference_coefficients',
            'chart_reference_frequencies', 'gauge_amplitude', 'meridian_length')


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, data):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(data, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def locate(value, parent):
    value, parent = Path(value), Path(parent)
    choices = [value, parent/value, parent/value.name]
    for choice in choices:
        if choice.is_file():
            return choice.resolve()
    raise FileNotFoundError('Required accepted data file is unavailable: ' + str(value))


def accepted(data):
    if (not data.get('solver_success') or data.get('audit_pending', True)
            or not data.get('config', {}).get('actual_nonlinear_tail')):
        raise ValueError('A genuinely successful and audited actual endpoint is required')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted', type=Path, required=True)
    parser.add_argument('--tail-config', type=Path, required=True)
    parser.add_argument('--fixed-report', type=Path)
    parser.add_argument('--initial-full-tangent-manifest', type=Path)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--frozen-reference-ready', type=Path, required=True)
    parser.add_argument('--frozen-calibration-ledger', type=Path, required=True)
    parser.add_argument('--computations-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--port', type=Path)
    parser.add_argument('--port40', type=Path)
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--route', choices=('response', 'refine-response', 'refine'), default='refine-response')
    parser.add_argument('--radial-workers', type=int, default=4)
    parser.add_argument('--node-heap', type=int, default=1024)
    parser.add_argument('--max-nodes', type=int, default=8000)
    parser.add_argument('--audit-angular', type=int, default=768)
    parser.add_argument('--audit-radial', type=int, default=801)
    parser.add_argument('--terminal-relative-width', type=float, default=2e-5)
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    comp = args.computations_dir.resolve()
    port32 = (args.port or comp/'alternative-neck-provider-smallcut30-port32-r2048.json').resolve()
    port40 = (args.port40 or comp/'alternative-neck-provider-smallcut30-port40-exact-prefix-r4096.json').resolve()
    source = args.source_topic.resolve()
    out, work = args.out_dir.resolve(), args.work.resolve()
    data, logs = out/'data', out/'logs'
    for path in (data, logs, work):
        path.mkdir(parents=True, exist_ok=True)
    status_file = out/'sequence-status.json'
    if status_file.exists():
        raise FileExistsError('Use a fresh output directory; accepted files are never overwritten')
    state = dict(scope=__doc__, status='preparing', route=args.route,
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256=sha(__file__), cwd=str(data), input_files=[], phases=[],
        prepare_only=args.prepare_only, new_nonlinear_solution=False,
        original_numerical_and_physical_gates_preserved=True)

    def event(kind, **details):
        state['last_event'] = dict(event=kind,
            utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), **details)
        write(status_file, state)
        print(json.dumps(state['last_event'], allow_nan=False), flush=True)

    def retain(path, expected=None):
        path = Path(path).resolve()
        digest = sha(path)
        if expected is not None and digest != expected:
            raise ValueError('Accepted input hash differs: ' + str(path))
        destination = data/path.name
        if destination.exists():
            if sha(destination) != digest:
                raise ValueError('Different input files share a basename: ' + path.name)
        else:
            try:
                os.link(path, destination)
            except OSError:
                shutil.copy2(path, destination)
        if not any(row['file'] == destination.name for row in state['input_files']):
            state['input_files'].append(dict(file=destination.name, sha256=digest,
                bytes=destination.stat().st_size, original_file=str(path)))
        return destination.name

    seed_path = args.accepted.resolve()
    seed = read(seed_path)
    accepted(seed)
    matching_ports = [path for path in (port32, port40)
                      if path.is_file() and sha(path) == seed['physical_port_sha256']]
    if not matching_ports:
        raise ValueError('Supply the unchanged physical port used by the accepted endpoint')
    seed_port = matching_ports[0]
    seed_name = retain(seed_path)
    raw_path = locate(seed['raw_collocation_checkpoint']['file'], seed_path.parent)
    raw_name = retain(raw_path, seed['raw_collocation_checkpoint']['sha256'])
    raw = read(raw_path)
    for item in raw['arrays'].values():
        for chunk in item['chunks']:
            retain(locate(chunk['file'], raw_path.parent), chunk['sha256'])
    for chunk in seed['pp_coefficient_chunks']:
        retain(locate(chunk['file'], seed_path.parent), chunk['sha256'])
    tail_path = locate(seed['actual_tail']['final_response'], seed_path.parent)
    tail_name = retain(tail_path)
    tail = read(tail_path)
    config_name = retain(args.tail_config, raw['identity']['coupling_context']['tail_config_sha256'])
    if not (tail['request'].get('jacobian') and tail['request'].get('audit')
            and tail['response'].get('converged') and tail['response'].get('audit')):
        raise ValueError('The accepted full-H tail Jacobian and audit are required')
    snapshot = tail['response'].get('fullFlowTangentSnapshot')
    manifest = args.initial_full_tangent_manifest
    if snapshot is not None:
        manifest = locate(snapshot['manifestPath'], tail_path.parent)
    if manifest is not None:
        manifest = Path(manifest).resolve()
        retain(manifest, snapshot['manifestSha256'] if snapshot else None)
        packed = read(manifest)
        for row in [packed['base'], *packed['chunks']]:
            retain(locate(row['file'], manifest.parent), row['sha256'])
    report_name = retain(args.fixed_report) if args.fixed_report else None
    fixed = bool(seed['config'].get('fixed_metric'))
    if args.prepare_only and not fixed:
        raise ValueError('Prepare-only uses an existing genuine fixed view; it never invents a converted field')
    if args.route != 'response' and int(seed['modes']) != 32:
        raise ValueError('The available same-g spectral entry is explicitly M32 -> M40')
    if fixed and args.route != 'response' and report_name is None:
        raise ValueError('Supply the original genuine fixed-view conversion report for the M40 entry')
    fixed_name = seed_name if fixed else 'fixed-view.json.gz'
    fixed_raw = raw_name if fixed else 'fixed-view-raw-collocation.json.gz'
    fixed_report = report_name if fixed else 'fixed-view-report.json'

    def command(name, *items):
        return [sys.executable, '-u', str(comp/name), *map(str, items)]

    def threaded(label, name, items):
        return command('root_20261114_threaded_entry.py', '--radial-workers', args.radial_workers,
            '--parallel-run-record', logs/(label+'-parallel.json'), '--target-entry', comp/name, *items)

    def run(label, cmd):
        phase = dict(name=label, command=cmd, status='running',
            log=str(Path('logs')/(label+'.log')))
        state['phases'].append(phase)
        event('phase_started', phase=label, command=cmd)
        with (logs/(label+'.log')).open('w') as stream:
            result = subprocess.run(cmd, cwd=data, stdout=stream, stderr=subprocess.STDOUT)
        phase.update(returncode=result.returncode, status='finished' if result.returncode == 0 else 'failed')
        event('phase_returned', phase=label, returncode=result.returncode)
        if result.returncode:
            raise RuntimeError('Original numerical entry failed in phase ' + label)

    def audit(label, endpoint, port):
        return command('strong_anchor_interior_fullmean_audit.py', '--input', endpoint,
            '--source-topic', source, '--port', port, '--out', label+'.json',
            '--angular', args.audit_angular, '--radial', args.audit_radial, '--batch', 8)

    def refine_command():
        return threaded('same-g-m40', 'strong_sameg_m40_initial_laws_fullflow_refinement.py', [
            '--fixed-reference', fixed_name, '--spectral-fixed-raw', fixed_raw,
            '--spectral-fixed-report', fixed_report, '--spectral-warm-tail', tail_name,
            '--spectral-baseline-config', config_name, '--spectral-temporary-parent', work,
            '--spectral-node-young-space', 16, '--spectral-stage-cache-directory', work/'m40-stage-cache',
            '--frozen-reference-ready', args.frozen_reference_ready.resolve(),
            '--frozen-calibration-ledger', args.frozen_calibration_ledger.resolve(),
            '--source-topic', source, '--port', port40, '--frozen-port', seed_port,
            '--out-prefix', 'same-g-m40', '--modes', 40, '--angular', 1536,
            '--tol', repr(float(seed['config']['tol'])), '--max-nodes', args.max_nodes,
            '--node-heap', args.node_heap])

    def response_command(endpoint, raw_endpoint, tail_endpoint, tail_config, port, label):
        return threaded(label, 'strong_20261114_response_widths.py', [
            '--response-checkpoint', endpoint, '--response-raw', raw_endpoint,
            '--response-tail', tail_endpoint, '--response-out-prefix', work/label,
            '--response-fields', ','.join(FIELDS), '--response-relative-width',
            'terminal_peak_fraction='+repr(args.terminal_relative_width),
            '--radial-batch-size', 24, '--collocation-batch-size', 24,
            '--disk-temporary-parent', work, '--source-topic', source,
            '--port', port, '--tail-config', tail_config])

    def publish_response(label):
        full_path = work/(label+'.json')
        response = read(full_path)
        if (not response.get('finished') or response.get('new_solution')
                or response.get('tail_worker_started') or tuple(response['fields']) != FIELDS):
            raise ValueError('The complete declared thirteen-field response did not finish')
        keep, omitted = [], []
        for item in response['tangent_arrays']:
            name = Path(item['file']).name
            needed = ('-prescribed-' in name or '-core-held-' in name or any(
                name.endswith('-external-'+field+'.npy.gz') for field in FIELDS[:3]))
            if not needed:
                omitted.append(item)
                continue
            original = locate(item['file'], full_path.parent)
            retained = retain(original, item['sha256'])
            keep.append({**item, 'file': retained})
        portable = copy.deepcopy(response)
        portable['tangent_arrays'] = keep
        portable['portable_sequence_archive'] = dict(
            original_summary_sha256=sha(full_path), complete_continuation_directions_retained=True,
            omitted_regenerable_arrays=omitted, full_original_array_package_archived=False,
            global_J_and_QR_archived=False, nonlinear_solution=False)
        shutil.copy2(full_path, data/(label+'-full-summary.json'))
        write(data/(label+'.json'), portable)
        return dict(file=label+'.json', sha256=sha(data/(label+'.json')),
            retained_array_count=len(keep), omitted_regenerable_array_count=len(omitted))

    try:
        state.update(status='running', input_accepted_checkpoint=dict(file=seed_name, sha256=sha(data/seed_name)))
        event('accepted_inputs_materialized', files=len(state['input_files']), modes=seed['modes'])
        if not fixed:
            run('fixed-view', threaded('fixed-view', 'strong_anchor_freeze_design_view.py', [
                '--design-checkpoint', seed_name, '--design-raw', raw_name, '--design-tail', tail_name,
                '--fixed-view-prefix', 'fixed-view', '--radial-batch-size', 24,
                '--source-topic', source, '--port', seed_port, '--tail-config', config_name]))
            accepted(read(data/fixed_name))
        if args.prepare_only:
            if args.route != 'response':
                run('same-g-m40-prepare', refine_command()+['--spectral-prepare-only'])
            if args.route != 'refine':
                run('response-metadata', response_command(fixed_name, fixed_raw, tail_name,
                    config_name, seed_port, 'response-metadata')+['--metadata-only'])
                shutil.copy2(work/'response-metadata.json', data/'response-metadata.json')
            state.update(status='prepared', numerical_solve_executed=False, new_nonlinear_solution=False)
            event('sequence_prepared_without_numerical_solve')
            return
        run('coarse-fullmean-audit', audit('coarse-fullmean-audit', fixed_name, seed_port))
        current_name, current_raw, current_tail, current_config, current_port = (
            fixed_name, fixed_raw, tail_name, config_name, seed_port)
        if args.route != 'response':
            run('same-g-m40', refine_command())
            fine = read(data/'same-g-m40.json.gz')
            accepted(fine)
            coarse = read(data/fixed_name)
            if any(coarse[key] != fine[key] for key in PHYSICAL):
                raise ValueError('A physical datum changed in the same-g refinement')
            current_name = 'same-g-m40.json.gz'
            current_raw = locate(fine['raw_collocation_checkpoint']['file'], data).name
            current_tail = locate(fine['actual_tail']['final_response'], data).name
            current_config, current_port = 'same-g-m40-config.json', port40
            state.update(new_nonlinear_solution=True, accepted_refinement=dict(
                file=current_name, sha256=sha(data/current_name), physical_metric_unchanged=True))
            run('fine-fullmean-audit', audit('fine-fullmean-audit', current_name, port40))
            run('same-g-comparison', command('strong_sameg_anchor_complete_mean_comparison.py',
                '--coarse', fixed_name, '--fine', current_name, '--source-topic', source,
                '--port', port40, '--out', 'same-g-comparison.json', '--angular', args.audit_angular,
                '--batch', 8))
        if args.route != 'refine':
            run('control-response', response_command(current_name, current_raw, current_tail,
                current_config, current_port, 'control-response'))
            state['complete_response'] = publish_response('control-response')
        state.update(status='finished', accepted_current_endpoint=current_name,
            complete_closed_surface_or_amplitude_goal_claimed=False)
        event('accepted_endpoint_sequence_finished', current_endpoint=current_name)
    except BaseException as error:
        state.update(status='failed', error=repr(error),
            accepted_input_remains_available=True, partial_outputs_are_not_accepted_automatically=True)
        event('sequence_failed', error=repr(error))
        raise


if __name__ == '__main__':
    main()
