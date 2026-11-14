#!/usr/bin/env python3
"""Explicit optional first-piece speed pulse for the finite-neck provider.

The physical profile key is initial_speed_pulse (default 0).  A nonzero value
changes the metric while preserving the first piece's radius increment and
endpoint radius/speed/acceleration data.  No old provider is edited.  Install
this hook on the actual loaded provider after its angle-boost hook.  For an
absent or exactly zero key all original arithmetic and geometry are delegated.
Small negative values are supported for genuine central finite differences;
the analytic sufficient guards below keep their speed nonnegative and <1.
"""
from __future__ import annotations
import math
import numpy as np


def install(provider):
    if getattr(provider, '_strong_initial_speed_pulse_installed', False):
        return
    old_velocity = provider.velocity
    old_jet = provider.piece_jet
    old_prefix = provider.NeckPrefix

    def pulse_velocity(seg, u):
        u = np.asarray(u)
        V, kS, b = seg['v1'], seg['k0']*seg['length'], seg['strong_initial_speed_pulse']
        return V*u*u*(3-2*u) + kS*u*(1-u)**2 + 64*b*u**3*(1-u)**3

    def velocity(seg, u):
        if seg.get('strong_initial_speed_pulse', 0.) != 0.:
            return pulse_velocity(seg, u)
        return old_velocity(seg, u)

    def piece_jet(seg, u):
        if seg.get('strong_initial_speed_pulse', 0.) == 0.:
            return old_jet(seg, u)
        u = np.asarray(u)
        S, V, b = seg['length'], seg['v1'], seg['strong_initial_speed_pulse']
        kS = seg['k0']*S
        primitive = (V*u**3*(2-u)/2 + kS*u*u*(6-8*u+3*u*u)/12
            + (16*b/35)*u**4*(35-84*u+70*u*u-20*u**3))
        derivative = 6*V*u*(1-u)+kS*(1-u)*(1-3*u)+192*b*u*u*(1-u)**2*(1-2*u)
        return seg['a0']+S*primitive, pulse_velocity(seg, u), derivative/S

    class InitialPulsePrefix(old_prefix):
        def append(self, segment):
            if segment['kind'] == 'hermite' and not self.segments:
                b = float(self.cfg.get('initial_speed_pulse', 0.))
                if not math.isfinite(b):
                    raise ValueError('Nonfinite initial speed pulse')
                if b != 0.:
                    V, k0, delta = segment['v1'], segment['k0'], float(self.cfg['delta'])
                    if not (0 < V < 1 and k0 > 0 and delta > 0):
                        raise ValueError('Invalid pulsed initial piece')
                    # For b<0, 64*u^3*(1-u)^3/[u^2*(3-2u)] <= 27/4.
                    # The base Hermite speed is in [0,V] if k0*S<=3V.
                    if b >= 0 and not V+b < 1:
                        raise ValueError('Positive pulse violates the sufficient speed bound')
                    if b < 0 and not V-(27/4)*abs(b) > 0:
                        raise ValueError('Negative pulse violates the sufficient positivity bound')
                    c = V/2+16*b/35
                    if c <= 0:
                        raise ValueError('Invalid initial pulse length coefficient')
                    S = 2*delta/(math.sqrt(c*c+k0*delta/3)+c)
                    if not (math.isfinite(S) and S > 0 and k0*S <= 3*V):
                        raise ValueError('Pulsed base Hermite speed is outside its proved domain')
                    self.S = S
                    segment = dict(segment, length=S, strong_initial_speed_pulse=b)
            return super().append(segment)

    provider.velocity = velocity
    provider.piece_jet = piece_jet
    provider.NeckPrefix = InitialPulsePrefix
    provider._strong_initial_speed_pulse_installed = True


def install_globals(namespace):
    """Support providers loaded without registering a sys.modules entry."""
    from types import SimpleNamespace
    proxy = SimpleNamespace(**namespace)
    install(proxy)
    for key in ('velocity', 'piece_jet', 'NeckPrefix', '_strong_initial_speed_pulse_installed'):
        namespace[key] = getattr(proxy, key)
