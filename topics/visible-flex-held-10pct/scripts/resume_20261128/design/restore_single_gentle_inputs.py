#!/usr/bin/env python3
"""Recover only the published R87 prefix inputs after scratch loss.

The original 70-source recovery reads immutable git objects.  Original source
installers and port/chart exporters then restore the necessary definitions.
The already published linear calibration and root profile are serialized only
when their full SHA-256 agrees with the original recorded file.  No root search,
BVP, nonlinear tail, native compilation or old q=.06 branch is executed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    args = parser.parse_args()
    repo, work = args.repo.resolve(), args.work.resolve()
    if work == repo or repo in work.parents:
        raise ValueError('Reproducible arrays and recovered inputs stay outside Git')
    work.mkdir(parents=True, exist_ok=False)
    topic = repo/'topics/visible-flex-held-10pct'
    scripts = topic/'scripts'
    seed = scripts/'nonlinear_tail/m3_coupled_seed_deliverable'
    sparse = scripts/'nonlinear_tail/m3_sparse_shooting_deliverable'
    env = dict(os.environ, OPENBLAS_NUM_THREADS='2', OMP_NUM_THREADS='2',
               MKL_NUM_THREADS='2', VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
               VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(sparse/'sparse_shooting_linear.py'))
    for key in ('LD_LIBRARY_PATH', 'LD_PRELOAD'):
        env.pop(key, None)
    commands = []
    started = time.monotonic()

    def save(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('x') as stream:
            stream.write(json.dumps(value, indent=2, allow_nan=False)+'\n')

    def py(script, *arguments):
        command = [sys.executable, str(script), *map(str, arguments)]
        commands.append(dict(command=command, source_sha256=sha(script)))
        subprocess.run(command, env=env, check=True)

    py(seed/'recover_m3_source.py', '--repo', repo, '--dest', work/'recovered-source')
    py(sparse/'make_sparse_source.py', '--source-recovery', work/'recovered-source',
       '--dest', work/'runtime-source')
    source = work/'runtime-source/bundle/topics/visible-flexible-closed-surface'
    short = work/'runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py'
    py(scripts/'resume_m3/multistage_flat_profile.py', '--source-topic', source,
       '--dest', work/'multistage-source')
    py(scripts/'resume_m3/install_shared_tail_engines.py', '--copy-from', work/'multistage-source',
       '--source-topic', work/'shared-source', '--manifest', work/'shared-install.json',
       '--export-modules', work/'shared-modules')
    inputs = work/'inputs'
    inputs.mkdir()
    base = json.loads((scripts/'resume_m3/recovered_q021/tail-settings.json').read_text())
    prefix, count = base.pop('valleyControlsPrefix'), base.pop('valleyControlsLength')
    base.update(valleyControls=prefix+[0]*(count-len(prefix)), projectionFloor=.05)
    save(inputs/'baseline-tail.json', base)
    cfg = json.loads((topic/'notes/2026-11-20-m3-m24-warm050-execution.json').read_text())['config']
    for key in ('chordMaxCorrections', 'initialCheckpoint', 'traceFile'):
        cfg.pop(key, None)
    save(work/'m24-tail-settings.json', cfg)
    exporter = scripts/'resume_m3/recovered_q021/export_original_worker_port.py'
    for conf, output in [(inputs/'baseline-tail.json', inputs/'baseline-port.json'),
                         (work/'m24-tail-settings.json', work/'m24-linear-port.json')]:
        py(exporter, '--source-topic', work/'shared-source', '--config', conf, '--out', output)
    py(seed/'regenerate_m3_reference.py', '--source-topic', source, '--short-bridge', short,
       '--profile', seed/'fast45-reference-profile.json', '--port', inputs/'baseline-port.json',
       '--out', inputs/'reference')

    first_path = topic/'notes/2026-11-28-design-single-gentle-linear-first-return-observed.json'
    root_path = topic/'notes/2026-11-28-design-single-gentle-linear-root-observed.json'
    first = json.loads(first_path.read_text())
    root = json.loads(root_path.read_text())
    restored = []
    records = [
        (work/'R87-single-gentle-linear-calibration-20261128/calibration.json',
         first['result'], '1f2ea915c659fdd944d1c2310e75081737504bb402c9bb6583f85d8afce21dec', first_path),
        (work/'R87-single-gentle-linear-calibration-extended-20261128/calibration.json',
         root['actual_linear_calibration'], root['complete_original_calibration_sha256'], root_path),
        (work/'R87-single-gentle-linear-calibration-extended-20261128/linear-root-profile.json',
         root['actual_linear_seed_profile']['parameters'], root['actual_linear_seed_profile']['sha256'], root_path),
    ]
    for path, record, expected, published in records:
        data = (json.dumps(record, indent=2, allow_nan=False)+'\n').encode()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError('Published text does not reconstruct original bytes: '+str(path))
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('xb') as stream:
            stream.write(data)
        restored.append(dict(path=str(path), sha256=sha(path), bytes=len(data),
                             published_source=str(published), published_source_sha256=sha(published)))
    calibration = root['actual_linear_calibration']
    for group in ('source_hashes', 'inputs'):
        for filename, expected in calibration[group].items():
            if sha(filename) != expected:
                raise ValueError('Recovered original calibration binding differs: '+filename)
    result = dict(status='published_R87_inputs_exactly_recovered',
        scope=__doc__, command=sys.argv, source_sha256=sha(__file__), commands=commands,
        restored_small_original_files=restored,
        calibration_source_and_input_bindings_all_match=True,
        generated=dict(chart_sha256=sha(inputs/'reference/chart.json'),
                       m24_port_sha256=sha(work/'m24-linear-port.json'),
                       source_topic=str(work/'multistage-source'),
                       shared_source=str(work/'shared-source'), short_bridge=str(short)),
        elapsed_seconds=time.monotonic()-started, launcher_requested_threads=2,
        original_modules_may_set_their_own_threads=True,
        new_root_search=False, new_mathematical_conclusion=False, BVP_executed=False,
        tail_executed=False, native_compiled=False)
    save(work/'R87-input-recovery-after-volume-reset.json', result)
    print(json.dumps(dict(status=result['status'], elapsed_seconds=result['elapsed_seconds'],
                          generated=result['generated'])))


if __name__ == '__main__':
    main()
