#!/usr/bin/env python3
"""Extract a complete saved neck boundary in the physical tail orientation."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import numpy as np


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'checkpoint', 'port', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--desired-first-height', type=float, default=1.2e-4)
    a = p.parse_args()
    loader_path = Path(__file__).with_name('geometric-checkpoint-core-pullback.py')
    spec = importlib.util.spec_from_file_location('numerical_saved_neck_direction', loader_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    saved, _ = module.load_saved(a.checkpoint, a.source_topic, a.port, angular=512)
    if not saved.rec['solver_success'] or saved.mode != 2:
        raise ValueError('A successful complete m2 finite prefix is required')
    if saved.flow.iz != 2 * saved.M + 1:
        raise ValueError('Unexpected saved height-state layout')
    end = saved.flow.end
    psi = 2 * np.pi * np.arange(512) / 512
    angle = saved.angle(np.array([end]), psi[None, :])
    base = saved.base(np.array([end]), psi[None, :])
    checks = {
        'angle_identity_error': float(np.max(abs(angle['theta'] - psi[None, :]))),
        'angle_derivative_identity_error': float(np.max(abs(angle['rho'] - 1))),
        'angle_first_s_error': float(np.max(abs(angle['theta_s']))),
        'angle_second_s_error': float(np.max(abs(angle['theta_ss']))),
        'reference_height_error': float(np.max(abs(base['pos'][..., 2]))),
    }
    if max(checks.values()) > 1e-12:
        raise ValueError('The saved cut is not the required identity angle / zero reference height')
    sigma = float(saved.flow.bridge.sigma)
    port = json.loads(a.port.read_text())
    if sigma != float(np.sign(port['cut']['radius'] - 1)):
        raise ValueError('Saved neck radial orientation differs from the tail probe convention')
    prefix = saved.q * saved.sol.sol(end)[saved.flow.iz:]
    height = sigma * prefix
    if len(height) != saved.M or not np.all(np.isfinite(height)) or height[0] == 0:
        raise ValueError('Invalid complete physical boundary vector')
    coefficient_files = []
    for chunk in saved.rec.get('pp_coefficient_chunks', []):
        path = a.checkpoint.parent / chunk['file']
        actual_hash = digest(path)
        if actual_hash != chunk['sha256']:
            raise ValueError('Coefficient chunk hash mismatch')
        coefficient_files.append({'file': str(path), 'sha256': actual_hash,
                                  'bytes': path.stat().st_size})
    result = {
        'scope': 'Complete physical boundary extracted from one successful finite neck prefix. Its saved endpoint may use a finite linear tail condition. An external scalar multiple of this vector is a boundary-direction experiment, not a solved larger prefix or a coupled closed surface.',
        'source_revision': json.loads((a.source_topic / 'source-origin.json').read_text())['source_revision'],
        'prefix_checkpoint': str(a.checkpoint), 'prefix_checkpoint_sha256': digest(a.checkpoint),
        'coefficient_files': coefficient_files,
        'port': str(a.port), 'port_sha256': digest(a.port),
        'prefix_was_coupled_to_actual_tail': bool(saved.rec['config'].get('actual_nonlinear_tail')),
        'requested_q': saved.rec.get('requested_q'), 'gauge_amplitude': saved.q,
        'modes': saved.M, 'physical_frequencies': saved.frequencies.tolist(),
        'physical_length': end, 'frozen_prefix_profile': saved.rec['frozen_profile'],
        'physical_tail_parameters': port['parameters'], 'physical_tail_cut': port['cut'],
        'prefix_radial_orientation': sigma,
        'height_orientation_equation': 'Z_prefix = sigma * Z_tail + constant; H_tail = sigma * H_prefix',
        'prefix_nonmean_height': prefix.tolist(), 'tail_nonmean_height': height.tolist(),
        'complete_vector_preserved': True, 'cut_chart_checks': checks,
        'second_to_first_ratio': float(height[1] / height[0]),
        'desired_absolute_first_height': a.desired_first_height,
        'suggested_external_multiplier': a.desired_first_height / abs(float(height[0])),
        'loader_sha256': digest(loader_path), 'script_sha256': digest(Path(__file__)),
    }
    with a.out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'output': str(a.out), 'modes': saved.M,
                      'first_height': float(height[0]),
                      'second_height': float(height[1]),
                      'second_to_first_ratio': result['second_to_first_ratio'],
                      'external_multiplier': result['suggested_external_multiplier'],
                      'cut_chart_checks': checks}))


if __name__ == '__main__':
    main()
