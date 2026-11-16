"""Fixed original CM input and triangular elliptic germ for public Actions."""
import os
import math
from sage.all import QQ, PolynomialRing, NumberField, GF

def original_first_differential(precision):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution is restricted to the public Actions.")
    QT = PolynomialRing(QQ,"T")
    T = QT.gen()
    K = NumberField(T**2+T+1,"omega")
    omega = K.gen()
    alpha = -1+2*omega
    c = -1-19*omega
    KV = PolynomialRing(K,"V")
    V = KV.gen()
    L = K.extension(V**3+367395*V**2+147*V+K(QQ(1)/17),"vL")
    vL = L.gen()
    ell = ((21905009-23122022*omega)
           +(112353990182+54575060764*omega)*vL
           +(305813+148546*omega)*vL**2)/25505280
    tau_v = alpha**3*vL/ell**3
    def tau(z):
        co = L(z).list()
        return sum((L(co[i])*tau_v**i for i in range(len(co))), L.zero())
    assert tau(tau(tau_v)) == vL
    assert ell*tau(ell)*tau(tau(ell)) == c
    u1,u2 = tau(tau(ell)),L(c)/ell
    FF = PolynomialRing(GF(17),"W")
    W = FF.gen()
    F289 = GF(17**2,name="omega17",modulus=W**2+W+1)
    omega17 = F289.gen()
    alpha17 = -1+2*omega17
    dlog = {}
    z = F289.one()
    for r in range(288):
        assert z not in dlog
        dlog[z] = r%9
        z *= alpha17
    assert z == 1 and len(dlog) == 288
    fcoeff = [[K.zero(),K.zero(),K.zero()] for _ in range(precision+1)]
    bound = math.isqrt((4*precision)//3)+2
    ideal_count = 0
    for A in range(-bound,bound+1):
        for B in range(-bound,bound+1):
            nm = A*A-A*B+B*B
            if nm < 1 or nm > precision:
                continue
            orbit = [(A,B),(-B,A-B),(B-A,-A)]
            orbit += [(-aa,-bb) for aa,bb in orbit]
            if (A,B) != min(orbit):
                continue
            if (A+B)%3 == 0 or (A%17 == 0 and B%17 == 0):
                continue
            eps = 1 if (A+B)%3 == 1 else -1
            r = dlog[F289(A)+F289(B)*omega17]
            fcoeff[nm][r%3] += eps*(A+B*omega)*c**(r//3)/alpha**r
            ideal_count += 1
    F = NumberField(T**3-17,"a17")
    a = F.gen()
    v = -122465-47628*a-F(QQ(314892)/17)*a**2
    assert v**3+367395*v**2+147*v+F(QQ(1)/17) == 0
    H0 = []
    for f0,f1,f2 in fcoeff:
        z = L(f0)+u1*f1+u2*f2
        co = z.list()
        realco = []
        for ci in co:
            cc = K(ci).list()
            assert len(cc) <= 1 or cc[1] == 0
            realco.append(QQ(cc[0]) if cc else QQ(0))
        H0.append(sum((F(ci)*v**i for i,ci in enumerate(realco)),F.zero()))
    assert H0[1] == 1 and H0[4] == -2
    assert all(z == 0 for i,z in enumerate(H0) if i%3 != 1)
    return F,v,H0,ideal_count

def original_y_germ(field,v,f,n,maximum):
    """Return coefficients Y_{j-1}, 0<=j<=maximum, in exact arithmetic."""
    n = field(n)
    t = n**3*v
    e,e2,e3,r = [field.one()],[field.one()],[field.one()],[field.one()]
    for m in range(1,maximum+1):
        rm = (-4*t*e3[m-1]
              -sum((r[i]*r[m-i] for i in range(1,m)),field.zero()))/2
        r.append(rm)
        em = sum((f[i]*r[m-i] for i in range(m+1)),field.zero())/field(3*m+1)
        e.append(em)
        e2.append(sum((e[i]*e[m-i] for i in range(m+1)),field.zero()))
        e3.append(sum((e2[i]*e[m-i] for i in range(m+1)),field.zero()))
    inverse = [field.one()]
    for m in range(1,maximum+1):
        inverse.append(-sum((e3[i]*inverse[m-i] for i in range(1,m+1)),field.zero()))
    y = []
    for m in range(maximum+1):
        z = 2*inverse[m]+sum((r[i]*inverse[m-i] for i in range(1,m+1)),field.zero())
        y.append(-z/(2*n**3))
    assert y[0] == -1/n**3
    assert y[1] == -(v+3/n**3)/2
    return y
