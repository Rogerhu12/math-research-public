"""H96: complete physical height rows of the unchanged finite TC trials.

Definitions only at import.  The public owner supplies whole original TC
and RHI carriers and complete successful P96/RHI records.  No old residual,
strip, phase, norm or propagation certificate target is evaluated here.
The new adjoint algebra carries genuine uniform C0 errors of unrestricted
angular support; its primitive bound is 2/5, never the Wiener-only 1/4.
"""
from fractions import Fraction as F

GRID = 8192
OLD_GRID = 2048
MAXIMUM_DEGREE = 3584
STOP = F(9, 50)
EA = F(13, 100000000)
EX = F(33, 500000000)
TARGETS = [
    "complete_same_selected_TC_canonical_height_row96",
    "complete_same_selected_TC_waist_Jacobian_L2_upper96",
    "complete_same_selected_TC_reference_height_row96",
    "complete_same_selected_TC_actual_cap_height_row96",
    "complete_same_selected_TC_actual_cap_height_joint_radius",
    "complete_same_selected_TC_height_reduced_phase_row96",
    "complete_same_selected_TC_height_reduced_phase_joint_radius",
]
COUNTS = [96, 96, 96, 96, 1, 96, 1]
SIGNED_INDICES = (0, 2, 3, 5)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def saved_bound_comparisons():
    """New rational consequences, not a replay of the RHI/WRC/CW targets."""
    checks = {
        "full_real_interpolation_dimension": 2049 < 46**2,
        "whole_A_uniform_error": 46*F("2.788351e-9")+F("3.131e-26") < EA,
        "whole_x_uniform_error": 46*F("1.424040e-9")+F("4.181e-27") < EX,
        "whole_relative_position_bound": F(19, 5)*STOP == F(171, 250),
        "full_y_L1_receiver": F(5, 2)*(1+F(19, 5)*STOP) == F(421, 100),
        "whole_Jy_receiver": F(27, 8)*F(421, 100) == F("14.20875"),
        "all_finite_adjoint_products_unaliased": 2*MAXIMUM_DEGREE < GRID,
        "actual_waist_height_mod_constant": (
            F(".000232743")+F(".004288")+F(".002235")*F(171, 250)
            < F(".00605")),
        "actual_waist_frame_error": F(".000108627")+F(".002235") < F(".002344"),
    }
    require(all(checks.values()), "all new exact saved-bound deductions")
    return checks


class FullContext:
    """Same directed backend, a separate complete 8192-point algebra."""
    def __init__(self, original):
        self.original = original
        self.np, self.arb = original.np, original.arb
        self.Box, self.CBox = original.Box, original.CBox
        self.zeros, self.fft = original.zeros, original.fft
        labels = self.np.arange(GRID)
        self.modes = self.np.where(labels < GRID//2, labels, labels-GRID)
        self.primitive_multiplier = self.zeros((GRID, 1, 1))
        for j in range(-MAXIMUM_DEGREE, MAXIMUM_DEGREE+1):
            if j:
                self.primitive_multiplier[j % GRID, 0, 0] = self.CBox(
                    0., self.arb_box(-self.arb(1)/(4*j)))

    def __getattr__(self, name):
        return getattr(self.original, name)


class UniformPolynomial:
    """Finite real polynomial plus an unrestricted uniform angular error.

    norm bounds the finite polynomial in C0 on its whole current radial
    interval.  It need not be a Wiener norm.  No derivative of error is
    ever taken, and error is never assigned the finite polynomial degree.
    """
    def __init__(self, c, coefficients, degree, norm, error=0., angular_error=True):
        self.context, self.coefficients = c, list(coefficients)
        self.degree = int(degree)
        self.norm, self.error = c.upper(norm), c.upper(error)
        self.angular_error = bool(angular_error)
        self._fourier = None
        require(self.coefficients and 0 <= self.degree <= MAXIMUM_DEGREE
                and 2*self.degree < GRID, "every whole finite angular product fits")
        require(all(x.lo.ndim == 2 and x.lo.shape[0] in (1, GRID)
                    for x in self.coefficients), "complete radial/angle/column axes")
        for x in self.coefficients:
            c.finite(x)

    @classmethod
    def scalar(cls, c, coefficients, error=0.):
        values = []
        for value in coefficients:
            value = c.box(value)
            if not value.lo.shape:
                value = value.reshape(1, 1)
            elif value.lo.ndim == 1:
                value = value.reshape(1, -1)
            require(value.lo.ndim == 2 and value.lo.shape[0] == 1,
                    "one radial scalar, including its complete scalar error")
            values.append(value)
        norm = c.add_upper(*(c.absolute(x[0]) for x in values))
        return cls(c, values, 0, norm, error, False)

    @classmethod
    def from_fourier(cls, c, z, degree, error=0., angular_error=True, norm=None):
        require(z.real.lo.ndim == 3 and z.real.lo.shape[0] == GRID,
                "the entire new Fourier tensor")
        absent = abs(c.modes) > degree
        require(c.np.all(z.real.lo[absent] <= 0)
                and c.np.all(z.real.hi[absent] >= 0)
                and c.np.all(z.imag.lo[absent] <= 0)
                and c.np.all(z.imag.hi[absent] >= 0),
                "only proved absent finite-polynomial coefficients are zeroed")
        z[absent] = 0
        values = c.real(z[0:1] if degree == 0 else c.fft.fft(z, inverse=True)*GRID)
        if norm is None:
            norm = c.wiener(z)
        result = cls(c, [values[:, k, :] for k in range(values.lo.shape[1])],
                     degree, norm, error, angular_error)
        result._fourier = z
        return result

    def coerce(self, other):
        if isinstance(other, UniformPolynomial):
            require(other.context is self.context, "one complete new C0 algebra")
            return other
        return self.scalar(self.context, [other])

    def __add__(self, other):
        other, c = self.coerce(other), self.context
        cs = [(self.coefficients[k] if k < len(self.coefficients) else c.Box(0.))
              +(other.coefficients[k] if k < len(other.coefficients) else c.Box(0.))
              for k in range(max(len(self.coefficients), len(other.coefficients)))]
        return UniformPolynomial(c, cs, max(self.degree, other.degree),
            c.add_upper(self.norm, other.norm), c.add_upper(self.error, other.error),
            self.angular_error or other.angular_error)

    __radd__ = __add__

    def __neg__(self):
        return UniformPolynomial(self.context, [-x for x in self.coefficients],
            self.degree, self.norm, self.error, self.angular_error)

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other, c = self.coerce(other), self.context
        cs = []
        for k in range(len(self.coefficients)+len(other.coefficients)-1):
            value = c.Box(0.)
            for i in range(max(0, k-len(other.coefficients)+1),
                           min(k, len(self.coefficients)-1)+1):
                value = value+self.coefficients[i]*other.coefficients[k-i]
            cs.append(value)
        error = c.add_upper(c.mul_upper(self.norm, other.error),
            c.mul_upper(other.norm, self.error), c.mul_upper(self.error, other.error))
        degree = self.degree+other.degree
        return UniformPolynomial(c, cs, degree, c.mul_upper(self.norm, other.norm),
            error, degree > 0 or self.angular_error or other.angular_error)

    __rmul__ = __mul__

    def Fourier(self):
        if self._fourier is None:
            c = self.context
            columns = max(x.lo.shape[1] for x in self.coefficients)
            z = c.zeros((GRID, len(self.coefficients), columns))
            if self.degree == 0:
                for k, value in enumerate(self.coefficients):
                    z[0, k, :] = c.CBox(value[0])
            else:
                for k, value in enumerate(self.coefficients):
                    z[:, k, :] = c.CBox(value)
                z = c.fft.fft(z)/GRID
                absent = abs(c.modes) > self.degree
                require(c.np.all(z.real.lo[absent] <= 0)
                        and c.np.all(z.real.hi[absent] >= 0)
                        and c.np.all(z.imag.lo[absent] <= 0)
                        and c.np.all(z.imag.hi[absent] >= 0),
                        "all finite adjoint products formed before Fourier projection")
                z[absent] = 0
            self._fourier = z
        return self._fourier

    def primitive(self):
        c = self.context
        # A scalar error known to be radial has exactly zero angular primitive.
        error = c.mul_upper(c.box(F(2, 5)), self.error) if self.angular_error else 0.
        if self.degree == 0:
            return UniformPolynomial(c, [c.Box(0.).reshape(1, 1)], 0, 0., error, True)
        return self.from_fourier(c, self.Fourier()*c.primitive_multiplier,
            self.degree, error, True, c.mul_upper(c.box(F(2, 5)), self.norm))

    def mean(self):
        c = self.context
        values = c.real(self.Fourier()[0:1])
        result = self.scalar(c, [values[0, k, :] for k in range(values.lo.shape[1])],
                             self.error)
        result.norm = self.norm
        return result

    def affine(self, offset, slope):
        c = self.context
        return UniformPolynomial(c, c.affine_polynomial(self.coefficients, offset, slope),
            self.degree, self.norm, self.error, self.angular_error)


def from_old(c, value):
    """Re-embed complete old finite coefficients; Wiener errors imply C0 errors."""
    old = value.Fourier()
    n = old.real.lo.shape[0]
    require(n == 1024 and 2*value.degree < n, "same original small coefficient algebra")
    out = c.zeros((GRID, old.real.lo.shape[1], old.real.lo.shape[2]))
    out[:n//2] = old[:n//2]
    out[-n//2:] = old[n//2:]
    return UniformPolynomial.from_fourier(c, out, value.degree, value.error,
        value.error_degree > 0, value.norm)


def lift_relative(c, coefficients):
    """The original real Nyquist interpolant of all twelve A/x coefficients."""
    require(coefficients.ndim == 3 and coefficients.shape[1:] == (OLD_GRID, 12)
            and c.np.all(c.np.isfinite(coefficients)), "all original A9/x3 coefficients")
    old = c.fft.fft(c.CBox(c.Box(c.np.transpose(coefficients, (1, 0, 2)))))/OLD_GRID
    count = coefficients.shape[0]
    z = c.zeros((GRID, count, 12))
    half = OLD_GRID//2
    z[:half] = old[:half]
    z[-half+1:] = old[-half+1:]
    nyquist = c.real(old[half])
    z[half], z[-half] = c.CBox(nyquist/2), c.CBox(nyquist/2)
    values = c.real(c.fft.fft(z, inverse=True)*GRID)
    out = []
    for j in range(12):
        error = c.box(EA if j < 9 else EX)
        norm = c.box((F(1) if j < 9 else F(171, 250))+(EA if j < 9 else EX))
        value = UniformPolynomial(c, [values[:, k, j:j+1] for k in range(count)],
                                  half, norm, error, True)
        value._fourier = z[:, :, j:j+1]
        out.append(value)
    return out


def selected_fields(bundle, item, left, right):
    """All original selected coefficients for a new homogeneous height row."""
    c, core, nu = bundle["c"], bundle["core"], bundle["nu"]
    f = bundle["rhi"].Fields(c, core, nu)
    row, read = bundle["rows"][item["row"]], bundle["read_ball"]
    scalar = {name: core.scalar_taylor(c, row["intrinsic_midpoint_jets"],
        row["intrinsic_whole_third_jets"], name, *row["interval"], left, right, read)
        for name in ("beta", "K", "gamma", "s")}
    background = nu.base_background(c, core, bundle["base"], bundle["offsets"],
                                   item["background_piece"], left, right, scalar["s"])
    u, v = (f.selected(value) for value in background)
    require(right <= nu.A or left >= nu.A, "the whole original metric-bump seam")
    scalar = core.selected_intrinsic_fees(c, scalar, row["intrinsic_whole_third_jets"],
                                         F(1, 10000000000), left >= nu.A, read)
    beta, K, gamma = (f.cut(scalar[name]) for name in ("beta", "K", "gamma"))
    a = f.cut(f.radius(row, left, right, read))
    invm, invg = f.reciprocal(f.cut(v.mean())), f.reciprocal(gamma)
    d = -f.product(beta, f.cut(f.product(u, u)+f.product(K, f.product(v, v))).primitive())
    return dict(u=u, v=v, beta=beta, K=K, gamma=gamma, a=a,
                invm=invm, invg=invg, d=d)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), 0)


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def height_adjoint(c, fields, relative, endpoint, J0):
    """PH.20--21, using exact SO3 covariance before polynomial approximation."""
    f = {name: from_old(c, value) for name, value in fields.items()}
    A = [relative[3*i:3*i+3] for i in range(3)]
    x, x0 = relative[9:12], endpoint[9:12]
    chi = [endpoint[0], endpoint[3], endpoint[6]]
    vf = [J0*dot([A[k][i] for k in range(3)], chi) for i in range(3)]
    world_cross = cross([x[k]-x0[k] for k in range(3)], chi)
    axial = [J0*dot([A[k][i] for k in range(3)], world_cross) for i in range(3)]
    rt, rk, rp = axial[0], -axial[1], axial[2]
    a, beta, gamma, K, u, v, d, im, ig = (f[name] for name in
        ("a", "beta", "gamma", "K", "u", "v", "d", "invm", "invg"))
    kt = beta*ig*rp-a*vf[1]
    kd = kt*v*im+a*rk*u*im+a*rt*im
    k1 = -gamma*kt+a*rk*d*im
    k2 = kt*d*im+a*rk*gamma*K
    km = -kt*d*v*im*im-a*rk*d*u*im*im-a*rt*d*im*im
    primitive = kd.primitive()
    return k1+2*beta*u*primitive, k2+2*beta*K*v*primitive+km.mean()


def row_coefficients(c, first, second):
    za, zb = first.Fourier(), second.Fourier()
    count = max(za.real.lo.shape[1], zb.real.lo.shape[1])
    output = c.Box(c.np.zeros((count, 193)))
    root2 = 2*c.sqrt_half
    if zb.real.lo.shape[1]:
        value = zb.real[0, :, 0]
        output.lo[:len(value.lo), 96], output.hi[:len(value.hi), 96] = value.lo, value.hi
    for j in range(1, 97):
        aa, bb = -root2*za.imag[j, :, 0], root2*zb.real[j, :, 0]
        output.lo[:len(aa.lo), j-1], output.hi[:len(aa.hi), j-1] = aa.lo, aa.hi
        output.lo[:len(bb.lo), 96+j], output.hi[:len(bb.hi), 96+j] = bb.lo, bb.hi
    return [output[k, :].reshape(193, 1) for k in range(count)]


def signed_integral(c, row, trial, length):
    require(len(trial) == 8 and all(x.lo.shape == (193, 96) for x in trial),
            "all eight true-root radial coefficients of every original trial")
    total = c.Box(c.np.zeros(96))
    for k, coefficient in enumerate(trial):
        moment = c.Box(c.np.zeros((193, 1)))
        for j, value in enumerate(row):
            if (j+k) % 2 == 0:
                moment = moment+value*c.box(length/F(j+k+1))
        total = total+c.reduce_box(moment*coefficient, axis=0)
    return c.finite(total)


def magnitude(value):
    require(value.is_finite(), "one whole finite directed scalar")
    return max(abs(value.lower()), abs(value.upper())).upper()


def vector_balls(c, box):
    require(box.lo.shape == box.hi.shape == (96,), "all signed finite rows")
    return [c.arb(float(lo)).union(c.arb(float(hi))) for lo, hi in zip(box.lo, box.hi)]


def centres_and_radius(c, values):
    require(len(values) == 96, "the entire simultaneous row before its radius")
    centres = [str(F.from_float(float(value.mid()))) for value in values]
    square = c.arb(0)
    for value, centre in zip(values, centres):
        error = magnitude(value-c.exact(F(centre)))
        square += error*error
    return centres, square.sqrt().upper()


def waist_data(bundle, c):
    """Full original waist Jacobian and all96 true-coordinate variation norms."""
    row, read = bundle["rows"][0], bundle["read_ball"]
    left, right = map(F, row["interval"])
    require(left == 0 < right, "the genuine original waist")
    delta = c.exact(-(left+right)/2)
    jets, whole = row["intrinsic_midpoint_jets"], row["intrinsic_whole_third_jets"]
    s = read(jets["s"])+delta*read(jets["s1"])+delta**2*read(jets["s2"])/2
    s += delta**3*read(whole["s3"])/6
    raw, offsets = bundle["base"]["piece_coefficients"], bundle["offsets"]
    require(raw.shape == (4, 6144, 65), "entire original nominal centre")
    physical = []
    for j in range(65):
        offset = c.arb(float(offsets["lower"][0, j])).union(
                         c.arb(float(offsets["upper"][0, j])))
        physical.append(c.exact(bundle["nu"].ALPHA)*c.arb(float(raw[3, 0, j]))+offset)
    mean = s+physical[32]
    require(mean.upper() < -c.exact(F(16, 15)), "whole actual nonzero waist mean")
    v = [mean]+[physical[32+j]/2 for j in range(1, 33)]
    z = c.zeros((GRID, 1, 1))
    z[0, 0, 0] = 1
    for j in range(1, 33):
        value = c.CBox(c.arb_box(v[j]/mean))
        z[j, 0, 0], z[-j, 0, 0] = value, value
    epsilon = c.exact(F(1, 500000000))
    EJ = (c.exact(F(525, 128))*epsilon).upper()
    J0 = UniformPolynomial.from_fourier(c, z, 32, c.arb_box(EJ), True,
                                        c.arb_box(c.exact(F(27, 8))+EJ))
    waist = bundle["tc_jets"][0][0]
    require(waist.shape == (193, 96), "every original TC waist column and mean")
    output = []
    for column in range(96):
        mu = c.arb(float(waist[96, column]))
        h2 = sum((c.arb(float(waist[96+j, column]))**2 for j in range(97)), c.arb(0))
        h2 = h2.sqrt().upper()
        g2 = c.arb(0)
        for j in range(1, 97):
            hj = c.arb(float(waist[96+j, column]))*(c.arb(1)/2).sqrt()
            vj = v[j] if j < len(v) else c.arb(0)
            coefficient = (hj-vj*mu/mean)/mean
            bound = magnitude(coefficient)
            g2 += 2*bound*bound
        output.append((g2.sqrt()+c.exact(F(7875, 1024))*epsilon*h2).upper())
    return J0, output


def compute(bundle, publish, save_prefix, progress):
    """Seven NEW whole height/phase targets; unchanged carrier identities supplied."""
    np, small, core = bundle["np"], bundle["c"], bundle["core"]
    c = FullContext(small)
    plan, tcplan = bundle["rhi_plan"], bundle["tc_plan"]
    require(len(plan) == 2847 and len(tcplan) == 7724,
            "all original whole RHI/TC cells, with no omitted seam")
    cache = np.memmap(bundle["relative_polynomial_path"], dtype="<f8", mode="r",
                      shape=(len(plan), 7, OLD_GRID, 12))
    endpoint_raw = bundle["relative_endpoint"]
    require(endpoint_raw.shape == (OLD_GRID, 18), "the whole original18 endpoint")
    endpoint = lift_relative(c, np.asarray(endpoint_raw[:, :12])[None, :, :])
    J0, gnorm = waist_data(bundle, c)
    records = bundle["p96_actual"]["new_records"]
    Hrecord = records["complete_original_TC_negative_trial_L1_L2_upper96"]
    phase_record = records["complete_same_selected_TC_phase_row96"]
    require(Hrecord["complete_count"] == phase_record["complete_count"] == 96,
            "the entire old phase and L1 vectors, not selected scalar rows")
    H = [c.arb(text).upper() for text in Hrecord["balls"]]
    require(all(x.is_finite() and x >= 0 for x in H), "all whole old trial L1 bounds")
    phase = [c.arb(text) for text in phase_record["balls"]]
    total, maximum_error = c.Box(np.zeros(96)), c.arb(0)
    cursor, tc_cursor, intersections, last_trial = F(0), 0, 0, None
    maximum_degree, maximum_radial_degree = 0, 0
    for index, item in enumerate(plan):
        a, b = map(F, item["interval"])
        require(a == cursor and a < b <= STOP, "the complete chronological relative cover")
        cell = lift_relative(c, np.asarray(cache[index]))
        left = a
        while left < b:
            while F(tcplan[tc_cursor]["interval"][1]) <= left:
                tc_cursor += 1
            trial_item = tcplan[tc_cursor]
            tl, tr = map(F, trial_item["interval"])
            require(trial_item["side"] == "negative" and tl <= left < tr,
                    "the original TC negative trial at this genuine intersection")
            right = min(b, tr)
            piece = trial_item["trial_piece"]
            if piece != last_trial:
                true_left, unused_right, true_length = bundle["tc_helper"].true_interval(
                    small, bundle["tc_definition"], piece)
                trial_base = core.hermite_coefficients(small,
                    [small.Box(x[piece]) for x in bundle["tc_jets"]],
                    [small.Box(x[piece+1]) for x in bundle["tc_jets"]], true_length)
                last_trial = piece
            trial = core.restrict_trial_coefficients(small, trial_base, true_left,
                                                     true_length, left, right)
            centre, half = (left+right)/2, (right-left)/2
            relative = [value.affine((b-centre)/(b-a), -half/(b-a)) for value in cell]
            fields = selected_fields(bundle, item, left, right)
            ell1, ell2 = height_adjoint(c, fields, relative, endpoint, J0)
            maximum_degree = max(maximum_degree, ell1.degree, ell2.degree)
            rows = row_coefficients(c, ell1, ell2)
            maximum_radial_degree = max(maximum_radial_degree, len(rows)-1)
            total = total+signed_integral(c, rows, trial, right-left)
            error = c.add_upper(ell1.error, ell2.error)
            current_error = c.arb(float(np.max(error.hi))).upper()
            if current_error > maximum_error:
                maximum_error = current_error
            intersections += 1
            left = right
        cursor = b
        if (index+1) % 8 == 0 or index+1 == len(plan):
            save_prefix({"kind": "H96_complete_new_height_integral_prefix_v1",
                "exact_interval": ["0", str(cursor)], "complete_relative_cells": index+1,
                "complete_intersections": intersections,
                "all96_signed_polynomial_integrals": [x.str(60) for x in vector_balls(c, total)],
                "complete_uniform_adjoint_error_upper": maximum_error.str(60),
                "maximum_complete_angular_degree": maximum_degree,
                "maximum_complete_radial_degree": maximum_radial_degree,
                "old_L1_or_phase_targets_recomputed": False})
            progress("new_complete_TC96_height_row", {"relative_cells_complete": index+1,
                "relative_cells": len(plan), "exact_endpoint": str(cursor),
                "complete_intersections": intersections})
    require(cursor == STOP, "the entire exact height-body interval, not a partial prefix")
    canonical = [value+c.arb(0, (maximum_error*h).upper())
                 for value, h in zip(vector_balls(c, total), H)]
    canonical = publish(TARGETS[0], canonical, "signed_enclosure")
    gnorm = publish(TARGETS[1], gnorm, "upper")
    kq, kf = c.exact(F(".000108627")), c.exact(F(".000232743"))
    aq, pf = c.exact(F(".002235")), c.exact(F(".004288"))
    yfactor = c.exact(F(27, 8)*F(421, 100))
    reference = [value+c.arb(0, (kq*yfactor*h+kf*g).upper())
                 for value, h, g in zip(canonical, H, gnorm)]
    publish(TARGETS[2], reference, "signed_enclosure")
    cap = [value+c.arb(0, ((kq+aq)*yfactor*h+(kf+pf+aq*c.exact(F(171, 250)))*g).upper())
           for value, h, g in zip(canonical, H, gnorm)]
    cap_centres, unused = centres_and_radius(c, cap)
    cap = publish(TARGETS[3], cap, "signed_enclosure", cap_centres)
    # The radius is relative to the same complete dyadic centres just published.
    cap_radius = sum((magnitude(x-c.exact(F(s)))**2 for x, s in zip(cap, cap_centres)),
                     c.arb(0)).sqrt().upper()
    publish(TARGETS[4], [cap_radius], "upper")
    rho = c.exact(F("-1.543")).union(c.exact(F("-1.5208")))
    reduced = [p-rho*h for p, h in zip(phase, cap)]
    reduced_centres, unused = centres_and_radius(c, reduced)
    reduced = publish(TARGETS[5], reduced, "signed_enclosure", reduced_centres)
    reduced_radius = sum((magnitude(x-c.exact(F(s)))**2
                         for x, s in zip(reduced, reduced_centres)), c.arb(0)).sqrt().upper()
    publish(TARGETS[6], [reduced_radius], "upper")
    return {"complete_new_target_count": 7, "complete_new_target_order": TARGETS,
        "same_original96_TC_trials": True, "same_original_selected_member": True,
        "true_PDE_corrected_columns": False, "complete_original_relative_cells": len(plan),
        "complete_new_intersections": intersections,
        "maximum_complete_angular_degree": maximum_degree,
        "maximum_complete_radial_degree": maximum_radial_degree,
        "full_real_Nyquist_cosine_retained": True,
        "whole_selected_RHI_uniform_A_error": str(EA),
        "whole_selected_RHI_uniform_x_error": str(EX),
        "unrestricted_C0_error_primitive_factor": "2/5",
        "whole_old_P96_L1_and_phase_vectors_reused": True,
        "full_physical_coordinate_term_g_f0_paid": True,
        "one_fixed_height_constant_cancelled_by_Pi_g_zero": True,
        "independent_Yb_Kb_and_geometric_impulse_ports_retained": True,
        "raw_phase_chart_and_direct_parameter_terms_retained_separately": True,
        "actual_cap_input_admissibility_or_full_Schur_proved": False,
        "old_completed_scientific_target_calls": 0,
        "topic_completion_proved": False}
