"""Bound temporary frame storage for pointwise radial flow evaluations.

Each radial point uses the unchanged angular quadrature and physical flow.
Only independent radial evaluations are split; no physical mesh or tolerance
is changed. The final state Jacobian is still fully assembled for solve_bvp.
"""
from __future__ import annotations
import numpy as np


def value(flow, s, y, p, batch_size=48):
    if len(s) <= batch_size:
        return flow.fun(s, y, p)
    output = None
    for first in range(0, len(s), batch_size):
        sl = slice(first, first + batch_size)
        block = flow.fun(s[sl], y[:, sl], p)
        if output is None:
            output = np.empty((block.shape[0], len(s)), dtype=block.dtype)
        output[:, sl] = block
    return output


def state_jacobian(flow, s, y, p, batch_size=48):
    if len(s) <= batch_size:
        return flow.fun_jac(s, y, p)[0]
    output = None
    for first in range(0, len(s), batch_size):
        sl = slice(first, first + batch_size)
        block = flow.fun_jac(s[sl], y[:, sl], p)[0]
        if output is None:
            output = np.empty((*block.shape[:2], len(s)), dtype=block.dtype)
        output[:, :, sl] = block
    return output
