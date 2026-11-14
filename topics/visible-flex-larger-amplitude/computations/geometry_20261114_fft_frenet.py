#!/usr/bin/env python3
"""FFT evaluation of the same uniform-angle finite Frenet Fourier equations.

No coefficient is removed, damped, or changed. This replaces dense trigonometric
matrix products by mathematically identical DFT synthesis/projection. Real and
imaginary inputs are transformed separately so complex-step derivatives retain
their tiny imaginary part without an FFT roundoff imaginary background.
"""
import types
import numpy as np


def real_jet(q, y):
    r, t, z = q.unpack(y)
    c = np.zeros((3, q.N//2+1), dtype=complex)
    n = q.freq.astype(int)
    c[0, n] = (q.N/2)*r
    c[0, 0] *= 2
    c[1, n[1:]] = -1j*(q.N/2)*t
    c[2, n] = (q.N/2)*z
    c[2, 0] *= 2
    multiplier = 1j*np.arange(q.N//2+1)
    value = np.fft.irfft(c, n=q.N, axis=1).T
    derivative = np.fft.irfft(c*multiplier, n=q.N, axis=1).T
    second = np.fft.irfft(c*multiplier*multiplier, n=q.N, axis=1).T
    d = np.stack((derivative[:, 0]-value[:, 1],
                  derivative[:, 1]+value[:, 0], derivative[:, 2]), axis=1)
    dd = np.stack((second[:, 0]-2*derivative[:, 1]-value[:, 0],
                   second[:, 1]+2*derivative[:, 0]-value[:, 1], second[:, 2]), axis=1)
    return value, d, dd


def fft_jet(q, y):
    y = np.asarray(y)
    if np.iscomplexobj(y):
        real = real_jet(q, y.real)
        imag = real_jet(q, y.imag)
        return tuple(r+1j*i for r, i in zip(real, imag))
    return real_jet(q, y)


def real_project(q, value):
    c = np.fft.rfft(value.T, n=q.N, axis=1)
    n = q.freq.astype(int)
    r = (2/q.N)*c[0, n].real
    r[0] *= .5
    t = -(2/q.N)*c[1, n[1:]].imag
    z = (2/q.N)*c[2, n].real
    z[0] *= .5
    return np.r_[r, t, z]


def fft_project(q, value):
    value = np.asarray(value)
    if np.iscomplexobj(value):
        return real_project(q, value.real)+1j*real_project(q, value.imag)
    return real_project(q, value)


def enable_fft(q):
    if q.N < 4*q.M+4 or q.N % 2:
        raise ValueError('FFT adapter needs the original uniform even grid and all retained frequencies below Nyquist')
    q.jet = types.MethodType(fft_jet, q)
    q.project = types.MethodType(fft_project, q)
    return q
