"""R134 pointwise Gauss/cap initializer, reconstructed after executor loss.

This is a NEW source identity.  It is not the old b15ec... implementation.
Floating point output is a finite screen, not an interval certificate.
"""
from __future__ import annotations
import numpy as np


def shape_curvature(n, m, l):
    n, m, l = np.broadcast_arrays(np.asarray(n, float), np.asarray(m, float), np.asarray(l, float))
    half = 0.5 * (n + l)
    rad = np.hypot(0.5 * (n - l), m)
    return np.maximum(np.abs(half - rad), np.abs(half + rad))


def _prepare(n, m, l, K, cap, preserve):
    vals = np.broadcast_arrays(*[np.asarray(q, float) for q in (n, m, l, K)])
    n0, m0, l0, K = [q.copy() for q in vals]
    C = float(cap)
    if not np.isfinite(C) or C <= 0:
        raise ValueError("cap must be finite and positive")
    if any(not np.all(np.isfinite(q)) for q in vals):
        raise ValueError("all fields must be finite")
    mask = np.zeros(n0.shape, bool) if preserve is None else np.broadcast_to(np.asarray(preserve, bool), n0.shape).copy()
    active = ~mask
    if np.any(np.abs(K[active]) > C*C):
        raise ValueError("|K| > cap^2 at an active point: no feasible symmetric matrix")
    return n0, m0, l0, K, C, mask, active


def _bounds(m0, K, C):
    mcap = (C - K/C) / 2
    m = np.clip(m0, -mcap, mcap)
    T = C + K/C
    d = C - K/C
    delta = np.sqrt(np.maximum((d-2*np.abs(m))*(d+2*np.abs(m)), 0.0))
    high = (T + delta) / 2
    A = K + m*m
    low = np.divide(np.abs(A), high, out=np.zeros_like(A), where=high > 0)
    # The exact interval has low<=high.  Remove only rounded endpoint inversion.
    low = np.minimum(low, high)
    return m, A, T, low, high


def _max(q):
    return float(np.max(q)) if np.size(q) else 0.0


def _finish(n, m, l, n0, m0, l0, K, C, mask, active, method):
    gauss = l*n-m*m-K
    curvature = shape_curvature(n, m, l)
    change = (n-n0)**2 + (l-l0)**2 + 2*(m-m0)**2
    diag = dict(
        method=method, cap=C, active_count=int(np.sum(active)),
        preserved_count=int(np.sum(mask)),
        preserved_bitwise=bool(np.array_equal(n[mask], n0[mask]) and np.array_equal(m[mask], m0[mask]) and np.array_equal(l[mask], l0[mask])),
        active_max_gauss_defect=_max(np.abs(gauss[active])),
        all_max_gauss_defect=_max(np.abs(gauss)),
        active_max_curvature=_max(curvature[active]),
        all_max_curvature=_max(curvature),
        changed_m=int(np.sum(m[active] != m0[active])),
        changed_n=int(np.sum(n[active] != n0[active])),
        frobenius_change_squared=float(np.sum(change)),
        max_field_change=dict(n=_max(np.abs(n-n0)),m=_max(np.abs(m-m0)),l=_max(np.abs(l-l0))),
        scope="Pointwise floating initializer; no Codazzi, smoothness, finite-basis or continuous certificate.")
    return dict(n=n, m=m, l=l, preserve=mask, diagnostics=diag)


def project_gauss_curvature_cap(n, m, l, K, cap=7.0, preserve=None):
    n0,m0,l0,K,C,mask,active = _prepare(n,m,l,K,cap,preserve)
    nn,mm,ll = n0.copy(),m0.copy(),l0.copy()
    ma,A,T,low,high = _bounds(m0[active],K[active],C)
    na = np.clip(n0[active],low,high)
    # This deliberately reproduces the simple selector's arbitrary open-branch
    # choice.  Use fixed-m nearest recovery for the closed n>=0 branch instead.
    na = np.where((na <= 0) & (high > 0), high/2, na)
    la = np.divide(A,na,out=np.zeros_like(A),where=na > 0)
    nn[active],mm[active],ll[active] = na,ma,la
    return _finish(nn,mm,ll,n0,m0,l0,K,C,mask,active,"simple positive-n selector; explicit zero corner")
