#!/usr/bin/env python3
"""Solve the original nonlinear tail for the recorded lambda=.004 M24 height.

This target is the complete 24-component height retained by the actual old
lambda=.004 linear-prefix execution. That prefix failed its metric gate.
The target is used only for an independent finite tail solve and a possible
complete warm initializer; it is not lambda=.002 full-H, accepted coupling,
fixed-g refinement, or a complete closed surface.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import threading
import traceback

RECORDED_SHA = '6d774ea36c069d0dd991aa4e2e9ed74aed8d91723b10b5ad4d5d1cd72250b7de'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo','work','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--tail-warmup',type=float,nargs='*',default=[.25,.5,.75,.9])
    a = parser.parse_args()
    repo, work, out = a.repo.resolve(), a.work.resolve(), a.outdir.resolve()
    if work not in out.parents or repo == work or repo in work.parents:
        raise ValueError('Generated fields must stay under work outside the repository')
    out.mkdir(parents=True,exist_ok=False)
    topic = repo/'topics/visible-flex-held-10pct'
    scripts = topic/'scripts'
    source = work/'native-tail24'
    tail = None
    done = threading.Event()
    lock = threading.Lock()
    monitor = None
    state = dict(scope=__doc__,status='validating_recorded_height',stages=[],progress={},
                 actual_tail_requested=True,fixed_metric_refinement=False,complete_surface=False)

    def save():
        temporary = out/'summary.json.tmp'
        temporary.write_text(json.dumps(state,indent=2,allow_nan=False)+'\n')
        temporary.replace(out/'summary.json')

    save()
    try:
        recorded = topic/'notes/2026-11-20-m3-newg-lambda0004-m24-execution.json'
        if digest(recorded) != RECORDED_SHA:
            raise ValueError('The declared complete historical height record changed')
        old = read(recorded)
        H = old['raw_return']['candidate_H']
        if len(H)!=24 or not all(math.isfinite(v) for v in H):
            raise ValueError('A complete finite 24-component target is required')
        if (old['configuration']['core_settings']['homotopy']!=.004
                or old['original_metric_gate_passed'] is not False):
            raise ValueError('The recorded target scope differs')
        cfg_path = work/'m24-tail-settings.json'
        cfg = read(cfg_path)
        port_path = work/'m24-linear-port.json'
        port = read(port_path)
        if port['source']['config_sha256'] != digest(cfg_path):
            raise ValueError('Tail configuration differs from the recovered exact port')
        if digest(port_path) not in old['input_hashes'].values():
            raise ValueError('This is not the recorded M24 physical port')
        for key,value in old['configuration']['physical_tail_parameters'].items():
            if cfg.get(key)!=value:
                raise ValueError('The recorded physical tail differs: '+key)
        manifest_path = source/'native-manifest.json'
        manifest = read(manifest_path)
        for key,value in dict(M=24,spacing=3,quadrature=512,steps=16).items():
            if manifest['fixed_scope'][key]!=value:
                raise ValueError('Native dimension/discretization differs: '+key)
        if manifest['execution_provider']['workers']!=2:
            raise ValueError('Retain the declared two native workers')
        for ref in [*manifest['owned_sources'],*manifest['native_files'].values()]:
            if digest(ref['path'])!=ref['sha256']:
                raise ValueError('Changed native source/binary: '+ref['path'])
        core_text = (source/'scripts/950f-tail-stage-core.mjs').read_text()
        if 'bounded-chord-v1' not in core_text or 'fresh-original' not in core_text:
            raise ValueError('The recorded original-final-J chord source is required')
        cfg.update(chordMaxCorrections=3,traceFile=str(out/'worker-trace.jsonl'))
        cfg.pop('initialCheckpoint',None)
        actual_cfg = out/'tail-settings.json'
        actual_cfg.write_text(json.dumps(cfg,indent=2)+'\n')
        runs = out/'native-runs'
        runs.mkdir()
        os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
            VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
            VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(
                scripts/'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'),
            VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest_path),
            VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=digest(manifest_path),
            VISIBLE_FLEX_NATIVE_RUN_DIR=str(runs))
        for key in ('LD_LIBRARY_PATH','LD_PRELOAD'):
            os.environ.pop(key,None)
        client_path = source/'scripts/950f-tail-client-v3.py'
        state['source_hashes'] = {str(p):digest(p) for p in
            (Path(__file__),recorded,cfg_path,actual_cfg,port_path,manifest_path,client_path)}
        state['progress'] = dict(target_scope='Recorded lambda=.004 prefix candidate_H; independent tail only',
            candidate_H=H,warm_factors=a.tail_warmup,
            original_solve_tolerance=cfg['solveTolerance'],prefix_metric_passed=False)
        state['status'] = 'initializing_original_worker'
        save()

        def watch():
            while not done.wait(15):
                try:
                    trace = out/'worker-trace.jsonl'
                    if not trace.exists():
                        continue
                    latest = None
                    for line in trace.read_text().splitlines():
                        try:
                            row = json.loads(line)
                            latest = {k:(str(v) if isinstance(v,float) and not math.isfinite(v) else v)
                                      for k,v in row.items()
                                      if v is None or isinstance(v,(str,bool,int,float))}
                        except (ValueError,AttributeError):
                            pass
                    if latest is not None:
                        with lock:
                            state['progress']['last_actual_worker_trace'] = latest
                            save()
                except OSError:
                    pass

        monitor = threading.Thread(target=watch,daemon=True)
        monitor.start()
        spec = importlib.util.spec_from_file_location('held10_recorded_height_client',client_path)
        client = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(client)
        tail = client.WeightedTailPort(actual_cfg,source/'repro/source-root',out/'tail',node_heap=2048)
        for index,factor in enumerate([*a.tail_warmup,1.]):
            full = index==len(a.tail_warmup)
            height = [v*factor**(j+1) for j,v in enumerate(H)]
            with lock:
                state['status'] = 'original_full_height_running' if full else 'original_warm_height_running'
                state['progress'].update(factor=factor,full_height=full)
                save()
            response = tail.solve(height,jacobian=full,audit=True)
            if (response.get('converged') is not True or not math.isfinite(response['residual'])
                    or response['residual']>cfg['solveTolerance'] or response.get('audit') is None):
                raise ValueError('Original finite nonlinear tail/audit gate failed')
            if full:
                jac = response.get('heightJetJacobian')
                if not isinstance(jac,list) or len(jac)!=(3*24+2)*24 or not all(math.isfinite(v) for v in jac):
                    raise ValueError('Original full height Jacobian did not return')
            saved = out/f'tail_{tail.calls:04d}.json.gz'
            row = dict(factor=factor,full_height=full,converged=response['converged'],
                residual=response['residual'],audit=response['audit'],record=str(saved),sha256=digest(saved))
            with lock:
                state['stages'].append(row)
                save()
            print(json.dumps(dict(event='recorded_height_original_tail_return',**row)),flush=True)
        with lock:
            state['status'] = 'recorded_height_original_finite_tail_passed'
            state['result'] = dict(accepted=True,full_height_record=str(saved),
                                  sha256=digest(saved),prefix_coupling_accepted=False)
            save()
        return 0
    except Exception as exc:
        with lock:
            state.update(status='original_tail_failed',error=repr(exc),
                         exception=traceback.format_exc()[-6000:])
            save()
        return 2
    finally:
        done.set()
        if monitor:
            monitor.join(timeout=2)
        if tail is not None:
            tail.close()


if __name__=='__main__':
    sys.exit(main())
