"""Export actual terminal 0/1/2 jets from the frozen radial reconstruction.

Use as --radial-reader for radial-measure.py.  The small NPZ is written next
to the raw input, not into the repository.  No geometry equation is changed.
The exact boundary functions are defined by the original radial integrals;
the exported angular grid is numerical data for evaluating a closure.
"""
import contextlib
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path

import numpy as np

_path = Path(__file__).with_name('2026-11-17-parallel-geometry-radial-tail-readout.py')
_spec = importlib.util.spec_from_file_location('frozen_radial_end', _path)
_base = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_base)
read_geometry = _base.read_geometry


def run(args):
    prior = read_geometry
    terminal = {}

    def observed(alpha, xy, mean_height, data, coefficients, rho):
        geometry = prior(alpha, xy, mean_height, data, coefficients, rho)
        terminal.clear()
        for name in ('F', 'Fr', 'Frr'):
            terminal[name] = geometry[name][-1].copy()
        for name in ('h_phi', 'h_phiphi', 'hperp'):
            terminal[name] = data[name][-1].copy()
        for name in ('r', 'w', 'wr', 'c', 'cr'):
            terminal[name] = float(data[name][-1])
        terminal['mean_height'] = float(mean_height[-1])
        terminal['rho'] = rho.copy()
        terminal['alpha'] = alpha[-1].copy()
        tangent = np.column_stack((np.cos(alpha[-1]), np.sin(alpha[-1])))
        hp = geometry['angular_error'][-1]+coefficients['q'][-1, :, None]*tangent
        terminal['Fphi'] = np.column_stack((hp, data['h_phi'][-1]))
        return geometry

    _base.read_geometry = observed
    final_out = args.out; args.out = None
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        _base.run(args)
    result = json.loads(captured.getvalue())
    if result['height_anchor'] != 'left':
        raise ValueError('This outer-end export requires a left-anchored outward run')
    source = json.loads(gzip.decompress(args.input.read_bytes()))
    phi = 2*np.pi*np.arange(args.angles)/args.angles
    coefficients = np.asarray(source.get('rho_cos_coefficients', []))
    frequency = 2*np.arange(1, len(coefficients)+1)
    terminal['phi'] = phi
    terminal['Theta'] = phi+np.sin(phi[:, None]*frequency)@(coefficients/frequency)
    terminal['rho_phi'] = -np.sin(phi[:, None]*frequency)@(frequency*coefficients)
    terminal['Fphiphi'] = np.column_stack((
        _base.angular_derivative(terminal['F'][None, :, :2], 2)[0], terminal['h_phiphi']))
    terminal['Frphi'] = _base.angular_derivative(terminal['Fr'][None, :, :])[0]
    identity = dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        input_sha256=result['input_sha256'], background_sha256=result['background_sha256'],
        radial_source_sha256=result['source_sha256'],
        height_reader_sha256=result['height_reader_sha256'],
        angular_helper_sha256=result['angular_helper_sha256'],
        angles=args.angles, radial_gauss=args.radial_gauss,
        scope='Sampled actual endpoint jets of the exact integral-defined candidate')
    terminal['identity_json'] = json.dumps(identity, sort_keys=True)
    stem = args.input.name.removesuffix('.json.gz')
    target = args.input.with_name(f'{stem}-end-jets-n{args.angles}-g{args.radial_gauss}.npz')
    np.savez_compressed(target, **terminal)
    result['end_jet_export'] = dict(**identity, path=str(target),
        sha256=hashlib.sha256(target.read_bytes()).hexdigest())
    text = json.dumps(result, indent=2)+'\n'
    if final_out:
        final_out.write_text(text)
    print(text, end='')
