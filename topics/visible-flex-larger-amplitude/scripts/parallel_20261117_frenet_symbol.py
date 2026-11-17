#!/usr/bin/env python3
"""Finite Frenet flow and its Fourier-convolution Jacobian.

The only dependencies are NumPy and SciPy (SciPy is used by the CLI probe).
This is a new implementation of the same sampled even-Fourier Frenet field,
not a claimed closed flexible surface.  The Jacobian differentiates the full
sampled finite field, without dropping frequencies or differentiating an
unrelated Gram solver.  Reproducible numerical outputs belong in scratch.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np


class Frenet:
    def __init__(self, modes: int, angles: int):
        if modes < 1 or angles % 2 or angles < 4*modes+4:
            raise ValueError("Need M>=1 and even N>=4M+4")
        self.M, self.N, self.n = modes, angles, 3*modes+2
        self.freq = 2*np.arange(modes+1)
        self.angle = 2*np.pi*np.arange(angles)/angles
        J = np.array([[0., -1., 0.], [1., 0., 0.], [0., 0., 0.]])
        self.Dp = 1j*self.freq[:, None, None]*np.eye(3)+J
        self.Dm = -1j*self.freq[:, None, None]*np.eye(3)+J
        self.D2p = self.Dp @ self.Dp
        self.D2m = self.Dm @ self.Dm
        self.plus_indices = (self.freq[:, None]-self.freq[None, :]) % angles
        self.minus_indices = (self.freq[:, None]+self.freq[None, :]) % angles

    def _jet_real(self, y):
        M, N = self.M, self.N
        y = np.asarray(y)
        spec = np.zeros((3, N//2+1), dtype=complex)
        spec[0, self.freq] = (N/2)*y[:M+1]
        spec[1, self.freq[1:]] = -1j*(N/2)*y[M+1:2*M+1]
        spec[2, self.freq] = (N/2)*y[2*M+1:]
        spec[[0, 2], 0] *= 2
        multiplier = 1j*np.arange(N//2+1)
        x = np.fft.irfft(spec, n=N, axis=-1).T
        dx = np.fft.irfft(spec*multiplier, n=N, axis=-1).T
        ddx = np.fft.irfft(spec*multiplier**2, n=N, axis=-1).T
        d = dx.copy(); d[:, 0] -= x[:, 1]; d[:, 1] += x[:, 0]
        e = ddx.copy()
        e[:, 0] -= 2*dx[:, 1]+x[:, 0]
        e[:, 1] += 2*dx[:, 0]-x[:, 1]
        return x, d, e

    def jet(self, y):
        y = np.asarray(y)
        if np.iscomplexobj(y):
            return tuple(a+1j*b for a, b in zip(self._jet_real(y.real), self._jet_real(y.imag)))
        return self._jet_real(y)

    def _project_real(self, value):
        spectrum = np.fft.rfft(value, axis=0)/self.N
        rr = 2*spectrum[self.freq, 0].real; rr[0] *= .5
        tt = -2*spectrum[self.freq[1:], 1].imag
        zz = 2*spectrum[self.freq, 2].real; zz[0] *= .5
        return np.r_[rr, tt, zz]

    def project(self, value):
        value = np.asarray(value)
        if np.iscomplexobj(value):
            return self._project_real(value.real)+1j*self._project_real(value.imag)
        return self._project_real(value)

    def local(self, y, k):
        """k=a'/a.  Q=d.d, c=d cross e, H=c.c-k^2 Q^3."""
        _, d, e = self.jet(y)
        Q = np.sum(d*d, axis=1)
        T = np.sum(d*e, axis=1)
        c = np.cross(d, e)
        W = np.sum(c*c, axis=1)
        H = W-k*k*Q**3
        if min(np.min(Q.real), np.min(W.real), np.min(H.real)) <= 0:
            raise FloatingPointError("Frenet domain Q,W,H must be positive")
        root = np.sqrt(H)
        A = Q[:, None]*e-T[:, None]*d
        V = (-k*Q[:, None]*A+root[:, None]*c)/W[:, None]
        return dict(d=d, e=e, Q=Q, T=T, c=c, W=W, H=H, root=root, A=A, V=V, k=k)

    @staticmethod
    def variation(z, u, v, dk=0.):
        d, e, Q, T = (z[key] for key in ('d', 'e', 'Q', 'T'))
        c, W, root, A, V, k = (z[key] for key in ('c', 'W', 'root', 'A', 'V', 'k'))
        dQ = 2*np.sum(d*u, axis=1)
        dT = np.sum(u*e+d*v, axis=1)
        dc = np.cross(u, e)+np.cross(d, v)
        dW = 2*np.sum(c*dc, axis=1)
        dA = dQ[:, None]*e+Q[:, None]*v-dT[:, None]*d-T[:, None]*u
        dH = dW-2*k*dk*Q**3-3*k*k*Q*Q*dQ
        return ((-dk*Q-k*dQ)[:, None]*A-k*Q[:, None]*dA
                +(dH/(2*root))[:, None]*c+root[:, None]*dc
                -V*dW[:, None])/W[:, None]

    def rhs(self, y, k):
        return self.project(self.local(y, k)['V'])

    def jvp(self, y, k, direction, dk=0.):
        z = self.local(y, k)
        _, u, v = self.jet(direction)
        return self.project(self.variation(z, u, v, dk))

    def jacobian(self, y, k):
        """All (3M+2)^2 entries via six local derivatives and convolution.

        Fourier differences use modular DFT indices.  Consequently this is
        the derivative of this exact sampled projection, with its existing
        aliasing, rather than a different dealiased or infinite-mode model.
        """
        z = self.local(y, k)
        zero = np.zeros((self.N, 3))
        Ad = np.empty((self.N, 3, 3)); Ae = np.empty_like(Ad)
        for j in range(3):
            basis = zero.copy(); basis[:, j] = 1
            Ad[:, :, j] = self.variation(z, basis, zero)
            Ae[:, :, j] = self.variation(z, zero, basis)
        Ah = np.fft.fft(Ad, axis=0)/self.N
        Bh = np.fft.fft(Ae, axis=0)/self.N
        Kp = Ah[self.plus_indices] @ self.Dp[None, :, :, :] + Bh[self.plus_indices] @ self.D2p[None, :, :, :]
        Km = Ah[self.minus_indices] @ self.Dm[None, :, :, :] + Bh[self.minus_indices] @ self.D2m[None, :, :, :]
        C = (Kp+Km)/2
        S = (-1j*Kp+1j*Km)/2
        factor = np.full(self.M+1, 2.); factor[0] = 1.
        blocks = []
        for input_component, kernel, start in ((0, C, 0), (1, S, 1), (2, C, 0)):
            block = np.vstack((factor[:, None]*kernel[:, start:, 0, input_component].real,
                               -2*kernel[1:, start:, 1, input_component].imag,
                               factor[:, None]*kernel[:, start:, 2, input_component].real))
            blocks.append(block)
        return np.hstack(blocks)

    def core(self, coefficients):
        coefficients = np.asarray(coefficients)
        if len(coefficients) > self.M:
            raise ValueError("Core has more modes than the field")
        y = np.zeros(self.n); y[0] = 1
        y[1:len(coefficients)+1] = coefficients
        y[self.M+1:self.M+1+len(coefficients)] = -self.freq[1:len(coefficients)+1]*coefficients
        return y


def probe(args):
    from scipy.integrate import solve_ivp
    q = Frenet(args.M, args.N)
    y0 = q.core([args.amplitude, -args.amplitude/(10*np.sqrt(2))])
    S, v, k0 = .65, .25, .45
    def profile(s):
        u = s/S; b = k0*S; c = 3*v-2*b; d = b-2*v
        a = 1+S*(b*u*u/2+c*u**3/3+d*u**4/4)
        ap = b*u+c*u*u+d*u**3
        return a, ap
    begin = time.perf_counter()
    sol = solve_ivp(lambda s, y:q.rhs(y, profile(s)[1]/profile(s)[0]), (0., args.end), y0,
                    method='DOP853', rtol=1e-10, atol=1e-12, max_step=.002, dense_output=True)
    rows = []
    rng = np.random.default_rng(17)
    for s in (0., args.end/2, args.end):
        y = sol.sol(s); a, ap = profile(s); k = ap/a
        start = time.perf_counter(); J = q.jacobian(y, k); analytic_seconds = time.perf_counter()-start
        start = time.perf_counter(); JC = np.empty_like(J); h = 1e-25
        for j in range(q.n):
            yy = y.astype(complex); yy[j] += 1j*h
            JC[:, j] = q.rhs(yy, k).imag/h
        complex_seconds = time.perf_counter()-start
        direction = rng.standard_normal(q.n)/(1+np.arange(q.n))
        A = q.jvp(y, k, direction)
        rows.append(dict(s=s, jac_max_abs=float(np.max(abs(J-JC))),
                         jac_relative_frobenius=float(np.linalg.norm(J-JC)/np.linalg.norm(JC)),
                         jvp_max_abs=float(np.max(abs(A-J@direction))),
                         analytic_seconds=analytic_seconds, complex_step_seconds=complex_seconds,
                         speedup=complex_seconds/analytic_seconds))
    report = dict(scope='Finite open-prefix operator implementation experiment; no closed or reach claim.',
                  M=args.M, N=args.N, amplitude=args.amplitude, end=args.end,
                  success=sol.success, message=sol.message, calls=sol.nfev,
                  seconds=time.perf_counter()-begin, rows=rows,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if args.out:
        args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--M', type=int, default=48)
    parser.add_argument('--N', type=int, default=512)
    parser.add_argument('--amplitude', type=float, default=.38)
    parser.add_argument('--end', type=float, default=.65)
    parser.add_argument('--out', type=Path)
    probe(parser.parse_args())
