#!/usr/bin/env python3
"""Original flat coupled equations selecting the new bounded DN coordinator.

Only the shared-client import is redirected. Original BVP, physical BC,
outer true-DN acceptance, restart, tolerances and final seam remain intact.
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD_HERE = Path('/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/scripts')
spec = importlib.util.spec_from_file_location('db6f_flat_linear_control_original', OLD_HERE / 'db6f-prefix-flat-coupled.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
runner = base.m
original_module = runner.module
selected_control_module = None


def controlled_module(name, file):
    global selected_control_module
    file = Path(file)
    if file.resolve() == (OLD_HERE / 'db6f-prefix-tail-shared-client.py').resolve():
        selected_control_module = original_module(name, HERE / '78718-prefix-tail-linear-m15q512-v1.py')
        return selected_control_module
    return original_module(name, file)


runner.module = controlled_module
if __name__ == '__main__':
    runner.main()
