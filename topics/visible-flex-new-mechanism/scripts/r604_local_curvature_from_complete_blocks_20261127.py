#!/usr/bin/env python3
"""Pure R604 curvature assembly on the SAME complete radial/angular cell.

No new input, reconstruction, optimization, interval traversal or execution
scope is created here. A caller must have paid complete same-field boxes.
Only a later declared public Actions scope may consume this interface.
"""
import hashlib
from pathlib import Path

FRAME_FILE = 'r604_rotating_frame_continuous_norms_20261127.py'
FRAME_SHA = '2fa3a89f2bc2bc0e739ae69f391b06f3b44cb3033d236df632205a3c357516e0'
if hashlib.sha256(Path(__file__).with_name(FRAME_FILE).read_bytes()).hexdigest() != FRAME_SHA:
    raise RuntimeError('the complete same-field covariant blocks changed')

from r604_rotating_frame_continuous_norms_20261127 import I, sqrt_i, absolute


def local_curvature_bound(reference, complete_cell_norms):
    """Bound actual principal curvatures from already formed complete boxes.

    ``reference`` and ``complete_cell_norms`` must describe one identical
    radial cell and every angle of it. The latter is the unmodified output
    of radial_block_bounds, not a finite sample or a requested budget.
    Reference order is (unit meridian, unit angular direction). The caller
    retains coverage of all cells, the cylinder, both complete caps and
    all junctions; no local output grants a global or all-time certificate.
    """
    a, ar, arr, zr, zrr = [reference[k] for k in ('a', 'a_s', 'a_ss', 'z_s', 'z_ss')]
    if not all(isinstance(x, I) for x in (a, ar, arr, zr, zrr)):
        raise TypeError('same-reference complete interval jets required')
    speed2 = ar**2+zr**2
    if a.lo <= 0 or speed2.lo <= 0:
        raise ArithmeticError('positive radius and regular meridian required')
    alpha = I(complete_cell_norms['C1_difference_upper'])
    blocks = complete_cell_norms['normalized_covariant_blocks_upper']
    if len(blocks) != 3:
        raise ValueError('complete independent H11/H12/H22 output required')
    h11, h12, h22 = [I(value) for value in blocks]
    if not (0 <= alpha.lo <= alpha.hi < 1 and all(x.lo >= 0 for x in (h11, h12, h22))):
        raise ArithmeticError('local immersion or nonnegative block bounds unresolved')
    speed = sqrt_i(speed2)
    km = absolute(ar*zrr-zr*arr)/(speed2*speed)
    ko = absolute(zr)/(a*speed)
    diagonal1, diagonal2 = km+h11, ko+h22
    numerator = (diagonal1+diagonal2+sqrt_i(
        (diagonal1-diagonal2)**2+4*h12**2))/2
    curvature = numerator/(1-alpha)**2
    return {
        'same_cell_actual_principal_curvature_upper': curvature.hi,
        'same_cell_reference_meridian_curvature_upper': km.hi,
        'same_cell_reference_orbit_curvature_upper': ko.hi,
        'same_cell_second_form_matrix_eigenvalue_upper': numerator.hi,
        'same_cell_C1_upper': alpha.hi,
        'same_cell_covariant_blocks_upper': list(blocks),
        'all_angles_and_identical_material_cell_required': True,
        'original_block_norms_not_recomputed': True,
        'complete_closed_surface_or_README_claim': False,
    }
