"""Closed trigonometric latitude coordinates and complete physical two-jets."""
import hashlib
import json
import os

import numpy as np


def public():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public' or
            not os.environ.get('GITHUB_RUN_ID', '').isdigit()):
        raise RuntimeError('Public scientific Actions runner required.')


def r703_paid(raw, run, job, source, conclusion):
    expected = 'bd5a52dcc40e31e898d3e02b99e4e5c0d449bfd697ac95faa8a168082c6012b2'
    if (run, job, source, conclusion) != (46151140087, 140997832329,
            '1b2ba533d51b4f4b416d30dcee1aaa516b2c64be', 'success'):
        raise ValueError('The named R703 job has not naturally succeeded at the bound source.')
    # The recovered member is the exact original JSON literal. Its producer's
    # key order is not a semantic condition; retain the full byte identity gate.
    start = 0 if len(raw) == 39163 and hashlib.sha256(raw).hexdigest() == expected else raw.find(b'{"actual_accepted"')
    while start >= 0:
        data = raw[start:start + 39163]
        if hashlib.sha256(data).hexdigest() == expected:
            q = json.loads(data)
            if (q['actual_space'] != [12, 5] or len(q['all_parameters']) != 157 or
                    q['frozen'] is not None or q['attempted_level'] != 1 or q['actual_accepted'] != 62):
                raise ValueError('The actual source field differs from the declared seed.')
            return q
        start = raw.find(b'{"actual_accepted"', start + 1)
    raise ValueError('The exact 39163-byte naturally completed FINAL is absent.')


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    x, d, h = a
    y, e, k = b
    return x*y, d*y+x*e, h*y+2*d*e+x*k


def inv(a):
    x, d, h = a
    return 1/x, -d/x**2, 2*d*d/x**3-h/x**2


def lift(fn, a):
    return tuple(fn(x) for x in a)


def stack(*jets):
    return tuple(np.stack(s, axis=-1) for s in zip(*jets))


def stereo(z, sign):
    ss = lift(lambda x: x.sum(axis=1, keepdims=True), mul(z, z))
    one = (np.ones_like(ss[0]), np.zeros_like(ss[0]), np.zeros_like(ss[0]))
    den = inv(add(one, ss))
    first = mul(add(one, neg(ss)), den)
    rest = mul(z, den)
    return tuple(np.concatenate((sign*a, 2*b), axis=1) for a, b in zip(first, rest))


class ClosedSpinor:
    def __init__(self, K, nphi=None):
        public()
        self.K = K
        self.degree = 2*K+1
        self.N = 8*K+5 if nphi is None else nphi
        if self.N < 8*K+5 or self.N % 2 != 1 or K < 0:
            raise ValueError('An odd, unaliased full product lattice is required.')
        self.psi = 2*np.pi*np.arange(self.N)/self.N
        k = (np.arange(K+1)+.5)[:, None]
        self.even_half = np.cos(k*self.psi)
        self.odd_half = np.sin(k*self.psi)
        n = np.arange(1, 2*self.degree+1)[:, None]
        self.cos = np.cos(n*self.psi)
        self.sin = np.sin(n*self.psi)

    def modes(self, f, degree):
        c = 2*np.einsum('mn,rn...->rm...', self.cos[:degree], f)/self.N
        s = 2*np.einsum('mn,rn...->rm...', self.sin[:degree], f)/self.N
        return f.mean(axis=1), c, s

    def angular(self, f, integral):
        k = self.degree
        _, c, s = self.modes(f, k)
        freq = np.arange(1, k+1).reshape((1, k)+(1,)*(f.ndim-2))
        a, b = (-s/freq, c/freq) if integral else (s*freq, -c*freq)
        return (np.einsum('mn,rm...->rn...', self.cos[:k], a) +
                np.einsum('mn,rm...->rn...', self.sin[:k], b))

    def halves(self, z, sign, basis):
        cf = stereo(z, sign)
        return (lift(lambda a: a[:, 0::2] @ basis, cf),
                lift(lambda a: a[:, 1::2] @ basis, cf))

    def state(self, r, za, zb, center, frozen_E=None):
        r = np.asarray(r).reshape(-1, 1)
        if np.any(r <= 0):
            raise ValueError('Positive material radii required.')
        for z in (za, zb):
            if len(z) != 3 or any(np.shape(a) != (len(r), 2*self.K+1) for a in z):
                raise ValueError('Each real stereographic coefficient needs its two radial jets.')
        if len(center) != 3 or any(np.shape(a) != (len(r), 3) for a in center):
            raise ValueError('The actual center and its two radial jets are required.')
        ar, ai = self.halves(za, 1, self.even_half)
        br, bi = self.halves(zb, -1, self.odd_half)
        aa = add(mul(ar, ar), mul(ai, ai))
        bb = add(mul(br, br), mul(bi, bi))
        vx = lift(lambda z: 2*z, add(mul(ar, br), mul(ai, bi)))
        vz = lift(lambda z: 2*z, add(mul(ai, br), neg(mul(ar, bi))))
        velo = stack(vx, add(aa, neg(bb)), vz)
        jj = add(aa, bb)
        j, jr, _ = jj
        if not np.all(np.isfinite(j)) or np.any(j.real <= 0):
            raise FloatingPointError('A sampled closed curve speed failed positivity.')

        def primitive(x):
            return self.angular(x, True)

        gamma = lift(primitive, velo)
        moment = lift(lambda z: z.mean(axis=1, keepdims=True),
                      mul(gamma, lift(lambda z: z[..., None], jj)))
        u, ur, urr = add(gamma, neg(moment))

        def from_zero(x):
            out = primitive(x)
            return out-out[:, 0:1]

        shift, p, pr = lift(from_zero, jj)
        v, vr, _ = velo
        rr = r[..., None]
        c, cr, crr = (z[:, None, :] for z in center)
        tangent = v/j[..., None]
        w = cr+u+rr*ur
        rb = np.sum(w*v, axis=-1)-r*p*j
        alpha = np.sum(w*w, axis=-1)-(r*p)**2
        e = alpha.mean(axis=1) if frozen_E is None else np.asarray(frozen_E)
        if e.shape != (len(r),) or not np.all(np.isfinite(e)) or np.any(e.real <= 0):
            raise FloatingPointError('A common positive radial E is required at every radius.')
        ra = alpha-e[:, None]
        zra, cra, sra = self.modes(ra, 2*self.degree)
        zrb, crb, srb = self.modes(rb, 2*self.degree)
        vp = self.angular(v, False)
        jp = self.angular(j, False)
        g = p/j
        gp = (jr-g*jp)/j
        gr = (pr-g*jr)/j
        tp = (vp-jp[..., None]*tangent)/j[..., None]
        tr = (vr-jr[..., None]*tangent)/j[..., None]-g[..., None]*tp
        du = ur-g[..., None]*v
        ddu = urr-2*g[..., None]*vr+g[..., None]**2*vp+(g*gp-gr)[..., None]*v
        jets = (c+rr*u, w-(r*p)[..., None]*tangent, tangent,
                crr+2*du+rr*ddu, tangent/rr+tr, tp/(r*j)[..., None])
        j0, jc, js = self.modes(j, self.degree)
        derivative_bound = (np.arange(1, self.degree+1)*(abs(jc)+abs(js))).sum(axis=1)
        jlower = np.min(j.real, axis=1)-np.pi*derivative_bound/self.N

        def max_psi(y):
            return np.max(abs(y), axis=1)

        identity_reads = dict(
            mean_J_minus_target_0_1_2=tuple(a.mean(axis=1)-(1. if k == 0 else 0.)
                                            for k, a in enumerate(jj)),
            mean_V_closure_0_1_2=tuple(a.mean(axis=1) for a in velo),
            interpolated_Phi_psi_minus_J_radial_0_1_2=tuple(
                max_psi((1. if k == 0 else 0.)+self.angular(a, False)-q)
                for k, (a, q) in enumerate(zip((shift, p, pr), jj))),
            interpolated_U_psi_minus_V_radial_0_1_2=tuple(
                max_psi(self.angular(a, False)-q) for a, q in zip((u, ur, urr), velo)),
            sampled_V_squared_minus_J_squared=max_psi(np.sum(v*v, axis=-1)-j*j),
            certified_continuous=False)
        return dict(E=e, all_cos_RA=cra, all_sin_RB=srb, mean_RA=zra,
                    complete_RA=(zra, cra, sra), complete_RB=(zrb, crb, srb),
                    parity_read=(sra, zrb, crb), full_RA=ra, full_RB=rb,
                    material_angle=self.psi+shift, material_angle_r=p, material_angle_rr=pr,
                    auxiliary_position_jets=(u, ur, urr), auxiliary_shift_jets=(shift, p, pr),
                    J=j, sampled_mean_J=j0, ordinary_angular_J_lower=jlower,
                    physical_six_jets=jets, center=center[0], spectral_identity_reads=identity_reads)
