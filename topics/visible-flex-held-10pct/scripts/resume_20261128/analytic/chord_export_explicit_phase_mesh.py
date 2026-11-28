#!/usr/bin/env python3
"""Export a genuine original 7a field on an explicitly supplied phase interval."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name] = '1'
from explicit_phase_mesh_adapter import run

if __name__ == '__main__':
    run('chord',__file__)
