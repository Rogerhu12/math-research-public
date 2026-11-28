"""Exact first-order characteristic equation for all four true first ratios.

The entries can be scalars or normalized angular jets at ONE real point.
rho derivatives use inward orientation. No E_G quadrature or second radial
derivative occurs in either the forcing or the endpoint reconstruction.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class First:
    value: object
    inward: object
    angle: object

    def __add__(self,other):
        return First(self.value+other.value,self.inward+other.inward,self.angle+other.angle)

    def __mul__(self,other):
        return First(self.value*other.value,
                     self.inward*other.value+self.value*other.inward,
                     self.angle*other.value+self.value*other.angle)

    def scale(self,a):
        return First(self.value*a,self.inward*a,self.angle*a)

    def inverse(self):
        a=1/self.value
        return First(a,-a*a*self.inward,-a*a*self.angle)


def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]


def packet(sign,i,x,v,x_phi,v_phi,s,b,b_rho,d_phi,rho,B,B_rho,A,A1,A_phi,
           k,k1,beta_mean_S,T0,V0,theta):
    """Return (boundary correction, full source of U) with R=U+correction.

    i is the actual complex i*epsilon. B=b/sqrt(rho), k=-K/rho, A=3omega/
    (2rho^(3/2)), A1=L A, k1=partial_rho k, s=sqrt(-T). The caller certifies
    the positive gaps of b,B,k,A,p_sigma,s on the same whole physical bin.
    """
    if sign not in (-1,1):raise ValueError("actual signed ray required")
    xjet=First(x,b*v_phi-d_phi*x,x_phi)
    vjet=First(v,b*x_phi-d_phi*v,v_phi)
    sjet=First(s,b*x/(2*s*s),v/(2*s*s))
    g=(xjet*xjet+vjet*vjet,(xjet*vjet*sjet.inverse()).scale(2*i))
    # All derivatives here are first order. The regular logarithmic formula
    # retains the known cancellation of the two separate 1/(4*rho) terms.
    lg=2*beta_mean_S+A1/(6*A)-k1/(4*k)
    pg=A_phi/(6*A)
    lgplus=lg+sign*b*pg
    T=-s*s
    p=x-sign*v
    c=(-i*sign/(2*b*p**3),s/(2*b*p**3))
    gD=[v.inward+lg*v.value for v in g]
    gphi=[v.angle+pg*v.value for v in g]
    gminus=[a-sign*b*q for a,q in zip(gD,gphi)]
    corr=dot(c,gminus)
    # L_sigma p_sigma=-d_phi*p_sigma. In the second entry, s/b=A^(1/3)/B
    # cancels the singular radial factors before taking a box or derivative.
    rate0=3*d_phi-B_rho/B-1/(2*rho)
    rate1=3*d_phi-B_rho/B+(A1+sign*b*A_phi)/(3*A)
    dc=(c[0]*(rate0-lgplus),c[1]*(rate1-lgplus))
    oldtheta=(i*theta*(b/s)*T*g[1].value,i*theta*(b/s)*g[0].value)
    rest=[sign*(b_rho-b*d_phi)*gphi[j]+T0*gD[j]+V0*g[j].value+oldtheta[j]
          for j in range(2)]
    return corr,dot(c,rest)-dot(dc,gminus)
