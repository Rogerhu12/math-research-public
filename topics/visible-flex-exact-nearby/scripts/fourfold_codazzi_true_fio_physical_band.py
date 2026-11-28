"""Directed true-phase L2/H^-k block norms with all physical output modes.

No discrete j derivative, Fourier output cutoff, or substituted approximate
phase. One amplitude component and one common true circle map per call. A
frequency tile may be a validated continuum covering infinitely many j.
"""
from math import comb
from fractions import Fraction
from flint import arb,acb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_characteristic_seed_owner import frac_power


def mul(a,b):
    n=min(len(a),len(b))
    return [sum((a[i]*b[k-i] for i in range(k+1)),a[0]*0) for k in range(n)]


def diff(a):
    return [k*a[k] for k in range(1,len(a))]


def negative_rows(amplitude,p,degree):
    """Return value and phi-derivative of every normalized half-density row."""
    if degree<0 or min(len(amplitude),len(p))<degree+2 or not p[0].lower()>0:
        raise ValueError("true positive phase slope and all required jets")
    ip=frac_power(p,Fraction(-1),exact)
    half=frac_power(p,Fraction(-1,2),exact)
    a=[amplitude]
    for k in range(degree):
        b=[mul(row,ip) for row in a]
        da=[diff(row) for row in b]
        nxt=[[-v for v in da[0]]]
        for m in range(1,k+1):
            nxt.append([x-y for x,y in zip(b[m-1],da[m])])
        a=[*nxt,b[-1]]
    rows=[]
    for m,v in enumerate(a):
        z=mul(v,half)
        scale=arb(comb(degree,m)).sqrt()
        rows.append((acb(z[0])/scale,acb(z[1])/scale))
    return rows


def norm(v):
    return sum((abs(z).upper()**2 for z in v),arb(0)).upper().sqrt().upper()


class Circle:
    """One whole frequency tile, closed angular bins of normalized widths.

    Spatial quadrature encloses signed vector means before taking a norm.
    Each cell yields one common pointwise upper of the full derivative stack.
    """
    def __init__(self,degree):
        self.degree=degree
        self.phi_mean=[acb(0) for _ in range(degree+1)]
        self.root_mean=[acb(0) for _ in range(degree+1)]
        self.slope=[]
        self.widths=[]
        self.total=Fraction(0)

    def cell(self,width,amplitude,p):
        width=Fraction(width)
        if not 0<width<=1:raise ValueError("exact normalized angular width")
        self.total+=width
        rows=negative_rows(amplitude,p,self.degree);w=exact(width)
        for m,(v,_) in enumerate(rows):
            self.phi_mean[m]+=w*v
            self.root_mean[m]+=w*v*p[0]
        self.slope.append(norm([v for _,v in rows]))
        self.widths.append(width)


def full_set(tiles):
    """The union supremum is taken inside the angular variation integral."""
    if not tiles or any(t.total!=1 or t.widths!=tiles[0].widths or
                        t.degree!=tiles[0].degree for t in tiles):
        raise ValueError("complete identical angular partition for all frequency tiles")
    variation=arb(0)
    for j,w in enumerate(tiles[0].widths):
        variation+=exact(w)*max(t.slope[j] for t in tiles)
    variation*=arb.pi()/4
    mean1=max(norm(t.phi_mean) for t in tiles)
    mean2=max(norm(t.root_mean) for t in tiles)
    return (min(mean1,mean2)+variation).upper()
