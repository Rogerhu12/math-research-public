#!/usr/bin/env python3
"""Apply the original finite metric-error decomposition to one accepted field.

The complete saved physical quintic is read without alteration. The original
diagnose routine separates radial interpolant residual, Fourier projection of
the physical velocity, and angular quadrature at every saved node, midpoint,
and the original 151 extra samples. This does not produce a new solution or a
continuous certificate. The mean and observation angular rule is the original
physical postprocessor's max(512,16*(3*M+1)); RHS angular order stays recorded.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
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
        p.add_argument('--' + name, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Fresh diagnostic output required')
    for name, expected in EXPECTED.items():
        if sha(HERE / name) != expected:
            raise ValueError('Frozen original source differs: ' + name)
    import strong_initial_laws_interior_fullmean_audit as laws
    observations = dict(provider_loads=0, saved_fields=[])
    hooked = laws.install_audit_loader(load, observations)
    pb = hooked('strong_residual_decomposition_pullback', HERE / 'geometric-checkpoint-core-pullback.py')
    raw = a.input.read_bytes()
    record = json.loads(gzip.decompress(raw) if a.input.suffix == '.gz' else raw)
    M = int(record['modes'])
    saved, loader = pb.load_saved(a.input, a.source_topic, a.port, angular=int(record['config']['angular']))
    if saved.flow.M != M or saved.flow.nt != int(record['config']['angular']):
        raise ValueError('Original M/angular identity was not restored')
    if observations['provider_loads'] != 1 or len(observations['saved_fields']) != 1:
        raise ValueError('Expected exactly one original accepted provider load')
    utility = load('strong_residual_decomposition_original', HERE / 'geometric-fixed-dual-prefix.py')
    result = utility.diagnose(saved, angular=max(512, 16*(3*M+1)))
    inputs = {str(a.input): sha(a.input), str(a.port): sha(a.port)}
    for item in record['pp_coefficient_chunks']:
        path = a.input.parent / item['file']
        if sha(path) != item['sha256']:
            raise ValueError('Original physical quintic chunk SHA differs')
        inputs[str(path)] = item['sha256']
    output = dict(scope=__doc__, input=str(a.input), input_sha256=sha(a.input),
        source_sha256={str(HERE/name): value for name, value in EXPECTED.items()},
        wrapper_sha256=sha(__file__), inputs_sha256=inputs, source_transforms=loader.TRANSFORMS,
        source_dependencies=loader.dependencies(a.source_topic), provider_observations=observations,
        complete_physical_profile=saved.rec['frozen_profile'], full_core=saved.rec['core'],
        numerical_solution_modified=False, newton_or_tail_worker_started=False, original_diagnose_unmodified=True,
        original_saved_metric_l1=saved.rec['summary']['metric_l1'],
        original_saved_flow_defect=saved.rec['summary']['flow_defect'], result=result)
    with a.out.open('x') as stream:
        json.dump(output, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(output=str(a.out), sha256=sha(a.out), result=result)), flush=True)


if __name__ == '__main__':
    main()
