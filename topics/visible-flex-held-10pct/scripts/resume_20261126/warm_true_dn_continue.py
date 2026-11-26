#!/usr/bin/env python3
"""Prepare and observe original true DN for a real accepted warm lambda-one field.

This controller never manufactures a lambda-one source. It binds the actual
warm fixed-metric model, prepares the existing original native tail at its
actual M, and invokes warm_true_dn_solve.py. Generated arrays and complete
tail packets remain under work; compact scalar progress stays below 24 KiB.
"""
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            value.update(block)
    return value.hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def tail_text(path, limit=1800):
    if not path.exists():
        return ''
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size-limit))
        return stream.read().decode('utf-8', 'replace')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--tail-settings', type=Path,
        help='Optional exact base settings whose SHA is bound by the accepted source port')
    parser.add_argument('--native-source', type=Path,
        help='Optional existing owned native source at the identical M/spacing/quadrature')
    parser.add_argument('--initial-tail', type=Path,
        help='Same-source accepted complete audited packet, used only as a new Newton initializer')
    parser.add_argument('--tail-warmup', type=float, nargs='*', default=[.25, .5, .75, .9])
    parser.add_argument('--audit-angular', type=int, nargs='+')
    parser.add_argument('--rhs-block', type=int, default=8)
    parser.add_argument('--max-nodes', type=int, default=6000)
    args = parser.parse_args()
    repo, work, out = args.repo.resolve(), args.work.resolve(), args.outdir.resolve()
    source_path = args.source_run.resolve()
    if (work not in out.parents or work not in source_path.parents
            or repo == work or repo in work.parents):
        raise ValueError('The actual source and generated fields must stay in owned work outside Git')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    current = scripts/'resume_20261126'
    solver = current/'warm_true_dn_solve.py'
    state = dict(scope=__doc__, status='checking_real_lambda_one_input', progress={}, stages=[],
                 actual_tail_requested=True, fixed_metric_refinement=False,
                 complete_surface=False)
    process = stream = None

    def save():
        if len(json.dumps(state).encode()) > 24000:
            raise RuntimeError('Compact controller summary exceeded 24 KiB')
        write(out/'summary.json', state)

    save()
    try:
        spec = importlib.util.spec_from_file_location('_warm_actual_validators', solver)
        implementation = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(implementation)
        source = implementation.validate_warm_source(repo, source_path)
        modes = int(source['modes'])
        port = load(source['linear_port_path'])
        if args.tail_settings:
            cfg = load(args.tail_settings)
        else:
            cfg = load(work/'m24-tail-settings.json')
            cfg['modes'] = modes
            while int(cfg['quadrature']) <= 4*modes*int(cfg['spacing']):
                cfg['quadrature'] *= 2
        if any(key in cfg for key in ('traceFile', 'chordMaxCorrections', 'initialCheckpoint')):
            raise ValueError('Provide the exact source linear port base settings, without runtime fields')
        base_path = out/'base-tail-settings.json'
        if args.tail_settings:
            base_path.write_bytes(args.tail_settings.read_bytes())
        else:
            write(base_path, cfg)
        if sha(base_path) != port['source']['config_sha256']:
            raise ValueError('Derived settings do not bind the actual source port; provide --tail-settings with its exact recorded configuration')
        if (cfg['modes'] != modes or cfg['spacing'] != 3 or cfg['quadrature'] <= 4*modes*3
                or cfg['solveTolerance'] != 2e-9
                or any(key in cfg and cfg[key] != value for key, value in source['physical_tail_parameters'].items())):
            raise ValueError('The source physical tail parameters, dimension or original tolerance changed')
        env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
                   PYTHONUNBUFFERED='1', VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
                   VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                       'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        for key in ('LD_LIBRARY_PATH', 'LD_PRELOAD'):
            env.pop(key, None)
        state['source_hashes'] = {str(path): sha(path) for path in
            (Path(__file__), solver, source_path, Path(source['linear_port_path']), base_path)}
        state['result'] = dict(source_run=str(source_path), source_run_sha256=sha(source_path),
            source_raw_sha256=source['raw_return']['sha256'], source_physical_sha256=source['physical_sha256'],
            original_lambda_one_linear_source_accepted=True, modes=modes,
            mean_nodes=1168, gauge_q=source['gauge_q'], actual_delta=source['frozen_profile']['delta'])
        save()

        def run(name, command, child_directory=None):
            nonlocal process, stream
            command = list(map(str, command))
            write(out/(name+'-command.json'), dict(command=command,
                script_sha256=sha(command[2]) if len(command)>2 and Path(command[2]).is_file() else None))
            row = dict(name=name, status='running')
            state['stages'].append(row)
            state.update(status=name, progress=dict(current_stage=name))
            save()
            log = out/(name+'.log')
            stream = log.open('x')
            process = subprocess.Popen(command, cwd=repo, env=env, stdout=stream, stderr=subprocess.STDOUT)
            while process.poll() is None:
                if child_directory is not None and (child_directory/'summary.json').exists():
                    try:
                        detail = load(child_directory/'summary.json')
                        state['progress']['actual_solver'] = {key: detail[key] for key in
                            ('status', 'progress', 'result', 'error') if key in detail}
                        row['tail_stages'] = detail.get('stages', [])[-4:]
                    except (OSError, ValueError):
                        pass
                state['progress']['last_log'] = tail_text(log)
                save()
                time.sleep(15)
            code = process.returncode
            row.update(status='finished', returncode=code)
            stream.close()
            stream = process = None
            save()
            if code:
                raise RuntimeError(name+' returned '+str(code))

        if args.native_source:
            native = args.native_source.resolve()
        elif modes == 24 and cfg['quadrature'] == 512 and cfg['steps'] == 16:
            native = work/'native-tail24'
        else:
            native = out/'native-source'
            run('prepare_original_native', [sys.executable, '-u',
                scripts/'resume_n4_tail/native_extended/prepare_recovered_native.py',
                '--source-topic', work/'chord-source', '--dest', native,
                '--native-cli', work/'frozen_flow_batch', '--modes', modes, '--spacing', 3,
                '--quadrature', cfg['quadrature'], '--steps', cfg['steps'], '--workers', 2])
        if work not in native.parents:
            raise ValueError('The native source must remain under the owned work directory')
        manifest_path = native/'native-manifest.json'
        manifest = load(manifest_path)
        for key, expected in dict(M=modes, spacing=3, quadrature=cfg['quadrature'],
                                  steps=cfg['steps'], projectionFloor=.05,
                                  orientation=1, cuspAwareFlow=True).items():
            if manifest['fixed_scope'][key] != expected:
                raise ValueError('Native source dimension/geometry differs: '+key)
        if manifest['execution_provider']['workers'] != 2:
            raise ValueError('Retain the original declared two native workers')
        for ref in [*manifest['owned_sources'], *manifest['native_files'].values()]:
            if sha(ref['path']) != ref['sha256']:
                raise ValueError('An original native source/binary changed: '+ref['path'])
        core_text = (native/'scripts/950f-tail-stage-core.mjs').read_text()
        if 'bounded-chord-v1' not in core_text or 'fresh-original' not in core_text:
            raise ValueError('The recorded original-final-J bounded-chord path is required')
        actual = copy.deepcopy(cfg)
        actual.update(chordMaxCorrections=3, traceFile=str(out/'worker-trace.jsonl'))
        if args.initial_tail:
            packet_path = args.initial_tail.resolve()
            if work not in packet_path.parents:
                raise ValueError('The accepted warm packet must remain under work')
            with gzip.open(packet_path, 'rt') as source_file:
                packet = json.load(source_file)
            response, checkpoint = packet['response'], packet['response']['checkpoint']
            if (response.get('converged') is not True or response.get('failed')
                    or not implementation.finite_leq(response.get('residual'), 2e-9)
                    or packet['request'].get('audit') is not True
                    or not isinstance(response.get('audit'), dict)):
                raise ValueError('The initializer has not passed the original audited finite tail gate')
            for key, value in cfg.items():
                if packet['config'].get(key) != value:
                    raise ValueError('The accepted initializer configuration differs: '+key)
            names = {'950f-tail-client-v3.py', '950f-tail-stage-port-v3.mjs',
                '950f-tail-stage-core.mjs', '950f-tail-stage-split.mjs', '950f-tail-subdivision.mjs',
                '950f-tail-warm-remesh.mjs', 'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs'}
            if set(packet['source_sha256']) != names:
                raise ValueError('The initializer lacks the full original client/worker identity')
            for name, expected in packet['source_sha256'].items():
                if sha(native/'scripts'/name) != expected:
                    raise ValueError('The initializer original tail source changed: '+name)
            states, height, parameters = checkpoint['states'], checkpoint['cutHeight'], checkpoint['parameters']
            if (parameters['modes'] != modes or parameters['spacing'] != 3
                    or len(states) != parameters['depth']+1 or len(height) != modes
                    or height != packet['request']['height']
                    or not all(math.isfinite(value) for value in height)
                    or any(len(row) != 2*modes or not all(math.isfinite(value) for value in row)
                           for row in states)):
                raise ValueError('The accepted initializer lacks the complete finite state')
            # depth counts every subdivided shooting interval. physicalDepth
            # counts physical cells and is the cfg.depth value. The original
            # v3 packet records both meshes; neither may be confused with M.
            physical_depth = parameters.get('physicalDepth', parameters['depth'])
            raw_nodes, raw_states = checkpoint['rawNode'], checkpoint['rawStates']
            if (physical_depth != cfg['depth']
                    or parameters['shootingParts'] != cfg.get('shootingParts', 1)
                    or not isinstance(raw_nodes, list) or len(raw_nodes) != physical_depth+1
                    or raw_nodes[0] != 0 or raw_nodes[-1] != parameters['depth']
                    or any(not isinstance(node, int) for node in raw_nodes)
                    or any(right <= left for left, right in zip(raw_nodes[:-1], raw_nodes[1:]))
                    or len(raw_states) != len(raw_nodes)
                    or any(row != states[node] for node, row in zip(raw_nodes, raw_states))):
                raise ValueError('The complete physical-cell and subdivided shooting meshes disagree')
            actual['initialCheckpoint'] = str(packet_path)
            state['source_hashes'][str(packet_path)] = sha(packet_path)
        actual_path = out/'tail-settings.json'
        write(actual_path, actual)
        (out/'native-runs').mkdir()
        state['source_hashes'].update({str(path): sha(path) for path in (actual_path, manifest_path)})
        child = out/'actual'
        command = [sys.executable, '-u', solver, '--repo', repo, '--work', work,
            '--source-run', source_path, '--native-source', native,
            '--base-tail-config', base_path, '--tail-config', actual_path, '--outdir', child,
            '--rhs-block', args.rhs_block, '--max-nodes', args.max_nodes,
            '--tail-warmup', *args.tail_warmup]
        if args.audit_angular:
            command.extend(['--audit-angular', *args.audit_angular])
        run('original_warm_true_dn', command, child)
        result = load(child/'run.json')
        accepted = bool(result.get('finite_actual_dn_candidate_pass') and not result.get('error'))
        state.update(status='actual_warm_true_dn_returned',
            result=dict(run=str(child/'run.json'), run_sha256=sha(child/'run.json'),
                        original_nonlinear_DN_accepted=accepted,
                        full_Cartesian_seam_paid=False, complete_surface=False,
                        actual=result.get('result')))
        save()
        return 0 if accepted else 2
    except Exception as error:
        if process is not None and process.poll() is None:
            process.send_signal(signal.SIGINT)
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
        if stream is not None:
            stream.close()
        child_file = out/'actual/summary.json'
        if child_file.exists():
            detail = load(child_file)
            state['progress']['actual_solver'] = {key: detail[key] for key in
                ('status', 'result', 'error') if key in detail}
        state.update(status='actual_warm_true_dn_failed', error=repr(error),
                     exception=traceback.format_exc().splitlines()[-24:])
        save()
        return 2


if __name__ == '__main__':
    sys.exit(main())
