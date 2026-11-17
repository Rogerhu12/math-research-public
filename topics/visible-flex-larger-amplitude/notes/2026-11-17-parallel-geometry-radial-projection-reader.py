"""Observe the literal planar projection without changing radial geometry.

Use as --radial-reader for radial-measure.py.  All scalar products below use
the actual F, F_r and literal F_phi returned by the frozen reconstruction.
Positive sampled margins alone are not a continuous embedding certificate.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path

import numpy as np

_path = Path(__file__).with_name('2026-11-17-parallel-geometry-radial-tail-readout.py')
_spec = importlib.util.spec_from_file_location('frozen_radial_projection', _path)
_base = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_base)
read_geometry = _base.read_geometry


def cross2(a, b):
    return a[..., 0]*b[..., 1]-a[..., 1]*b[..., 0]


def run(args):
    previous_reader = read_geometry
    minima = {key: float('inf') for key in
        ('planar_radius', 'polar_angle_derivative', 'planar_jacobian',
         'radius_derivative_at_fixed_polar_angle')}
    winding = None

    def observed(alpha, xy, mean_height, data, coefficients, rho):
        nonlocal winding
        geometry = previous_reader(alpha, xy, mean_height, data, coefficients, rho)
        position = geometry['F'][:, :, :2]
        velocity = geometry['Fr'][:, :, :2]
        tangent = np.stack((np.cos(alpha), np.sin(alpha)), axis=2)
        # The stored error is exactly literal F_phi - q*t, not its PDE prediction.
        angular = geometry['angular_error']+coefficients['q'][:, :, None]*tangent
        radius = np.linalg.norm(position, axis=2)
        cross = cross2(position, angular)
        jacobian = cross2(velocity, angular)
        values = dict(planar_radius=radius,
            polar_angle_derivative=cross/(radius*radius),
            planar_jacobian=jacobian,
            radius_derivative_at_fixed_polar_angle=radius*jacobian/cross)
        for name, value in values.items():
            minima[name] = min(minima[name], float(np.min(value)))
        if winding is None:
            first = position[0]
            second = np.roll(first, -1, axis=0)
            winding = float(np.sum(np.arctan2(cross2(first, second),
                np.sum(first*second, axis=1)))/(2*np.pi))
        return geometry

    _base.read_geometry = observed
    final_out = args.out; args.out = None
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        _base.run(args)
    result = json.loads(captured.getvalue())
    result['projection_reader_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['planar_projection_measurements'] = dict(minima=minima,
        initial_polygon_winding=winding,
        scope='Actual open-tail sampled derivatives and initial polygon winding; no continuous embedding certificate')
    text = json.dumps(result, indent=2)+'\n'
    if final_out:
        final_out.write_text(text)
    print(text, end='')
