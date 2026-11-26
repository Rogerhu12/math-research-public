#!/usr/bin/env python3
"""Original finite nonlinear DN: complete low modes, then the full M24 height.

Use the actual accepted original lambda=.002/M24 prefix height in this runner.
M8/N128 requests all first eight modes at factors .25/.5/.75/.9/1; M16/N256
and M24/N512 then request their complete unscaled prefixes of that same H.
Only M/N and an unaccepted remeshed initial guess change. Every request uses
the original audit; the final M24 request also requires the full original J.
This does not solve prefix coupling, lambda=1, fixed-g refinement or closure.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import gzip
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import traceback

HELPER_SHA = '7a1ce40d5141c08f4d76b2bc201f3113b04d02f12f60c06809a9053ba03321cc'
REMESH_SHA = '91686f1c9e70c36ea53357101b619830015288354d1045116a75b5a9ce47667b'
RESOLUTIONS = ((8, 128), (16, 256), (24, 512))
M8_FACTORS = (.25, .5, .75, .9, 1.)
RUNTIME_KEYS = ('chordMaxCorrections', 'traceFile', 'initialCheckpoint')
PACKET_SOURCES = ('950f-tail-client-v3.py', '950f-tail-stage-port-v3.mjs',
    '950f-tail-stage-core.mjs', '950f-tail-stage-split.mjs',
    '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
    'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'tail-config', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    repo, work = args.repo.resolve(), args.work.resolve()
    source_run, baseline_path = args.source_run.resolve(), args.tail_config.resolve()
    out = args.outdir.resolve()
    if (repo == work or repo in work.parents or work not in out.parents
            or work not in source_run.parents or work not in baseline_path.parents):
        raise ValueError('All actual inputs and generated fields must stay in this outside-repo runner work directory')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    public, resume = scripts/'resume_20261126', scripts/'resume_m3'
    native = scripts/'resume_n4_tail/native_extended'
    helper_path = public/'continue_original_actual_dn_chord.py'
    if hashlib.sha256(helper_path.read_bytes()).hexdigest() != HELPER_SHA:
        raise ValueError('The reviewed source/native provenance helper changed')
    import importlib.util
    spec = importlib.util.spec_from_file_location('_low_modes_original_chord_helpers', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    digest, read, ref = helper.digest, helper.load, helper.reference
    state = dict(scope=__doc__, status='checking_actual_original_source', stages=[],
        source_hashes={}, result=dict(accepted=False, prefix_coupling_accepted=False,
        fixed_metric_refinement=False, complete_surface=False,
        original_m24_full_height_returned=False))
    tail = None

    def save():
        helper.write(out/'summary.json', state)

    def numeric_scalars(value):
        return {str(k): helper.diagnostic_json(v) for k, v in value.items()
                if v is None or isinstance(v, (bool, int, float))}

    def height_summary(height):
        values = np.asarray(height, dtype='<f8')
        return dict(count=int(values.size), nonzero_count=int(np.count_nonzero(values)),
            l1=float(np.sum(np.abs(values))), linf=float(np.max(np.abs(values))),
            f64le_sha256=hashlib.sha256(values.tobytes()).hexdigest())

    def observe_packet(packet_path, expected_request, config, native_source, manifest_path,
                       factor, M, N, returned=False):
        with gzip.open(packet_path, 'rt') as stream:
            packet = json.load(stream)
        response = packet['response']
        # This packet is bound to ITS OWN dimension/source, never the next M.
        if (packet['request'] != expected_request or packet['config'] != config
                or set(packet['source_sha256']) != set(PACKET_SOURCES)):
            raise ValueError('The saved original request/config/source identity differs')
        for name, expected in packet['source_sha256'].items():
            if digest(native_source/'scripts'/name) != expected:
                raise ValueError('Changed source of the saved packet: '+name)
        row = dict(modes=M, quadrature=N, factor=factor,
            full_height_at_current_modes=factor == 1.,
            original_m24_full_height=M == 24 and factor == 1.,
            requested_jacobian=expected_request['jacobian'], requested_audit=True,
            client_returned=returned, packet=ref(packet_path),
            native_manifest=ref(manifest_path), height=height_summary(expected_request['height']),
            converged=response.get('converged'), failed=bool(response.get('failed')),
            residual=helper.diagnostic_json(response.get('residual')))
        if isinstance(response.get('audit'), dict):
            row['audit'] = numeric_scalars(response['audit'])
        if isinstance(response.get('history'), list) and response['history']:
            row['last_original_iteration'] = numeric_scalars(response['history'][-1])
        checkpoint = response.get('checkpoint')
        if isinstance(checkpoint, dict):
            params = checkpoint.get('parameters', {})
            row['checkpoint'] = dict(modes=params.get('modes'), spacing=params.get('spacing'),
                physical_depth=params.get('physicalDepth'), shooting_parts=params.get('shootingParts'),
                stage_count=params.get('depth'), state_rows=len(checkpoint.get('states', [])))
        state['stages'].append(row)
        save()
        return response, row

    save()
    try:
        import numpy as np
        gate_path = public/'material_design_secant_predictor.py'
        gate = helper.module('_low_modes_accepted_original_source', gate_path)
        record, raw_arrays = gate.accepted_original(source_run, repo)
        del raw_arrays
        if record['modes'] != 24 or record['core_settings']['homotopy'] != .002:
            raise ValueError('This entry requires the actual original lambda=.002/M24 source')
        command = list(record['command'])
        original_source = Path(helper.option(command, '--source-topic')).resolve()
        port_path = Path(helper.option(command, '--port')).resolve()
        port, baseline = read(port_path), read(baseline_path)
        if (digest(baseline_path) != port['source']['config_sha256']
                or any(key in baseline for key in RUNTIME_KEYS)
                or baseline['modes'] != 24 or baseline['spacing'] != 3
                or baseline['quadrature'] != 512):
            raise ValueError('Use the unchanged original M24/N512 baseline config bound by the actual source port')
        H = np.asarray(record['raw_return']['candidate_H'], dtype=float)
        if H.shape != (24,) or not np.all(np.isfinite(H)):
            raise ValueError('The actual source must retain all 24 finite height coefficients')
        raw = source_run.parent/record['raw_return']['file']
        physical = source_run.parent/'physical.npz'
        if digest(raw) != record['raw_return']['sha256'] or digest(physical) != record['physical_sha256']:
            raise ValueError('The actual original field identity changed')
        height_path = out/'height-reference.json'
        helper.write(height_path, dict(scope='Complete actual M24 source candidate_H, retained only in runner',
            source_run=ref(source_run), raw=ref(raw), physical=ref(physical),
            field='raw_return.candidate_H', candidate_H=H.tolist(),
            source_homotopy=record['core_settings']['homotopy'],
            gauge_q=record['gauge_q'], source_mean_nodes=record['prefix_audit']['samples_psi'],
            warm_arithmetic='NumPy H[:M] * factor**arange(1,M+1); factor=1 uses an exact copy'))

        # The identical bootstrap/native and chord provenance checks are reused
        # from the published original lambda-one DN attachment, without invoking
        # that lambda-one solver or changing this source's genuine identity.
        chord, executable = work/'chord-source', work/'frozen_flow_batch'
        setup_path = work/'recovery-setup.json'
        setup = read(setup_path)
        bootstrap_path = work/'native-tail24/native-manifest.json'
        if (digest(executable) != setup['generated']['frozen_flow_batch']
                or digest(bootstrap_path) != setup['generated']['native-tail24/native-manifest.json']):
            raise ValueError('The actual bootstrap native executable or manifest changed')
        bootstrap = read(bootstrap_path)
        helper.verify_references(bootstrap)
        if (bootstrap['native_files']['executable'] != ref(executable)
                or bootstrap['native_files']['cpp'] != ref(native/'frozen_flow_production.cpp')
                or bootstrap['native_files']['header'] != ref(native/'frozen_flow.h')):
            raise ValueError('The reused native binary lost its original source binding')
        install_path = work/'chord-install.json'
        installed = read(install_path)
        if (Path(installed['destination']).resolve() != chord
                or installed['status'] != 'installed_and_syntax_checked'
                or installed['installer_sha256'] != digest(resume/'install_bounded_chord_tail.py')
                or installed['patched_stage_source_sha256'] != digest(chord/'scripts/950f-tail-stage-core.mjs')
                or installed['original_stage_source_sha256'] != digest(
                    Path(installed['source_topic'])/'scripts/950f-tail-stage-core.mjs')
                or installed['final_accepted_stage_jacobians'] != 'fresh original full evaluation'):
            raise ValueError('The preinstalled original bounded-chord source binding changed')
        helper.equal_prefix_python(original_source, chord)
        if digest(chord/'scripts/950f-tail-warm-remesh.mjs') != REMESH_SHA:
            raise ValueError('The original complete-state remesh source changed')
        state['input'] = dict(source_run=ref(source_run), raw=ref(raw), physical=ref(physical),
            source_homotopy=.002, source_modes=24, source_prefix_original_gates_passed=True,
            source_mean_nodes=record['prefix_audit']['samples_psi'], gauge_q=record['gauge_q'],
            source_rms=record['raw_return']['rms'], source_metric=record['prefix_audit']['metric_l1'],
            source_physical_bc=record['prefix_audit']['physical_bc_max'],
            port=ref(port_path), baseline_config=ref(baseline_path),
            height_reference=ref(height_path), height=height_summary(H),
            height_reference_key='candidate_H', recovery_setup=ref(setup_path),
            bootstrap_native_manifest=ref(bootstrap_path), chord_install=ref(install_path),
            native_executable=ref(executable), native_workers=helper.WORKERS,
            physical_depth=baseline['depth'], shooting_parts=baseline['shootingParts'],
            rk_steps=baseline['steps'], audit_steps=baseline['auditSteps'],
            original_solve_tolerance=baseline['solveTolerance'])
        files = (Path(__file__), helper_path, gate_path, public/'material_design_continue.py',
            native/'prepare_recovered_native.py', native/'native_batch_adapter.mjs',
            native/'native_batch_factory.mjs', native/'parallel_native_batch.py',
            native/'frozen_flow_production.cpp', native/'frozen_flow.h',
            chord/'scripts/950f-tail-warm-remesh.mjs')
        state['source_hashes'] = {str(path.resolve()): digest(path) for path in files}
        env = dict(os.environ, PYTHONUNBUFFERED='1',
            VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
            VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        for key in ('LD_PRELOAD', 'LD_LIBRARY_PATH'):
            env.pop(key, None)
        save()
        previous_packet = None
        previous_sha = None
        for M, N in RESOLUTIONS:
            stage = out/f'm{M:02d}'
            stage.mkdir(exist_ok=False)
            native_source = stage/'native-source'
            native_runs = stage/'native-runs'
            manifest_path = native_source/'native-manifest.json'
            prepare = [sys.executable, str(native/'prepare_recovered_native.py'),
                '--source-topic', str(chord), '--dest', str(native_source),
                '--native-cli', str(executable), '--modes', str(M), '--spacing', '3',
                '--quadrature', str(N), '--steps', str(baseline['steps']),
                '--workers', str(helper.WORKERS)]
            state['status'] = f'preparing_native_m{M}'
            state['result']['current_modes'] = M
            save()
            with (stage/'prepare.log').open('x') as stream:
                subprocess.run(prepare, cwd=repo, env=env, stdout=stream,
                               stderr=subprocess.STDOUT, check=True)
            manifest = read(manifest_path)
            helper.verify_references(manifest)
            scope = dict(M=M, spacing=3, quadrature=N, steps=baseline['steps'],
                         projectionFloor=.05, orientation=1, cuspAwareFlow=True)
            if (manifest['schema'] != 'n4-native-batch-adapter-v1'
                    or Path(manifest['source_topic']).resolve() != native_source
                    or Path(manifest['original_source_topic']).resolve() != chord
                    or manifest['fixed_scope'] != scope
                    or manifest['execution_provider']['workers'] != helper.WORKERS):
                raise ValueError('The fresh dimension-specific native binding differs')
            runtime = copy.deepcopy(baseline)
            runtime.update(modes=M, quadrature=N, chordMaxCorrections=3,
                           traceFile=str(stage/'worker-trace.jsonl'))
            if previous_packet is not None:
                if digest(previous_packet) != previous_sha:
                    raise ValueError('The just-accepted previous-M packet changed')
                runtime['initialCheckpoint'] = str(previous_packet)
            exclude = (*RUNTIME_KEYS, 'modes', 'quadrature')
            if ({k:v for k,v in runtime.items() if k not in exclude}
                    != {k:v for k,v in baseline.items() if k not in exclude}):
                raise ValueError('A physical/depth/parts/tolerance input changed during mode continuation')
            runtime_path = stage/'tail-settings.json'
            helper.write(runtime_path, runtime)
            if native_runs.exists():
                raise FileExistsError('The native evaluator creates its own fresh run directory')
            stage_env = dict(env, VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest_path),
                VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=digest(manifest_path),
                VISIBLE_FLEX_NATIVE_RUN_DIR=str(native_runs))
            os.environ.update(stage_env)
            for key in ('LD_PRELOAD', 'LD_LIBRARY_PATH'):
                os.environ.pop(key, None)
            state['result']['current_native_manifest'] = ref(manifest_path)
            state['result']['current_runtime_config'] = ref(runtime_path)
            state['result']['previous_mode_initializer'] = (ref(previous_packet)
                if previous_packet is not None else None)
            state['status'] = f'initializing_original_worker_m{M}'
            save()
            client_path = native_source/'scripts/950f-tail-client-v3.py'
            client = helper.module('_low_modes_actual_client_'+str(M), client_path)
            tail = client.WeightedTailPort(runtime_path, native_source/'repro/source-root',
                                          stage/'tail', node_heap=2048)
            factors = M8_FACTORS if M == 8 else (1.,)
            for factor in factors:
                height = H[:M].copy() if factor == 1. else H[:M]*factor**np.arange(1, M+1)
                final = M == 24 and factor == 1.
                request = dict(height=height.tolist(), jacobian=final, audit=True)
                state['status'] = 'original_full_m24_height_running' if final else 'original_low_mode_tail_running'
                state['result']['current_request'] = dict(modes=M, quadrature=N, factor=factor,
                    original_m24_full_height=final, requested_jacobian=final,
                    requested_audit=True, height=height_summary(height))
                save()
                packet_path = stage/f'tail_{tail.calls+1:04d}.json.gz'
                try:
                    response = tail.solve(height, jacobian=final, audit=True)
                except Exception:
                    if packet_path.is_file():
                        observe_packet(packet_path, request, runtime, native_source,
                                       manifest_path, factor, M, N, returned=False)
                    raise
                response, row = observe_packet(packet_path, request, runtime, native_source,
                    manifest_path, factor, M, N, returned=True)
                # These are the same original finite response/residual/audit and
                # full-J checks as tail_solve_recorded_height.py, not a new norm.
                if (response.get('converged') is not True or not math.isfinite(response['residual'])
                        or response['residual'] > runtime['solveTolerance']
                        or response.get('audit') is None):
                    raise ValueError('The original finite nonlinear response/audit gate failed')
                if final:
                    jac = response.get('heightJetJacobian')
                    if (not isinstance(jac, list) or len(jac) != (3*M+2)*M
                            or not all(math.isfinite(v) for v in jac)):
                        raise ValueError('The original full M24 height Jacobian did not return')
                    row['full_height_jacobian_count'] = len(jac)
                    row['full_height_jacobian_finite'] = True
                row['original_finite_response_passed'] = True
                previous_packet, previous_sha = packet_path, digest(packet_path)
                save()
            tail.close()
            tail = None
        state['status'] = 'original_full_m24_height_tail_returned'
        state['result'].update(accepted=True, original_m24_full_height_returned=True,
            full_height_record=str(previous_packet), full_height_record_sha256=previous_sha,
            height_reference=str(height_path), height_reference_sha256=digest(height_path),
            height_reference_key='candidate_H', prefix_coupling_accepted=False,
            source_homotopy=.002, lambda_one_reached=False, complete_surface=False)
        save()
        return 0
    except Exception as exc:
        error_path = out/'exception.txt'
        error_path.write_text(traceback.format_exc())
        state.update(status='original_tail_route_failed', error=type(exc).__name__)
        state['result'].update(accepted=False, exception_record=ref(error_path))
        save()
        return 2
    finally:
        if tail is not None:
            tail.close()


if __name__ == '__main__':
    sys.exit(main())
