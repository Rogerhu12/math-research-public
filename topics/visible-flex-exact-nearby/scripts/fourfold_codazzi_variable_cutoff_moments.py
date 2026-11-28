"""Whole signed partial cutoff moments and their derivatives on physical T, complex amplitude parameter."""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb,factorial
from flint import arb,acb
import fourfold_codazzi_common_radial_potential_budget as P
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_signed_density_transport_arithmetic import exact

L=Q(1,2000)
RADIUS=Q(7,10000)
M=32
NORMAL=Q(factorial(129),2**129*factorial(64)**2)


@lru_cache(maxsize=8192)
def partial_beta(x):
    """x rational in [1/2,1]. Lower normalized moments of Y through order 31."""
    a=4*x-3;t=(1+a)/2
    mass=sum((comb(129,j)*t**j*(1-t)**(129-j) for j in range(65,130)),Q(0))
    wall=NORMAL*(1-a*a)**65;out=[mass,-wall/130]
    for i in range(2,M):out.append(((i-1)*out[i-2]-a**(i-1)*wall)/(i+129))
    return out


@lru_cache(maxsize=32768)
def partial_moment(x,k):
    """I_k(x)=int_0^1 t^(2k) chi(-Lxt^2)dt. The shape is decreasing."""
    if x<=Q(1,2):return exact(Q(1,2*k+1))
    check(x<=1,'complete variable cutoff support')
    j=Q(2*k+1,2);a=partial_beta(x);v=Q(0);c=Q(1)
    for h in range(M):
        v+=c*a[h]
        c*=Q(j-h,3*(h+1))
    ratio=Q(3,4*x);amp=exact(ratio**k)*exact(ratio).sqrt()
    summ=exact(v)+arb(0,exact(abs(c)*Q(3,2)).upper())
    z=(exact(1-a[0])+amp*summ)/(2*k+1)
    return z.intersection(arb(0).union(exact(Q(1,2*k+1))))


def coefficients(c,z):
    """All 13 coefficients of V(z,-Lx) for one actual transverse complex sector."""
    count=15
    plain={key:[p.scalar_value() for p in c[key][:count]] for key in ('K','beta','gamma','s','eta','k','a')}
    check(plain['K'][0]==0 and all(len(row)==count for row in plain.values()),'entire unchanged physical root germ')
    data={'intrinsic':plain,'eta':plain['eta']}
    for k in ('u','v'):data[k]={j:[p.coefficient(j) for p in c[k][:count]] for j in range(-96,97)}
    fields=P.full_frequency_fields(data,z,count)
    abar=[a*P.ex(Q(3,2*i+3)) for i,a in enumerate(plain['a'])]
    rr=lambda row:[-v for v in P.jdr(row)]
    def logd(row):return P.jdiv(rr(row),row,count-1)
    er=logd(plain['eta']);kr=logd(plain['k']);ar=logd(abar)
    zr=logd(P.jadd(P.jconst(1,count),fields['theta'],count))
    cc=[kr[i]/4-ar[i]/6-fields['D'][i]/2-zr[i]/2 for i in range(count-1)]
    ell=[2*er[i]+kr[i]/2-ar[i]/3+fields['D'][i]+zr[i] for i in range(count-1)]
    n=count-2
    cross=P.jmul(cc,ell,n);aa=fields['alpha']
    freq=P.jadd(P.jscale(P.jmul(plain['eta'],aa,n),2),P.jscale(P.jmul(aa,aa,n),z),n)
    kfreq=P.jmul(plain['K'],freq,n)
    W=[-v+cross[i]/2-16*kfreq[i] for i,v in enumerate(rr(cc))]
    kappa=P.jmul(plain['a'],P.jpow(abar,Q(-1,3),n),n)
    pot=P.jdiv(W,P.jmul(kappa,kappa,n),n)
    # Positive rho gives x=-T/L; the signed triangular reversion stays complex.
    xt=[acb(0)]+[w/P.ex(L) for w in P.jpow(abar,Q(2,3),n-1)]
    powers=[P.jconst(1,n)]
    for _ in range(1,n):powers.append(P.jmul(powers[-1],xt,n))
    out=[]
    for k,pk in enumerate(pot):
        out.append((pk-sum((out[j]*powers[j][k] for j in range(k)),acb(0)))/powers[k][k])
    return out


def cutoff(lo,hi):
    """True normalized x derivatives to order three, on one complete real subinterval."""
    if hi<=Q(1,2):return [arb(1),arb(0),arb(0),arb(0)]
    check(lo>=Q(1,2) and hi<=1,'cutoff polynomial on its own complete region')
    y=exact(4*lo-3).union(exact(4*hi-3))
    small=0 if lo<=Q(3,4)<=hi else min(abs(4*lo-3),abs(4*hi-3))
    large=max(abs(4*lo-3),abs(4*hi-3))
    def p(k):return exact((1-large**2)**k).union(exact((1-small**2)**k))
    den=exact(NORMAL)
    value=exact(1-partial_beta(hi)[0]).union(exact(1-partial_beta(lo)[0]))
    # Derivatives of -4c(1-y²)^64, divided by each Taylor factorial.
    return [value,-4*den*p(64),1024*den*y*p(63),
            exact(Q(4096,3))*den*(p(63)-126*y*y*p(62))]


def tail(x,j,average=False):
    """Complete normalized coefficient tail, using the genuine V_TT bound."""
    K=13;rat=L/RADIUS
    # Terms at k=13 use |d_k|<=M2 L² (L/R)^(k-2)/(k(k-1)).
    top=Q(3830956)*L**2*rat**(K-2)*comb(K,j)*x**(K-j)/(K*(K-1))
    # For j<=4, ratios (k-1)/(k+1-j) are monotone toward one if >1.
    q=x*rat*max(Q(1),Q(K-1,K+1-j))
    check(q<1,'all further original complex Taylor derivatives')
    return exact(top/(1-q)/(2*K+1 if average else 1)).upper()


def derivative(coeff,lo,hi,j,average=False):
    x=exact(lo).union(exact(hi));p=acb(0)
    for k in range(len(coeff)-1,j-1,-1):
        p=p*x+coeff[k]*comb(k,j)/(2*k+1 if average else 1)
    rad=arb(0,tail(hi,j,average))
    return p+acb(rad,rad)


def packet(coeff,lo,hi):
    check(0<=lo<hi<=1 and len(coeff)==13,'whole true negative radial potential cell')
    chk=cutoff(lo,hi);v=[derivative(coeff,lo,hi,j) for j in range(4)]
    ext=[sum((v[k]*chk[j-k] for k in range(j+1)),acb(0)) for j in range(4)]
    if hi<=Q(1,2):
        return ext,[derivative(coeff,lo,hi,j,True) for j in range(5)]
    x=exact(lo).union(exact(hi));p=arb(1);value=acb(0)
    for k,c in enumerate(coeff):
        box=partial_moment(hi,k).union(partial_moment(lo,k))
        value+=c*p*box;p*=x
    # Pointwise bound of every neglected power followed by the actual t integral.
    rad=arb(0,tail(hi,0,True));out=[value+acb(rad,rad)]
    for j in range(4):
        out.append((ext[j]-(2*j+1)*out[j])/(2*(j+1)*x))
    check(all(a.is_finite() for a in ext+out),'complete true potential and averaged cutoff jets')
    return ext,out
