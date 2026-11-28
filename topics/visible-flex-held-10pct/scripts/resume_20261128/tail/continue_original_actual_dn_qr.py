#!/usr/bin/env python3
"""Attach full native4/chord3/8outer DN using the complete prefix QR stack.

Independent resource successor of the byte-bound original 7a coordinator.
Only the original-support R53 family is admitted. Its complete portable
residuals, physical gates, raw/physical distinction, native requests and
final physical-height binding remain unchanged. The actual prefix executable
is explicitly the full CSR/QR/V5/checkpoint adapter, never the old streamed
SuperLU wrapper. Analytical delta and QR arithmetic are declared changes to
Jacobian evaluation and linear solution, not to the original equations.
Delta/support remain design unknowns; this is not fixed-g refinement or a
continuous closed-surface certificate. No old accepted field is relabelled.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import time
import traceback

PREFIX_PYTHON = (
    'db6f-prefix-coupled.py',
    '950f-prefix-adaptive-chart-bvp-v2.py',
    '950f-prefix-warped-bvp.py',
    '78718-prefix-fourier-jacobian.py',
)
RUNTIME_KEYS = ('chordMaxCorrections', 'traceFile', 'initialCheckpoint')
WORKERS = 4
ORIGINAL_ENTRY = Path(__file__).resolve().parents[2]/'resume_20261126/continue_original_actual_dn_chord.py'
ORIGINAL_ENTRY_SHA256 = '7a1ce40d5141c08f4d76b2bc201f3113b04d02f12f60c06809a9053ba03321cc'
SCHEMA = 'original-lambda-one-native4-chord3-outer8-prefix-qr-v1'
sys.path.insert(0, str(Path(__file__).resolve().parent))
import prefix_actual_dn_qr_driver as qr_execution


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def reference(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=digest(path))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def diagnostic_json(value):
    if isinstance(value, float) and not math.isfinite(value):
        return 'nonfinite:'+repr(value)
    if isinstance(value, dict):
        return {str(k): diagnostic_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [diagnostic_json(v) for v in value]
    return value


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(diagnostic_json(value), indent=2,
                                    allow_nan=False)+'\n')
    temporary.replace(path)


def option(command, flag):
    if command.count(flag) != 1:
        raise ValueError('Require one actual original argument: '+flag)
    return command[command.index(flag)+1]


def replace(command, flag, value):
    if flag in command:
        option(command, flag)
        command[command.index(flag)+1] = str(value)
    else:
        command.extend((flag, str(value)))


def verify_references(manifest):
    references = list(manifest['owned_sources'])+list(manifest['native_files'].values())
    references += manifest.get('runtime_libraries', [])
    references.append(manifest['installer'])
    for value in references:
        if digest(value['path']) != value['sha256']:
            raise ValueError('Changed native source or executable: '+value['path'])


def equal_prefix_python(left, right):
    result = {}
    for name in PREFIX_PYTHON:
        old, new = left/'scripts'/name, right/'scripts'/name
        old_sha, new_sha = digest(old), digest(new)
        if old_sha != new_sha:
            raise ValueError('The actual prefix Python changed: '+name)
        result[name] = dict(original=reference(old), replacement=reference(new),
                            bytes_equal=True)
    return result


def last_scalar_event(path):
    if not path.is_file():
        return None
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size-16384))
        lines = stream.read().decode('utf-8', errors='replace').splitlines()
    for line in reversed(lines):
        try:
            value = json.loads(line)
        except (ValueError, TypeError):
            continue
        if isinstance(value, dict):
            result = {}
            for key, item in value.items():
                if isinstance(item, (int, float, bool, type(None))):
                    result[key] = diagnostic_json(item)
                elif isinstance(item, str):
                    result[key] = item[:512]
            if result:
                return result
    return None


def check_streamed_provenance(path, actual_argv, wrapper, portable, block, expected_sha=None):
    path=Path(path)
    if expected_sha is not None and digest(path)!=expected_sha:
        raise ValueError('The saved streamed execution provenance changed')
    data=load(path)
    if (data.get('command')!=list(actual_argv)[1:]
            or data.get('wrapper_sha256')!=digest(wrapper)
            or data.get('original_driver_sha256')!=digest(portable)
            or data.get('radial_rhs_jacobian_block')!=block
            or data.get('mathematical_parameters_changed') is not False
            or data.get('original_gates_relaxed') is not False):
        raise ValueError('The actual streamed execution differs from its original portable contract')
    return reference(path)


def source_streamed_block(record, wrapper, portable):
    execution=record.get('execution_provenance')
    if execution is None:
        return None
    command=list(record['command'])
    if (not isinstance(execution,dict)
            or execution.get('original_portable_argv')!=command
            or execution.get('original_portable_command_fabricated') is not False):
        raise ValueError('The source execution provenance does not bind its real portable command')
    if execution.get('wrapper_invoked') is False:
        if execution.get('actual_argv')!=command:
            raise ValueError('The direct source execution argv differs')
        return None
    block=execution.get('streamed_rhs_block')
    if (execution.get('wrapper_invoked') is not True
            or not isinstance(block,int) or isinstance(block,bool) or block<1
            or Path(execution['wrapper']).resolve()!=wrapper.resolve()
            or execution.get('wrapper_sha256')!=digest(wrapper)):
        raise ValueError('The source streamed-wrapper identity or radial block differs')
    expected=[command[0],str(wrapper),'--rhs-block',str(block),*command[2:]]
    if execution.get('actual_argv')!=expected:
        raise ValueError('The source did not execute the recorded streamed argv')
    check_streamed_provenance(execution['provenance'],expected,wrapper,portable,block,
                              execution['provenance_sha256'])
    return block


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'tail-config', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--tail-warmup', type=float, nargs='*',
                        default=[.25, .5, .75, .9],
                        help='Explicit original harmonic warm factors; full H is always retained')
    parser.add_argument('--streamed-rhs-block', type=int, default=8,
        help='Use this positive radial block in the full CSR/QR/V5/checkpoint prefix adapter')
    args = parser.parse_args()
    if digest(ORIGINAL_ENTRY) != ORIGINAL_ENTRY_SHA256:
        raise ValueError('The byte-bound original 7a coordination source changed')
    if args.streamed_rhs_block is not None and args.streamed_rhs_block<1:
        raise ValueError('A positive radial block is required')
    repo, work = args.repo.resolve(), args.work.resolve()
    source_run, baseline_path = args.source_run.resolve(), args.tail_config.resolve()
    out = args.outdir.resolve()
    if (work == repo or repo in work.parents or work not in out.parents
            or work not in source_run.parents or work not in baseline_path.parents):
        raise ValueError('Actual fields and all generated data must remain in this outside-repo runner work directory')
    if (any(not math.isfinite(v) or not 0 < v < 1 for v in args.tail_warmup)
            or args.tail_warmup != sorted(set(args.tail_warmup))):
        raise ValueError('Warm factors must be strictly increasing inside (0,1)')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    public, resume = scripts/'resume_20261126', scripts/'resume_m3'
    native = scripts/'resume_n4_tail/native_extended'
    portable = resume/'portable_prefix_continue.py'
    legacy_wrapper = public/'streamed_release_prefix_driver.py'
    wrapper = Path(__file__).resolve().with_name('prefix_actual_dn_qr_driver.py')
    chord, executable = work/'chord-source', work/'frozen_flow_batch'
    native_source, native_runs = out/'native-source', out/'native-runs'
    actual = out/'actual'
    trace_path = out/'worker-trace.jsonl'
    summary = out/'summary.json'
    state = dict(schema=SCHEMA, scope=__doc__, status='checking_real_lambda_one_source', stages=[],
        original_coordination_source=reference(ORIGINAL_ENTRY),
        execution_backend='complete_original_prefix_CSR_QR_V5_checkpoints',
        native_full_J_replaced_by_prefix_QR=False, original_record_relabelled=False,
        progress={}, actual_tail_requested=True, fixed_metric_refinement=False,
        complete_surface=False, source_is_linear_candidate=True,
        prefix_delta_still_unknown=True, material_parameter_advanced=False,
        original_outer_budget=8, tail_warmup=list(args.tail_warmup),
        original_full_height_and_audit_preserved=True, native_workers=WORKERS)
    env = dict(os.environ, PYTHONUNBUFFERED='1',
        VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
        VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
            'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    for key in ('LD_PRELOAD', 'LD_LIBRARY_PATH'):
        env.pop(key, None)

    def save():
        write(summary, state)

    def invoke(name, command, require_success=True):
        command = list(map(str, command))
        log = out/(name+'.log')
        stage = dict(name=name, argv=command, log=str(log), status='running')
        state['stages'].append(stage)
        state['status'] = name
        state['progress'] = dict(stage=name)
        save()
        print(json.dumps(dict(event='command', name=name, argv=command)), flush=True)
        with log.open('x') as stream:
            process = subprocess.Popen(command, cwd=repo, env=env,
                                       stdout=stream, stderr=subprocess.STDOUT)
            while process.poll() is None:
                state['progress'] = dict(stage=name, process_running=True,
                    last_prefix_event=last_scalar_event(actual/'events.jsonl'),
                    last_original_tail_event=last_scalar_event(trace_path))
                save()
                time.sleep(15)
        stage.update(status='finished', returncode=process.returncode)
        state['progress']['process_running'] = False
        state['progress']['returncode'] = process.returncode
        save()
        if require_success and process.returncode:
            raise RuntimeError(name+' returned '+str(process.returncode))
        return process.returncode

    save()
    try:
        preliminary = load(source_run)
        if preliminary.get('model_kind') is not None:
            raise ValueError('This QR resource stack is reviewed only for the original R53 support family')
        if preliminary.get('core_settings', {}).get('homotopy') != 1:
            raise ValueError('A real lambda-one source is required before any native preparation')
        if not isinstance(preliminary.get('modes'), int) or not 1 <= preliminary['modes'] <= 64:
            raise ValueError('Retain the native 1<=M<=64 ABI gate')
        if preliminary.get('model_kind') is None:
            gate_file = public/'material_design_secant_predictor.py'
            gate = module('_chord_original_r53_input', gate_file)
            record, source_arrays = gate.accepted_original(source_run, repo)
            del source_arrays
            family = 'original-R53-material-support'
            if record['core_settings'].get('curvature_blend') != 1:
                raise ValueError('The declared lambda-one R53 source also retains curvature_blend=1')
        else:
            gate_file = public/'warm_delta_phase_entry_v5.py'
            gate = module('_chord_v5_input', gate_file)
            if preliminary.get('model_kind') != gate.KIND:
                raise ValueError('Only original R53 or the explicitly declared v5 family is supported')
            record = gate.accepted_input(source_run)
            if record.get('acceptance_kind') != gate.SOLVER_RETURN or record.get('solver_invoked') is not True:
                raise ValueError('A v5 zero-control reexpression is not a true solver return')
            family = gate.KIND
        command = list(record['command'])
        if Path(command[1]).resolve() != portable.resolve():
            raise ValueError('The genuine source command must be the original portable driver')
        if any(flag in command for flag in ('--tail-config', '--tail-warmup', '--skip-audit', '--probe-only')):
            raise ValueError('Only an actually audited linear-DN source may start this attachment')
        source_block=source_streamed_block(record,legacy_wrapper,portable)
        # The old source may bind its own direct/streamed execution; this new
        # process always selects the honestly recorded complete QR resource stack.
        streamed_block=args.streamed_rhs_block
        original_source = Path(option(command, '--source-topic')).resolve()
        raw = (source_run.parent/record['raw_return']['file']).resolve()
        physical = source_run.parent/'physical.npz'
        if work not in raw.parents:
            raise ValueError('The actual raw checkpoint must stay in this runner')
        if digest(raw) != record['raw_return']['sha256'] or digest(physical) != record['physical_sha256']:
            raise ValueError('The actual source raw/physical identity changed')
        for group in ('source_hashes', 'inputs'):
            for path, expected in record[group].items():
                if digest(path) != expected:
                    raise ValueError('Changed actual source/input: '+path)
        profile = load(option(command, '--profile'))
        chart = load(option(command, '--chart'))
        port_path = Path(option(command, '--port')).resolve()
        port = load(port_path)
        expected_cut = dict(port['cut'], _prefix_bridge=profile['prefix_bridge'])
        if (profile != record['physical_profile'] or chart != record['angular_chart']
                or port['parameters'] != record['physical_tail_parameters']
                or expected_cut != record['physical_tail_cut']
                or load(option(command, '--core-config')) != record['core_settings']):
            raise ValueError('The full source profile/chart/core/physical port contract differs')
        baseline = load(baseline_path)
        if digest(baseline_path) != port['source']['config_sha256']:
            raise ValueError('The baseline tail config must match the actual original port SHA')
        if any(key in baseline for key in RUNTIME_KEYS):
            raise ValueError('Use the original baseline config, without runtime execution additions')
        M = record['modes']
        spacing, N, steps = (baseline[key] for key in ('spacing', 'quadrature', 'steps'))
        if (any(not isinstance(v, int) or isinstance(v, bool) or v < 1 for v in (M,spacing,N,steps))
                or M > 64 or spacing != 3 or N <= 4*M*spacing
                or baseline['modes'] != M or int(option(command, '--modes')) != M
                or int(option(command, '--angular')) != record['angular']
                or port['modes'] != [spacing*j for j in range(1,M+1)]
                or float(option(command, '--amplitude')) != record['gauge_q']
                or float(option(command, '--warp-reference')) != record['warp_reference']):
            raise ValueError('Original mode/gauge/native ABI or strict angular quadrature contract failed')
        mean_nodes = record['prefix_audit']['samples_psi']
        if (not isinstance(mean_nodes, int) or isinstance(mean_nodes, bool)
                or mean_nodes != max(int(option(command, '--audit-angular')),16*(3*M+1))):
            raise ValueError('Retain the actual original literal finite-mean grid')
        if record['gates'].get('original_outer_budget') != 8:
            raise ValueError('The original eight-outer budget must remain explicit')

        # Reuse only this bootstrap's actual compiled binary and source binding.
        setup_path = work/'recovery-setup.json'
        setup = load(setup_path)
        bootstrap_manifest_path = work/'native-tail24/native-manifest.json'
        if (digest(executable) != setup['generated']['frozen_flow_batch']
                or digest(bootstrap_manifest_path) != setup['generated']['native-tail24/native-manifest.json']):
            raise ValueError('The already prepared native executable/bootstrap manifest changed')
        bootstrap_manifest = load(bootstrap_manifest_path)
        verify_references(bootstrap_manifest)
        if (bootstrap_manifest['native_files']['executable'] != reference(executable)
                or bootstrap_manifest['native_files']['cpp'] != reference(native/'frozen_flow_production.cpp')
                or bootstrap_manifest['native_files']['header'] != reference(native/'frozen_flow.h')):
            raise ValueError('The reused native binary lost its actual original source binding')
        chord_install_path = work/'chord-install.json'
        chord_install = load(chord_install_path)
        if (Path(chord_install['destination']).resolve() != chord
                or chord_install['status'] != 'installed_and_syntax_checked'
                or chord_install['installer_sha256'] != digest(resume/'install_bounded_chord_tail.py')
                or chord_install['patched_stage_source_sha256'] != digest(chord/'scripts/950f-tail-stage-core.mjs')
                or chord_install['original_stage_source_sha256'] != digest(
                    Path(chord_install['source_topic'])/'scripts/950f-tail-stage-core.mjs')
                or chord_install['final_accepted_stage_jacobians'] != 'fresh original full evaluation'):
            raise ValueError('The preinstalled original bounded-chord source binding changed')
        prefix_before = equal_prefix_python(original_source, chord)
        state['input'] = dict(source_run=reference(source_run), raw=reference(raw),
            physical=reference(physical), source_family=family,
            source_model_kind=record.get('model_kind'),
            source_acceptance_kind=record.get('acceptance_kind'),
            source_execution_provenance=copy.deepcopy(record.get('execution_provenance')),
            source_streamed_rhs_block=source_block,selected_streamed_rhs_block=streamed_block,
            actual_prefix_backend='complete_original_prefix_CSR_QR_V5_checkpoints',
            source_core_settings=copy.deepcopy(record['core_settings']),
            original_base_profile=copy.deepcopy(record['physical_profile']),
            source_actual_profile=copy.deepcopy(record['frozen_profile']),
            physical_tail_parameters=copy.deepcopy(record['physical_tail_parameters']),
            physical_tail_cut=copy.deepcopy(record['physical_tail_cut']),
            angular_chart=copy.deepcopy(record['angular_chart']),
            gauge_q=record['gauge_q'], warp_reference=record['warp_reference'],
            modes=M, angular=record['angular'], source_mean_nodes=mean_nodes,
            original_gates=copy.deepcopy(record['gates']),
            bc_normalization=record['gates']['physical_bc_tol']/record['gates']['bc_tol'],
            parameter_zero_meaning='additive delta increment',
            port=reference(port_path), baseline_tail_config=reference(baseline_path),
            recovery_setup=reference(setup_path),
            bootstrap_native_manifest=reference(bootstrap_manifest_path),
            bootstrap_manifest_scope='Executable/source provenance only, not the M-specific runtime manifest',
            native_executable=reference(executable), chord_install=reference(chord_install_path),
            prefix_python_equivalence_before_native=prefix_before)
        files = [Path(__file__), gate_file, portable,
            public/'material_design_continue.py', resume/'continue_material_true_tail.py',
            resume/'install_bounded_chord_tail.py', public/'tail_recovery_setup.py',
            native/'prepare_recovered_native.py', native/'native_batch_adapter.mjs',
            native/'native_batch_factory.mjs', native/'parallel_native_batch.py',
            native/'frozen_flow_production.cpp', native/'frozen_flow.h']
        files.extend([ORIGINAL_ENTRY, *qr_execution.source_files()])
        state['source_hashes'] = {str(path.resolve()):digest(path) for path in files}
        save()
        invoke('prepare_actual_native4', [sys.executable, native/'prepare_recovered_native.py',
            '--source-topic', chord, '--dest', native_source, '--native-cli', executable,
            '--modes', M, '--spacing', spacing, '--quadrature', N,
            '--steps', steps, '--workers', WORKERS])
        manifest_path = native_source/'native-manifest.json'
        manifest = load(manifest_path)
        verify_references(manifest)
        expected_scope = dict(M=M,spacing=spacing,quadrature=N,steps=steps,
                              projectionFloor=.05,orientation=1,cuspAwareFlow=True)
        if (manifest['schema'] != 'n4-native-batch-adapter-v1'
                or Path(manifest['source_topic']).resolve() != native_source
                or Path(manifest['original_source_topic']).resolve() != chord
                or manifest['fixed_scope'] != expected_scope
                or manifest['execution_provider']['workers'] != WORKERS):
            raise ValueError('The fresh actual-M native binding differs')
        state['native'] = dict(manifest=reference(manifest_path),
            executable=reference(executable), fixed_scope=expected_scope, workers=WORKERS,
            prefix_python_equivalence=equal_prefix_python(original_source,native_source))
        runtime = copy.deepcopy(baseline)
        runtime.update(chordMaxCorrections=3,traceFile=str(trace_path))
        runtime_path = out/'runtime-tail-settings.json'
        runtime_path.write_text(json.dumps(runtime,indent=2,allow_nan=False)+'\n')
        if {k:v for k,v in runtime.items() if k not in RUNTIME_KEYS} != baseline:
            raise ValueError('The runtime config changed a baseline numerical or physical input')
        state['tail_configuration'] = dict(baseline=reference(baseline_path),
            baseline_matches_original_port_sha256=port['source']['config_sha256'],
            runtime=reference(runtime_path),
            additions=dict(chordMaxCorrections=3,traceFile=str(trace_path)),
            baseline_numerical_and_physical_inputs_unchanged=True)
        if native_runs.exists():
            raise FileExistsError('The native evaluator, not this entry, creates its fresh run directory')
        env.update(VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest_path),
                   VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=digest(manifest_path),
                   VISIBLE_FLEX_NATIVE_RUN_DIR=str(native_runs))
        command[0] = sys.executable
        for flag in ('--control-record','--restart-checkpoint'):
            if flag in command:
                option(command,flag)
                index=command.index(flag)
                del command[index:index+2]
        for flag,value in (('--source-topic',native_source),('--raw-restart',raw),
                           ('--tail-config',runtime_path),('--outdir',actual)):
            replace(command,flag,value)
        if args.tail_warmup:
            command.extend(['--tail-warmup',*map(str,args.tail_warmup)])
        executed=(list(command) if streamed_block is None else
            [sys.executable,str(wrapper),'--rhs-block',str(streamed_block),*command[2:]])
        state['original_portable_command'] = list(command)
        state['actual_command'] = executed
        state['result'] = dict(actual_process_returned=False,accepted=False,
            execution_binding=dict(source_run=reference(source_run),
                source_raw=reference(raw),source_physical=reference(physical),
                source_family=family,homotopy=record['core_settings']['homotopy'],
                modes=M,spacing=spacing,quadrature=N,steps=steps,
                wrapper_invoked=streamed_block is not None,streamed_rhs_block=streamed_block,
                workers=WORKERS,source_mean_nodes=mean_nodes,
                source_bc_normalization=record['gates']['physical_bc_tol']/record['gates']['bc_tol'],
                original_port=reference(port_path),baseline_tail_config=reference(baseline_path),
                runtime_tail_config=reference(runtime_path),native_manifest=reference(manifest_path)),
            complete_surface=False,fixed_metric_refinement=False)
        save()
        code=invoke('original_full_height_dn_and_outer_bvp',executed,require_success=False)

        # Preserve the real returned record and artifact identity before any
        # supplementary provenance check can fail. Never rewrite run.json.
        result_path=actual/'run.json'
        state['result'].update(actual_process_returned=True,
            process_returncode=code,run=str(result_path),
            run_sha256=digest(result_path) if result_path.is_file() else None)
        save()
        if not result_path.is_file():
            raise RuntimeError('The original portable process did not write run.json')
        result=load(result_path)
        returned=result.get('raw_return') or {}
        raw_path=actual/returned['file'] if returned.get('file') else None
        returned_physical=actual/'physical.npz'
        actual_rules=module('_chord_original_actual_rules',resume/'continue_material_true_tail.py')
        finite_rules=module('_chord_original_finite_rules',public/'material_design_continue.py')
        checks=finite_rules.original_finite_checks(result)
        original_gate=bool(code==0 and actual_rules.actual_gate(result)
                           and checks['solver_and_boundary_pass'])
        state['result'].update(original_finite_checks=checks,
            original_actual_gate_passed=original_gate,
            solver_success=result.get('solver_success'),error=result.get('error'),
            nodes=returned.get('nodes'),rms=returned.get('rms'),
            metric=result.get('prefix_audit',{}).get('metric_l1'),
            physical_bc_max=result.get('prefix_audit',{}).get('physical_bc_max'),
            actual_outer_checks=[
                {k:row[k] for k in ('outer','actual_bc','actual_tail')
                 if k in row and isinstance(row[k],(int,float,bool,type(None)))}
                for row in (result.get('actual_outer_checks') or [])],
            actual_tail_requested=result.get('actual_tail_requested'),
            actual_delta=(result.get('frozen_profile') or {}).get('delta'),
            source_family=family,
            homotopy=(result.get('core_settings') or {}).get('homotopy'),
            raw=reference(raw_path) if raw_path and raw_path.is_file() else None,
            physical=reference(returned_physical) if returned_physical.is_file() else None,
            original_seam_scalar_diagnostics={
                k:v for k,v in (result.get('tail_seam') or {}).items()
                if isinstance(v,(str,int,float,bool,type(None)))})
        save()
        state['input']['actual_output_core_settings']=copy.deepcopy(result.get('core_settings'))
        state['input']['actual_output_profile']=copy.deepcopy(result.get('frozen_profile'))
        if result.get('command')!=list(map(str,command)):
            raise ValueError('The original portable driver did not record its actual literal command')
        execution=dict(actual_argv=executed,original_portable_argv=list(map(str,command)),
            wrapper_invoked=streamed_block is not None,
            original_portable_command_fabricated=False,
            source_execution_inherited=False,
            execution_backend='complete_original_prefix_CSR_QR_V5_checkpoints',
            original_streamed_SuperLU_execution_claimed=False)
        if streamed_block is not None:
            provenance=qr_execution.check_execution(actual/'actual-dn-qr-execution.json',
                executed,wrapper,portable,streamed_block)
            execution.update(wrapper=str(wrapper),wrapper_sha256=digest(wrapper),
                streamed_rhs_block=streamed_block,provenance=provenance,
                floating_point_bit_identity_claimed=False)
        execution_path=out/'prefix-execution.json'
        write(execution_path,execution)
        state['result']['prefix_execution']=reference(execution_path)
        save()
        for key in ('physical_profile','physical_tail_parameters','physical_tail_cut',
                    'angular_chart','gauge_q','warp_reference','modes','angular',
                    'core_settings','parameter_scales','gates'):
            if result.get(key)!=record.get(key):
                raise ValueError('The actual output changed the declared source contract: '+key)
        for path,expected in state['source_hashes'].items():
            if digest(path)!=expected:
                raise ValueError('A bound coordination/numerical source changed during the run: '+path)
        verify_references(manifest)
        if raw_path and raw_path.is_file() and digest(raw_path)!=returned.get('sha256'):
            raise ValueError('The original returned raw SHA differs')
        if returned_physical.is_file() and digest(returned_physical)!=result.get('physical_sha256'):
            raise ValueError('The original returned physical SHA differs')
        audit=result.get('prefix_audit') or {}
        if original_gate and audit.get('samples_psi')!=mean_nodes:
            raise ValueError('The actual prefix finite mean changed')
        seam=result.get('tail_seam') or {}
        if original_gate:
            name=seam.get('tail_record')
            if not isinstance(name,str) or Path(name).name!=name:
                raise ValueError('Require the original final seam packet filename')
            packet_path=actual/name
            with gzip.open(packet_path,'rt') as stream:
                packet=json.load(stream)
            request,response=packet['request'],packet['response']
            if (packet['config']!=runtime or request.get('jacobian') is not True
                    or request.get('audit') is not True or response.get('converged') is not True):
                raise ValueError('The final original packet does not carry full J/audit success under the bound config')
            for name,expected in packet['source_sha256'].items():
                if digest(native_source/'scripts'/name)!=expected:
                    raise ValueError('The final packet source identity changed: '+name)
            binding=dict(scope='The unscaled physical-endpoint height of the original seam_audit call. No additional tail solve or reencoding was performed.',
                original_run=reference(result_path),physical=reference(returned_physical),
                raw=reference(raw_path),packet=reference(packet_path),
                candidate_H=request['height'],
                height_reference_kind='original_seam_audit_physical_endpoint',
                raw_candidate_H=returned.get('candidate_H'),
                raw_candidate_height_bitwise_equal=(returned.get('candidate_H')==request['height']),
                source_mean_nodes=mean_nodes,
                original_seam_mean_nodes=seam.get('angular_samples'),
                same_mean_cartesian_seam_certified=False,
                baseline_tail_config=reference(baseline_path),
                runtime_tail_config=reference(runtime_path),
                native_manifest=reference(manifest_path),
                source_design_run=reference(source_run),source_family=family)
            binding_path=out/'height-binding.json'
            write(binding_path,binding)
            state['result'].update(full_height_packet=reference(packet_path),
                full_height_binding=reference(binding_path),
                source_mean_nodes=mean_nodes,
                original_seam_mean_nodes=seam.get('angular_samples'),
                same_mean_cartesian_seam_certified=False)
        state['result']['accepted']=original_gate
        state['status']=('original_finite_true_dn_gates_passed' if original_gate
                         else 'original_finite_true_dn_gates_failed')
        save()
        return 0 if original_gate else 2
    except Exception as error:
        state.update(status='entry_error',error=repr(error),
                     exception=traceback.format_exc()[-6000:])
        save()
        return 1


if __name__=='__main__':
    sys.exit(main())
