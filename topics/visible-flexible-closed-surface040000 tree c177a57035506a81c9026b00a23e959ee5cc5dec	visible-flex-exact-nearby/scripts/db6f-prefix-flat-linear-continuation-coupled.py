#!/usr/bin/env python3
"""Original flat coupled equations selecting the new bounded DN coordinator.

Only the shared-client import is redirected. Original BVP, physical BC,
outer true-DN acceptance, restart, tolerances and final seam remain intact.
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('db6f_flat_linear_control_original', HERE / 'db6f-prefix-flat-coupled.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
runner = base.m
original_module = runner.module


def controlled_module(name, file):
    file = Path(file)
    if file.resolve() == (HERE / 'db6f-prefix-tail-shared-client.py').resolve():
        return original_module(name, HERE / 'db6f-prefix-tail-linear-continuation-client.py')
    return original_module(name, file)


runner.module = controlled_module
if __name__ == '__main__':
    runner.main()
