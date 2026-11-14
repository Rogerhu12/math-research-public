#!/usr/bin/env python3
"""Original flat coupled solve, selecting the diagnostic-only tail client.

The reviewed original BVP/BC/outer acceptance and actual DN equations are
unchanged. Only the existing shared-client import is redirected to the
reviewed trial-recording client, so failures retain stage inputs/reasons.
"""
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('db6f_flat_trial_original',HERE/'db6f-prefix-flat-coupled.py')
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
runner=base.m
original_module=runner.module


def recorded_module(name,file):
    file=Path(file)
    if file.resolve()==(HERE/'db6f-prefix-tail-shared-client.py').resolve():
        return original_module(name,HERE/'db6f-prefix-tail-trial-client.py')
    return original_module(name,file)


runner.module=recorded_module
if __name__=='__main__':
    runner.main()
