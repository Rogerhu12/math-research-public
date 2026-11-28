"""Fixed affine geometry and full Laurent arithmetic for the physical base Newton response."""
from fractions import Fraction
from functools import lru_cache

from flint import acb, acb_poly, acb_series, arb, ctx

import fourfold_codazzi_fixed_eta0_correlated_mean_retraction as fm

DEGREE = 22
DISC = 16
GRID = 48
HEAD = 96
BAND = 160
DIM = 2*HEAD+1


def require(ok, message):
    if not ok:
        raise ValueError(message)


def scalar_germ(target, left, right, z0, count, tail_radius, real_input):
    """The exact same intrinsic affine member and controlled rotational reference as FM."""
    old, ctx.cap = ctx.cap, count
    try:
        data = target.intrinsic(z0, count, "body", tail_radius, real_input)
        a, beta, height, en, ebar, k0 = (data[k] for k in ("a","beta","H","energy","Ebar","Kold"))
        z = acb_series([acb(z0), 1])
        w = fm.bump(left, right, z)
        control = (fm.rat(fm.NU)*w).exp()
        expminus = acb_series([(fm.rat(fm.NU)*w[0]).expm1()]
                              +[control[k] for k in range(1,control.prec)],prec=control.prec)
        g = ebar*control
        r = height**2 + en/a**2 + ebar/a**2*expminus
        ratio = g/r
        require(a[0].abs_lower()>0 and ebar[0].real>0 and g[0].real>0 and
                r[0].real>0 and ratio[0].real>0, "one finite analytic rotational branch")
        curvature = (k0+fm.rat(fm.NU)*beta*w.derivative()/(2*a**2*ebar))/control
        fields = (beta, curvature, g.sqrt(), -ratio.sqrt())
        require(all(v.prec>=1 and v[0].is_finite() for v in fields), "four finite actual geometric fields")
        return fields
    finally:
        ctx.cap = old


class Geometry:
    """All Fourier aliases of the original affine primitive remain in the coefficient balls."""
    def __init__(self, target, left, right):
        part, germ = target.select(left,right)
        require(part=="body" and germ[0]<=left<right<=germ[1], "same original local intrinsic germ")
        self.mid = fm.rat((left+right)/2)
        half = fm.rat((right-left)/2)
        rho = 24*half
        box = acb(self.mid+fm.sym(rho),fm.sym(rho))
        wide = scalar_germ(target,left,right,box,4,arb(".003"),False)
        self.cap = [abs(v[0]).upper() for v in wide]
        point = scalar_germ(target,left,right,acb(self.mid),DEGREE+4,
                             max(rho,arb(".003")).upper(),True)
        require(all(v.prec>=DEGREE+1 for v in point), "complete four actual radial Taylor polynomials")
        self.coeff = [[fm.real(v[i],"fixed geometric coefficient") for i in range(DEGREE+1)] for v in point]
        eta = fm.rat(Fraction(1,24))
        self.tail = [(b*eta**(DEGREE+1)/(1-eta)).upper() for b in self.cap]

    def real_values(self,r):
        x = r-self.mid
        ans = []
        for cs, tail in zip(self.coeff,self.tail):
            val = cs[-1]
            for c in reversed(cs[:-1]):
                val = val*x+c
            ans.append(val+fm.sym(tail))
        return ans


class Laurent:
    """No Fourier truncation. Index i in the FLINT polynomial is label i minus degree."""
    def __init__(self,degree,poly):
        self.degree = degree
        self.p = poly

    @classmethod
    def scalar(cls,value):
        return cls(0,acb_poly([acb(value)]))

    def __add__(self,other):
        if not isinstance(other,Laurent):
            other = Laurent.scalar(other)
        d = max(self.degree,other.degree)
        def shifted(z):
            off = d-z.degree
            return z.p if off==0 else z.p*monomial(off)
        return Laurent(d,shifted(self)+shifted(other))
    __radd__ = __add__

    def __neg__(self):
        return Laurent(self.degree,-self.p)

    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        if isinstance(other,Laurent):
            return Laurent(self.degree+other.degree,self.p*other.p)
        return Laurent(self.degree,self.p*acb(other))
    __rmul__ = __mul__

    def coeff(self,k):
        return self.p[k+self.degree] if -self.degree<=k<=self.degree else acb(0)

    def primitive(self):
        d = self.degree
        return Laurent(d,acb_poly([self.coeff(k)/acb(0,4*k) if k else acb(0)
                                    for k in range(-d,d+1)]))

    def derivative(self):
        d = self.degree
        return Laurent(d,acb_poly([self.coeff(k)*acb(0,4*k) for k in range(-d,d+1)]))


@lru_cache(maxsize=192)
def monomial(n):
    return acb_poly([0]*n+[1])


def reflected(vector,n,normalized):
    require(len(vector)==2*n+1, "the two complete reflected fields, with independent even mean")
    # Pure parity is valid at complex r as well. There is no coefficient conjugation here.
    denom = arb(2).sqrt() if normalized else arb(2)
    p = [acb(0,1)*v/denom for v in vector[:n]]
    q = [acb(v)/denom for v in vector[n+1:]]
    return (Laurent(n,acb_poly(p[::-1]+[0]+[-v for v in p])),
            Laurent(n,acb_poly(q[::-1]+[acb(vector[n])]+q)))


class RawCubic:
    def __init__(self,base,offsets,k):
        self.knot = fm.rat(Fraction.from_float(float(base["radial_nodes"][k])))
        raw = base["piece_coefficients"][:,k,:][::-1]
        require(raw.shape==(4,65), "all 65 base raw real rows")
        alpha = fm.rat(fm.ALPHA)
        self.c = [[alpha*arb(float(a)) for a in row] for row in raw]
        for j in range(65):
            repair = arb(float(offsets["lower"][k,j])).union(arb(float(offsets["upper"][k,j])))
            self.c[0][j] += repair

    def vectors(self,r):
        x = r-self.knot
        c0,c1,c2,c3 = self.c
        value = [((d*x+c)*x+b)*x+a for a,b,c,d in zip(c0,c1,c2,c3)]
        grad = [(3*d*x+2*c)*x+b for b,c,d in zip(c1,c2,c3)]
        return value,grad


def physical_node(raw,geo,r):
    beta,k,g,s = geo.real_values(r)
    q,qr = raw.vectors(r)
    u,w = reflected(q,32,False)
    ur,wr = reflected(qr,32,False)
    v = w+s
    up,vp = u.derivative(),v.derivative()
    m = v.coeff(0)
    uu,vv,uv = u*u,v*v,u*v
    S = uu+vv*k
    d = S.primitive()*(-beta)
    a12,a21 = g*m*k,-g*m
    force = (d*up+vp*a12-u*(1+S)*beta-ur,
             d*vp+up*a21+(w-uu*v-w*(vv+v*s+s*s)*k)*beta-wr)
    op = (d,a12,a21,-(1+3*uu+vv*k)*beta,uv*(-2*beta*k),
          uv*(-2*beta),(1-uu-vv*(3*k))*beta,u,v*k,up*(-2*beta),
          vp*(-2*beta),vp*(g*k),up*(-g))
    return force,op


def apply(op,pair):
    d,a12,a21,l11,l12,l21,l22,u,kv,n1,n2,m1,m2 = op
    a,b = pair
    ap,bp = a.derivative(),b.derivative()
    inner = (u*a+kv*b).primitive()
    mean = b.coeff(0)
    return (d*ap+bp*a12+l11*a+l12*b+n1*inner+m1*mean,
            d*bp+ap*a21+l21*a+l22*b+n2*inner+m2*mean)


def norm2(pair,weights):
    # Parseval on the full real angular circle, including the even mean exactly once.
    # Parity gives equal moduli for the +/- pair, independently of the interval radii.
    terms = []
    for field in pair:
        require(field.degree<=BAND,"every physical output mode is enclosed")
        terms.append(abs(field.coeff(0))**2)
        terms.extend(2*weights[k]*abs(field.coeff(k))**2 for k in range(1,field.degree+1))
    return sum(terms,arb(0)).upper()


def quadrature():
    nodes = [(arb.pi()*j/GRID).cos() for j in range(GRID+1)]
    weights = []
    for i in range(GRID+1):
        theta = arb.pi()*i/GRID
        term = 1+sum((2*(2*k*theta).cos()/(1-4*k*k) for k in range(1,GRID//2)),arb(0))
        term += (GRID*theta).cos()/(1-GRID*GRID)
        w = term/GRID/(2 if i in (0,GRID) else 1)
        require(w>0,"positive complete flat Clenshaw-Curtis weight")
        weights.append(w)
    require(sum(weights,arb(0)).contains(1),"total normalized flat mass")
    return nodes,weights


def complex_cap(raw,geo,mid,half,L,Lr):
    box = acb(mid+fm.sym(DISC*half),fm.sym(DISC*half))
    q,qr = raw.vectors(box)
    beta,k,g,s = geo.cap
    u = sum(map(abs,q[:32]),arb(0))
    w = sum(map(abs,q[32:]),arb(0))
    v = w+s
    p = sum((4*(j+1)*(abs(q[j])+abs(q[33+j])) for j in range(32)),arb(0))
    qr = sum(map(abs,qr),arb(0))
    m = s+abs(q[32])
    S = u*u+k*v*v
    d = beta*S/4
    kmax = max(arb(1),k).upper()
    # Pair A0 is the sum of both component norms. Every nonlocal primitive
    # has its zero coefficient removed and its full A0 operator norm <=1/4.
    force = (d+g*m*kmax)*p+beta*(u*(1+S)+w+u*u*v+k*w*(v*v+v*s+s*s))+qr
    zero = beta*(2+4*(1+k)*(u+v)**2)+2*beta*p*(u+k*v)/4+g*kmax*p
    oper = ((d+g*m*kmax)*4*HEAD+zero)*L
    return (force+oper+Lr).upper()
