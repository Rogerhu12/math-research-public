#!/usr/bin/env python3
"""Continue one actual accepted M24 prefix through the original nonlinear DN.

Use the already restored native/chord source in the same live worker. The
source material homotopy and all original gates stay unchanged. Generated
fields remain in the worker; summary.json contains compact observations.
This remains a finite design solve, not fixed-g refinement or closure.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
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
    a = parser.parse_args()
    repo, work = a.repo.resolve(), a.work.resolve()
    source_run, out = a.source_run.resolve(), a.outdir.resolve()
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
        from continue_material_true_tail import prefix_gate, actual_gate
        record = load_json(source_run)
        if not prefix_gate(record) or not record.get('raw_return', {}).get('success'):
            raise ValueError('The actual source must pass all original finite prefix gates')
        argv = list(record['command'])
        runner = resume/'portable_prefix_continue.py'
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
        native_runs.mkdir()
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
        state['source_hashes'] = {str(p):digest(p) for p in
            (Path(__file__),runner,resume/'continue_material_true_tail.py',source_run,
             raw,physical,tail_path,actual_cfg,port_path,manifest)}
        if initial_tail:
            state['source_hashes'][str(initial_tail)] = digest(initial_tail)
        state['progress'] = dict(source_metric=record['prefix_audit']['metric_l1'],
            modes=modes, warm_factors=a.tail_warmup,
            warm_definition='H_j * factor**j for j=1,...,M; then full H',
            initial_tail=str(initial_tail) if initial_tail else None,
            original_outer_budget=record['gates']['original_outer_budget'])
        state['status'] = 'original_true_dn_running'
        save()
        print(json.dumps(dict(event='actual_true_dn_command',argv=argv)),flush=True)
        proc = subprocess.Popen(argv,cwd=repo,env=env)
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
        accepted = proc.returncode == 0 and actual_gate(result)
        state['returncode'] = proc.returncode
        state['result'] = dict(accepted=accepted,solver_success=result.get('solver_success'),
            error=result.get('error'),prefix_audit=result.get('prefix_audit'),
            actual_outer_checks=result.get('actual_outer_checks'),tail_seam=result.get('tail_seam'),
            raw_return=result.get('raw_return'),physical_sha256=result.get('physical_sha256'),
            run_sha256=digest(result_path))
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
