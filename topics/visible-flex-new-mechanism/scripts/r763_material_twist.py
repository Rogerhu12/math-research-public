"""Right twist about the true source meridian. All R760 radial differentials stay fixed."""
import numpy as np
from scipy.sparse import csr_matrix, hstack

import r760_full_annulus_frame as material

SMALL = material.weak.FILLET_START
SMALL_WIDTH = material.old.FLAT_START - SMALL
WIDE = .065
WIDE_WIDTH = material.weak.FILLET_START - WIDE
PANELS = (
    ('small_fillet_test', SMALL + .12 * SMALL_WIDTH, SMALL + .22 * SMALL_WIDTH),
    ('wide_first_leg_test', WIDE + .02 * WIDE_WIDTH, WIDE + .06 * WIDE_WIDTH),
    ('whole_free_meridian', material.old.early.FORCED_END, material.old.FLAT_START),
    ('first_S_half', material.old.early.FORCED_END, .326),
    ('second_S_half', .326, material.weak.FILLET_START),
    ('whole_fillet', material.weak.FILLET_START, material.old.FLAT_START),
    ('middle_S', .188, .464),
)


def basis_tags(degree):
    if degree not in (3, 5):
        raise ValueError('R763 has two actual native degrees')
    panels = PANELS[:3] if degree == 3 else PANELS
    modes = 2 if degree == 3 else 4
    return [(name, side, mode) for name, _, _ in panels for side in (1, 3) for mode in range(modes)]


def all_tags(degree):
    return material.shoulders.tags(degree), basis_tags(degree)


def initial_twist(phase, degree, factor):
    name = 'small_fillet_test' if phase <= .08 else 'wide_first_leg_test'
    return np.array([factor * .5074 * phase if label == name and mode == 0 else 0.
                     for label, side, mode in basis_tags(degree)])


def bump(t):
    t = np.asarray(t)
    live = (t > 0) & (t < 1)
    z = np.where(live, t, 0.)
    a = z * (1. - z)
    return 64. * a**3, 192. * a**2 * (1. - 2.*z)


def radial_and_angular(build, degree, radii, angles):
    """All new scalar twist rows and their actual r,s derivatives; s is normalized around the ring."""
    r, s = np.broadcast_arrays(np.asarray(radii, float), np.asarray(angles, float))
    r, s = r.ravel(), s.ravel()
    ell, er, _ = material.space.ell_data(r)
    d, kind, _ = build.ring.label(s)
    length, lu = build.ring.length, build.ring.LU
    radial = {}
    for name, lo, hi in PANELS[:3] if degree == 3 else PANELS:
        value, der = bump((ell-lo)/(hi-lo))
        radial[name] = value, der*er/(hi-lo)
    angular = {}
    for side, start in ((1, 2.), (3, 4.+lu)):
        u = (d-start)/lu
        inside = (kind == side) & (u > .01) & (u < .99)
        t = np.where(inside, (u-.01)/.98, 0.)
        c, dc = bump(t)
        x = 2.*t-1.
        polynomials = (np.ones_like(x), x, (3.*x*x-1.)/2., (5.*x**3-3.*x)/2.)
        derivs = (np.zeros_like(x), 2.*np.ones_like(x), 6.*x, 15.*x*x-3.)
        for mode in range(2 if degree == 3 else 4):
            p, dp = polynomials[mode], derivs[mode]
            angular[side, mode] = c*p, (dc*p+c*dp)*length/(.98*lu)
    ns = len(r)
    tags = basis_tags(degree)
    values, dr, ds = (np.zeros((ns, len(tags))) for _ in range(3))
    for col, (name, side, mode) in enumerate(tags):
        v, vr = radial[name]
        g, gs = angular[side, mode]
        values[:, col], dr[:, col], ds[:, col] = v*g, vr*g, v*gs
    return values, dr, ds


def source_direction(jets):
    _, xr, _, xrr, xrs, _ = jets
    g = np.linalg.norm(xr, axis=1)
    if not np.all(g > 0.):
        raise ValueError('singular source radial direction on actual twist support')
    gr = np.einsum('ij,ij->i', xr, xrr)/g
    gs = np.einsum('ij,ij->i', xr, xrs)/g
    return g[:, None], gr[:, None], gs[:, None]


def turn_jets(original, source, a, ar, az):
    """Curl and five differentials in R732 .read(output=True) order.

    Native r increases toward the outer rim, so L points along -beta_r.
    The old source normalization is real and independent of complex control probes.
    """
    kr, br, bs, brs, brr, bss = original
    g, gr, gs = source
    L = -br/g
    Lr = (-brr-gr*L)/g
    Ls = (-brs-gs*L)/g
    bsr = kr+brs
    proxy = np.cross(L, bs)
    proxy_r = np.cross(Lr, bs)+np.cross(L, bsr)
    proxy_s = np.cross(Ls, bs)+np.cross(L, bss)
    cosine, sine = np.cos(a)[:, None], np.sin(a)[:, None]
    # Stable differences leave the original curvature and mixed terms untouched at zero.
    cosine_change = -2.*np.sin(.5*a)[:, None]**2
    axis_derivative = -sine*bs+cosine*proxy
    changed = bs+cosine_change*bs+sine*proxy
    curl = kr+cosine_change*bsr+sine*proxy_r+ar[:, None]*axis_derivative
    changed_s = bss+cosine_change*bss+sine*proxy_s+az[:, None]*axis_derivative
    return curl, br, changed, brs, brr, changed_s


def original_from_local(frame, ang, dr, ds):
    """Original R760 right Euler angles/derivatives, independently controllable for the Jacobian."""
    apply = material.weak.fields.apply
    matrix, mr, ms = frame.base, frame.br, frame.bs
    for axis in range(3):
        q, qd = material.weak.fields.rotation(ang[:, axis], axis)
        d = matrix@qd
        mr = mr@q+dr[:, axis, None, None]*d
        ms = ms@q+ds[:, axis, None, None]*d
        matrix = matrix@q
    _, pr, ps, prr, prs, pss = frame.j0
    return (apply(mr, ps)-apply(ms, pr), apply(matrix, pr), apply(matrix, ps),
            apply(ms, pr)+apply(matrix, prs), apply(mr, pr)+apply(matrix, prr),
            apply(ms, ps)+apply(matrix, pss))


def native_rows(frame, q, z, basis):
    coefficients = np.asarray(q).reshape(-1, 3)
    angles, dr, ds = (v@coefficients for v in (frame.B, frame.Br, frame.Bs))
    orig = original_from_local(frame, angles, dr, ds)
    jets = turn_jets(orig, source_direction(frame.j0), *(v@z for v in basis))
    return jets


def local_jacobian(frame, q, z, basis):
    """Every old coefficient and every added twist coefficient at exactly the supplied rows."""
    coef = np.asarray(q, float).reshape(-1, 3)
    aa = [v@coef for v in (frame.B, frame.Br, frame.Bs)]
    ax = [v@z for v in basis]
    source = source_direction(frame.j0)
    def curl(parts):
        original = original_from_local(frame, *parts)
        return turn_jets(original, source, *ax)[0]/frame.det[:, None]
    step = 1.e-24
    channels = []
    for j in range(3):
        for axis in range(3):
            parts = list(aa)
            v = parts[j].astype(complex)
            v[:, axis] += step*1j
            parts[j] = v
            channels.append(curl(parts).imag/step)
    original = original_from_local(frame, *aa)
    twist_channels = []
    for j in range(2):
        parts = list(ax)
        parts[j] = parts[j].astype(complex)+step*1j
        physical = turn_jets(original, source, *parts)[0]/frame.det[:, None]
        twist_channels.append(physical.imag/step)
    # Sparse storage uses the exact old scalar-major, physical-axis-minor ordering.
    rows, old_terms = frame.B.shape
    old_j = np.zeros((rows, 3, old_terms, 3))
    for i, native in enumerate((frame.B, frame.Br, frame.Bs)):
        for axis in range(3):
            old_j[:, :, :, axis] += channels[3*i+axis][:, :, None]*native[:, None, :]
    new_j = sum(ch[:, :, None]*v[:, None, :] for ch, v in zip(twist_channels, basis[:2], strict=True))
    full = hstack((csr_matrix(old_j.reshape(3*rows, -1)), csr_matrix(new_j.reshape(3*rows, -1))), format='csr')
    return full, np.asarray(channels), np.asarray(twist_channels)


def closest_circumference(radial_unit, angular, length):
    """Rotation-independent physical defect of a single outer-anchored radial reconstruction."""
    L, w = np.asarray(radial_unit), np.asarray(angular)
    h = np.asarray(length)
    projection = np.einsum('...i,...i->...', L, w)
    orthogonal = w-projection[..., None]*L
    norm = np.linalg.norm(orthogonal, axis=-1)
    return dict(radial_dot=projection, transverse_length=norm, source_length=h,
                lower_bound=np.hypot(projection, norm-h))
