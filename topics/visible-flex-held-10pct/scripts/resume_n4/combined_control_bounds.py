"""A cancellation-aware bound for one complete complementary control.

The underlying canonical functions, coefficient intervals and rho floor are
unchanged. Combine the trigonometric coefficients first; use the original
rational coefficient enclosures plus an explicit dot-product roundoff budget.
This only sharpens a sufficient derivative bound for the actual same core.
"""
from fractions import Fraction as F
import math,numpy as np


def bounds(basis,c,homotopy):
    c=np.asarray(c,float);M=basis.M
    if c.shape!=(M-1,):raise ValueError('Wrong complete coefficient vector')
    if not hasattr(basis,'_combined_coefficient_errors'):
        Herror=np.empty_like(basis.H)
        for j,row in enumerate(basis.certificate['coefficients']):
            for k,interval in enumerate(row):
                err=max(abs(F.from_float(float(basis.H[j,k]))-v)for v in interval)
                Herror[j,k]=math.nextafter(float(err),math.inf)
        basis._combined_coefficient_errors=Herror
    ld=np.longdouble;cc=c.astype(ld);H=basis.H.astype(ld)
    coef=cc@H;absolute_products=np.abs(cc)@np.abs(H)
    nops=4*M+16;eps=np.finfo(ld).eps;gamma=ld(nops)*eps/(1-ld(nops)*eps)
    error=np.abs(cc)@basis._combined_coefficient_errors.astype(ld)+gamma*absolute_products
    high=np.nextafter(np.abs(coef)+error,np.inf)
    freq=basis.freq.astype(ld);trig=[]
    for r in range(4):
        weight=np.ones_like(freq)if r==0 else freq**r
        trig.append(np.nextafter(np.sum(high*weight)*(1+gamma),np.inf))
    D=[]
    cut=basis.cutoff_bounds.astype(ld)
    for r in range(4):D.append(sum(math.comb(r,j)*cut[j]*trig[r-j]for j in range(r+1))*(1+gamma))
    compact=np.array([D[0]+D[2],D[1]+D[3]],dtype=ld)
    leak=cc@basis.fundamental_leakage.astype(ld)
    leakerr=np.abs(cc)@basis.fundamental_evaluation_error.astype(ld)+gamma*(np.abs(cc)@np.abs(basis.fundamental_leakage.astype(ld)))
    leakabs=np.abs(leak)+leakerr
    m=basis.target_freq.astype(ld);low=np.array([
       np.sum(np.abs(cc)*(m*m-1))+leakabs*(basis.n**2-1),
       np.sum(np.abs(cc)*m*(m*m-1))+leakabs*basis.n*(basis.n**2-1)],dtype=ld)*(1+gamma)
    result=ld(homotopy)*compact+(1-ld(homotopy))*low
    return tuple(math.nextafter(float(v*(1+gamma)),math.inf)for v in result)
