#!/usr/bin/env python3
"""Regenerate the lost source/chart/port inputs from committed scalar records.

No former scratch path or deleted numerical checkpoint is required.  The
historical source manifest is used by recover_m3_source.py; subsequently only
the already published sparse linear algebra patch is installed.  Generated
ports/charts remain scratch data.  A regenerated numerical chart has its own
hash and is not asserted bitwise equal to the former unpreserved chart.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--workdir', type=Path, required=True)
    a = p.parse_args()
    repo, work = a.repo.resolve(), a.workdir.resolve()
    if repo == work or repo in work.parents:
        raise ValueError('Generated data must be outside the repository')
    work.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    seed = scripts/'nonlinear_tail/m3_coupled_seed_deliverable'
    sparse = scripts/'nonlinear_tail/m3_sparse_shooting_deliverable'
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
               VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(sparse/'sparse_shooting_linear.py'))
    commands = []
    def run(args):
        command = [sys.executable, *map(str,args)]
        commands.append(command)
        subprocess.run(command, env=env, check=True)
    run([seed/'recover_m3_source.py','--repo',repo,'--dest',work/'recovered-source'])
    run([sparse/'make_sparse_source.py','--source-recovery',work/'recovered-source',
         '--dest',work/'runtime-source'])
    source = work/'runtime-source/bundle/topics/visible-flexible-closed-surface'
    short = work/'runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py'
    inputs = work/'inputs'
    inputs.mkdir()
    binding_path = scripts/'resume_closed/q060_cosine_reference_binding.json'
    binding = json.loads(binding_path.read_text())
    cfg = json.loads((scripts/'resume_m3/recovered_q021/tail-settings.json').read_text())
    prefix, length = cfg.pop('valleyControlsPrefix'), cfg.pop('valleyControlsLength')
    cfg['valleyControls'] = prefix+[0]*(length-len(prefix))
    cfg['projectionFloor'] = .05
    def save(name,value):
        path = inputs/name
        path.write_text(json.dumps(value,indent=2)+'\n')
        return path
    baseline_config = save('baseline-tail.json',cfg)
    cfg.update(binding['physical_tail_parameters'])
    cfg['shootingParts'] = 16
    config = save('q060-tail.json',cfg)
    save('q060-profile.json',binding['physical_profile'])
    exporter = scripts/'resume_m3/recovered_q021/export_original_worker_port.py'
    for name, config_path in [('baseline',baseline_config),('q060',config)]:
        run([exporter,'--source-topic',source,'--config',config_path,
             '--out',inputs/f'{name}-port.json'])
    run([seed/'regenerate_m3_reference.py','--source-topic',source,
         '--short-bridge',short,'--profile',seed/'fast45-reference-profile.json',
         '--port',inputs/'baseline-port.json','--out',inputs/'reference'])
    sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
    result = dict(scope=__doc__,commands=commands,source_topic=str(source),
        short_bridge=str(short),binding_sha256=sha(binding_path),
        generated={str(f.relative_to(work)):sha(f) for f in inputs.rglob('*.json')},
        old_checkpoint_restored=False,old_unknown_lambda082_terminal_inferred=False)
    (work/'bootstrap.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(source_topic=str(source),short_bridge=str(short),
                         inputs=str(inputs),bootstrap_sha256=sha(work/'bootstrap.json'))))


if __name__=='__main__':
    main()
