"""Signed WUA.13 on the two exact characteristics using the wave product rule.

Slots may be directed scalars or normalized angular jets.  Every slot is at
one common physical angle.  The caller supplies one-sided OLD r derivatives.
No rough derivative of an independently fitted phase or amplitude is used.
"""
from dataclasses import dataclass
from fractions import Fraction as Q


@dataclass(frozen=True)
class Wave:
    value: object
    drift: object
    angle: object
    wave: object


def add(u,v):
    return Wave(u.value+v.value,u.drift+v.drift,u.angle+v.angle,u.wave+v.wave)


def scale(u,k):
    return Wave(u.value*k,u.drift*k,u.angle*k,u.wave*k)


def product(u,v,b2):
    return Wave(u.value*v.value,u.drift*v.value+u.value*v.drift,
                u.angle*v.value+u.value*v.angle,
                u.wave*v.value+u.value*v.wave+2*(u.drift*v.drift-b2*u.angle*v.angle))


def power(u,exponent,b2,positive_power):
    # Caller checks a genuine uniform positive gap and implements jet powers.
    z=positive_power(u.value,exponent)
    first=exponent*z/u.value
    second=(exponent-1)*first/u.value
    return Wave(z,first*u.drift,first*u.angle,
                first*u.wave+second*(u.drift*u.drift-b2*u.angle*u.angle))


def forcing(omega,v,v_phi,x,x_phi,b,b_r,d_phi,d_phiphi,drift_d_phi,
            radial_prefactor,T0,V0,theta,imaginary_epsilon,positive_power):
    """Return (F_b,F_a) and the two positive leading ray weights.

    Inputs v=omega_phi and v_phi come from the same signed gap as omega.
    x=X_phi and x_phi may be the half sums of the two genuine label jets.
    radial_prefactor is (k*/eta*)^(1/6) q^(-1/2) E_G with its first two
    outward derivatives, i.e. a Wave with zero angular derivative.
    """
    b2=b*b
    commutator=drift_d_phi+d_phi*d_phi
    first=b_r+3*b*d_phi
    om=Wave(omega,-b*x,v,-(b_r+b*d_phi)*x)
    xx=Wave(x,-b*v_phi+d_phi*x,x_phi,
            -first*v_phi-b*d_phiphi*v+commutator*x)
    vv=Wave(v,-b*x_phi+d_phi*v,v_phi,
            -first*x_phi-b*d_phiphi*x+commutator*v)
    three_half=scale(om,Q(3,2))
    s=power(three_half,Q(1,3),b2,positive_power)
    G=product(radial_prefactor,power(three_half,Q(1,6),b2,positive_power),b2)
    a=product(G,add(product(xx,xx,b2),product(vv,vv,b2)),b2)
    bw=scale(product(product(G,xx,b2),product(vv,power(s,-1,b2,positive_power),b2),b2),
             2*imaginary_epsilon)
    y=-v/s.value
    T=-s.value*s.value
    DX=-b*v
    DT=b*x/s.value
    D=(x-v)*(x+v)
    i=imaginary_epsilon
    h0=i*DX*a.value+DT*T*bw.value
    h1=DT*a.value+i*DX*bw.value
    # H inverse = (i*x I - y K_T)/(-D).
    u0=(y*T*h1-i*x*h0)/D
    u1=(y*h0-i*x*h1)/D
    mu=b2*D/(s.value*s.value)
    Fb=-(a.wave-T0*a.drift+V0*a.value-theta*u0)/mu
    Fa=-(bw.wave-T0*bw.drift+V0*bw.value-theta*u1)/mu
    return Fb,Fa,G.value*(x-v)*(x-v),G.value*(x+v)*(x+v)
