"""Physical lag, exact zero-output removal and the near/far remainder Schur bound."""
from fractions import Fraction as Q
from functools import lru_cache
from flint import arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_collar_signed_laurent_enclosure import DEGREE,WIDTH

SPLITS=(Q(1,8),Q(1,4),Q(1,2),Q(3,4))


def power(x,p):
    # Arguments are strictly positive real radius endpoints.
    return (x.log()*exact(p)).exp()


@lru_cache(maxsize=32000)
def normalized(j,k):
    return (power(arb(4*j),Q(1,6))*power(arb(1+16*j*j),Q(2,3))/
            power(arb(1+16*k*k),Q(5,6))).upper()


def max_weight(lo,hi,h,eps):
    m=-eps*h
    if m<=0:
        if lo==hi:return normalized(lo,lo-m)
        return (power(arb(4*lo),Q(-1,6))*power(arb(1)+exact(Q(1,16*lo*lo)),Q(2,3))).upper()
    cand=[]
    left=min(hi,m-1);right=max(lo,m+1)
    if left>=lo:cand.append(normalized(left,m-left))
    if right<=hi:cand.append(normalized(right,right-m))
    return max(cand,default=arb(0))


def magnitude(a,b,single):
    if single:return abs(a).upper()
    return (abs(a).upper()**2+abs(b).upper()**2).sqrt().upper()


def error_weights(lo,hi,t):
    one=arb(1);z=(-8*exact(WIDTH*(1-t))).exp();d=one-z
    near=power(arb(4*lo),Q(-1,6))*power(one+exact(Q(1,16*lo*lo)),Q(2,3))/power(exact(t),Q(5,3))
    # finite sum or its closed geometric moment, whichever is smaller.
    limit=z**lo*(lo**3/d+3*lo**2*z/d**2+3*lo*z*(1+z)/d**3+z*(1+4*z+z*z)/d**4)
    critical=Q(3)/(8*WIDTH*(1-t))
    x=exact(min(max(critical,Q(lo)),Q(hi)))
    finite=(hi-lo+1)*x**3*(-x*8*exact(WIDTH*(1-t))).exp()
    series=min(limit.upper(),finite.upper())
    freq=64*power(one+exact(Q(1,16*lo*lo)),Q(4,3))
    # Both input signs. Summing k != 0 yields 2*4^(-10/3)*(1+3/7).
    hs2=2*freq*series*(2*power(arb(4),Q(-10,3))*exact(Q(10,7)))
    return near.upper(),hs2.upper()


def compress(rows):
    # Precompute the directed row norms once. The same signed input is used
    # on both sides of the physical Fourier shift. Data remain valid at
    # individual input labels inside these frequency-parameter boxes.
    weights={}
    for single in (True,False):
        cap=[];tail=[]
        for a,b in rows:
            cap.append([magnitude(a.coeff(h),b.coeff(h),single) for h in range(-DEGREE,DEGREE+1)])
            tail.append(magnitude(a.error,b.error,single))
        weights[single]=cap,max(tail)
    return weights


def band(weights,lo,hi,single):
    cap,err=weights[single];discrete=[]
    for i,h in enumerate(range(-DEGREE,DEGREE+1)):
        discrete.append(max((cap[0][i]*max_weight(lo,hi,h,1)).upper(),
                            (cap[1][i]*max_weight(lo,hi,h,-1)).upper()))
    split=[]
    for t in SPLITS:
        n,f=error_weights(lo,hi,t)
        split.append([(n*err).upper(),(f*err**2).upper()])
    return discrete,split


def zero():
    return [arb(0)]*(2*DEGREE+1),[[arb(0),arb(0)] for t in SPLITS]


def merge(old,new):
    a,b=old;c,d=new
    return [max(x,y) for x,y in zip(a,c)], [[max(x[0],y[0]),(x[1]+y[1]).upper()] for x,y in zip(b,d)]


def full_cost(data):
    lag,split=data
    z=(-4*exact(WIDTH)).exp()
    error=min((n*(1+z)/(1-z)+f.sqrt()).upper() for n,f in split)
    return (sum(lag,arb(0))+error).upper()
