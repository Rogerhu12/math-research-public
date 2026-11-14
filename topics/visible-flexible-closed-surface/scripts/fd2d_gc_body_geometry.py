#!/usr/bin/env python3
"""R122 body-frame evaluation of the actual R119 position map.

These vector operations are numerical evaluations, not interval certificates.
For a continuous certificate, bound the returned residual and initial errors
on complete cells as in R122. All arrays use their final axis for dimension 3.
"""
from __future__ import annotations
import numpy as np


def negative_connection(l, m, q):
    """Return -A q for exactly the R119 radial connection convention."""
    q = np.asarray(q)
    if q.shape[-1] != 3:
        raise ValueError('The final body-coordinate dimension must be three')
    l, m = np.asarray(l), np.asarray(m)
    return np.stack((l*q[..., 2], m*q[..., 2],
                     -l*q[..., 0]-m*q[..., 1]), axis=-1)


def body_rhs(l, m, q, *,fixed_point=True):
    """q=F.T@(X-p) if fixed_point, or h=F.T@v otherwise."""
    out = negative_connection(l, m, q)
    if fixed_point:
        out[..., 0] += 1
    return out


def body_residual(l, m, q, q_s, *,fixed_point=True):
    """Use the derivative of the actual saved interpolant, not a new RHS."""
    return np.asarray(q_s)-body_rhs(l, m, q, fixed_point=fixed_point)


def initial_body(frame, position, point=(0., 0., 0.)):
    """frame columns are the actual initial e1,e2,N, with N inward above."""
    frame, position, point = map(np.asarray, (frame, position, point))
    if frame.shape[-2:] != (3, 3):
        raise ValueError('Initial frame must have three orthonormal columns')
    return np.einsum('...ji,...j->...i', frame, position-point)


def initial_direction(frame, vector):
    return np.einsum('...ji,...j->...i', np.asarray(frame), np.asarray(vector))


def numerical_readout(q0, *,q_witness=None, h_y=None, h_z=None):
    """Diagnostics of an evaluated body state; no support correction hidden."""
    q0 = np.asarray(q0)
    out = dict(radius=np.linalg.norm(q0, axis=-1),
               auxiliary_outward_support=-q0[..., 2])
    if q_witness is not None:
        out['witness_distance'] = np.linalg.norm(q_witness, axis=-1)
    for name, value in (('y', h_y), ('z', h_z)):
        if value is not None:
            out[name] = np.einsum('...i,...i->...', q0, value)
    return out
