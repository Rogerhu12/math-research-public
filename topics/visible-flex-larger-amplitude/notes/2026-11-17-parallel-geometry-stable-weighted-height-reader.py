"""Full fixed-physical-angle rho with the same safeguarded mean-root solve.

This combines the frozen weighted chain rule with the integral-K evaluation
and residual-based Newton stopping already used for the material reader.
No rho coefficient, height mode, or nonlinear mean equation is changed.
"""
from pathlib import Path
import importlib.util


def _load(filename, name):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_weighted = _load('2026-11-17-parallel-geometry-weighted-height-reader.py',
                  'frozen_weighted_height')
_stable = _load('2026-11-17-parallel-geometry-stable-height-reader.py',
                'stable_material_height')


class HeightReader(_weighted.HeightReader):
    solve_mean = _stable.HeightReader.solve_mean
    evaluate = _stable.HeightReader.evaluate

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.height_source != 'k-integral':
            raise ValueError('This adapter preserves the integral-K candidate only')
