"""Analytic second angular jets of the frozen positive R139 reference.

This supplements, without changing, FrozenCoastReference and its saved first
jet cache.  All divisions by n are divisions by the already positive frozen
reference or inlet, never by an unknown raw field.  The finite Fourier inlet
is differentiated analytically through its fixed material chart.  Numerical
material inversion remains explicitly limited by the original tolerance.
"""
from __future__ import annotations
from collections import OrderedDict
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_frozen_coast_reference import (
    FrozenCoastReference, INVERSE_TOLERANCE, _canonical_u)


def inlet_material_three(coast, material_t):
    """Return derivatives 0..3 in the incoming physical material t.

    The stored n/m coefficients are cosine/sine functions of the fixed seed
    normal angle phi.  h=dt/dphi is the exact moment-defined rho/a0 function;
    this routine evaluates its representatives with the original geometry.
    """
    t = np.asarray(material_t, np.longdouble)
    phi = coast.geometry.normal_angle(t)
    freq = coast.f
    C, S = np.cos(phi[..., None]*freq), np.sin(phi[..., None]*freq)
    pn = (C@coast.n, -S@(freq*coast.n),
          -C@(freq*freq*coast.n), S@(freq*freq*freq*coast.n))
    pm = (S[..., 1:]@coast.m, C[..., 1:]@(freq[1:]*coast.m),
          -S[..., 1:]@(freq[1:]**2*coast.m),
          -C[..., 1:]@(freq[1:]**3*coast.m))
    g = coast.geometry
    sn, cs = np.sin(2*phi), np.cos(2*phi)
    th = np.tanh(g.k*(cs-g.c)); sech = 1-th*th
    rhopp = (2*g.D*g.k*cs*sech + 4*g.D*g.k*g.k*sn*sn*th*sech
             - 4*g.u2*cs - 16*g.u4*np.cos(4*phi))
    h = g.radius(phi)/g.a0
    hp = g.radius_derivative(phi)/g.a0
    hpp = rhopp/g.a0
    if np.any(h <= 0):
        raise FloatingPointError('The frozen inlet material chart is not positive')

    def convert(p):
        f0, f1, f2, f3 = p
        return (f0, f1/h, f2/(h*h)-f1*hp/(h*h*h),
                f3/(h*h*h)-3*f2*hp/(h**4)-f1*hpp/(h**4)
                +3*f1*hp*hp/(h**5))
    return dict(n=convert(pn), m=convert(pm), phi=phi,
                material_inverse_error=np.max(abs(g.material_coordinate(phi)['u']-t)))


class FrozenCoastSecondJets:
    """Small bounded cache of physical value/s/u/uu/su jets, order n,m,l."""
    def __init__(self, reference, *, max_cached_points=4):
        if not isinstance(reference, FrozenCoastReference):
            raise TypeError('Pass the bound immutable FrozenCoastReference object')
        self.reference = reference
        self.max_cached_points = int(max_cached_points)
        if self.max_cached_points < 0:
            raise ValueError('Cache size must be nonnegative')
        self._cache = OrderedDict()
        self.hits = self.misses = 0
        self.maximum_inverse_residual = 0.
        self.maximum_first_jet_discrepancy = 0.
        self.maximum_value_discrepancy = 0.

    def point(self, physical_s, material_u):
        s = float(physical_s)
        ref = self.reference
        if not np.isfinite(s) or not ref.entry_s <= s <= ref.exit_s:
            raise ValueError('Second-jet reference point is outside the frozen coast')
        u, unused_text, digest = _canonical_u(material_u)
        key = (s.hex(), digest)
        if key in self._cache:
            row = self._cache.pop(key)
            if not np.array_equal(row['material_u'], u):
                raise ValueError('The second-jet cache must match the full actual u column')
            self._cache[key] = row
            self.hits += 1
            return row
        sigma = 0. if s == ref.entry_s else ref.length if s == ref.exit_s else s-ref.entry_s
        coast = ref._coast
        q = coast.evaluate(sigma, u, tolerance=INVERSE_TOLERANCE)
        inlet = inlet_material_three(coast, q['inlet_u'])
        nc, nc1, nc2, nc3 = inlet['n']
        mc, mc1, mc2, mc3 = inlet['m']
        if np.any(nc <= 0):
            raise FloatingPointError('The strictly positive frozen inlet was not represented')
        k = mc/nc
        kt = (mc1-nc1*k)/nc
        ktt = (mc2-nc2*k-2*nc1*kt)/nc
        kttt = (mc3-nc3*k-3*nc2*kt-3*nc1*ktt)/nc
        # Match the saved scalar representatives and the original r0=a/v
        # evaluation; no parameter from the current raw state enters here.
        a, v = coast.a, coast.v
        r0, r = a/v, a/v+sigma
        delta = sigma*(2*r0+sigma)
        Q = np.sqrt(r0*r0+(1+k*k)*delta)
        Qt = delta*k*kt/Q
        Qtt = delta*(kt*kt+k*ktt)/Q-delta*delta*k*k*kt*kt/(Q**3)
        denominator = r0+Q
        w = delta/denominator
        wt = -delta*Qt/(denominator*denominator)
        wtt = -delta*Qtt/(denominator*denominator)+2*delta*Qt*Qt/(denominator**3)
        B = v*(1+k*k)-kt
        Bt = 2*v*k*kt-ktt
        Btt = 2*v*(kt*kt+k*ktt)-kttt
        D = a+w*B
        Dt, Dtt = wt*B+w*Bt, wtt*B+2*wt*Bt+w*Btt
        if np.any(D <= 0):
            raise FloatingPointError('The frozen ruling denominator is not positive')
        n = a*nc*Q*Q/(D*r*r)
        logfirst = nc1/nc+2*Qt/Q-Dt/D
        logsecond = (nc2/nc-(nc1/nc)**2
                     +2*(Qtt/Q-(Qt/Q)**2)-Dtt/D+(Dt/D)**2)
        nt, ntt = n*logfirst, n*(logfirst*logfirst+logsecond)
        ratio = k*r0/Q
        rt = r0*(kt/Q-k*Qt/(Q*Q))
        rtt = r0*(ktt/Q-2*kt*Qt/(Q*Q)-k*Qtt/(Q*Q)+2*k*Qt*Qt/(Q**3))
        m, l = n*ratio, n*ratio*ratio
        mt, lt = nt*ratio+n*rt, nt*ratio*ratio+2*n*ratio*rt
        mtt = ntt*ratio+2*nt*rt+n*rtt
        ltt = ntt*ratio*ratio+4*nt*ratio*rt+2*n*(rt*rt+ratio*rtt)
        Ut = D/(v*Q)
        Utt = Ut*(Dt/D-Qt/Q)
        if np.any(Ut <= 0):
            raise FloatingPointError('The frozen material inverse is not monotone')
        first = np.stack((nt, mt, lt), axis=-1)
        second = np.stack((ntt, mtt, ltt), axis=-1)
        uu = (second*Ut[:, None]-first*Utt[:, None])/(Ut[:, None]**3)

        # Retain the original first-jet evaluation pathway.  The new analytic
        # pathway supplies only the previously missing derivatives.
        n0, m0, ns, ms = (np.asarray(q[z], np.longdouble) for z in ('n', 'm', 'n_s', 'm_s'))
        nu, mu, lu = (np.asarray(q[z], np.longdouble) for z in ('n_u', 'm_u', 'l_u'))
        actual_ratio = m0/n0
        ratio_u = (mu*n0-m0*nu)/(n0*n0)
        ls = 2*actual_ratio*ms-actual_ratio*actual_ratio*ns
        radius, connection = a+v*sigma, v/(a+v*sigma)
        nsu = uu[:, 1]/radius+connection*(lu-nu)
        msu = uu[:, 2]/radius-2*connection*mu
        lsu = (2*ratio_u*ms+2*actual_ratio*msu
               -2*actual_ratio*ratio_u*ns-actual_ratio*actual_ratio*nsu)
        values = np.stack((n0, m0, q['l']), axis=-1)
        ds = np.stack((ns, ms, ls), axis=-1)
        du = np.stack((nu, mu, lu), axis=-1)
        su = np.stack((nsu, msu, lsu), axis=-1)
        numerical = dict(material_inverse_residual=float(np.max(abs(q['material_u']-u))),
            inlet_inverse_residual=float(inlet['material_inverse_error']),
            inverse_iterations=int(q['inverse_iterations']),
            first_u_formula_discrepancy=float(np.max(abs(first/Ut[:, None]-du))),
            value_formula_discrepancy=float(np.max(abs(np.stack((n, m, l), axis=-1)-values))))
        row = dict(material_u=u.copy(), physical_s_value=s, diagnostics=numerical)
        for name, value in (('values', values), ('physical_s', ds), ('physical_u', du),
                            ('physical_uu', uu), ('physical_su', su)):
            row[name] = np.asarray(value, dtype=float)
            if not np.all(np.isfinite(row[name])):
                raise FloatingPointError('Nonfinite analytic frozen reference jet: '+name)
            row[name].flags.writeable = False
        row['material_u'].flags.writeable = False
        self.misses += 1
        self.maximum_inverse_residual = max(self.maximum_inverse_residual, numerical['material_inverse_residual'])
        self.maximum_first_jet_discrepancy = max(self.maximum_first_jet_discrepancy, numerical['first_u_formula_discrepancy'])
        self.maximum_value_discrepancy = max(self.maximum_value_discrepancy, numerical['value_formula_discrepancy'])
        if self.max_cached_points:
            self._cache[key] = row
            while len(self._cache) > self.max_cached_points:
                self._cache.popitem(last=False)
        return row

    def definition(self):
        return dict(schema='fd2d-frozen-R139-analytic-second-jets-v1',
            source=identity(Path(__file__)), reference_binding_sha256=self.reference.binding_sha256,
            component_order=['n', 'm', 'l'], physical_derivatives=['s', 'u', 'uu', 'su'],
            inlet_derivatives='Finite Fourier through phi order three, converted analytically by dt/dphi=rho/a0',
            second_u='(f_tt*U_t-f_t*U_tt)/U_t^3 with U_t=D/(v*Q)',
            mixed_su='Differentiate the exact base Codazzi identities; differentiate frozen l=m*m/n',
            reference_parameters_frozen=True, unknown_raw_n_never_divided=True,
            numerical_inversion_tolerance=INVERSE_TOLERANCE,
            finite_differences_define_derivatives=False, continuous_numeric_certificate=False,
            cache=dict(maximum_points=self.max_cached_points, entries=len(self._cache), hits=self.hits, misses=self.misses),
            diagnostics=dict(maximum_material_inverse_residual=self.maximum_inverse_residual,
                maximum_first_u_formula_discrepancy=self.maximum_first_jet_discrepancy,
                maximum_value_formula_discrepancy=self.maximum_value_discrepancy))
