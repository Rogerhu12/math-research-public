#!/usr/bin/env python3
"""Long-precision FFT synthesis/projection of the complete cylindrical basis.

Only recognized B/B1/B2 tables are accelerated. The original binary er/et
rotation and original sum(B*B) denominators are retained. Real and imaginary
inputs are transformed separately to avoid complex-step roundoff crosstalk.
This reorders floating operations; it is not a byte-identical transform.
"""
import types
import numpy as np
from scipy import fft


def _real_dtype(dtype):
    real = np.empty((), dtype=dtype).real.dtype
    return np.dtype(np.longdouble if real.itemsize > 8 else np.float64)


def _synthesize_real(C, family, order):
    M, N, k = family['M'], family['N'], family['k']
    dtype = _real_dtype(C.dtype)
    C = np.asarray(C, dtype=dtype)
    complex_dtype = np.clongdouble if dtype.itemsize > 8 else np.complex128
    spectral = np.zeros((C.shape[1], 3, N//2+1), dtype=complex_dtype)
    r, t, z = C[1:M+1].T, C[M+1:2*M+1].T, C[2*M+1:].T
    if order == 0:
        spectral[:,0,0] = C[0]
        spectral[:,0,k] = r/2
        spectral[:,1,k] = -1j*t/2
        spectral[:,2,k] = z/2
    elif order == 1:
        spectral[:,0,k] = 1j*(k*r+t)/2
        spectral[:,1,0] = C[0]
        spectral[:,1,k] = (r+k*t)/2
        spectral[:,2,k] = 1j*k*z/2
    else:
        spectral[:,0,0] = -C[0]
        spectral[:,0,k] = -((k*k+1)*r+2*k*t)/2
        spectral[:,1,k] = 1j*(2*k*r+(k*k+1)*t)/2
        spectral[:,2,k] = -k*k*z/2
    # norm='forward' leaves the inverse unscaled, so these are Fourier
    # coefficients rather than NumPy's N-times-coefficient convention.
    local = fft.irfft(spectral, n=N, axis=2, norm='forward', workers=1)
    co, si = family['cos'], family['sin']
    result = np.empty((C.shape[1], N, 3), dtype=dtype)
    result[:,:,0] = local[:,0]*co-local[:,1]*si
    result[:,:,1] = local[:,0]*si+local[:,1]*co
    result[:,:,2] = local[:,2]
    return result


def _project_real(F, family, order):
    M, N, k = family['M'], family['N'], family['k']
    dtype = _real_dtype(F.dtype)
    F = np.asarray(F, dtype=dtype)
    local = np.empty((F.shape[0], 3, N), dtype=dtype)
    co, si = family['cos'], family['sin']
    local[:,0] = F[:,:,0]*co+F[:,:,1]*si
    local[:,1] = -F[:,:,0]*si+F[:,:,1]*co
    local[:,2] = F[:,:,2]
    transformed = fft.rfft(local, axis=2, norm='backward', workers=1)
    r, t, z = transformed[:,0,k], transformed[:,1,k], transformed[:,2,k]
    result = np.empty((3*M+1, F.shape[0]), dtype=dtype)
    if order == 0:
        result[0] = transformed[:,0,0].real
        result[1:M+1] = r.real.T
        result[M+1:2*M+1] = -t.imag.T
        result[2*M+1:] = z.real.T
    elif order == 1:
        result[0] = transformed[:,1,0].real
        result[1:M+1] = (k*r.imag+t.real).T
        result[M+1:2*M+1] = (r.imag+k*t.real).T
        result[2*M+1:] = (k*z.imag).T
    else:
        result[0] = -transformed[:,0,0].real
        result[1:M+1] = (-(k*k+1)*r.real+2*k*t.imag).T
        result[M+1:2*M+1] = (-2*k*r.real+(k*k+1)*t.imag).T
        result[2*M+1:] = (-k*k*z.real).T
    return result/family['norms'][order][:,None]


def _separate_complex(operation, values, family, order):
    values = np.asarray(values)
    if not np.iscomplexobj(values):
        return operation(values, family, order)
    real = operation(values.real, family, order)
    imaginary = operation(values.imag, family, order)
    result = np.empty(real.shape, dtype=np.clongdouble if real.dtype.itemsize > 8 else np.complex128)
    result.real = real
    result.imag = imaginary
    return result


def attach(flow):
    """Attach to one new flow; retain exact original fallbacks for other bases."""
    if getattr(flow, '_long_fourier_attached', False):
        return flow._long_fourier_stats
    old_basis, old_values, old_project = flow.basis, flow.values, flow.project
    families = {}
    stats = {'values_calls':0, 'project_calls':0, 'fallback_values':0,
             'fallback_project':0, 'registered_angular_counts':[]}
    def register(tables):
        B, B1, B2 = tables
        M, N = flow.M, B.shape[1]
        k = np.asarray(flow.even)
        if (B.shape != (3*M+1,N,3) or len(k) != M
            or not np.all(k == k.astype(int)) or np.min(k) < 2
            or 2*(np.max(k)+1) >= N):
            return tables
        # At most one currently known family per N. A displaced table remains
        # valid and simply uses the original fallback if passed again later.
        families[N] = {'M':M, 'N':N, 'k':k.astype(int), 'tables':tables,
                       'cos':B[0,:,0].copy(), 'sin':B[0,:,1].copy(),
                       'norms':[np.sum(v*v,axis=(1,2)) for v in tables]}
        stats['registered_angular_counts'] = sorted(families)
        return tables
    def lookup(B):
        family = families.get(B.shape[1]) if getattr(B, 'ndim', None) == 3 else None
        if family is not None:
            for order, table in enumerate(family['tables']):
                if B is table:
                    return family, order
        return None, None
    def basis(self, N):
        return register(old_basis(N))
    def values(self, C, B):
        family, order = lookup(B)
        if family is None or np.asarray(C).shape[0] != 3*flow.M+1:
            stats['fallback_values'] += 1
            return old_values(C, B)
        stats['values_calls'] += 1
        return _separate_complex(_synthesize_real, C, family, order)
    def project(self, F, B):
        family, order = lookup(B)
        if family is None:
            stats['fallback_project'] += 1
            return old_project(F, B)
        stats['project_calls'] += 1
        return _separate_complex(_project_real, F, family, order)
    register((flow.B, flow.B1, flow.B2))
    flow.basis = types.MethodType(basis, flow)
    flow.values = types.MethodType(values, flow)
    flow.project = types.MethodType(project, flow)
    flow._long_fourier_attached = True
    flow._long_fourier_stats = stats
    return stats


def install(adaptive):
    """Select only subsequent new flows; current running solvers are untouched."""
    original = adaptive.build_classes
    def selected(chart):
        Flow, BVP = original(chart)
        original_init = Flow.__init__
        def initialize(self, *values, **kwargs):
            original_init(self, *values, **kwargs)
            attach(self)
        Flow.__init__ = initialize
        return Flow, BVP
    adaptive.build_classes = selected
    return original
