#!/usr/bin/env python3
"""Audit frozen physical data and material two-jets along a true finite D-N chain.

Only saved successful solutions are compared. This is a spatial sample audit,
not an infinite-tail existence theorem or a continuous error enclosure.
"""
from __future__ import annotations
import os
for _variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_variable] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def read(path):
    with gzip.open(path, 'rt') if path.suffix == '.gz' else path.open() as handle:
        return json.load(handle)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoints', type=Path, nargs='+', required=True)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--port', type=Path, required=True)
    parser.add_argument('--angular', type=int, default=256)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if len(args.checkpoints) < 2:
        raise ValueError('Provide at least two actually solved checkpoints')
    metadata = [read(path) for path in args.checkpoints]
    fixed_keys = ('frozen_profile', 'physical_tail_parameters', 'physical_tail_cut',
                  'angular_chart', 'chart_reference_coefficients',
                  'chart_reference_frequencies', 'gauge_amplitude', 'meridian_length')
    for data in metadata:
        if not data.get('solver_success') or not data['config'].get('actual_nonlinear_tail'):
            raise ValueError('Every checkpoint must be an actual successful nonlinear-tail solve')
        for key in fixed_keys:
            if canonical(data[key]) != canonical(metadata[0][key]):
                raise ValueError('Fixed physical datum changed: ' + key)
        for key in ('depth', 'shootingParts'):
            if data['actual_tail']['config'][key] != metadata[0]['actual_tail']['config'][key]:
                raise ValueError('Finite-tail domain or shooting topology changed: ' + key)
    result = dict(scope=__doc__, physical_data_canonically_identical=True,
                  fixed_datum_sha256={key: hashlib.sha256(canonical(metadata[0][key])).hexdigest()
                                     for key in fixed_keys},
                  finite_tail_depth=metadata[0]['actual_tail']['config']['depth'],
                  shooting_parts=metadata[0]['actual_tail']['config']['shootingParts'],
                  checkpoints=[], consecutive_material_comparisons=[],
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    pullback = module('root_chain_pullback', HERE / 'geometric-checkpoint-core-pullback.py')
    utility = module('root_chain_fixed_utility', HERE / 'geometric-fixed-dual-prefix.py')
    previous = None
    start = time.time()
    for path, data in zip(args.checkpoints, metadata):
        saved, _ = pullback.load_saved(path, args.source_topic, args.port,
                                       angular=data['config']['angular'])
        tail = data['actual_tail']
        response_path = Path(tail['final_response'])
        response = read(response_path)['response']
        row = dict(file=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                   modes=data['modes'], angular=data['config']['angular'], nodes=data['nodes'],
                   tolerance=data['config']['tol'], fixed_metric=data['config']['fixed_metric'],
                   summary=data['summary'], actual_tail_residual=tail['residual'],
                   actual_tail_audit=response.get('audit'),
                   actual_tail_final_response=str(response_path),
                   actual_tail_response_sha256=hashlib.sha256(response_path.read_bytes()).hexdigest(),
                   physical_polynomial_degree=int(saved.sol.sol.c.shape[0] - 1),
                   coefficient_chunks=data.get('pp_coefficient_chunks'))
        result['checkpoints'].append(row)
        if previous is not None:
            comparison = utility.compare_shape(previous, SimpleNamespace(flow=lambda: saved.flow),
                                                saved.sol, args.angular)
            comparison.update(previous_file=result['checkpoints'][-2]['file'], current_file=str(path))
            result['consecutive_material_comparisons'].append(comparison)
            print(json.dumps(dict(event='compared', previous_file=comparison['previous_file'],
                                  current_file=str(path),
                                  max_distance=comparison['maximum_material_point_displacement_sample'],
                                  jets=comparison['physical_material_jet_differences_max_sample'])), flush=True)
        previous = saved
        result['seconds'] = time.time() - start
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
