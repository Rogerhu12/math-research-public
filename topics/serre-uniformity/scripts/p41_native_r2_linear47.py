#!/usr/bin/env python3
"""Native exact integer F47^2 elimination, preserving the published pivots.

All entry operations before reduction are positive and below 4*47^2.
The full 47^4 inverse and every Makdisi kernel remain verified by the
published bounded matrix products after two Newton lifting steps.
"""
import ctypes
import hashlib
from pathlib import Path
import subprocess


def install(r, build_dir):
    import numpy as np
    if getattr(r.rank_pivots, 'native_exact_mod47', False):
        return r.rank_pivots.native_manifest
    source = Path(__file__).with_name('p41_r2_mod47_native.cpp')
    source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
    build_dir = Path(build_dir).resolve()
    build_dir.mkdir(parents=True, exist_ok=True)
    output = build_dir/('p41_r2_mod47_'+source_sha[:16]+'.so')
    command = ['c++', '-O3', '-std=c++17', '-shared', '-fPIC', '-march=native', str(source), '-o', str(output)]
    if not output.exists():
        subprocess.run(command, check=True, capture_output=True, text=True)
    lib = ctypes.CDLL(str(output))
    p64 = np.ctypeslib.ndpointer(dtype=np.int64, ndim=2, flags='C_CONTIGUOUS')
    p32 = np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='C_CONTIGUOUS')
    lib.r2_rank_p.argtypes = [ctypes.c_int, ctypes.c_int, p64, p64, p32, p32]
    lib.r2_rank_p.restype = ctypes.c_int
    lib.r2_inverse_p.argtypes = [ctypes.c_int, p64, p64, p64, p64]
    lib.r2_inverse_p.restype = ctypes.c_int
    old_rank, old_inverse = r.rank_pivots, r.inverse_matrix
    manifest = {'method': 'exact native integer Gaussian elimination in F47[i]/(i^2+1)',
                'cpp_source_sha256': source_sha,
                'wrapper_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'compiled_binary_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                'compile_command': command,
                'compiler': subprocess.run(['c++', '--version'], check=True, capture_output=True, text=True).stdout.splitlines()[0]}

    def rank_pivots(A):
        ar, ai = [np.ascontiguousarray(x, dtype=np.int64) for x in A]
        assert ar.shape == ai.shape and ar.ndim == 2
        m, n = ar.shape
        rr, cc = np.empty(min(m, n), dtype=np.int32), np.empty(min(m, n), dtype=np.int32)
        k = lib.r2_rank_p(m, n, ar, ai, rr, cc)
        assert 0 <= k <= min(m, n)
        return rr[:k].astype(int).tolist(), cc[:k].astype(int).tolist()

    def inverse_matrix(A, q=r.Q):
        ar, ai = [np.ascontiguousarray(x, dtype=np.int64) for x in A]
        n = ar.shape[0]
        assert ar.shape == ai.shape == (n, n)
        re, im = np.empty((n, n), dtype=np.int64), np.empty((n, n), dtype=np.int64)
        assert lib.r2_inverse_p(n, ar, ai, re, im) == 0, 'Matrix has no unit inverse'
        inverse = re, im
        if q != r.P:
            for _ in range(2):
                inverse = r.mm(inverse, r.sub(r.add(r.eye(n), r.eye(n), q), r.mm(A, inverse, q), q), q)
        assert r.equal(r.mm(A, inverse, q), r.eye(n))
        return inverse

    rank_pivots.native_exact_mod47 = True
    rank_pivots.native_manifest = manifest
    rank_pivots.original_numpy_rank = old_rank
    inverse_matrix.native_exact_mod47 = True
    inverse_matrix.original_numpy_inverse = old_inverse
    r.rank_pivots, r.inverse_matrix = rank_pivots, inverse_matrix
    return manifest
