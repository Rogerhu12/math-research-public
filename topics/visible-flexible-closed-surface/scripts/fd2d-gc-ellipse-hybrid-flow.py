#!/usr/bin/env python3
"""Same fixed-g Codazzi flow with pointwise position/frame dynamics.

Only n,m use independent finite Fourier coefficients. Position and the
auxiliary frame evolve on the fine angular grid without truncating their
skew rotation products. Actual E,F,G and curvature remain separate finite
diagnostics. This is not a continuum certificate or a closed-surface solve.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from scipy import fft

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fd2d_hybrid_gc_base', HERE/'fd2d-gc-ellipse-flow.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
Original = base.Flow


class Hybrid(Original):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shape_selection = self.indices[1] < 2
        self.shape_indices = tuple(x[self.shape_selection] for x in self.indices)
        self.shape_size = len(self.shape_indices[0])
        self.active_wave = np.concatenate((self.shape_indices[0], np.zeros(12*self.work)))

    def initial(self):
        full = super().initial()
        other = np.zeros((self.work, 12), dtype=np.longdouble)
        ct, st = np.cos(self.theta), np.sin(self.theta)
        other[:, 0], other[:, 1] = self.A*ct, self.B*st
        other[:, 5] = 1
        other[:, 6], other[:, 7] = -self.A*st/self.ell0, self.B*ct/self.ell0
        other[:, 9], other[:, 10] = -other[:, 7], other[:, 6]
        return np.concatenate((full[self.shape_selection], np.asarray(other.ravel(), dtype=float)))

    def decode(self, state):
        raw = np.zeros((self.work//2+1, 2), dtype=np.clongdouble)
        factors = np.where(self.shape_indices[1] == 1, 1j, 1)
        raw[self.shape_indices] = np.asarray(state[:self.shape_size], dtype=np.longdouble)*factors
        shapes = fft.irfft(raw, n=self.work, axis=0, norm='forward')
        other = np.asarray(state[self.shape_size:], dtype=np.longdouble).reshape(self.work, 12)
        return np.column_stack((shapes, other))

    def encode(self, values):
        raw = fft.rfft(values[:, :2], axis=0, norm='forward')[self.shape_indices]
        shapes = np.where(self.shape_indices[1] == 1, raw.imag, raw.real)
        return np.asarray(np.concatenate((shapes, values[:, 2:].ravel())), dtype=float)


if __name__ == '__main__':
    base.Flow, base.__doc__ = Hybrid, __doc__
    base.main()
    out = Path(sys.argv[sys.argv.index('--out')+1])
    report = json.loads(out.read_text())
    report['pointwise_frame_adapter'] = base.identity(__file__)
    report['state_representation'] = 'Fourier n,m and native fine-grid position plus frame'
    report['skew_frame_products_angularly_truncated'] = False
    out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
