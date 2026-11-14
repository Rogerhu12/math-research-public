#!/usr/bin/env python3
"""A physical coast-length design parameter in a smooth radial chart.

Changing T changes the physical metric and is an OUTER DESIGN operation.
The computational x domain stays fixed.  Inside the two changing coasts,
s(x,T) uses a quintic step with s_x=1 at both ends; all other pieces are
translated.  Thus no artificial derivative jump is imposed on a global
C1 collocation polynomial.  The old candidate file is never edited.
"""
from __future__ import annotations
import numpy as np
from fd2d_partial_return_parameter import PartialReturnParameter


class CoastDesignProfile:
    def __init__(self, source, *, reference_T=None):
        self.model = PartialReturnParameter(source)
        self.reference_T = self.model.T0 if reference_T is None else float(reference_T)
        self.base = self.model.candidate(self.reference_T)
        self.ellipse, self.a0 = self.base.ellipse, self.base.a0
        self.end, self.breaks, self.segments = self.base.end, self.base.breaks, self.base.segments
        self.T = None
        self._cache = {}
        self.set_parameter(self.reference_T)

    def set_parameter(self, T):
        T = float(T)
        if self.T == T:
            return
        if not 0 < T < self.model.Tmax:
            raise FloatingPointError('Coast length is outside the physical positive-length interval')
        candidate = self.model.candidate(T)
        if len(candidate.segments) != len(self.base.segments):
            raise FloatingPointError('A zero-length segment needs a different radial chart')
        minimum = 1.
        for index in (self.model.shallow, self.model.deep):
            ratio = candidate.segments[index]['L']/self.base.segments[index]['L']
            minimum = min(minimum, 1+min(0., ratio-1)*1.875)
        if minimum <= 0:
            raise FloatingPointError('The radial design chart needs recentering at another T; no physical nonexistence assertion')
        self.T, self.current, self.minimum_radial_scale = T, candidate, minimum
        self._cache = {}

    def jet(self, x):
        x = np.atleast_1d(np.asarray(x, dtype=float))
        key = x.tobytes()
        if key in self._cache:
            return self._cache[key]
        if np.any(x < -2e-12) or np.any(x > self.end+2e-12):
            raise ValueError('Outside the fixed computational radial domain')
        ids = np.clip(np.searchsorted(self.breaks, x, side='right')-1, 0, len(self.segments)-1)
        keys = ('a','a_s','a_ss','a_T','a_s_T','a_ss_T','s','s_T','radial_scale','radial_scale_T')
        out = {k:np.empty_like(x) for k in keys}
        for j in np.unique(ids):
            mask = ids == j
            old, new = self.base.segments[j], self.current.segments[j]
            tau = np.clip((x[mask]-old['s0'])/old['L'], 0, 1)
            if j <= self.model.shallow:
                shift_T = 0.
            elif j <= self.model.deep:
                shift_T = 1.
            else:
                shift_T = self.model.total_length_derivative
            changing = j in (self.model.shallow, self.model.deep)
            if changing:
                length_T = 1. if j == self.model.shallow else self.model.deep_length_derivative
                step = tau**3*(10-15*tau+6*tau*tau)
                first = 30*tau*tau*(1-tau)**2
                delta_length = new['L']-old['L']
                local_s = old['L']*tau+delta_length*step
                local_s_T = length_T*step
                physical_tau = local_s/new['L']
                scale = 1+(delta_length/old['L'])*first
                scale_T = (length_T/old['L'])*first
                a_T = (self.model.vm*step if j == self.model.shallow else self.model.vm*(1-step))
            else:
                local_s = new['L']*tau
                local_s_T = np.zeros_like(tau)
                physical_tau, scale, scale_T = tau, np.ones_like(tau), np.zeros_like(tau)
                a_T = np.full_like(tau, self.model.vm if self.model.shallow < j < self.model.deep else 0.)
            aa, ap, app = self.current._jet(new, physical_tau)
            out['a'][mask], out['a_s'][mask], out['a_ss'][mask] = aa, ap, app
            out['a_T'][mask] = a_T
            out['a_s_T'][mask] = out['a_ss_T'][mask] = 0.
            out['s'][mask] = new['s0']+local_s
            out['s_T'][mask] = shift_T+local_s_T
            out['radial_scale'][mask], out['radial_scale_T'][mask] = scale, scale_T
        if np.any(out['radial_scale'] <= 0):
            raise FloatingPointError('The smooth radial chart is not monotone')
        out['c'] = out['a_s']/out['a']
        out['c_T'] = -out['c']*out['a_T']/out['a']
        out['K'] = -out['a_ss']/out['a']
        out['K_T'] = -out['K']*out['a_T']/out['a']
        out['piece'] = ids
        if len(self._cache) >= 4:
            self._cache.pop(next(iter(self._cache)))
        self._cache[key] = out
        return out

    def profile(self, x):
        jet = self.jet(x)
        return jet['a'], jet['a_s'], jet['a_ss']

    def definition(self):
        return dict(kind='coast-T-outer-physical-design-with-smooth-radial-chart',
            reference_T=self.reference_T, actual_T=self.T, physical_T_domain=[0., self.model.Tmax],
            computational_endpoint=self.end, actual_physical_endpoint=self.current.end,
            minimum_s_x=self.minimum_radial_scale,
            changing_coasts=[int(self.model.shallow), int(self.model.deep)],
            coast_map='s=s0(T)+L_ref*tau+(L(T)-L_ref)*(10*tau^3-15*tau^4+6*tau^5)',
            other_piece_map='s=s0(T)+L*tau', physical_metric_changes_with_T=True,
            radial_chart_is_only_a_coordinate_change_at_each_fixed_T=True,
            future_chart_recenter_is_not_a_physical_parameter_restriction=True)
