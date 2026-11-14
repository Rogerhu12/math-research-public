#!/usr/bin/env python3
"""Lossless compressed storage for the unchanged separated QR elimination.

The retained L, R, LU, piv and T arrays are identical to the original backend.
Only ZIP storage changes to DEFLATE. After a file is complete, Linux may drop
that owned clean file from page cache; no other file or global cache is touched.
"""
import importlib.util
import json
import os
import warnings
from pathlib import Path

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('compressed_original_qr', P/'geometry_20261114_separated_qr_bvp.py')
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)


class CompressedDiskQRFactor(original.DiskQRFactor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.raw_array_bytes = 0
        self.compressed_file_bytes = 0

    def append(self, j, L, R):
        if j != self.next_interval:
            raise ValueError('Intervals must be appended sequentially')
        with warnings.catch_warnings():
            warnings.simplefilter('error', original.LinAlgWarning)
            try:
                LU, piv = original.lu_factor(R.copy(order='F'), overwrite_a=True, check_finite=False)
            except original.LinAlgWarning as error:
                raise RuntimeError('Local right collocation block is singular; QR elimination broke down') from error
        T = original.lu_solve((LU, piv), -L, check_finite=False)
        self.U[j+1], self.transport[j] = original.qr(T@self.U[j], mode='economic', check_finite=False)
        filename = self.directory/f'{j:05d}.npz'
        arrays = dict(L=L, R=R, LU=LU, piv=piv, T=T)
        original.np.savez_compressed(filename, **arrays)
        self.raw_array_bytes += sum(a.nbytes for a in arrays.values())
        self.compressed_file_bytes += filename.stat().st_size
        if hasattr(os, 'posix_fadvise'):
            with filename.open('rb') as stream:
                os.fdatasync(stream.fileno())
                os.posix_fadvise(stream.fileno(), 0, 0, os.POSIX_FADV_DONTNEED)
        self.next_interval += 1

    def finish(self):
        result = super().finish()
        print(json.dumps(dict(event='lossless_qr_storage', intervals=self.m-1,
                              raw_array_bytes=self.raw_array_bytes,
                              compressed_file_bytes=self.compressed_file_bytes,
                              ratio=self.compressed_file_bytes/self.raw_array_bytes,
                              arithmetic_unchanged=True)), flush=True)
        return result


original.DiskQRFactor = CompressedDiskQRFactor
DiskQRFactor = CompressedDiskQRFactor
local_blocks = original.local_blocks
enable = original.enable
factor = original.factor
