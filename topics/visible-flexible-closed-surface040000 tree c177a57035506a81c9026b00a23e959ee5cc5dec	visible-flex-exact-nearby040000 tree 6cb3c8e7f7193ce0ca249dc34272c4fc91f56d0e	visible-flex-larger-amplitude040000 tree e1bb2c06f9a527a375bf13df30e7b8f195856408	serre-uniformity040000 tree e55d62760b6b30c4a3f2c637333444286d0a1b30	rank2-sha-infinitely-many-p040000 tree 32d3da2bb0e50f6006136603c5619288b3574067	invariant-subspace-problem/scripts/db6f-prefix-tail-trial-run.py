#!/usr/bin/env python3
"""Replay a saved actual DN state with diagnostic-only line-search recording.

This performs no prefix BVP. Output remains a failed/unconverged response
unless the unchanged shooting equations actually meet their original tol.
The max-iteration budget, recovery input and recording paths are the only
configuration changes from the input config.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_text())


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,required=True)
    ap.add_argument('--config',type=Path,required=True)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--max-iterations',type=int,default=2)
    ap.add_argument('--node-heap',type=int,default=1536)
    a=ap.parse_args()
    out=a.out_prefix.resolve()
    if any(p.name != out.name+'-run.log' for p in out.parent.glob(out.name+'*')):
        raise FileExistsError('Diagnostic output prefix already used')
    original=read(a.config)
    record=read(a.checkpoint)
    cp=record.get('response',{}).get('checkpoint') or record.get('checkpoint') or record
    if not all(k in cp for k in ('parameters','states','cutHeight')):
        raise ValueError('Input lacks complete actual shooting state and target')
    for key in ('modes','steps','quadrature','spacing'):
        if cp['parameters'][key] != original[key]:
            raise ValueError('Config/checkpoint numerical mismatch: '+key)
    cfg=dict(original)
    overrides=dict(initialCheckpoint=str(a.checkpoint.resolve()),
                   maxIterations=a.max_iterations,
                   traceFile=str(out)+'-trace.jsonl',
                   iterationCheckpointFile=str(out)+'-iteration.json.gz',
                   trialDiagnosticFile=str(out)+'-trials.jsonl',
                   trialStatePrefix=str(out)+'-stage-input')
    cfg.update(overrides)
    config_path=Path(str(out)+'-config.json')
    config_path.write_text(json.dumps(cfg,indent=2)+'\n')
    script=Path(__file__).resolve()
    source_map=script.parent.parent/'notes/2026-11-09-db6f-prefix-tail-trial-diagnostic-source-map.json'
    client=script.with_name('db6f-prefix-tail-trial-client.py')
    reproduction=dict(scope=__doc__, command=[sys.executable,str(script),*sys.argv[1:]],
                      script_sha256=sha(script), client_sha256=sha(client),
                      input_config=str(a.config.resolve()), input_config_sha256=sha(a.config),
                      input_checkpoint=str(a.checkpoint.resolve()), input_checkpoint_sha256=sha(a.checkpoint),
                      input_checkpoint_scope=cp.get('scope'),
                      source_map=str(source_map),source_map_sha256=sha(source_map),
                      diagnostic_config=str(config_path), diagnostic_config_sha256=sha(config_path),
                      overrides=overrides, original_projection_floor=cp['parameters'].get('projectionFloor'),
                      request=dict(jacobian=True,audit=False),
                      independent_static_review='Root read all four shared-to-trial source diffs and found no change to RK/Jacobian/evaluation, trial steps, guard or strict norm-decrease acceptance. This is a source review, not a numerical result.')
    repro_path=Path(str(out)+'-reproduction.json')
    repro_path.write_text(json.dumps(reproduction,indent=2)+'\n')
    spec=importlib.util.spec_from_file_location('trial_client',client)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    port=None;error=None;response=None;start=time.time()
    try:
        port=mod.WeightedTailPort(config_path,a.source_root.resolve(),str(out)+'_tail',a.node_heap)
        response=port.solve(cp['cutHeight'],jacobian=True,audit=False)
    except Exception as exc:
        error=repr(exc)
    finally:
        if port is not None:
            port.close()
    output_record=Path(str(out)+'_tail_0001.json.gz')
    saved=read(output_record)['response'] if output_record.is_file() else {}
    summary=dict(scope='Actual finite DN replay only; no coupled prefix or infinite-tail claim.',
                 converged=bool(saved.get('converged')),error=error,
                 response_failed=saved.get('failed'),residual=saved.get('residual'),
                 last_iteration=saved.get('lastIteration'),seconds=time.time()-start,
                 actual_worker_exit_code=None if port is None else port.proc.poll(),
                 response_record=str(output_record) if output_record.is_file() else None,
                 response_record_sha256=sha(output_record) if output_record.is_file() else None)
    Path(str(out)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary),flush=True)
    # Natural process completion means a recorded result, not math success.


if __name__ == '__main__':
    main()
