#!/usr/bin/env python3
"""Compare every original/compressed stored array and actual Newton solution."""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import splu

P = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, P/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--profile', type=Path, required=True)
    p.add_argument('--projector', type=Path, required=True)
    p.add_argument('--work', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    base = load('compressed_compare_driver', 'geometry_20261114_projected_core_bvp.py')
    plain = load('compressed_compare_plain', 'geometry_20261114_separated_qr_bvp.py')
    compressed = load('compressed_compare_zip', 'geometry_20261114_separated_qr_compressed.py')
    data = base.fixed.read(args.checkpoint)
    profile = base.fixed.read(args.profile)
    projector = base.fixed.read(args.projector)
    M, N = data['M'], data['N']
    law = profile['geometry']['initial_law']
    c = np.array(data['states'][0][1:M+1])
    q = base.native.outward.FullCoreProbe(c, M, N, law['velocity'], law['length'], law['k0'])
    q.profile = base.fixed.FixedProfile(profile['geometry']).profile
    base.fixed.fft.enable_fft(q)
    flow = base.BatchedFFTFlow(q)
    x = np.array(data['mesh'][-3:])
    y = np.array(data['states'][-3:]).T
    n, m = q.n, len(x)
    h = np.diff(x)
    f = flow(x, y)
    ym = (y[:, :-1]+y[:, 1:])/2-h/8*(f[:, 1:]-f[:, :-1])
    df = flow.jac(x, y)
    dm = flow.jac((x[:-1]+x[1:])/2, ym)
    K = projector['first_mode']-1
    nl = 2*M+K+2
    left = np.zeros((n, n))
    right = np.zeros_like(left)
    left[:K+1, :K+1] = np.eye(K+1)
    j = np.arange(M)
    left[K+1+j, 1+j] = q.freq[1:]
    left[K+1+j, M+1+j] = 1
    j = np.arange(M+1)
    left[K+1+M+j, 2*M+1+j] = 1
    right[nl:] = np.array(projector['rows'])
    J = base.block_csc.assemble(n, m, h, df, dm, left, right)
    expected = np.sin(np.arange(n*m)*.17)*1e-3
    rhs = J@expected
    args.work.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='lossless-qr-compare-', dir=args.work) as work:
        factors = [module.DiskQRFactor(n, m, left, right, nl, work) for module in (plain, compressed)]
        for j in range(m-1):
            blocks = plain.local_blocks(h[j], df[:, :, j], dm[:, :, j], df[:, :, j+1])
            for factor in factors:
                factor.append(j, *blocks)
        exact_arrays = {}
        for j in range(m-1):
            with np.load(factors[0].directory/f'{j:05d}.npz') as a, np.load(factors[1].directory/f'{j:05d}.npz') as b:
                for name in a.files:
                    exact_arrays[f'{j}/{name}'] = a[name].dtype == b[name].dtype and a[name].shape == b[name].shape and a[name].tobytes() == b[name].tobytes()
        answers = [factor.finish().solve(rhs) for factor in factors]
        direct = splu(J).solve(rhs)
        sizes = [sum(p.stat().st_size for p in factor.directory.iterdir()) for factor in factors]
        result = dict(scope=__doc__, all_stored_arrays_bitwise_equal=all(exact_arrays.values()),
                      stored_array_checks=exact_arrays, complete_newton_solution_bitwise_equal=answers[0].tobytes() == answers[1].tobytes(),
                      original_vs_compressed_max=float(abs(answers[0]-answers[1]).max()),
                      compressed_residual_max=float(abs(J@answers[1]-rhs).max()),
                      compressed_vs_direct_max=float(abs(answers[1]-direct).max()),
                      rhs_max=float(abs(rhs).max()), uncompressed_bytes=sizes[0],
                      compressed_bytes=sizes[1], ratio=sizes[1]/sizes[0],
                      M=M, N=N, n=n, stations=x.tolist(), source_hashes={name: hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
                        ('geometry_20261114_separated_qr_bvp.py', 'geometry_20261114_separated_qr_compressed.py',
                         'geometry_20261114_compressed_qr_compare.py')},
                      input_hashes={str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (args.checkpoint, args.profile, args.projector)})
        for factor in factors:
            factor.close()
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
