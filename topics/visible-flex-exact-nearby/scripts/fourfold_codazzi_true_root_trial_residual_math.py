"""TC complete finite-root trial residual algebra; no IO or work at import.

The owner supplies the old directed Box/CBox/FFT implementation and imports
numpy/flint only in public Actions.  All radial coefficients below are
correlated polynomials in one common variable t in [-1,1].  A scalar tail is
a uniform Wiener error with proved finite angular support, never a radial
derivative oracle.  The extra final axis holds independent trial columns.
"""
from fractions import Fraction
from math import factorial, comb

GRID = 1024
HEAD = 96
DIMENSION = 193
MAX_RESIDUAL_DEGREE = 288
NORM_NAMES = ("positive_low", "positive_high_collar", "positive_high_body",
              "negative_root", "negative_strict")
HERMITE_LEFT = (
    (1,0,0,0,-35,84,-70,20),
    (0,1,0,0,-20,45,-36,10),
    (0,0,1,0,-10,20,-15,4),
    (0,0,0,1,-4,6,-4,1),
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


class DirectedContext:
    def __init__(self, np, arb, Box, CBox, zeros, arb_box, reduce_box, fft):
        self.np, self.arb, self.Box, self.CBox = np, arb, Box, CBox
        self.zeros, self.arb_box, self.reduce_box, self.fft = zeros, arb_box, reduce_box, fft
        modes = np.arange(GRID)
        self.modes = np.where(modes < GRID//2, modes, modes-GRID)
        self.sqrt_half = arb_box((arb(1)/2).sqrt())
        self.weights = {}
        for name, exponent in (("L2", Fraction(0)),
                               ("Hminus1", Fraction(-1)),
                               ("Hminus2over3", Fraction(-2,3))):
            vals = []
            for j in self.modes:
                v = arb(1+16*int(j)**2)
                vals.append(arb_box((self.exact(exponent)*v.log()).exp()))
            self.weights[name] = Box(np.array([float(v.lo) for v in vals]),
                                     np.array([float(v.hi) for v in vals]))
        self.primitive_multiplier = zeros((GRID,1,1))
        for j in range(-MAX_RESIDUAL_DEGREE, MAX_RESIDUAL_DEGREE+1):
            if j:
                self.primitive_multiplier[j % GRID,0,0] = CBox(
                    0., arb_box(-arb(1)/(4*j)))
        self._legendre = {}

    def exact(self, value):
        q = value if isinstance(value, Fraction) else Fraction(value)
        return self.arb(q.numerator)/q.denominator

    def box(self, value):
        if isinstance(value, self.Box):
            return value
        if isinstance(value, Fraction):
            return self.arb_box(self.exact(value))
        if hasattr(value, "is_finite"):
            return self.arb_box(value)
        return self.Box(value)

    def finite(self, value):
        require(self.np.all(self.np.isfinite(value.lo))
                and self.np.all(self.np.isfinite(value.hi))
                and self.np.all(value.lo <= value.hi),
                "finite outward interval array")
        return value

    def upper(self, value):
        value = self.finite(self.box(value))
        require(self.np.all(value.hi >= 0), "nonnegative complete upper vector")
        return self.Box(value.hi.copy())

    def absolute(self, value):
        return self.Box(self.finite(value).abs_upper())

    def add_upper(self, *values):
        require(values, "nonempty upper sum")
        out = self.Box(0.)
        for value in values:
            value = self.upper(value)
            if self.np.any(value.hi):
                out = self.upper(out+value)
        return out

    def mul_upper(self, a, b):
        a, b = self.upper(a), self.upper(b)
        if not self.np.any(a.hi) or not self.np.any(b.hi):
            shape = self.np.broadcast_shapes(a.hi.shape, b.hi.shape)
            return self.Box(self.np.zeros(shape))
        return self.upper(a*b)

    def sqrt_upper(self, value):
        value = self.upper(value)
        flat = []
        for x in value.hi.reshape(-1):
            y = self.arb(float(x)).sqrt().upper()
            flat.append(float(self.arb_box(y).hi))
        return self.Box(self.np.array(flat).reshape(value.hi.shape))

    def real(self, value):
        require(self.np.all(value.imag.lo <= 0) and self.np.all(value.imag.hi >= 0),
                "the full real Fourier polynomial has a zero imaginary enclosure")
        return self.finite(value.real)

    def wiener(self, z):
        # z has (mode, radial order, independent column).
        absolute = self.Box(z.magnitude_upper())
        return self.upper(self.reduce_box(self.reduce_box(absolute, axis=0), axis=0))

    def affine_polynomial(self, coefficients, offset, slope):
        """Exact finite substitution p(offset+slope*t); all data are boxes."""
        coefficients = [self.box(x) for x in coefficients]
        offset, slope = self.box(offset), self.box(slope)
        out = [coefficients[-1]]
        for value in reversed(coefficients[:-1]):
            old = out
            out = [old[0]*offset+value]
            for k in range(1, len(old)):
                out.append(old[k]*offset+old[k-1]*slope)
            out.append(old[-1]*slope)
        return out

    def legendre_coefficients(self, z):
        n = z.real.lo.shape[1]
        if n not in self._legendre:
            table = {}
            for k in range(n):
                for j in range(k,n,2):
                    odd = 1
                    for q in range(1,j+k+2,2):
                        odd *= q
                    even = 2**((j-k)//2)*factorial((j-k)//2)
                    table[k,j] = self.box(Fraction((2*k+1)*factorial(j),even*odd))
            self._legendre[n] = table
        out = self.zeros(z.real.lo.shape)
        for (k,j), factor in self._legendre[n].items():
            out[:,k,:] = out[:,k,:]+z[:,j,:]*factor
        return out


class BatchRadialFourier:
    """Real sample polynomial plus one complete finite-support error per column."""
    def __init__(self, context, coefficients, degree, norm, error=0., error_degree=None):
        self.context, self.coefficients = context, list(coefficients)
        self.degree = int(degree)
        self.error_degree = self.degree if error_degree is None else int(error_degree)
        self.norm, self.error = context.upper(norm), context.upper(error)
        require(self.coefficients and 0 <= self.error_degree <= self.degree
                and 0 <= 2*self.degree < GRID, "complete unaliased finite support")
        for value in self.coefficients:
            context.finite(value)
            require(value.lo.ndim == 2 and value.lo.shape[0] in (1,GRID),
                    "sample polynomial has angle and column axes")
        self._fourier = None

    @classmethod
    def scalar(cls, context, coefficients, error=0.):
        cs = []
        for value in coefficients:
            value = context.box(value)
            shape = value.lo.shape
            if not shape:
                value = value.reshape(1,1)
            elif len(shape) == 1:
                value = value.reshape(1,-1)
            require(value.lo.ndim == 2 and value.lo.shape[0] == 1,
                    "scalar radial polynomial has one angular value")
            cs.append(value)
        norm = context.add_upper(*(context.absolute(x[0]) for x in cs))
        return cls(context, cs, 0, norm, error, 0)

    @classmethod
    def from_fourier(cls, context, z, degree, error=0., error_degree=None):
        require(z.real.lo.ndim == 3 and z.real.lo.shape[0] == GRID,
                "complete Fourier/radial/column tensor")
        absent = abs(context.modes) > degree
        require(context.np.all(z.real.lo[absent] <= 0)
                and context.np.all(z.real.hi[absent] >= 0)
                and context.np.all(z.imag.lo[absent] <= 0)
                and context.np.all(z.imag.hi[absent] >= 0),
                "known absent Fourier modes contain zero")
        z[absent] = 0
        if degree == 0:
            values = context.real(z[0:1])
        else:
            values = context.real(context.fft.fft(z, inverse=True)*GRID)
        out = cls(context, [values[:,k,:] for k in range(values.lo.shape[1])],
                  degree, context.wiener(z), error, error_degree)
        out._fourier = z
        return out

    def coerce(self, other):
        if isinstance(other, BatchRadialFourier):
            require(other.context is self.context, "one exact Fourier context")
            return other
        return self.scalar(self.context, [other])

    def __add__(self, other):
        other = self.coerce(other)
        c = self.context
        n = max(len(self.coefficients),len(other.coefficients))
        cs = []
        for k in range(n):
            a = self.coefficients[k] if k < len(self.coefficients) else c.Box(0.)
            b = other.coefficients[k] if k < len(other.coefficients) else c.Box(0.)
            cs.append(a+b)
        return BatchRadialFourier(c,cs,max(self.degree,other.degree),
                c.add_upper(self.norm,other.norm),c.add_upper(self.error,other.error),
                max(self.error_degree,other.error_degree))
    __radd__ = __add__

    def __neg__(self):
        return BatchRadialFourier(self.context,[-x for x in self.coefficients],
                self.degree,self.norm,self.error,self.error_degree)

    def __sub__(self,other):
        return self+-self.coerce(other)

    def __rsub__(self,other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other = self.coerce(other)
        c = self.context
        cs = []
        for k in range(len(self.coefficients)+len(other.coefficients)-1):
            value = None
            for i in range(max(0,k-len(other.coefficients)+1),
                           min(len(self.coefficients)-1,k)+1):
                term = self.coefficients[i]*other.coefficients[k-i]
                value = term if value is None else value+term
            cs.append(value)
        error = c.add_upper(c.mul_upper(self.norm,other.error),
                            c.mul_upper(other.norm,self.error),
                            c.mul_upper(self.error,other.error))
        degrees = [0]
        if c.np.any(self.error.hi):
            degrees.append(self.error_degree+other.degree)
        if c.np.any(other.error.hi):
            degrees.append(other.error_degree+self.degree)
        if c.np.any(self.error.hi) and c.np.any(other.error.hi):
            degrees.append(self.error_degree+other.error_degree)
        return BatchRadialFourier(c,cs,self.degree+other.degree,
                    c.mul_upper(self.norm,other.norm),error,max(degrees))
    __rmul__ = __mul__

    def Fourier(self):
        if self._fourier is None:
            c = self.context
            count = max(x.lo.shape[1] for x in self.coefficients)
            z = c.zeros((GRID,len(self.coefficients),count))
            if self.degree == 0:
                for k,value in enumerate(self.coefficients):
                    z[0,k,:] = c.CBox(value[0])
            else:
                for k,value in enumerate(self.coefficients):
                    z[:,k,:] = c.CBox(value)
                z = c.fft.fft(z)/GRID
                absent = abs(c.modes) > self.degree
                require(c.np.all(z.real.lo[absent] <= 0)
                        and c.np.all(z.real.hi[absent] >= 0)
                        and c.np.all(z.imag.lo[absent] <= 0)
                        and c.np.all(z.imag.hi[absent] >= 0),
                        "no exact finite output lost by angular truncation")
                z[absent] = 0
            self._fourier = z
        return self._fourier

    def derivative(self):
        c = self.context
        if self.degree == 0:
            return self.coerce(0.)
        z = self.Fourier()*c.CBox(0.,c.Box((4*c.modes)[:,None,None]))
        return self.from_fourier(c,z,self.degree,
                    c.mul_upper(4*self.error_degree,self.error),self.error_degree)

    def primitive(self):
        c = self.context
        if self.degree == 0:
            return self.coerce(0.)
        z = self.Fourier()*c.primitive_multiplier
        error = c.mul_upper(c.box(Fraction(1,4)),self.error) if self.error_degree else 0.
        return self.from_fourier(c,z,self.degree,error,self.error_degree)

    def mean(self):
        c = self.context
        if self.degree == 0:
            return self
        z = self.Fourier()[0:1]
        values = c.real(z)
        return self.scalar(c,[values[0,k,:] for k in range(values.lo.shape[1])],self.error)

    def radial_derivative(self, scale):
        c = self.context
        require(not c.np.any(self.error.hi),
                "radial differentiation is only allowed for an exact trial polynomial")
        if len(self.coefficients) == 1:
            return self.coerce(0.)
        z = self.Fourier()
        out = c.zeros((GRID,len(self.coefficients)-1,z.real.lo.shape[2]))
        for k in range(1,len(self.coefficients)):
            out[:,k-1,:] = z[:,k,:]*(k*c.box(scale))
        return self.from_fourier(c,out,self.degree,0.,0)

    def scalar_range(self):
        c = self.context
        require(self.degree == 0, "whole radial scalar range")
        out = self.coefficients[-1][0]
        for value in reversed(self.coefficients[:-1]):
            out = out*c.Box(-1.,1.)+value[0]
        err = c.Box(-self.error.hi,self.error.hi)
        return c.finite(out+err)


def reflection_polynomial(context, real_coefficients):
    """Every coefficient has shape (193, columns); normalized real basis."""
    c = context
    require(real_coefficients and all(x.lo.ndim == 2 and x.lo.shape[0] == DIMENSION
            for x in real_coefficients), "all193 real coordinates for every order")
    columns = real_coefficients[0].lo.shape[1]
    require(all(x.lo.shape[1] == columns for x in real_coefficients),
            "one complete common column set")
    za = c.zeros((GRID,len(real_coefficients),columns))
    zb = c.zeros((GRID,len(real_coefficients),columns))
    for k,x in enumerate(real_coefficients):
        zb[0,k,:] = c.CBox(x[HEAD])
        for j in range(1,HEAD+1):
            a = c.sqrt_half*x[j-1]
            b = c.sqrt_half*x[HEAD+j]
            za[j,k,:] = c.CBox(0.,-a)
            za[-j,k,:] = c.CBox(0.,a)
            zb[j,k,:] = c.CBox(b)
            zb[-j,k,:] = c.CBox(b)
    return (BatchRadialFourier.from_fourier(c,za,HEAD,0.,0),
            BatchRadialFourier.from_fourier(c,zb,HEAD,0.,0))


def unnormalized_background(context, real_coefficients, mean_scalar):
    """Original signed sin/cos coefficients, with complete scalar s0 added."""
    c = context
    require(real_coefficients and all(x.lo.ndim == 2 and x.lo.shape[0] == DIMENSION
            and x.lo.shape[1] == 1 for x in real_coefficients),
            "whole physical193 background coefficients")
    za = c.zeros((GRID,len(real_coefficients),1))
    zb = c.zeros((GRID,len(real_coefficients),1))
    for k,x in enumerate(real_coefficients):
        zb[0,k,0] = c.CBox(x[HEAD,0])
        for j in range(1,HEAD+1):
            a,b = x[j-1,0]/2,x[HEAD+j,0]/2
            za[j,k,0],za[-j,k,0] = c.CBox(0.,-a),c.CBox(0.,a)
            zb[j,k,0],zb[-j,k,0] = c.CBox(b),c.CBox(b)
    return (BatchRadialFourier.from_fourier(c,za,HEAD,0.,0),
            BatchRadialFourier.from_fourier(c,zb,HEAD,0.,0)+mean_scalar)


def hermite_coefficients(context, left_jets, right_jets, true_length):
    """TC.7 with four physical endpoint jets, returned in z=2t-1."""
    c = context
    require(len(left_jets) == len(right_jets) == 4,
            "value and three complete endpoint derivative vectors")
    h = c.box(true_length)
    require(c.np.all(h.lo > 0), "strict whole true interval length")
    cs = [c.Box(c.np.zeros(left_jets[0].lo.shape)) for _ in range(8)]
    power = c.Box(1.)
    for k in range(4):
        if k:
            power = power*h
        factor = power/c.box(Fraction(factorial(k)))
        for j,a in enumerate(HERMITE_LEFT[k]):
            if a:
                cs[j] = cs[j]+a*factor*left_jets[k]
                for ell in range(j+1):
                    coeff = a*(-1)**(k+ell)*comb(j,ell)
                    cs[ell] = cs[ell]+coeff*factor*right_jets[k]
    return c.affine_polynomial(cs,Fraction(1,2),Fraction(1,2))


def restrict_trial_coefficients(context, coefficients, true_left, true_length,
                                certified_left, certified_right):
    """Algebraic extension is allowed; true endpoints are never replaced."""
    c = context
    centre = (Fraction(certified_left)+Fraction(certified_right))/2
    half = (Fraction(certified_right)-Fraction(certified_left))/2
    require(half > 0, "nonempty exact certification subinterval")
    left,h = c.box(true_left),c.box(true_length)
    require(c.np.all(h.lo > 0), "complete true polynomial coordinate")
    offset = (2*(c.box(centre)-left)/h)-1
    slope = 2*c.box(half)/h
    return c.affine_polynomial(coefficients,offset,slope)


def cutoff_scalar(context, left, right):
    """TC.10 on a certification cell split at 3; derivative is exact."""
    c = context
    left,right = Fraction(left),Fraction(right)
    require(left < right and (right <= 3 or left >= 3),
            "fixed cutoff seam is included in the exact cover")
    if right <= 3:
        return BatchRadialFourier.scalar(c,[1.]),BatchRadialFourier.scalar(c,[0.])
    centre,half = (left+right)/2,(right-left)/2
    cs = c.affine_polynomial([c.Box(x) for x in HERMITE_LEFT[0]],
                             8*(centre-3),8*half)
    chi = BatchRadialFourier.scalar(c,cs)
    return chi,chi.radial_derivative(c.exact(1/half))


def scalar_taylor(context, midpoint_jets, whole_jets, name, old_left, old_right,
                   new_left, new_right, read_ball):
    """Full old eta radius is retained; no old scalar or derivative is rerun."""
    c = context
    a,b,l,r = map(Fraction,(old_left,old_right,new_left,new_right))
    require(a <= l < r <= b, "new true restriction lies in one complete old row")
    centre,half = (a+b)/2,(b-a)/2
    values = [read_ball(midpoint_jets[name+str(k) if k else name])/factorial(k)
              for k in range(3)]
    values.append(read_ball(whole_jets[name+"3"])/6)
    points,error = [],c.arb(0)
    for k,value in enumerate(values):
        require(value.is_finite(), "whole original derivative enclosure")
        f = float(value.mid())
        require(c.np.isfinite(f), "finite explicit dyadic polynomial coefficient")
        exact = c.arb(f)
        difference = value-exact
        e = max(abs(difference.lower()),abs(difference.upper()))
        error += e*c.exact(half)**k
        points.append(c.Box(f))
    new_c,new_h = (l+r)/2,(r-l)/2
    cs = c.affine_polynomial(points,new_c-centre,new_h)
    return BatchRadialFourier.scalar(c,cs,c.arb_box(error.upper()).hi)


def selected_intrinsic_fees(context, scalar, whole, delta_upper, active, read_ball):
    """TC.6; complete fixed old whole coefficients, no new metric jets."""
    c = context
    require(set(scalar) == {"beta","K","gamma","s"}, "all four true scalar carriers")
    if not active:
        return scalar
    d = c.exact(delta_upper)
    require(d > 0, "strict proved selected absolute parameter bound")
    beta,K,gamma,a = (read_ball(whole[name]) for name in ("beta","K","gamma","a"))
    require(a.lower() > 0 and gamma.lower() > 0,
            "complete original positive physical scalar denominator")
    magnitude = lambda x:max(abs(x.lower()),abs(x.upper()))
    t = (magnitude(beta)/(2*(a.lower()*gamma.lower())**2)).upper()
    eg = (magnitude(gamma)*((d/2).exp()-1)).upper()
    ek = (magnitude(K)*(d.exp()-1)+d*t*c.exact(Fraction(2400,13))*d.exp()).upper()
    out = dict(scalar)
    for name,e in (("gamma",eg),("K",ek)):
        old = scalar[name]
        out[name] = BatchRadialFourier(c,old.coefficients,0,old.norm,
                        c.add_upper(old.error,c.arb_box(e).hi),0)
    return out


def prepare_operator(background, scalar):
    """Same full unsolved-background linearization; all finite outputs kept."""
    u,v = background
    beta,K,gamma = (scalar[n] for n in ("beta","K","gamma"))
    u2,v2,uv = u*u,v*v,u*v
    up,vp = u.derivative(),v.derivative()
    m = v.mean()
    return {
        "d":-beta*(u2+K*v2).primitive(),
        "speed12":gamma*m*K, "speed21":-gamma*m,
        "l11":-beta*(1+3*u2+K*v2), "l12":-2*beta*K*uv,
        "l21":-2*beta*uv, "l22":beta*(1-u2-3*K*v2),
        "inner1":u, "inner2":K*v,
        "nonlocal1":-2*beta*up, "nonlocal2":-2*beta*vp,
        "mean1":gamma*K*vp, "mean2":-gamma*up,
    }


def apply_operator(operator, trial):
    a,b = trial
    ap,bp = a.derivative(),b.derivative()
    inside = (operator["inner1"]*a+operator["inner2"]*b).primitive()
    mean = b.mean()
    x = (operator["d"]*ap+operator["speed12"]*bp
         +operator["l11"]*a+operator["l12"]*b
         +operator["nonlocal1"]*inside+operator["mean1"]*mean)
    y = (operator["d"]*bp+operator["speed21"]*ap
         +operator["l21"]*a+operator["l22"]*b
         +operator["nonlocal2"]*inside+operator["mean2"]*mean)
    require(max(x.degree,y.degree) <= MAX_RESIDUAL_DEGREE,
            "the complete M+192 angular residual support")
    return x,y


def complete_residual(operator, trial, radial_derivative):
    rhs = apply_operator(operator,trial)
    return tuple(d-a for d,a in zip(radial_derivative,rhs))


def _square(context, value):
    c = context
    a,b = value.lo*value.lo,value.hi*value.hi
    # One outward step after each binary64 product; zero-crossing lower is exact.
    lo = c.np.where((value.lo <= 0)&(value.hi >= 0),0.,
                   c.np.nextafter(c.np.minimum(a,b),-c.np.inf))
    hi = c.np.nextafter(c.np.maximum(a,b),c.np.inf)
    return c.Box(lo,hi)


def pair_cell_norm_squared(context, pair, length, windows, mode_subset):
    """TC.14 followed by the COMPLETE finite-support error triangle.

    Returns one directed upper L2 norm squared for every independent column.
    """
    c = context
    require(len(pair) == len(windows) == 2 and isinstance(length,Fraction) and length > 0,
            "full pair and exact positive certification-subinterval mass")
    length_box = c.box(length)
    sqrt_length = c.sqrt_upper(length_box)
    mask = (abs(c.modes) <= HEAD if mode_subset == "low" else
            abs(c.modes) >= HEAD+1 if mode_subset == "high" else
            c.np.ones(GRID,dtype=bool))
    require(mode_subset in ("low","high","all"), "an explicit complete projection")
    result = c.Box(0.)
    for p,window in zip(pair,windows):
        require(window in c.weights, "proved original source Sobolev window")
        L = c.legendre_coefficients(p.Fourier())
        square = _square(c,L.real)+_square(c,L.imag)
        weight = c.weights[window]*c.Box(mask.astype(float))
        total = c.Box(0.)
        for ell in range(square.lo.shape[1]):
            term = c.reduce_box(square[:,ell,:]*weight.reshape(GRID,1),axis=0)
            total = total+term*c.box(Fraction(1,2*ell+1))
        finite = c.sqrt_upper(c.upper(total*length_box))
        # s <= 0, so the full Wiener error dominates every projected H^s error.
        full = c.add_upper(finite,c.mul_upper(sqrt_length,p.error))
        result = c.add_upper(result,c.mul_upper(full,full))
    return c.upper(result)


def trial_value(context, coefficients, coordinate):
    c = context
    value = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        value = value*c.box(coordinate)+coefficient
    return c.finite(value)


def full_waist_density(context, raw_normalized, q, ng):
    """Finite degree96 waves, both means; no old target norm is recomputed."""
    c = context
    require(raw_normalized.lo.ndim == 2 and raw_normalized.lo.shape[0] == DIMENSION,
            "complete same signed trial at the true waist")
    q,ng = c.box(q),c.box(ng)
    require(c.np.all(q.lo > 0) and c.np.all(ng.lo > 0),
            "proved positive whole selected waist density scalars")
    # Square roots are whole interval, not an upper endpoint used as a divisor.
    qq = c.arb(float(q.lo)).union(c.arb(float(q.hi)))
    normalizer = ng/c.arb_box((2*qq).sqrt())
    a,b = reflection_polynomial(c,[raw_normalized])
    waves = ((a+b*q)*normalizer,(a-b*q)*normalizer)
    return {"primitive_pair":tuple(w.primitive() for w in waves),
            "means":tuple(w.mean() for w in waves)}


def density_norm_squared(context, density):
    c = context
    total = c.Box(0.)
    for p in density["primitive_pair"]:
        z = p.Fourier()
        require(z.real.lo.shape[1] == 1, "waist value, not a radial polynomial")
        sq = _square(c,z.real[:,0,:])+_square(c,z.imag[:,0,:])
        finite = c.sqrt_upper(c.upper(c.reduce_box(sq,axis=0)))
        value = c.add_upper(finite,p.error)
        total = c.add_upper(total,c.mul_upper(value,value))
    for p in density["means"]:
        require(len(p.coefficients) == 1 and p.degree == 0,
                "both complete independent scalar means")
        value = c.add_upper(c.absolute(p.coefficients[0][0]),p.error)
        total = c.add_upper(total,c.mul_upper(value,value))
    return c.upper(total)


def real_signed_density_pairing(context, row, density, incoming=False):
    """One complete saved RW Fourier row against every signed trial column.

    row contains the full Fourier coefficients k=0..1024 (real and even).
    Only their true overlap |k|<=96 enters this EXACT finite pairing.  No
    old RW epsilon/norm target is evaluated here.
    """
    c = context
    require(len(row) == 1025, "entire exact original RW row carrier admitted")
    require(all(not c.np.any(p.error.hi) for p in
                density["primitive_pair"]+density["means"]),
            "signed finite pairing has no uncharged uniform density error")
    total = c.Box(0.)
    fields = density["primitive_pair"][:1] if incoming else density["primitive_pair"]
    for p in fields:
        z = p.Fourier()
        require(z.real.lo.shape[1] == 1 and z.real.lo.shape[2] >= 1,
                "full waist column set")
        for k in range(1,HEAD+1):
            rk = c.box(row[k])
            # Same real Hilbert pairing; both Fourier signs retained.
            scale = 1 if incoming else c.box(Fraction(1,2))
            total = total+scale*rk*(z.real[k,0,:]+z.real[-k,0,:])
    if incoming:
        total = total+c.box(row[0])*density["means"][0].coefficients[0][0]
    return c.finite(total)
