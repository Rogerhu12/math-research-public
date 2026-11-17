#!/usr/bin/env python3
"""Restore exact sources and regenerate a widecut port/chart in scratch.

Only source, physical parameters and commands are read from the repository.
The original positive-A worker and all nonlinear acceptance gates remain intact.
No generated DN, chart or checkpoint is copied into the repository.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--dest', type=Path, required=True)
    p.add_argument('--config', type=Path,
                   default=Path(__file__).with_name('widecut_m2_opt_config.json'))
    p.add_argument('--peak-fraction', type=float, default=.2)
    a = p.parse_args()
    repo, dest = a.repo.resolve(), a.dest.resolve()
    if dest == repo or repo in dest.parents:
        raise ValueError('All regenerated files must stay outside the repository')
    dest.mkdir(parents=True, exist_ok=False)
    here = Path(__file__).resolve().parent
    topic = here.parents[2]
    coupling = topic / 'scripts/coupling'
    # The existing 71-file closure includes the immutable prefix, physical
    # factory, original worker and all its imports, plus the prefix chart code.
    manifests = [coupling / 'coupling_recovery_manifest.json',
                 here / 'widecut_extra_sources.json']
    recovery = dest / 'recovery'
    restored = []
    for manifest in manifests:
        for row in json.loads(manifest.read_text())['files']:
            payload = subprocess.check_output(
                ['git', '-C', str(repo), 'show', row['revision']+':'+row['path']])
            if (len(payload) != row['bytes'] or
                    hashlib.sha256(payload).hexdigest() != row['sha256']):
                raise ValueError('Immutable source mismatch: '+row['path'])
            target = recovery / row['target']
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            restored.append(row['target'])
    source = recovery / 'bundle/topics/visible-flexible-closed-surface'
    comp = recovery / 'bundle/topics/visible-flex-larger-amplitude/computations'
    worker = source / 'scripts/78718-prefix-tail-tangent-fourier-worker.mjs'
    config = dest / 'tail-config.json'
    shutil.copyfile(a.config, config)
    port = dest / 'physical-port.json'
    export = [sys.executable, str(here/'export_hybrid_ready_port.py'),
              '--source-topic', str(source), '--worker', str(worker),
              '--config', str(config), '--out', str(port),
              '--constructor', 'closing_weighted_tail_v1']
    subprocess.run(export, check=True)
    path = recovery / 'coupling_helpers/smallcut_prefix_sweep.py'
    spec = importlib.util.spec_from_file_location('widecut_replay_sweep', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    profile = dict(direction='outward', vu=.55, vd=.6, delta=.1718,
                   ramp=.4, ramp_eta=.05, ramp_law='flat', cycles=1,
                   prefix_bridge=dict(kind='turn_plateau_v1', curvature=4.,
                                      peak_fraction=a.peak_fraction))
    module.prepare(source, comp, port, profile, dest)
    common = ['--source-topic', str(source), '--profile', str(dest/'profile.json'),
              '--chart', str(dest/'chart.json'), '--port', str(port)]
    seed = [sys.executable, '-u', str(comp/'numerical-m2-prefix.py'), *common,
            '--out-prefix', str(dest/'linear-seed'), '--amplitude', '.001',
            '--warp-reference', '.001', '--modes', '8', '--angular', '256',
            '--audit-angular', '512', '--nodes', '401', '--max-nodes', '2000',
            '--tol', '1e-6', '--bc-tol', '1e-7', '--physical-bc-tol', '2e-9']
    design = [sys.executable, '-u', str(coupling/'couple_smallcut.py'), *common,
              '--prefix-driver', str(comp/'numerical-m2-prefix.py'),
              '--coupler-source', str(source/'scripts/db6f-prefix-coupled.py'),
              '--worker', str(worker), '--tail-config', str(config),
              '--restart', str(dest/'linear-seed.json.gz'),
              '--out', str(dest/'coupled'), '--amplitude', '.001', '--modes', '8',
              '--nodes', '401', '--max-nodes', '2000', '--tol', '1e-6',
              '--warmup-scales', '.01', '.1', '.3', '1', '--inner-verbose', '2']
    # Historical diagnostic failure is an initializer only. These fixed-g
    # commands retain every original physical boundary and outer DN gate.
    shutil.copyfile(here/'q001-fixed-profile.json', dest/'fixed-profile.json')
    fixed_config = json.loads(config.read_text())
    fixed_config['initialCheckpoint'] = str(dest/'coupled/response_0006.json.gz')
    (dest/'fixed-tail-config.json').write_text(json.dumps(fixed_config, indent=2)+'\n')
    fixed = design.copy()
    replacements = {'--profile': str(dest/'fixed-profile.json'),
                    '--tail-config': str(dest/'fixed-tail-config.json'),
                    '--restart': str(dest/'coupled/prefix.json.gz'),
                    '--out': str(dest/'fixed-coupled'), '--max-nodes': '2200'}
    for key, value in replacements.items():
        fixed[fixed.index(key)+1] = value
    j = fixed.index('--warmup-scales')
    fixed[j+1:j+5] = ['1']
    fixed.append('--fixed')
    fixed_config['initialCheckpoint'] = str(dest/'fixed-coupled/response_0004.json.gz')
    (dest/'q002-tail-config.json').write_text(json.dumps(fixed_config, indent=2)+'\n')
    next_stage = fixed[:-1]
    replacements = {'--tail-config': str(dest/'q002-tail-config.json'),
                    '--restart': str(dest/'fixed-coupled/prefix.json.gz'),
                    '--out': str(dest/'q002-coupled'), '--max-nodes': '2400',
                    '--nodes': '501', '--amplitude': '.002'}
    for key, value in replacements.items():
        next_stage[next_stage.index(key)+1] = value
    j = next_stage.index('--warmup-scales')
    next_stage[j+1:j+2] = ['.51', '.65', '.8', '1']
    report = dict(scope=__doc__, restored_source_files=len(restored),
                  source_manifest_hashes={x.name:digest(x) for x in manifests},
                  commands=dict(export=export, seed=seed, design=design,
                                fixed=fixed, next_design=next_stage),
                  generated_hashes={x:digest(dest/x) for x in
                      ('tail-config.json', 'physical-port.json', 'profile.json',
                       'chart.json', 'fixed-profile.json')},
                  checkpoint_note='Response numbers are the recorded historical sequence. '
                      'If a new solve changes call counts, select its last converged full '
                      'tail response explicitly and update initialCheckpoint; never substitute '
                      'an unconverged state. No solve is run by this preparation command.')
    (dest/'widecut-preparation.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(event='widecut_prepared', destination=str(dest),
                          restored_source_files=len(restored),
                          manifest=str(dest/'widecut-preparation.json'))))


if __name__ == '__main__':
    main()
