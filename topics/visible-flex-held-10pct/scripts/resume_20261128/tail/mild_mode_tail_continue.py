#!/usr/bin/env python3
"""Original complete-height nonlinear tail with modes raised at a mild amplitude.

The previous M8 full-amplitude -> M16 remesh returned a failed original worker
response. This independent continuation raises M at factor .5 instead, then
raises the full original height at the final M. Every accepted request retains
the original residual/guard/audit contract; the final request also pays J.
Generated packets and fields stay outside Git. This is an actual original DN
solver, not prefix coupling, fixed-g refinement, or a closed-surface claim.
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
DEFAULT_MODES = (8, 12, 16, 24, 32, 40, 48, 56, 64)
INITIAL_FACTORS = (.25, .5)
FINAL_FACTORS = (.5, .625, .75, .875, .9375, 1.)
RUNTIME_KEYS = ('chordMaxCorrections', 'traceFile', 'initialCheckpoint')
PACKET_SOURCES = ('950f-tail-client-v3.py', '950f-tail-stage-port-v3.mjs',
    '950f-tail-stage-core.mjs', '950f-tail-stage-split.mjs',
    '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
    'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'tail-config', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--workers', type=int, choices=(1, 2, 3, 4), default=2)
    parser.add_argument('--resume-summary', type=Path,
                        help='Continue only from an actual accepted packet of this identical source')
    parser.add_argument('--final-factors', type=float, nargs='+', default=FINAL_FACTORS)
    parser.add_argument('--stop-after-modes', type=int,
                        help='Return an intermediate accepted packet for separate resource scheduling')
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
    spec = importlib.util.spec_from_file_location('_mild_mode_original_chord_helpers', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    digest, read, ref = helper.digest, helper.load, helper.reference
    state = dict(scope=__doc__, status='checking_actual_original_source', stages=[],
        source_hashes={}, result=dict(accepted=False, prefix_coupling_accepted=False,
        fixed_metric_refinement=False, complete_surface=False,
        original_full_height_returned=False))
    tail = None
    final_factors = tuple(args.final_factors)
    if (not final_factors or final_factors[0] != .5 or final_factors[-1] != 1.
            or any(not math.isfinite(f) for f in final_factors)
            or any(a >= b for a, b in zip(final_factors, final_factors[1:]))):
        raise ValueError('Final continuation must increase strictly from .5 to complete factor 1')

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
            original_full_height=M == full_M and factor == 1.,
            requested_jacobian=expected_request['jacobian'], requested_audit=True,
            client_returned=returned, packet=ref(packet_path),
            native_manifest=ref(manifest_path), height=height_summary(expected_request['height']),
            converged=response.get('converged'), failed=bool(response.get('failed')),
            residual=helper.diagnostic_json(response.get('residual')))
        if isinstance(response.get('audit'), dict):
            row['audit'] = numeric_scalars(response['audit'])
        if isinstance(response.get('history'), list) and response['history']:
            row['last_original_iteration'] = numeric_scalars(response['history'][-1])
        if response.get('failed'):
            row['failure_message'] = str(response['failed'])[:2000]
        if isinstance(response.get('lastIteration'), dict):
            row['failed_last_original_iteration'] = numeric_scalars(response['lastIteration'])
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
        gate = helper.module('_mild_mode_accepted_original_source', gate_path)
        record, raw_arrays = gate.accepted_original(source_run, repo)
        del raw_arrays
        full_M = int(record['modes'])
        homotopy = float(record['core_settings']['homotopy'])
        if full_M not in DEFAULT_MODES or not (0 <= homotopy <= 1):
            raise ValueError('Use a declared accepted original source with supported full dimension')
        if args.stop_after_modes is not None and args.stop_after_modes not in DEFAULT_MODES:
            raise ValueError('The scheduling boundary must be one of the declared modes')
        command = list(record['command'])
        original_source = Path(helper.option(command, '--source-topic')).resolve()
        port_path = Path(helper.option(command, '--port')).resolve()
        port, baseline = read(port_path), read(baseline_path)
        if (digest(baseline_path) != port['source']['config_sha256']
                or any(key in baseline for key in RUNTIME_KEYS)
                or baseline['modes'] != full_M or baseline['spacing'] != 3
                or baseline['quadrature'] <= 12*full_M):
            raise ValueError('Use the unchanged full-dimension baseline config bound by the actual source port')
        H = np.asarray(record['raw_return']['candidate_H'], dtype=float)
        if H.shape != (full_M,) or not np.all(np.isfinite(H)):
            raise ValueError('The actual source must retain all of its finite height coefficients')
        raw = source_run.parent/record['raw_return']['file']
        physical = source_run.parent/'physical.npz'
        if digest(raw) != record['raw_return']['sha256'] or digest(physical) != record['physical_sha256']:
            raise ValueError('The actual original field identity changed')
        height_path = out/'height-reference.json'
        helper.write(height_path, dict(scope='Complete actual source candidate_H, retained only in runner',
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
            source_homotopy=homotopy, source_modes=full_M, source_prefix_original_gates_passed=True,
            source_mean_nodes=record['prefix_audit']['samples_psi'], gauge_q=record['gauge_q'],
            source_rms=record['raw_return']['rms'], source_metric=record['prefix_audit']['metric_l1'],
            source_physical_bc=record['prefix_audit']['physical_bc_max'],
            port=ref(port_path), baseline_config=ref(baseline_path),
            height_reference=ref(height_path), height=height_summary(H),
            height_reference_key='candidate_H', recovery_setup=ref(setup_path),
            bootstrap_native_manifest=ref(bootstrap_path), chord_install=ref(install_path),
            native_executable=ref(executable), native_workers=args.workers,
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
        resumed_modes, resumed_factor = 0, 0.
        if args.resume_summary is not None:
            old_path = args.resume_summary.resolve()
            if work not in old_path.parents:
                raise ValueError('The actual continuation summary must be in the same work directory')
            old = read(old_path)
            for key in ('source_run', 'raw', 'physical', 'baseline_config'):
                if old['input'][key] != state['input'][key]:
                    raise ValueError('Resume source identity changed: '+key)
            accepted = [row for row in old.get('stages', [])
                        if row.get('original_finite_response_passed') is True]
            if not accepted:
                raise ValueError('The previous run has no actual accepted packet to continue')
            last = accepted[-1]
            previous_packet = Path(last['packet']['path']).resolve()
            previous_sha = last['packet']['sha256']
            old_native_path = Path(last['native_manifest']['path']).resolve()
            if (work not in previous_packet.parents or work not in old_native_path.parents
                    or digest(previous_packet) != previous_sha
                    or digest(old_native_path) != last['native_manifest']['sha256']):
                raise ValueError('The actual accepted resume packet/native binding changed')
            old_native = read(old_native_path)
            helper.verify_references(old_native)
            with gzip.open(previous_packet, 'rt') as stream:
                packet = json.load(stream)
            old_response = packet['response']
            resumed_modes, resumed_factor = int(last['modes']), float(last['factor'])
            expected = (H[:resumed_modes].copy() if resumed_factor == 1. else
                        H[:resumed_modes]*resumed_factor**np.arange(1, resumed_modes+1))
            if (packet['request'] != dict(height=expected.tolist(),
                    jacobian=resumed_modes == full_M and resumed_factor == 1., audit=True)
                    or packet['config']['modes'] != resumed_modes
                    or packet['config']['quadrature'] != last['quadrature']
                    or old_response.get('converged') is not True
                    or old_response.get('failed')
                    or not math.isfinite(old_response.get('residual', math.nan))
                    or old_response['residual'] > packet['config']['solveTolerance']
                    or not isinstance(old_response.get('audit'), dict)
                    or set(packet['source_sha256']) != set(PACKET_SOURCES)):
                raise ValueError('The resume packet is not an original accepted audited response for this H')
            for name, expected_sha in packet['source_sha256'].items():
                if digest(Path(old_native['source_topic'])/'scripts'/name) != expected_sha:
                    raise ValueError('The source of the resume response changed: '+name)
            if resumed_modes == full_M and resumed_factor == 1.:
                jac = old_response.get('heightJetJacobian')
                if (not isinstance(jac, list) or len(jac) != (3*full_M+2)*full_M
                        or not all(math.isfinite(v) for v in jac)):
                    raise ValueError('The complete resume response is missing its original full height Jacobian')
            state['resumed_from'] = dict(summary=ref(old_path), accepted_packet=ref(previous_packet),
                modes=resumed_modes, factor=resumed_factor, accepted_response_recomputed=False)
            # Keep the accepted packet available as a further resume anchor even
            # if the first new request fails. It remains explicitly inherited.
            state['stages'].append(dict(last, inherited_from_summary=ref(old_path)))
            save()
        resolutions = [(M, (int(baseline['quadrature']) if M == full_M else 16*M))
                       for M in DEFAULT_MODES if M <= full_M]
        state['continuation'] = dict(resolutions=resolutions, initial_factors=INITIAL_FACTORS,
            intermediate_factors=[.5], final_factors=final_factors,
            original_full_height_factor=1., previous_full_amplitude_jump_repeated=False)
        save()
        for M, N in resolutions:
            factors = (INITIAL_FACTORS + final_factors[1:] if full_M == 8 else
                       INITIAL_FACTORS if M == 8 else
                       final_factors if M == full_M else (.5,))
            factors = tuple(f for f in factors
                            if M > resumed_modes or (M == resumed_modes and f > resumed_factor))
            if not factors:
                continue
            stage = out/f'm{M:02d}'
            stage.mkdir(exist_ok=False)
            native_source = stage/'native-source'
            native_runs = stage/'native-runs'
            manifest_path = native_source/'native-manifest.json'
            prepare = [sys.executable, str(native/'prepare_recovered_native.py'),
                '--source-topic', str(chord), '--dest', str(native_source),
                '--native-cli', str(executable), '--modes', str(M), '--spacing', '3',
                '--quadrature', str(N), '--steps', str(baseline['steps']),
                '--workers', str(args.workers)]
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
                    or manifest['execution_provider']['workers'] != args.workers):
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
            client = helper.module('_mild_mode_actual_client_'+str(M), client_path)
            tail = client.WeightedTailPort(runtime_path, native_source/'repro/source-root',
                                          stage/'tail', node_heap=2048)
            for factor in factors:
                height = H[:M].copy() if factor == 1. else H[:M]*factor**np.arange(1, M+1)
                final = M == full_M and factor == 1.
                request = dict(height=height.tolist(), jacobian=final, audit=True)
                state['status'] = 'original_complete_height_running' if final else 'original_low_mode_tail_running'
                state['result']['current_request'] = dict(modes=M, quadrature=N, factor=factor,
                    original_full_height=final, requested_jacobian=final,
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
                        raise ValueError('The original full height Jacobian did not return')
                    row['full_height_jacobian_count'] = len(jac)
                    row['full_height_jacobian_finite'] = True
                row['original_finite_response_passed'] = True
                previous_packet, previous_sha = packet_path, digest(packet_path)
                save()
            tail.close()
            tail = None
            if args.stop_after_modes is not None and M >= args.stop_after_modes and M < full_M:
                state['status'] = 'original_intermediate_mode_returned'
                state['result'].update(accepted=False, intermediate_audited_response=True,
                    original_full_height_returned=False, modes=M, factor=factor,
                    continuation_packet=ref(previous_packet), resource_scheduling_only=True)
                save()
                return 0
        state['status'] = 'original_complete_height_tail_returned'
        state['result'].update(accepted=True, original_full_height_returned=True,
            full_height_record=str(previous_packet), full_height_record_sha256=previous_sha,
            height_reference=str(height_path), height_reference_sha256=digest(height_path),
            height_reference_key='candidate_H', prefix_coupling_accepted=False,
            source_homotopy=homotopy, lambda_one_reached=homotopy == 1., complete_surface=False)
        save()
        return 0
    except Exception as exc:
        error_path = out/'exception.txt'
        error_path.write_text(traceback.format_exc())
        state.update(status='original_tail_route_failed', error=type(exc).__name__, error_message=str(exc)[:2400])
        state['result'].update(accepted=False, exception_record=ref(error_path))
        save()
        return 2
    finally:
        if tail is not None:
            tail.close()


if __name__ == '__main__':
    sys.exit(main())
