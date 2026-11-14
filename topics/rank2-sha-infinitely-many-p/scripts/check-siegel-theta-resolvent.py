#!/usr/bin/env python3
"""Non-rigorous phase check; the note proves the identities exactly.

This script uses mpmath truncations, not certified interval/tail bounds.
"""
import mpmath as mp

mp.mp.dps = 90
logs = {pow(3, k, 17): k for k in range(16)}
def lam(n):
    return (-mp.j) ** logs[n % 17]
def e(x):
    return mp.exp(2 * mp.pi * mp.j * x)
def theta(a, b, tau):
    return mp.fsum(mp.exp(mp.pi * mp.j * tau * (k+a)**2)
                   * e((k+a)*b) for k in range(-30, 31))
def siegel(a, b, tau):
    q = lambda c: mp.exp(2 * mp.pi * mp.j * tau * c)
    ans = -q((a*a-a+mp.mpf(1)/6)/2)
    ans *= mp.exp(mp.pi * mp.j * b*(a-1)) * (1-q(a)*e(b))
    for k in range(1, 80):
        ans *= (1-q(k+a)*e(b)) * (1-q(k-a)*e(-b))
    return ans

for tau in (mp.j, mp.mpf("0.12")+mp.j*mp.mpf("1.13")):
    direct = mp.fsum(
        lam(n)*e(mp.mpf(19*n*n)/289)
        * mp.exp(mp.pi*mp.j*tau*mp.mpf(n*n)/289)
        for n in range(-350, 351) if n % 17)
    grouped = mp.fsum(
        lam(r)*e(mp.mpf(15*r*r)/289)
        * theta(mp.mpf(r)/17, mp.mpf(4*r)/17, tau)
        for r in range(1, 17))
    den = siegel(mp.mpf(1)/2, mp.mpf(1)/2, tau)
    units = mp.fsum(
        lam(r)*e(mp.mpf(4*r*r+3*r)/68)
        * siegel(mp.mpf(17+2*r)/34, mp.mpf(17+8*r)/34, tau)/den
        for r in range(1, 17))
    errors = abs(direct-grouped), abs(direct/theta(0, 0, tau)-units)
    assert all(err < mp.mpf("1e-80") for err in errors)
    print("tau =", mp.nstr(tau, 8),
          "uncertified numerical differences =",
          tuple(mp.nstr(err, 8) for err in errors))
