"""R139 physical second jets evaluated at a known frozen ruling label.

This is the same positive frozen reference used by the closed first/second
jet consumers.  It uses the actual atlas label directly, so no material
inverse is needed. The unknown raw n remains independent and is not divided.
"""
from __future__ import annotations
import numpy as np


def ruling_reference_second_jets(atlas, physical_s, labels):
    s = float(physical_s)
    xi = np.atleast_1d(np.asarray(labels, np.longdouble))
    if xi.ndim != 1 or not np.all(np.isfinite(xi)):
        raise ValueError('Use a finite one-dimensional actual ruling label array')
    data = atlas.label_data(xi)
    ruled = atlas.ruling_jet(s, xi, include_native=True)
    q = ruled['native']
    coast = atlas.ruling.base
    sigma = 0. if s == atlas.entry_s else atlas.length if s == atlas.exit_s else s-atlas.entry_s
    nc, mc, nc1, mc1, nc2, mc2 = (np.asarray(data[k], np.longdouble)
        for k in ('n', 'm', 'n_u', 'm_u', 'n_uu', 'm_uu'))
    if np.any(nc <= 0):
        raise FloatingPointError('The strictly positive frozen inlet is not represented')
    g = coast.geometry; freq = coast.f
    C, S = np.cos(xi[:, None]*freq), np.sin(xi[:, None]*freq)
    nphi1, nphi2 = -S@(freq*coast.n), -C@(freq*freq*coast.n)
    nphi3 = S@(freq*freq*freq*coast.n)
    mphi1, mphi2 = C[:, 1:]@(freq[1:]*coast.m), -S[:, 1:]@(freq[1:]**2*coast.m)
    mphi3 = -C[:, 1:]@(freq[1:]**3*coast.m)
    h, hp = data['inlet_chart_derivative'], data['inlet_chart_second']
    sn, cs = np.sin(2*xi), np.cos(2*xi)
    th = np.tanh(g.k*(cs-g.c)); sech = 1-th*th
    hpp = (2*g.D*g.k*cs*sech+4*g.D*g.k*g.k*sn*sn*th*sech
            -4*g.u2*cs-16*g.u4*np.cos(4*xi))/g.a0
    def third(f1, f2, f3):
        return f3/(h**3)-3*f2*hp/(h**4)-f1*hpp/(h**4)+3*f1*hp*hp/(h**5)
    nc3, mc3 = third(nphi1, nphi2, nphi3), third(mphi1, mphi2, mphi3)
    k, kt, ktt = data['k'], data['k_u'], data['k_uu']
    kttt = (mc3-nc3*k-3*nc2*kt-3*nc1*ktt)/nc
    a, v = coast.a, coast.v
    r0, r = a/v, a/v+sigma
    delta = sigma*(2*r0+sigma)
    Q = np.sqrt(r0*r0+(1+k*k)*delta)
    Qt = delta*k*kt/Q
    Qtt = delta*(kt*kt+k*ktt)/Q-delta*delta*k*k*kt*kt/(Q**3)
    den = r0+Q
    w = delta/den
    wt = -delta*Qt/(den*den)
    wtt = -delta*Qtt/(den*den)+2*delta*Qt*Qt/(den**3)
    B = v*(1+k*k)-kt
    Bt = 2*v*k*kt-ktt
    Btt = 2*v*(kt*kt+k*ktt)-kttt
    D, Dt = a+w*B, wt*B+w*Bt
    Dtt = wtt*B+2*wt*Bt+w*Btt
    if np.any(D <= 0):
        raise FloatingPointError('Frozen positive ruling denominator failed')
    n = a*nc*Q*Q/(D*r*r)
    log1 = nc1/nc+2*Qt/Q-Dt/D
    log2 = nc2/nc-(nc1/nc)**2+2*(Qtt/Q-(Qt/Q)**2)-Dtt/D+(Dt/D)**2
    nt, ntt = n*log1, n*(log1*log1+log2)
    ratio = k*r0/Q
    rt = r0*(kt/Q-k*Qt/(Q*Q))
    rtt = r0*(ktt/Q-2*kt*Qt/(Q*Q)-k*Qtt/(Q*Q)+2*k*Qt*Qt/(Q**3))
    mt, lt = nt*ratio+n*rt, nt*ratio*ratio+2*n*ratio*rt
    mtt = ntt*ratio+2*nt*rt+n*rtt
    ltt = ntt*ratio*ratio+4*nt*ratio*rt+2*n*(rt*rt+ratio*rtt)
    Ut = D/(v*Q); Utt = Ut*(Dt/D-Qt/Q)
    first, second = np.stack((nt, mt, lt), axis=-1), np.stack((ntt, mtt, ltt), axis=-1)
    uu = (second*Ut[:, None]-first*Utt[:, None])/(Ut[:, None]**3)
    n0, m0, ns, ms = (np.asarray(q[k], np.longdouble) for k in ('n', 'm', 'n_s', 'm_s'))
    nu, mu, lu = (np.asarray(q[k], np.longdouble) for k in ('n_u', 'm_u', 'l_u'))
    ratio = m0/n0; ru = (mu*n0-m0*nu)/(n0*n0)
    ls = 2*ratio*ms-ratio*ratio*ns
    radius = a+v*sigma; connection = v/radius
    nsu = uu[:, 1]/radius+connection*(lu-nu)
    msu = uu[:, 2]/radius-2*connection*mu
    lsu = 2*ru*ms+2*ratio*msu-2*ratio*ru*ns-ratio*ratio*nsu
    values = np.stack((n0, m0, q['l']), axis=-1)
    du = np.stack((nu, mu, lu), axis=-1)
    result = dict(material_u=np.asarray(ruled['u'], np.longdouble),
        label=xi.copy(), diagnostics=dict(material_inverse_used=False,
            first_u_formula_discrepancy=float(np.max(abs(first/Ut[:, None]-du))),
            second_derivatives_from='Analytic finite inlet phi third derivative and R139 rational/radical derivatives'),
        values=values, physical_s=np.stack((ns, ms, ls), axis=-1), physical_u=du,
        physical_uu=uu, physical_su=np.stack((nsu, msu, lsu), axis=-1))
    for name in ('values', 'physical_s', 'physical_u', 'physical_uu', 'physical_su'):
        result[name] = np.asarray(result[name], float)
        if not np.all(np.isfinite(result[name])):
            raise FloatingPointError('Nonfinite direct-label second jet: '+name)
    return result
