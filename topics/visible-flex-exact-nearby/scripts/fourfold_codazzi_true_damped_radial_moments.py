"""Positive-weight propagation on the actual common drift for moment jets.

Within means the entire radial step; end is passed to the next step, so no
damping is discarded in a long march. Angular derivatives use factorial
normalization. The uncertain root occurs once in the correlated ratio h/rho0.
"""
from fractions import Fraction
from flint import arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact


def finite_positive(values):
    vals=[v.upper() for v in values]
    if not all(v.is_finite() and v>=0 for v in vals):
        raise ValueError("finite nonnegative actual angular majorants")
    return vals


def propagate(initial,source,d,slope,h,rho0,a,c):
    """rho L y+a*y=c*f. Include -m*d_phi*y_m and the full lower coupling.

    h is exact (or an actual positive interval); a,c are positive rational
    constants; d[j] encloses |partial_phi^j d/j!| on the entire piece.
    source[m] encloses the actual f_m. Return separate within and end jets.
    """
    a,c=map(Fraction,(a,c))
    if not (a>0 and c>0 and h.lower()>=0 and rho0.lower()>0 and h.is_finite() and rho0.is_finite()):
        raise ValueError("positive physical moment interval")
    y=finite_positive(initial);F=finite_positive(source);d=finite_positive(d)
    M=len(y)-1
    if M<0 or len(F)!=M+1 or len(d)<M+1:
        raise ValueError("missing physical angle derivative")
    slope=finite_positive([slope])[0]
    h_up=h.upper()
    z=exact(a)*(1+h/rho0).log()
    # Integrating factor w=exp(-z). The loss mass 1-w can equally use its
    # positive integral z*int exp(-s*z) ds as a cancellation-safe upper.
    w=(-z).exp()
    mass=min((1-w).upper(),z.upper(),arb(1))
    if mass<0:raise ValueError("positive moment mass")
    c0=exact(c/a)
    # As tau ranges over [0,h], the true homogeneous/forcing convex mix
    # lies between initial and its endpoint mixing. This elementwise hull
    # uses the same root even on the shortest original rational pieces.
    endpoint=[(w.upper()*v+mass*c0*f).upper() for v,f in zip(y,F)]
    within=[max(v,r).upper() for v,r in zip(y,endpoint)]
    def positive_exponential(b):
        out=list(b);term=list(b)
        for k in range(1,M+1):
            term=[(h_up/k*sum((j*d[m-j+1]*term[j] for j in range(1,m)),arb(0))).upper()
                  for m in range(M+1)]
            out=[(v+x).upper() for v,x in zip(out,term)]
        return [(v*(m*slope*h_up).exp()).upper() for m,v in enumerate(out)]
    return positive_exponential(within),positive_exponential(endpoint)


def direct_first(A,B,x,rho):
    """Normalized jets of A1=3(B*x-A)/(2rho); B and rho are true radial."""
    if len(A)!=len(x) or rho.lower()<=0:raise ValueError("actual positive radial coordinate")
    return [(B*y-a)*3/(2*rho) for a,y in zip(A,x)]


def tightened(signed,envelope):
    if len(signed)!=len(envelope):raise ValueError("same full moment derivative window")
    result=[]
    for z,a in zip(signed,envelope):
        box=arb(0,a.upper())
        if not z.overlaps(box):raise ValueError("independent true moment enclosures are disjoint")
        result.append(z.intersection(box))
    return result
