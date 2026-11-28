"""Once-only physical R703 curve transport to normalized half-frequency coordinates."""
import numpy as np
from scipy.linalg import qr, solve_triangular
from scipy.interpolate import BSpline
from r703_weighted_material_field import spectral
from r726_closed_spinor_fourier import public


def paid_primitive(field, x):
    """Accept the authenticated 157-vector and the specified original 289-angle field."""
    public()
    st = field.state(x, 1.)
    j = st['j']
    t, b = j['T'], j['b']
    w = j['v']/(1+b*b).power(.5)
    J = w/w.avg()
    mt = (t*J.col()).avg()
    raw = ((t-mt)*J.col()).transform(spectral)
    A = raw-(raw*J.col()).avg()

    def anchored(y):
        p = spectral(y)
        return p-p[:, 0:1]

    shift = J.transform(anchored)
    g, c0 = field.g, st['C0']
    center = (st['C'], g.c_value@c0, g.c_derivative@c0)
    other = (st['C'][g.edge_ids], g.left_value@c0, g.left_derivative@c0)
    return A, shift, J, center, other, st


def angular_at(values, psi, order=0):
    """Evaluate the same real, odd-lattice trigonometric polynomial on shared angles."""
    n = values.shape[1]
    if n % 2 != 1 or np.iscomplexobj(values):
        raise ValueError('Real odd-lattice paid source required.')
    a = np.fft.rfft(values, axis=1)/n
    freq = np.arange(1, a.shape[1])
    shape = (1, len(freq))+(1,)*(values.ndim-2)
    s = np.exp(1j*freq[:, None]*np.asarray(psi)[None, :])
    result = 2*np.einsum('rk...,kn->rn...', a[:, 1:]*(1j*freq).reshape(shape)**order, s).real
    return result+(a[:, 0:1].real if order == 0 else 0.)


def half_projection(A, K, half_cells):
    """A is the source primitive's value array at one immutable angular band."""
    public()
    psi = np.linspace(0., np.pi, half_cells+1)
    wt = np.ones(len(psi))/half_cells
    wt[[0, -1]] *= .5
    v = angular_at(A, psi, 1)
    mir = angular_at(A, -psi, 1)*np.array([1., -1., 1.])
    true = .5*(v-mir)
    sym_delta = np.linalg.norm(true-v, axis=-1).max()
    forced = float(abs(true[:, [0, -1]][:, :, [0, 2]]).max())
    for end in (0, -1):
        true[:, end, 0] = 0.
        true[:, end, 2] = 0.
    speed = np.linalg.norm(true, axis=-1)
    L = speed@wt
    if (np.any(speed <= 0) or np.any(true[:, 0, 1] <= 0) or np.any(true[:, -1, 1] >= 0)):
        raise FloatingPointError('Paid curve has failed pole orientation or sampled regularity.')
    normal = true/speed[..., None]
    q = np.zeros((len(A), len(psi), 2), complex)
    q[:, 0, 0] = 1.
    overlap = 1.
    for j in range(1, len(psi)):
        nx, ny, nz = normal[:, j].T
        off = nx+1j*nz
        f, h = q[:, j-1].T
        cand = np.column_stack(((1+ny)*f+off*h, off.conj()*f+(1-ny)*h))/2
        length = np.linalg.norm(cand, axis=1)
        overlap = min(overlap, float(length.min()))
        if np.any(length < .3):
            raise FloatingPointError('Discrete spinor transport needs more angular points.')
        q[:, j] = cand/length[:, None]
    q *= np.sqrt(speed/L[:, None])[..., None]
    phase = (np.arange(K+1)[:, None]+.5)*psi[None, :]
    a = 2*(q[..., 0]*wt)@np.cos(phase).T
    b = 2*(q[..., 1]*wt)@np.sin(phase).T
    na, nb = np.linalg.norm(a, axis=1), np.linalg.norm(b, axis=1)
    if np.any(na < .2) or np.any(nb < .2) or np.any(abs(a[:, 0]) < .2):
        raise FloatingPointError('The proposed spinor or common phase chart has lost its margin.')
    a /= na[:, None]
    b /= nb[:, None]
    gauge = a[:, 0].conj()/abs(a[:, 0])
    a *= gauge[:, None]
    b *= gauge[:, None]

    def inverse(c, sgn):
        flat = np.stack((c.real, c.imag), axis=-1).reshape(len(c), -1)
        den = 1+sgn*flat[:, 0]
        if np.any(den < .05):
            raise FloatingPointError('The real stereographic chart needs a new pole.')
        return flat[:, 1:]/den[:, None], float(den.min())

    za, ma = inverse(a, 1)
    zb, mb = inverse(b, -1)
    aa, bb = a@np.cos(phase), b@np.sin(phase)
    cross = 2*aa*bb.conj()
    approx = np.stack((cross.real, abs(aa)**2-abs(bb)**2, cross.imag), axis=-1)
    return za, zb, dict(min_overlap=overlap, min_sample_speed=float(speed.min()),
            source_length_estimates=L.tolist(), pole_adjustment=forced, symmetry_adjustment=float(sym_delta),
            pre_normalization_A_range=[float(na.min()), float(na.max())],
            pre_normalization_B_range=[float(nb.min()), float(nb.max())],
            pole_margins=[ma, mb],
            actual_velocity_projection_error=float(np.linalg.norm(approx-true/L[:, None, None], axis=-1).max()))


class AnchoredSpaces:
    def __init__(self, a, b, spans, theta):
        self.a, self.b, self.spans, self.theta = a, b, spans, theta
        edges = np.linspace(a, b, spans+1)
        knots = np.r_[[a]*5, edges, [b]*5]
        self.spline = BSpline(knots, np.eye(len(knots)-6), 5)

    def basis(self, r, order):
        b = self.spline(r, order)
        return b[:, 3:-3], np.column_stack((b[:, :3].sum(axis=1), b[:, 3:-3]))

    def seed(self, r, order):
        t = (r-self.a)/(self.b-self.a)
        p = np.polynomial.Polynomial([1, 0, 0, -10, 15, -6]).deriv(order)
        return -np.tan(self.theta/2)*p(t)/(self.b-self.a)**order

    def fit(self, r, weight, fit, za, zb, center):
        bs, bc = self.basis(r, 0)
        target_b = zb.copy()
        target_b[:, 0] -= self.seed(r, 0)

        def least(mat, values):
            scale = np.sqrt(weight[fit])[:, None]
            Q, R = qr(mat[fit]*scale, mode='economic')
            sig = np.linalg.svd(R, compute_uv=False)
            if sig[-1] <= np.finfo(float).eps*sig[0]*len(R):
                raise ArithmeticError('Raw full-column anchored fit has unresolved rank.')
            return solve_triangular(R, Q.T@(values[fit]*scale)), sig.tolist()

        fa, sa = least(bs, za)
        fb, sb = least(bs, target_b)
        fc, sc = least(bc, center[:, [0, 2]])
        report = dict(full_A_singular_values=sa, full_B_singular_values=sb, full_center_singular_values=sc,
                      omitted_source_center_y=float(abs(center[:, 1]).max()))
        return (fa, fb, fc), report

    def actual_jets(self, r, coeff):
        ca, cb, cc = coeff
        za, zb, center = [], [], []
        for i in range(3):
            m, h = self.basis(r, i)
            za.append(m@ca)
            b = m@cb
            b[:, 0] += self.seed(r, i)
            zb.append(b)
            c = h@cc
            zero = np.zeros(len(r), dtype=c.dtype)
            center.append(np.column_stack((c[:, 0], zero, c[:, 1])))
        return tuple(za), tuple(zb), tuple(center)


def source_centroid(A, center, r):
    """New sampled arclength centroid and radial jets at the same source angles."""
    from r703_weighted_material_field import rdot
    av = A.transform(lambda z: spectral(z, True))
    speed = rdot(av, av).power(.5)
    length = speed.avg()
    if np.any(speed.x <= 0):
        raise FloatingPointError('Irregular source curve.')
    mean = (A*(speed/length).col()).avg()
    m, mr, mrr = (v[:, 0, :] for v in (mean.x, mean.d, mean.dd))
    r = r[:, None]
    c, cr, crr = center
    return (c+r*m, cr+m+r*mr, crr+2*mr+r*mrr), length


def material_six(r, U, shift, center, angles, radial_chunk=8):
    """Read the native finite interpolant at fixed physical material angles."""
    public()
    N = U[0].shape[1]
    phi = np.asarray(angles)
    f = np.arange(1, (N+1)//2)
    if N % 2 != 1 or any(np.iscomplexobj(a) for a in (*U, *shift, *center)):
        raise ValueError('Real, odd-lattice native physical source required.')

    def coefficients(values):
        return np.fft.rfft(values, axis=1)/N

    reads = [[] for _ in range(6)]
    glow, inverse_error = float('inf'), 0.
    for lo in range(0, len(r), radial_chunk):
        ids = slice(lo, min(lo+radial_chunk, len(r)))
        rd = np.asarray(r[ids])[:, None, None]
        u, ur, urr = [coefficients(v[ids]) for v in U]
        s, p, pr = [coefficients(v[ids]) for v in shift]

        def expo(z):
            return np.exp(1j*z[..., None]*f[None, None, :])

        def at(a, h, order=0):
            mult = (1j*f).reshape((1, len(f))+(1,)*(a.ndim-2))**order
            val = 2*np.einsum('rtk,rk...->rt...', h, a[:, 1:]*mult).real
            return val+(a[:, 0:1].real if order == 0 else 0.)

        zero = np.ones((len(s), 1, len(f)), complex)
        z0, z1, z2 = (at(a, zero) for a in (s, p, pr))
        lip = 2*(abs(s[:, 1:])*f[None, :]**2).sum(axis=1)
        for m in (N, 2*N, 4*N, 8*N, 16*N):
            pilot = np.broadcast_to(2*np.pi*np.arange(m)/m, (len(s), m))
            lb = (1+at(s, expo(pilot), 1)).min(axis=1)-np.pi*lip/m
            if np.all(lb > 1.e-9):
                break
        else:
            raise FloatingPointError('Native angle has no resolved positive lower estimate.')
        glow = min(glow, float(lb.min()))
        left = np.zeros((len(s), len(phi)))
        right = np.full_like(left, 2*np.pi)
        for _ in range(50):
            mid = (left+right)/2
            ph = mid+at(s, expo(mid))-z0
            less = ph < phi[None, :]
            left, right = np.where(less, mid, left), np.where(less, right, mid)
        psi = (left+right)/2
        h = expo(psi)
        inverse_error = max(inverse_error, float(abs(psi+at(s, h)-z0-phi[None, :]).max()))
        J, jp, jr = 1+at(s, h, 1), at(s, h, 2), at(p, h, 1)
        P, Pr = at(p, h)-z1, at(pr, h)-z2
        g = P/J
        gp, gr = (jr-g*jp)/J, (Pr-g*jr)/J
        a, ar, arr = at(u, h), at(ur, h), at(urr, h)
        ap, app, arp = at(u, h, 1), at(u, h, 2), at(ur, h, 1)
        T = ap/J[..., None]
        tp = (app-jp[..., None]*T)/J[..., None]
        tr = (arp-jr[..., None]*T)/J[..., None]-g[..., None]*tp
        du = ar-g[..., None]*ap
        ddu = arr-2*g[..., None]*arp+g[..., None]**2*app+(g*gp-gr)[..., None]*ap
        c, cr, crr = [z[ids, None, :] for z in center]
        actual = (c+rd*a, cr+a+rd*du, T, crr+2*du+rd*ddu, T/rd+tr, tp/(rd*J[..., None]))
        for out, val in zip(reads, actual):
            out.append(val)
    return tuple(np.concatenate(a, axis=0) for a in reads), dict(
            native_ordinary_J_lower=glow, native_inverse_error=inverse_error, certified_continuous=False)
