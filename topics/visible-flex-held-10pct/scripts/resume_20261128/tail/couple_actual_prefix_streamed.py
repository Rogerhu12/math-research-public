#!/usr/bin/env python3
"""Couple an actual accepted M24 prefix to its original full nonlinear DN.

The existing entry/inner radial-batching v2 wrapper bounds the prefix memory;
it preserves every node/component, complete collocation matrix, analytic
Jacobian, domain/RMS gate, full-H/J/audit request and eight-outer budget.
Actual execution argv and both v2/base wrapper sidecars are explicitly bound.
Generated fields remain outside git. This is a finite design coupling, not
fixed-g refinement, a continuous Cartesian seam or a completed surface.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
import traceback


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'outdir'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--tail-warmup', type=float, nargs='*', default=[.25,.5,.75,.9])
    parser.add_argument('--initial-tail', type=Path,
                        help='Same-source accepted complete tail packet, used only as an initial guess')
    parser.add_argument('--rhs-block', type=int, default=32)
    a = parser.parse_args()
    repo, work = a.repo.resolve(), a.work.resolve()
    source_run, out = a.source_run.resolve(), a.outdir.resolve()
    if a.rhs_block < 1:
        raise ValueError('A positive prefix radial block is required')
    if work not in out.parents or work not in source_run.parents:
        raise ValueError('The source and generated result must stay under the work directory')
    if repo == work or repo in work.parents:
        raise ValueError('Generated fields must stay outside the repository')
    out.mkdir(parents=True, exist_ok=False)
    summary = out/'summary.json'
    state = dict(scope=__doc__, status='checking_actual_input', stages=[], progress={},
                 actual_tail_requested=True, fixed_metric_refinement=False,
                 complete_surface=False)
    proc = None

    def save():
        temporary = summary.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(state, indent=2, allow_nan=False)+'\n')
        temporary.replace(summary)

    save()
    try:
        scripts = repo/'topics/visible-flex-held-10pct/scripts'
        resume = scripts/'resume_m3'
        sys.path.insert(0, str(resume))
        public = scripts/'resume_20261126'
        sys.path.insert(0, str(public))
        from continue_material_true_tail import prefix_gate, actual_gate
        from material_design_secant_predictor import accepted_original
        from material_design_continue import original_finite_checks
        record, initial_arrays = accepted_original(source_run, repo)
        del initial_arrays
        if not prefix_gate(record) or not record.get('raw_return', {}).get('success'):
            raise ValueError('The actual source must pass all original finite prefix gates')
        argv = list(record['command'])
        runner = resume/'portable_prefix_continue.py'
        design = scripts/'resume_20261128/design'
        wrapper = design/'prefix_resource_driver_v2.py'
        base_wrapper = design/'prefix_resource_driver.py'
        cache_source = design/'cached_fourier_tables.py'
        original_batch = public/'streamed_release_prefix_driver.py'
        original_entry = public/'tail_continue_recovered_prefix.py'
        if digest(original_entry) != 'f2ea6d64257cd7070a86fea3d51cce626507eb41b0832ef85b79e4b0618c4784':
            raise ValueError('The reviewed original coupling entry changed')
        if len(argv) < 2 or Path(argv[1]).resolve() != runner:
            raise ValueError('Expected the original portable prefix entry')

        def option(flag):
            if argv.count(flag) != 1:
                raise ValueError('Expected one original argument '+flag)
            return argv[argv.index(flag)+1]

        def replace(flag, value):
            if flag in argv:
                option(flag)
                argv[argv.index(flag)+1] = str(value)
            else:
                argv.extend([flag, str(value)])

        if any(x in argv for x in ('--tail-config','--tail-warmup','--probe-only','--skip-audit')):
            raise ValueError('Use the accepted original linear-prefix source with its audit')
        for field in ('source_hashes','inputs'):
            for name, expected in record[field].items():
                if digest(name) != expected:
                    raise ValueError('Changed original source/input: '+name)
        raw = source_run.parent/record['raw_return']['file']
        physical = source_run.parent/'physical.npz'
        if digest(raw) != record['raw_return']['sha256']:
            raise ValueError('Actual raw checkpoint hash differs')
        if digest(physical) != record['physical_sha256']:
            raise ValueError('Actual physical field hash differs')
        tail_path = work/'m24-tail-settings.json'
        tail = load_json(tail_path)
        port_path = Path(option('--port')).resolve()
        port = load_json(port_path)
        if port['source']['config_sha256'] != digest(tail_path):
            raise ValueError('Original tail settings differ from exported port')
        modes, spacing = int(tail['modes']), int(tail['spacing'])
        if modes != 24 or int(record['modes']) != modes or int(option('--modes')) != modes:
            raise ValueError('This native source is the declared M24 case')
        if port['modes'] != [spacing*j for j in range(1,modes+1)]:
            raise ValueError('Tail port harmonics differ')
        if int(tail['quadrature']) <= 4*modes*spacing:
            raise ValueError('Original strict quadrature guard failed')
        source = Path(option('--source-topic')).resolve()
        native_source = work/'native-tail24'
        for name in ('db6f-prefix-coupled.py','db6f-prefix-flat-profile.py',
                     '950f-prefix-adaptive-chart-bvp-v2.py','78718-prefix-fourier-jacobian.py'):
            if digest(source/'scripts'/name) != digest(native_source/'scripts'/name):
                raise ValueError('Prepared native source changed prefix equation: '+name)
        manifest = native_source/'native-manifest.json'
        native = load_json(manifest)
        for name, expected in dict(M=modes,spacing=spacing,quadrature=tail['quadrature'],
                                   steps=tail['steps']).items():
            if native['fixed_scope'][name] != expected:
                raise ValueError('Native fixed scope differs: '+name)
        for ref in [*native['owned_sources'], *native['native_files'].values()]:
            if digest(ref['path']) != ref['sha256']:
                raise ValueError('Prepared native source/binary changed: '+ref['path'])
        if native['execution_provider']['workers'] != 2:
            raise ValueError('Retain the declared two native workers')
        core_text = (native_source/'scripts/950f-tail-stage-core.mjs').read_text()
        if 'bounded-chord-v1' not in core_text or 'fresh-original' not in core_text:
            raise ValueError('Prepared source lacks the recorded original-final-J chord path')
        initial_tail = None
        if a.initial_tail:
            initial_tail = a.initial_tail.resolve()
            if work not in initial_tail.parents:
                raise ValueError('The accepted tail initializer must stay under work')
            with gzip.open(initial_tail,'rt') as stream:
                packet = json.load(stream)
            prior = packet['response']
            checkpoint = prior['checkpoint']
            residual = prior.get('residual')
            if (prior.get('converged') is not True or prior.get('failed')
                    or not isinstance(residual,(int,float)) or not math.isfinite(residual)
                    or residual > tail['solveTolerance'] or packet['request'].get('audit') is not True
                    or not isinstance(prior.get('audit'),dict)):
                raise ValueError('Tail initializer did not pass the original audited finite gate')
            source_names = {'950f-tail-client-v3.py','950f-tail-stage-port-v3.mjs',
                '950f-tail-stage-core.mjs','950f-tail-stage-split.mjs',
                '950f-tail-subdivision.mjs','950f-tail-warm-remesh.mjs',
                'closing_weighted_tail.mjs','closing_recalibrated_tail.mjs'}
            if set(packet['source_sha256']) != source_names:
                raise ValueError('Tail initializer has an incomplete source identity')
            for name, expected in packet['source_sha256'].items():
                if digest(native_source/'scripts'/name) != expected:
                    raise ValueError('Tail initializer used a different source: '+name)
            for key, value in tail.items():
                if packet['config'].get(key) != value:
                    raise ValueError('Tail initializer configuration differs: '+key)
            states, cut_height = checkpoint['states'], checkpoint['cutHeight']
            parameters = checkpoint['parameters']
            if (parameters['modes']!=modes or parameters['spacing']!=spacing
                    or not isinstance(states,list) or len(states)!=parameters['depth']+1
                    or len(cut_height)!=modes
                    or cut_height != packet['request']['height']
                    or any(len(row)!=2*modes or not all(math.isfinite(v) for v in row)
                           for row in states)
                    or not all(math.isfinite(v) for v in cut_height)):
                raise ValueError('Tail initializer lacks the complete finite state')
            # The original worker reads the full packet's response.checkpoint,
            # checks all physical geometry keys, and remeshes it. Its existing
            # predictor explicitly permits a new Dirichlet height; that guess
            # must still pass every original nonlinear gate at each request.
        tail.update(chordMaxCorrections=3, traceFile=str(out/'worker-trace.jsonl'))
        tail.pop('initialCheckpoint', None)
        if initial_tail:
            tail['initialCheckpoint'] = str(initial_tail)
        actual_cfg = out/'tail-settings.json'
        actual_cfg.write_text(json.dumps(tail, indent=2)+'\n')
        native_runs = out/'native-runs'
        # The native evaluator creates its own previously absent run directory.
        env = dict(os.environ, PYTHONUNBUFFERED='1', OPENBLAS_NUM_THREADS='1',
            OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
            VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
            VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(
                scripts/'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'),
            VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest),
            VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=digest(manifest),
            VISIBLE_FLEX_NATIVE_RUN_DIR=str(native_runs))
        for key in ('LD_PRELOAD','LD_LIBRARY_PATH'):
            env.pop(key, None)
        argv[0] = sys.executable
        replace('--source-topic', native_source)
        replace('--raw-restart', raw)
        replace('--tail-config', actual_cfg)
        replace('--outdir', out/'actual')
        if '--control-record' in argv:
            i = argv.index('--control-record')
            del argv[i:i+2]
        if a.tail_warmup:
            argv.extend(['--tail-warmup', *map(str,a.tail_warmup)])
        executed = [sys.executable, str(wrapper), '--rhs-block', str(a.rhs_block),
                    *argv[2:]]
        state['source_hashes'] = {str(p):digest(p) for p in
            (Path(__file__),runner,resume/'continue_material_true_tail.py',source_run,
             raw,physical,tail_path,actual_cfg,port_path,manifest,wrapper,base_wrapper,
             cache_source,original_batch,original_entry,
             public/'material_design_secant_predictor.py',public/'material_design_continue.py')}
        if initial_tail:
            state['source_hashes'][str(initial_tail)] = digest(initial_tail)
        state['progress'] = dict(source_metric=record['prefix_audit']['metric_l1'],
            modes=modes, warm_factors=a.tail_warmup,
            warm_definition='H_j * factor**j for j=1,...,M; then full H',
            initial_tail=str(initial_tail) if initial_tail else None,
            original_outer_budget=record['gates']['original_outer_budget'],
            radial_rhs_jacobian_block=a.rhs_block,
            initial_domain_rhs_also_batched=True)
        state['execution'] = dict(actual_argv=executed, original_portable_argv=argv,
            original_portable_command_fabricated=False,
            wrapper=str(wrapper), wrapper_sha256=digest(wrapper),
            source_design_run=str(source_run), mathematical_parameters_changed=False,
            original_gates_relaxed=False)
        state['status'] = 'original_true_dn_running'
        save()
        print(json.dumps(dict(event='actual_true_dn_command',actual_argv=executed,
                              original_portable_argv=argv)),flush=True)
        proc = subprocess.Popen(executed,cwd=repo,env=env)
        seen = set()

        def observe():
            def scalars(obj):
                return {k:(str(v) if isinstance(v,float) and not math.isfinite(v) else v)
                        for k,v in obj.items()
                        if v is None or isinstance(v,(bool,int,float,str))}
            for path in sorted((out/'actual').glob('tail_*.json.gz')):
                if path.name in seen:
                    continue
                try:
                    with gzip.open(path,'rt') as stream:
                        packet = json.load(stream)
                    response = packet['response']
                    request = packet['request']
                    row = dict(name=path.name,sha256=digest(path))
                    row.update(scalars({k:response[k] for k in
                        ('converged','failed','residual')
                        if k in response}))
                    row['requested_jacobian'] = request['jacobian']
                    row['requested_audit'] = request['audit']
                    if isinstance(response.get('audit'),dict):
                        row['audit'] = scalars(response['audit'])
                    if isinstance(response.get('history'),list) and response['history']:
                        row['last_original_iteration'] = scalars(response['history'][-1])
                    state['stages'].append(row)
                    seen.add(path.name)
                except (OSError,EOFError,ValueError,TypeError,KeyError):
                    pass
            trace = out/'worker-trace.jsonl'
            if trace.exists():
                try:
                    last = None
                    for line in trace.read_text().splitlines():
                        try:
                            value = json.loads(line)
                            if isinstance(value,dict):
                                last = scalars(value)
                        except ValueError:
                            pass
                    if last is not None:
                        state['progress']['last_actual_worker_trace'] = last
                except OSError:
                    pass
            events = out/'actual/events.jsonl'
            if events.exists():
                try:
                    last = json.loads(events.read_text().splitlines()[-1])
                    state['progress']['last_actual_prefix_event'] = scalars(last)
                except (OSError,ValueError,IndexError):
                    pass
            save()

        while proc.poll() is None:
            observe()
            time.sleep(15)
        observe()
        result_path = out/'actual/run.json'
        result = load_json(result_path)
        finite_checks = original_finite_checks(result)
        accepted = bool(proc.returncode == 0 and actual_gate(result)
                        and finite_checks['solver_and_boundary_pass'])
        state['returncode'] = proc.returncode
        state['result'] = dict(accepted=False,original_finite_gate_before_binding=accepted,
            solver_success=result.get('solver_success'),
            error=result.get('error'),prefix_audit=result.get('prefix_audit'),
            actual_outer_checks=result.get('actual_outer_checks'),tail_seam=result.get('tail_seam'),
            raw_return=result.get('raw_return'),physical_sha256=result.get('physical_sha256'),
            run_sha256=digest(result_path), original_finite_checks=finite_checks)
        save()
        # Observe the real return before any supplementary execution binding
        # can fail; never rewrite the original portable run.json.
        if result['command'] != argv:
            raise ValueError('The original portable mathematical command differs')
        radial_path, cache_path = out/'actual/radial-batching.json', out/'actual/fourier-table-cache.json'
        radial, cached = load_json(radial_path), load_json(cache_path)
        if (radial.get('command') != executed[1:]
                or radial.get('wrapper_sha256') != digest(base_wrapper)
                or radial.get('original_driver_sha256') != digest(runner)
                or radial.get('existing_batching_sha256') != digest(original_batch)
                or radial.get('initial_domain_rhs_batched') is not True
                or radial.get('original_all_nodes_and_components_evaluated') is not True
                or radial.get('radial_rhs_jacobian_block') != a.rhs_block
                or radial.get('mathematical_parameters_changed') is not False
                or radial.get('original_gates_relaxed') is not False
                or radial.get('released_stale_factor', {}).get('arithmetic_changed') is not False):
            raise ValueError('The actual entry/inner batching execution changed')
        expected_cache_sources = {str(p): digest(p) for p in (wrapper, base_wrapper, cache_source)}
        if (cached.get('command') != executed[1:]
                or cached.get('source_hashes') != expected_cache_sources
                or cached.get('original_equations_changed') is not False
                or cached.get('original_acceptance_gates_changed') is not False
                or cached.get('geometry_or_response_cached') is not False):
            raise ValueError('The actual read-only Fourier-cache execution changed')
        state['execution'].update(radial_provenance=dict(path=str(radial_path),sha256=digest(radial_path)),
            fourier_cache_provenance=dict(path=str(cache_path),sha256=digest(cache_path)),
            original_execution_binding_checked=True)
        for path, expected in state['source_hashes'].items():
            if digest(path) != expected:
                raise ValueError('A bound source or input changed during the actual coupling: '+path)
        if accepted:
            # Bind the true final physical-endpoint request separately from the
            # raw collocation candidate; these need not be bitwise identical.
            final_name = result['tail_seam']['tail_record']
            if Path(final_name).name != final_name:
                raise ValueError('The final original seam record must be a local filename')
            final_packet = out/'actual'/final_name
            with gzip.open(final_packet, 'rt') as stream:
                final = json.load(stream)
            request, response = final['request'], final['response']
            M = modes
            jac = response.get('heightJetJacobian')
            if (final['config'] != tail or request.get('jacobian') is not True
                    or request.get('audit') is not True
                    or response.get('converged') is not True or response.get('failed')
                    or not math.isfinite(response.get('residual', math.nan))
                    or response['residual'] > tail['solveTolerance']
                    or not isinstance(response.get('audit'), dict)
                    or not isinstance(jac, list) or len(jac) != (3*M+2)*M
                    or not all(math.isfinite(v) for v in jac)
                    or response['checkpoint']['cutHeight'] != request['height']):
                raise ValueError('The final original complete-height/J/audit identity failed')
            for name, expected in final['source_sha256'].items():
                if digest(native_source/'scripts'/name) != expected:
                    raise ValueError('The final original tail source changed: '+name)
            bound = dict(scope='Actual final seam_audit physical-endpoint full height; no additional tail solve',
                candidate_H=request['height'], raw_candidate_H=result['raw_return']['candidate_H'],
                raw_candidate_height_bitwise_equal=(request['height']==result['raw_return']['candidate_H']),
                source_run=dict(path=str(result_path),sha256=digest(result_path)),
                physical=dict(path=str(out/'actual/physical.npz'),sha256=digest(out/'actual/physical.npz')),
                packet=dict(path=str(final_packet),sha256=digest(final_packet)),
                source_mean_nodes=result['prefix_audit']['samples_psi'],
                original_seam_mean_nodes=result['tail_seam']['angular_samples'],
                complete_Cartesian_seam_certified=False)
            binding_path = out/'height-binding.json'
            binding_path.write_text(json.dumps(bound,indent=2,allow_nan=False)+'\n')
            state['result'].update(full_height_packet=bound['packet'],
                full_height_binding=dict(path=str(binding_path),sha256=digest(binding_path)))
        state['result']['accepted'] = accepted
        state['status'] = ('original_finite_true_dn_gates_passed' if accepted
                           else 'original_finite_true_dn_gates_failed')
        save()
        return 0 if accepted else 2
    except Exception as exc:
        if proc is not None and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=20)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()
        state.update(status='entry_error',error=repr(exc),
                     exception=traceback.format_exc()[-6000:])
        save()
        raise


if __name__ == '__main__':
    sys.exit(main())
