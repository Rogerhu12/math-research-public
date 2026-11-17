"""The same integral-K height with a roundoff-aware literal mean-root solve.

This material-angle adapter changes only the numerical root iteration.  The
height, fixed background, weighted-free rho=1 mean equation, and implicit
derivative are unchanged.  The actual residual is returned without clipping
or replacing it by zero.  No BVP acceptance flag is manufactured.
"""
from pathlib import Path
import importlib.util
import numpy as np

_path = Path(__file__).with_name('2026-11-17-parallel-geometry-tail-readout.py')
_spec = importlib.util.spec_from_file_location('frozen_height_reader', _path)
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)
piece_value = _base.piece_value


class HeightReader(_base.HeightReader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'rho_cos_coefficients' in self.data:
            raise ValueError('This adapter is for material rho=1, not a physical-angle weighted input')
        if self.height_source != 'k-integral':
            raise ValueError('This adapter preserves the integral-K candidate only')

    def solve_mean(self, P, T, Kbar, z, initial):
        c = initial.copy()
        for iteration in range(32):
            fields = self.mean_fields(P, T, Kbar+c[:, None], z)
            mean = np.mean(fields['B'], axis=1)
            mu = 1+c+np.mean(fields['BK1']-(Kbar+c[:, None])-(1+z)*T, axis=1)
            tolerance = 16*np.finfo(float).eps*(1+np.mean(abs(fields['B']), axis=1))
            active = abs(mean) > tolerance
            if not np.any(active):
                return c, fields, mu, iteration+1, tolerance
            correction = np.where(active, mean/mu, 0.)
            current_score = np.max(abs(mean)/tolerance)
            damping = 1.
            for _ in range(32):
                trial = c-damping*correction
                try:
                    candidate = self.mean_fields(P, T, Kbar+trial[:, None], z)
                    new_mean = np.mean(candidate['B'], axis=1)
                    new_tolerance = 16*np.finfo(float).eps*(1+np.mean(abs(candidate['B']), axis=1))
                    if np.max(abs(new_mean)/new_tolerance) < current_score:
                        c = trial
                        break
                except FloatingPointError:
                    pass
                damping /= 2
            else:
                raise FloatingPointError('The actual mean residual did not decrease under safeguarded Newton')
        raise FloatingPointError('Literal mean root did not reach its stated roundoff-scaled residual tolerance')

    def evaluate(self, points, references):
        old = piece_value(self.state, points, references)
        old_x = piece_value(self.state, points, references, 1)
        if self.bg.coordinate == 'source-index':
            r = piece_value(self.bg.radius, points, references)
            rx = piece_value(self.bg.radius, points, references, 1)
            index = np.searchsorted(self.bg.x, references, side='right')-1
            index = np.clip(index, 0, len(self.bg.x)-2)
            rref = self.bg.r[index]
        else:
            r, rx, rref = points, np.ones_like(points), references
        if np.min(rx) <= 0:
            raise ValueError('Physical radius must increase')
        w = np.exp(piece_value(self.bg.spline, r, rref))
        ell = piece_value(self.bg.spline, r, rref, 1)
        hc = self.height_coefficients(points, references)
        p = -self.frequency*hc/(r*w)[:, None]
        k = old[:, self.M:2*self.M]
        kr = old_x[:, self.M:2*self.M]/rx[:, None]
        pr = -self.frequency*k/r[:, None]-(1/r+ell)[:, None]*p
        P, T = p@self.sin.T, (p*self.frequency)@self.cos.T
        Pr, Tr = pr@self.sin.T, (pr*self.frequency)@self.cos.T
        Kbar, Krbar = k@self.cos.T, kr@self.cos.T
        z = w[:, None]**2
        c, fields, mu, iterations, tolerance = self.solve_mean(P, T, Kbar, z, old[:, -1])
        cr = -np.mean(fields['BP']*Pr+fields['BK1']*Krbar+fields['BT1']*Tr
                      + fields['Bz']*(2*w*w*ell)[:, None], axis=1)/mu
        K, Kr = Kbar+c[:, None], Krbar+cr[:, None]
        hperp = hc@self.cos.T
        hr = w[:, None]*(1+K)
        hrr = (w*ell)[:, None]*(1+K)+w[:, None]*Kr
        oldK = old[:, self.M:2*self.M]@self.cos.T+old[:, -1, None]
        oldKr = ((old_x[:, self.M:2*self.M]/rx[:, None])@self.cos.T
                 +(old_x[:, -1]/rx)[:, None])
        return dict(r=r, rx=rx, w=w, wr=w*ell, c=c, cr=cr, hperp=hperp,
                    hr=hr, hrr=hrr, h_phi=(r*w)[:, None]*P,
                    h_phiphi=(r*w)[:, None]*T,
                    hr_phi=-w[:, None]*((k*self.frequency)@self.sin.T),
                    hr_phiphi=-w[:, None]*((k*self.frequency**2)@self.cos.T),
                    height_mean_x=rx*w*(1+c),
                    delta_P=(p-old[:, :self.M])@self.sin.T,
                    delta_K=K-oldK, delta_Kr=Kr-oldKr,
                    delta_c=c-old[:, -1], delta_cr=cr-old_x[:, -1]/rx,
                    literal_mean=np.mean(fields['B'], axis=1),
                    root_iterations=iterations, root_residual_tolerance=tolerance,
                    fields=fields)
