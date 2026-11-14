#!/usr/bin/env python3
"""Evaluate actual pointwise relative metric error at declared saved-field rows.

This distinguishes a finite angular FFT l1 diagnostic from actual pointwise
errors. The complete original physical quintic, material derivative formulas,
and original postprocessor mean rule are retained. All results are floating
point samples, not interval enclosures or global continuum bounds.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
EXPECTED = {
    'geometric-fixed-dual-prefix.py': 'f189c8f94880ff5455a140a686219a1805399e1d45a3809e176630bb92772280',
    'geometric-checkpoint-core-pullback.py': 'd319574d946f2f6c465b76ffeb92117201aa95bc4318e7100377b184a530fa33',
    'strong_initial_laws_interior_fullmean_audit.py': '35155b17516ce3ff72ddfc957894e53cbd2c7a4a6707d57e62887a8d72e4fbe0',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'source-topic', 'port', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--s', type=float, nargs='+', required=True)
    p.add_argument('--angular', type=int, required=True)
    a = p.parse_args()
    if a.out.exists() or a.angular < 128:
        raise ValueError('Require a fresh output and explicit angular samples')
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Original physical source changed: '+name)
    import strong_initial_laws_interior_fullmean_audit as laws
    observations = dict(provider_loads=0, saved_fields=[])
    pb = laws.install_audit_loader(load, observations)(
        'strong_metric_point_original_pullback', HERE/'geometric-checkpoint-core-pullback.py')
    data = a.input.read_bytes()
    record = json.loads(gzip.decompress(data) if a.input.suffix == '.gz' else data)
    saved, loader = pb.load_saved(a.input, a.source_topic, a.port, angular=int(record['config']['angular']))
    f, pp = saved.flow, saved.sol.sol
    s = np.asarray(a.s, dtype=np.float64)
    if np.any((s < 0)|(s > f.end)):
        raise ValueError('A declared sample lies outside the actual saved field')
    N = a.angular
    B, B1, B2 = f.basis(N)
    Y, Yp = pp(s), pp(s, 1)
    frame = f.frame(s, f.q*Y, B1, B2)
    g, radius = frame['geo'], frame['a']
    meanN = max(512, 16*(3*f.M+1))
    if N == meanN:
        mean = frame
    else:
        _, meanB1, meanB2 = f.basis(meanN)
        mean = f.frame(s, f.q*Y, meanB1, meanB2)
    velocity = g['s1']+f.q*f.values(Yp, B)
    velocity[:, :, 2] += np.mean(mean['V'][:, :, 2], axis=1)[:, None]
    velocity -= g['v'][:, :, None]*frame['d']
    tangent = frame['d']/g['rho'][:, :, None]
    E = np.sum(velocity*velocity, axis=2)-1
    F = np.sum(velocity*tangent, axis=2)/radius[:, None]
    G = np.sum(tangent*tangent, axis=2)/radius[:, None]**2-1
    relative_norm = np.abs((E+G)/2)+np.sqrt(((E-G)/2)**2+F**2)
    rows = []
    for i, value in enumerate(s):
        j = int(np.argmax(relative_norm[i]))
        components = {}
        for name, values in (('E', E), ('F', F), ('G', G)):
            k = int(np.argmax(np.abs(values[i])))
            components[name] = dict(maximum_pointwise_absolute=float(abs(values[i, k])),
                signed_value=float(values[i, k]), angular_index=k, psi=float(2*np.pi*k/N),
                finite_fft_l1=float(np.sum(abs(np.fft.fft(values[i])/N))))
        rows.append(dict(s=float(value), components=components,
            relative_metric_operator_norm=float(relative_norm[i, j]),
            norm_witness=dict(angular_index=j, psi=float(2*np.pi*j/N),
                E=float(E[i, j]), F=float(F[i, j]), G=float(G[i, j]))))
    chunks = {}
    for item in record['pp_coefficient_chunks']:
        path = a.input.parent/item['file']
        if sha(path) != item['sha256']:
            raise ValueError('Original physical quintic chunk differs')
        chunks[str(path)] = item['sha256']
    output = dict(scope=__doc__, input=str(a.input), input_sha256=sha(a.input),
        port_sha256=sha(a.port), physical_quintic_chunks_sha256=chunks,
        source_sha256={**EXPECTED, Path(__file__).name: sha(__file__)},
        source_dependencies=loader.dependencies(a.source_topic),
        provider_observations=observations, complete_physical_profile=record['frozen_profile'],
        complete_core=record['core'], rows=rows, angular=N, mean_angular=meanN,
        metric_normalization='g=diag(1,a(s)^2) in the fixed material (s,theta) coordinates',
        operator_norm_formula='abs((E+G)/2)+sqrt(((E-G)/2)^2+F^2)',
        actual_pointwise_sample=True, continuous_enclosure=False,
        original_saved_fft_l1=record['summary']['metric_l1'],
        no_field_modification_newton_or_tail_worker=True)
    with a.out.open('x') as stream:
        json.dump(output, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(event='actual_metric_point_witness', output=str(a.out),
        sha256=sha(a.out), rows=rows)), flush=True)


if __name__ == '__main__':
    main()
