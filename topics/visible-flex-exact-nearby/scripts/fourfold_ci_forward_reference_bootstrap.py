#!/usr/bin/env python3
"""Restore the existing exact forward reference, without committing its cache.

The historical numerical driver is used only to recover coefficient-selection
data. Every raw input and every final U/L and Q shard must match its historical
SHA256 before a cache is published. A different floating result is a failed
recovery, never a substitute for the reference in the existing proofs.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tarfile
import time
import traceback

BASE=Path('data/phase_ring_continuation')
RAW=BASE/'exact_affine_step4_shared_knot_dense1032'
UL=BASE/'step4_shared1032_reference_forward'
Q=BASE/'step5_retargeted_reference/Q_forward'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def checked_files(directory,manifest):
    rows=[]
    for row in manifest['shards']:
        path=directory/row['path']
        if not path.is_file() or sha(path)!=row['sha256']:
            raise ValueError('historical exact reference shard absent or changed: '+str(path))
        rows.append(dict(path=str(path),sha256=row['sha256'],bytes=path.stat().st_size))
    return rows


def raw_forward_only():
    # This wrapper leaves the historical driver's initialization, source
    # hashes, geometry, forward branch and serialization unchanged. It stops
    # after that branch instead of starting the unused backward branch.
    import numpy as np
    import fourfold_phase_exact_affine_nodes as runner
    import fourfold_phase_shared_grid_adaptive_chunks as adaptive
    class ForwardSaved(Exception):pass
    original=adaptive.AdaptiveSharedMap.round_trip
    def only_forward(self,theta,tolerance,directory,first):
        self.branch(theta,-1.,-np.pi/2,np.pi/2,tolerance,
                    directory/f'block_{first:04d}_forward')
        raise ForwardSaved()
    runner.ExactAffineMap=adaptive.AdaptiveSharedMap
    runner.save_trace=adaptive.save_adaptive_trace
    adaptive.AdaptiveSharedMap.round_trip=only_forward
    argv=sys.argv
    sys.argv=['fourfold_phase_shared_grid_adaptive_chunks.py',
        '--object',str(BASE/'type_fixed_step02_d5_exact_affine_step4_object.json'),
        '--root-certificate',str(BASE/'type_fixed_step02_d5_exact_affine_step4_root_tight.json'),
        '--dyadic-conjugacy',str(BASE/'type_fixed_step02_d5_exact_affine_step4_dyadic_H.json'),
        '--out','ci-output/unused-two-leg-report.json','--trace-dir',str(RAW),
        '--progress','ci-output/raw-progress.json','--rays','1032',
        '--block-size','1032','--quarter-nodes','256','--tolerance','2e-12']
    try:
        runner.main()
    except ForwardSaved:
        pass
    finally:
        sys.argv=argv
        adaptive.AdaptiveSharedMap.round_trip=original


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-existing',action='store_true')
    p.add_argument('--no-archive',action='store_true')
    a=p.parse_args();out=Path('ci-output');out.mkdir(exist_ok=True)
    started,cpu=time.monotonic(),time.process_time()
    result=dict(kind='historical_exact_forward_reference_cache_recovery',complete=False,
        source_sha256=sha(__file__),source_commit=os.environ.get('GITHUB_SHA'),
        python=sys.version,platform=platform.platform(),historical_reference_unchanged=True,
        true_flow_or_KAM_completion_claimed=False)
    try:
        import numpy,scipy,flint
        result['versions']=dict(numpy=numpy.__version__,scipy=scipy.__version__,flint=flint.__version__)
        if result['versions']!=dict(numpy='2.3.5',scipy='1.17.0',flint='0.9.0'):
            raise ValueError('the historical reference software versions must be retained')
        ul,q=read(UL/'manifest.json'),read(Q/'manifest.json')
        manifests={str(directory/'manifest.json'):sha(directory/'manifest.json') for directory in (UL,Q)}
        if not a.check_existing:
            try:
                checked_files(UL,ul);checked_files(Q,q)
            except ValueError:
                raw_forward_only()
                raw=[]
                for row in ul['input_traces']:
                    path=Path(row['path'])
                    if sha(path)!=row['sha256']:
                        raise ValueError('recovered floating raw differs from the actual reference input: '+str(path))
                    raw.append(dict(path=str(path),sha256=row['sha256'],bytes=path.stat().st_size))
                result['historical_raw_inputs']=raw
                replay=out/'UL-replay'
                if replay.exists():raise ValueError('use a fresh CI workspace for reference selection')
                subprocess.run([sys.executable,'scripts/fourfold_shared_dense_reference.py',
                    '--trace-dir',str(RAW),'--leg','forward','--rays','1032','--degree','516',
                    '--segments-per-file','24','--out-dir',str(replay)],check=True)
                if sha(replay/'manifest.json')!=manifests[str(UL/'manifest.json')]:
                    raise ValueError('the recovered U/L manifest differs from the historical definition')
                checked_files(replay,ul)
                from fourfold_shared_reference_retarget import construct_Q
                qreplay=out/'Q-replay'
                construct_Q(ul,qreplay,128,48,sha('scripts/fourfold_shared_reference_retarget.py'))
                if sha(qreplay/'manifest.json')!=manifests[str(Q/'manifest.json')]:
                    raise ValueError('the recovered Q manifest differs from the historical definition')
                checked_files(qreplay,q)
                for destination,temporary,manifest in ((UL,replay,ul),(Q,qreplay,q)):
                    for row in manifest['shards']:
                        path=destination/row['path']
                        if path.exists() and sha(path)!=row['sha256']:
                            raise ValueError('refuse to overwrite a different existing reference shard')
                        if not path.exists():shutil.copyfile(temporary/row['path'],path)
        result['files']=checked_files(UL,ul)+checked_files(Q,q)
        result['historical_manifests']=manifests
        result['all_550_exact_reference_segments_recovered']=ul['segment_count']==q['segment_count']==550
        if not result['all_550_exact_reference_segments_recovered']:
            raise ValueError('the historical full forward partition is incomplete')
        if not a.no_archive:
            archive=out/'forward-reference-cache.tar'
            with tarfile.open(archive,'w') as handle:
                for directory,manifest in ((UL,ul),(Q,q)):
                    for name in ['manifest.json',*[row['path'] for row in manifest['shards']]]:
                        path=directory/name;handle.add(path,arcname=str(path),recursive=False)
            result['archive']=dict(path=str(archive),sha256=sha(archive),bytes=archive.stat().st_size)
        result['complete']=True
    except Exception as exc:
        result.update(failure=type(exc).__name__+': '+str(exc),traceback=traceback.format_exc())
    result.update(wall_seconds=time.monotonic()-started,cpu_seconds_this_python_process=time.process_time()-cpu)
    (out/'forward-reference-cache-proof.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:result.get(k) for k in ('complete','failure','wall_seconds')},flush=True)
    return 0 if result['complete'] else 2


if __name__=='__main__':raise SystemExit(main())
