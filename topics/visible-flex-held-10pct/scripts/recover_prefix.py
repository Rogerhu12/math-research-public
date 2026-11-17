#!/usr/bin/env python3
"""Recover two archived open-prefix candidates without checking out old topics.

All generated checkpoints, source copies and endpoint arrays go to --dest.
The input repository may be a blob-filtered sparse clone. The immutable blob
hashes and commits are recorded in prefix_recovery_manifest.json. No credential
is accepted, persisted or required by this program beyond git's own transport.
These are finite open prefixes, not closed flexible surfaces.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

SOURCE_REL = Path('bundle/topics/visible-flexible-closed-surface')
COMP_REL = Path('bundle/topics/visible-flex-larger-amplitude/computations')
ARTIFACTS = {
    'q18': 'numerical-m2-v55v60-m10-q18',
    'q20': 'numerical-m2-v55v60-m16-q20',
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def restore(repo: Path, dest: Path, manifest: dict) -> None:
    repo, dest = repo.resolve(), dest.resolve()
    if dest == repo or repo in dest.parents:
        raise ValueError('--dest must be outside the repository: generated data stay in scratch')
    for row in manifest['files']:
        output = dest / row['target']
        if output.exists():
            if digest(output) != row['sha256']:
                raise ValueError('Existing output differs from manifest: ' + str(output))
            continue
        data = subprocess.check_output(['git', '-C', str(repo), 'show', row['revision'] + ':' + row['path']])
        if len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError('Immutable source hash mismatch: ' + row['path'])
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
    source = dest / SOURCE_REL
    (source / 'source-origin.json').write_text(json.dumps({
        'source_revision': manifest['source_revision'],
        'scope': 'Only individually SHA256-verified source files were restored.',
    }, indent=2) + '\n')
    (dest / 'recovery-provenance.json').write_text(json.dumps({
        'scope': __doc__, 'source_revision': manifest['source_revision'],
        'checkpoint_revision': manifest['checkpoint_revision'],
        'manifest_sha256': hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest(),
        'files': manifest['files'],
    }, indent=2) + '\n')


def load_prefix(dest: Path, name: str, angular: int = 512):
    import numpy as np
    from scipy.interpolate import PPoly
    source, comp = dest / SOURCE_REL, dest / COMP_REL
    spec = importlib.util.spec_from_file_location('held10_recovered_m2', comp / 'numerical-m2-prefix.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    adaptive = module.load(source)
    from curve_stable_prefix_bvp import load_checkpoint
    checkpoint = dest / 'restored_prefix' / (ARTIFACTS.get(name, name) + '.json.gz')
    rec = load_checkpoint(checkpoint)
    if not rec['solver_success']:
        raise ValueError('The supplied prefix was not a successful finite solve')
    port = json.loads((comp / 'numerical-m2-port24.json').read_text())
    _, BVP = adaptive.build_classes(rec['chart'])
    obj = BVP(rec['frozen_profile'], port, rec['gauge_amplitude'], rec['config']['modes'], angular, True, rec['warp_reference_q'])
    par = np.array(rec['parameters'])
    par[0] = math.log(rec['actual_primary_amplitude'] / obj.q)
    obj.initial(par)
    flow = obj.flow(par[0])
    x = np.array(rec['mesh'])
    pp = PPoly.construct_fast(np.array(rec['pp_coefficients']), x, extrapolate=True, axis=1)
    sol = SimpleNamespace(x=x, y=pp(x), p=par, sol=pp)
    return rec, obj, flow, pp, sol


def endpoint(dest: Path, name: str, angular: int = 512) -> dict:
    """Physical terminal position and two-jet, including the missing mean height."""
    import numpy as np
    rec, obj, flow, pp, sol = load_prefix(dest, name, angular)
    s = np.array([flow.end])
    height = flow.height_integral(sol, s, angular, 6)[0]
    B, B1, B2 = flow.basis(angular)
    Y, Yp, Ypp = pp(s), pp(s, 1), pp(s, 2)
    frame, Fsp, dW = flow.velocity_s(s, Y, Yp, B1, B2)
    geo = frame['geo']
    # At this terminal circle, the adaptive angular warp is exactly the
    # material chart. Hence these derivatives require no chart correction.
    for key in ('v', 'vp', 'vs'):
        if np.max(abs(geo[key])) >= 1e-12:
            raise ValueError('Endpoint is not in the identity angular chart')
    if np.max(abs(geo['rho'] - 1)) >= 1e-12:
        raise ValueError('Endpoint angular scale differs from one')
    X = (geo['pos'] + obj.q * flow.values(Y, B))[0]
    X[:, 2] += height
    Xs = (geo['s1'] + obj.q * flow.values(Yp, B))[0]
    Xs[:, 2] += np.mean(frame['V'][:, :, 2])
    Xss = (geo['s2'] + obj.q * flow.values(Ypp, B))[0]
    Xss[:, 2] += np.mean(dW[:, :, 2])
    data = dict(X=X, Xs=Xs, Xss=Xss, Xtheta=frame['d'][0],
                Xthetatheta=frame['dd'][0], Xstheta=Fsp[0], s=flow.end,
                height=height, theta=2 * np.pi * np.arange(angular) / angular)
    out = dest / 'restored_prefix' / (name + '_endpoint.npz')
    np.savez_compressed(out, **data)
    summary = {
        'scope': 'Recovered finite open-prefix terminal physical two-jet; not a closed surface.',
        'checkpoint': ARTIFACTS.get(name, name), 'angular': angular,
        'mean_height_quadrature_order': 6, 's': float(flow.end),
        'height_mean': float(height),
        'position_mean': X.mean(0).tolist(),
        'velocity_mean': Xs.mean(0).tolist(),
        'acceleration_mean': Xss.mean(0).tolist(),
        'derivative_norm_max': [float(np.linalg.norm(data[k], axis=1).max()) for k in ('Xs', 'Xss')],
        'npz_sha256': digest(out),
    }
    out.with_name(name + '_endpoint_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    return summary


def refine(dest: Path, stage: str, manifest: dict, force: bool = False) -> dict:
    """Execute the recorded q18 fixed-profile refinement, never redesign delta."""
    import numpy as np
    import scipy
    spec = manifest['refinements'][stage]
    out = dest / 'restored_prefix' / stage
    summary_path = out.with_name(out.name + '-summary.json')
    base = dest / 'restored_prefix' / (ARTIFACTS['q18'] + '.json.gz')
    with gzip.open(base, 'rt') as f:
        archived = json.load(f)
    if summary_path.exists() and not force:
        record = json.loads(summary_path.read_text())
        if not record.get('solver_success'):
            raise ValueError('Existing failed refinement: choose a new --dest or --force-refine')
        if record['frozen_profile'] != archived['frozen_profile'] or record['chart'] != archived['chart']:
            raise ValueError('Existing refinement does not have the archived fixed metric and chart')
        if not record.get('config', {}).get('fixed_metric'):
            raise ValueError('Existing output was a design solve, not a fixed-metric refinement')
        return record
    # The physical metric and the angular chart come from the same archived
    # q18 record at every spectral/radial resolution.
    profile, chart = dest / 'q18_fixed_profile.json', dest / 'q18_fixed_chart.json'
    profile.write_text(json.dumps(archived['frozen_profile'], indent=2) + '\n')
    chart.write_text(json.dumps(archived['chart'], indent=2) + '\n')
    restart = dest / 'restored_prefix' / (spec['restart'] + '.json.gz')
    if not restart.exists():
        if spec['restart'] in manifest['refinements']:
            refine(dest, spec['restart'], manifest, force=False)
        else:
            raise FileNotFoundError(restart)
    command = [sys.executable, str(dest / COMP_REL / 'numerical-m2-prefix.py'),
               '--source-topic', str(dest / SOURCE_REL), '--profile', str(profile),
               '--chart', str(chart), '--port', str(dest / COMP_REL / 'numerical-m2-port24.json'),
               '--out-prefix', str(out), '--restart', str(restart), '--fixed'] + spec['arguments']
    launch = dict(command=command, profile_sha256=digest(profile), chart_sha256=digest(chart),
                  restart_sha256=digest(restart), python=sys.version,
                  numpy=np.__version__, scipy=scipy.__version__,
                  scope='Actual fixed-metric open-prefix solve. The linear tail port is not a closed tail.')
    out.with_name(out.name + '-launch.json').write_text(json.dumps(launch, indent=2) + '\n')
    env = os.environ.copy()
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        env[key] = '1'
    log = out.with_name(out.name + '-run.log')
    with log.open('w') as stream:
        subprocess.run(command, env=env, stdout=stream, stderr=subprocess.STDOUT, check=True)
    record = json.loads(summary_path.read_text())
    if not record.get('solver_success'):
        raise RuntimeError('Finite BVP did not converge; inspect ' + str(log))
    if record['frozen_profile'] != archived['frozen_profile'] or record['chart'] != archived['chart']:
        raise ValueError('The supposedly fixed refinement changed its physical profile or chart')
    return record


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--dest', type=Path, required=True)
    p.add_argument('--manifest', type=Path, default=Path(__file__).with_name('prefix_recovery_manifest.json'))
    p.add_argument('--endpoints', nargs='*', default=['q18', 'q20'])
    p.add_argument('--angular', type=int, default=512)
    p.add_argument('--refine', nargs='*', choices=['q18-fixed-m16', 'q18-fixed-m24'], default=[])
    p.add_argument('--force-refine', action='store_true')
    a = p.parse_args()
    manifest = json.loads(a.manifest.read_text())
    restore(a.repo, a.dest, manifest)
    for stage in a.refine:
        record = refine(a.dest, stage, manifest, a.force_refine)
        print(json.dumps({'refinement': stage, 'success': record['solver_success'],
                          'nodes': record['nodes'], 'summary': record.get('summary', {})}), flush=True)
    for name in a.endpoints:
        print(json.dumps({'endpoint': name, **endpoint(a.dest, name, a.angular)}), flush=True)


if __name__ == '__main__':
    main()
