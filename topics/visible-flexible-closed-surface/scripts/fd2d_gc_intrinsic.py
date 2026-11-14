#!/usr/bin/env python3
"""Small intrinsic Gauss--Codazzi state and exact finite-system JVP.

The fixed metric is ds^2 + a(s)^2 du^2.  Every candidate and central seed
uses ONE reference angle theta and a fixed map u(theta).  The independent
state contains only n and m; position and the orthonormal frame are not
unknowns of this nonlinear system.  Actual position derivatives still have
to be checked after frame reconstruction.  No BVP or closed surface is
asserted by this numerical provider.

State convention (real amplitudes, not complex FFT coefficients):
  [n_0, n_2, ..., n_(2K), m_2, ..., m_(2K)],
where n uses cos(k theta) and m uses sin(k theta).  The central free
curvature modes and the tail height modes instead use MATERIAL u.
"""
from __future__ import annotations
import os
for _variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_variable] = '1'
from dataclasses import dataclass
import hashlib
from pathlib import Path
import time
import numpy as np
from scipy import fft
from scipy.integrate import solve_ivp

LD = np.longdouble
PI = np.arccos(LD(-1))


def identity(path):
    path = Path(path)
    return dict(path=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


@dataclass
class StageResult:
    left: float
    right: float
    state: np.ndarray
    tangent: np.ndarray | None
    rhs_calls: int
    seconds: float
    segments: list


class FixedNormalReference:
    """The normal angle of ONE fixed convex seed, never the changing curve.

    The supplied seed's arc(phi), reference_radius(phi) and derivative are
    used.  For the balanced oval this makes u_phi=rho_seed/a0 and preserves
    the same physical material u as the original ellipse coordinate.
    """
    def __init__(self, seed):
        self.seed = seed
        self.a0 = LD(seed.a0)

    def reference_coordinate(self, phi):
        return dict(u=np.asarray(self.seed.arc(phi), dtype=LD)/self.a0,
                    u_theta=np.asarray(self.seed.reference_radius(phi), dtype=LD)/self.a0,
                    u_theta_theta=np.asarray(self.seed.reference_radius_derivative(phi), dtype=LD)/self.a0)

    def coordinate_speed(self, phi):
        return np.asarray(self.seed.reference_radius(phi), dtype=LD)/self.a0


class IntrinsicGC:
    """Finite even/odd theta Fourier Codazzi equations on a supplied g."""
    def __init__(self, candidate, maximum_mode=95, oversample=2, *, reference=None):
        if maximum_mode < 2 or oversample < 2:
            raise ValueError('At least mode 2 and twofold angular oversampling are required')
        self.candidate = candidate
        self.maximum_mode = int(maximum_mode)
        self.K = self.maximum_mode//2
        self.dimension = 2*self.K+1
        self.work = 2*int(oversample)*(self.maximum_mode+1)
        self.theta = np.arange(self.work, dtype=LD)*(2*PI/self.work)
        self.frequencies = 2*np.arange(1, self.K+1)
        self.n_frequencies = np.concatenate(([0], self.frequencies))
        self.wave = np.fft.fftfreq(self.work, 1/self.work).astype(LD)
        self.wave_rfft = np.arange(self.work//2+1, dtype=LD)
        if reference is None:
            # The longdouble common-coordinate provider is independent of
            # the current support/curvature seed and every free coefficient.
            from fd2d_metric_curvature_core import SupportSeed
            reference = SupportSeed()
        self.reference = reference
        coord = reference.reference_coordinate(self.theta)
        if not isinstance(coord, dict):
            u, u_theta, u_theta_theta = coord
            coord = dict(u=u, u_theta=u_theta, u_theta_theta=u_theta_theta)
        self.u = np.asarray(coord['u'], dtype=LD)
        self.u_theta = np.asarray(coord['u_theta'], dtype=LD)
        self.u_theta_theta = np.asarray(coord['u_theta_theta'], dtype=LD)
        self.a0 = LD(reference.a0)
        self.calls = 0
        self.jvp_calls = 0

    def decode(self, state):
        state = np.asarray(state, dtype=LD)
        if state.shape[0] != self.dimension:
            raise ValueError('Intrinsic state has an incorrect first dimension')
        raw = np.zeros((self.work//2+1, 2)+state.shape[1:], dtype=np.clongdouble)
        raw[0, 0] = state[0]
        raw[self.frequencies, 0] = state[1:self.K+1]/2
        raw[self.frequencies, 1] = -1j*state[self.K+1:]/2
        return fft.irfft(raw, n=self.work, axis=0, norm='forward')

    def encode(self, values, *, dtype=float):
        values = np.asarray(values, dtype=LD)
        if values.shape[:2] != (self.work, 2):
            raise ValueError('Expected values with shape (angular, 2, ...)')
        raw = fft.rfft(values, axis=0, norm='forward')
        result = np.concatenate((raw[[0], 0].real,
                                 2*raw[self.frequencies, 0].real,
                                 -2*raw[self.frequencies, 1].imag), axis=0)
        return np.asarray(result, dtype=dtype)

    def derivative(self, values, order=1):
        values = np.asarray(values, dtype=LD)
        shape = (-1,)+(1,)*(values.ndim-1)
        raw = fft.rfft(values, axis=0, norm='forward')
        raw *= (1j*self.wave_rfft.reshape(shape))**order
        # The real Nyquist derivative is not represented by an odd sine.
        if order % 2:
            raw[-1] = 0
        return fft.irfft(raw, n=self.work, axis=0, norm='forward')

    def profile(self, s):
        args = np.atleast_1d(np.asarray(s, dtype=float))
        aa, ap, app = (np.asarray(x, dtype=LD) for x in self.candidate.profile(args))
        if np.any(aa <= 0):
            raise ArithmeticError('Metric radius must be positive in the n chart')
        return aa, ap, app

    def fields(self, s, state):
        state = np.asarray(state)
        single = state.ndim == 1
        if single:
            state = state[:, None]
        if state.ndim != 2:
            raise ValueError('Expected one state or a radial array of states')
        values = self.decode(state)
        n, m = values[:, 0], values[:, 1]
        if np.any(n <= 0) or not np.all(np.isfinite(n)):
            raise ArithmeticError('The positive n chart has failed')
        aa, ap, app = self.profile(s)
        if len(aa) not in (1, state.shape[1]):
            raise ValueError('Radial coordinates and states disagree')
        c, K = ap/aa, -app/aa
        inverse_b = 1/(self.u_theta[:, None]*aa[None, :])
        l = (m*m+K[None, :])/n
        return dict(n=n, m=m, l=l, a=aa, ap=ap, app=app, c=c, K=K,
                    inverse_b=inverse_b, single=single)

    def rhs(self, s, state):
        f = self.fields(s, state)
        lm = np.stack((f['l'], f['m']), axis=1)
        deriv = self.derivative(lm)
        velocity = np.stack((deriv[:, 1]*f['inverse_b']+f['c']*(f['l']-f['n']),
                             deriv[:, 0]*f['inverse_b']-2*f['c']*f['m']), axis=1)
        self.calls += 1
        answer = self.encode(velocity)
        return answer[:, 0] if f['single'] else answer

    def jvp(self, s, state, direction):
        """Analytic JVP of the actual projected finite equations.

        A single base state accepts a vector or a matrix of independent
        directions.  The fixed metric and fixed u(theta) are not varied.
        """
        state = np.asarray(state)
        direction = np.asarray(direction)
        if state.ndim != 1:
            raise ValueError('JVP currently accepts one radial base state')
        one_direction = direction.ndim == 1
        if one_direction:
            direction = direction[:, None]
        f = self.fields(s, state)
        dn_dm = self.decode(direction)
        dn, dm = dn_dm[:, 0], dn_dm[:, 1]
        dl = (2*f['m']*dm-f['l']*dn)/f['n']
        deriv = self.derivative(np.stack((dl, dm), axis=1))
        velocity = np.stack((deriv[:, 1]*f['inverse_b']+f['c']*(dl-dn),
                             deriv[:, 0]*f['inverse_b']-2*f['c']*dm), axis=1)
        self.jvp_calls += 1
        answer = self.encode(velocity)
        return answer[:, 0] if one_direction else answer

    def jacobian(self, s, state):
        state = np.asarray(state)
        if state.ndim == 1:
            return self.jvp(s, state, np.eye(self.dimension))
        coordinates = np.broadcast_to(np.asarray(s), (state.shape[1],))
        return np.stack([self.jvp(float(x), y, np.eye(self.dimension))
                         for x, y in zip(coordinates, state.T)], axis=-1)

    def central_state(self, core):
        """Project an actual central provider, retaining all discarded error."""
        if isinstance(self.reference, FixedNormalReference) and self.reference.seed is core:
            n = 1/np.asarray(core.reference_radius(self.theta), dtype=LD)
            nm = np.column_stack((n, np.zeros_like(n)))
        elif hasattr(core, 'gauss_codazzi_initial'):
            value = core.gauss_codazzi_initial(self.u, reference_angle=False)
            nm = np.column_stack((value['n'], value['m']))
        else:
            value = core.evaluate(self.u)
            nm = np.asarray(value['gc_values'])[:, :2]
        state = self.encode(nm)
        difference = self.decode(state)-nm
        return state, dict(maximum_n_projection_difference=float(abs(difference[:, 0]).max()),
                           maximum_m_projection_difference=float(abs(difference[:, 1]).max()),
                           material_total_turn_projection_difference=float(
                               2*PI*np.mean(self.u_theta*difference[:, 0])*self.a0))

    def central_material_directions(self, count=None):
        """cos(2 j u(theta)), NOT cos(2 j theta)."""
        count = self.K if count is None else int(count)
        frequencies = 2*np.arange(1, count+1)
        values = np.zeros((self.work, 2, count), dtype=LD)
        values[:, 0] = np.cos(self.u[:, None]*frequencies[None, :])
        return self.encode(values)

    def central_reference_directions(self, count=None):
        """Reference-angle curvature modes with MATERIAL weighted mean zero.

        psi_j(theta)=cos(2j theta)-mean(u_theta*cos(2j theta))/mean(u_theta).
        This is a different but still fixed-material curvature basis.  The
        numerical weights are not interval enclosures; full curve closure
        and projection error must still be checked in the final candidate.
        """
        count = self.K if count is None else int(count)
        frequencies = 2*np.arange(1, count+1)
        basis = np.cos(self.theta[:, None]*frequencies[None, :])
        means = np.mean(self.u_theta[:, None]*basis, axis=0)/np.mean(self.u_theta)
        values = np.zeros((self.work, 2, count), dtype=LD)
        values[:, 0] = basis-means
        return self.encode(values), np.asarray(means, dtype=float)

    def at_angle(self, state, theta):
        state = np.asarray(state, dtype=LD)
        theta = np.asarray(theta, dtype=LD)
        if state.ndim != 1:
            raise ValueError('Expected a single radial state')
        n = state[0]+np.cos(theta[..., None]*self.frequencies)@state[1:self.K+1]
        m = np.sin(theta[..., None]*self.frequencies)@state[self.K+1:]
        return np.stack((n, m), axis=-1)

    def integrate_stage(self, left, right, state, *, tangent=None, rtol=2e-11,
                        atol=2e-14, max_step=.001):
        """One real intrinsic stage, optionally with its analytic tangent.

        Split at the supplied profile breakpoints.  Returned tangent is the
        derivative of this actual finite ODE flow, not a tail DN derivative.
        """
        if right < left:
            raise ValueError('Use increasing radial arclength for this stage')
        state = np.asarray(state, dtype=float).copy()
        if tangent is not None:
            tangent = np.asarray(tangent, dtype=float)
            if tangent.ndim == 1:
                tangent = tangent[:, None]
            if tangent.shape[0] != self.dimension:
                raise ValueError('Wrong tangent dimension')
        columns = 0 if tangent is None else tangent.shape[1]
        combined = state if columns == 0 else np.concatenate((state, tangent.ravel()))
        breaks = [left]+[float(x) for x in self.candidate.breaks if left < x < right]+[right]
        begin, calls = time.monotonic(), self.calls
        records = []
        def augmented(s, y):
            initial = y[:self.dimension]
            base = self.rhs(s, initial)
            if columns == 0:
                return base
            variation = y[self.dimension:].reshape(self.dimension, columns)
            return np.concatenate((base, self.jvp(s, initial, variation).ravel()))
        for lo, hi in zip(breaks[:-1], breaks[1:]):
            if hi == lo:
                continue
            sol = solve_ivp(augmented, (lo, hi), combined, method='DOP853',
                            rtol=rtol, atol=atol, max_step=max_step)
            records.append(dict(left=lo, right=float(sol.t[-1]), success=bool(sol.success),
                                rhs_calls=int(sol.nfev), message=sol.message))
            combined = sol.y[:, -1]
            if not sol.success:
                raise ArithmeticError('Intrinsic stage failed: '+sol.message)
        return StageResult(float(left), float(right), combined[:self.dimension],
                           None if columns == 0 else combined[self.dimension:].reshape(self.dimension, columns),
                           self.calls-calls, time.monotonic()-begin, records)

    def angular_monodromy(self, s, state, *, rtol=2e-12, atol=2e-14):
        """Actual angular frame and translation closure of one finite slice.

        Codazzi curvature data on a periodic grid alone do not certify
        closure.  This returns both monodromies without silently projecting
        away either residual.  It is a finite diagnostic.
        """
        aa, ap, _ = self.profile(s)
        aa, ap = float(aa[0]), float(ap[0])
        def rhs(theta, vector):
            n, m = np.asarray(self.at_angle(state, theta), dtype=float)
            if hasattr(self.reference, 'coordinate_speed'):
                speed = float(self.reference.coordinate_speed(theta))
            else:
                coordinate = self.reference.reference_coordinate(theta)
                speed = float(coordinate['u_theta'] if isinstance(coordinate, dict) else coordinate[1])
            b, gamma = aa*speed, ap*speed
            generator = np.array([[0., -gamma, -b*m], [gamma, 0., -b*n], [b*m, b*n, 0.]])
            frame = vector[:9].reshape(3, 3)
            return np.concatenate(((frame@generator).ravel(), b*frame[:, 1]))
        initial = np.concatenate((np.eye(3).ravel(), np.zeros(3)))
        sol = solve_ivp(rhs, (0., 2*np.pi), initial, method='DOP853', rtol=rtol,
                        atol=atol, max_step=np.pi/(4*(self.maximum_mode+1)))
        frame = sol.y[:9, -1].reshape(3, 3)
        translation = sol.y[9:, -1]
        return dict(success=bool(sol.success), frame=frame.tolist(), translation=translation.tolist(),
                    frame_error=float(np.linalg.norm(frame-np.eye(3), ord=2)),
                    translation_error=float(np.linalg.norm(translation)),
                    orthogonality_error=float(np.linalg.norm(frame.T@frame-np.eye(3), ord=2)),
                    rhs_calls=int(sol.nfev), message=sol.message)
