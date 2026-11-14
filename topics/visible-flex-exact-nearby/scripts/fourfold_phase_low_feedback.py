#!/usr/bin/env python3
"""Physical finite core/cap feedback, retaining both regular mean rows.

This assembles saved floating finite models. Multiplication traces are
projected at the same finite cutoff and their discarded modes are not paid.
It is an executable candidate for later true Schur certification, not the
complete infinite low block or a proof of its inverse.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.linalg import block_diag

from fourfold_phase_core_low_block import CoreBlock, physical_coefficients


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_arrays(report):
    entry = report['arrays']
    path = Path(entry['path'])
    if sha(path) != entry['sha256']:
        raise ValueError('a saved finite matrix array changed')
    with np.load(path, allow_pickle=False) as stored:
        return {key:stored[key].copy() for key in stored.files}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--core', type=Path, default=Path('notes/2026-11-12-actual-core-low-block-M4.json'))
    parser.add_argument('--cap', type=Path, default=Path('notes/2026-11-12-actual-cap-low-Schur-M4.json'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    core, cap = [json.loads(path.read_text()) for path in (args.core, args.cap)]
    for key in ('object_sha256', 'origin_inputs_sha256', 'direction_sha256', 'exact_delta_fraction', 'modes'):
        if core[key] != cap[key]:
            raise ValueError('core and cap models have different physical inputs: '+key)
    if (not core['complete'] or not cap['complete'] or not cap['mean_not_eliminated']
        or Fraction(core['exact_physical_cuts'][1]) != Fraction(cap['physical_radial_interval'][0])):
        raise ValueError('two-port/mean interface mismatch')
    core_arrays, cap_arrays = load_arrays(core), load_arrays(cap)
    M = core['modes']; n = 2*M+1
    block = CoreBlock(core['object_path'], M, core['primitive_nodes'], core['angular_nodes'])
    cut = Fraction(core['exact_physical_cuts'][1])
    fields = physical_coefficients(block.geometry, float(cut), core['angular_nodes'])
    Y = fields['Yz']
    pY = fields['a']*fields['Yz_r']+fields['b']*fields['Yz_theta']
    CY = block.fourier(Y)
    CS = block.fourier(Y*pY)
    mulY, shear = CY[block.lag % block.angles], CS[block.lag % block.angles]
    chart = block_diag(mulY, mulY)
    dncap = cap_arrays['augmented_DN']
    leftcap = dncap[:n, :n]
    crosscap, mean = dncap[:n, n], dncap[n, n]
    height_block = (chart.conj().T@core_arrays['core_DN']@chart
                    +block_diag(leftcap-shear, leftcap-shear))
    cross = np.zeros((2*n, 2), complex)
    cross[:n, 0], cross[n:, 1] = crosscap, crosscap
    matrix = np.block([[height_block, cross], [cross.conj().T, mean*np.eye(2)]])
    # On the left cap choose the positive height -Yz; the global physical
    # vertical translation therefore has grounded signs (-1,+1).
    translation = np.zeros(2*n+2, complex)
    translation[M], translation[n+M], translation[-2], translation[-1] = -1, 1, -1, 1
    translation /= np.linalg.norm(translation)
    bordered = np.block([[matrix, translation[:, None]],
                         [translation.conj()[None, :], np.zeros((1, 1))]])
    singular = np.linalg.svd(matrix, compute_uv=False)
    border_singular = np.linalg.svd(bordered, compute_uv=False)
    report = dict(kind='floating_physical_two_cap_core_feedback_with_two_regular_means',
        complete=True, rigorous_full_Schur_inverse=False, source_sha256=sha(__file__),
        input_sha256={str(args.core):sha(args.core), str(args.cap):sha(args.cap)},
        **{key:core[key] for key in ('object_sha256', 'origin_inputs_sha256',
              'direction_sha256', 'exact_delta_fraction', 'modes')},
        physical_core_cuts=core['exact_physical_cuts'],
        state_slots=['left positive-grounded height modes', 'right positive-grounded height modes',
                     'left regular mean xi', 'right regular mean xi'],
        left_positive_height='-Yz', right_positive_height='Yz',
        mean_flux_rows_retained=[2*n, 2*n+1],
        core_to_cap_rule='w=Y U; p_g,cap=-(Y p_core-w pY_core)',
        physical_height_min=float(np.min(Y)),
        projected_height_minimum_eigenvalue=float(np.min(np.linalg.eigvalsh(mulY))),
        height_multiplier_discarded_Fourier_l1=float(sum(abs(CY[k]) for k in range(len(CY))
            if min(k, len(CY)-k) > 2*M)),
        shear_multiplier_discarded_Fourier_l1=float(sum(abs(CS[k]) for k in range(len(CS))
            if min(k, len(CS)-k) > 2*M)),
        Hermitian_defect=float(np.linalg.norm(matrix-matrix.conj().T, 2)),
        singular_values=singular.tolist(),
        expected_vertical_translation_residual=float(np.linalg.norm(matrix@translation)),
        bordered_singular_values=border_singular.tolist(),
        floating_bordered_inverse_norm=float(1/border_singular[-1]),
        limitations=[
            'The full-frequency core/cap trace products have been projected; their high-mode feedback is not discarded in the intended proof.',
            'This finite candidate retains all two-channel and both regular mean slots, but is not the true infinite Schur complement.',
            'Core radial ODE, cap quadrature/Galerkin, exact-tail midpoint and floating arithmetic errors remain separate.',
            'A numerical bordered inverse is not a certified inverse of the actual operator.'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    arrays = args.out.with_suffix('.npz')
    np.savez_compressed(arrays, feedback=matrix, bordered=bordered, translation=translation,
        projected_height=mulY, projected_shear=shear,
        height_Fourier=CY, shear_Fourier=CS)
    report['arrays'] = dict(path=str(arrays), sha256=sha(arrays), bytes=arrays.stat().st_size)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('modes','Hermitian_defect',
        'expected_vertical_translation_residual','floating_bordered_inverse_norm',
        'height_multiplier_discarded_Fourier_l1','shear_multiplier_discarded_Fourier_l1')},indent=2),flush=True)


if __name__ == '__main__':
    main()
