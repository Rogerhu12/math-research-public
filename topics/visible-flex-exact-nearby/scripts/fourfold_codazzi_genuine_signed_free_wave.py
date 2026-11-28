"""Complete free wave of the true first correction on an open strict piece.

Normalized inward radial jets contain normalized physical-angle jets. The
only ratio data used here are its value and angular derivatives. Both true
characteristic equations supply its needed radial derivatives with signs.
"""
from fractions import Fraction
from flint import arb,arb_series
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import check


def angle(a):
    check(a.prec>=2,"next true angular derivative")
    return arb_series([(j+1)*a[j+1] for j in range(a.prec-1)],prec=a.prec-1)


class Mixed:
    """Finite genuine mixed Taylor data. No missing derivative is zero-padded."""
    def __init__(self,rows):
        self.c=tuple(rows)
        check(self.c and all(s.prec>0 for s in self.c),"nonempty true mixed data")

    def __add__(self,o):
        if not isinstance(o,Mixed):
            return Mixed([self.c[0]+o,*self.c[1:]])
        return Mixed([a+b for a,b in zip(self.c,o.c)])
    __radd__=__add__

    def __neg__(self):
        return Mixed([-a for a in self.c])
    def __sub__(self,o):
        return self+(-o)
    def __rsub__(self,o):
        return (-self)+o

    def __mul__(self,o):
        if not isinstance(o,Mixed):
            return Mixed([a*o for a in self.c])
        return Mixed([sum(self.c[j]*o.c[k-j] for j in range(k+1))
                      for k in range(min(len(self.c),len(o.c)))])
    __rmul__=__mul__

    def power(self,s):
        s=exact(s)
        check(self.c[0][0].lower()>0,"qualified positive physical fractional power")
        out=[(self.c[0].log()*s).exp()]
        for k in range(1,len(self.c)):
            # f g' = s f' g, g=f**s, in the common angular jet algebra.
            rhs=sum(self.c[j]*out[k-j]*((s+1)*j-k) for j in range(1,k+1))
            out.append(rhs/(self.c[0]*k))
        return Mixed(out)

    def __truediv__(self,o):
        return self*o.power(-1) if isinstance(o,Mixed) else Mixed([a/o for a in self.c])
    def __rtruediv__(self,o):
        return self.power(-1)*o

    def phi(self):
        out=[]
        for a in self.c:
            if a.prec<2:break
            out.append(angle(a))
        return Mixed(out)

    def rho(self):
        return Mixed([a*j for j,a in enumerate(self.c[1:],1)])


def physical_geometry(x0,v0,omega0,d,b,orders=3):
    """Original common fixed-angle derivatives from the true hyperbolic PDE."""
    xx=[x0];vv=[v0];oo=[omega0]
    for k in range(orders):
        x=Mixed(xx);v=Mixed(vv)
        xr=(b*v.phi()-(d*x).phi()).c[k]
        vr=(b*x.phi()-(d*v).phi()).c[k]
        wr=(b*x-d*v).c[k]
        xx.append(xr/(k+1));vv.append(vr/(k+1));oo.append(wr/(k+1))
    return Mixed(xx),Mixed(vv),Mixed(oo)


def common_moment_to_physical(moments,d):
    """A_j=L^j A on the same circle; output ordinary inward A mixed derivatives."""
    fields=[[z] for z in moments]
    for k in range(len(moments)-1):
        for j in range(len(moments)-k-1):
            drift=(d*Mixed(fields[j]).phi()).c[k]
            fields[j].append((fields[j+1][k]-drift)/(k+1))
    return Mixed(fields[0])


def radial_gauge(rate,order,angular_count):
    # At the base radius use E/E(base)=1. Its complete local derivatives
    # are retained before factoring the common scalar E(base) out.
    E=[arb_series([arb(1)],prec=angular_count)]
    for j in range(order):
        E.append((rate*Mixed(E)).c[j]/(j+1))
    return Mixed(E)


def advect(f,velocity):
    return f.rho()+velocity*f.phi()


def wave(f,d,b):
    return advect(advect(f,d),d)-b*b*f.phi().phi()


def rows(x,v,omega,A,k,d,b,beta_mean_S,T0,V0,theta,rplus,rminus,angular_order):
    """Return (imag a, real b) of A0(w1)/E(base) on epsilon=+.

    The signed full first ratios r_sigma=R_sigma/i at epsilon=+ and their
    fixed-physical-angle normalized jets enter in their original order.
    E(base) includes the constant (k_star/eta_star)**(1/6). The opposite
    carrier has the corresponding conjugate real structure on the real slice.
    """
    check(angular_order>=0 and min(rplus.prec,rminus.prec)>=angular_order+2,
          "true first ratios and one additional angular derivative")
    E=radial_gauge(2*beta_mean_S,3,angular_order+4)
    G=E*A.power(Fraction(1,6))*k.power(Fraction(-1,4))
    s=(omega*exact(Fraction(3,2))).power(Fraction(1,3))
    T=-s*s;Q=b/s
    a=G*(x*x+v*v);w=2*G*x*v/s
    fa=wave(a,d,b)+T0*advect(a,d)+V0*a-theta*Q*T*w
    fb=wave(w,d,b)+T0*advect(w,d)+V0*w+theta*Q*a
    bdot=b.rho()-b*d.phi()
    aw=bw=None
    for sign,r in ((1,rplus),(-1,rminus)):
        p=x-sign*v
        F=(-sign*fa+s*fb)/(2*b*G*p*p*p)
        F0=F.c[0]
        # char(F) here acts on the *opposite* true branch.
        Fm=advect(F,d-sign*b).c[0]
        rp=angle(r)
        def scalar(M):
            value=M.c[0]*r
            L=advect(M,d).c[0]*r+M.c[0]*(F0-sign*b.c[0]*rp)
            W=(wave(M,d,b).c[0]*r+M.c[0]*(Fm-sign*bdot.c[0]*rp)
               +advect(M,d-sign*b).c[0]*F0
               +advect(M,d+sign*b).c[0]*(F0-2*sign*b.c[0]*rp))
            return value,W+T0.c[0]*L+V0.c[0]*value
        M=G*p*p/2
        aa,s1=scalar(M)
        cc,s2=scalar(sign*M/s)
        f=s1+(theta*Q*T).c[0]*cc
        g=s2-(theta*Q).c[0]*aa
        aw=f if aw is None else aw+f
        bw=g if bw is None else bw+g
    check(min(aw.prec,bw.prec)>angular_order,"all complete free wave output jets")
    return ([aw[j] for j in range(angular_order+1)],
            [bw[j] for j in range(angular_order+1)])
