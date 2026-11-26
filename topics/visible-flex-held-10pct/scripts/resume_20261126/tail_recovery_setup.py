#!/usr/bin/env python3
"""Restore the recorded M24 inputs without an old scratch directory.

This performs necessary source/parameter reconstruction, not a new BVP or a
new proof. Generated charts, ports, native code and arrays stay outside Git.
The shared allocation exporter avoids the unobserved initialization failure
of the original unshared bootstrap in the 2026-11-26 environment.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    args = parser.parse_args()
    repo, work = args.repo.resolve(), args.work.resolve()
    if work == repo or repo in work.parents:
        raise ValueError('Generated data must be outside the repository')
    work.mkdir(parents=True, exist_ok=False)
    topic = repo/'topics/visible-flex-held-10pct'
    scripts = topic/'scripts'
    seed = scripts/'nonlinear_tail/m3_coupled_seed_deliverable'
    sparse = scripts/'nonlinear_tail/m3_sparse_shooting_deliverable'
    commands = []
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
               VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(sparse/'sparse_shooting_linear.py'))
    for key in ('LD_LIBRARY_PATH', 'LD_PRELOAD'):
        env.pop(key, None)

    def run(*command):
        command = list(map(str, command))
        commands.append(command)
        subprocess.run(command, env=env, check=True)

    def py(script, *args):
        run(sys.executable, script, *args)

    def save(path, value):
        path.write_text(json.dumps(value, indent=2)+'\n')

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
    center_path = scripts/'resume_m3/multistage_m24_core_neighborhood.json'
    center = json.loads(center_path.read_text())
    save(work/'m24-recovery-controls.json', dict(
        full_actual_controls=[float.fromhex(x) for x in center['center_control_hex']],
        scope='Recorded physical controls for necessary direct field regeneration; no full raw checkpoint.',
        source_center_sha256=hashlib.sha256(center_path.read_bytes()).hexdigest()))
    profile = json.loads((scripts/'resume_m3/multistage_profile_linear_root.json').read_text())
    profile['delta'] = .06413464104697915
    save(work/'m24-recovery-profile.json', profile)
    shutil.copytree(work/'shared-source', work/'periodic-source',
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    py(scripts/'resume_n4_tail/install_periodic_quadrature.py', '--source-topic', work/'periodic-source',
       '--manifest', work/'periodic-install.json')
    py(scripts/'resume_m3/install_bounded_chord_tail.py', '--copy-from', work/'periodic-source',
       '--source-topic', work/'chord-source', '--manifest', work/'chord-install.json')
    native = scripts/'resume_n4_tail/native_extended'
    run('g++', '-std=c++17', '-O2', '-fno-fast-math', '-ffp-contract=off',
        '-fexcess-precision=standard', '-frounding-math', '-DVF_BUILD_MAIN',
        native/'frozen_flow_production.cpp', '-o', work/'frozen_flow_batch', '-lm')
    py(native/'prepare_recovered_native.py', '--source-topic', work/'chord-source',
       '--dest', work/'native-tail24', '--native-cli', work/'frozen_flow_batch',
       '--modes', 24, '--spacing', 3, '--quadrature', 512, '--steps', 16, '--workers', 2)
    files = [inputs/'reference/chart.json', work/'m24-tail-settings.json',
             work/'m24-linear-port.json', work/'frozen_flow_batch',
             work/'native-tail24/native-manifest.json']
    result = dict(scope=__doc__, commands=commands, generated={
        str(path.relative_to(work)):hashlib.sha256(path.read_bytes()).hexdigest() for path in files},
        BVP_executed=False, tail_executed=False)
    save(work/'recovery-setup.json', result)
    print(json.dumps(result['generated']))


if __name__ == '__main__':
    main()
